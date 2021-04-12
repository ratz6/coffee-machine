MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coff": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coff": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coff": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coff": 100,
}
def resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry,not enough {item} in the machine")
            return False
    return True

def total_cost():
    total = int(input(" Enter quarters ")) *.25
    total += int(input(" Enter dime ")) * .1
    total += int(input(" Enter nickel ")) * .05
    total += int(input(" Enter cents ")) * .01
    return total

def transaction_successful(money_received,drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")
    return True


is_on = True
while is_on:
    choice = input("What would you like to have? espresso/latte/cappuccino \n")
    if choice == "off":
        is_on = False
    elif choice == 'Report'.lower():
        print(f" resources left are {resources['water']}")
        print(f" resources left are {resources['milk']}")
        print(f" resources left are {resources['coff']}")
    else:
        drink = MENU[choice]
        if resource_available(drink):
            payment = total_cost()
            if transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])







