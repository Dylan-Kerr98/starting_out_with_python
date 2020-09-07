# In Python, the % symbol is the remainder operator, also know as the modulus operator
# This operator performs division, but instead of returning the quotient, it returns the remainder

leftOver = 17 % 3   # Remainder of 2 
print(leftOver)

# Time converter program

# Get number of seconds from user
total_seconds = float(input("Please enter number of seconds: "))

# Get number of hours
hours = total_seconds // 3600

# Get number of remaining minutes
minutes = (total_seconds // 60) % 60

# Get the number of remaining seconds
seconds = total_seconds % 60

# Display the results
print("The number of seconds work out to:")
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
