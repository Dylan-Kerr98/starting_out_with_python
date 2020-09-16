# If you want to write some text in the graphics window you can use the turtle.write(text) command to do this, the text
# that you want to display is passed to the command as an argument, quotation marks must be used when passing argument

# When the string is displayed, the lower-left corner of the first character will be positioned at the turtle's X and
# Y coordinates

import turtle

turtle.setup(300, 300)          # Set graphic window size
turtle.penup()                  # Raise pen
turtle.hideturtle()             # Hide turtle icon
turtle.goto(-120, 120)          # Go to specified location on canvas
turtle.write("Top Left")        # Display string at location
turtle.goto(70, -120)           # Go to specified location on canvas
turtle.write("Bottom Right")    # Display string at location

turtle.done()
