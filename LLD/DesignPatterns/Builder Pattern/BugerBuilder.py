
class Burger:
    def __init__(self,burgerBuilder) -> None:
        self.lettuce = burgerBuilder.lettuce
        self.cheese = burgerBuilder.cheese
        self.meatPatty = burgerBuilder.meatPatty
        self.vegPatty = burgerBuilder.vegPatty
        self.roastedBread = burgerBuilder.roastedBread


class BurgerBuilder:

    def __init__(self) -> None:
        self.lettuce = False
        self.cheese = False
        self.meatPatty = False
        self.vegPatty = False
        self.roastedBread = False
    
    def addLettuce(self):
        self.lettuce = True
        return self
    
    def addCheese(self):
        self.cheese = True
        return self #returning self for chaining 
    
    def addMeat(self):
        self.meatPatty = True
        return self
    
    def addVegPatty(self):
        self.vegPatty = True
        return self

    def addRoastedBread(self):
        self.roastedBread = True
        return self

    def createBorgir(self):
        return Burger(self)


myCustomBurger = BurgerBuilder().addCheese().addLettuce().addMeat().addRoastedBread().createBorgir()
print(type(myCustomBurger))