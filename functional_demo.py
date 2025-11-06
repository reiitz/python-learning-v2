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
# MAP: Apply a function to every item
numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squared_map = list(map(lambda x: x ** 2, numbers))
print(f"Squared (map): {squared_map}")

# Compare to comprehension (often more Pythonic)
squared_comp = [x ** 2 for x in numbers]
print(f"Squared (comprehension): {squared_comp}")

# FILTER: Keep only items that pass a test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with lambda
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens (filter): {evens_filter}")

# Compare to comprehension
evens_comp = [x for x in numbers if x % 2 == 0]
print(f"Evens (comprehension): {evens_comp}")

# Your turn: filter for high-achieving students
students_data = [
    {"name": "Chiamaka", "average": 87},
    {"name": "Tunde", "average": 90},
    {"name": "Amara", "average": 79},
    {"name": "Kemi", "average": 92}
]

high_achievers = list(filter(lambda s: s["average"] >= 85, students_data))
print(f"High achievers: {[s['name'] for s in high_achievers]}")