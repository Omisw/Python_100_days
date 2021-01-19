from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True

while machine_on:
    coffees = menu.get_items()
    coffee_choice = input(f"What coffee would you like?: {coffees}")
    if coffee_choice == "off":
        machine_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
