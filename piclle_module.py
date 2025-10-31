import json

student = {'student':{"name":'jon',"roll":123,'sport':True},
           'student1':{"name":'ram',"roll":569,'sport':False},

           }
# with open('student.txt', 'wt') as fh:
#     fh.write(str(student))

with open("student.txt","rt") as f:
    contant = f.read()

    print(contant)
    out = dict(contant)
    print(out)
