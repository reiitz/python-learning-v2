# Old way: for loop
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]

# New way: list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print(squared)  # [1, 4, 9, 16, 25]

print(list(range(20)))   # See where it stops
print(list(range(21)))   # See if 20 appears

evens = [num for num in range(21) if num % 2 == 0]
print(evens)
# Regular function
def square(x):
    return x ** 2

# Lambda (anonymous function)
square_lambda = lambda x: x ** 2

print(square(5))          # 25
print(square_lambda(5))   # 25

# Practical use: sorting students by average
students = [
    {"name": "Chiamaka", "average": 87},
    {"name": "Tunde", "average": 90},
    {"name": "Amara", "average": 79}
]

# Sort by average using lambda
sorted_students = sorted(students, key=lambda s: s["average"])
print([s["name"] for s in sorted_students])  # ['Amara', 'Chiamaka', 'Tunde']