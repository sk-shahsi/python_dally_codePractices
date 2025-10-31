"""
1.Compile time error => Syntex error & Indentation Error
2. Exception => error during execution

"""
# age =24
# if age >= 18:
#   print(age)

# print("hello world")
# x=10
# result=x+y

#How to handle exception => try-exception block
num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))
try:
    result=num1/num2
    print(result)

except ZeroDivisionError:
    print("The denominate cannot be 0")

except IndexError:
    print("Index out of range")