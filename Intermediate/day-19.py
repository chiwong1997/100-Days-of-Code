# Instances, State, Higher Order Functions 

import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

# example of higher order functions

# def add(n1, n2):
#     return n1+n2

# def multiply(n1, n2):
#     return n1*n2

# # our higher order function takes another function as an input
# def calculator(n1: int, n2: int, func: function):
#     return func(n1, n2)

# result = calculator (2,3,add)