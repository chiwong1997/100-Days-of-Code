from tkinter import *
from pathlib import Path
import pandas as pd
import random

# File Opening
BASE_DIR = Path(__file__).parent
data_file_path = BASE_DIR / "data/french_words.csv"
card_front_image_path = BASE_DIR / "images/card_front.png"
card_back_image_path = BASE_DIR / "images/card_back.png"
right_image_path = BASE_DIR / "images/right.png"
wrong_image_path = BASE_DIR / "images/wrong.png"

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 32, "italic")
WORD_FONT = ("Ariel", 60, "bold")
LANGUAGE = "French"
ENGLISH = "English"

# Functions
def change_word():
    index = random.randint(0, len(df) - 1)
    card_front_canvas.itemconfig(word_text, text=df[index][LANGUAGE])
    card_front_canvas.itemconfig(title_text, text = LANGUAGE)

# ------------------- Data Loading ------------------
df = pd.read_csv(data_file_path).to_dict(orient="records") # converts to a list of dictionaries

# ------------------ UI Setup ------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Canvas
card_front_image = PhotoImage(file=card_front_image_path)
card_front_canvas = Canvas(width=800, height=526)
card_front_canvas.create_image(400, 263, image=card_front_image)
card_front_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = card_front_canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = card_front_canvas.create_text(400, 263, text="", font=WORD_FONT)
card_front_canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
wrong_image = PhotoImage(file=wrong_image_path)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(column=0, row=1)

# Right Button
right_image = PhotoImage(file=right_image_path)
right_button = Button(image=right_image, highlightthickness=0, command = change_word)
right_button.grid(column=1, row=1)

change_word()

window.mainloop()