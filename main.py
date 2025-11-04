import csv

# Read the original CSV
with open('books.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    books = list(csv_reader)

# Filter for high-rated books (rating >= 4)
high_rated = [book for book in books if int(book['rating']) >= 4]

# Write to new CSV
with open('high_rated_books.csv', 'w', newline='') as file:
    fieldnames = ['title', 'author', 'year', 'rating']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()
    for book in high_rated:
        csv_writer.writerow(book)

print(f"Created high_rated_books.csv with {len(high_rated)} books")