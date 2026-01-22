# Exception Handlling

# An exception is an runtime  error that stops an execution of a program.
# We have to manage/continue the flow of program even if any runtime error occurs by using Exception Handlling

# def Div(a,b):
#     print(a/b)
# Div(10,0)       # Generate the error 
# Div(10,2)       # This will not Execute after error occurs

# So we need to use exception Handling 

# ex:

# try:
#     a = 10
#     b = 0
#     print(a/b)
# except:
#     print("Error Occured ZeroDivisionError")


# ex:

# try:
#     def Calci(a,b):
#         return a/b
#     print(Calci(5,5))
#     res=Calci(50,0)
#     print(res)

# except:
#     print("Error Occured ZeroDivisionError")

# ex:
# Printing the error

# try:
#     def Calci(a,b):
#         return a/b
#     print(Calci(5,5))
#     res=Calci(50,0)
#     print(res)

# except Exception as e:
#     print("Error Occured",e) # division by zero


# ex:
# type error

# try:
#     x = 100
#     y = "300"
#     print(x,y)  
#     print(x+y)  # unsupported operand type(s) for +: 'int' and 'str'
# except Exception as e:
#     print("Error: ",e)

# ======================================================

# Types of Error:

# ZeroDivisionError -> Ocuurs when try to divide a number by zero
# TypeError -> 





# =============================================

# block 

# try - 
# -It includes the code that may ganerate the error

# catch-
# -Catch block handel the error
# -It catch the error and gives appropriate message to the user without stoping the execution of program after error occurs

# finally-
# -Finally block always executed even if error occuredd or not.

# else-
# -else block executed when there is no error occurs.

# ex:


# try:
#     num=int(input("Enter Number :"))
# except ValueError:
#     print("Invalid Number")
# else:
#     print("You Entered ",num)
# finally:
#     print("Finally block executed")
    


# ========================================================

# Raising an Error

# raise keyword is used to raise an error
# Error raising is use when you want to raise tour own error 
# try:
#     age = int(input("Enter Your Age : "))
    
#     def Demo(a):
#         if a<=0:
#             raise ValueError("Age cannot be 0 or Negative..")
#         print("Your age is",a)
#     Demo(age)
# except Exception as e:
#     print("Error : ",e)



# ==============================================
# Task - Take Username Input From User
# Rules:

# cannot be empty
# length must be at least 4
# must not contain  spaces

# if fails- raise ValueError

# try:
#     userName = input("Enter your Name: ")
#     def user(userName):
#         if len(userName)<4:
#             raise ValueError("User Name must be of Four letters..")
#         if " "in userName:
#             raise ValueError("User Name Does Not contain Space")
#     user(userName)
# except Exception as err:
#     print("Error Occured,",err)
# else:
#     print("UserName is",userName)
# finally:
#     print("Finally block..")