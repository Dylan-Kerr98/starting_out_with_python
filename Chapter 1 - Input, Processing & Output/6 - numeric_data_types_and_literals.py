# As different types of numbers are stored and manipulated in different ways, Python uses data types to categorize
# in memory

# An integer is classified as an int & a real number(floating point) is classified as a float
# A number which is written into a programs code is called a numeric literal

# When a Python interpreter reads a numeric literal it determines its data type according to the following

# A numeric literal written as a whole number with no decimal points is considered an int, e.g. (7, 124, -9)
# A numeric literal written with a decimal point is considered a float, e.g. (1.5, 3.141, -5.79)

# As an experiment, you can use the built-in type function to determine the data type of a value

print(type(1))
print(type(1.0))

room = 503
dollars = 2.75

print(type(room))
print(type(dollars))

# WARNING! - You cannot write currency symbols, spaces or  commas in numeric literals

#          value = £4,567.99 - Error
#          value = 4567.99 - Correct

# Python also has a data type named str which is used for storing strings

print(type("Test"))

name = "Dylan"
print(type(name))
