correct_password="java"
while True:
    user_password =input("Enter your password: ")
    if user_password == correct_password:
        print("Congratulations, you have entered the correct password")
        break

    else:
        print("wrong password, try again.")

print("Logged in !!!!!!!!")