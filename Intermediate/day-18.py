import turtle
import random

# from turtle import Turtle()
# from turtle import * - avoid this as it makes it confusing when coding
# import turtle as t - alias'es are good to use 

# to change the colormode, we need to tap into the actual turtle module, not the turtle object
turtle.colormode(255)

tim = turtle.Turtle()
tim.shape('turtle')
tim.color('black', 'green')
tim.speed('fastest')
tim.pensize(1)

# Challenge 1: Draw a square 
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2: Draw a dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3: Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon 
# with different colors
# for sides in range(3,11):
#     angle = 360/sides
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     tim.pencolor((r,g,b))
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(angle)

# Challenge 4: Generate a random walk (random movements)
# directions = [0, 90, 180, 270]
# num_steps = 200
# step_length = 50

# for _ in range(num_steps):
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     tim.pencolor((r,g,b))
#     chosen_direction = random.choice(directions)
#     tim.setheading(chosen_direction)
#     tim.forward(step_length)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_code = (r,g,b)
    return rgb_code

# Tuples are immutable - they are used for when you want something to stay constant
my_tuple = (1,5,10,20)
print(my_tuple[2])
print(my_tuple[3])
# convert tuple to list
my_list = list(my_tuple)
print(my_list)

# Challenge 5: Draw a Spirograph

def draw_spirograph(size_of_gap):
    radius = 100
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(radius)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()