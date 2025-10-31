
balance = 0.0
def checking_balance():
    print(f"Your Current Balance is {balance}")
    print("===========================")



def deposit(amount):
    global balance
    if amount > 0:
      balance += amount
    else:
        print("Cannot deposit a negative or zero amount")
        print("===========================")
    # print(f"Depositing an amount")

def withdraw(amount):
    global balance
    if amount <=0:
        print("Cannot withdraw a negative or zero amount")
        print("===========================")
    elif amount > balance:
        print("Cannot withdraw. Insufficient balance")
        print("===========================")
    else:
        balance -= amount
  #  print("Withdrawing a amount")



def kyc(**docs):
    global  kyc
    kyc.update(docs)

if __name__ == "__main__":
    print("Welcome to Simple Banking App")

while True:
    print("1. Check your balance")
    print("2. Deposit an amount")
    print("3. Withdraw an amount")
    print("4. Quit")
    choice = input("Enter your choice: ")
    print("===========================")
    if choice == '1':
        checking_balance()
    elif choice == '2':
        amt = float(input("Enter the amount to deposit: "))
        print("===========================")
        deposit(amt)

    elif choice == '3':
        amt =float(input("Enter the amount to withdraw: "))
        print("===========================")
        withdraw(amt)

    elif choice == '4':
        break

    else:
        print("Invalid choice")
        print()

print("Thank you for banking with us")