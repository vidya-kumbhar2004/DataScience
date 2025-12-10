# WEEK 3: NUMPY AND PANDAS FOR DATA MANIPULATION
# OBJECTIVES: NumPy operations, Pandas indexing, Data Cleaning, and Aggregation.

import numpy as np
import pandas as pd

# --- 1. SETUP: Simulate a Dataset (Client Project) ---
# Using the well-known Iris dataset as a stand-in for your client data.
print("--- 1. Initial Data Inspection ---")
df = pd.DataFrame({
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9],
    'sepal_width':  [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1],
    'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5],
    'species':      ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Versicolor', 'Versicolor', 'Versicolor', 'Versicolor', 'Versicolor']
})

# Simulate some missing data (Client Project: Clean and aggregate)
df.loc[3, 'sepal_width'] = np.nan
df.loc[6, 'petal_length'] = np.nan
print(f"Original Data with 2 NaN values:\n{df}\n")

# --- 2. HANDS-ON: NumPy Operations & Pandas Manipulation ---
print("--- 2. NumPy Operations & Pandas Slicing ---")

# THEORY: NumPy arrays, operations, broadcasting
# Hands-On: Perform operations with NumPy
data_array = np.array(df['sepal_length'].head(5))
print(f"NumPy Array (First 5 sepal_length): {data_array}")
# Example of vectorized operation (broadcasting)
processed_array = data_array * 10
print(f"NumPy Operation (Array * 10): {processed_array}\n")

# THEORY: Pandas DataFrames, Series, indexing
# Hands-On: Manipulate datasets with Pandas
# Select rows using .loc (label-based indexing)
subset_loc = df.loc[df['species'] == 'Setosa', ['sepal_length', 'sepal_width']]
print(f"Pandas Selection (.loc - only 'Setosa' species):\n{subset_loc}\n")

# --- 3. CLIENT PROJECT: Clean and Aggregate Data ---
print("--- 3. Data Cleaning and Aggregation ---")

# Step A: Data Cleaning (Handle Missing Values)
print(f"Missing Values before cleaning:\n{df.isnull().sum()}")
# Fill missing 'sepal_width' values with the column mean (Imputation)
mean_sepal_width = df['sepal_width'].mean()
df['sepal_width'].fillna(mean_sepal_width, inplace=True)
# Fill missing 'petal_length' with the median
median_petal_length = df['petal_length'].median()
df['petal_length'].fillna(median_petal_length, inplace=True)

print("\nData Cleaning Complete (NaNs imputed with mean/median).")
print(f"Missing Values after cleaning:\n{df.isnull().sum()}")

# Step B: Data Aggregation (Calculate Averages)
# Client Project: Calculate averages (Grouping)
species_summary = df.groupby('species').agg(
    avg_sepal_length=('sepal_length', 'mean'),
    max_sepal_width=('sepal_width', 'max'),
    count=('species', 'size')
).reset_index()

print("\nData Aggregation (Averages by Species):")
print(species_summary)

# SCRIPT END