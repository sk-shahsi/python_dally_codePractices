def func(**kwargs):
    print(kwargs)


func(x=10,y=20)

def student_details(sid,sname,**marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exam")
    else:
      percentage=sum(marks.values())/len(marks)
      print(f"")