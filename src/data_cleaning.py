import pandas as pd
import os

# get path relative to this file
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "..", "data", "student_productivity.csv")

# load data
df = pd.read_csv(file_path)

# clean column names
df.columns = df.columns.str.strip().str.lower()

# drop any missing values
df = df.dropna()

# OPTIONAL: remove unrealistic values
df = df[df["sleep_hours"] > 0]

# save cleaned dataset
output_path = os.path.join(BASE_DIR, "..", "data", "clean_data.csv")
df.to_csv(output_path, index=False)

print("Data cleaned and saved at:", output_path)
print(df.head())