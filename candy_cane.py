"""
Project Name: Candy Cane
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
# Set the pen size to 10 pixels
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
def draw_circle(x_pos, y_pos, radius, extent, heading):
    # Lift up the pen
    turtle.penup()

    # Change the heading of the pen
    turtle.setheading(heading)

    # Move the pen to the location x_pos y_pos
    turtle.setposition(x_pos, y_pos)

    # Place the pen down
    turtle.pendown()

    # Draw the circle
    turtle.circle(radius, extent)

# Draw the lines on the candy cane
def draw_candy_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    turtle.penup()
    turtle.begin_fill()
    turtle.setposition(x1, y1)
    turtle.pendown()
    turtle.setposition(x3, y3)
    turtle.setposition(x4, y4)
    turtle.setposition(x2, y2)
    turtle.setposition(x1, y1)
    turtle.end_fill()

# Draw the vertical lines
draw_line(-45, 100, -45, -135)
draw_line(0, 100, 0, -135)
draw_line(50, 65, 50, 100)
draw_line(95, 65, 95, 100)

# Draw the circles
draw_circle(0, -135, -22.5, 180, 270)
draw_circle(95, 65, -22.5, 180, 270)
draw_circle(95, 100, 70, 180, 90)
draw_circle(50, 100, 25, 180, 90)

# Set the pensize to 1
turtle.pensize(1)

# Draw the candy lines
draw_candy_lines(-40, -130, -10, -155, -40, -90, 0, -120)
draw_candy_lines(-40, -45, 0, -75, -40, -5, 0, -40)
draw_candy_lines(-40, 40, 0, 5, -40, 80, 0, 40)
draw_candy_lines(-40, 130, 0, 90, -25, 150, 5, 120)
draw_candy_lines(10, 165, 90, 85, 40, 170, 90, 120)
draw_candy_lines(60, 50, 80, 45, 50, 75, 85, 40)
 
# End the program
turtle.hideturtle()
