import sqlite3

conn = sqlite3.connect('learning.db')
cursor = conn.cursor()

print("=== ROW_NUMBER: Assign row numbers to grades ===")
cursor.execute('''
    SELECT 
        students.name,
        enrollments.course_name,
        enrollments.grade,
        ROW_NUMBER() OVER (ORDER BY enrollments.grade DESC) as rank
    FROM students
    INNER JOIN enrollments ON students.student_id = enrollments.student_id
''')

for row in cursor.fetchall():
    print(f"#{row[3]}: {row[0]} - {row[1]} ({row[2]})")

print("\n=== RANK: Rank students within each course ===")
cursor.execute('''
    SELECT 
        students.name,
        enrollments.course_name,
        enrollments.grade,
        RANK() OVER (PARTITION BY enrollments.course_name ORDER BY enrollments.grade DESC) as rank
    FROM students
    INNER JOIN enrollments ON students.student_id = enrollments.student_id
    ORDER BY enrollments.course_name, rank
''')

for row in cursor.fetchall():
    print(f"{row[1]} - Rank {row[3]}: {row[0]} ({row[2]})")

print("\n=== PRACTICE: Top student in each course ===")
cursor.execute('''
    SELECT name, course_name, grade
    FROM (
        SELECT 
            students.name,
            enrollments.course_name,
            enrollments.grade,
            RANK() OVER (PARTITION BY enrollments.course_name ORDER BY enrollments.grade DESC) as rank
        FROM students
        INNER JOIN enrollments ON students.student_id = enrollments.student_id
    )
    WHERE rank = 1
''')

for row in cursor.fetchall():
    print(f"{row[0]} tops {row[1]} with {row[2]}")

conn.close()