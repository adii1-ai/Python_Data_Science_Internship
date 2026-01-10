# Type Casting 

print("Hello Welcome to python")

age = int("20")
print(age)
print(type(age))

# functions ->
#     str()
#     float()
#     bool()

a = 20
b = "30"
# print(a+b)# error
print(a+int(b))


empId = str(1123)
print(empId)
print(type(empId))

# ============================================

# Concatanation
# Merging two or more string together is called concatanation
# Three ways to concat string
# +
# ,
# f'' ->> Most ecomended or new
name = "Adi"
print("name is"+ name)
print(f'Name is {name}')
print("name is ", name)

# Differenc of + and , in concatanation
# -in
number1 = 100
skill = "Python"
print(number1,skill)   # O/P :- 100 Python
# print(number1 + skill) # Error, Because + operator requires same datatypes of both variable


num1 = 100
num2 = 200
print(num1,skill)   # O/P :- 100 200
print(num1 + num2)  # O/P :- 300


name1 = "Adi"
name2 = "Yash"
print(name1,name2)   # O/P :- Adi Yash
print(name1 + name2)  # O/P :- AdiYash


# , is most used and automatically convert into string

no1 = 872
no2= "172"
print(no1,no2)

empRole = "Python Fullstack Developer"
empAddress  = "Pune"
print(empRole, empAddress)

# f'' -->> clean and modern
empAge = 20
empCTC = "20 LPA"
print(f'Your age is {empAge} and salary is {empCTC}')


age = 20
name = "Aditya"
skill = "Python"
print(f'Your name is {name}, Age is {age}, and Skill is {skill}')
# print("Your name is " + name + " Age is " + age + " and Skill is " + skill)
print("Your name is " , name,", Age is ",age,", and Skill is ", skill)

# =========================================

# Taking input from User

# input() function is used 
# input() function takes the string by default

a = input("Enter the number 1") # Takes the input as string
b = input("Enter the number 2")
print("Addition is ", a+b)

a = int(input("Enter the number 1")) # Takes the input as Integer
b = int(input("Enter the number 2"))
print("Addition is ", a+b)


# =========================================
 
#  Reserved Keywords 

import keyword
print("keywords are : ", keyword.kwlist)


# ==============================================

# Memory Concept

# id() - to check the memory location
# if value is same then pointed at same memory location
# if value changes of both variables have different memory location
x = 10
print(x)
y = 20
print(y)
print("id of x is",id(x))
print("id of y is",id(y))