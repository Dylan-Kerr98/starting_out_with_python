# Most programming statements are written on one line. If a statement is too long, however, you will not be able to
# view all of it in your editor window  without scrolling

# Python allows you to break a statement into multiple lines by using the ling continuation character, which is a
# single backslash /

# Simple type the backslash character at the point you want to break the statement and press the enter key

var1 = 10
var2 = 20
var3 = 30
var4 = 40
var5 = 50

result = var1 * 2 + var2 * 3 + var3 \
    * 3 + var4 * 4 + var5 * 5

print(result)

# Python also allows you to break any part of a statement that is enclosed in parentheses into multiple lines without
# using the line continuation character:

mondaySales = 123.00
tuesdaySales = 345.00
wednesdaySales = 678.00

print("Monday's sales are", mondaySales,    # String line continuation
      "and Tuesday's sales are", tuesdaySales,
      "and wednesday's sales are", wednesdaySales)

# The following is another example:

value1 = 100
value2 = 200
value3 = 300
value4 = 400
value5 = 500
value6 = 600

total = (value1 + value2 +    # Calculation line continuation
         value3 + value4 +
         value5 + value6)

print(total)
