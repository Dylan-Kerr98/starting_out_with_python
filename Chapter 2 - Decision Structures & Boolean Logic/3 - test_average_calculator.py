# This program gets five test scores and displays the average, it will congratulate the user if the average score is
# above a certain score

HIGH_SCORE = 95

test_one = int(input("Please enter score of first test: "))
test_two = int(input("Please enter score of second test: "))
test_three = int(input("Please enter score of third test: "))
test_four = int(input("Please enter score of four test: "))
test_five = int(input("Please enter score of fifth test: "))

average = (test_one + test_two + test_three + test_four + test_five) / 5

print("Your average score is:", average)

if average >= HIGH_SCORE:
    print("Congratulations!, you got a very high score")
