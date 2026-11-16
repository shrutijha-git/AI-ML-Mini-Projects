
from pathlib import Path
import re

import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


# STEP 1: File paths
project_dir = Path(__file__).resolve().parent
data_path = project_dir / "data" / "labeled_data.csv"
models_dir = project_dir / "models"
outputs_dir = project_dir / "outputs"

models_dir.mkdir(exist_ok=True)
outputs_dir.mkdir(exist_ok=True)

model_path = models_dir / "hate_speech_model.joblib"

label_names = {
    0: "Hate Speech",
    1: "Offensive Language",
    2: "Neither",
}


# STEP 2: Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = re.sub(r"[^a-z\s#]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# STEP 3: Load dataset
print("Loading hate speech dataset...")

df = pd.read_csv(data_path)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

required_columns = {"tweet", "class"}

if not required_columns.issubset(df.columns):
    raise ValueError(
        "Dataset must contain 'tweet' and 'class' columns."
    )

print("\nMissing values:")
print(df[["tweet", "class"]].isnull().sum())

df = df.dropna(subset=["tweet", "class"]).copy()
df = df[df["class"].isin(label_names)].copy()

# Avoid training and testing on identical tweet text.
df["cleaned_text"] = df["tweet"].apply(clean_text)
df = df[df["cleaned_text"].str.len() > 0]
df = df.drop_duplicates(subset=["cleaned_text"])

print("\nRecords after cleaning:", len(df))

print("\nClass distribution:")
print(df["class"].map(label_names).value_counts())


# STEP 4: Split dataset
X = df["cleaned_text"]
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# STEP 5: Build NLP model
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            max_features=20000,
            ngram_range=(1, 2),
            min_df=2,
            sublinear_tf=True,
        ),
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        ),
    ),
])

print("\nTraining the model...")
model.fit(X_train, y_train)

print("Model trained successfully!")


# STEP 6: Evaluate model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n--- MODEL EVALUATION ---")
print(f"Accuracy: {accuracy * 100:.2f}%")

report = classification_report(
    y_test,
    predictions,
    labels=[0, 1, 2],
    target_names=[
        "Hate Speech",
        "Offensive Language",
        "Neither",
    ],
    zero_division=0,
)

print("\nClassification Report:")
print(report)

report_path = outputs_dir / "classification_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(f"Accuracy: {accuracy * 100:.2f}%\n\n")
    file.write(report)

print("Saved: classification_report.txt")


# STEP 7: Create confusion matrix
matrix = confusion_matrix(
    y_test,
    predictions,
    labels=[0, 1, 2],
)

plt.figure(figsize=(9, 7))

sns.heatmap(
    matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=list(label_names.values()),
    yticklabels=list(label_names.values()),
)

plt.title("Hate Speech Detection - Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()

plt.savefig(
    outputs_dir / "confusion_matrix.png",
    dpi=300,
)
plt.close()

print("Saved: confusion_matrix.png")


# STEP 8: Save trained model
joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Saved to:", model_path)


# STEP 9: Interactive prediction
print("\n--- TEST YOUR MODEL ---")
print("Enter a sentence to classify.")
print("Type 'exit' to stop.")

while True:
    user_text = input("\nEnter text: ").strip()

    if user_text.lower() == "exit":
        print("Program closed successfully!")
        break

    if not user_text:
        print("Please enter some text.")
        continue

    cleaned = clean_text(user_text)

    if not cleaned:
        print("Please enter text containing words.")
        continue

    prediction = int(model.predict([cleaned])[0])

    print("Predicted category:", label_names[prediction])
    print(
        "Note: Predictions can be wrong and should not "
        "be treated as definitive moderation decisions."
    )
