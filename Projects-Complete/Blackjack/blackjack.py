import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

### Function that deals a random card from a list of cards
def deal_card(cards: list) -> int:
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card

### Function that calculates the scores
def calculate_score(cards: list) -> int:
    """
    Returns the sum of the cards in a hand. 
    Returns 0 if blackjack. 
    Converts A from 11 to 1 if sum is greater than 21 and then returns that sum. 
    """
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

### Function to compare user and computer score
def compare(u_score: int, c_score: int, u_cards: list):
    """Compare scores of user and computer and determine outcome"""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win, you have Blackjack!"
    elif u_score > 21:
        return "You went over - you lose"
    elif c_score > 21:
        return "Opponent is over - you win!"
    elif u_score > c_score:
        return "You Win"
    elif len(u_cards) > 5:
        return "You drew more than 5 cards and didn't bust so you win!"
    else:
        return "You Lose"

def play_game():
    """Function that plays the game of blackjack"""
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    # Draw initial 2 cards
    for i in range(0,2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    # User draws cards until bust or stop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User current cards {user_cards}, User current score {user_score}")
        print(f"Computer current cards {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        if len(user_cards) > 5:
            is_game_over = True
        else:
            user_should_deal = input("Would you like another card? (y/n): ")
            if user_should_deal == "y":
                user_cards.append(deal_card(cards))
            else:
                is_game_over = True

    # Computer will keep drawning cards until it draws 17 or above
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score {user_score}")
    print(f"Computer final hand: {computer_cards}, computer final score {computer_score}")
    print(compare(user_score, computer_score, user_cards))

play_again = input("Do you want to play a game of blackjack (y/n): ")
while play_again == "y":
    print("\n" * 20)
    play_game()
    play_again = input("Do you want to play a game of blackjack (y/n): ")