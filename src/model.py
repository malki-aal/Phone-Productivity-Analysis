import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# ---------------------------
# Load cleaned data
# ---------------------------
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "..", "data", "clean_data.csv")

df = pd.read_csv(file_path)

# ---------------------------
# Features and target
# ---------------------------
X = df[["phone_usage_hours", "sleep_hours", "study_hours_per_day"]]
y = df["productivity_score"]

# ---------------------------
# Train linear regression
# ---------------------------
model = LinearRegression()
model.fit(X, y)

# ---------------------------
# Print model info
# ---------------------------
print("Model coefficients (phone, sleep, study):", model.coef_)
print("Model intercept:", model.intercept_)

# Optional: predict for first 5 students
predictions = model.predict(X.head())
print("Predicted productivity for first 5 students:", predictions)