"""
Project Name: Drinking Glasses
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
# Set the pen size to 10
turtle.pensize(10)

# Draw lines in the symbol
def draw_line(x1, y1, x2, y2):
    # Lift up the pen
    turtle.penup()

    # Move the pen to the position x1, y1
    turtle.setposition(x1, y1)

    # Place the pen down
    turtle.pendown()

    # Draw the line
    turtle.setposition(x2, y2)

# Draw circles in the symbol
def draw_circle(x_pos, y_pos, radius, extent):
    # Lift up the pen
    turtle.penup()

    # Change the heading of the pen
    turtle.setheading(270)

    # Move the pen to the location x_pos y_pos
    turtle.setposition(x_pos, y_pos)

    # Place the pen down
    turtle.pendown()

    # Draw the circle
    turtle.circle(radius, extent)

# Draw the horizontal lines the first cup
draw_line(-155, 155, -35, 155)
draw_line(-155, 135, -35, 135)
draw_line(-145, -135, -45, -135)

# Draw the vertical lines for the first cup
draw_line(-155, 155, -155, 20)
draw_line(-35, 155, -35, 20)
draw_line(-95, -40, -95, -135)

# Draw the semicircle for the first cup
draw_circle(-35, 20, -60, 180)

# Draw the bubbles for the first cup
draw_circle(-125, 75, 10, 360)
draw_circle(-95, 15, 10, 360)
draw_circle(-85, 105, 10, 360)

# Draw the horizontal lines the second cup
draw_line(35, 155, 155, 155)
draw_line(35, 135, 155, 135)
draw_line(45, -135, 145, -135)

# Draw the vertical lines for the second cup
draw_line(35, 155, 35, 20)
draw_line(155, 155, 155, 20)
draw_line(95, -40, 95, -135)

# Draw the semicircle for the second cup
draw_circle(155, 20, -60, 180)

# Draw the bubbles for the second cup
draw_circle(65, 75, 10, 360)
draw_circle(95, 15, 10, 360)
draw_circle(105, 105, 10, 360)

# End the program
turtle.hideturtle()
