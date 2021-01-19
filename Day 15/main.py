# Day 15 - Final challenge "Coffe machine".


from menu import MENU, resources

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIE = 0.01

# print(f"Total, quarters: {quarters_paid}, dimes: {dimes_paid}, nickles: {nickles_paid}, pennies: {pennies_paid}")
# print(MENU[coffee_choice]['ingredients']['water'])

make_coffee = True
while make_coffee:

    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    print("Please insert coins.")

    quarters_paid = QUARTER * int(input("How many quarters?: "))
    dimes_paid = DIME * int(input("How many dimes?: "))
    nickles_paid = NICKLE * int(input("How many nickles?: "))
    pennies_paid = PENNIE * int(input("How many pennies?: "))
    total_amount = quarters_paid + dimes_paid + nickles_paid + pennies_paid

    if coffee_choice == "espresso":

        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"]:
            change = round(total_amount - MENU[coffee_choice]["cost"], 2)
            if total_amount < MENU[coffee_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                make_coffee = False

            resources["water"] = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]

            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_choice}. Enjoy!")

        else:
            print("Sorry theres no enough ingredients.")
            make_coffee = False

    elif coffee_choice == "latte":
        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and \
                resources["milk"] >= MENU[coffee_choice]["ingredients"]["milk"] and \
                resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"]:

            change = round(total_amount - MENU[coffee_choice]["cost"], 2)
            if total_amount < MENU[coffee_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                make_coffee = False

            resources["water"] = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[coffee_choice]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]

            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_choice}. Enjoy!")
            # print(resources)
        else:
            print("Sorry theres no enough ingredients.")
            make_coffee = False

    elif coffee_choice == "cappuccino":
        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and resources["milk"] >= MENU[coffee_choice]["ingredients"]["milk"] and resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"]:
            change = round(total_amount - MENU[coffee_choice]["cost"], 2)
            if total_amount < MENU[coffee_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                make_coffee = False

            resources["water"] = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[coffee_choice]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]

            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_choice}. Enjoy!")
            # print(resources)
        else:
            print("Sorry theres no enough ingredients.")
            make_coffee = False
