from turtle import Turtle

MOVE_DISTANCE = 20
Y_UPPER_LIMIT = 280
Y_LOWER_LIMIT = -280

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(starting_position)
        # self.start_position = starting_position
        # self.create_paddle()

    # def create_paddle(self):
    #     paddle = Turtle('square')
    #     paddle.color('white')
    #     paddle.shapesize(stretch_wid=5,stretch_len=1)
    #     paddle.penup()
    #     paddle.goto(self.start_position)

    def go_up(self):
        if self.ycor() <= Y_UPPER_LIMIT:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= Y_LOWER_LIMIT:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)