# If you are writing a program that works with a percentage, you have to make sure that the percentage's decimal point
# is in  the correct location before doing any math with the percentage

# This is essential when the user enters a percentage as an input. Most users would enter 50 to mean 50 percent and so
# forth, before any calculations are performed you would need to divide the input by 100 to move its decimal point two
# places to the left

original_price = float(input("Please enter items price: "))     # Get the item's original price

discount = original_price * 0.4     # Calculate the amount of discount

sale_price = original_price - discount      # Calculate the sale price

print("The sale price is", sale_price)      # Display the sale price
