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
words_to_learn_file_path = BASE_DIR / "data/words_to_learn.csv"

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 32, "italic")
WORD_FONT = ("Ariel", 60, "bold")
RESET_FONT = ("Ariel", 12, "bold")
LANGUAGE = "French"
ENGLISH = "English"
current_card = {}
to_learn = {}

# Functions
def change_word():
    global current_card
    global flip_timer
    # Invalidate the previous timer
    window.after_cancel(flip_timer)
    index = random.randint(0, len(to_learn) - 1)
    current_card = to_learn[index]
    # Update the card with the new LANGUAGE word
    card_front_canvas.itemconfig(word_text, text=current_card[LANGUAGE], fill="black")
    card_front_canvas.itemconfig(title_text, text = LANGUAGE, fill="black")
    card_front_canvas.itemconfig(card_background, image=card_front_image)
    # Set up a new timer so it will wait 3 seconds before flipping
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    # Update the card with the corresponding ENGLISH word (after 3 seconds)
    card_front_canvas.itemconfig(title_text, text=ENGLISH, fill="white")
    card_front_canvas.itemconfig(word_text, text=current_card[ENGLISH], fill="white")
    card_front_canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv(words_to_learn_file_path, index=False)
    change_word()

def reset():
    global to_learn
    original_df = pd.read_csv(data_file_path)
    to_learn = original_df.to_dict(orient="records") 
    pd.DataFrame(to_learn).to_csv(words_to_learn_file_path, index=False)


# ------------------- Data Loading ------------------
try:
    df = pd.read_csv(words_to_learn_file_path) # converts to a list of dictionaries
except FileNotFoundError:
    # this error will occur if the words_to_learn file does not exist (first time running the program or accidental deletion)
    original_df = pd.read_csv(data_file_path)
    to_learn = original_df.to_dict(orient="records") # converts to a list of dictionaries
else:
    to_learn = df.to_dict(orient="records")

# ------------------ UI Setup ------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

# Flash Card Canvas
card_front_image = PhotoImage(file=card_front_image_path)
card_back_image = PhotoImage(file=card_back_image_path)
card_front_canvas = Canvas(width=800, height=526)
card_background = card_front_canvas.create_image(400, 263, image=card_front_image)
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
right_button = Button(image=right_image, highlightthickness=0, command = is_known)
right_button.grid(column=1, row=1)

# Reset Button
reset_button = Button(text="RESET PROGRESS", width=16, font=RESET_FONT,command = reset)
reset_button.grid(column=0, row=2, columnspan=2)

change_word()

window.mainloop()