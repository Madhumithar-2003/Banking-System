import time

class Bank:
    
    def __init__(self,username,pan,address):
       self.username=username
       self.pan=pan
       self.address=address
       self.balance=0.0
#deposit the amount   

    def deposit(self,amount):
       self.balance=self.balance+amount
       print(f"{amount} deposited succesfully")

#withdraw the amount

    def withdraw (self,amount):
       if amount<self.balance:
          self.balance=self.balance-amount
          print(f"{amount} withdraw succesfully")
       else:
          print("Insufficient Fund...")

#Check the bank balanace
    def bankbalance (self):
          print(f"your account balance is{self.balance}")


print("Welcome to Indian Bank")
time.sleep(1)
username=input("Enter your name:")
pan=input("Enter your card number:")
address=input("Enter your address:")
print(f"Hello {username} your account is created successfully")

process=Bank(username,pan,address)

while True:
    time.sleep(0.5)
    print("\nplease select any option:")
    print("1.Deposit\n2.withdraw\n3.bankbalance\n4.Stop")
    option=int(input(" "))
    

    if option==1:
        amount=float(input("Enter deposited amount:"))
        process.deposit(amount)

    elif option==2:
        amount=float(input("Enter withdraw amount:"))
        process.withdraw(amount)

    elif option==3:
        process.bankbalance()

    elif option==4:
        print("Thaking yoy!...")
        break

    else:
        print("Invalid option")


