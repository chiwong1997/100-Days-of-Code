from tkinter import *
from pathlib import Path

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

# ------------------ UI Setup ------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Canvas
card_front_image = PhotoImage(file=card_front_image_path)
card_front_canvas = Canvas(width=800, height=526)
card_front_canvas.create_image(400, 263, image=card_front_image)
card_front_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_front_canvas.create_text(400, 263, text="Word", font=WORD_FONT)
card_front_canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
wrong_image = PhotoImage(file=wrong_image_path)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Right Button
right_image = PhotoImage(file=right_image_path)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()