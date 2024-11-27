"""
Project Name: Baubles
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
# Make the pensize 10
turtle.pensize(10)

# Draw the big circle the colour red
turtle.penup()
turtle.setposition(105, 0)
turtle.color("red", "red")
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(105)
turtle.end_fill()

# Draw the two golden lines
turtle.penup()
turtle.color("gold", "gold")
turtle.setposition(-95, 50)
turtle.pendown()
turtle.setposition(95, 50)
turtle.penup()
turtle.setposition(-95, -50)
turtle.pendown()
turtle.setposition(95, -50)

# Draw the bauble holder
turtle.color("black", "black")
turtle.pensize(10)
turtle.penup()
turtle.setposition(25, 125)
turtle.setheading(90)
turtle.pendown()
turtle.circle(25, 180)

# Draw the top of the bauble
turtle.penup()
turtle.color("green", "green")
turtle.setposition(40, 100)
turtle.setheading(270)
turtle.begin_fill()
turtle.circle(-20, 180)
turtle.penup()
turtle.setheading(270)
turtle.setposition(0, 100)
turtle.circle(-20, 180)
turtle.setheading(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(25)
turtle.end_fill()
    
# End the program
turtle.hideturtle()
