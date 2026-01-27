# **3️⃣ Electricity Bill Calculator**

# **Problem Statement:**

# Create a function to calculate electricity bill.

# **Rules:**

# - Units must be a positive number
# - Rate:
#     - 1–100 units → ₹5 per unit
#     - 101–300 units → ₹7 per unit
#     - Above 300 → ₹10 per unit
# - Handle invalid unit input (string, negative, empty)

# **Concepts to use:**

# - Function
# - `try-except`
# - `if-elif-else`

# ============================================

def calculate_electricty_bill():
    rs_per_unit = 0
    total_bill = 0
    try:
        unit = input("Enter the Units: ")

        if(not unit.isdigit()):
            raise ValueError("Unit must be in Number..")
        
        if(int(unit)<=0):
            raise ValueError("Units should be positive number")
        
        if(int(unit)>=1 and int(unit) <= 100):
            rs_per_unit = 5
        
        if(int(unit)>=101 and int(unit) <= 300):
            rs_per_unit = 7
        
        if(int(unit)>300):
            rs_per_unit = 10

        total_bill = int(unit)*rs_per_unit

    except ValueError as ve:
        print("Value Error:",ve)
    else:
        print(f'Total Bill is {total_bill}')

calculate_electricty_bill()