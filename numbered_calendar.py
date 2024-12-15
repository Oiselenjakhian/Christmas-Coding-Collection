"""
Project Name: Numbered Calendar
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
turtle.delay(500)

# Increase the pen size
turtle.pensize(15)

# Function to draw a line between two points
def draw_line(x1, y1, x2, y2):
    # Lift up the pen
    turtle.penup()

    # Move the turtle to the first position
    turtle.setposition(x1, y1)

    # Place the pen down
    turtle.pendown()

    # Move the turtle to the second position
    turtle.setposition(x2, y2)

def draw_hook(xpos, ypos):
    # Lift up the pen
    turtle.penup()

    # Move to the position
    turtle.setposition(xpos, ypos)

    # Set the heading
    turtle.setheading(180)

    # Place the pen down
    turtle.pendown()

    # Draw a circle
    turtle.circle(25, 90)

    # Move forward by some steps
    turtle.forward(30)

# Draw the horizontal lines
draw_line(-120, 120, 90, 120)
draw_line(-100, 75, 60, 75)
draw_line(-130, -80, 30, -80)
draw_line(-165, -140, 50, -140)
draw_line(80, -140, 160, -140)

# Draw the vertical lines
draw_line(-120, 120, -170, -140)
draw_line(90, 120, 50, -140)
draw_line(90, 120, 160, -140)

# Draw the number 2
draw_line(-90, 35, -45, 35)
draw_line(-45, 35, -55, -5)
draw_line(-55, -5, -95, -5)
draw_line(-95, -5, -100, -40)
draw_line(-100, -40, -60, -40)

# Draw the number 5
draw_line(30, 30, -15, 30)
draw_line(-15, 30, -20, -5)
draw_line(-20, -5, 20, -5)
draw_line(20, -5, 15, -40)
draw_line(15, -40, -30, -40)

# Draw the hooks
draw_hook(-65, 160)
draw_hook(-25, 160)
draw_hook(15, 160)
draw_hook(55, 160)

# End the program
#turtle.hideturtle()
