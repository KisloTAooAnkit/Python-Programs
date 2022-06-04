from parkinglot.ParkingLot import AdminActions


class Admin:
    def __init__(self,person) -> None:
        self.parkingLot : AdminActions = None
        self.person = person

    def addSpot(self,type):
        self.parkingLot.addSpot(type)

    def removeSpot(self,type):
        self.parkingLot.removeSpot(type)

    def addFloor(self,type):
        pass

    def removeFloor(self,type):
        pass


class ParkingAttendant:
    pass


