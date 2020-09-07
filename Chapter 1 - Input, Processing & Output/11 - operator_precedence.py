# You can write statements that use complex mathematical expressions involving several operators

x = 123
y = 543
answer = 17 + x + 21 + y
print(answer)

# Some expressions are not that straightforward, below:

outcome = 12.0 + 6.0 / 3.0

# In this statement, its possible that the number 6.0 might be used as an operand for either the addition or division
# operator. The outcome variable could be assigned either 6.0 or 14.0, depending on when the division takes place

# Fortunately, the answer is easy to find because Python follows the same order of operations that you learned in math

# First, operations that are enclosed in parentheses () are performed first. Then when two operators share an operand
# the operator with the higher precedence is applied first

# The precedence of the math operators from highest to lowest, are:

#   1 - Exponentiation **
#   2 - Multiplication *, Division / //, Remainder %
#   3 - Addition +, Subtraction -

# When two operators with the same precedence share an operand, the operations execute from left to right

print(outcome)

# Parts of mathematical expressions may be grouped with parentheses to force some operations to be performed before
# others

a = 5
b = 20

result = (a + b) / 4
print(result)

a = 5 + 2 * 4
b = (5 + 2) * 4
print(a, b)    # Result are different with parentheses

c = 10 / 5 - 3
d = 10 / (5-3)
print(c, d)    # Result are different with parentheses

e = 8 + 12 * 6 - 2
f = 8 + 12 * (6 - 2)
print(e, f)    # Result are different with parentheses

g = 6 - 3 * 2 + 7 / 3
h = (6 - 3) * (2 + 7) / 3
print(g, h)    # Result are different with parentheses
