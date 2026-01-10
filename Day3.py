print("Hello, Welcome to python")

# Single line Commment:

# Shortcut :
# ctl + forward slash

print(10+30)
print(30*2)
# print(2**3)  #This will not printed

# Multiline comment

'''print(10+30)
print(30*2)
print(2**3)''' 

# =======================

# Identifiers

# Identifiers are the unique name to any value, class and the functions.
# it should nat start with unique character/Symbol and the number.
# It should start with underscore or simple english letters.


_skill = "Python" # Here _skill is the identifier
print(_skill)

name="Aditya"
age = 20
print(age)

# CammelCase 

'''username => userName
empid => empId
empname => empName
empskill => empSkill
emproll => emproll'''

# PascalCase

'''username => UserName
empid => EmpId
empname => EmpName
empskill => EmpSkill
emproll => Emproll'''

# Variable

# varible is also called an identifier.
# Variable is a container used to store integer, string or any other datatype value.

# Memmory 

# 1 byte = 8 bits
# 8 byte = 64 bits
# 1024 bytes = 1 KB
# 1024 KB = 1 MB
# 1024 MB = 1 GB
# 1024 GB = 1 TB
# 1024 TB = 1 


# Data Types (Variables)

# integer
empId = 1092

# float
age = 11.5

# string
empName = "Hritik"

# Bolean 
# Used for validation purpose

a = True
b = False

# Dynamic Typing
# -Python is a dynamic type lang. in which there is no need to define data type while defining variable
# Python allows to hold the different type of values at different time in same variable
# Multiline Variable 
a,b,c = 10, 20, 30
print(a)
print(b)
print(c)

x = y = z = "adi"
print(x)
print(y)
print(z)


# Introduction to Datatypes

# Primitive Data types
# int, float, string, boolean, None

# Non-Primitive Data Type
# list, tuple, dict, set

# int
empAge = 20
print(empAge)
print(type(empAge))

# float
empAge = 20
print(empAge)
print(type(empAge))

# string
empName = "Aditya"
print(empName)
print(type(empName))

# boolean
isEmployee = True
print(type(isEmployee))

# None
a = None
print(type(a))