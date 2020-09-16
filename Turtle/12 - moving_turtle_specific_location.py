# A cartesian coordinate system is used to identify the position of each pixel in the turtle's graphics window. Each
# pixel has an X coordinate and a Y coordinate. THe X identifies the pixels horizontal position and the
# Y identifies the vertical position

# The pixel in the center of the graphics window is at the position (0, 0)
# The X coordinates increase in value as you move towards the right side of the window and decrease going left
# The Y coordinates increase in value as you move up the window and decrease going down the window
# Pixels to the right side of the X coordinates are positive and pixels to the left are negative
# Pixels above of the Y coordinates are positive and pixels below the Y coordinates are negative

# You can use the turtle.goto(x, y) command to move the turtle from its current location to a specific position in
# the graphics window, the x & y coordinates are passed to the command as arguments

# If the turtle's pen is down, a line will be drawn as the turtle moves
import turtle
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)

turtle.done()

# In an interactive session, you can use the turtle.pos() command to display the turtle's current position

# You can also use the turtle.xcor() command to display just the turtle's X coordinate and the turtle.ycor() command
# to display just the turtle's X coordinate
