# AI/ML Mini-Projects Portfolio

Welcome to my **AI/ML Mini-Projects Portfolio!** 🚀

This repository contains nine hands-on projects exploring Artificial Intelligence, Machine Learning, Natural Language Processing, Data Analysis, Automation, and Web Development using Python.

The goal of this collection is to strengthen my practical programming skills, understand important AI/ML concepts, and build real-world applications through project-based learning.

## 📌 Portfolio Overview

- **Total Projects:** 9
- **Projects Implemented:** 9
- **Primary Language:** Python
- **Focus Areas:** Machine Learning, NLP, Data Science, Transformers, Chatbots, and Automation
- **Development Environment:** VS Code, Python Virtual Environment, Git, GitHub

## 📂 Project Collection

| No. | Project | Key Technologies | Status |
|---|---|---|---|
| 01 | [Spam Detection](./01-Spam-Email-Detection/) | Python, NLP, TF-IDF, Scikit-learn, Naive Bayes | ✅ Completed |
| 02 | [Calories Burned Prediction](./02-Calories-Burned-Prediction/) | Python, Pandas, Scikit-learn, Random Forest Regression | ✅ Completed |
| 03 | [YouTube Trending Videos Analysis](./03-YouTube-Trending-Videos-Analysis/) | Python, Pandas, NumPy, Matplotlib, Seaborn | ✅ Completed |
| 04 | [Hate Speech Detection](./04-Hate-Speech-Detection/) | Python, NLP, TF-IDF, Logistic Regression | ✅ Completed |
| 05 | [Chatbot with NLP](./05-Chatbot-with-NLP/) | Python, NLTK, TF-IDF, Scikit-learn | ✅ Completed |
| 06 | [Text Autocorrector](./06-Text-Autocorrector/) | Python, N-grams, NLP, Edit Distance | ✅ Completed |
| 07 | [Telegram Bot](./07-Telegram-Bot/) | Python, Telegram Bot API, python-telegram-bot | ✅ Completed |
| 08 | [Flask Chatbot](./08-Flask-Chatbot/) | Python, Flask, HTML, CSS, JavaScript | ✅ Completed |
| 09 | [Language Translation Using Transformers](./09-Language-Translation/) | Python, PyTorch, Hugging Face Transformers, MarianMT | 🔄 Testing |

**Note:** Project 9 is marked as testing until its translation program runs successfully. Once tested, change its status to `✅ Completed`.

Each project has its own folder containing source code, dependencies, and documentation.

---

## 🌟 Featured Projects

### 01 — Spam Detection

A machine learning application that classifies text messages as spam or legitimate.

**Technologies:** Python, Scikit-learn, TF-IDF, Multinomial Naive Bayes

**Highlights:**
- Text preprocessing and feature extraction
- Spam classification using supervised machine learning
- Model evaluation using accuracy and classification metrics

**Model Accuracy:** 97.04%

[View Project](./01-Spam-Email-Detection/)

### 02 — Calories Burned Prediction

A regression-based machine learning project that predicts calories burned during physical activity.

**Technologies:** Python, Pandas, Scikit-learn, Random Forest Regressor

**Highlights:**
- Data preprocessing and feature engineering
- Regression model training
- Model evaluation using MAE, RMSE, and R²

**Results:**
- MAE: 1.70
- RMSE: 2.67
- R² Score: 0.9982

[View Project](./02-Calories-Burned-Prediction/)

### 03 — YouTube Trending Videos Analysis

An exploratory data analysis project examining YouTube trending video statistics.

**Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn

**Highlights:**
- Dataset cleaning and exploration
- Analysis of video views, likes, comments, and categories
- Data visualization and trend identification

[View Project](./03-YouTube-Trending-Videos-Analysis/)

### 04 — Hate Speech Detection

An NLP-based classification project for detecting hate speech and offensive language in text.

**Technologies:** Python, NLP, TF-IDF, Logistic Regression

**Highlights:**
- Text cleaning and preprocessing
- Multi-class text classification
- Classification report and confusion matrix

**Model Accuracy:** 86.86%

[View Project](./04-Hate-Speech-Detection/)

### 05 — Chatbot with NLP

An intent-based chatbot that recognizes user messages and generates predefined responses.

