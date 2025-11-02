#class variable defind as class level
"""
same copy of the class
"""
# CLass methode
class Welcome:
    @classmethod
    def greet(self):
        print("Hello")

w1 = Welcome()
w1.greet()
print("Welcome")

#static methode
