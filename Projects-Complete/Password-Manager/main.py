from tkinter import *
from tkinter import messagebox
from pathlib import Path
import random
import pyperclip
import json

BASE_DIR = Path(__file__).parent
file_path_text = BASE_DIR / "password_manager.txt"
file_path_json = BASE_DIR / "password_manager.json"
print(file_path_text)
MY_EMAIL = "chiyinwong97@gmail.com"

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
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
        }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Field", message="Some fields are empty, please recheck.")
    else:
        is_ok = messagebox.askokcancel(title=f"Details for {website}", 
                                       message=f"These are the details entered: \nEmail:{email} \nPassword:{password}\n Is it ok to save?")
        if is_ok == TRUE:
            # with open(file_path_text, "a") as data_file:
            #     data_file.write(f"{website} | {email} | {password}\n")
            #     website_entry.delete(0, END)
            #     password_entry.delete(0, END)
            try:
                with open(file_path_json, "r") as data_file:
                    # Reading old data from json file
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file_path_json, "w") as data_file:
                    # Creating json file if it doesn't exist and writing data into it
                    json.dump(new_data, data_file, indent = 4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open(file_path_json, "w") as data_file:
                    # Writing new data back to the json file
                    json.dump(data, data_file, indent = 4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ------------- SEARCH FUNCTIONALITY -------------------

def search():
    website = website_entry.get()
    try:
        with open(file_path_json, "r") as data_file:
            passwords = json.load(data_file)

        email_password_dict = passwords[website]
        email = email_password_dict["email"]
        password = email_password_dict["password"]
        messagebox.showinfo(title=f"Password for {website}",
                            message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="No passwords saved yet",
                             message="There are currently no passwords saved yet, please save first.")
    except KeyError:
        messagebox.showerror(title="No password saved",
                             message = f"No data found for {website}")
        
    ### An easier way to write the above code - for reference, as it seems cleaner and easier to follow: 

    # website = website_entry.get()
    # try:
    #     with open(file_path_json, "r") as data_file:
    #         passwords = json.load(data_file)
    # except FileNotFoundError:
    #     messagebox.showerror(title="Error", message="No data file found")
    # else:
    #     if website in passwords:
    #         email=passwords[website]["email"]
    #         password = passwords[website]["password"]
    #         messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
    #     else:
    #         messagebox.error(title="Error", message=f"No details for {website} found.")

# ---------------------------- UI SETUP ------------------------------- #
# Window - Password Manager
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=500, height=500)

# Canvas - Password Logo
canvas = Canvas(width=200, height=200)
file_path_logo = BASE_DIR / "logo.png"
logo_img = PhotoImage(file=file_path_logo)
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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Entry - Email/Username
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, MY_EMAIL)

# Entry - Password
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button - Generate Password
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Button - Add
add_button = Button(text="Add", width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Button - Search
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

window.mainloop()