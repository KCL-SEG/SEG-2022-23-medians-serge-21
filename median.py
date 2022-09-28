"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# median function
def median(numbers: list) -> float:
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median = numbers[len(numbers) // 2]
    return median

# user input
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

# return solution
print(median(numbers))