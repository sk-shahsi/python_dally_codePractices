#loop with list
percent=[1,2,5,9,6,3]
for p in percent:
    print(p)


# loop with string
s1="hello"
for s in s1:
    print(s)

#dict
employee={"empid":101,"name":"jon","salary":20000}
for e in employee:
    print(e,employee[e])
    print(employee.items())


for i in employee.items():
    print(i)
    print("i ptinting ",i[0] ,i[1])