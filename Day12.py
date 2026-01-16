# Tuple

# tuple are faster than list
# Tuple is collection of similar or different ypes of element
# Tuple is similar like list
# It can store similar or different types of elements
# It has fixedd size 
# We cannot perform any updation, deltion and appending on tuple.
# It is written in ( )
# start indexing from 0
# It is Immutable
# It is a faster than a list

# ====================================

# Syntax-

# skill = ("HTML","CSS","JS","Python")
# print(skill)

# print(skill[2])  # JS

# # skill[1]="Tailwind"   # Error
# # print(skill[1])

# ================================

# we can also store tuple values without paranthesis 

# emp = "HTML","CSS","JS"
# print(emp)  # ('HTML', 'CSS', 'JS')
# print(type(emp))  # tuple

# =======================================

# for storing single element in tuple

# emp = ("aditya")
# print(type(emp))  # str

# emp = ("aditya",)
# print(type(emp))  # tuple

# ====================================

# looping - access without index

# user = ("motu", "patlu","shiva","Ninja","Aditya","Singchan")
# for x in user:
#     print(x)

# slicing

# print(user[1:5]) # ('patlu', 'shiva', 'Ninja', 'Aditya')
# print(user[:3])  # ('motu', 'patlu', 'shiva')
# print(user[2:])  # ('shiva', 'Ninja', 'Aditya', 'Singchan')


# range - access using index

# user = ("motu", "patlu","shiva","Ninja","Aditya","Singchan")
# for x in range(2,6):
#     print(user[x])

# ========================================

# built in function

# sum()
# len()
# min()
# max()

# tuple_1 = ("AWS","Next JS","Express JS","Node JS")
# # tuple_1.sort()     # error 
# # tuple_1.reverse()  # error

# tuple_x = (1,2,3,4)
# print(min(tuple_1))
# print(max(tuple_1))
# print(sum(tuple_x))

# ================================

# searching

# in 
# not in

# tup = (1,2,3,4,6678,67)
# print(2 in tup) # True
# print(10 not in tup) # True
# print(10 in tup)  # False

# ===============================

# sorted()
# - Sort the tuple

# tuple_n = ("AWS","Next JS","AWS","Express JS","Node JS")
# print(sorted(tuple_n))

# ================================
# count()

# tuple_2 = ("AWS","Next JS","AWS","Express JS","Node JS")
# print(tuple_2.count("AWS"))

# ===================================

# Packing and Unpacking

brands = ("Samsung","Lenovo","Apple","Xiaomi","Realme")
print(brands)
print(brands[0])
print(brands[2])

# Unpacking
brand1, brand2,brand3, brand4, brand5, brand5 = brands
print(brand1)
print(brand2)


# ===============================

# list to tuple conversion

# list_1 = [10,20,30,40,50]
# print(type(list_1))
# print(list_1)

# print(tuple(list_1)) # Converting the list into tuple

# print(list_1) # main list not changed 


# =================================

# tuple to list tuple conversion


# tup_1 = (10,20,30,40,50)
# print(type(tup_1))
# print(tup_1)

# print(list(tup_1))  # Converting the tuple into list

# print(tup_1) # main tuple not changed

# =============================

# tasks

# 4️⃣ Count how many times `"apple"` appears in `("apple", "banana", "apple")`.

tup = ("apple", "banana", "apple")
print(tup.count("apple"))

# 5️⃣ Unpack a tuple `(10, 20, 30)` into 3 variables.

tup_1 = (10, 20, 30)
n1, n2, n3 = tup_1
print(n1)
print(n2)
print(n3)

# 6️⃣ Create a nested tuple and access the second row, third element.
tup_2 = ((1,2,3, 11),(4,5,6,10),(7,8,9,12))
print(tup_2[2][3])

# 1️⃣ Create a tuple of 5 colors and print them one by one.

tup_3 = ("red","orange","yellow","black","white")
for x in tup_3:
    print(x)