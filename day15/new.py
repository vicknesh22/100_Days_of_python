# todo: 1 - import
from data import resources, MENU

# todo: 2 - ask user

water_storage = resources['water']
milk_storage = resources['milk']
coffee_storage = resources['coffee']

while water_storage != "Not enough Water" or coffee_type(
        coffee_name=coffee) != "Not enough milk" or coffee_type(coffee_name=coffee) != "Not enough coffee":
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    print("Please insert coins. ")
    u_quarters = int(input("\nhow many quarters?: "))
    u_dimes = int(input("\nhow many dimes?: "))
    u_nickles = int(input("\nhow many nickles?: "))
    u_pennies = int(input("\nhow many pennies?: "))


    def dollar_con(u_quarters, u_dimes, u_nickles, u_pennies):
        dollar = ((u_quarters * 0.25) + (u_dimes * 0.10) + (u_nickles * 0.05) + (u_pennies * 0.01))
        return dollar


    u_dollar = dollar_con(u_quarters, u_dimes, u_nickles, u_pennies)


    def balance_teller(user_dollar, cost):
        balance = round(float(user_dollar - cost), 2)
        if balance < 0:
            return "Sorry that's not enough money. Money refunded."
        elif balance == 0:
            return f"Here is your {coffee} ☕️. Enjoy!"
        elif balance > 0:
            return f"Here is ${balance} in change.\nHere is your {coffee} ☕️. Enjoy!"


    def coffee_type(coffee_name):
        global water_storage, milk_storage, coffee_storage, u_dollar
        if coffee_name == "espresso":
            coffee_cost = float(MENU['espresso']['cost'])
            coffee_water = int(MENU['espresso']['ingredients']['water'])
            coffee_coffee = int(MENU['espresso']['ingredients']['coffee'])
            coffee_milk = 0

            if water_storage < 50:
                return "Not enough Water"
            elif coffee_storage < 24:
                return "Not enough coffee"
            else:
                water_storage -= coffee_water
                milk_storage -= coffee_milk
                coffee_storage -= coffee_coffee
                return balance_teller(user_dollar=u_dollar, cost=coffee_cost)

        elif coffee_name == "latte":
            coffee_cost = float(MENU['latte']['cost'])
            coffee_water = int(MENU['latte']['ingredients']['water'])
            coffee_milk = int(MENU['latte']['ingredients']['milk'])
            coffee_coffee = int(MENU['latte']['ingredients']['coffee'])

            if water_storage < 200:
                return "Not enough Water"
            elif coffee_storage < 24:
                return "Not enough coffee"
            elif milk_storage < 150:
                return "Not enough milk"
            else:
                water_storage -= coffee_water
                milk_storage -= coffee_milk
                coffee_storage -= coffee_coffee
                return balance_teller(user_dollar=u_dollar, cost=coffee_cost)

        elif coffee_name == "cappuccino":

            coffee_cost = float(MENU['cappuccino']['cost'])
            coffee_water = int(MENU['cappuccino']['ingredients']['water'])
            coffee_milk = int(MENU['cappuccino']['ingredients']['milk'])
            coffee_coffee = int(MENU['cappuccino']['ingredients']['coffee'])

            if water_storage < 250:
                return "Not enough Water"
            elif coffee_storage < 24:
                return "Not enough coffee"
            elif milk_storage < 100:
                return "Not enough milk"
            else:
                water_storage -= coffee_water
                milk_storage -= coffee_milk
                coffee_storage -= coffee_coffee
                return balance_teller(user_dollar=u_dollar, cost=coffee_cost)

    print(coffee_type(coffee_name=coffee))



