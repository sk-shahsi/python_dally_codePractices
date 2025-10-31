import json
student = {'student':{"roll":123,'sport':True},
           'student1':{"roll":569,'sport':False},}


print(student)
print(type(student))

#dump()
with open("student_data.json","w") as fh:
    json.dump(student,fh, indent=4)