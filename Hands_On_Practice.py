#sum of Squares
def sum_of_squares(numbers):
    return sum([x**2 for x in numbers])

nums = [1, 2, 3, 4, 5]
print("Sum of squares:", sum_of_squares(nums))
# Filter even numbers from a list using lambda
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)
