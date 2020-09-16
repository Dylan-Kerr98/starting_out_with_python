# Orion is one of the most famous constellations in the night sky
# The top most stars are Orion's shoulders, the row of three stars in the middle are Orion's belt
# The bottom two stars are Orion's knees

# This program will display the stars, star names and the constellation lines

import turtle

# Set window size
turtle.setup(500, 500)

# Setup the turtle
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELT_STAR_X = -40
LEFT_BELT_STAR_Y = -20

MIDDLE_BELT_STAR_X = 0
MIDDLE_BELT_STAR_Y = 0

RIGHT_BELT_STAR_X = 40
RIGHT_BELT_STAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw & name the stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)          # Left shoulder star
turtle.dot()
turtle.write("Betegeuse")
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)        # Right shoulder star
turtle.dot()
turtle.write("Miessa")
turtle.goto(LEFT_BELT_STAR_X, LEFT_BELT_STAR_Y)        # Left belt star
turtle.dot()
turtle.write("Alnitak")
turtle.goto(MIDDLE_BELT_STAR_X, MIDDLE_BELT_STAR_Y)    # Middle belt star
turtle.dot()
turtle.write("Alnilam")
turtle.goto(RIGHT_BELT_STAR_X, RIGHT_BELT_STAR_Y)      # Right belt star
turtle.dot()
turtle.write("Mintaka")
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)                  # Left knee star
turtle.dot()
turtle.write("Saiph")
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)                # Right knee star
turtle.dot()
turtle.write("Rigel")

# Draw a line from left shoulder to left belt star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELT_STAR_X, LEFT_BELT_STAR_Y)
turtle.penup()

# Draw a line from right shoulder to right belt star
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELT_STAR_X, RIGHT_BELT_STAR_Y)
turtle.penup()

# Draw a line from left belt star to middle belt star
turtle.goto(LEFT_BELT_STAR_X, LEFT_BELT_STAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELT_STAR_X, MIDDLE_BELT_STAR_Y)

# Draw a line from middle belt star to right belt star
turtle.goto(RIGHT_BELT_STAR_X, RIGHT_BELT_STAR_Y)
turtle.penup()

# Draw a line from left belt star to left knee
turtle.goto(LEFT_BELT_STAR_X, LEFT_BELT_STAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Draw a line from right belt star to right knee
turtle.goto(RIGHT_BELT_STAR_X, RIGHT_BELT_STAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

# Keep the window open.
turtle.done()
