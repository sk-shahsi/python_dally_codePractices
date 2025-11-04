# a = 10
# b = 20
# print(a+b)
#
# s1 = "hello"
# s2 = "Hi"
#
# print(s1+s2)


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self) :
        return self.length * self.breadth

r1 = Rectangle(5, 3)
r2 = Rectangle(8,6)

print(r1.area())
print(r2.area())

# print(r1 + r2)