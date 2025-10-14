from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.setheading(180)
    
    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def starting_position(self):
        x = random.randint(-300,300)
        y = random.randint(-250,250)
        self.goto(x,y)
