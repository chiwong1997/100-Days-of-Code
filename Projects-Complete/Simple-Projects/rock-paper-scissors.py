"""
Rock Paper Scissors 
concepts: Randomization, Lists, Nested Lists

"""
import random 

# ASCII art 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lst = [rock, paper,scissors]

# User Input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

# Print User Input
if user_choice in range(0,3):
    print(lst[user_choice])
else:
    print("Choice not valid - please only pick 0, 1, or 2")

# Computer Choice
print("Computer choose:")
computer_choice = random.randint(0,2)
print(lst[computer_choice])

# Outcomes 
# Scenario 1 - draw 
if user_choice == computer_choice:
    print("It's a draw.")
# Scenario 2 - user picks rock
elif user_choice == 0:
    if computer_choice == 1:
        print("You lose.")
    elif computer_choice == 2:
        print("You win.")
# Scenario 3 - user picks paper
elif user_choice == 1:
    if computer_choice == 0:
        print("You win.")
    elif computer_choice == 2:
        print("You lose.")
# Scenario 4 - user picks scissors
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win.")
else:
    print("Impossible scenario")