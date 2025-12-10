#temperature converter
# Temperature Converter in Python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
 
print("Select conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
 
choice = input("Enter choice(1/2): ")
 
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius)} Fahrenheit.")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit)} Celsius.")
else:
    print("Invalid input")