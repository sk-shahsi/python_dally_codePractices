
mark1=int(input("enter firs Subject Marks Scored "))
mark2=int(input("enter Second Subject Marks Scored "))
mark3=int(input("enter Third Subject Marks Scored "))

total_percentage=(100*(mark1+mark2+mark3))/100
if(total_percentage>=40 and mark1>=30 and mark2>=30 and mark3>=30):
    print("you are pass this exam Congratulation !!! Percentage is",total_percentage)


else:
    print("you are failed")