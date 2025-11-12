import sqlite3

# Connect to database (creates it if doesn't exist)
conn = sqlite3.connect('learning.db')
cursor = conn.cursor()

# Create tables for JOIN practice
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
)
''')

# Insert sample data
students_data = [
    (1, 'Chiamaka', 16),
    (2, 'Tunde', 17),
    (3, 'Amara', 16),
    (4, 'Kemi', 17),
    (5, 'Bola', 16)
]

enrollments_data = [
    (1, 1, 'Mathematics', 85),
    (2, 1, 'Physics', 90),
    (3, 2, 'Mathematics', 92),
    (4, 2, 'Chemistry', 88),
    (5, 3, 'Physics', 76),
    (6, 3, 'Chemistry', 82),
    (7, 4, 'Mathematics', 95)
    # Note: Bola (student_id 5) has no enrollments
]

cursor.executemany('INSERT OR IGNORE INTO students VALUES (?, ?, ?)', students_data)
cursor.executemany('INSERT OR IGNORE INTO enrollments VALUES (?, ?, ?, ?)', enrollments_data)

conn.commit()
print("Database setup complete!")
print(f"Students: {len(students_data)}")
print(f"Enrollments: {len(enrollments_data)}")

conn.close()