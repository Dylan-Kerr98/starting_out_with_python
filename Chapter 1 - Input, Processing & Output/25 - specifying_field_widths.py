# The format specifier can also include a minimum field width, which is the minimum number of spaces that should be
# used to display a value

# The following example prints a number in a field that is 12 spaces wide:

print("The number is", format(12345.6789, '12,.2f'))

# The number given only uses 9 spaces on the screen but is displayed in a field that is 12 spaces wide

print("The number is", format(12345.6789, '9,.2f'))    # Set to 9 spaces instead

# Field widths can help when you need to print numbers aligned in columns:

# This program displays the following floating-point numbers in a column with their decimal point aligned:
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Display each number in a field of 7 spaces with two decimal places
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))
