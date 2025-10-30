"""
def add(a):
    return a + 1
res = add(1)
print(res)
"""

fun = lambda a : a + 1
res = fun(2)
print("one arg example: ",res)

fun = lambda a,b:a+b
res = fun(2,3)
print("Two args function: ",res)