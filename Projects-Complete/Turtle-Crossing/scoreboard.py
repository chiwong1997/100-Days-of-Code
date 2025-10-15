from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")
GAME_OVER_MESSAGE= "Game Over"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.goto(-200,250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.current_level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write(GAME_OVER_MESSAGE, align=ALIGNMENT, font=FONT)
