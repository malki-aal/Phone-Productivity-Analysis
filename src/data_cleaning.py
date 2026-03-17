import pandas as pd


df = pd.read_csv('../data/student_productivity.csv')

df.columns = df.columns.str.strip().str.lower()


df = df.dropna()


df = df[df["sleep_hours"] > 0]


df.to_csv("../data/clean_data.csv", index=False)

print("Cleaned data saved!")
print(df.head())