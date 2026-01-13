import smtplib
import pandas as pd
import datetime as dt
import pathlib
import random

# -------- constants --------
BASE_DIR = pathlib.Path(__file__).parent
BIRTHDAYS_FILE = BASE_DIR / "birthdays.csv"
LETTER_TEMPLATES_DIR = BASE_DIR / "letter_templates"
GMAIL_SMTP = "smtp.gmail.com"
PORT = 587
MY_EMAIL = "100daysofcodeproject@gmail.com"
MY_PASSWORD = "flhitjcbrwhfybmx"

# -------- functions ---------
def choose_random_letter():
    random_letter_path = random.choice(list(LETTER_TEMPLATES_DIR.glob("*.txt")))
    return random_letter_path

def send_birthday_email(to_email: str, subject: str, body: str):
    with smtplib.SMTP(GMAIL_SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{body}"
                            )
    print("Email successfully sent!")

# -------- code --------
now = dt.datetime.now()
todays_date = (now.month, now.day)
birthdays_data = pd.read_csv(BIRTHDAYS_FILE)
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_data.iterrows()
    }

if todays_date in birthdays_dict:
    print("today is someone's birthday")
    with open(file=choose_random_letter()) as letter_file:
        letter_contents = letter_file.read()
    
    # in case there are multiple people with the same birthday
    todays_birthdays = birthdays_data[(birthdays_data["month"] == now.month) & 
                                      (birthdays_data["day"] == now.day)]

    for index, birthday_person in todays_birthdays.iterrows():
        customized_letter = letter_contents.replace("[NAME]", birthday_person["name"])
        send_birthday_email(to_email=birthday_person["email"],
                            subject=f"Happiest of Birthdays to {birthday_person['name']}!",
                            body=customized_letter)
else:
    print("today is not anyone's birthday")