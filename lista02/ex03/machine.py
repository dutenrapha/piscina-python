import random
from beverages import *

class CoffeeMachine():

    def __init__(self) -> None:
        self.drinks_served = 0
        self.is_working = True
        
    class EmptyCup(HotBeverage):
        price = 0.90
        name = "empty cup"

        def description(self):
            return super().description("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            self.message = message
            super().__init__(self.message)

    def repair(self):
        self.is_working = True
        self.drinks_served = 0
        print("Your machine has been repair!!!\n")

    def serve(self, hotBeverage:HotBeverage):

        if self.drinks_served >= 10:
            self.is_working = False
        if self.is_working:
            self.drinks_served +=1
            return random.choice([self.EmptyCup(), hotBeverage()])
        else:
            raise CoffeeMachine.BrokenMachineException

if __name__ == '__main__':
    machine = CoffeeMachine()
    beverages = [Coffee, Tea, Cappuccino]
    try:
        #Should work
        for i in range(10):
            beverage = random.choice(beverages)
            print(f"#{i +1} {machine.serve(beverage)}\n")
        #Must broke
        beverage = random.choice(beverages)
        print(f"#{i +1} {machine.serve(beverage)}\n")
    except CoffeeMachine.BrokenMachineException as e:
        print(f"{e}\n")
    
    machine.repair()

    try:
        #Should work
        for i in range(10):
            beverage = random.choice(beverages)
            print(f"#{i +1} {machine.serve(beverage)}\n")
        #Must broke
        beverage = random.choice(beverages)
        print(f"#{i +1} {machine.serve(beverage)}\n")
    except CoffeeMachine.BrokenMachineException as e:
        print(f"{e}\n")