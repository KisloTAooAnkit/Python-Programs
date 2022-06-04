from abc import ABC, abstractmethod

class Peg(ABC):
    @abstractmethod
    def getRadius(self):
        None

class RoundHole:
    def __init__(self,radius) -> None:
        self.radius = radius


    def fits(self,roundPeg : Peg):
        print(f'Current Peg is fitting ? -> {self.radius >= roundPeg.getRadius()}')
    


class RoundPeg(Peg):

    def __init__(self,radius) -> None:
        self.pegRadius = radius

    def getRadius(self):
        return self.pegRadius



class SquarePeg():
    def __init__(self,size) -> None:
        self.sideSize = size

    def getSide(self):
        return self.sideSize

class SquarePegAdapter(Peg):

    def __init__(self,squarePeg) -> None:
        self.sqPeg = squarePeg
    

    def getRadius(self):
        diag = ((self.sqPeg.getSide() ** 2)*2)**(1/2)
        return diag/2



roundHole = RoundHole(10)
roundPeg = RoundPeg(5)
roundHole.fits(roundPeg)

squarePeg = SquarePeg(5)
#roundHole.fits(squarePeg) #this line produces error as we cant check for square peg on round holes directly 

squarePegAdapter = SquarePegAdapter(squarePeg)
roundHole.fits(squarePegAdapter)