import json
from pathlib import Path
import random
import string

class Bank:
    data = []
    __database = "data.json"
   
    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"An error occurred as {err}") 
    
    @classmethod
    def __updatedata(cls):
        with open(cls.__database, "w") as fs:
            fs.write(json.dumps(cls.data))
    
    @classmethod
    def __generate_account_number(cls):
        alpha = random.choices(string.ascii_letters, k=5)
        number = random.choices(string.digits, k=5)
        account_id = alpha + number
        random.shuffle(account_id)
        return "".join(account_id)
        
    def create_account(self):
        info = {
            "name": input("Tell your name: - "),
            "age": int(input("Tell your age: - ")),
            "gender": input("Tell your gender: - "),
            "phone": int(input("Tell your phone number: - ")),
            "gmail": input("Tell your Gmail: - "),
            "AccountNo": Bank.__generate_account_number(),
            "pin": input("Tell your pin: - "),
            "balance": 0
        }
        
        if info['age'] < 18:
            print("Sorry, you cannot create the account.")
        elif not len(str(info['phone'])) == 10:
            print("Invalid phone number.")
        elif not len(str(info['pin'])) == 4:
            print("Invalid pin.")
        else:
            Bank.data.append(info)
            Bank.__updatedata()
            print(f"Your account number is {info['AccountNo']}")
    
    def deposit_money(self):
        account_no = input("Tell your account number: - ")
        pin = input("Tell your pin: - ")
        userdata = None
        
        for i in Bank.data:
            if i["AccountNo"] == account_no and i["pin"] == pin:
                userdata = i
                break
        
        if userdata is None:
            print("No such account found.")
        else:
            amount = float(input("How much you want to deposit? "))
            if amount < 0:
                print("Sorry, you cannot deposit a negative amount.")
            elif amount > 20000:
                print("Sorry, you cannot deposit more than 20,000.")
            else:
                userdata['balance'] += amount
                Bank.__updatedata()
                print("Amount deposited successfully.")
    
    def withdraw_money(self):
        account_no = input("Tell your account number: - ")
        pin = input("Tell your pin: - ")
        userdata = None
        
        for i in Bank.data:
            if i["AccountNo"] == account_no and i["pin"] == pin:
                userdata = i
                break
        
        if userdata is None:
            print("No such account found.")
        else:
            amount = float(input("How much you want to withdraw? "))
            if amount < 0:
                print("Sorry, you cannot withdraw a negative amount.")
            elif amount > userdata['balance']:
                print("Insufficient balance.")
            else:
                userdata['balance'] -= amount
                Bank.__updatedata()
                print("Amount withdrawn successfully.")
    
    def account_details(self):
        account_no = input("Tell your account number: - ")
        pin = input("Tell your pin: - ")
        userdata = None
        
        for i in Bank.data:
            if i["AccountNo"] == account_no and i["pin"] == pin:
                userdata = i
                break
        
        if userdata is None:
            print("No such account found.")
        else:
            print("Account details: ")
            print(f"Name: {userdata['name']}")
            print(f"Age: {userdata['age']}")
            print(f"Gender: {userdata['gender']}")
            print(f"Phone: {userdata['phone']}")
            print(f"Gmail: {userdata['gmail']}")
            print(f"Account No: {userdata['AccountNo']}")
            print(f"Balance: {userdata['balance']}")
    
    def update_details(self):
        account_no = input("Tell your account number: - ")
        pin = input("Tell your pin: - ")
        userdata = None
        
        for i in Bank.data:
            if i["AccountNo"] == account_no and i["pin"] == pin:
                userdata = i
                break
        
        if userdata is None:
            print("No such account found.")
        else:
            userdata['name'] = input("Update your name: - ")
            userdata['phone'] = int(input("Update your phone number: - "))
            userdata['gmail'] = input("Update your Gmail: - ")
            Bank.__updatedata()
            print("Your details have been updated successfully.")
    
    def delete_account(self):
        account_no = input("Tell your account number: - ")
        pin = input("Tell your pin: - ")
        userdata = None
        
        for i in Bank.data:
            if i["AccountNo"] == account_no and i["pin"] == pin:
                userdata = i
                break
        
        if userdata is None:
            print("No such account found.")
        else:
            Bank.data.remove(userdata)
            Bank.__updatedata()
            print("Your account has been deleted successfully.")

print("""Press the following for your task: 
        Press 1 for creating a bank account.
        Press 2 for depositing money in your account.
        Press 3 for withdrawing money from your account.
        Press 4 for account details.
        Press 5 for updating your details.
        Press 6 for deleting the account.
        Press 0 to exit.""")

check = input("Tell your response: - ")

user = Bank()

if check == "1":
    user.create_account()
elif check == "2":
    user.deposit_money()
elif check == "3":
    user.withdraw_money()
elif check == "4":
    user.account_details()
elif check == "5":
    user.update_details()
elif check == "6":
    user.delete_account()
elif check == "0":
    print("Goodbye!")
