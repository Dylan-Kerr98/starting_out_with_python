# When you perform a math operation on two operands, the data type of the result will depend on the data type of the
# operands

# Python follows these rules when evaluating mathematical expressions:

# If operation is performed on two int values, result will be int
# If operation is performed on two float values, result will be float
# If operation is performed on an int & float, int value will be temporarily converted to float and result will be float

# An expression that uses operands of different data types is called a mixed-type expression

integers = 3 + 3    # Result 6
print(integers)

floats = 3.0 + 3.0    # Result 6.0
print(floats)

mixed_type = 3.0 + 3    # Result 6.0
print(mixed_type)

# The int to float conversion that takes place in the previous statement happens implicitly (automatically)

# If for a reason you need to explicitly (manually) perform a conversion, you can use either the int() or float()
# functions

floatValue = 2.6
intValue = int(floatValue)    # Converts float value to int value
print(intValue)

intValue2 = - 2
floatValue2 = float(intValue2)    # Converts float value to int value
print(floatValue2)
