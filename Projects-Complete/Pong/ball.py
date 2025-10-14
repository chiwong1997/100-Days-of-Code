from turtle import Turtle

BALL_DISTANCE = 10
STARTING_MOVE_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = BALL_DISTANCE
        self.y_move = BALL_DISTANCE
        self.move_speed = STARTING_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        """On miss, return ball to center, change back speed, and send ball to other player"""
        self.home()
        self.move_speed = STARTING_MOVE_SPEED
        self.bounce_x()