# OOP Introduction

# OOP -> Object Oriented Programing
# OOP is a professional way of writing our code to solve real world problems
# It avoids code code repitition
# It also provides security and Protection 
# Easy maintainance 
# Code becomes Organised/reusable by using OOP

# 4 Pillars of OOP 
# 1. Inheritance
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction


# Class
# Class is a real world entity
# Class can have propeties and methods
# Class is a blueprint of Object

# Object
# Object is instance of class
# e.x., We can create 1000 of mobile by using same mobile class

# ===========================================

# # creating class

# class Mobile:
#     pass

# # creating object

# m1 = Mobile()
# m2 = Mobile()

# ====================================

# self

# self in python is like a this keyword in other languages
# self is not a keyword
# self is used to refer the current object of class
# self is important to access the variables outside there scope

# ====================================
# eg.,

# # class creation
# class Mobile:
#     # properties/ Variables
#     name = "Vivo S1 Pro"
#     brand = "Vivo"
#     color = "Black"

#     def calling(self):
#         print("Hello,.....")
    
#     def switchOn(self):
#         print("Mobile is On")

#     def switchOff(self):
#         print("I am Dead..")

#     def chatting(self):
#         print("I am Busy with Someone on Whatsapp...")
# # objects creation
# m1 = Mobile()
# print(m1.name)
# print(m1.brand)
# m1.calling()

# m2 = Mobile()
# m2.switchOff()
# m2.chatting()

# =========================================

# real world Example:

class BankAccount:
    account_Number = 12345555
    account_Holder = "ABCdEFG"
    account_type = "Saving"
    IFSC_code = "XYZ192839"
    
    def deposit(self):
        print("Balnce deposited Successfully")
    
    def withdraw(self):
        print("Withdraw Successfully")
    
    def calculate_interest(self):
        print("Your Interest is.......")

b1 = BankAccount()
print(b1.account_Holder)
b1.calculate_interest()