# Bank that manages a dictionary of Account objects

from account import *


class Bank:
    def __init__(self, hours, address, phone):
        self.accounts_dict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        account_number = input("What is your account number? ")
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        if account_number not in self.accounts_dict:
            raise AbortTransaction("There is no account " + str(account_number))
        return account_number

    def get_account(self):
        account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[account_number]
        self.ask_for_valid_password(account)
        return account

    def ask_for_valid_password(self, account):
        password = input("Please enter your password: ")
        account.check_password_match(password)

    def create_account(self, name, starting_amount, password):
        account = Account(name, starting_amount, password)
        account_number = self.next_account_number
        self.accounts_dict[account_number] = account
        # Increment for next account to prepare for next account to be created
        self.next_account_number = self.next_account_number + 1
        return account_number

    def open_account(self):
        print("*** Open account ***")
        name = input("What is your name? ")
        starting_amount = input("How much money to start your account? ")
        password = input("What password would you like to use for this account? ")
        account_number = self.create_account(name, starting_amount, password)
        print("Your new account number is:", account_number)

    def close_account(self):
        print("*** Close account ***")
        account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[account_number]
        self.ask_for_valid_password(account)
        balance = account.get_balance()
        print("You had", balance, "in your account, which is being returned to you.")
        del self.accounts_dict[account_number]
        print("Your account is now closed.")

    def get_balance(self):
        print("*** Get balance ***")
        account = self.get_account()
        balance = account.get_balance()
        print("Your balance is:", balance)

    def deposit(self):
        print("*** Deposit ***")
        account = self.get_account()
        deposit_amount = input("Please enter the amount to deposit: ")
        balance = account.deposit(deposit_amount)
        print("Deposited:", deposit_amount)
        print("Your new balance is:", balance)

    def withdraw(self):
        print("*** Withdraw ***")
        account = self.get_account()
        withdraw_amount = input("Please enter the amount to withdraw: ")
        balance = account.withdraw(withdraw_amount)
        print("Withdrawn", withdraw_amount)
        print("Your new balance is:", balance)

    def get_info(self):
        print("Hours:", self.hours)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("We currently have", len(self.accounts_dict), "account(s) open")

    # Special method for bank administrator only
    def show(self):
        print("*** Show ***")
        print("This would typically require an admin password")
        for account_number in self.accounts_dict:
            account = self.accounts_dict[account_number]
            print("Account:", account_number)
            account.show()
