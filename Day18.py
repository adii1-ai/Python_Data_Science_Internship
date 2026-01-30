# Inheritance

# Purpose - 
# - Used to inherit the properties and methods of parent class 
# - provides code reusability
# - improves code readability

# Parent class == Super class == Base class
# Child class == Sub classs == Innherited class

# Types of Inheritance :

# 1. single Inhritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# =============================
# 1. Single Inheritance
# =============================

# - In single Inheritance Child class can access the properties and methods of a only one/ single parent class 
# - there is only one parent class and only one child class

# Eg.,

# class Employee:  # Parent class

#     def __init__(self,empName, empRole,empId, empDept, empCTC):
#         self.empName = empName
#         self.empRole = empRole
#         self.empId = empId
#         self.empDept = empDept
#         self.empCTC = empCTC

#     def empDetails(self):
#         print(f'Emp Id = {self.empId}\nEmp Name = {self.empName}\nEmp Role = {self.empRole}')

# class Manager(Employee): # Child class

#     def __init__(self, name, dept_name,empId, empRole, empCTC, empDept):
#         self.name = name
#         self.dept_name = dept_name

#         super().__init__(name,empRole,empId,dept_name,empCTC)

#     def managerDetails(self):
#         print(f'Manager Name = {self.name}, Department Name = {self.dept_name}')
    
#     # super().empDetails()

# s1 = Manager("Aditya", "IT", 123456, "Junior Data Scientist", "20LPA","Hiring department")
# s1.managerDetails()   # Calling Child class method
# s1.empDetails()       # Calling Parent class method

# ========================================================================

# # parent class
# class Vehicle:

#     def __init__(self,vehicle_type,vehicle_mode,fuel_type):

#         # instance variable
#         self.vehicle_type=vehicle_type
#         self.vehicle_mode=vehicle_mode
#         self.fuel_type=fuel_type

#     def details(self):
#         print(f"Vehicle Details........{self.vehicle_type}")

# # child class 
# class Car(Vehicle):

#     def __init__(self,name,brand,color,model,price,vehicle_type,vehicle_mode,fuel_type):
#         self.name=name
#         self.brand=brand
#         self.color=color
#         self.model=model
#         self.price=price

#         # call parent __init__
#         super().__init__(vehicle_type,vehicle_mode,fuel_type)

#     def details(self):
        
#         super().details()# called parent details

#         print(f"Car Details...{self.name}")

# car1=Car("Hyrider","TATA","White","TOp","40LAC","4 Wheeler","Hybrid","Petrol")
# car1.details()

# ===========================================================

# # ===========================
# Multilevel inheritance
# # ===========================

# - In multilevel Inheritance the child class Inherit the properties and methods of parent cass and parent class can inherit the properties and methods of Grandparent class
# - grandParent class -> parent class -> child class

# Eg.,

# class GrandParent:
#     def gp(self):
#         print("grand Parent class")

# class parentClass(GrandParent):
#     def p(self):
#         print("Parent class")

# class ChildClass(parentClass):
#     def c(self):
#         print("Child Class")

# c1 = ChildClass()
# c1.gp()
# c1.p()
# c1.c()

# # ================================================

# # Grand Parent Class
# class Bank:

#     def __init__(self, name, branch):
#         self.name = name
#         self.branch = branch
    
#     def details(self):
#         print(f'Bank Name = {self.name}\nBranch name = {self.branch}')

# # Parent Class  
# class Account(Bank):

#     def __init__(self, acc_no, acc_type, acc_bal, name, branch):
#         self.acc_no = acc_no
#         self.acc_type = acc_type
#         self.acc_bal = acc_bal

#         super().__init__(name, branch)

#     def details(self):

#         super().details() # calling grandparent class method
#         print(f'Account Number is: {self.acc_no}\nAccount type: {self.acc_type}\nAccount Balance: {self.acc_bal}')
# # Child Class
# class Customer(Account):

#     def __init__(self, cust_name, cust_age, acc_no, acc_type, acc_bal, name, branch):
#         self.cust_name = cust_name
#         self.cust_age = cust_age

#         super().__init__(acc_no, acc_type, acc_bal, name, branch)
    
#     def details(self):

#         super().details()  # calling parent class method
#         print(f'Customer Name = {self.cust_name}\nCustomer age: {self.cust_age}')

# # creating Instance and accessing
# customer1 = Customer("Adi", 20, 123216, "Current", 100000, "HDFC", "HYD")
# customer1.details()

# ============================================================

# ======================
# Multile Inheritance
# ======================

# - In Mulptiple Inheritance a single child can access the properties and methods of 2 or more than 2 parent class

# - Parent1 ---> 
#                child
# - Parent2 --->

# Eg., 

# class mother:
#     def rel1(self):
#         print("Mother")
# class father:
#     def rel2(self):
#         print("Father")
# class child(mother, father):
#     def rel3(self):
#         print("Child")
# c1 = child()
# c1.rel1()
# c1.rel2()
# c1.rel3()

# =======================================================

# ======================
# Hierarchical Inheritance
# ======================

# -In hierarchical inheritance Multiple Child class inherit the properties of single parent class


class Parent:
    parent_name = "ABCD"
    print("Inside Parent class")
class Child1(Parent):
    child1_name = "XXXX"
    print("Child 1")

class Child2(Parent):
    child2_name = "YYYYY"
    print("Child 2")
class Child3(Parent):
    child3_name = "ZZZZ"
    print("Child 2")

c1 = Child1()
c1.child1_name
c1.parent_name

c2 = Child2()
c2.child2_name
c2.parent_name

c3 = Child3()
c3.child2_name 
c3.parent_name
