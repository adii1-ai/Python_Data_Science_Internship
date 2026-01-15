# List

# -lists- is a collection of similar of different data type of elements
# -stored in. []
# -starts indexing from 0
# -we can stored mulitple type of data in a single variable
# -Mutable- we can change, add,remove, or update


# int - a=20
# string- a="" or ''
# boolean- True | False
# None-  empRole=None
# float- a=23.5

# **********************
# Non-Primitive Data Types

list=[100,25.3,True,None,"Aditya"]
print(list)
skills=["HTML","CSS","Tailwind","JS","React JS","Node JS","Express JS","Next JS","MongoDB","PostregsSQL"]
print(skills)


# ===================================================================

# indexing-

# indexes are used to access the particular elements from the list
# access list elements- indexing

print(skills[0])
print(skills[1])

#(negative index = from end)
# -Negative indexing start from -1

print(skills[-1]) # PostgresSQL
# print(skills[10]) # error :-list index out of range

# ==================================

# len()

# to check length of a s list
# -len() function is used to check the length of list
print(len(skills))

# ==========================================

# append()

# we can update given lists
# adding elements to the end of list
# append() function is used to append the new elements at the end of the list

roles=["admin","manager","user"]
# update list element
roles[2]="super-admin"
print(roles)
roles.append("HR")
print(roles)



# =====================================

# insert()

# add element on specific index
# insert(index,value)

roles.insert(0,"HR")
roles.insert(1,"HR")
print(roles)


# =======================================

# extend()

# extend- used to merge or concatenate 2 or more lists
# modified original list

list_1=["100","200",500,"OM","Vaibhav","Aditya"]
list_2=[True,None,"ABC","XYZ"]

# 1. without extend
# for x in list_2:
#     list_1.append(x)

# 2
# print(list_1+list_2)

# 3
# print(list_1,list_2)

# 4. with extend

list_1.extend(list_2)
print(list_1)

# ====================================

# pop()

# pop()- used to remove elements from lists
# pop()- by default it will remove last element
# pop(index)- When we pass the index it will remove specific element at that index

list_3=[10,20,30,40,50,60,70]
list_3.pop()
list_3.pop()
list_3.pop(2) 
print(list_3)

# ===========================================

# reverse()

# -reverse the given list

list_3.reverse()
print(list_3)

# ======================================

# sort()

# -it sorts the list elements alphabetically or numerically

fruits = ["apple",  "cherry","pomegrante","grapes","orange","banana","pineapple","custard apple","watermelon"]
fruits.sort()
print(fruits)

no=[100,300,500,250,350,50,30,1000,100]
no.sort()
no.reverse()
print(no)

# ======================================

# clear()
# -empty lists/ removes all the elements of the list

list_4=[10,40,50,80]
list_4=[]

# or

list_4=[10,40,50,80]
list_4.clear()
print(list_4)

# ========================================

# remove()
# -remove 1st matching element from the list

list_5=["HTML","CSS","Next JS","Redux","MUI","CSS"] 
list_5.remove("CSS")
print(list_5)

# ====================================

# copy() - most IMP

# user=["Pratik","Bhavesh","Shubham","Aniket","Aditya"]
# roles=["MERN Stack","Python Dev","AI Engineer","SDE-1","L-1"]

# assign roles in a new_roles variable
# new_roles=roles   #copying 
# new_roles.append("Senior Product manager") # Problem:- This makes changes in both the lists

# print(roles)
# print(new_roles)

# ===============

# problem

# it changes both the lists when we add the element or do any operation
# to avoid this make a independent copy of new list so it will not affect on original list

# solution- copy()
# create independent copy

roles=["MERN Stack","Python Dev","AI Engineer","SDE-1","L-1"]

# shallow copy
new_roles=roles.copy()
new_roles.append("Vice President")

print(roles)
print(new_roles)

# =========================================

# Searching in a List

emp=["Pratik","Sanmesh","Aditya","Om","Snehit","Pratik"]

# membership operator- in and not in

print("Pratik" in emp) # True
print("ABC" in emp)    # False
print("ABC" not in emp)# True

# ====================================

# looping

for x in emp:
    print(x)

# ===================================

# count()
# -count the number of values present in the list
print(emp.count("Pratik"))

# ==================================

# built in functions:

# len()
# min()
# max()-
# sum()

list_6=[10,40,50,80,90,300,30]
print(max(list_6)) # 300
print(min(list_6)) # 10
print(sum(list_6)) # 600
print(len(list_6)) # 7

# ===================================

# Slicing
# - extract some part of a list
# - Accessing the small piece of data from the list

# syntax-[start:end] ignore last
print(list_6[1:3]) # 40,50
print(list_6[0:5]) # 10 ...90
print(list_6[2])   # 50
print(list_6[2:])  # 50......
print(list_6[:3])  # 10,40,50
print(list_6[:])   # 10,...,30