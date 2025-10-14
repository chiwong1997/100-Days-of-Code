from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 60, 'normal')
GAME_OVER_FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def score_left(self):
        self.l_score += 1
    
    def score_right(self):
        self.r_score += 1

    def game_over(self):
        self.home()
        if self.l_score > self.r_score:
            self.write(f"Game over - left player wins with score of {self.l_score}", align=ALIGNMENT, font=GAME_OVER_FONT)
        else:
            self.write(f"Game over - right player wins with score of {self.r_score}", align=ALIGNMENT, font=GAME_OVER_FONT)