# Dictionary

# - used to store large amount of data in key value pair

# Syntax:

# emp = {
#     # key:value
#     "name":"Aditya",
#     "skill":{
#         "skill1":"Python",
#         "skill2":"Java"
#     }
# }

# used to store large amount of data
# having methods and properties
# Dictionary is mutable in nature.
# All keys must be unique and Immutable.
# Purpose of Dictionary is to store the related information.
# 

emp={
    "id":1,
    "name":"Aditya",
    "skill":["Python","Java","Machine learning"],
    "CTC":"15LPA",
    "role":"Data Scientist",
    "company":"Google",
    "onRole":True,
    "age":23,
    "promotion":None,
    "age":20,
}
print(emp)


# Accessing elements of Dictionary

print(emp["role"])    # Data Scientist
print(emp["skill"])   # ["Python","Java","Machine learning"]
print(emp["skill"][2])# Machine learning

# No duplicate is allowed, It will not give error but when we try to access one value it gives another value
print(emp["age"]) # 20

# Updating the Data

emp["role"]="Senior Data Scientist"
print(emp["role"])


# Adding new data
emp["email"]="aditya@gmail.com"
print(emp["email"])

print(emp)

# ========================================

# Methods

# keys() method

# By default this loop prints all the keys inside the dictionary.
for keys in emp:
    print(keys)


# usng keys() method:
print("Keys are:")
for keys in emp.keys():
    print(keys)

# =======================

# values() method:

print("\n Values are:")
for val in emp.values():
    print(val)


# items() method:
print("\nItems are:")
for x in emp.items():
    print(x)

# ==============================================
# membership operator : in, not in

res = "role" in emp
print(res)

res = "role" not in emp
print(res)

# =================================

# len
# copy
# clear
# type

print(len(emp)) # print the lenght of dictionary
print(type(emp))# print the type of emp i.e Dictionary
emp.clear() # clears the Dictionary


#  copy

# -It creates the Shallow copy/ indepenent copy of a exsting dict

dict1 = {
    "user":"Aditya",
    "email":"aditya@gmail.com"
}
dict2 = {
    "address":"Pune",
    "skill":"Python"
}


# dict3 = dict2     # It does not create Shallow copy/Independent copy, When changes made inside dict3 then changes also reflected in dict2.

dict3 = dict2.copy()  # It creates the Shallow/Independent copy

print(dict1)
print(dict2)
print(dict3)

dict3["CTC"]="15LPA"   # This change will not reflect in dict2
print(dict3)     

# ===================================================

# Update- Updates the dictionary with another

products = {
    "productName":"Mac",
    "productPrize":"1lac",
    "productDetails":{
        "ram":"16GB",
        "rom":"256GB",
        "processor":"m4"
    }
}

products.update({"productOfferPrice":10000, "productBrand":"Apple"})
print(products)

# ===================================

# pop
# -pop is used to remove data
# -we have to pass key name which one want to  remove

products.pop("productName")
print(products)

# ========================================

# list to tuple Conversion

list3 = ["Aditya","Yash", "Onkar","Om"]
print(list3)
print(tuple(list3))


# ====================================

# list to Dictionary Conversion

list4 = [("name","Aditya"),('age', 20),('Role', "Data Analyst")]
print(list4)
print(dict(list4))

# ================================

# setDefault 
# - Used to set Default values in a dictonary
# - If key is present then it will consider existing one else as default one
# - If there is no any key:value present in dictionary but the default key is always present.


student={
    "name":"Aditya",
    "address":"Pune",
    "role":"Software Trainee" # this key is considered as default one and printed
    # If this was not present then Data scientist will be default one value printed
}

student.setdefault("role","Data Scientist")

print(student)