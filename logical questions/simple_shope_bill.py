# A small shop wants a reusable function to calculate a customer's bill.

def calculate_bill(price,quantity=1):

      if price > 0 and quantity > 0:

            total_bill = price*quantity

            return total_bill

      else :
            return "Invalid input"

price = int(input("Enter the price : "))

quantity = int(input("Enter the Quantity : "))

# 1. Normal function call
print("Total Bill:", calculate_bill(price, quantity))


# 2. Quantity not provided
# Default quantity = 1 will be used
print("Default Quantity Bill:", calculate_bill(price))


# 3. Keyword arguments in reverse order
print("Keyword Argument Bill:", calculate_bill(quantity=quantity, price=price))
