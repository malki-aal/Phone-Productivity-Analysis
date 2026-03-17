import pandas as pd
import matplotlib.pyplot as plt
import os

# get path relative to this file
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "..", "data", "clean_data.csv")

# load cleaned data
df = pd.read_csv(file_path)

# -------------------------------
# 1. Phone Usage vs Productivity
# -------------------------------
plt.scatter(df["phone_usage_hours"], df["productivity_score"])
plt.xlabel("Phone Usage (hours)")
plt.ylabel("Productivity Score")
plt.title("Phone Usage vs Productivity")
plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_productivity.png"))
plt.show()

# -------------------------------
# 2. Phone Usage vs Study Hours
# -------------------------------
plt.scatter(df["phone_usage_hours"], df["study_hours_per_day"])
plt.xlabel("Phone Usage (hours)")
plt.ylabel("Study Hours")
plt.title("Phone Usage vs Study Time")
plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_study.png"))
plt.show()

# -------------------------------
# 3. Phone Usage vs Sleep
# -------------------------------
plt.scatter(df["phone_usage_hours"], df["sleep_hours"])
plt.xlabel("Phone Usage (hours)")
plt.ylabel("Sleep Hours")
plt.title("Phone Usage vs Sleep")
plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_sleep.png"))
plt.show()

# -------------------------------
# 4. Sleep vs Productivity
# -------------------------------
plt.scatter(df["sleep_hours"], df["productivity_score"])
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity Score")
plt.title("Sleep vs Productivity")
plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "sleep_vs_productivity.png"))
plt.show()

# -------------------------------
# 5. Correlations
# -------------------------------
print("Phone vs Productivity:", df["phone_usage_hours"].corr(df["productivity_score"]))
print("Phone vs Study:", df["phone_usage_hours"].corr(df["study_hours_per_day"]))
print("Phone vs Sleep:", df["phone_usage_hours"].corr(df["sleep_hours"]))
print("Sleep vs Productivity:", df["sleep_hours"].corr(df["productivity_score"]))

# -------------------------------
# 6. High vs Low Phone Usage Groups
# -------------------------------
high_phone = df[df["phone_usage_hours"] > 5]
low_phone = df[df["phone_usage_hours"] <= 5]

print("High phone usage avg productivity:", high_phone["productivity_score"].mean())
print("Low phone usage avg productivity:", low_phone["productivity_score"].mean())