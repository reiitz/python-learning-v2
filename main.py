import json

# Read JSON
with open('books.json', 'r') as file:
    data = json.load(file)

# Filter for programming books
programming_books = [
    book for book in data['books'] 
    if 'programming' in book['tags']
]

# Create new structure
output = {
    'books': programming_books,
    'count': len(programming_books)
}

# Write to new JSON file
with open('programming_books.json', 'w') as file:
    json.dump(output, file, indent=2)

print(f"Created programming_books.json with {output['count']} books")