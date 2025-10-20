import pandas as pd
from pathlib import Path
from statewriter import StateWriter
import turtle

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "50_states.csv"
BG_IMG_FILE = BASE_DIR / "blank_states_img.gif"
US_STATES_COUNT = 50

# Read states data
data = pd.read_csv(DATA_FILE)
states_list = data.state.str.lower().to_list()

# Set up screen
screen = turtle.Screen()
screen.title("US State Game")
screen.setup(width=725, height=491)
screen.bgpic(BG_IMG_FILE)

statewriter = StateWriter()

guessed_states = []
game_is_on = True

while len(guessed_states) < US_STATES_COUNT and game_is_on:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 correct", 
                                  prompt="What is your guess? ")
    # If user types exit or exits the text input, exit the game
    if answer_state.lower() == "exit" or answer_state is None:
        game_is_on = False
        break
    # If user types the wrong answer, continue the game
    answer_state = answer_state.lower()
    if answer_state not in states_list:
        continue
    # If user types the correct answer, write the state name on the map
    else:
        state_data = data[data.state.str.lower() == answer_state] # pulls out a row of data
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        # Get the state name from the series with the item() method
        state_name = state_data.state.item()
        guessed_states.append(answer_state)
        statewriter.write_state(state_name=state_name, x=x_cor, y=y_cor)
    
# Create a list of states to learn
missing_states = []
for state in states_list:
    if state not in guessed_states:
        missing_states.append(state.capitalize())

# Save the missing states to a CSV file
missing_states_data = {'Missing States': missing_states}
missing_states_df = pd.DataFrame(missing_states_data)
missing_states_df.to_csv(BASE_DIR / "missed_states.csv")

screen.exitonclick()