# You probably remember from algebra class that the expression 2xy is understood to mean 2 times x times y, in maths
# you do not always use an operator for multiplication.

# Python as well as other programming languages, requires an operator for any mathematical operation

#   6b    ==  6 * b
#   (3)(12)   ==    3 * 12
#   4xy   ==    4 * x * y

# When converting some algebraic expressions, you may need to insert parentheses that do not appear in the expression

#       A + b
#   x = -----
#         c

#   x = (a+b)/c

# Suppose you want to deposit a certain amount of money into a savings account and leave it alone to draw interest for
# the next 10 years. At the end of 10 years you would like to have £10,000 in the account. How much do you need to
# deposit today to make this happen

# You can yous the following formula to find out

#         F
#   P = -----
#       (1+r)n

# P is the present value, or amount you need to deposit today
# F is the future value that you want in the account (In this case, F is £10,000)
# r is the annual interest rate
# n is the number of years that you plan to let the money sit

# It would be very convenient to write a computer program to perform the calculations because then you can experiment
# with different values

# Here is the algorithm that we can use:

# Step 1 - Get the desired future value
# Step 2 - Get the annual interest rate
# Step 3 - Get the number of years that the money will sit
# Step 4 - Calculate the amount that will have to be deposited
# Step 5 - Display the results of the calculation in step 4 to user

# Get the desired future value
future_value = float(input("Enter the desired future value: "))

# Get the annual interest rate of savings account
rate = float(input("Enter the annual interest rate of account: "))

# Get the number of years that the money will appreciate
years = int(input("Enter the number of years money will be kept in account: "))

# Calculate the amount needed to deposit into account
present_value = future_value / (1.0 + rate) ** years

# Display the amount that needs to be deposited
print("You will need to deposit:", present_value)

# Unlike the output shown for this program, dollar amounts are usually rounded to two decimal places
# Later in this chapter, you will learn how to format numbers so they are rounded to specified number of decimal places
