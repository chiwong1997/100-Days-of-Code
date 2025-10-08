from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: ")
color_list = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
y_coordinates = [150, 90, 30, -30, -90, -150]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost. The {winning_color} turtle won the race.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


# tim = Turtle(shape='turtle')
# tim.color('red')
# tim.penup()
# tim.goto(x=-230, y=150)

# tom = Turtle(shape='turtle')
# tom.color('blue')
# tom.penup()
# tom.goto(x=-230, y=90)

# jim = Turtle(shape='turtle')
# jim.color('yellow')
# jim.penup()
# jim.goto(x=-230, y=30)

# dwight = Turtle(shape='turtle')
# dwight.color('green')
# dwight.penup()
# dwight.goto(x=-230, y=-30)

# pam = Turtle(shape='turtle')
# pam.color('purple')
# pam.penup()
# pam.goto(x=-230, y=-90)

# kev = Turtle(shape='turtle')
# kev.color('orange')
# kev.penup()
# kev.goto(x=-230, y=-150)

screen.exitonclick()