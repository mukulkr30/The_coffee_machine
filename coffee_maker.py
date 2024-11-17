class CoffeeMaker:
    def __init__(self,):
        self.resource_avail = {
            "water": 300,
            "coffee": 100,
            "milk": 200,
        }

    def report(self):
        print(f"water:{self.resource_avail["water"]}ml")
        print(f"milk:{self.resource_avail["milk"]}ml")
        print(f"coffee:{self.resource_avail["coffee"]}g")

    def Is_resource_sufficient(self,drink):
        can_make = True
        for item in drink.ingredient:
            if drink.ingredient[item] > self.resource_avail[item]:
                print(f"sorry there is not enough {item}")
                can_make = False
        return can_make
    def make_coffee(self,order):
        for item in order.ingredient:
            self.resource_avail[item] -= order.ingredient[item]
        print(f"here is your {order.name}")

    def filling_resource(self):
        self.resource_avail = {
            "water":300,
            "coffee":100,
            "milk":200,
        }
