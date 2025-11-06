from student import Student

class Course:
  def __init__(self,course_name):
     self.course_name = course_name
     self.students = []

  def add_student(self, student):
      self.students.append(student)

  def get_class_average(self):
    if len(self.students) == 0:
        return 0
    
    return sum(s.calculate_average() for s in self.students) / len(self.students)
    
        # Calculate the total average of all students in the course
total = 0
   for student in self.students:
        total += student.calculate_average()


     return total / len(self.students)
  #Test it
chemistry = Course("Chemistry 101")

#Create some students and add them to the course 
student1 = Student("Chiamaka", 16)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student2 = Student("Tunde", 17)
student2.add_grade(92)
student2.add_grade(88)

student3 = Student("Amara", 16)
student3.add_grade(76)
student3.add_grade(82)

chemistry.add_student(student1)
chemistry.add_student(student2)
chemistry.add_student(student3)

print(f"Course: {chemistry.course_name}")
print(f"Class average: {chemistry.get_class_average()}")