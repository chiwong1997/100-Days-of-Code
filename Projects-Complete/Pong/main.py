from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITION_R = (350,0)
STARTING_POSITION_L = (-350,0)

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong.exe")
screen.tracer(0)

r_paddle = Paddle(STARTING_POSITION_R)
l_paddle = Paddle(STARTING_POSITION_L)
ball = Ball()
scoreboard = Scoreboard()
sleep_time = 0.1

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.update_score()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print('contact')
        ball.bounce_x()

    # Detect if R paddle misses
    if ball.xcor() > 380:
        print('missed')
        ball.reset_position()
        scoreboard.score_left()
    
    # Detect if L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_right()

    # Detect if score is 7
    if scoreboard.l_score == 7 or scoreboard.r_score == 7:
        scoreboard.update_score()
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()