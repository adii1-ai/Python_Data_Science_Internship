# steps
# 1. User enter Amount
# 2. Select payment method
# 3. Gateway validates payment
# 4. Bank process transaction
# 5. Success OR failure message\

# =======================================


class BankAccount:
    def __init__(self,pin,balance=0):
        # create instance variables and stored in a object
        self.balance=balance
        self.pin=pin


        # method to verify pin 
    def verifyPin(self,user_pin):
            if user_pin!=self.pin:
                raise ValueError("Invalid Pin ...")
            return True
        

    def reset_pin(self,old_pin,new_pin):
            self.verifyPin(old_pin)
            self.pin=new_pin
            print("Pin reset.....Done")



class ATM:
    def __init__(self,account):
       
        self.account=account

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Invalid Withdraw Amount...")
        if amount>self.account.balance:
            raise ValueError("Insufficient Balance....")
        
        self.account.balance-=amount
        print("Money Withdrawm Successfully....")
        print("Your Current Balance Is ", self.account.balance)
            

    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Invalid Deposit Amount...")
        self.account.balance+=amount
        print("Deposit Amount Successfully....")
        print("Your Current Balance Is ", self.account.balance)

    

    def checkbalance(self):
         print("Your Current Balance Is ", self.account.balance)


account=BankAccount("12345",1000000)

atm=ATM(account)

try:
    your_pin=input('Enter Your Pin....')
    account.verifyPin(your_pin)

    while True:

        print("\n=============== ATM MENU ===================\n")
        print(f"1. WIthdraw\n2. Deposit\n3. Check balance\n4. Reset Pin\n5. Exit")

        
        choice=input("Choose Option...")

        match choice:
            case "1":
                amount=int(input("Enter Withdraw Amount"))
                atm.withdraw(amount)

            case "2":
                amount=int(input("Enter Deposit Amount"))
                atm.deposit(amount)

            case "3":
                atm.checkbalance()
            
            case "4":
                old_pin=input('enter your current pin')
                new_pin=input("enter Your new pin")
                account.reset_pin(old_pin,new_pin)
            
            case "5":
                print("Thanks Bro.....")
            
            case _:
                print("Invalid Option...")

except Exception as e:
     print("Error Occurred :  ", e)