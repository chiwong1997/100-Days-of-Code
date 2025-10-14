import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

UP = "Up"
cars = []
i = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
for _ in range(30):
    car = CarManager()
    car.starting_position()
    cars.append(car)
screen.listen()
screen.onkey(player.move, UP)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in cars:
        car.move_car()
    screen.update()
    player.check_finished()