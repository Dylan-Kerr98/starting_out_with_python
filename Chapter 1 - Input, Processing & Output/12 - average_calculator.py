# Determining the average of a group of values is a simple calculation, however, it is easy to make a mistake when
# writing a program

# Let's assume variables a, b & c each hold a value and we want to calculate the average of those values. If you are
# careless , you might write a statement such as:

a = 1
b = 2
c = 3

average = a + b + c / 3.0
print(average)

# When this statement executes the division will take place first and and will throw off the entire calculation
# This can be prevented by using parentheses as shown below:

d = 1
e = 2
f = 3

average = (a + b + c) / 3.0
print(average)

# Program to get average for test scores

# Get three test scores from user
test1 = float(input("Enter the first test score: "))
test2 = float(input("Enter the second test score: "))
test3 = float(input("Enter the third test score: "))

# Calculate the average of the three scores & assign result to average variable
average = (test1 + test2 + test3) / 3.0

# Display the average
print("The average score is", average)
