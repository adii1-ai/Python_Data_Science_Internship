# Controle Statements ==>> 
# 1. Conditional Statements
# 2. Looping Statements

# Conditional Statements
# if
# if else
# if elif else
# match-case (Python 3.10+Switch Case)== Switch case


# Looping Statement
# for in
# while

# =================================

# if
# -Check only one condition

# if(condition):
#     // Block of code

# Ex:1

# n = int(input("Enter a Number : "))
# if (n%2 == 0):
#     print("Number is even")
# if (n%2 != 0):
#     print("Number is Odd")

# Ex:2

# age = input("Enter your age : ")
# if(age <= 18):
#     print("Sorry Bhai...")

# Ex:3

# ShopAmt = int(input("Enter Shoping amount"))

# if(ShopAmt >= 20000):
#     Discount = ShopAmt*0.2
#     print("Congrats you got 20% Discount")
#     print("Discount is ",Discount)
#     print("Total amount to be paid ", ShopAmt-Discount)
# else:
#     print("Sorry, No Discount for you")
#     print("Amount to be paid",ShopAmt)

# if else
# -It checks 2 conditions

# age = int(input("Enter your age"))
# if(age>=18):
#     print("Congrats..")
# else:
#     print("Sorry..")


#  Nested if else

# score1 = int(input("Enter score 1"))
# score2 = int(input("Enter score 2"))
# score3 = int(input("Enter score 3"))
# score4 = int(input("Enter score 4"))
# score5 = int(input("Enter score 5"))
# score6 = int(input("Enter score 6"))
# if(score1>=35 and score2>=35 and score3>=35 and score4>=35 and score5>=35 and score6>=35):
#     print("Pass..")

#     percentage = ((score1+score2+score3+score4+score5+score6)/100)*100

#     if(percentage>=75):
#         print("You got distinction class", percentage)
#     else:
#         print("You got Pass class", percentage)
# else:
#     print("Fail..")


# if elif else
# - to check multiple condition

# Ex:

# shop_amt = int(input("Enter Shoping Amount : "))
# discount = 0
# if(shop_amt >= 10000 and shop_amt < 20000):
#     discount = 20
# elif(shop_amt >= 20000 and shop_amt<30000):
#     discount = 30
# elif(shop_amt>=30000 and shop_amt<40000):
#     discount = 40
# elif(shop_amt>=40000):
#     discount = 50
# else:
#     print("No Discount")

# disc_amt = shop_amt*discount/100
# net_total =  shop_amt-disc_amt

# print(f"Your Shopping Amount Is {shop_amt} \n")
# print(f"You Got A {discount}% \n")
# print(f"Your Discount Amt is {disc_amt}")
# print(f"Net Total Is {net_total}")

