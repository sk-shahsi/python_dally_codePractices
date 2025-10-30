#Local variable = created within a function
# Global variable = created outside of all the function

#age = 18
def fun():
    age =20
    print(f"Inside the function :{age}")
 #workin as global variable
age = 30
fun()
print(f"Out side of function: {age}")
