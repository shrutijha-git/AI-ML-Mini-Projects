
from pathlib import Path

import torch
from transformers import MarianMTModel, MarianTokenizer


# STEP 1: Project paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "sample_sentences.txt"
OUTPUTS_DIR = PROJECT_DIR / "outputs"

OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

HISTORY_PATH = OUTPUTS_DIR / "translation_history.txt"

# Pretrained English-to-French translation model
MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"


# STEP 2: Load pretrained model and tokenizer
print("Loading English-to-French translation model...")
print("The first run may download model files.")

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

model.to(device)
model.eval()

print("\nModel loaded successfully!")
print("Running on:", device)


# STEP 3: Translation function
def translate_text(text):
    encoded = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=256,
    )

    encoded = {
        key: value.to(device)
        for key, value in encoded.items()
    }

    with torch.no_grad():
        translated_tokens = model.generate(
            **encoded,
            max_new_tokens=256,
            num_beams=4,
            early_stopping=True,
        )

    translated_text = tokenizer.decode(
        translated_tokens[0],
        skip_special_tokens=True,
    )

    return translated_text


# STEP 4: Translate sample sentences
print("\n--- SAMPLE TRANSLATIONS ---")

history = []

if DATA_PATH.exists():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        sample_sentences = [
            line.strip()
            for line in file
            if line.strip()
        ]

    for sentence in sample_sentences:
        french = translate_text(sentence)

        print("\nEnglish:", sentence)
        print("French :", french)

        history.append((sentence, french))


# STEP 5: Interactive translator
print("\n--- LANGUAGE TRANSLATOR READY ---")
print("Translate English text into French.")
print("Type 'exit' to stop.")

while True:
    user_text = input("\nEnter English text: ").strip()

    if user_text.lower() in {"exit", "quit"}:
        print("\nTranslator closed successfully!")
        break

    if not user_text:
        print("Please enter some English text.")
        continue

    french_translation = translate_text(user_text)

    print("English:", user_text)
    print("French :", french_translation)

    history.append((user_text, french_translation))


# STEP 6: Save translation history
with open(HISTORY_PATH, "w", encoding="utf-8") as file:
    file.write("ENGLISH TO FRENCH TRANSLATION RESULTS\n")
    file.write("=" * 45 + "\n\n")

    for english, french in history:
        file.write(f"English: {english}\n")
        file.write(f"French : {french}\n\n")

print("\nTranslation history saved to:")
print(HISTORY_PATH)
