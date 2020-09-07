# A named constant is a name that represents a value that cannot be changed during the program's execution

# Imagine, you are a programmer working for a large banking chain. You are updating an existing program that calculates
# data pertaining to loans, and you see the following line of code:

#   amount = balance * 0.069

# As someone else wrote the program, you aren't sure what the number 0.069 is. It appears to be an interest rate, but
# it could be a number that is used to calculate some fee instead. You simply can't determine the purpose of the number
# by reading this line of code

# This is an example of a magic number, an unexplained value that appears in a program's code

# Magic numbers can be very problematic for a number of reasons:

# 1 - It can be difficult for someone reading the code to determine the purpose of the number
# 2 - If the magic number is used in multiple places in the program, it can take allot of effort to change the number
# in every location it appears, should the need arise
# 3 - You take the risk of a typo mistake each time you type the magic number which will cause mathematical errors

# These problems can all be addressed by using named constants to represent magic numbers:

INTEREST_RATE = 0.072    # Value can be changed here an will be changed an every instance it appears in program
balance = 25000

amount = balance * INTEREST_RATE
print(amount)

