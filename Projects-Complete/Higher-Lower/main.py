import art
import game_data
import random

def choose_celebrity():
    """Returns a dictionary with the name, follower count, description, 
    and country of a randomly chosen celebrity."""
    choice = random.choice(game_data.data)
    return choice

def celebrity_stats(celebrity):
    """Takes the account data and returns the printable format."""
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}"

def compare_followers(celeb_A, celeb_B):
    """Takes two accounts and compare the number of followers between the two accounts"""
    if celeb_A['follower_count'] > celeb_B['follower_count']:
        return "A"
    return "B"

def game():
    print(art.logo)

    score = 0
    celebrity_A = choose_celebrity()
    celebrity_B = choose_celebrity()
    user_choice = "A"
    more_followers = "A"
    already_chosen = []

    while user_choice == more_followers:

        celebrity_A = celebrity_B
        already_chosen.append(celebrity_A)
        # Choose a different celebrity if celebrity A and B are the same
        while celebrity_A == celebrity_B and celebrity_B in already_chosen:
            celebrity_B = choose_celebrity()

        print(f"Compare A: {celebrity_stats(celebrity_A)}.")
        print(art.vs)
        print(f"\nAgainst B: {celebrity_stats(celebrity_B)}")

        more_followers = compare_followers(celebrity_A, celebrity_B)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 20)
        print(art.logo)
        if user_choice != more_followers:
            return print(f"\nSorry that's wrong. Final score: {score}")
        score += 1
        print(f"\nYou're right! Current score: {score}\n")

game()