
from pathlib import Path

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# STEP 1: Load the dataset
project_dir = Path(__file__).resolve().parent
dataset_path = project_dir / "SMSSpamCollection.tsv"

df = pd.read_csv(
    dataset_path,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

print("Dataset loaded successfully!")
print("Total messages:", len(df))
print(df["label"].value_counts())

# STEP 2: Prepare input and output
X = df["message"]
y = df["label"]

# STEP 3: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# STEP 4: Create machine learning model
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", MultinomialNB())
])

# STEP 5: Train model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# STEP 6: Evaluate model
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=["ham", "spam"]))

# STEP 7: Save trained model
model_path = project_dir / "spam_model.joblib"
joblib.dump(model, model_path)

print("\nModel saved successfully!")

# STEP 8: Predict custom messages
while True:
    message = input("\nEnter a message (or type 'exit'): ").strip()

    if message.lower() == "exit":
        print("Goodbye!")
        break

    if not message:
        print("Please enter a message.")
        continue

    prediction = model.predict([message])[0]

    if prediction == "spam":
        print("Prediction: SPAM")
    else:
        print("Prediction: NOT SPAM (HAM)")
