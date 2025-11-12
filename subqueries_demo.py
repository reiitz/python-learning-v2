import sqlite3

conn = sqlite3.connect('learning.db')
cursor = conn.cursor()

print("=== All grades ===")
cursor.execute('SELECT AVG(grade) FROM enrollments')
avg_grade = cursor.fetchone()[0]
print(f"Average grade: {avg_grade:.2f}\n")

print("=== Students with above-average grades (using subquery) ===")
cursor.execute('''
    SELECT students.name, enrollments.course_name, enrollments.grade
    FROM students
    INNER JOIN enrollments ON students.student_id = enrollments.student_id
    WHERE enrollments.grade > (SELECT AVG(grade) FROM enrollments)
    ORDER BY enrollments.grade DESC
''')

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} - {row[2]}")

print("\n=== Students enrolled in Mathematics (using IN) ===")
cursor.execute('''
    SELECT name
    FROM students
    WHERE student_id IN (
        SELECT student_id
        FROM enrollments
        WHERE course_name = 'Mathematics'
    )
''')

for row in cursor.fetchall():
    print(f"{row[0]}")

print("\n=== PRACTICE: Students enrolled in more than 1 course ===")
cursor.execute('''
    SELECT name
    FROM students
    WHERE student_id IN (
        SELECT student_id
        FROM enrollments
        GROUP BY student_id
        HAVING COUNT(*) > 1
    )
''')

for row in cursor.fetchall():
    print(f"{row[0]}")
    
conn.close()