from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
menu_obj = Menu()
sell = True

while sell:
    selection = input(f"Please select a drink ({menu_obj.get_items()})\n").lower()
    if selection == "report":
        maker.report()
        money.report()
    if selection == "off":
        exit()
    if selection != "report":
        menu_it = menu_obj.find_drink(selection)
        if maker.is_resource_sufficient(menu_it):
            print(f"Cost of selection ${menu_it.cost}")
            if money.make_payment(menu_it.cost):
                maker.make_coffee(menu_it)
