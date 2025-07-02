import random 
import json
import string
from pathlib import Path




class Bank:
    database= 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print("File not found, creating a new one.")
    except Exception as err:
        print(f"an exception occurred: {err}")
    
    @staticmethod
    def update(data):
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data,))

    def createaccount(self):
        data = {
            "name": input("Enter your name :- "),
            "age": input("Enter your age :- "),
            "email": input("Enter your email :- "),
            "pin": input("Enter your pin :- "),
            "accountNo": 1234,
            "balance": 0,
        }
        if int(data['age']) < 18 or len(str(data['pin'])) != 4:
            print("You are not eligible to create an account")
        else:
            print("Account created successfully")
            for i in data:
                print(f"{i} : {data[i]}")
            print(("please note down your account number"))
            
            Bank.update(data)

user = bank()

print("press 1 for creating an account")
print("press 2 Diposit money in the bank")
print("press 3 Withdraw money from the bank")
print("press 4 for the detail")
print("press 5 update the details")
print("press 6 for delete the account")

check = int(input("Enter your choice: "))

if check == 1:
    user.CreateAccount()