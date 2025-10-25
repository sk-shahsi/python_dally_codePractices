age=20
percentage=85.6
student = ["jon",20,85.6]
print(type(student))
print(student)

day_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(day_of_week[0])
print(day_of_week[5])
print(day_of_week[-1])

#slicing
l1=[1,2,3,4,5,6,7,8,9]
print(l1[1:6:1])
l2=[10,20,30,40,50,60,70,80,90]
#concationation
print(l1+l2)

#reptitation
print(l1*3)
# adds an item to the end of the list
fruits=["apple","banana","orange"]
print(fruits)

fruits.append("cherry")
print(fruits)

#insert
fruits.insert(2,"avokado")
print(fruits)

#extend
#remove
#pop
fruits.append("kewe")
print(fruits)
fruits.extend(["orange","nuts"])
print(fruits)

fruits.remove("nuts")
print(fruits)

fruits.pop(3)
print(fruits)
fruits.pop()
print(fruits)

#reversed, sort, count, membership, operation
number=[100,56,99,1,2,3,4,5,6,7,8,9]
print(number)
number.reverse()
print("Reversed order: ",number)
number.sort()
print("Sorted List: ",number)
number.sort(reverse=True)
print("reversed==true List: ",number)

num=[100,500,100,100]
#num.count(100)
print(num.count(100))
#Meembership operator
lang=["python","java","javascript"]
print("python" in lang)
print("c++" in lang)