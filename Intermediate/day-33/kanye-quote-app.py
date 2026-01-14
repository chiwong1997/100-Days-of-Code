from tkinter import *
import requests
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
BACKGROUND_IMG_FILE_PATH = BASE_DIR / "background.png"
KANYE_ICON_FILE_PATH = BASE_DIR / "kanye.png"
CANVAS_FONT = ("Arial", 14, "bold")

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND_IMG_FILE_PATH)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="kanye quote goes here", width=250, font=CANVAS_FONT, fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_ICON_FILE_PATH)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()