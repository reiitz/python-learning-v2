from student import Student

def test_student_creation():
    """Test that a student is created with correct attributes"""
    student = Student("Chiamaka", 16)

    assert student.name == "Chiamaka"
    assert student.age == 16
    assert student.grades == []

def test_add_grade():
    """Test adding grades to a student"""
    student = Student("Tunde", 17)
    student.add_grade(85)
    student.add_grade(90)

    assert len(student.grades) == 2
    assert 85 in student.grades
    assert 90 in student.grades

def test_calculate_average():
    """Test average calculation"""
    student = Student("Amara", 16)
    student.add_grade(80)
    student.add_grade(90)
    student.add_grade(70)

    # Average of 80, 90, 70 is 80
    assert student.calculate_average() == 80

def test_is_passing():
    """Test passing status (average >= 70)"""
    passing_student = Student("Kemi", 17)
    passing_student.add_grade(75)
    passing_student.add_grade(80)

    failing_student = Student("Bola", 16)
    failing_student.add_grade(60)
    failing_student.add_grade(65)

    assert passing_student.is_passing() == True
    assert failing_student.is_passing() == False