
from pathlib import Path
from collections import Counter
import math
import re


# STEP 1: Set up file paths
project_dir = Path(__file__).resolve().parent
data_path = project_dir / "data" / "training_text.txt"
outputs_dir = project_dir / "outputs"

outputs_dir.mkdir(parents=True, exist_ok=True)

alphabet = "abcdefghijklmnopqrstuvwxyz"


# STEP 2: Load the training dataset
print("Loading text dataset...")

with open(data_path, "r", encoding="utf-8") as file:
    training_text = file.read().lower()

print("Dataset loaded successfully!")


# STEP 3: Tokenize the training text
def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())


lines = training_text.splitlines()

sentences = [
    tokenize(line)
    for line in lines
    if tokenize(line)
]

words = [
    word
    for sentence in sentences
    for word in sentence
]

print("\nTotal words:", len(words))


# STEP 4: Build unigram frequency model
unigram_counts = Counter(words)

print("Unique words:", len(unigram_counts))


# STEP 5: Build bigram frequency model
bigram_counts = Counter()

for sentence in sentences:
    previous_word = "<START>"

    for word in sentence:
        bigram_counts[(previous_word, word)] += 1
        previous_word = word

print("Unique bigrams:", len(bigram_counts))

vocabulary = set(unigram_counts)
total_words = sum(unigram_counts.values())


# STEP 6: Generate one-edit spelling candidates
def edits_one(word):
    splits = [
        (word[:i], word[i:])
        for i in range(len(word) + 1)
    ]

    deletes = [
        left + right[1:]
        for left, right in splits
        if right
    ]

    transposes = [
        left + right[1] + right[0] + right[2:]
        for left, right in splits
        if len(right) > 1
    ]

    replaces = [
        left + char + right[1:]
        for left, right in splits
        if right
        for char in alphabet
    ]

    inserts = [
        left + char + right
        for left, right in splits
        for char in alphabet
    ]

    return set(
        deletes + transposes + replaces + inserts
    )


# STEP 7: Find known candidate words
def get_candidates(word):
    if word in vocabulary:
        return {word}

    one_edit = edits_one(word)
    known_one_edit = one_edit & vocabulary

    if known_one_edit:
        return known_one_edit

    # Try two edits only if no known one-edit
    # correction exists.
    known_two_edits = set()

    if len(word) <= 15:
        for candidate in one_edit:
            known_two_edits.update(
                edits_one(candidate) & vocabulary
            )

    if known_two_edits:
        return known_two_edits

    return {word}


# STEP 8: Calculate unigram and bigram scores
def unigram_probability(word):
    return (
        (unigram_counts[word] + 1)
        / (total_words + len(vocabulary) + 1)
    )


def bigram_probability(previous_word, word):
    bigram_frequency = bigram_counts[
        (previous_word, word)
    ]

    if previous_word == "<START>":
        previous_count = len(sentences)
    else:
        previous_count = unigram_counts[previous_word]

    return (
        (bigram_frequency + 1)
        / (previous_count + len(vocabulary) + 1)
    )


# STEP 9: Choose the best spelling
def correct_word(word, previous_word="<START>"):
    word = word.lower()

    # Preserve words already in our vocabulary.
    if word in vocabulary:
        return word

    candidates = get_candidates(word)

    if candidates == {word}:
        return word

    def score(candidate):
        unigram_score = math.log(
            unigram_probability(candidate)
        )

        bigram_score = math.log(
            bigram_probability(previous_word, candidate)
        )

        # Combine word frequency with context.
        return unigram_score + 2 * bigram_score

    return max(
        sorted(candidates),
        key=score
    )


# STEP 10: Correct an entire sentence
def correct_sentence(text):
    previous_word = "<START>"

    def replace_word(match):
        nonlocal previous_word

        original_word = match.group(0)

        corrected = correct_word(
            original_word,
            previous_word
        )

        previous_word = corrected

        # Preserve simple capitalization.
        if original_word.isupper():
            return corrected.upper()

        if original_word.istitle():
            return corrected.capitalize()

        return corrected

    return re.sub(
        r"[A-Za-z]+",
        replace_word,
        text
    )


# STEP 11: Interactive autocorrector
print("\n--- TEXT AUTOCORRECTOR READY ---")
print("Enter a sentence to correct.")
print("Type 'exit' to stop.")

history = []

while True:
    user_text = input("\nEnter text: ").strip()

    if user_text.lower() == "exit":
        print("\nAutocorrector closed successfully!")
        break

    if not user_text:
        print("Please enter some text.")
        continue

    corrected_text = correct_sentence(user_text)

    print("Original :", user_text)
    print("Corrected:", corrected_text)

    history.append(
        (user_text, corrected_text)
    )


# STEP 12: Save the results
output_path = outputs_dir / "correction_history.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write("TEXT AUTOCORRECTOR RESULTS\n")
    file.write("=" * 40 + "\n\n")

    for original, corrected in history:
        file.write(f"Original : {original}\n")
        file.write(f"Corrected: {corrected}\n\n")

print("Results saved to:", output_path)
