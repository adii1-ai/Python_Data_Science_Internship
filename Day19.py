# Polymorphism
# - Polymorphism means one thing behave in different ways.
# - In polymorphism the same method/function/operator behaves differently on the object, argument, class, data type
# - The same function can perform different work i.e allows one function to handle multiple types 
# - Code becomes reusable
# - We can add new features without breaking the old code

# Applications:
# -Used in Payments, Vehicle, Notifications, Search, delivery apps
# - Search bar (search anything)
# - Payment option (UPI/Card/NetBanking)

# =============================

# Runtime polymorphism(Method Overriding)
# -It is also called as Dynamic Polymorphism
# -Runtime polymorphism in Python occurs when the specific method to be executed is determined at the program's runtime, rather than during compilation.
# -This is primarily achieved through method overriding and Python's dynamic typing, also known as "duck typing". 

# Method Overriding
# -Same function name and same number of parameters but different types of parameters during funnction call 
# -Same Method name but different behaviour based on the object.

# ==============================

# Compile time Polymorphism(Method Overriding)
# -Compile-time polymorphism means deciding which method or operation to run during compilation, usually through method or operator overloading.

# Method Loading
# -Same method name but different number of parameters.

# ================================================

# Runtime Polymorphism

# class Parent:
#     def hello():
#         print("Hello parent class")

# class Child(Parent):
#     def hello(self):
#         print("hello child class")

# child1 = Child()
# child1.hello()

# ===========================

# eg

# class Payment:

#     def __init__(self,wallet_balance,order_id,status,customer_id):
#         self.wallet_balance=wallet_balance
#         self.order_id=order_id
#         self.status=status
#         self.customer_id=customer_id

#     def details(self):
#         print("Hello Details Method in Parent class.....")
#         print(f"""Wallet Balance : {self.wallet_balance} , order Id {self.order_id} , 
#                status = {self.status} and customer Id. {self.customer_id} """)

# class UPI(Payment):

#     upi="Phone PAY"

#     def details(self):

#         print("Hello UPI Details.......")
#         super().details()

#     def pay(self):
#         print("Pay Here ........ UPI")

# class COD(Payment):
#     def pay(self):
#         print("Pay - COD")


# payment=UPI("100000","#123","OrderPlaced","1234567")
# payment.details()

# =================================================================

# Method Overloading

# - Python Does Not support Overloading but we can achieve it using *args

# *args

# class Calculator:
#     def sum(self, a,b,c,*args):
#         for x in args:
#             print(a+b+c+x)

# result1 = Calculator()
# result1.sum(1,2,3,4,5,6,7,8,9)

# Operator Overloading


# len(), +
# type()

# string="Pratik"
# list=["A","b","C"]
# tuple_1=(10,20,30,50)
# print(len(string))
# print(len(list))
# print(len(tuple_1))

#  +

# print(10+20)
# print("ABC"+"PQR")
# print(str(10)+"20")
# a=str(10)
# print(a)

