from contextlib import redirect_stderr


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

profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coin():
    """ calculate the total (coins)money inserted by the customer
    """
    print("inset coins")
    total = int(input("How many Quaters: ")) * 0.25
    total += int(input("How many  Dimes: ")) * 0.10
    total += int(input("How many Nickles: ")) * 0.05
    total += int(input("How many  pennys: ")) * 0.01
    return total


def is_transaction_successful(money_received, order_price):
    if money_received >= order_price:
        change = round(money_received - order_price,2)
        global profit
        profit += order_price
        print(f"Here is ${change} in change.")
        return True
    else:
        print("sorry not enough money to purchase. here is your refund")
        return False


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        if resources[item] >= order_ingredients[item]:
            resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


def refill():
    resources["water"] +=  int(input("How much water did you add: "))
    resources["milk"] = int(input("How much milk did you add: "))
    resources["coffee"] = int(input("How much coffee did you add: "))
    print("Done.")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} ml")
        print(f"Money: {profit}")
    elif choice == "refill":
        refill()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])








