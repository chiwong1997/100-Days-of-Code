from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


input("Hello")

is_on = True
menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

full_menu = menu.get_items()

while is_on == True:
    choice = input(f"What would you like to drink?: {full_menu}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffeemaker.report())
        print(moneymachine.report())