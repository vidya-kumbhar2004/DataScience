# Week 4 – Data Visualization with Matplotlib and Seaborn
# Author: Vidya
# Description: This project demonstrates basic and advanced visualizations
# using Matplotlib and Seaborn. Contains scatter plots, histograms, heatmaps,
# and a simple dashboard-style set of charts.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ----------------------------------------
# Example 1: Simple Line Plot
# ----------------------------------------
x = [1, 2, 3, 4, 5]
y = [10, 14, 12, 18, 20]

plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# ----------------------------------------
# Example 2: Histogram
# ----------------------------------------
data = np.random.randint(1, 100, 50)

plt.figure(figsize=(6,4))
plt.hist(data, bins=10, edgecolor='black')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ----------------------------------------
# Example 3: Scatter Plot
# ----------------------------------------
hours = np.random.randint(1, 10, 20)
marks = hours * 9 + np.random.randint(-5, 5, 20)

plt.figure(figsize=(6,4))
plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# ----------------------------------------
# Example 4: Seaborn Pairplot
# ----------------------------------------
df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
plt.show()

# ----------------------------------------
# Example 5: Heatmap
# ----------------------------------------
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, linewidths=0.5)
plt.title("Correlation Heatmap (Iris Dataset)")
plt.show()

# ----------------------------------------
# Dashboard Style Layout
# ----------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(14,4))

# Scatter
axs[0].scatter(df["sepal_length"], df["sepal_width"])
axs[0].set_title("Sepal Length vs Width")

# Histogram
axs[1].hist(df["petal_length"], bins=10)
axs[1].set_title("Petal Length Distribution")

# Line Plot
axs[2].plot(df["petal_width"])
axs[2].set_title("Petal Width Trend")

plt.tight_layout()
plt.show()

print("\nSummary:")
print("• Created line, scatter, and histogram plots using Matplotlib.")
print("• Used Seaborn for pairplots and heatmaps.")
print("• Built a dashboard with multiple plots for dataset overview.")
