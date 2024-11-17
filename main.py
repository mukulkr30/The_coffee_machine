from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import The_Money_Machine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = The_Money_Machine()
THE_machine_ON = True
while THE_machine_ON:
    ask = input(f"what can i do {menu.get_item()}report").lower()
    if ask == "off":
        THE_machine_ON = False

    elif ask =="report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(ask)
        if coffee_maker.Is_resource_sufficient(drink):

            if money_machine.process_coins(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            feedback = input("do you want to fill resources")
            if feedback =="yes":
                coffee_maker.filling_resource()
            else:
                THE_machine_ON = False