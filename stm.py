import pandas as pd
import numpy as np
import os
# Load user data from CSV
class ATM:
    def __init__(self):
        self.users = pd.read_csv('atmdata.csv')
        self.current_user = None

    def login(self):
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")

        user = self.users[(self.users['user_id'] == int(user_id)) & (self.users['pin'] == int(pin))]

        if not user.empty:
            self.current_user = user
            print("Login successful!")
        else:
            print("Invalid credentials. Please try again.")

    def check_balance(self):
        if self.current_user is not None:
            balance = self.current_user['balance'].values[0]
            print(f"Your balance is ${balance:.2f}")
        else:
            print("Please log in first.")

    def deposit(self, amount):
        if self.current_user is not None:
            self.current_user['balance'] += amount
            self.users.to_csv('users.csv', index=False)
            print(f"Deposited ${amount:.2f}")
        else:
            print("Please log in first.")

    def withdraw(self, amount):
        if self.current_user is not None:
            balance = self.current_user['balance'].values[0]
            if balance >= amount:
                self.current_user['balance'] -= amount
                self.users.to_csv('users.csv', index=False)
                print(f"Withdrew ${amount:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Please log in first.")

    def transfer(self, to_user_id, amount):
        if self.current_user is not None:
            to_user = self.users[self.users['user_id'] == int(to_user_id)]

            if not to_user.empty:
                balance = self.current_user['balance'].values[0]
                if balance >= amount:
                    self.current_user['balance'] -= amount
                    to_user['balance'] += amount
                    self.users.to_csv('users.csv', index=False)
                    print(f"Transferred ${amount:.2f} to user {to_user_id}.")
                else:
                    print("Insufficient balance.")
            else:
                print("Recipient user not found.")
        else:
            print("Please log in first.")

    def quit(self):
        self.current_user = None
        print("Logged out. Goodbye!")

if __name__ == "__main__":
    atm = ATM()
    os.system('cls')
    while True:
        
        print("\n\t\t\t\t\tATM MENU:")
        print("---------------------------------------------------------------------------------------------------------------")
        print()
        print("1. Login")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Quit")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            os.system('cls')
            atm.login()
        elif choice == '2':
            os.system('cls')
            atm.check_balance()
        elif choice == '3':
            os.system('cls')
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '4':
            os.system('cls')
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '5':
            os.system('cls')
            to_user_id = input("Enter recipient's User ID: ")
            amount = float(input("Enter transfer amount: "))
            atm.transfer(to_user_id, amount)
        elif choice == '6':
            os.system('cls')
            atm.quit()
            break
        else:
            print("Invalid choice. Please try again.")
