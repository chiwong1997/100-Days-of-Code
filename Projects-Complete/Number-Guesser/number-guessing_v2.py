from random import randint

EASY_NUMBER_TURNS = 10
HARD_NUMBER_TURNS = 5

# Function that checks users answers against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Function that checks the user answer with the actual
    answer. If the guess is too high or too low, it tells
    the user, and then reduces a turn. If the guess is 
    correct, it will tell the user"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    if user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function that sets the difficulty (number of turns)
def set_difficulty():
    """Function that sets the difficulty level based on user and 
    returns the number of turns as an integer"""
    level = input("Do you want to play in easy or hard mode? ")
    if level == "easy":
        return EASY_NUMBER_TURNS
    else:
        return HARD_NUMBER_TURNS

def game():
    print("Welcome to the number guessing game.")
    answer = randint(1,100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left to guess.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("out of guesses! outta here!")
            return
        elif guess != answer:
            print("Guess again!")

# main code
game()