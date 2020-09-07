# When multiple arguments are passed to the print function, they are automatically separated by a space when displayed
# on the screen:

print("One", "Two", "Three")

# If you do not want a space printed between the items:

print("One", "Two", "Three", sep='')

# You can also use this special argument to specify a character other than space to separate multiple items:

print("One", "Two", "Three", sep='***')
print("One", "Two", "Three", sep='§§§')
print("One", "Two", "Three", sep='%%%')
print("One", "Two", "Three", sep='±±±')
