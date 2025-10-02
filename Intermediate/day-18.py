import turtle
from random import randint

# from turtle import Turtle()
# from turtle import * - avoid this as it makes it confusing when coding
# import turtle as t - alias'es are good to use 

turtle.colormode(255)
tim = turtle.Turtle()
tim.shape('turtle')
tim.color('black', 'green')

# Draw a square 
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon 
# with different colors
for sides in range(3,11):
    angle = 360/sides
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    tim.pencolor((r,g,b))
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)

screen = turtle.Screen()
screen.exitonclick()