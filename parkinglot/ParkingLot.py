

from abc import ABC, abstractmethod
from datetime import date

from parkinglot.constants import TicketStatus

class AdminActions(ABC):

    @abstractmethod
    def addSpot(self,type):
        pass

    @abstractmethod
    def removeSpot(self,type):
        pass

    @abstractmethod
    def removeFloor(self):
        pass
    
    @abstractmethod
    def addFloor(self,bike,car,truck):
        pass


class ParkingAttendantActions(ABC):

    @abstractmethod
    def assingSpot(self,Vehicle):
        pass

    @abstractmethod
    def freeSpot(self,ticket):
        pass


class ParkingLot(AdminActions,ParkingAttendantActions):
    
    def __init__(self) -> None:
        pass

    def assingSpot(self, Vehicle):
        return super().assingSpot(Vehicle)

    def freeSpot(self, ticket):
        pass

    def addFloor(self, bike, car, truck):
        return super().addFloor(bike, car, truck)
    
    def removeFloor(self):
        return super().removeFloor()
    
    def addSpot(self, type):
        return super().addSpot(type)
    
    def removeSpot(self, type):
        return super().removeSpot(type)





class RegimeCalculator(ABC):
    @abstractmethod
    def calculateFare(ticket):
        pass

class OldRegimeCalc(RegimeCalculator):
    def __init__(self) -> None:
        pass

    def calculateFare(ticket):
        pass

class NewRegimeCalc(RegimeCalculator):
    def __init__(self) -> None:
        pass

    def calculateFare(ticket):
        pass

class FareCalculator():
    def __init__(self , caculatingStrat : RegimeCalculator) -> None:
        self.strat = caculatingStrat
    
    def calculatePrice(self,ticket):
        return self.strat.calculateFare(ticket)

    def changeRegime(self,strat):
        self.strat = strat

class Ticket:

    def __init__(self,vehicle) -> None:
        self.issueTime = date.today()
        self.vehicle = vehicle
        self.person = vehicle.person
        self.ticketStatus = TicketStatus.Active
    

    def expireTicket(self):
        self.ticketStatus = TicketStatus.Expired
