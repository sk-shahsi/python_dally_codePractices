subject1=int(input("Enter your first Subject Scorred Mark "))
subject2=int(input("Enter your Second Subject Scoerd Mark "))
subject3=int(input("Enter your Third Subject Scored Mark "))

total_Percentage=(100*(subject1+subject2+subject3))/100

print("total Percentage is ",total_Percentage)
if(total_Percentage>=40):
    print("You are passed")
    print("Congratulation !!!!")

else:
     print("you are faield")