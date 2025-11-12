import sqlite3

conn = sqlite3.connect('learning.db')
cursor = conn.cursor()

print("=== INNER JOIN ===")
print("Students who have enrollments:\n")

cursor.execute('''
    SELECT students.name, enrollments.course_name, enrollments.grade
    FROM students
    INNER JOIN enrollments ON students.student_id = enrollments.student_id
''')

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} - {row[2]}")

print("\n=== LEFT JOIN ===")
print("ALL students (including those without enrollments):\n")

cursor.execute('''
    SELECT students.name, enrollments.course_name, enrollments.grade
    FROM students
    LEFT JOIN enrollments ON students.student_id = enrollments.student_id
''')

for row in cursor.fetchall():
    course = row[1] if row[1] else "No enrollment"
    grade = row[2] if row[2] else "N/A"
    print(f"{row[0]}: {course} - {grade}")

print("\n=== PRACTICE: Count courses per student ===")
cursor.execute('''
    SELECT students.name, COUNT(enrollments.course_name) as course_count
    FROM students
    LEFT JOIN enrollments ON students.student_id = enrollments.student_id
    GROUP BY students.name
    ORDER BY course_count DESC
''')

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} courses")

conn.close()