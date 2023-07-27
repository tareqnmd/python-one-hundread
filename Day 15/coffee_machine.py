from menu import menu
from resources import resources


def print_resources(money):
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
    )


def resource_check(type):
    if resources["water"] < menu[type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] < menu[type]["ingredients"]["coffee"]:
        print("Sorry there is not enough water.")
        return False
    if type != "espresso" and resources["milk"] < menu[type]["ingredients"]["milk"]:
        print("Sorry there is not enough water.")
        return False
    return True


def get_money(command):
    return menu[command]["cost"]


def money_check(command):
    quarters = int(input("how many quarters?: ") or 0)
    dimes = int(input("how many dimes?: ") or 0)
    nickels = int(input("how many nickels?: ") or 0)
    pennies = int(input("how many pennies?: ") or 0)
    customer_money = (
        (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    )
    remaining_money = customer_money - get_money(command)
    if remaining_money < 0:
        print("Sorry that's not enough money. Money refunded.")
    return remaining_money


def deduct_resources(command):
    resources["water"] -= menu[command]["ingredients"]["water"]
    if command != "espresso":
        resources["milk"] -= menu[command]["ingredients"]["milk"]
    resources["coffee"] -= menu[command]["ingredients"]["coffee"]


def make_coffee(command):
    resource = resource_check(command)
    if resource:
        remaining_money = money_check(command)
        if remaining_money >= 0:
            if remaining_money > 0:
                print(f"Here is ${remaining_money:.2f} in change.")
            print(f"Here is your {command} ☕️. Enjoy!")
            return True
    return False


def coffee_machine():
    machine_continue = True
    money = 0
    while machine_continue:
        command = input("What would you like? (espresso/latte/cappuccino): ")
        if command == "report":
            print_resources(money)
        elif command == "espresso" or command == "latte" or command == "cappuccino":
            make = make_coffee(command)
            if make:
                money += menu[command]["cost"]
                deduct_resources(command)
        elif command == "off":
            machine_continue = False
        else:
            print("Unknown Command")


coffee_machine()
