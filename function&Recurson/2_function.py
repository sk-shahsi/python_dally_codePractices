# a=int(input("enter the number which you wan to change in Celcious: "))

# f=5 * (a-32) /9
# print(f)

def change_inTo_Celcious(a):
    return 5 * (a-32) /9


a=int(input("give a number to change in celcious: "))
c=change_inTo_Celcious(a)
print(f"Tempratur is {round(c,2)}°C")