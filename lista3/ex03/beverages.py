class HotBeverage():
    price = 0.30
    name = "hot beverage"

    def description(self, des= "Just some hot water in a cup."):
        return(des)

    def __str__(self) -> str:
        return (f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}")

class Coffee(HotBeverage):
    price = 0.4
    name = "coffee"

    def description(self):
        return super().description("A coffee, to stay awake.")

class Tea(HotBeverage):
    name = "tea"

    def description(self):
        return super().description("Just some hot water in a cup.")

class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"

    def description(self):
        return super().description("Un po’ di Italia nella sua tazza!")


if __name__ == '__main__':
    hotBeverage = HotBeverage()
    print(hotBeverage)
    coffe = Coffee()
    print(coffe)
    tea = Tea()
    print(tea)
    cappuccino = Cappuccino()
    print(cappuccino) 