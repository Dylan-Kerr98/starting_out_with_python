# Even though the test grader program is a fairly simple program, the logic of the nested decision structure is fairly
# complex. Python provides a special version of the decision structure know as the if-elif-else statement, which makes
# this type of logic simpler to write

A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user
score = int(input("Enter your test score: "))

# Determine the grade
if score >= A_SCORE:
    print("Your grade is A.")
elif score >= B_SCORE:
    print("Your achieved grade is B.")
elif score >= C_SCORE:
    print("Your achieved grade is C.")
elif score >= D_SCORE:
    print("Your achieved grade is D.")
else:
    print("Your grade is F")

# Notice the alignment and indentation that is used with the if-elif-else statement, all clauses are aligned and the
# conditionally executed blocks are indented

# A long series of nested if-else statements has two particular disadvantages:

# (1) - The code can grow complex and become difficult to understand
# (2) - Due to the required indentation, a long series of nested statements can grow too long to be displayed on the
# computer screen without horizontal scrolling

