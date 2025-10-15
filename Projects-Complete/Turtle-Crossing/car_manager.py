from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 1
CAR_LENGTH = 2

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create one new car and append to list all_cars"""
        random_chance = random.randint(1,4)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shape('square')
            new_car.shapesize(stretch_wid=CAR_WIDTH,stretch_len=CAR_LENGTH)
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
