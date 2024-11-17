class The_Money_Machine:
    def __init__(self):
        self.profit=0
    @staticmethod
    def report(self):
        return f"your current profit is {self.profit}"

    def process_coins(self,cost):
        self.cost = cost
        doller = self.make_payment()

        if doller>=self.cost:
            refundable_coin = doller - self.cost
            print(f"refunded {refundable_coin}$")
            self.profit += self.cost
            return True
        else:
            print(f"not enough money..refunded {doller}")
            return False

    @staticmethod
    def make_payment():
        penny = int(input("how many penny"))
        nickel = int(input("how many nickel"))
        dime = int(input("how many dime"))
        quarter = int(input("how many quarter"))
        doller = (penny / 100) + (nickel / 20) + (dime / 10) + (quarter / 4)
        return doller

