# importing the required class
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

# creating objects from class

cafe_day = CoffeeMaker()
my_money_machine = MoneyMachine()

# 1. print the coffee menu contents

cafe_day.report()
my_money_machine.report()

# 2. Check resources

# get items

coffee_menus = Menu()

machine = "on"

while machine == "on":
    items = coffee_menus.get_items()
    choice = input(f"What would you like? {items}:")
    if choice == "off":
        machine = "off"
    elif choice == "report":
        cafe_day.report()
        my_money_machine.report()
    else:
        drink = coffee_menus.find_drink(choice)
        print(choice)
        if cafe_day.is_resource_sufficient(drink):
            print("true")
            if my_money_machine.make_payment(drink.cost):
                cafe_day.make_coffee(drink)


