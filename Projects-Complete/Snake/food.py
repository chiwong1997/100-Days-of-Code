from turtle import Turtle
import random

# We want the Food Class to inherit from the Turtle class
# so that we can use all the methods and attributes of the Turtle class

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #creates a 10x10 circle
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)