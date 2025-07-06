import json
import random
import string
from pathlib import Path
from datetime import datetime


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            print("File not found, creating a new one.")
    except Exception as err:
        print(f"An exception occurred: {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def __accountgenerator(cls):
        return ''.join(random.choices(string.digits, k=6))

    def CreateAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": input("Enter your age: "),
            "email": input("Enter your email: "),
            "pin": input("Enter your 4-digit pin: "),
            "accountNo": self.__accountgenerator(),
            "balance": 0,
            "created_at": datetime.now().isoformat(),
            "transactions": []
        }
        if not info['age'].isdigit() or int(info['age']) < 18:
            print("You are not eligible to create an account.")
        elif not info['pin'].isdigit() or len(info['pin']) != 4:
            print("Invalid PIN. Must be 4 digits.")
        else:
            print("Account created successfully.")
            for key, val in info.items():
                print(f"{key}: {val}")
            print("Please note down your account number.")
            self.data.append(info)
            self.__update()

    def __get_user(self, accnumber, pin):
        return [i for i in self.data if i['accountNo'] == accnumber and i['pin'] == pin]

    def __log_transaction(self, user, type_, amount):
        user['transactions'].append({
            'type': type_,
            'amount': amount,
            'date': datetime.now().isoformat()
        })

    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = self.__get_user(accnumber, pin)

        if not userdata:
            print("Sorry, no data found.")
        else:
            try:
                amount = int(input("Enter deposit amount: "))
                if amount > 10000 or amount <= 0:
                    print("Amount must be between 1 and 10000.")
                else:
                    userdata[0]["balance"] += amount
                    self.__log_transaction(userdata[0], "deposit", amount)
                    self.__update()
                    print(f"Your new balance is {userdata[0]['balance']}")
            except ValueError:
                print("Please enter a valid amount.")

    def withdrawmoney(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = self.__get_user(accnumber, pin)

        if not userdata:
            print("Sorry, no data found.")
        else:
            try:
                amount = int(input("Enter withdrawal amount: "))
                if userdata[0]["balance"] < amount:
                    print("Insufficient balance.")
                else:
                    userdata[0]["balance"] -= amount
                    self.__log_transaction(userdata[0], "withdraw", amount)
                    self.__update()
                    print(f"Your new balance is {userdata[0]['balance']}")
            except ValueError:
                print("Please enter a valid amount.")

    def showdetails(self):
        account = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = self.__get_user(account, pin)

        if not userdata:
            print("Sorry, no data found.")
        else:
            for key, val in userdata[0].items():
                if key != "transactions":
                    print(f"{key}: {val}")

    def showtransactions(self):
        account = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = self.__get_user(account, pin)

        if not userdata:
            print("Sorry, no data found.")
        else:
            print("Transaction History:")
            for txn in userdata[0]["transactions"]:
                print(f"{txn['date']} - {txn['type']} - Rs. {txn['amount']}")

    def updatedetails(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = self.__get_user(accnumber, pin)

        if not userdata:
            print("Sorry, no data found.")
        else:
            user = userdata[0]
            print("You cannot change account number, age or balance.")

            new_name = input("Enter new name (or press Enter to keep current): ") or user['name']
            new_email = input("Enter new email (or press Enter to keep current): ") or user['email']
            new_pin = input("Enter new 4-digit pin (or press Enter to keep current): ") or user['pin']

            if not new_pin.isdigit() or len(new_pin) != 4:
                print("Invalid PIN. Must be 4 digits.")
                return

            user['name'] = new_name
            user['email'] = new_email
            user['pin'] = new_pin
            self.__update()
            print("Account details updated successfully.")

    def deleteaccount(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = self.__get_user(accnumber, pin)

        if not userdata:
            print("Sorry, no data found.")
        else:
            confirm = input("Are you sure you want to delete your account? (y/n): ")
            if confirm.lower() == 'y':
                self.data.remove(userdata[0])
                self.__update()
                print("Account deleted successfully.")
            else:
                print("Account deletion cancelled.")


if __name__ == '__main__':
    user = Bank()
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Details")
        print("5. Show Transaction History")
        print("6. Update Details")
        print("7. Delete Account")
        print("8. Exit")

        try:
            choice = int(input("\nEnter your choice (1-8): "))
            if choice == 1:
                user.CreateAccount()
            elif choice == 2:
                user.depositmoney()
            elif choice == 3:
                user.withdrawmoney()
            elif choice == 4:
                user.showdetails()
            elif choice == 5:
                user.showtransactions()
            elif choice == 6:
                user.updatedetails()
            elif choice == 7:
                user.deleteaccount()
            elif choice == 8:
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")
