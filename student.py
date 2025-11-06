class Student:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.grades = []

  def add_grade(self, grade):
      self.grades.append(grade)

  def is_passing(self):
    return self.calculate_average() >= 70

  def calculate_average(self):
      if len(self.grades) == 0:
          return 0
      return sum(self.grades) / len(self.grades)

# Create two student objects (two peaches from the same seed)
student1 = Student("Chiamaka", 16)
student2 = Student("Tunde", 17)

# Add grades to Chiamaka
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

# Add grades to Tunde
student2.add_grade(92)
student2.add_grade(88)

# Calculate averages
print(f"{student1.name}'s average: {student1.calculate_average()}")
print(f"{student2.name}'s average: {student2.calculate_average()}")
student1.add_grade(95)
print(f"{student1.name}'s new average: {student1.calculate_average()}")
print(f"Is {student1.name} passing? {student1.is_passing()}")
print(f"Is {student2.name} passing? {student2.is_passing()}")