import random
import hangman_art
import hangman_words
import os

logo = hangman_art.logo
stages = hangman_art.stages

# Print starting logo
print(logo)

# Generate a random word
word_list = hangman_words.word_list
word = random.choice(word_list)

# List to hold word and guesses
display = []
for letter in word:
    display.append("_")

# Defining starting variables
lives_left = 6
end_of_game = False
guesses = []

while not end_of_game:
    print(stages[lives_left])
    # End the game if there are no lives left
    if lives_left == 0:
        end_of_game = True
        print("You lose!")
    # Continue the game if there are still lives left
    else:
      guess = input("Guess a letter: ").lower()
      os.system('cls') # This is for clearing the console for clarity

      # If guess was already made
      if guess in guesses:
          print(f"You already guessed {guess}.")
      # If guess wasn't made
      else:
        guesses.append(guess)
        word_length = len(word)
        in_word = False

        # Checking if the guess is in the word
        for i in range(0, word_length):
            if word[i] == guess:
                display[i] = guess
                in_word = True
                
        if not in_word:
            lives_left -= 1
            print(f"You guessed {guess}. That's not in the word. You lose a life.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("Congrats you have guessed all the letters! You've won.")


# for letter in word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")