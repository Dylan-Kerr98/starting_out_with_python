# Variables are called "variable" because they can reference different values while a program is running.
# When you assign a value to a variable, the variable will reference  that value until you assign it a different value

dollar_bills = 1245                                     # Initial variable value
print("I have", dollar_bills, "dollars in my account")

dollar_bills = 1100                                     # reassigned variable value
print("I have", dollar_bills, "dollars in my account")

# The initial variable value is still present in the computers memory, however, it can no longer be used as it is not
# reference by a variable

# Keep in mind that in Python, a variable is just a name that refers to a price of data in  memory
# A python variable can refer to items of any data type, once a variable has been assigned one type, it can be
# reassigned to a different type

x = 99
print(x)

x = 99.00
print(x)

x = "Ninety Nine"
print(x)
