# 

# name = input("Enter your Name :")
# m1 = int(input("Enter score 1 : "))
# m2 = int(input("Enter score 2 : "))
# m3 = int(input("Enter score 3 : "))
# m4 = int(input("Enter score 4 : "))
# print(f"""Your name is {name}
# your percantage is {(m1+m2+m3+m4)/400 *(100)}""")

# =====================================

# Primitive Data types are Immutable 

# =============================

# Operators in Python
# Arithmatic 

a = 100
b = 20
print(a+b)
print(a*b)
print(a-b)
print(a/b)  # return Quotient
print(a%b) # return reminder

print(2**3) #power

# Example
print(a*b+a)
print(a+b/a)
print(a*b/a)
print(a+(b*a))

# Comparison Operator
# ==, !=, <, > , <=, >=

x = 20
y = 30
print(x==y) #False
print(x!=y) # True
print(x<y) # True
print(x>y) # False
print(x>=y) # False
print(x<=y) # True

# Logical Operator
# - Used to handle multiple conditions
# and, or, not

# and --> both or all the conditions should be satistfied 
# or --> any one of the conditioon to be true to execute operation

# and
# 1 and 1 = 1
# 1 and 0 = 0
# 0 and 1 = 0
# 0 and 0 = 0

p = 200
q = 300
r = 500
print(p<q and p<r) #True and True ==>> True
print(p>q and p<r) # False and True ==>> False

# or 
# 1 or 1 = 1
# 1 or 0 = 1
# 0 or 1 = 1
# 0 or 0 = 0

print(p<q or q<r) # True or True ==>> True
print(p<q or r<q) # True or False ==>> True
print(p>q or r<q) # False or False ==>> False

# not 
print("Logical Not")
print(not (5 > 2)) # not(False) ==> True


# Assignment Operator
# -Used to assign the the value to a variable 
# -It assigns the right hand side value into the left hand side variable

#  =, +=, -+, /=, %=

a = 20
b = a
print(a,b)

no1 = 20
no2 = 40

print(no1+no2) #60
no1 += no2 
print(no1) #60
print(no2) #40

no1 *= no2 
print(no1) #2400
print(no2) #40

no1-=no2
print(no1) #2360
print(no2) #40

# Bitwise Operator

# &  -> Bitwise AND
# `  -> Bitwise OR
# ^  -> Bitwise XOR
# ~  -> Bitwise Not
# >> -> left Shift
# << -> Right Shift


# Ternary Operator
# Syntax ->> result = "if Condition True " if(condition) else "if Condition false"

# In python- result="if true" if condition else "if false"
# Example 
Byear = int(input("Enter your Birth year"))
result = "You are GenZ" if Byear >= 2000 else "You are not GenZ"
print(result)


# Membership Operator 
# -Used to check given element is present or not in the list/tuple/...

# in, not in

data = [20,40,60,80,100]
print("OM" in data)   # False
print(20 in data)     # True
print("OM" not in data) # True



# Identity Operator
# is, is not

a = 10
b = a
c = [10,20,30]
print(a is b) # True
print(a is c) # False
print(a is not c) # True