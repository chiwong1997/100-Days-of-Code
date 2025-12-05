from tkinter import *
from pathlib import Path
import random

BASE_DIR = Path(__file__).parent

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    random_letters = [random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(random.randint(8, 10))]
    random_symbols = [random.choice('!#$%&()*+') for _ in range(random.randint(2,4))]
    random_numbers = [random.choice('0123456789') for _ in range(random.randint(2,4))]
    password_list = random_letters + random_symbols + random_numbers
    print(password_list)
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open(BASE_DIR / "password_manager.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #
# Window - Password Manager
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=500, height=500)

# Canvas - Password Logo
canvas = Canvas(width=200, height=200)
file_path = BASE_DIR / "logo.png"
logo_img = PhotoImage(file=file_path)
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# Label - Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Label - Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Label - Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry - Website
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

# Entry - Email/Username
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

# Entry - Password
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button - Generate Password
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Button - Add
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()