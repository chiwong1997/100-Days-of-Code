from tkinter import *
from pathlib import Path
import math

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
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text = "00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_seconds)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_seconds)
        timer.config(text="Break", fg=PINK)
    else:
        countdown(work_seconds)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count/60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_seconds}")

    if count > 0:
        global time
        time = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        tick.config(text=marks)

        
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label 1 - Timer
timer = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(column=2, row=1)

# Canvas class allows you to place images onto the screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
file_path = BASE_DIR / 'tomato.png'
tomato_img = PhotoImage(file=file_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)



# Button 1 - Start 
start = Button(text='start', font=(FONT_NAME, 10, 'normal'), command=start_timer)
start.grid(column=1, row=3)

# Button 2 - Reset
reset = Button(text='reset', font=(FONT_NAME, 10, 'normal'), command = reset_timer)
reset.grid(column=3, row=3)

# Label 2 - Tick
tick = Label(font=(FONT_NAME, 16, 'bold'), fg=GREEN, bg=YELLOW)
tick.grid(column=2, row=4)

window.mainloop()