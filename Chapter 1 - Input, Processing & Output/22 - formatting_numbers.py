# You might not always be happy with the way that numbers, especially floating-point numbers, are displayed on the
# screen

# When a float is displayed by the print function, it can appear with up to 12 significant digits

# This program demonstrates how a floating-point
# number is displayed with no formatting

amount_due = 5000.0
monthly_payment = amount_due / 12.0
print("The monthly payment is", monthly_payment)    # Output - 416.666666667

# As this program displays a pounds amount, it would be better to see the amount rounded to two decimal places, Python
# has a built in function which gives you a way to do just that, it is know as the format function

# When you call the format function, you pass two arguments to it, a numeric value and a format specifier. The format
# specifier contains special characters which specify how the number value should be formatted.

print(format(12345.6789, ".2f"))

# The .2 specifies the precision. It indicates that you want to round the number to two decimal places
# The f specifies that the data type of the number you are formatting is a floating-point number

# This is the same program as above but with the output formatted

amount_due2 = 5000.0
monthly_payment2 = amount_due / 12.0
print("The monthly payment is", format(monthly_payment2, '.2f'))    # Output - 416.67
