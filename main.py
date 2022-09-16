MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

game_on = True
profit = 0


def is_resource_sufficient(coffee_choice):
    """This returns true is there is sufficient resources and returns false otherwise"""
    for specific_ingredient in coffee_choice:
        ingredient_value = coffee_choice[specific_ingredient]
        while specific_ingredient in resources and coffee_choice:
            if ingredient_value <= resources[specific_ingredient]:
                return True
            else:
                print(f"Not sufficient {specific_ingredient}")
                return False


def right_price():
    """This takes the input for coins"""
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def is_transaction_successful(amount_paid, coffee_cost):
    """This returns True if transaction is successful and returns false if otherwise"""
    if amount_paid >= coffee_cost:
        if amount_paid > coffee_cost:
            change = round(amount_paid - coffee_cost, 2)
            print(f"Here is your change ${change}")
        global profit
        profit += round(coffee_cost, 2)
        return True
    else:
        print("Not enough money to make an order. Your money is refunded")
        return False


def make_coffee(resource, ingredient):
    """This makes the coffee and reduces the ingredients from the available resources"""
    for each_resource in ingredient:
        #balance_resources = resource[each_resource] - ingredient[each_resource]
        resource[each_resource] -= ingredient[each_resource]
    return f"Please take your {choice}"


while game_on:
    choice = input("What would you like? (espresso, latte, cappuccino) ")
    if choice == "end":
        game_on = False
    elif choice == "resources":
        print("Resources left:")
        for resources_left in resources:
            balance = resources[resources_left]
            print(f"{resources_left}: {balance}")
        print(f"profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            price = right_price()
            if is_transaction_successful(price, drink["cost"]):
                print(make_coffee(resources, drink["ingredients"]))
                game_on = True

# if resources is indeed sufficient, display the coin request
##if transaction is successful, make the coffee

# check if there is enough resources to make the preferred coffee
# define a function called resources and pass in the coffee type
# def check_resources():
#     water_left = resources["water"]
#     milk_left = resources["milk"]
#     coffee_left = resources["coffee"]
#
#
# def enough_ingredients(the_coffee_type):
#     ingredient_specifics = MENU[the_coffee_type]["ingredients"]
#     water_required = ingredient_specifics["water"]
#     milk_required = ingredient_specifics["milk"]
#     coffee_required = ingredient_specifics["coffee"]
#
#     if water_left >= water_required:
#         water_left = water_left - water_required
#         return water_left
#     else:
#         return f"Sorry, there is no enough water left!"
#     if milk_left >= milk_required:
#         milk_left = milk_left - milk_requred
#         return milk_left
#     else:
#         return "Sorry, there is not enough milk left!"
#     if coffee_left >= coffee_required:
#         coffee_left = coffee_left - coffee_required
#         return coffee_left
#     else:
#         return "Sorry, there is not enough coffee left!"
#
#
# def select_coffee_type(coffee_type):
#     ingredient_amount = MENU[coffee_type]["ingredients"]
#     water_required = ingredient_amount["water"]
#     milk_required = ingredient_amount["milk"]
#     coffee_required = ingredient_amount["coffee"]
#
#
# def check_cost(quarter_input, dimes_input, nickles_input, pennies_input):
#     amount = (quarter_input * 0.25) + (dimes_input * 0.1) + (nickles_input * 0.15) + (pennies_input * 0.01)
#     coffee_cost = MENU[coffee_type]["cost"]
#     if coffee_cost <= amount:
#         change = amount - coffee_cost
#         if change > 0:
#             return f"take your change of ${change}"
#         return f"Here's your {coffee_type} coffee!"
#     else:
#         return f"No sufficient amount. {coffee_cost} required"
#
# # TODO 1: Prompt user by asking "What would you like?"
#
#
# coffee_type = input("What would you like? (espresso, late, cappuccino) ")
# if enough_ingredients(coffee_type):
#
#
# quarter_input = input("how many quarters?: ")
# dimes_input = input("how many dimes?: ")
# nickles_input = input("how many nickles?: ")
# pennies_input = input("how many pennies?: ")
#
# # TODO 2: Turn off the coffee Machine by entering 'OFF'
# # TODO 3: Print report
# # TODO 4: Check resources sufficient?
# # TODO 5: Process coins
# # TODO 6: Check transaction successful?
# # TODO 7: Make Coffee
# #
