
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


# STEP 1: Locate the dataset files
project_dir = Path(__file__).resolve().parent

exercise_path = project_dir / "exercise.csv"
calories_path = project_dir / "calories.csv"

# STEP 2: Load the datasets
exercise_data = pd.read_csv(exercise_path)
calories_data = pd.read_csv(calories_path)

print("Datasets loaded successfully!")
print("Exercise dataset shape:", exercise_data.shape)
print("Calories dataset shape:", calories_data.shape)

# STEP 3: Merge datasets using User_ID
data = pd.merge(
    exercise_data,
    calories_data,
    on="User_ID",
    how="inner",
    validate="one_to_one",
)

print("\nMerged dataset shape:", data.shape)
print("\nFirst five rows:")
print(data.head())

# STEP 4: Prepare features and target
feature_columns = [
    "Gender",
    "Age",
    "Height",
    "Weight",
    "Duration",
    "Heart_Rate",
    "Body_Temp",
]

target_column = "Calories"

X = data[feature_columns]
y = data[target_column]

print("\nMissing values:")
print(data[feature_columns + [target_column]].isnull().sum())

if X.isnull().any().any() or y.isnull().any():
    raise ValueError(
        "Dataset contains missing values. "
        "Please check the CSV files before training."
    )

# STEP 5: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# STEP 6: Encode gender and train the regression model
preprocessor = ColumnTransformer(
    transformers=[
        (
            "gender",
            OneHotEncoder(handle_unknown="ignore"),
            ["Gender"],
        )
    ],
    remainder="passthrough",
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]
)

print("\nTraining the model...")
model.fit(X_train, y_train)

print("Model trained successfully!")

# STEP 7: Evaluate model performance
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\n--- MODEL EVALUATION ---")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R2 Score: {r2:.4f}")

# STEP 8: Save the trained model
model_path = project_dir / "calories_model.joblib"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Saved to:", model_path)

# STEP 9: Make predictions from user input
print("\n--- CALORIES BURNED PREDICTOR ---")

while True:
    choice = input(
        "\nPress Enter to predict calories "
        "or type 'exit' to quit: "
    ).strip().lower()

    if choice == "exit":
        print("Goodbye!")
        break

    try:
        gender = input("Gender (male/female): ").strip().lower()

        if gender not in ["male", "female"]:
            print("Please enter male or female.")
            continue

        age = int(input("Age (years): "))
        height = float(input("Height (cm): "))
        weight = float(input("Weight (kg): "))
        duration = float(input("Exercise duration (minutes): "))
        heart_rate = float(input("Heart rate (bpm): "))
        body_temp = float(input("Body temperature (Celsius): "))

        if (
            age <= 0
            or height <= 0
            or weight <= 0
            or duration < 0
            or heart_rate <= 0
            or body_temp <= 0
        ):
            print("Please enter valid positive measurements.")
            continue

        user_data = pd.DataFrame(
            [
                {
                    "Gender": gender,
                    "Age": age,
                    "Height": height,
                    "Weight": weight,
                    "Duration": duration,
                    "Heart_Rate": heart_rate,
                    "Body_Temp": body_temp,
                }
            ]
        )

        predicted_calories = model.predict(user_data)[0]

        print(
            f"\nEstimated Calories Burned: "
            f"{predicted_calories:.2f} kcal"
        )

    except ValueError:
        print("Invalid input. Please enter numeric values.")
