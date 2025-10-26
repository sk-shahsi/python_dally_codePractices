#Count down  from 10 to 1 ( 1 include)
for i in range(10, 0, -1):
    print(i)
print("Happy Nwe Year!!!!")


#range(start, stop)=> step=1 by defult

for i in range(1, 10):
     print(i)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#range(stop) =>0 to -1
for i in range(5):
    print(i)


profit=[10,5,0,90,70]
for index in profit:
    print(profit.index(index),profit[index])