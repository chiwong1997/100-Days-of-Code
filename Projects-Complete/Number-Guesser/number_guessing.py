import random

EASY = 10
HARD = 5

# Function that checks the answer
def check_answer(guess: int):
    if computer_number < guess:
        print("Too high")
        return True
    if computer_number > guess:
        print("Too low")
        return True
    if computer_number == guess:
        print("Well done!")
        return False

# Aside: a function to set the difficulty - not currently used
def set_difficulty():
    """Function that sets the difficulty level based on user and 
    returns the number of turns as an integer"""
    level = input("Do you want to play in easy or hard mode? ")
    if level == "easy":
        return EASY
    else:
        return HARD

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
computer_number = random.randint(1,100)
print("The computer number is: " + str(computer_number))

# Ask user whether they want to play in easy or hard mode
mode = input("Do you want to play in easy or hard mode?: ")

if mode == "easy":
    number_guesses = EASY
    print(f"You have chosen {mode} mode. You have {number_guesses} guesses.")

else:
    number_guesses = HARD
    print(f"You have chosen {mode} mode. You have {number_guesses} guesses.")

# Play the game

while number_guesses > 0:
    user_guess = int(input("what is your guess? "))
    still_playing = check_answer(user_guess)
    if still_playing == True:
        print("Try Again.")
        number_guesses -= 1
        print(f"the number of guesses you have left is {number_guesses}")
        if number_guesses == 0:
            print("Out of guesses, better luck next time!")
    elif still_playing == False:
        number_guesses = 0