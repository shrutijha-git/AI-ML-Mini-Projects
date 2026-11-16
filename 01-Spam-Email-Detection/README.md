
# Spam Detection Using Machine Learning

## Project Overview

A machine learning-based spam detection system developed
using Python and Natural Language Processing (NLP).

The system classifies SMS text messages into two categories:

- **Spam:** Unwanted or suspicious promotional messages.
- **Ham:** Legitimate messages.

The project demonstrates text preprocessing, feature
extraction, supervised machine learning, model evaluation,
and real-time predictions through a command-line interface.

**Note:** Although originally developed as a spam email
detection practice project, the current model is trained
and evaluated using an SMS dataset.

---

## Technologies Used

- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **NLP Feature Extraction:** TF-IDF Vectorization
- **Classification Algorithm:** Multinomial Naive Bayes
- **Model Serialization:** Joblib
- **Development Environment:** Visual Studio Code

---

## Dataset

**Dataset Name:** SMS Spam Collection v.1

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

The dataset file used in this project contains:

| Category | Number of Messages |
|----------|-------------------:|
| Ham | 4,825 |
| Spam | 747 |
| **Total** | **5,572** |

The original dataset documentation describes 5,574
messages, while the downloaded file used for this
implementation contains 5,572 records.

The dataset is divided into:

- **Training data:** 80%
- **Testing data:** 20%

A stratified split is used to preserve the class
distribution in both sets.

---

## Project Workflow

### 1. Data Loading

Load the labeled SMS dataset using Pandas.

### 2. Data Preparation

Separate the dataset into:

- Input features (X): SMS message text
- Target labels (y): Spam or Ham

### 3. Train-Test Split

Split the dataset into training and testing sets
using an 80:20 ratio.

### 4. Feature Extraction

Apply TF-IDF (Term Frequency-Inverse Document
Frequency) to convert text messages into numerical
feature representations.

English stop-word removal is applied through
the TF-IDF vectorizer.

### 5. Model Training

Train a Multinomial Naive Bayes classifier using
the training data.

### 6. Model Evaluation

Evaluate the trained model using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### 7. Model Saving

Save the trained machine learning pipeline
using Joblib for future use.

### 8. User Input Prediction

Allow users to enter custom text messages through
the terminal and classify them as Spam or Ham.

---

## Model Performance

The model was evaluated on 1,115 test messages.

| Evaluation Metric | Result |
|-------------------|--------|
| Overall Accuracy | 97.04% |
| Spam Precision | 100% |
| Spam Recall | 77.85% |
| Spam F1-Score | 0.88 |
| Ham Precision | 0.97 |
| Ham Recall | 1.00 |
| Ham F1-Score | 0.98 |

### Classification Report

```text
              precision    recall  f1-score   support

         ham       0.97      1.00      0.98       966
        spam       1.00      0.78      0.88       149

    accuracy                           0.97      1115
   macro avg       0.98      0.89      0.93      1115
weighted avg       0.97      0.97      0.97      1115
```

### Confusion Matrix

```text
[[966   0]
 [ 33 116]]
```

| Actual / Predicted | Ham | Spam |
|--------------------|----:|-----:|
| Ham | 966 | 0 |
| Spam | 33 | 116 |

**Interpretation:**

- 966 legitimate messages were correctly classified.
- 116 spam messages were correctly detected.
- 33 spam messages were incorrectly classified as ham.
- No legitimate messages were incorrectly classified
  as spam in the test set.

The model correctly classified 1,082 out of 1,115
test messages.

Although the overall accuracy is high, spam recall
can be improved because the model missed 33 spam
messages in the test set.

---

## Sample Predictions

The following messages were tested through the
command-line interface.

### Test 1: Spam Message

**Input:**

Congratulations! You have won a free iPhone.
Claim your prize now!

**Prediction:**

SPAM

### Test 2: Legitimate Message

**Input:**

Hey, are we meeting tomorrow for our college project?

**Prediction:**

NOT SPAM (HAM)

### Test 3: Spam Message

**Input:**

URGENT! You have won a cash reward.
Call now to claim!

**Prediction:**

SPAM

All three sample messages were classified as expected.

---

## Installation and Setup

### Prerequisites

- Python 3.11 or 3.12 recommended
- Visual Studio Code or another Python editor
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-ML-Mini-Projects.git
```

Replace `YOUR_USERNAME` with your GitHub username
after publishing the repository.

### Step 2: Navigate to the Project Folder

```bash
cd AI-ML-Mini-Projects/01-Spam-Email-Detection
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Project

```bash
python spam_detector.py
```

Enter a text message when prompted.

Type `exit` to stop the program.

---

## Project Files

```text
01-Spam-Email-Detection/
|
|-- spam_detector.py
|-- requirements.txt
|-- README.md
|-- SMSSpamCollection.tsv
|-- DATASET_INFO.txt
```

The program also generates `spam_model.joblib`
after successful training.

---

## Learning Outcomes

Through this project, I strengthened my understanding of:

- Natural Language Processing fundamentals
- Text classification using machine learning
- TF-IDF feature extraction
- Multinomial Naive Bayes classification
- Supervised learning workflows
- Stratified train-test splitting
- Model evaluation using classification metrics
- Understanding confusion matrices
- Saving and reusing trained ML models
- Python-based command-line applications

---

## Limitations and Future Improvements

- The model is trained on SMS messages rather
  than a dedicated email dataset.
- Some spam messages are incorrectly classified
  as legitimate messages.
- Model performance may differ on new or
  unfamiliar message formats.

Possible future improvements:

- Experiment with Logistic Regression and
  Support Vector Machine classifiers.
- Tune classification thresholds to improve
  spam recall.
- Evaluate the model on additional datasets.
- Develop a Flask or Streamlit web interface.
- Extend the project using an email-specific
  dataset.

---

## Dataset Attribution

**Dataset:** SMS Spam Collection v.1

**Creators:**
Tiago A. Almeida and José María Gómez Hidalgo.

**Reference:**

Almeida, T. A., Gómez Hidalgo, J. M., and
Yamakami, A. (2011).

*Contributions to the Study of SMS Spam Filtering:
New Collection and Results.*

Proceedings of the ACM Symposium on
Document Engineering (DOCENG 2011).

**Dataset Source:**
https://archive.ics.uci.edu/dataset/228/sms+spam+collection

The original dataset documentation and licensing
information are preserved in `DATASET_INFO.txt`.

---

## Project Status

**Baseline Model Completed and Tested**

- Dataset successfully loaded
- Model trained successfully
- Test accuracy: 97.04%
- Classification metrics evaluated
- Model saved using Joblib
- Custom message predictions tested successfully

Future improvements and additional model
experiments are planned.
