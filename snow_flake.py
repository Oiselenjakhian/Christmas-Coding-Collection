"""
Project Name: Snow Flake
Developer Name: Truston Ailende
Email Address: trustonailende@gmail.com
"""
import turtle
import math
 
# Square
def drawSquare(length):
    turtle.penup()
    turtle.setposition(-length/2.0, length/2.0)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()
    turtle.home()
 
# Horizontal lines
def drawHorizontalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    for j in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(-half, j)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Vertical lines
def drawVerticalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    turtle.right(90)
    for k in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(k, half)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Draw the grid
turtle.speed(0)
drawSquare(400)
drawHorizontalLine(400, 40)
drawVerticalLine(400, 40)
 
# Change the colour mode
turtle.colormode(255)
 
# Change the pencolor to red
turtle.pencolor(255, 0, 0)
 
# Draw the horizontal centre line
turtle.setposition(-200, 0)
turtle.pendown()
turtle.forward(400)
turtle.penup()
 
# Draw the vertical centre line
turtle.setposition(0, 200)
turtle.setheading(270)
turtle.pendown()
turtle.forward(400)
 
# Reset all the properties
turtle.home()
turtle.pencolor(0, 0, 0)
 
# Place code here
def draw_dendrite(heading):
    # Lift up the pen
    turtle.penup()
    
    # Move the turtle back to its home position of (0, 0)
    turtle.home()

    # Set the heading of the turtle
    turtle.setheading(heading)

    # Move the turtle forward by 25 pixels
    turtle.forward(25)

    # Place the pen down
    turtle.pendown()

    # Draw the core of the dendrite
    turtle.forward(140)

    # Move back by 90 pixels
    turtle.back(90)

    # Set the heading to the sum of 90 and the current heading
    turtle.setheading(90 + heading)

    # Draw a line forward
    turtle.forward(20)

    # Move back by 40 pixels
    turtle.back(40)

    # Move forward by 20 to get the turtle back on the main line
    turtle.forward(20)

    # Set the heading to its original value
    turtle.setheading(heading)

    # Move the turtle forward by 10 pixels
    turtle.forward(10)

    # Set the heading of the turtle to 45 degrees plus its current value
    turtle.setheading(45 + heading)

    # Move the turtle forward
    turtle.forward(60)

    # Move the turtle backward
    turtle.back(60)

    # Set the heading of the turtle to the current heading minus 45
    turtle.setheading(heading - 45)

    # Move the turtle forward
    turtle.forward(60)

    # Move the turtle back
    turtle.back(60)

    # Set the heading of the turtle
    turtle.setheading(heading)

    # Move the turtle forward
    turtle.forward(40)

    # Set the heading of the turtle to 45 degrees plus its current value
    turtle.setheading(45 + heading)

    # Move the turtle forward
    turtle.forward(45)

    # Move the turtle backward
    turtle.back(45)

    # Set the heading of the turtle to the current heading minus 45 
    turtle.setheading(heading - 45)

    # Move the turtle forward
    turtle.forward(45)

# Change the pen colour to a blue hue
turtle.pencolor(17, 108, 172)

# Increase the pensize to 15 pixels
turtle.pensize(15)

# Lift up the pen
turtle.penup()

# Move the turtle to the position (25, 0)
turtle.setposition(25, 0)

# Set the heading of the turtle
turtle.setheading(90)

# Place the pen down
turtle.pendown()

# Draw a circle of radius 25 pixels
turtle.circle(25)

# Draw the dendrites
draw_dendrite(30)
draw_dendrite(90)
draw_dendrite(150)
draw_dendrite(210)
draw_dendrite(270)
draw_dendrite(330)

# End the program
turtle.hideturtle()
