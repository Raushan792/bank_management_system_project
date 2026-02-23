import streamlit as st
import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        st.error(f"Error loading database: {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        accid = alpha + num + spchar
        random.shuffle(accid)
        return "".join(accid)

    def createaccount(self, name, age, email, pin):
        info = {
            "name": name,
            "Age": age,
            "email": email,
            "Pin": pin,
            "Account.No": Bank.__accountgenerate(),
            "Bank Balance": 0
        }
        if age < 18 or len(str(pin)) != 4:
            return None
        else:
            Bank.data.append(info)
            Bank.__update()
            return info

    def depositmoney(self, accnumber, pin, amount):
        userdata = [i for i in Bank.data if i['Account.No'] == accnumber and i['Pin'] == pin]
        if not userdata:
            return False, "No such user found"
        if amount > 15000 or amount <= 0:
            return False, "You can deposit only upto 15000 at a time"
        userdata[0]['Bank Balance'] += amount
        Bank.__update()
        return True, userdata[0]['Bank Balance']

    def withdrawmoney(self, accnumber, pin, amount):
        userdata = [i for i in Bank.data if i['Account.No'] == accnumber and i['Pin'] == pin]
        if not userdata:
            return False, "No such user found"
        if userdata[0]['Bank Balance'] < amount:
            return False, "Not enough balance"
        userdata[0]['Bank Balance'] -= amount
        Bank.__update()
        return True, userdata[0]['Bank Balance']

    def showdetails(self, accnumber, pin):
        userdata = [i for i in Bank.data if i['Account.No'] == accnumber and i['Pin'] == pin]
        if not userdata:
            return None
        return userdata[0]

    def updatedetails(self, accnumber, pin, name, email, new_pin):
        userdata = [i for i in Bank.data if i['Account.No'] == accnumber and i['Pin'] == pin]
        if not userdata:
            return False
        if name:
            userdata[0]['name'] = name
        if email:
            userdata[0]['email'] = email
        if new_pin:
            userdata[0]['Pin'] = new_pin
        Bank.__update()
        return True

    def deleteaccount(self, accnumber, pin):
        userdata = [i for i in Bank.data if i['Account.No'] == accnumber and i['Pin'] == pin]
        if not userdata:
            return False
        Bank.data.remove(userdata[0])
        Bank.__update()
        return True


# ============= Streamlit UI =============
bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Menu", [
    "Create Account", "Deposit Money", "Withdraw Money",
    "Show Details", "Update Details", "Delete Account"
])

if menu == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4 digits)", type="password")

    if st.button("Create"):
        if name and email and pin:
            acc = bank.createaccount(name, age, email, int(pin))
            if acc:
                st.success("✅ Account created successfully!")
                st.json(acc)
            else:
                st.error("❌ Age must be 18+ and PIN must be 4 digits")
        else:
            st.warning("⚠️ Please fill all fields")

elif menu == "Deposit Money":
    st.subheader("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        ok, msg = bank.depositmoney(acc, int(pin), amt)
        if ok:
            st.success(f"✅ Deposited successfully! New Balance: {msg}")
        else:
            st.error(f"❌ {msg}")

elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        ok, msg = bank.withdrawmoney(acc, int(pin), amt)
        if ok:
            st.success(f"✅ Withdrawn successfully! New Balance: {msg}")
        else:
            st.error(f"❌ {msg}")

elif menu == "Show Details":
    st.subheader("Show Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.showdetails(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("❌ No such user found")

elif menu == "Update Details":
    st.subheader("Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    newpin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        ok = bank.updatedetails(acc, int(pin), name, email, int(newpin) if newpin else None)
        if ok:
            st.success("✅ Details updated successfully")
        else:
            st.error("❌ No such user found")

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        ok = bank.deleteaccount(acc, int(pin))
        if ok:
            st.success("✅ Account deleted successfully")
        else:
            st.error("❌ No such user found")




















