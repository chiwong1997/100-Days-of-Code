import tkinter
from pathlib import Path
from quiz_brain import QuizBrain

# ---- constants ----
THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")
BASE_DIR = Path(__file__).parent
RIGHT_FP = BASE_DIR / "images/true.png"
WRONG_FP = BASE_DIR / "images/false.png"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1,row=0)

        # Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, 
                                                     width = 280,
                                                     text="some question text", 
                                                     font = FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        # Right Button
        right_button_img = tkinter.PhotoImage(file=RIGHT_FP)
        self.right_button = tkinter.Button(image=right_button_img, 
                                           highlightthickness=0,
                                           command=self.true_pressed)
        self.right_button.grid(column=0, row=3)

        # Wrong Button
        wrong_button_img = tkinter.PhotoImage(file=WRONG_FP)
        self.wrong_button = tkinter.Button(image=wrong_button_img, 
                                           highlightthickness=0,
                                           command=self.false_pressed)
        self.wrong_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,  text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz!\n\nYour score is {self.quiz.score}/10")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)