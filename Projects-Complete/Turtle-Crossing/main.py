import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

UP = "Up"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, UP)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car and move forward
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car 
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing - speed up cars for next level
    if player.is_at_finish_line():
        player.return_to_start()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()