from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

STARTING_POSITION_1 = (350,0)
STARTING_POSITION_2 = (-350,0)

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong.exe")
screen.tracer(0)

r_paddle = Paddle(STARTING_POSITION_1)
l_paddle = Paddle(STARTING_POSITION_2)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()