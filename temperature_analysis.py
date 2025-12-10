count = int(input("How many temperature readings? "))

temperatures = []

for i in range(count):
    temp = float(input(f"Enter temperature {i+1}: "))
    temperatures.append(temp)

average = sum(temperatures) / count
highest = max(temperatures)
lowest = min(temperatures)

print("Average temperature:", average)
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
