#write a program to simulate a roll a dice/dice
# A die has 6 face with number 1 to 6 written on them
# the program should randomaly prints a number between 1 and 6


import random
print("Welcome to the game of rolling a dice")
while True:
    choice = input("Press 'Enter' to roll thr dice or 'q' to quit: ")
    if choice == "q":
        print("Thank you for playing")
        break
    elif choice =='':
        number =random.randint(1,6)
        print("You rolled", number)
    else:
        print("Invalid input")




