import sys

### Variables

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

allowed_input = ("e", "c", "l", "o", "r")
profits = 0
report_flag = True
order_flag = True
money_inserted = 0
previous_coffee_order = 'A'
enough_resource = True

### Functions

def print_resource_value(resource: dict):
    """Take the resource dictionary and print out the resource level as a string"""
    to_print = f"Water: {resource['water']}mL\nMilk: {resource['milk']}mL\nCoffee :{resource['coffee']}g"
    return print(to_print)

def check_resources(order: str, menu: dict):
    """Take the order of the customer as a string and return whether there is not 
    enough resource (and which resource) or if the customer can proceed to pay"""
    enough_water = resources['water'] >= menu[order]['ingredients']['water']
    if enough_water == False:
        print("Sorry there is not enough water.")
        enough_resources = False
    enough_milk = resources['milk'] >= menu[order]['ingredients']['milk']
    if enough_milk == False:
        print("Sorry there is not enough milk.")
        enough_resources = False
    enough_coffee = resources['coffee'] >= menu[order]['ingredients']['coffee']
    if enough_coffee == False:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    if enough_water and enough_milk and enough_coffee:
        enough_resources = True
    return enough_resources

def get_money_inputs(denomination: str):
    """Take coins (one of quarters, dimes, nickels, or pennies) and return 
    the number of coins inserted by the user as an integer"""
    money_denomination = int(input(f"How many {denomination}?: "))
    return money_denomination

def check_transaction(inserted: int, order: str, menu: dict, resource: dict, profit: int):
    if inserted >= menu[order]['cost']:
        if inserted > menu[order]['cost']:
            change = inserted - menu[order]['cost']
            print(f"Here is ${change} in change.")
        print(f"Here is your {order}! Enjoy.")
        reduce_resources(order=order, menu=menu, resource=resource)

    if inserted < menu[order]['cost']:
        print("Sorry that's not enough money. Money Refunded")
        sys.exit(0)

def reduce_resources(order: str, menu: dict, resource: dict):
    """Takes the coffee order if successful and reduces the number of 
    resources based on what the order was"""
    ingredients = ('water', 'milk', 'coffee')
    for ingredient in ingredients:
        new_level = resource[ingredient] - menu[order]['ingredients'][ingredient]
        resource[ingredient] = new_level

### Code

while report_flag == True and order_flag == True:
    # TODO: 1. Prompt user and ask what they would like - take first letter in case spelling
    coffee_order = input("What would you like? (espresso/latte/cappucino): ").lower()[0]
    while coffee_order not in allowed_input:
        coffee_order = input("Not allowed. Please choose either espresso, latte, or cappuccino: ")
    
    # convert first letter back to full expression
    if coffee_order == "e":
        coffee_order = "espresso"
    elif coffee_order == "l":
        coffee_order = "latte"
    elif coffee_order =="c":
        coffee_order = "cappuccino"

    # TODO: 2. Add functionality where if off is enterned, the machine is turned off 
    if coffee_order == "o":
        print("Turning off machine for maintenance...")
        sys.exit(0)

    # TODO: 3. Print report of the current resource value 

    if coffee_order == "r":
        print_resource_value(resources)
        if money_inserted != 0:
            profits += MENU[previous_coffee_order]['cost']
        print(f"Money: ${profits}")

# TODO: 4. Check if there are enough resources in the machine to make the drink 

    else:
        enough_resource = check_resources(order=coffee_order, menu=MENU)
        if enough_resource == True:
# TODO: 5. Process the number of coins - number of coins + change 
        
            quarters = get_money_inputs('quarters')
            dimes = get_money_inputs('dimes')
            nickels = get_money_inputs('nickels')
            pennies = get_money_inputs('pennies')

            money_inserted = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01

    # TODO: 6. Check if the transaction is successful

            check_transaction(inserted=money_inserted, order=coffee_order, menu=MENU, resource=resources, profit=profits)
            previous_coffee_order = coffee_order