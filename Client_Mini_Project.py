def clean_data(data):
    # Remove duplicates and empty values
    cleaned = list(set(filter(None, data)))
    return cleaned

data = ["apple", "", "banana", "apple", "mango", None, "banana"]
print(data)
print("Cleaned data:", clean_data(data))
