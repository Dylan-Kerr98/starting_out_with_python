# If you want the numbers to be formatted with comma separators, you can insert a comma into the format specifier:

print(format(123456789, ',.2f'))
print(format(123456789.456, ',.2f'))
print(format(123456789.456, ',f'))

# The program below demonstrates how the comma separator and a precision of two decimal places can be used to format
# larger numbers as currency amounts

monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print("Your annual pay is £", format(annual_pay, ',.2f'), sep='')

# Not that the sep ='' argument is also passed to the print function, If you do not pass this argument, a space would
# be printed after the £ sign
