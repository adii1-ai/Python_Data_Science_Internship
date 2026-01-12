# Match Case (Switch case)

# -Used to handle multiple cases at the same time
# - Handle multiple cases at same time

# Syntax :

# match choice:
#     case 1:
#     case 2:
#     case 3:
#     case _:   # Default case


# Ex 1:

# day = int(input("Enter a Day : "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")

#     # Dafault Case
#     case _:
#         print("Invalid Day No...")

# *************************************************

# Ex 2:

# a = int(input("Enter first number :"))
# b = int(input("Enter Second number :"))
# choice = input("Chose any one of these : +, -, *, / : ")
# match choice:
#     case "+":
#         print("Addition is ",a + b)
#     case "-":
#         print(f'Subtraction of {a} - {b} is{a-b}')
#     case "*":
#         print("Multilication of"+a+"*"+b+ "is : "+a*b)
#     case "/":
#         print(f"Division is {a}/{b} is {a/b}")
#     case _:
#         print("Invalid Operation...")

# Ex 3:
# day = input("Enter the Day :")
# match day:
#     case "Monday":
#         print("Its a Week Day")
#     case "Tuesday":
#         print("Its a Week Day")
#     case "Wednesday":
#         print("Its a Week Day")
#     case "Tuesday":
#         print("Its a Week Day")
#     case "Friday":
#         print("Its a Week Day")
#     case "Saturday":
#         print("Its a Weekend")
#     case "Sunday":
#         print("Its a Weekend")
#     case _:
#         print("Invalid Day")

# ****************************************

# Looping Statements
# Execute same statement multiple times until condition becomes false

# for in
# while


# Ex 1;

# a = 1
# while a <= 10:
#     print("Welcome to modern Python")
#     a+=1


# Ex 2:
# a = 0
# while a <= 100:
#     print(a)
#     a+=2

#  Ex 3:
# a = 0
# while a <= 100:
#     if(a%2==0):
#         print(a)
#     a+=1



# Ex : 3
# a = 0 
# even = 0
# while(a <=50):
#     if(a%2==0):
#         even+=a
#     a+=1
# print("Sum of Even Numbers is ",even)

# ***************************************


# for in

# for i in range(1,50):
#     print(i)



# for i in range(1,50,2):
#     print(i)


# list = ["Aditya", "Om","Onkar","Pratik","Yash"]
# for i in list:
#     print(i)


# break Statement
# - Stops the execution of the program/loop

# for i in range(2,10):
#     if i == 4:
#         break
#     print(i)

# Cotinue satement
# - When continue statement executes it skips the further loop execution and executes from its next iteration.

# Ex : 1
# for i in range(2,10):
#     if i == 4:
#         continue
#     print(i)


# for i in range(1,5):
#     print(i)
#     for j in range(1,10):
#         print(j)

# n = int(input("Enter the number : "))
# for i in  range(1,11):
#     print(n*i)

# =========================

# for else
# -executes the else block after the loop
# ex:

# for i in range(3):
#     print(i)
# else:
#     print("Loop finished Successfully")


