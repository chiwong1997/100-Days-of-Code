from tkinter import *
from pathlib import Path

BASE_DIR = Path(__file__).parent

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas class allows you to place images onto the screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
file_path = BASE_DIR / 'tomato.png'
tomato_img = PhotoImage(file=file_path)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

# Label 1 - Timer
timer = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(column=2, row=1)

# Button 1 - Start 
start = Button(text='start', font=(FONT_NAME, 10, 'normal'))
start.grid(column=1, row=3)

# Button 2 - Reset
reset = Button(text='reset', font=(FONT_NAME, 10, 'normal'))
reset.grid(column=3, row=3)

# Label 2 - Tick
tick = Label(text = '✔', font=(FONT_NAME, 16, 'bold'), fg=GREEN, bg=YELLOW)
tick.grid(column=2, row=4)

window.mainloop()