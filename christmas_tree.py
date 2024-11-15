"""
Project Name: Christmas Tree
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
# Lift up the pen
turtle.penup()

# Draw the star
turtle.color("gold", "gold")
turtle.setposition(0, 175)
turtle.pendown()
turtle.begin_fill()
turtle.setposition(-10, 155)
turtle.setposition(-30, 155)
turtle.setposition(-15, 140)
turtle.setposition(-20, 115)
turtle.setposition(0, 125)
turtle.setposition(20, 115)
turtle.setposition(15, 140)
turtle.setposition(30, 155)
turtle.setposition(10, 155)
turtle.setposition(0, 175)
turtle.end_fill()

# Lift up the pen
turtle.penup()

# Draw the tree leaves
turtle.color("green", "green")
turtle.setposition(0, 120)
turtle.pendown()
turtle.begin_fill()
turtle.setposition(-90, -120)
turtle.setposition(90, -120)
turtle.setposition(0, 120)
turtle.end_fill()

# Lift up the pen
turtle.penup()

# Draw the tree trunk
turtle.color("brown", "brown")
turtle.setposition(-20, -120)
turtle.pendown()
turtle.begin_fill()
turtle.setposition(-20, -165)
turtle.setposition(20, -165)
turtle.setposition(20, -120)
turtle.setposition(-20, -120)
turtle.end_fill()

def draw_circle(x_pos, y_pos, radius, colour):
    # Lift up the pen
    turtle.penup()

    # Move the turtle to the position you want to draw it to minus the radius
    turtle.setposition(x_pos - radius, y_pos)

    # Change the colour of the turtle
    turtle.color(colour, colour)

    # Place the pen down
    turtle.pendown()

    # Begin the fill
    turtle.begin_fill()

    # Draw the circle
    turtle.circle(radius)

    # End the fill
    turtle.end_fill()

# Draw the decorations as circles
draw_circle(-50, -95, 10, "red")
draw_circle(-30, -30, 10, "grey")
draw_circle(10, 35, 10, "gold")
draw_circle(-5, -65, 10, "red")
draw_circle(15, 0, 10, "grey")
draw_circle(30, -45, 10, "gold")
draw_circle(45, -95, 10, "red")
 
# End the program
turtle.hideturtle()
