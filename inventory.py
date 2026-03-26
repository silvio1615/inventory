# Requests the product name from the user
product = input("Enter product name: ")
# Starts in True to enter the loop
val_cant = True
# The loop repeats while val_cant is True
while val_cant:
    try:
        # Tries to convert the input to an integer
        quantity = int(input("Enter the product quantity: "))
        # Checks that the quantity is not negative
        if quantity < 0:
            print("Error: please enter a positive value for the quantity.")
        else:
            # If valid, changes to False to exit the loop
            val_cant = False
    except ValueError:
        # If the user enters text or another non-numeric value
        print("Error: please enter a valid number.")
# Starts in True to enter the loop
val_price = True
# The loop repeats while val_price is True
while val_price:
    try:
        # Tries to convert the input to a float
        price = float(input("Enter the product price: "))
        # Checks that the price is not negative
        if price < 0:
            print("Error: please enter a positive value for the price.")
        else:
            # If valid, changes to False to exit the loop
            val_price = False
    except ValueError:
        # If the user enters text or another non-numeric value
        print("Error: please enter a valid number.")
# Calculates the total cost by multiplying price by quantity
total_cost = price * quantity
# Displays the final results in a single formatted line
print(f"Product: {product} |Quantity: {quantity} |Unit price: ${price:.2f} |Total cost: ${total_cost:.2f}")

# -----------------------------------------------
# SUMMARY
# The program requests the name, quantity and price
# of a product from the user. It uses boolean flags
# (val_cant, val_price) along with while loops and
# try/except error handling to ensure that the entered
# values are numeric and positive, repeating the request
# until a valid input is obtained. Finally, it calculates
# the total cost and displays all the data in a single
# formatted line.
# -----------------------------------------------
