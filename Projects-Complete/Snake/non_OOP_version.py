from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game.exe")

# Task 1: Create Snake Body
# starting_position = [(0,0),(-20,0),(-40,0)]
# segments = []
game_is_on = True
snake = Snake()

# for position in starting_position:
#     segment = Turtle()
#     segment.color("white")
#     segment.shape("square")
#     segment.penup()
#     segment.goto(position)
#     segments.append(segment)

# Task 2: Move the snake

while game_is_on:
    screen.update()
    time.sleep(0.5)
    # we want the last segment to move to position of the 
    # second segment, and the second segment to move to the
    # position of the first segment
    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(x=new_x, y=new_y)
    # segments[0].forward(20)
    snake.move()



screen.exitonclick()