**Technologies:** Python, NLTK, TF-IDF, Logistic Regression

**Highlights:**
- Text tokenization and stemming
- Intent classification
- Interactive terminal-based chatbot
- Saving and loading trained models using Joblib

**Test Accuracy:** 87.50% on the project's test split

[View Project](./05-Chatbot-with-NLP/)

### 06 — Text Autocorrector

A Python-based text correction application using N-gram language modeling and word similarity.

**Technologies:** Python, NLP, Unigrams, Bigrams

**Highlights:**
- Vocabulary generation from training text
- Spelling correction suggestions
- Context-aware candidate ranking
- Interactive text correction

[View Project](./06-Text-Autocorrector/)

### 07 — Telegram Bot Using Python

An interactive Telegram chatbot developed using Python and the Telegram Bot API.

**Technologies:** Python, python-telegram-bot, python-dotenv

**Highlights:**
- Telegram BotFather integration
- Command handling
- Automated message responses
- Secure API token management using environment variables

[View Project](./07-Telegram-Bot/)

### 08 — Flask Chatbot with Web Interface

A browser-based chatbot application with a Python backend and interactive frontend.

**Technologies:** Python, Flask, HTML, CSS, JavaScript

**Highlights:**
- Responsive chatbot interface
- Flask API endpoints
- JavaScript Fetch API integration
- Rule-based automated responses
- Frontend and backend communication

[View Project](./08-Flask-Chatbot/)

### 09 — Language Translation Using Transformers

An English-to-French language translation application using a pretrained Transformer model.

**Technologies:** Python, PyTorch, Hugging Face Transformers, MarianMT

**Highlights:**
- Pretrained Transformer model integration
- Text tokenization
- English-to-French machine translation
- Interactive terminal-based translator
- Translation history saved to a text file

**Model:** `Helsinki-NLP/opus-mt-en-fr`

[View Project](./09-Language-Translation/)

---

## 🛠️ Technologies and Tools

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest
- Naive Bayes
- Logistic Regression

### Natural Language Processing
- NLTK
- TF-IDF
- N-gram Language Models
- Hugging Face Transformers
- MarianMT

### Data Analysis and Visualization
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Web Development and Automation
- Flask
- HTML
- CSS
- JavaScript
- Telegram Bot API

### Development Tools
- Visual Studio Code
- Git and GitHub
- Python Virtual Environments
- Jupyter Notebook

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shrutijha-git/AI-ML-Mini-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-ML-Mini-Projects
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 5. Install Project Dependencies

Each project contains its own `requirements.txt` file.

For example, to install dependencies for the Flask Chatbot:

```bash
python -m pip install -r 08-Flask-Chatbot/requirements.txt
```

### 6. Run a Project

For example:

```bash
python 08-Flask-Chatbot/app.py
```

Refer to each project's individual README for its setup instructions.

Some projects require additional datasets, pretrained model downloads, or environment variables.

---

## 📚 Key Learning Outcomes

Through these projects, I gained practical experience in:

- Python programming and problem-solving
- Data preprocessing and exploratory data analysis
- Supervised machine learning and model evaluation
- Text classification and natural language processing
- N-gram language modeling
- Building interactive chatbots
- Integrating APIs and environment variables
- Developing web applications with Flask
- Using pretrained Transformer models
- Managing Python dependencies
- Organizing and documenting projects with Git and GitHub

---

## 🔮 Future Improvements

- Deploy selected projects as interactive web applications
- Build more advanced chatbot systems
- Improve model evaluation and performance
- Explore deep learning architectures
- Add multilingual NLP capabilities
- Experiment with additional Transformer models
- Develop user-friendly interfaces for ML applications

---

## 👩‍💻 About This Repository

This repository documents my hands-on learning journey in Artificial Intelligence and Machine Learning.

Each project represents an opportunity to explore a new concept, implement it using Python, troubleshoot real development challenges, and improve my technical skills.

The projects are intended for learning, experimentation, and portfolio demonstration.

---

## ⭐ Support

If you find this repository helpful, consider giving it a star!

**GitHub Repository:** [AI-ML-Mini-Projects](https://github.com/shrutijha-git/AI-ML-Mini-Projects)

---

**Built with Python, curiosity, and a passion for learning AI/ML.** 🚀
