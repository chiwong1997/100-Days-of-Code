from turtle import Turtle
from pathlib import Path

SCORE_POSITION = (0,280)
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with FILE_PATH.open(mode = "r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCORE_POSITION)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()

    def update_highscore(self):
        with FILE_PATH.open(mode="w") as file:
            file.write(str(self.high_score))