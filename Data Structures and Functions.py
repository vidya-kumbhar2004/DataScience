# Week 2 – Data Structures and Functions
# Project: Data Cleaning Script
# Author: Vidya
# Description: This script demonstrates Python data structures, functions, 
# and a simple data cleaning project that removes duplicates and invalid data.

# ------------------------------
# Example 1: Working with Lists
# ------------------------------
fruits = ["apple", "banana", "cherry", "apple", "", "mango", None, "banana"]
print("Original Data:", fruits)

# ------------------------------
# Example 2: Function to Clean Data
# ------------------------------
def clean_data(data):
    """Removes duplicates, empty strings, and None values from the list."""
    cleaned = list(set(filter(lambda x: x not in ("", None), data)))
    return cleaned

cleaned_fruits = clean_data(fruits)
print("Cleaned Data:", cleaned_fruits)

# ------------------------------
# Example 3: Dictionary Example
# ------------------------------
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "mango": "orange"
}
print("Fruit Colors Dictionary:", fruit_colors)

# ------------------------------
# Example 4: List Comprehension
# ------------------------------
uppercase_fruits = [fruit.upper() for fruit in cleaned_fruits]
print("Uppercase Cleaned Fruits:", uppercase_fruits)

# ------------------------------
# Example 5: Using Lambda Function
# ------------------------------
lengths = list(map(lambda x: len(x), cleaned_fruits))
print("Length of Each Fruit Name:", lengths)

# ------------------------------
# Example 6: Recursive Function (Sum of Squares)
# ------------------------------
def sum_of_squares(n):
    """Calculates the sum of squares from 1 to n using recursion."""
    if n == 0:
        return 0
    else:
        return n**2 + sum_of_squares(n - 1)

print("Sum of squares from 1 to 5:", sum_of_squares(5))

# ------------------------------
# Final Summary Output
# ------------------------------
print("\nSummary:")
print("• Removed duplicates and empty data.")
print("• Demonstrated use of lists, sets, dictionaries, and functions.")
print("• Used lambda, recursion, and list comprehension.")
print("• Cleaned and transformed data successfully.")
