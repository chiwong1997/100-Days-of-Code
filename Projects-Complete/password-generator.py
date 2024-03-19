"""
Project: Random Password Generator 
concepts covered: loops 

"""

import random
import sys

# Generate alphabet list
ord_a = ord('a')
ord_z = ord('z')
ord_A = ord('A')
ord_Z = ord('Z')

alphabet = []
for letter in range(ord_a, ord_z + 1):
    alphabet.append(chr(letter))

for letter in range(ord_A, ord_Z + 1):
    alphabet.append(chr(letter))

numbers = []
for i in range(0, 10):
    numbers.append(str(i))

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')

try:
    nr_letters = int(input('How many letters would you like in your password?\n'))
    nr_symbols = int(input('How many symbols would you like in your password?\n'))
    nr_numbers = int(input('How many numbers would you like in your password?\n'))

except:
    print("Invalid input entered - please try again with only numbers")
    sys.exit(1)

password = []
for i in range(0, nr_letters):
    password.append(random.choice(alphabet))

for i in range(0, nr_symbols):
    password.append(random.choice(symbols))

for i in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f"Here is your password: {''.join(password)}")