def checking_balance():
    print(f"Your Current Balance is {balance}")



def deposit(amount):
    global balance
    if amount > 0:
      balance += amount
    else:
        print("Cannot deposit a negative or zero amount")
    # print(f"Depositing an amount")

def withdraw(amount):
    global balance
    if amount <=0:
        print("Cannot withdraw a negative or zero amount")
    elif amount > balance:
        print("Cnnot withdraw. Insufficent balance")
    else:
        balance -= amount
  #  print("Withdrawing a amount")


balance = 0.0

while True:
    print("1. Check your balance")
    print("2. Deposit an amount")
    print("3. Withdraw an amount")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        checking_balance()
    elif choice == '2':
        amt = float(input("Enter the amount to deposit: "))
        deposit(amt)

    elif choice == '3':
        amt =float(input("Enter the amount to withdraw: "))
        withdraw(amt)

    elif choice == '4':
        break

    else:
        print("Invalid choice")

print("Thank you for banking with us")