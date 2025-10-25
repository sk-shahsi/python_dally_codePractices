j=int(input("give a number to find factorial : "))

product=1
for i in range(1, j+1):
    product= product*i

print(f"the factorial of {j} is {product}")