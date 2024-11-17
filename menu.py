
class Menu_Items:
    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredient = {
            "water":water,
            "milk":milk,
            "coffee":coffee,
        }


class Menu:
    def __init__(self):
        self.menu=[
            Menu_Items(name="latte",water=200,milk=150,coffee=24,cost=2.5),
            Menu_Items(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            Menu_Items(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    def get_item(self):
        option = ""
        for item in self.menu:
            option +=f"{item.name}/"
        return option

    def find_drink(self,order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        else:
            print("sorry...that item is not available")

