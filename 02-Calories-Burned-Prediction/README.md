# Calories Burned Prediction Using Machine Learning

## Overview

A machine learning regression project that estimates calories burned during exercise using demographic and physiological measurements.

The project uses a **Random Forest Regressor** implemented with Scikit-learn.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

## Dataset

**Source:** [Calories and Exercise Dataset — Kaggle](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos)

The dataset consists of two files:

- `exercise.csv` — 15,000 records containing exercise-related features.
- `calories.csv` — 15,000 corresponding calorie measurements.

Both files are merged using `User_ID`, resulting in 15,000 records.

### Input Features

- Gender
- Age
- Height
- Weight
- Exercise duration
- Heart rate
- Body temperature

**Target variable:** Calories burned (kcal).

## Machine Learning Workflow

1. Load and merge both datasets.
2. Check for missing values.
3. Select input features and the target variable.
4. Split the dataset into training and testing sets (80:20).
5. Encode the gender feature using OneHotEncoder.
6. Train a Random Forest regression model with 100 estimators.
7. Evaluate predictions using MAE, RMSE, and R².
8. Save the trained model using Joblib.
9. Accept user inputs for interactive predictions.

## Model Performance

| Evaluation Metric | Result |
|---|---|
| Mean Absolute Error (MAE) | 1.70 kcal |
| Root Mean Squared Error (RMSE) | 2.67 kcal |
| R² Score | 0.9982 |
| Dataset Records | 15,000 |
| Training Split | 80% |
| Testing Split | 20% |

The model performed strongly on the held-out test set. These results do not guarantee equivalent accuracy on other datasets or real-world exercise measurements.

## Sample Predictions

| Gender | Age | Duration | Heart Rate | Predicted Calories |
|---|---|---|---|---|
| Male | 35 | 0 min | 90 bpm | 3.42 kcal |
| Female | 35 | 60 min | 120 bpm | 235.32 kcal |

These are model estimates rather than medically validated calorie measurements.

## How to Run

Clone the repository:

```bash
git clone https://github.com/shrutijha-git/AI-ML-Mini-Projects.git
```

Navigate to the project:

```bash
cd AI-ML-Mini-Projects/02-Calories-Burned-Prediction
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Download `exercise.csv` and `calories.csv` from the linked Kaggle dataset and place them inside this project folder.

Run the program:

```bash
python calories_prediction.py
```

## Limitations

- Predictions depend on the characteristics of the training dataset.
- The model has not been independently validated on real-world exercise data.
- Random Forest regression does not enforce physically meaningful constraints such as exactly zero calories for zero exercise duration.
- Results are educational estimates and should not be treated as clinical measurements.

## Project Status

**Completed — Model trained, evaluated, and tested.**

Part of the [AI-ML-Mini-Projects repository](../README.md).