# Main program for controlling a Bank made up of Accounts

from bank import *

# Create an instance of the Bank
bank = Bank("9 to 5", "123 Main Street, Anytown, USA", "(650) 555-1212")

# Main code
while True:
    print()
    print("To open a new account, press o")
    print("To close an account, press c")
    print("To get an account balance, press b")
    print("To make a deposit, press d")
    print("To make a withdrawal, press w")
    print("To get bank information, press i")
    print("To show all accounts, press s")
    print("To quit, press q")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]
    print()

    try:
        if action == "o":
            bank.open_account()
        elif action == "c":
            bank.close_account()
        elif action == "b":
            bank.get_balance()
        elif action == "d":
            bank.deposit()
        elif action == "w":
            bank.withdraw()
        elif action == "i":
            bank.get_info()
        elif action == "s":
            bank.show()
        elif action == "q":
            break
    except AbortTransaction as error:
        # Print the error message
        print(error)

print("Done")
