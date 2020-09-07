# The print function normally displays a line of output, the following three statements will produce three lines of
# output

print("One")
print("Two")
print("Three")

#  Each of the statements shown above displays a string and then prints a newline character, this newline character
# cannot be seen but when it is displayed, it causes the output to advance to the next line

# If you do not want the print function to start a new line of output when it finishes displaying its output, you can
# pass the special argument end=' ' :

print("One", end=' ')    # Space in argument
print("Two", end=' ')
print("Three")

# Notice in the first two statements that the argument end=' ' is passed to the print function and specifies that a
# space should be printed instead of a newline

# Sometimes, you might not want the print function to print anything at the end of its output, not even a space
# If that is the case, you can just pass the argument end='' instead:

print("One", end='')    # Nothing in argument
print("Two", end='')
print("Three")
