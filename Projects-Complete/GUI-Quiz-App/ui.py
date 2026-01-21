import tkinter
from pathlib import Path

# ---- constants ----
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
BASE_DIR = Path(__file__).parent
RIGHT_FP = BASE_DIR / "images/true.png"
WRONG_FP = BASE_DIR / "images/false.png"

class QuizInterface:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1,row=0)

        # Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, 
                                                     text="some question text", 
                                                     font = FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        # Right Button
        right_button_img = tkinter.PhotoImage(file=RIGHT_FP)
        self.right_button = tkinter.Button(image=self.right_button_img, highlightthickness=0)
        self.right_button.grid(column=0, row=3)

        # Wrong Button
        wrong_button_img = tkinter.PhotoImage(file=WRONG_FP)
        self.wrong_button = tkinter.Button(image=self.wrong_button_img, highlightthickness=0)
        self.wrong_button.grid(column=1, row=3)

        self.window.mainloop()
