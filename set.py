num={1,2,3,4,5,6,7,8,9,10,11,12,13}
nums_1={1,2,3,4,5,6,7,8,9,10,11,12,13}
#membership in set
print(0 in num)
print (1 in num)
#concation
#print(num + nums_1) #TypeError: unsupported operand type(s) for +: 'set' and 'set'

weakdays=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
weakdays1=set(weakdays)
print(weakdays1) #not mantaning order

#set are mutable
#not assigened item assignment
set_1={-1,2,0}
#set_1[0]=10    TypeError: 'set' object does not support item assignment
#add()
set_1.add(55)
print(set_1)
#remove
set_1.remove(55)
print(set_1)
#duplicate add
set_1.add(0)
print(set_1)
#descard
set_1.discard(0)
print(set_1)
