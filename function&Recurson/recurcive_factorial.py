input=int(input("Give a number to find factorial: "))
def fact_rec(num):
    if num == 1:
        return 1
    else:
        fact = num * fact_rec(num - 1)
        return fact
print(f"The factorial of {input} is {fact_rec(input)}")