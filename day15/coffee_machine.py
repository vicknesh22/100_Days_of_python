# todo: 1 - import
from data import resources, MENU

# todo: 2 - ask user

water_storage = resources['water']
milk_storage = resources['milk']
coffee_storage = resources['coffee']

storage = 1

while storage != 0:

    coffee = input("What would you like? (espresso/latte/cappuccino):")

    def resource_checker(water, milk, tcoffee):
        global water_storage, milk_storage, coffee_storage

        if water_storage < water:
            possible = water
        elif milk_storage < milk:
            possible = milk
        elif coffee_storage < tcoffee:
            possible = tcoffee
        else:
            possible = True
        return possible





    if coffee == "espresso":
        coffee_cost = float(MENU['espresso']['cost'])
        coffee_water = int(MENU['espresso']['ingredients']['water'])
        coffee_coffee = int(MENU['espresso']['ingredients']['coffee'])
        coffee_milk = 0
        water_storage -= coffee_water
        milk_storage -= coffee_milk
        coffee_storage -= coffee_coffee

    elif coffee == "latte":
        coffee_cost = float(MENU['latte']['cost'])
        coffee_water = int(MENU['latte']['ingredients']['water'])
        coffee_milk = int(MENU['latte']['ingredients']['milk'])
        coffee_coffee = int(MENU['latte']['ingredients']['coffee'])
        water_storage -= coffee_water
        milk_storage -= coffee_milk
        coffee_storage -= coffee_coffee

    elif coffee == "cappuccino":

        coffee_cost = float(MENU['cappuccino']['cost'])
        coffee_water = int(MENU['cappuccino']['ingredients']['water'])
        coffee_milk = int(MENU['cappuccino']['ingredients']['milk'])
        coffee_coffee = int(MENU['cappuccino']['ingredients']['coffee'])
        water_storage -= coffee_water
        milk_storage -= coffee_milk
        coffee_storage -= coffee_coffee

    if (resource_checker(water=coffee_water, milk=coffee_milk, tcoffee=coffee_coffee)) == "True":
        storage = 1
    else:
        print(f"there is not enough {(resource_checker(water=coffee_water, milk=coffee_milk, tcoffee=coffee_coffee))}")
        storage = 0


    print("Please insert coins. ")
    u_quarters = int(input("\nhow many quarters?: "))
    u_dimes = int(input("\nhow many dimes?: "))
    u_nickles = int(input("\nhow many nickles?: "))
    u_pennies = int(input("\nhow many pennies?: "))
    u_dollar = dollar(u_quarters, u_dimes, u_nickles, u_pennies)

    print(u_dollar)
    balance = round(float(u_dollar - coffee_cost), 2)
    print(balance)

    if balance < 0:
        print("Sorry that's not enough money. Money refunded.")
    elif balance == 0:
        print(f"Here is your {coffee} ☕️. Enjoy!")
    elif balance > 0:
        print(f"Here is ${balance} in change.\nHere is your {coffee} ☕️. Enjoy!")



