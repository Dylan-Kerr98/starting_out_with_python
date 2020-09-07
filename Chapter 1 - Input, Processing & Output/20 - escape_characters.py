# An escape character is a special character that is preceded with a backslash \, appearing inside a string literal
# When a string literal that contains escape characters is printed, the escape characters are treated as special
# commands that embedded in the string

# For example, /n is the newline escape character, this causes the following output to be advanced to a newline:

print("One\nTwo\nThree")

#   \t - Causes output to skip over to the next horizontal tab position

print("Mon\tTue\tWed\tThu"
      "\tFri\tSat\tSun")

#   \' - Causes a single quote mark to be printed

print('One\'Two\'Three')

#   \" - Causes a double quote mark to be printed

print("One\"Two\"Three")

#   \\ - Causes a backslash character to be printed

print("One\\Two\\Three")
