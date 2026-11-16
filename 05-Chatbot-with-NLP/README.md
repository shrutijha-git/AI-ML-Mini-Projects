# Project 5 — Chatbot with NLP using NLTK

## Project Overview

This project is an intent-based chatbot developed using Python, Natural Language Processing (NLP), and machine learning. The chatbot identifies the intent behind a user's message and selects an appropriate response from predefined answers.

This program uses NLTK for text tokenization and stemming, then trains a TF-IDF and Logistic Regression classifier. It evaluates the model on held-out examples before retraining on the complete dataset for interactive use.

Because our dataset is small, the accuracy score may vary substantially depending on the examples. The confidence threshold is also a simple heuristic, not a guarantee that a response is correct.

## Technologies Used

- **Python:** Main programming language.
- **NLTK:** Tokenization and stemming for text preprocessing.
- **Scikit-learn:** TF-IDF vectorization, Logistic Regression, train-test splitting, and evaluation.
- **Joblib:** Saving and loading trained machine learning models.
- **JSON:** Storing training patterns, intents, and chatbot responses.

## What Is Joblib?

Joblib is a Python library used to save and load trained machine learning models.

Instead of retraining a model every time we want to use it, we can save the trained model to a `.joblib` file and load it later.

**Save a model:**

```python
joblib.dump(model, model_path)
```

**Load a saved model:**

```python
model = joblib.load(model_path)
```

Only load model files from trusted sources.

## Project Folder Structure

```text
05-Chatbot-with-NLP/
│
├── chatbot.py
├── intents.json
├── requirements.txt
├── README.md
│
├── models/
│   └── chatbot_model.joblib
│
└── outputs/
    └── classification_report.txt
```

The trained model file is generated locally and can be excluded from GitHub.

## Dataset

The project uses a custom dataset stored in `intents.json`.

It contains:

- 64 training examples
- 8 intent categories
- Predefined responses for each category

### Supported Intents

1. Greeting
2. Goodbye
3. Thanks
4. Python
5. Artificial Intelligence
6. Machine Learning
7. Natural Language Processing
8. Help

Each intent contains example patterns and a list of possible responses.

No external dataset download is required.

## How the Chatbot Works

### Step 1: Load the Dataset

The program reads `intents.json` and extracts example questions, intent labels, and predefined responses.

### Step 2: Text Preprocessing

NLTK performs tokenization and stemming.

- **Tokenization:** Splits text into individual tokens.
- **Stemming:** Reduces related words to simpler root-like forms.

For example, words such as "learning" and "learned" may be reduced to a common stem.

### Step 3: TF-IDF Vectorization

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It converts processed text into numerical features that a machine learning model can use.

### Step 4: Intent Classification

Logistic Regression learns patterns in the TF-IDF features and predicts which intent best matches the user's message.

### Step 5: Model Evaluation

The dataset is divided into training and testing examples.

The classifier is first evaluated using held-out test data.

### Step 6: Retraining and Saving

After evaluation, the classifier is trained again using all 64 available examples.

Joblib saves the trained pipeline to `models/chatbot_model.joblib`.

### Step 7: Chatbot Response

When the user enters a message:

1. The message is preprocessed.
2. The model estimates intent probabilities.
3. The highest-probability intent is selected.
4. If confidence is below 0.30, the chatbot displays a fallback message.
5. Otherwise, the chatbot selects a predefined response for that intent.

## Model Evaluation Results

| Metric | Result |
|---|---:|
| Total examples | 64 |
| Number of intents | 8 |
| Training examples | 48 |
| Testing examples | 16 |
| Accuracy | 87.50% |
| Macro F1-score | 0.87 |
| Weighted F1-score | 0.87 |

### Classification Performance

| Intent | Precision | Recall | F1-score |
|---|---:|---:|---:|
| AI | 0.67 | 1.00 | 0.80 |
| Goodbye | 1.00 | 0.50 | 0.67 |
| Greeting | 0.67 | 1.00 | 0.80 |
| Help | 1.00 | 1.00 | 1.00 |
| Machine Learning | 1.00 | 0.50 | 0.67 |
| NLP | 1.00 | 1.00 | 1.00 |
| Python | 1.00 | 1.00 | 1.00 |
| Thanks | 1.00 | 1.00 | 1.00 |

These metrics are based on a very small test set of two examples per intent and should not be interpreted as reliable estimates of general real-world performance.

## Example Chatbot Conversations

**Example 1**

User: WHAT IS PYTHON?

Bot: Python is a beginner-friendly language with many useful libraries.

**Example 2**

User: explain machine learning

Bot: Machine learning uses data to train models that make predictions or classifications.

**Example 3**

User: what does nlp do?

Bot: NLP is used in chatbots, translation, text classification, and sentiment analysis.

**Example 4**

User: what is earth?

Bot: I'm not sure about that. Try asking me about Python, AI, ML, or NLP.

## Limitations

- The chatbot supports only eight predefined intents.
- It cannot answer arbitrary general-knowledge questions.
- The training dataset contains only 64 examples.
- Some valid questions may be rejected because of low confidence.
- The model may incorrectly classify unfamiliar messages.
- Responses are predefined rather than generated.
- The reported accuracy comes from a small test set.
- The confidence threshold does not guarantee correctness.

## Future Improvements

- Expand the dataset with more questions and intents.
- Add topics such as NumPy, Pandas, programming syntax, and chatbot identity.
- Add rules for common greetings.
- Improve confidence handling.
- Evaluate the model on a larger and more varied dataset.
- Explore advanced NLP models and transformers.
- Build a web interface using Flask.

## How to Run

### 1. Install dependencies

From the project folder:

```bash
python -m pip install -r requirements.txt
```

### 2. Run the chatbot

```bash
python chatbot.py
```

### 3. Start chatting

Ask questions about Python, AI, machine learning, and NLP.

Type `exit` or `quit` to close the chatbot.

## Key Learning Outcomes

This project helped me understand:

- How intent-based chatbots work.
- How NLTK processes text.
- How TF-IDF converts text into numerical features.
- How Logistic Regression performs text classification.
- How to evaluate a classifier using accuracy, precision, recall, and F1-score.
- How Joblib saves trained machine learning models.
- Why small datasets limit chatbot performance.
- Why model confidence is not the same as model correctness.

## Project Status

**Completed — Project 5 of 9 in the AI/ML Mini Projects portfolio.**

The initial intent-based chatbot has been implemented, trained, evaluated, and tested. Improving its conversational coverage is a future enhancement.