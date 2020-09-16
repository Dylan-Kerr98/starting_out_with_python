# As mentioned the if statement tests an expression to determine whether it is true or false, the expressions that are
# tested are called Boolean expressions, this name is taken from Boolean algebra (This is the branch of
# algebra in which the values of the variables are the truth values true and false)

# Typically, the Boolean expression that is tested by an if statement if formed with a relational operator which
# determines whether a specific relationship exists between two values, the relational operators available in Python
# are:

#    >    Greater than
#    <    Less than
#    >=   Greater than or equal to
#    <=   Less than or equal to
#    ==   Equal to
#    !=   Not equal to

# See several examples of Boolean expressions that compare the variables x & y:

#    x > y     Is x greater than y?
#    x < y     Is x less than y?
#    x >= y    Is x greater than or equal to y?
#    x <= y    Is x less than or equal to y?
#    x == y    Is x equal to y?
#    x != y    is x not equal to y?

# You can use the Python interactive mode to experiment with these operators, the interpreter will evaluate the
# expression and display its value as either True of False

sales = float(input("Please enter this months total sales: "))

if sales >= 50000.00:
    print("Congratulation!, you will receive a bonus in your pay")