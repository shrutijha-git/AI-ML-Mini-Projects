
# AI & Machine Learning Mini Projects

### A Collection of 9 Hands-On AI, Machine Learning, and NLP Projects

Welcome to my AI & Machine Learning Mini Projects repository!

This repository documents my practical learning journey
through Artificial Intelligence, Machine Learning,
Natural Language Processing, Deep Learning, and
Data Analytics using Python.

The collection includes projects involving text
classification, regression, exploratory data analysis,
chatbots, automation, and language translation.

Each project is organized in its own folder with
source code, dependencies, and documentation.

---

## Project Collection

| No. | Project | Key Technologies | Status |
|-----|---------|------------------|--------|
| 01 | [Spam Detection](./01-Spam-Email-Detection/) | Python, NLP, TF-IDF, Scikit-learn, Naive Bayes | Completed |
| 02 | Calories Burned Prediction | Python, Pandas, Scikit-learn, Regression | Planned |
| 03 | YouTube Trending Videos Analysis | Python, Pandas, NumPy, Matplotlib, Seaborn | Planned |
| 04 | Hate Speech Detection | Python, NLP, Deep Learning | Planned |
| 05 | Chatbot with NLP | Python, NLTK | Planned |
| 06 | Text Autocorrector | Python, N-grams, NLP | Planned |
| 07 | Telegram Bot | Python, Telegram Bot API | Planned |
| 08 | Flask Chatbot | Python, Flask, HTML, CSS | Planned |
| 09 | Language Translation | Python, Transformers, NLP | Planned |

Project links will be added as each project is completed.

---

## Featured Project: Spam Detection

### Project 01 — Spam Detection Using Machine Learning

A text classification system that identifies SMS
messages as spam or legitimate (ham).

The model uses TF-IDF vectorization and a
Multinomial Naive Bayes classifier.

**Key Results:**

- Test Accuracy: **97.04%**
- Spam Precision: **100%**
- Spam Recall: **77.85%**
- Spam F1-score: **0.88**
- Dataset: **5,572 SMS messages**
- Test Set: **1,115 messages**

**What I implemented:**

- Dataset loading and preparation
- TF-IDF feature extraction
- Stratified train-test splitting
- Multinomial Naive Bayes classification
- Model evaluation using classification metrics
- Model serialization with Joblib
- Interactive message classification in the terminal

**Project Link:**

[View Spam Detection Project](./01-Spam-Email-Detection/)

Note: This project uses an SMS dataset rather than
an email-specific dataset.

---

## Technologies and Tools

### Programming

- Python
- HTML and CSS (planned)

### Machine Learning

- Scikit-learn
- Classification algorithms
- Regression algorithms
- Model evaluation techniques

### Natural Language Processing

- TF-IDF Vectorization
- NLTK (planned)
- N-gram language models (planned)
- Transformers (planned)

### Data Analysis and Visualization

- Pandas
- NumPy
- Matplotlib (planned)
- Seaborn (planned)

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Python virtual environments
- Jupyter Notebook (planned)

### Additional Technologies to Explore

- Flask
- Telegram Bot API
- Deep Learning frameworks

---

## Repository Structure

```text
AI-ML-Mini-Projects/
|
|-- 01-Spam-Email-Detection/
|   |-- spam_detector.py
|   |-- requirements.txt
|   |-- README.md
|   |-- SMSSpamCollection.tsv
|   |-- DATASET_INFO.txt
|
|-- README.md
|-- .gitignore
```

Additional project folders will be added as
development progresses.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shrutijha-git/AI-ML-Mini-Projects.git
```

### 2. Navigate to the Repository

```bash
cd AI-ML-Mini-Projects
```

### 3. Open a Project Folder

For example:

```bash
cd 01-Spam-Email-Detection
```

### 4. Create a Virtual Environment

```bash
python -m venv .venv
```

### 5. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 6. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 7. Run the Project

```bash
python spam_detector.py
```

Refer to each project's README for
project-specific setup and usage instructions.

---

## Learning Objectives

Through these projects, I aim to strengthen
my practical understanding of:

- Data preprocessing and feature engineering
- Supervised machine learning
- Classification and regression
- Exploratory data analysis
- Natural Language Processing
- Deep Learning fundamentals
- Model training and evaluation
- Building Python-based applications
- Working with APIs
- Developing reproducible AI/ML workflows

---

## Development Roadmap

- [x] 01 — Spam Detection
- [ ] 02 — Calories Burned Prediction
- [ ] 03 — YouTube Trending Videos Analysis
- [ ] 04 — Hate Speech Detection
- [ ] 05 — Chatbot with NLP
- [ ] 06 — Text Autocorrector
- [ ] 07 — Telegram Bot
- [ ] 08 — Flask Chatbot
- [ ] 09 — Language Translation

---

## About This Repository

This repository is a growing collection of
hands-on AI and Machine Learning mini-projects.

My goal is to develop a stronger foundation
in machine learning algorithms, NLP techniques,
data analytics, and practical AI applications.

Projects are being rebuilt, tested, and documented
as part of my continued learning and portfolio
development.

---

## Connect With Me

**GitHub:**
https://github.com/shrutijha-git

**LinkedIn:**
https://www.linkedin.com/in/shrutijha21/

---

## Dataset Credits

Individual projects use publicly available datasets
where applicable.

Dataset sources, citations, and licensing
information are documented in their respective
project folders.

For the Spam Detection project, the dataset is
the SMS Spam Collection v.1 by Tiago A. Almeida
and José María Gómez Hidalgo.

---

### Repository Status

**1 of 9 projects completed.**

More projects will be added as development continues.
