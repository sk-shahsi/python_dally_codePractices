# """
# Creat a simple number guessing game.
# The user gets 10 chance to guess a nimber.
# if the use guesses the number before 10 chance, stop asking the number from the user,say Congrats and end the game
# if the user never guess the number, ask then 10 times and then end the game!!
# """
# num =1
# print("Welcome to the guessing game. We have a number that need to be guess. you have 10 attempts.")
# print("The secret number is between 1 and 50")
# secret_number =25
# attempts=10
#
# while num <=10:
#     user_number = int(input("Enter your guess:"))
#     if user_number == secret_number:
#         print("Congrats, you guess is correct!!")
#       break
#     else:
#     if user_number < secret_number:
#          print("Your guess is too low")
#     else:
#
#
#     print("your guess is wrong!")
#
#  num +=1