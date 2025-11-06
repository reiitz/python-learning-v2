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