from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instanciar os objetos
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_report():
    coffe_maker.report()
    money_machine.report()


is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        get_report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            cost = drink.cost
            if money_machine.make_payment(cost):
                coffe_maker.make_coffee(drink)
