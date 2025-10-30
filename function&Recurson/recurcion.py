"""
Recurcion is a process in which a function calls itself till a certain condition is not met
"""
def fact(num):
   fact = 1
   while num > 1:
       fact *= num
       num -=1
   return fact
n=4
print(f"Factorial of {n} is {fact(n)}")
