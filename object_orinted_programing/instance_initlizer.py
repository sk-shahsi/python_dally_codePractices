class Student:
     def __init__(self,name, roll, branch):
         print(f"Calling the initializer!{self}")
         self.name = name
         self.roll = roll
         self.branch = branch
     def study(self, n_hour):
         print(f"The student for{n_hour} hours a day!!")

     def sport(self, sport_name):
         print(f"The student plays {sport_name}")

student1 = Student("jon",11002,"art")

student2 = Student("caral",110023,"scince")
student2.name = "Carol"

print(student1.name,student1.roll,student1.branch)
print(student2.name,student2.roll,student2.branch)


print(student1.__dict__)
print(student2.__dict__)