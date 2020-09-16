# In addition to determining whether strings are equal or not equal, you can also determine whether one string is
# greater than or less than another string.

# This is useful because programmers commonly need to design programs that sort strings in some order

# As you know computers do not actually store characters, instead they store numeric codes that represent the
# characters (ASCII Codes)

# Uppercase characters A-Z are represented by the numbers 65-90
# Lowercase characters a-z are represented by the numbers 97-122
# Digits 0-9 are stored in memory as characters , they are represented by numbers 48-57
# A blank space is represented by the number 32

# ASCII also establishes an order for characters, A comes before B which comes before C and so on

# When a program compares characters, it actually compares the code for the characters

if "a" < "b":
    print("The letter a is less than the letter b.")

# Below shows how strings containing more than one character are typically compared

name1 = "Mary"    # M = 77, a = 97, r = 114, y = 121
name2 = "Mark"    # M = 77, a = 97, r = 114, k = 107
if name1 > name1:
    print("Mary is greater than Mark")
else:
    print("Mary is not greater than Mark")

# When compared all characters of both strings will be equal apart from Y & k, character y has a higher ASCII code than
# k so it is determined that the string "Mary" is greater than the string " Mark

# If one of the strings in a comparison is shorter than the other only the corresponding characters will be compared
# If the corresponding characters are identical, then the shorter string is considered less than the linger string

name3 = input("Enter a name (last name first): ")
name4 = input("Enter another name (last name first): ")

if name3 < name4:
    print(name3)
    print(name4)
else:
    print(name4)
    print(name3)

