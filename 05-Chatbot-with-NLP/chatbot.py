
from pathlib import Path
import json
import random
import re

import joblib
from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


# STEP 1: File paths
project_dir = Path(__file__).resolve().parent
intents_path = project_dir / "intents.json"
models_dir = project_dir / "models"
outputs_dir = project_dir / "outputs"

models_dir.mkdir(exist_ok=True)
outputs_dir.mkdir(exist_ok=True)

model_path = models_dir / "chatbot_model.joblib"

stemmer = PorterStemmer()


# STEP 2: Text preprocessing using NLTK
def preprocess_text(text):
    tokens = wordpunct_tokenize(text.lower())

    cleaned_tokens = [
        stemmer.stem(token)
        for token in tokens
        if re.fullmatch(r"[a-z]+", token)
    ]

    return " ".join(cleaned_tokens)


# STEP 3: Load intents dataset
print("Loading chatbot training data...")

with open(intents_path, "r", encoding="utf-8") as file:
    data = json.load(file)

patterns = []
labels = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]
    responses[tag] = intent["responses"]

    for pattern in intent["patterns"]:
        patterns.append(pattern)
        labels.append(tag)

print("Training examples:", len(patterns))
print("Number of intents:", len(responses))


# STEP 4: Prepare the dataset
processed_patterns = [
    preprocess_text(pattern) for pattern in patterns
]

X_train, X_test, y_train, y_test = train_test_split(
    processed_patterns,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)


# STEP 5: Build chatbot model
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
        ),
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            random_state=42,
        ),
    ),
])

print("\nTraining chatbot...")
model.fit(X_train, y_train)

print("Chatbot trained successfully!")


# STEP 6: Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

report = classification_report(
    y_test,
    predictions,
    zero_division=0,
)

print("\n--- MODEL EVALUATION ---")
print(f"Accuracy: {accuracy * 100:.2f}%")
print(report)

report_path = outputs_dir / "classification_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(f"Accuracy: {accuracy * 100:.2f}%\n\n")
    file.write(report)

print("Saved: classification_report.txt")


# STEP 7: Train on all available examples
# The held-out test set was used only for evaluation.
model.fit(processed_patterns, labels)

joblib.dump(model, model_path)
print("Saved chatbot model:", model_path)


# STEP 8: Generate chatbot responses
def chatbot_response(user_text):
    processed_text = preprocess_text(user_text)

    if not processed_text:
        return "Please enter a question containing words."

    probabilities = model.predict_proba([processed_text])[0]

    best_index = probabilities.argmax()
    confidence = probabilities[best_index]

    predicted_tag = model.classes_[best_index]

    if confidence < 0.30:
        return (
            "I'm not sure about that. "
            "Try asking me about Python, AI, ML, or NLP."
        )

    return random.choice(responses[predicted_tag])


# STEP 9: Interactive chatbot
print("\n--- CHATBOT IS READY ---")
print("Ask me about Python, AI, ML, or NLP.")
print("Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    if not user_input:
        print("Bot: Please enter a message.")
        continue

    answer = chatbot_response(user_input)
    print("Bot:", answer)
