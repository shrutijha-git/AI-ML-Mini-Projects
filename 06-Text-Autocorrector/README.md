# Project 6 — Text Autocorrector Using N-grams

## Project Overview

This project implements a text autocorrector using Python and Natural Language Processing (NLP). It identifies potentially misspelled words and suggests corrections using word frequencies, edit operations, and N-gram language modeling.

The autocorrector uses **unigrams** to measure individual word frequencies and **bigrams** to evaluate how well a suggested word fits the preceding word. It generates spelling candidates through character insertion, deletion, replacement, and transposition, then selects a candidate using a combined statistical score.

The project is designed to demonstrate how traditional statistical NLP techniques can be used for spelling correction without training a deep learning model.

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Unigram and Bigram Language Models
- Edit Distance Concepts
- Python Standard Library: `collections`, `re`, `math`, `pathlib`

No external Python packages are required.

## Project Folder Structure

```text
06-Text-Autocorrector/
│
├── autocorrect.py
├── requirements.txt
├── README.md
│
├── data/
│   └── training_text.txt
│
└── outputs/
    └── correction_history.txt
```

## Dataset

The project uses a small, custom-created text dataset stored in `data/training_text.txt`.

It contains sentences related to Python, programming, artificial intelligence, machine learning, data science, and natural language processing.

The dataset is used to calculate unigram and bigram frequencies.

No external dataset download is required.

## How the Autocorrector Works

### 1. Text Preprocessing

The training text is converted to lowercase and tokenized into words using regular expressions.

### 2. Unigram Model

A unigram model counts how often each word occurs in the training dataset.

More frequent words generally receive higher unigram probabilities.

### 3. Bigram Model

A bigram model counts pairs of consecutive words.

It estimates how likely a candidate word is to appear after the preceding word.

### 4. Candidate Generation

The program generates possible corrections using:

- Deletion of a character
- Insertion of a character
- Replacement of a character
- Transposition of adjacent characters

It first searches for known words one edit away. If none are found, it searches for candidates two edits away.

### 5. Correction Scoring

The program combines unigram probability and bigram probability:

**Score = log(P(candidate)) + 2 × log(P(candidate | previous word))**

The highest-scoring candidate is selected.

### 6. Sentence Correction

The program processes a complete sentence, corrects words when possible, and preserves basic capitalization and punctuation.

### 7. Saving Results

After the user exits, the program saves the original and corrected sentences to `outputs/correction_history.txt`.

## Example Input

```text
i love programing in pythn
```

## Intended Output

```text
i love programming in python
```

Actual results may vary depending on the training corpus and candidate scores.

## How to Run

### 1. Open the project folder

```powershell
cd 06-Text-Autocorrector
```

### 2. Run the Python program

```powershell
python autocorrect.py
```

### 3. Enter text

Type a sentence containing spelling mistakes.

### 4. Exit

Type:

```text
exit
```

The correction history will be saved automatically.

## Limitations

- The training dataset is small and focused on programming topics.
- Unknown words may remain unchanged.
- Correctly spelled words are not changed, even when they are contextually incorrect.
- The bigram model considers only the preceding word.
- Some candidate corrections may be inappropriate.
- The program is not a general-purpose grammar checker.
- It does not use a learned model of typing errors.

## Future Improvements

- Train using a larger text corpus.
- Use trigram language modeling.
- Improve candidate ranking using edit probabilities.
- Support more vocabulary and technical terminology.
- Handle real-word spelling errors.
- Build a graphical interface or web application.

## Learning Outcomes

Through this project, I learned:

- How unigrams and bigrams work.
- How word frequencies are calculated.
- How spelling correction candidates are generated.
- How context improves correction ranking.
- How statistical NLP methods can be implemented using Python.
- How to save autocorrection results to a file.

## Project Status

**Completed — Project 6 of 9 in the AI/ML Mini Projects portfolio.**
