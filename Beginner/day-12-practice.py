# Global Scope 
this_is_a_global_var = 1

# Local Scope 
def some_function():
    this_is_a_local_var = 1
    return 0

# you won't be able to use the variable this_is_a_local_var

# Prime number checker

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
print(is_prime(21))

print(math.sqrt(21) + 1)
print(21%2)
print(21%3)
print(21%4)

# Modifying the global scope - usually not a great idea
# You can use global scope, you can read it, without modifying
enemies = 1

def add_enemies():
    global enemies
    enemies += 1
    return enemies

# A better way of doing it:

enemies = 1
def add_enemies(enemy: int):
    return enemy + 1

enemies = add_enemies(enemies)
print(enemies)

# Global constants - define as upper case
PI = 3.1415
URL = "https://www.google.com"
