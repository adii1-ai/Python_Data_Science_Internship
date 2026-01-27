#  **2️⃣ Online Movie Ticket Booking**

# **Problem Statement:**

# Create a function to book movie tickets.

# **Requirements:**

# - Take number of tickets as input
# - Max allowed tickets = **6**
# - Ticket price = **₹250**
# - Calculate total price
# - Handle cases where:
#     - User enters non-numeric value
#     - User enters more than 6 tickets
#     - User enters zero or negative tickets

# **Concepts to use:**

# - Function
# - Exception handling
# - Conditional logic

# ==================================

def book_movie_ticket(ticket_price):
    try:
        tickets = int(input("Enter the number of Tickets you want..:"))
        
        if(tickets>6):
            raise ValueError("Maximum 6 Tickets Allowed Only..")

        if(tickets <= 0):
            raise ValueError("Number of Tickets should be greater than 0..")
        
        total_price = tickets*ticket_price

    except ValueError as ve:
        print("ValueError : ",ve)
    else:
        print(f'Amount to be paid is {total_price}')
        print(f'{tickets} tickets booked Successfully.')

ticket_price = 250
book_movie_ticket(ticket_price)