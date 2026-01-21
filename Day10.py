# Functions Continue

# def withdraw(balance):
#     withdraw_amt = int(input("Enter the Withdrawal Amount: "))
#     if(balance<=0):
#         print("Insufficient balance..")
#         return balance
#     elif(balance<withdraw_amt):
#         print("Inefficient balance..")
#         return balance
#     else:
#         balance -= withdraw_amt
#         print("Account balance is: ",balance)
#         return balance
    
# def deposit_(balance):
#     deposit_amt = int(input("Enter the Deposite Amount: "))
#     if(deposit_amt<0):
#         print("Invalid Deposit Amount..")
#         return balance
#     else:
#         balance = balance+deposit_amt
#         print("Account Balance is", balance)
#         return balance

# def main():
#     balance = 100000
#     ch = input("Would you like to withdraw or deposit? (withdraw/deposit/No): ").lower()
#     match(ch):
#         case "withdraw":
#             balance = withdraw(balance)
#         case "deposit":
#             balance = deposit_(balance)
#         case "no":
#             print("Your Balance is ",balance)
#         case _:
#             print("Invalid choice...")
# main()

# =============================================

# Types of Parameters in function

# Default paramater 
# -default paramaters are the parameters whose defaut value is defined at the time of function declaration/definition

# def Sum(a,b):
#     print(a+b)
# Sum(10,20)  # 30
# # Sum(20)     # Error  --> When we try to pass the less number of arguments than parameters defined inside function definition then error occurs, So we use default parameters 

# Ex:

# def Sum(a=0, b=0):
#     print(a+b)
# Sum(5)   # 5
# Sum(5,10)  #15

# Ex:

def Mult(a=1,b=1):
    print(a*b)
Mult(10)   # 10
Mult(5)    # 5


# =======

def Emp(empName="JOHN",empSkill="React",empId=None):
    return empName, " And ", empSkill, " And ", empId

print(Emp())        # ('JOHN', ' And ', 'React', ' And ', None)
print("","Python")  #  Python
print(Emp("","JS")) # ('', ' And ', 'JS', ' And ', None)

print(Emp(empSkill="Devops",empName="Pratik",empId=123))  # ('Pratik', ' And ', 'Devops', ' And ', 123)

# ================================================

# Arguments--->> *args

# -Handelling the Multiple arguments passed at the time of fucton calling

def Addition(x=0, y=0, z=0, *args):
    sum = x+y+z
    for x in args:
        sum += x
    print("Addition is",sum)
Addition(2,3,4,5,6,7,8,9,10)
Addition(100,200,300,400,500)


# ===============================

# Recursive function
# -Function Calling itself again and again is called the recursive function
# It includes two cases:
                # - base case -> to stop the recursion
                # - recursion case -> to call the function again and again
