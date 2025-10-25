#prime Number which is divided by 1 or by self
n=int(input("give me a number to check prime Number : "))
for i in range(2,n):
    if(n%i)==0:
        print("not a prime Number ")
        break

else:
    print(f" yes prime Number {n}")