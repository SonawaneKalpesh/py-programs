class Student:
    def __init__(self, name, marks):
        self.student_name = name
        self.marks = marks

# Original object
s = Student("Alice", 85)
print("Original:", s.student_name, s.marks)

# Modify attributes
s.student_name = "Bob"
s.marks = 90
print("Modified:", s.student_name, s.marks)
