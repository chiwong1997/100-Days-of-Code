import art
import game_data
import random

def choose_celebrity():
    """Returns a dictionary with the name, follower count, description, 
    and country of a randomly chosen celebrity."""
    choice = random.choice(game_data.data)
    return choice

def celebrity_stats(celebrity):
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}"

def compare_followers(celeb_A, celeb_B):
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

    while user_choice == more_followers:

        celebrity_A = celebrity_B
        while celebrity_A == celebrity_B:
            celebrity_B = choose_celebrity()

        # print(celebrity_A)
        # print(celebrity_B)

        print(f"Compare A: {celebrity_stats(celebrity_A)}.")
        print(art.vs)
        print(f"\nAgainst B: {celebrity_stats(celebrity_B)}")

        more_followers = compare_followers(celebrity_A, celebrity_B)

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        # print(user_choice == more_followers)
        if user_choice != more_followers:
            return print(f"\nSorry that's wrong. Final score: {score}")
        score += 1
        print(f"\nYou're right! Current score: {score}\n")

game()