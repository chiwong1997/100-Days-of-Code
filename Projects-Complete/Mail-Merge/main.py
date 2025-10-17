from pathlib import Path

BASE_DIR = Path(__file__).parent
PLACEHOLDER = '[name]'

start_letter_path = BASE_DIR / "Input/Letters/starting_letter.txt"
names_path = BASE_DIR / "Input/Names/invited_names.txt"
output_path = BASE_DIR / "Output/ReadyToSend"
output_path_str = str(output_path)

def write_to_folder(n_letter: str, guest_name: str):
    """Write a letter to the output folder with the
    guest name in the file name."""
    output_file_name = output_path_str + f"/letter_for_{guest_name}.txt"
    with open(output_file_name, mode="w") as output_file:
        output_file.write(n_letter)

# Save names of invited guest into list
with names_path.open(mode="r") as names_file:
    names = names_file.readlines()

# Open starting letter into text
with start_letter_path.open(mode = "r") as file:
    letter_contents = file.read()

for name in names:
    clean_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, clean_name)
    write_to_folder(new_letter, clean_name)