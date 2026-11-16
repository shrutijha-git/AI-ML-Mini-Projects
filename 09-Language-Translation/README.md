# Project 9 — Language Translation Using Transformers

## Project Overview

This project implements an English-to-French language translator using a pretrained Transformer-based neural network. It uses the Hugging Face Transformers library and the Helsinki-NLP MarianMT translation model.

The program loads a pretrained tokenizer and model, converts English text into model-compatible tokens, generates translated French tokens, and decodes them into readable text. The model is used for inference only; no additional model training or fine-tuning is performed.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- MarianMT
- SentencePiece
- Sacremoses

## Model

**Model:** `Helsinki-NLP/opus-mt-en-fr`

**Source:** https://huggingface.co/Helsinki-NLP/opus-mt-en-fr

**Task:** English-to-French machine translation

The model is pretrained and automatically downloaded during the first execution.

## Project Structure

```text
09-Language-Translation/
├── translator.py
├── requirements.txt
├── README.md
├── data/
│   └── sample_sentences.txt
└── outputs/
    └── translation_history.txt
```

## How It Works

1. Load the pretrained MarianMT model and tokenizer.
2. Detect whether CUDA is available; otherwise use the CPU.
3. Tokenize English input sentences.
4. Generate French output tokens using the Transformer model.
5. Decode the generated tokens into readable French text.
6. Display translations in the terminal.
7. Save sample and interactive translations to a text file.

## What Is a Transformer?

A Transformer is a neural network architecture that uses attention mechanisms to process relationships between tokens.

Transformer-based models are widely used in machine translation, text generation, summarization, and other NLP applications.

## What Is Tokenization?

Tokenization converts text into smaller units, called tokens, that the model can process.

The tokenizer maps these units to numerical IDs before passing them to the neural network.

## Installation

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## Run the Program

```bash
python translator.py
```

The first run requires an internet connection to download the model.

## Example

**English:** I love learning Python.

**French:** J'adore apprendre Python.

The exact output may vary depending on the model.

## Limitations

- Only English-to-French translation is supported.
- The pretrained model may produce inaccurate translations.
- Longer inputs may be truncated.
- The model download requires internet access on the first run.
- Translation may be slower when running on a CPU.
- No fine-tuning or custom training is performed.

## Future Improvements

- Add support for more languages.
- Build a Flask or Streamlit interface.
- Translate uploaded text files.
- Add automatic language detection.
- Evaluate translations using reference datasets.
- Compare different Transformer models.

## Learning Outcomes

Through this project, I learned:

- How pretrained Transformer models work.
- How Hugging Face Transformers is used.
- How tokenization and text generation work.
- How to perform machine translation.
- How to use PyTorch for inference.
- How to save generated translations.

## Project Status

Project 9 of 9 in the AI/ML Mini Projects portfolio. Complete after successful local testing.
