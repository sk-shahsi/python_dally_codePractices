import pickle

student = {'student1':{'roll':101,'name':'jon','percent':78.5},
           'student2':{'roll':102,'name':'carlo','percent':80.5},
           'student3':{'roll':103,'name':'jack','percent':70.5},
           'student4':{'roll':104,'name':'ram','percent':88.5}}

print(student, type(student))
print(type(student))

#Serilization
with open("student.bin","wb") as fh:
    for students in student:
      pickle.dump(students,fh)


#Deserilization
with open("student.bin","bw") as fh:
    while True:
        try:
            date = pickle.load(fh)
            print(date,type(date))
        except EOFError:
            print("Done !")
            break


