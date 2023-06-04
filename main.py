from menu import MENU, resources


def print_report(resources, money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: ${money}")


def process_coins(quarters, dimes, nickles, pennies):
    """Takes in inserted coins and returns the total."""
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_resources(order):
    """Takes in a drink order and returns if the resources are sufficient or not"""
    drink = MENU[order]
    req_water = drink["ingredients"]["water"]
    req_milk = drink["ingredients"]["milk"]
    req_coffee = drink["ingredients"]["coffee"]

    if req_water > resources["water"]:
        print("Sorry there is not enough water")
        return False
    elif req_milk > resources["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif req_coffee > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def check_transaction(order, total_payment):
    total_cost = MENU[order]["cost"]
    if total_payment >= total_cost:
        change = round(total_payment - total_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order, resources):
    drink = MENU[order]
    req_water = drink["ingredients"]["water"]
    req_milk = drink["ingredients"]["milk"]
    req_coffee = drink["ingredients"]["coffee"]

    resources["water"] = resources["water"] - req_water
    resources["milk"] = resources["milk"] - req_milk
    resources["coffee"] = resources["coffee"] - req_coffee

    return resources


is_machine_on = True
money = 0

while is_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_machine_on = False
    elif order == "report":
        print_report(resources, money)
    else:
        resources_sufficient = check_resources(order)
        if resources_sufficient:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))

            total_payment = process_coins(quarters, dimes, nickles, pennies)

            if check_transaction(order, total_payment):
                money += MENU[order]["cost"]
                resources = make_coffee(order, resources)

                print(f"Here is your {order} ☕. Enjoy!")









        # print(process_coins(quarters, dimes, nickles, pennies))


# TODO: 1. Print report of all coffee machine resources
# TODO: 2. Check resources sufficient to make drink order
