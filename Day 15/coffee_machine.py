from menu import menu
from resources import resources


def print_resources(money):
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
    )


def coffee_machine():
    machine_continue = True
    money = 0
    while machine_continue:
        command = input("What would you like? (espresso/latte/cappuccino): ")
        if command == "report":
            print_resources(money)
        elif command == "off":
            machine_continue = False


coffee_machine()
