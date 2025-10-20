from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 8, 'normal')

class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name, align=ALIGN, font=FONT)