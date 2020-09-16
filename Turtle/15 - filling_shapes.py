# To fill a shape with a colour, you can use the turtle.begin_fill() command before drawing the shape, then you use
# the turtle.end_fill() command after the shape is drawn
# When this executes the shape will be filled with the current fill colour
# The fill color is passed to the command as an argument

import turtle

turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.done()

