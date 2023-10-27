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
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(coffee):
    """Returns True when order can be made, False if ingredients are insufficient.

    :param coffee:

    """
    req_resc = coffee["ingredients"]
    for item in req_resc:
        if req_resc[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """ """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def check_transaction(coffee_price, payment_recieved):
    """

    :param coffee_price:
    :param payment_recieved:

    """
    if payment_recieved >= coffee_price:
        change = round(payment_recieved - coffee_price, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += coffee_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources.

    :param drink_name:
    :param order_ingredients:

    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")


def coffee_machine():
    """ """
    is_on = True
    while is_on:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")
        if user_order == "off":
            is_on = False
        elif user_order == "report":
            for k, v in resources.items():
                print(f"{k}: {v}")
            print(f"Money : ${profit}")
        else:
            drink = MENU[user_order]
            if check_resources(drink):
                payment = process_coins()
                if check_transaction(drink["cost"], payment):
                    make_coffee(user_order, drink["ingredients"])


coffee_machine()
