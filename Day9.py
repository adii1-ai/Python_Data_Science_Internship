# for else:
# -else block executed after loop finished

# for i in range(3):
#     print(i)
# else:
#     print("Loop finished Successfully")


# =================
# Star Pattern:

# for i in range(1,6):
#     print("*"*i)
# =====================

# Reverse Star pattern

# for i in range(5,1,-1):
#     print("*"*i)

# =========================================

# Functions

# -function is a block of code.
# -function is a mini program inside a program 
# -we can write a function at once and executes as many times we want
# -function provide reusability
# -defined once and reused multiple times

# Syntax:

# def fun_name():
    # block inside a function
# fun_name()  # function call


# ex:

# def demo():
#     print("hello world")
# demo()

# ex:

# def greet():
#     print("Welcome to our Program")

# greet()

# Addition program

# def add():
#     print(20+30)
# add()
# add()


# =========================================

# Parameters and Arguments in Function

# By using parameter and argument function becomes Dynamic

# Parameter - value whivh we pass during function declaration/definition
# Arguments - Actual value which we pass while function Calling

# def Sum(a,b):
#     print(a+b)
# Sum(30,40)


# ex:
# Take age from user and check is eligible for Voting

# def checkEligibility(age):
#     if(age>=18):
#         print("Eligible for Voting")
#     else:
#         print("Not Eligible..")
# age = int(input("Enter your age : "))
# checkEligibility(age)

# def UserInfo(userName, userSkill, userAddress):
#     print(f"Your Name is {userName}, Your Skill is {userSkill}, Your Address is {userAddress}")

# UserInfo("Aditya", "Java, Python..","Ahilyanagar" )

# def evenOdd(n):
#     result = "Even" if n%2==0 else "Odd"
#     print(result)

# evenOdd(4)
# evenOdd(5)


# ==============================

# return Keyword

# -used to return the values outside the function
# -it stops the execution of our after returning


# def mult(x,y):
#     return x*y
# result = mult(10,20)
# print(result)