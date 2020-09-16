# Python allows you to compare strings which allows you to create decision structures that test the value of a string

nameOne = "Mark"
nameTwo = "Marc"

if nameOne == nameTwo:
    print("The names are the same.")
else:
    print("The names are NOT the same!")


currentMonth = "September"

if currentMonth != "October":
    print("This is the wrong time for Octoberfest!")
else:
    print("It's time for Octoberfest!")

# The program below demonstrates how two strings can be compared, it prompts the user to enter a password, then
# determines whether the string entered is equal to "Prospero"

password = input("Enter password: ")

if password == "Prospero":
    print("Password accepted.")
else:
    print("Sorry, incorrect password!")
