student_1={"English","Math","CS","Physics","Science"}
student_2={"English","Biology","Chemistry","Physics"}

#commin subject
common_subjects=student_1.intersection(student_2)
print(common_subjects)

commonSubjects=student_1 & student_2
print(commonSubjects)

#All subjects are known
all_subjects=student_1.union(student_2)
print(all_subjects)

allSubjects=student_1 | student_2
print(allSubjects)

days={"mon","tues","wed","thu","fri","sat","sun"}
weakends={"sat","sun"}
print(days & weakends)
weekdays=days.difference(weakends)
print(weekdays)