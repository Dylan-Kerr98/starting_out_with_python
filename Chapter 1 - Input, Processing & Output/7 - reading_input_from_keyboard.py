# A large majority of the programs which you will write will need to read input and then perform an operation on that
# input

# An example of a basic input operation is reading data which has been typed on the keyboard, usually when a program
# reads data from the keyboard it will get stored in a variable

# Python has a built in function for reading from the keyboard called input, this reads a piece of data that has been
# entered at the keyboard and returns that piece of data, as a string, back to the program

name = input("What is your name? ")     # In general format, prompt is a string that is displayed on the screen
print("Hello", name)                    # The strings purpose is to instruct the user to enter a value

# Note the input function does not automatically place a space after prompt string

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hello", first_name, last_name)

# The input function always returns the user's input as a string, even if the user enters numeric data
# This can result in problems in you use the input in mathematical operations.
# Fortunately, Python has built ib functions that you can use to convert a string to a numeric type

hours_worked = int(input("How many hours did you work?: "))
pay_rate = float(input("What is your hourly pay rate?: "))

# The first statement gets the number of hours from the user and assigns that value as a string to the hours_worked
# variable
# The second statement calls the int() function, passing hours_worked as an argument which is then converted to an int
# This is know as nested function calls

# The int() & float() functions work only if the item that is being converted contains a valid numeric value. If cannot
# be converted to the specified data type, an error know as an exception occurs, this is an unexpected error that
# occurs when the program is running

age = int(input("What is your age?: "))  # Enter a string to view exception error
