import csv

filename = input("Enter CSV filename: ")

try:
    with open(filename, 'r') as file:
        data = csv.DictReader(file)
        rows = list(data)  # Convert to list to count
        print(f"Successfully loaded: {len(rows)} rows")

except FileNotFoundError:  
    print(f"Error: {filename} doesn't exist")