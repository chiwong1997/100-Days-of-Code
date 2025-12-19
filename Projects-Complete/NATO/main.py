import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
alphabet = pd.read_csv(BASE_DIR / 'nato_phonetic_alphabet.csv')

# Method 1: Doing this by iterating through a DF using dictionary comprehension
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}

# Method 2: Doing this manually
# alphabet_dict = alphabet.set_index(['letter'])['code'].to_dict()

def generate_phonetic():
    user_input = input("What is your name?: ").upper()
    try:
        output_list = [alphabet_dict[item] for item in user_input]
    except KeyError:
        print("Sorry - only letters allowed as user input")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()