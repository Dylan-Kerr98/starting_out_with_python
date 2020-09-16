# The turtle.speed(speed) command is used to change the speed at which that turtle moves, the speed is passed to the
# command as an argument

# The speed argument is a number in the range if 0 through 10

#  If you specify 0, then the turtle will make all of its moves instantly (animation is disabled)
import turtle

turtle.speed(0)
turtle.circle(100)

turtle.done()

# If you specify a speed value in the range of 1 through 10, then 1 is the slowest speed, and 10 is the fastest

# In interactive mode you can get the turtle's current animation speed with the turtle.speed() command with no
# argument passed to it

# If you don't want the turtle to be displayed, you can use the turtle.hideturtle() command to do this.
# This does not change the way graphics are drawn, it simple hides the turtle icon
# When you want to display it again, use the turtle.showturtle() command

