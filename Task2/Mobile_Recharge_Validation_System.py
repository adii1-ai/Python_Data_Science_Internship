#1️⃣ Mobile Recharge Validation System**

# **Problem Statement:**

# Create a function that allows a user to recharge their mobile number.

# **Requirements:**

# - Take **mobile number** and **recharge amount** as input
# - Mobile number must be **10 digits**
# - Recharge amount must be **greater than ₹10**
# - Handle invalid inputs using exception handling
# - Print success or failure message

# **Concepts to use:**

# - Function
# - `try-except`
# - `ValueError`

# ====================================

def recharge(mo_number, recharge_amt):
        try:
            if(len(mo_number)<10 or len(mo_number)>10):
                raise ValueError("Mobile Number Should be 10 Digits Only..")
                return
            
            if(recharge_amt <= 10):
                raise ValueError("Recharge Amount should be greater that ₹10")
                return
        except Exception as e:
            print(e)
        else:
            print("Recharge Success")

mo_number = input("Enter Mobile Number: ")
recharge_amt = int(input("Enter the recharge Amount"))

recharge(mo_number, recharge_amt)