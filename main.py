import random 
import json
import string
from pathlib import Path

from matplotlib.pylab import rand




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
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
            
            
    @classmethod
    def __accountgenerator(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar= random.choices("@!#%&", k= 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    
    

    def CreateAccount(self):
        info = {
            "name": input("Enter your name :- "),
            "age": input("Enter your age :- "),
            "email": input("Enter your email :- "),
            "pin": input("Enter your pin :- "),
            "accountNo": Bank.__accountgenerator(),
            "balance": 0,
        }
        if int(info['age']) < 18 or len(str(info['pin'])) != 4:
            print("You are not eligible to create an account")
        else:
            print("Account created successfully")
            for i in info:
                print(f"{i} : {info [i]}")
            print(("please note down your account number"))
            Bank.data.append(info)

            Bank.__update()

user = Bank()

print("press 1 for creating an account")
print("press 2 Diposit money in the bank")
print("press 3 Withdraw money from the bank")
print("press 4 for the detail")
print("press 5 update the details")
print("press 6 for delete the account")

check = int(input("Enter your choice: "))

if check == 1:
    user.CreateAccount()