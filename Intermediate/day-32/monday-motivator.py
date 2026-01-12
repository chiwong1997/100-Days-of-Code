import pathlib
import smtplib
import datetime
import random

# --- opening the file ---
BASE_DIR = pathlib.Path(__file__).parent
file_path = BASE_DIR / "quotes.txt"

# --- constants ---
GMAIL_SMTP = "smtp.gmail.com"
PORT = 587
MY_EMAIL = "100daysofcodeproject@gmail.com"
MY_PASSWORD = "flhitjcbrwhfybmx"
EMAIL_LIST = "xxx@gmail.com"

# --- functions ---
def text_processing(raw):
    quotes_dict = {}
    for quote in raw:
        try:
            quote_text, author = quote.split(' - ')
        except ValueError:
            # skip quotes that contain " - " in the text of the quote body
            continue
        else:
            quote_text = quote_text.strip('"').strip()
            quotes_dict[author.strip()] = quote_text

    return quotes_dict

def choose_random_quote(dictionary_of_quotes):
    authors = list(dictionary_of_quotes.keys())
    random_author = random.choice(authors)
    random_quote = dictionary_of_quotes[random_author]
    return random_quote, random_author

def check_monday():
    now = datetime.datetime.now()
    if now.weekday() == 0:
        return True
    return False

# --- code ---
raw_text = []
with open(file=file_path) as file:
    raw_text = file.readlines()

is_monday = check_monday()
print(is_monday)

if is_monday == True:
    print("an email will be sent")
    quotes = text_processing(raw=raw_text)
    author_of_the_day, quote_of_the_day = choose_random_quote(dictionary_of_quotes=quotes)
    with smtplib.SMTP(GMAIL_SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=EMAIL_LIST,
                            msg=f"Subject:Monday Motivator\n\n{quote_of_the_day} - {author_of_the_day}"
                            )