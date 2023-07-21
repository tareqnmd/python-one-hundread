from art import logo

print(logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    calc_continue = True
    num1 = float(input("What's the number? :"))
    while calc_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the other number? :"))
        calc = operations[operation]
        result = calc(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        next = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: "
        )
        if next == "y":
            num1 = result
        else:
            calc_continue = False
            calculator()


calculator()
