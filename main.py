import random 
import json
import string
from pathlib import Path

from matplotlib import use
from matplotlib.pylab import rand
from regex import B
from stripe import Account




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
        num = random.choices(string.digits, k=4)
        # spchar= random.choices("@!#%&", k= 1)
        id =  num
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
    
    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        
        userdata = [ i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]            

        if userdata == False:
            print("sorry no data  found")
        else:
            amount = int(input("how much money you want to deposit: "))
            if amount > 10000 or amount <= 0:
                print("You can not deposit more than 10000 at a time")
                
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print(f"Your new balance is {userdata[0]['balance']}")
  
    def withdrawmoney(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        
        userdata = [ i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]            

        if userdata == False:
            print("sorry no data  found")
        else:
            amount = int(input("how much money you want to deposit: "))
            if userdata[0]["balance"] < amount:
                print("You do not have sufficient balance to withdraw this amount")
                
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print(f"Your new balance is {userdata[0]['balance']}")


    def showdetails(self):
        account = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        userdata = [i for i in Bank.data if i['accountNo'] == account and i['pin'] == pin]
        
        if not userdata:
            print("Sorry, no data found")
        else:
            for key in userdata[0]:
                print(f" {key} : {userdata[0][key]}")
        

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
    
if check == 2:
    user.depositmoney()
    
if check == 3:
    user.withdrawmoney()
    
    
if check == 4:
    user.showdetails()