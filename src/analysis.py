import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# get path relative to this file
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "..", "data", "clean_data.csv")

# load cleaned data
df = pd.read_csv(file_path)

# helper function to create scatter + trend line
def scatter_with_trend(x, y, x_label, y_label, title, filename):

    plt.figure(figsize=(10,6))

    # scatter points (smaller + transparent)
    plt.scatter(x, y, alpha=0.4, s=25)

    # compute regression line
    m, b = np.polyfit(x, y, 1)

    # plot trend line
    plt.plot(x, m*x + b)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.grid(True)
    plt.tight_layout()

    # save figure
    plt.savefig(os.path.join(BASE_DIR, "..", "visuals", filename))

    plt.show()


# -------------------------------
# 1. Phone Usage vs Productivity
# -------------------------------
scatter_with_trend(
    df["phone_usage_hours"],
    df["productivity_score"],
    "Phone Usage (hours)",
    "Productivity Score",
    "Phone Usage vs Productivity",
    "phone_vs_productivity.png"
)

# -------------------------------
# 2. Phone Usage vs Study Hours
# -------------------------------
plt.figure(figsize=(10,6))

# transparent scatter
plt.scatter(
    df["phone_usage_hours"],
    df["study_hours_per_day"],
    alpha=0.05,
    s=12
)

# trend line
x = df["phone_usage_hours"]
y = df["study_hours_per_day"]
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Phone Usage (hours)")
plt.ylabel("Study Hours per Day")
plt.title("Phone Usage vs Study Time")

plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_study_scatter.png"))
plt.show()


# HEXBIN VERSION (density plot)
plt.figure(figsize=(10,6))

plt.hexbin(
    df["phone_usage_hours"],
    df["study_hours_per_day"],
    gridsize=45,
    cmap="Blues"
)

plt.colorbar(label="Number of Students")

plt.xlabel("Phone Usage (hours)")
plt.ylabel("Study Hours per Day")
plt.title("Density of Phone Usage vs Study Time")

plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_study_hexbin.png"))
plt.show()

# -------------------------------
# 3. Phone Usage vs Sleep
# -------------------------------
plt.figure(figsize=(10,6))

# transparent scatter
plt.scatter(
    df["phone_usage_hours"],
    df["sleep_hours"],
    alpha=0.05,
    s=12
)

# trend line
x = df["phone_usage_hours"]
y = df["sleep_hours"]
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Phone Usage (hours)")
plt.ylabel("Sleep Hours")
plt.title("Phone Usage vs Sleep")

plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_sleep_scatter.png"))
plt.show()


# HEXBIN VERSION
plt.figure(figsize=(10,6))

plt.hexbin(
    df["phone_usage_hours"],
    df["sleep_hours"],
    gridsize=45,
    cmap="Purples"
)

plt.colorbar(label="Number of Students")

plt.xlabel("Phone Usage (hours)")
plt.ylabel("Sleep Hours")
plt.title("Density of Phone Usage vs Sleep")

plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(BASE_DIR, "..", "visuals", "phone_vs_sleep_hexbin.png"))
plt.show()

# -------------------------------
# 4. Sleep vs Productivity
# -------------------------------
scatter_with_trend(
    df["sleep_hours"],
    df["productivity_score"],
    "Sleep Hours",
    "Productivity Score",
    "Sleep vs Productivity",
    "sleep_vs_productivity.png"
)

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