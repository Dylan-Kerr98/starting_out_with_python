# Python has numerous operators that can be used to perform mathematical calculations

# Most real world algorithms require calculations to be performed. The tools for performing calculations are math
# operators, below is a list of the math operators that are provided by the Python language

#   +   Addition - Adds two numbers
#   -   Subtraction - Subtracts two numbers
#   *   Multiplication - Multiplies one number by another
#   /   Division - Divides one number by another, result is given as floating point number
#   //  Integer division -  Divides one number by another, result is given as whole number
#   %   Remainder - Divides one number by another and dives the remainder
#   **  Exponent - Raises a number to a power

# Values placed on the left & right side of operators are called operands, these are the values the operator acts on

x = 80 + 20
print(x)

# Variables can also be used in math expressions

firstNumber = 20
secondNumber = 50

thirdNumber = firstNumber * secondNumber
print(thirdNumber)

# Simply math below

salary = float(input("What is total salary for the year?: "))
bonus = float(input("what is total bonus's for the year?: "))

yearly_pay = salary + bonus

print("Your total yearly pay is", yearly_pay)