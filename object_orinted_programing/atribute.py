class Student:
    pass

student = Student()
student1 = Student()

student1.name= "jon"
student1.roll=120



print(student1.roll)
print(student1.name)

# print(student.roll)
# print(student.name)

help(Student)
print(student1.__dict__)
print(student.__dict__)