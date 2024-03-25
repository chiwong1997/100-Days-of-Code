import random

# Generate a random word
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

display = []
for letter in word:
    display.append("_")

print(display)

lives_left = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    word_length = len(word)
    for i in range(0, word_length):
        if word[i] == guess:
            display[i] = guess

    print(display)

    if "_" not in display:
        end_of_game = True

print("Congrats you have guessed all the letters! You've won.")

# for letter in word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

