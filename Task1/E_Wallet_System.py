# Problem Statement :-

# You are building an **E-Wallet application** that allows users to manage their money digitally.
# The wallet should support adding money, spending money, and checking the balance.

# =========================================

# Requirements:-

# 1. Initialize the wallet balance with **₹50,000**
# 2. Display a menu with the following options:
#     - Add money
#     - Spend money
#     - Check balance
#     - Exit
# 3. Use **separate functions** for:
#     - Adding money
#     - Spending money
# 4. Avoid code duplication
# 5. Use meaningful function and variable names
# 6. Convert user input to **lowercase** to avoid input errors
# 7. Update and display the **wallet balance after every transaction**
# 8. Keep the program running until the user selects **Exit**

# ======================================

# Constrains:-

# - Do not use global variables inside functions
# - Do not allow:
#     - Negative amounts
#     - Spending more than available balance

# ======================================

# Code

def deposit(balance):
    deposit_amt = int(input("Enter the Deposit Amount: "))
    if(deposit_amt<=0):
        print("Transaction Failed...\nInvalid Deposit Amount..\nPlease Enter Valid Amount.")
        print("                             ")
    else:
        balance+=deposit_amt
        print("Transaction Successfull..")
        return balance
    
def spend_Money(balance):
    spending_amt = int(input("Enter the Spending Amount: "))
    
    if(spending_amt<0):
        print("Invalid Deposit Amount..\nPlease Enter Valid Amount.")
    if(balance<=0):
        print("Transaction Failed...\nInsufficient balance..")
    elif(spending_amt>balance):
        print("Insufficient balance..")
    else:
        balance -= spending_amt
        print(f"Transaction Successfull..\namount {spending_amt} deducted from your Wallet.")
        return balance

def check_Balance(balance):
    print("Current Balance is",balance)
    return balance

def Exit(x):
    x=0
    return x

def main():
    balance = 50000

    x = 1
    while(x==1):
        print("                          ")
        print("--- E-Wallet Menu ---")
        print("1. Add money. \n2. Spend money. \n3. Check Balance. \n4. Exit.")
        print("                          ")

        choice = input("Enter Your Choice: ").lower()
        match(choice):
            case "1"|"add money":
                balance = deposit(balance)
            case "2"|"spend money":
                balance = spend_Money(balance)
            case "3"|"check balance":
                balance = check_Balance(balance)
            case "4"|"exit":
                print("Exiting....")
                x = Exit(x)
            case _:
                print("Invalid Choice..")
    
main()