"""import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'-
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"An exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)




    def createaccount(self):
        info = {
            "name": input("Tell your name :-"),
            "Age": int(input("Tell your age :-")),
            "email": input("Tell your email :-"),
            "Pin": int(input("Tell your pin :-")),
            "Account.No" : Bank.__accountgenerate(),
            "Bank Balance" : 0
        }
        if info['Age'] < 18 or len(str(info['Pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been create successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Tell your pin as well :-"))

        userdata = [i for i in Bank.data if i ['Account.No'] == accnumber and i['Pin'] == pin]

        if not userdata:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to deposit :-"))
            if amount > 15000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 15000")

            else:
                userdata[0]['Bank Balance'] += amount
                Bank.__update()
                print("Amount depodited successfully")


    def withdrawmoney(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Tell your pin as well :-"))

        userdata = [i for i in Bank.data if i ['Account.No'] == accnumber and i['Pin'] == pin]

        if not userdata:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to withdraw :-"))
            if userdata[0]['Bank Balance'] < amount:
                print("Sorry you dont have that much money")

            else:
                userdata[0]['Bank Balance'] -= amount
                Bank.__update()
                print("Amount withdraw successfully")

   def showdetails(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Tell your pin as well :-"))

        userdata = [i for i in Bank.data if i ['Account.No'] == accnumber and i['Pin'] == pin]
        print("Your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnumber = input("Please tell your account number :-")
        pin = int(input("Tell your pin as well :-"))

        userdata = [i for i in Bank.data if i ['Account.No'] == accnumber and i['Pin'] == pin]

        if not userdata:
            print("No such user found")

        else:
            print("You cannot change the age, account number, bank balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("Please tell new name or press enter :"),
                "email": input("Please tell your new Email or press enter to skip"),
                "Pin": input("Enter new pin or press enter to skip")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']

            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']

            if newdata["Pin"] == "":
                newdata["Pin"] = userdata[0]['Pin']


            newdata['Age'] == userdata[0]['Age']
            newdata['Account.No'] == userdata[0]['Account.No']
            newdata['Bank Balance'] == userdata[0]['Bank Balance']

            if type(newdata['Pin']) == str:
                newdata['Pin'] = int(newdata['Pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue

            else:
                userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully")


user = Bank()



print("Press 1 for creating a account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting your account")

check = int(input("Tell your response :-"))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()
"""




