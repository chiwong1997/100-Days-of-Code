# some python built in functions: https://docs.python.org/3/library/functions.html

def my_function():
    print('Hello')
    print('Bye')

my_function()

# Reeborgs world 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_seq_1():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



number_of_hurdles = 5
while not at_goal():
    if wall_in_front():
        move_seq_1()
    if front_is_clear():
        move() 

# Hurdle 4 Exercise 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    if wall_in_front():
        turn_left()

# Day 6 Project - done in the reeborg website 
# Maze 
# same as the above code works 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    if wall_in_front():
        turn_left()