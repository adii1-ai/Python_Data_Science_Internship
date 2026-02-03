# Encapsulation
# -Used to restrict the access of variables and methods from outside of the class.
# -Protecting data from modification/ to prevent accidental damages/ modification.
# -Encapsulation provides the Security to the data.
# -Improves Security
# -Makes code modular and reusable
# Access Modifiers are used to secure data

# ===============================
# Access Modifiers:

# Public - Accessible everywhere (e.g., name)
# Private - Accessible only within the scope (e.g., __name)
# Protected - Internal use (e.g., _name)

# Private:
# - Double Underscore is used to make variable private

# protected :
# - Single underscore is used to make variable protected
# - It can be accessed but we cannot modify
# - We can Modify it but It is Standard (not modifying) to make variable Protected

# =================================================================

# class A:
#     # public/class member
#     __acc_no = 1233456677

#     def AccountHolder(self,userName, userId):
#         # instance variable
#         self.userName = userName
#         self.userId = userId
#         return f'username = {self.userName}\nuserId = {self.userId}'
    
# user1 = A()
# result = user1.AccountHolder("Aditya",1234)
# print(result)



# ===================================

class A:

    # public member
    name="Pratik"

    # private  member
    __empCTC="20LPA"

    # protected members
    # access but not modified
    _empRole="SDE-1"

    def Details(self):
        
        # instance Variable
        self.empId=12456
        # print(self.name)
        print(self.empId)

        # private
        print(self.__empCTC)

        # protected
        print(self._empRole)


class B(A):
    skill="Python"
    print(skill)

result1=B()
result1.Details()

# public member
print(result1.name)

# private member
# print(result1.__empCTC) # Gives an Error

# we can access private members
# Python uses name mangling internally:

print(result1._A__empCTC) # object._className__variableName


# protected members
# we can access but its says dont modify but we can modified ie. its just a convention in python
print(result1._empRole)

# ==============================

# eg

class Account:
        
        try:
            def __init__(self):
                self.__balance = 0

            def deposit(self, amount):
                self.__balance += amount

            def withdraw(self, amount):

                if amount <= self.__balance:
                    self.__balance -= amount
                else:
                  print("Insufficient Balance")


            def check_balance(self):
             return self.__balance
        except Exception as e:
            print("Error :",e)

acc = Account()
acc.deposit(500)
print(acc.check_balance())
acc.withdraw(200)
print(acc.check_balance())

# =====================================