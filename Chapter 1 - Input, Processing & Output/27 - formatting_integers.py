# You can also use the format function to format integers
# There are two differences to keep in mind when writing a format specifier that will be used to format integers:

# You use d as the type designator
# You cannot specify the precision

print(format(123456789, 'd'))    # Printed with no special formatting
print(format(123456789, ',d'))    # Printed with comma separators
print(format(123456789, '10,d'))    # Printed in a field that is 10 spaces wide with comma separators
