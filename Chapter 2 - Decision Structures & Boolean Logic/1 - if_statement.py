# The if statement is used to create a decision structure, which allows a program to have more than one path of
# execution. The if statement causes one or more statements to execute only when a Boolean expression is true

# A control structure is a logical design that controls the order in which a set of statements execute. So far you
# have only used the simplest tpe of  control structure, the sequence structure

# A sequence structure is a set of statements that execute in the order in which they appear (Sequentially)

# Although the sequence structure is heavily used in programming, it cannot handle every task. This is because some
# problems simply cannot be solved by performing a set of ordered steps one after each other

# In a decision structures simplest form, a specific action is performed only if a certain condition exists and if the
# condition dose not exist then the action is not performed

outside = input("Is it could outside?: ")

if outside == "Yes":                                # if clause followed by condition
    print("You might want to put on your coat!")    # alternative path

# In the example about the outside variable is the condition which must be tested. If this condition is true then the
# string "You might want to put on your coat!" is returned to user

# If the condition is false then the string "Enjoy your day!" is returned instead

# Programmers call the type of decision structure shown above a single alternative decision structure, this is because
# it provides only one alternative path of execution (if outside condition is met then take alternative path)
