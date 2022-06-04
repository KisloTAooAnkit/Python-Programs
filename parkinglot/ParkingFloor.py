

from collections import deque
from uuid import uuid4
from parkinglot.constants import VehicleType
from parkinglot.Dashboard import Dashboard
from parkinglot.ParkingSpot import CarParkingSpot,BikeParkingSpot,TruckParkingSpot

class ParkingFloor:
    def __init__(self,bikeSpotsC,truckSpotsC,carSpotsC) -> None:
        self.floorId = uuid4()
        self.dashBoard = Dashboard()
        self.bikeSpots = deque()
        self.truckSpots = deque()
        self.carSpots = deque()
        self.occupiedSpots = dict()
        self.__allotSlots(bikeSpotsC,truckSpotsC,carSpotsC)
        self.isEmpty = False

    def __allotSlots(bikeSpotsC,truckSpotsC,carSpotsC):
        pass
    

    def getBikeSpot(self):
        if not self.dashBoard.bikeSpot:
            raise("no spot available")
        
        spot = self.dashBoard.bikeSpot
        self.occupiedSpots[spot.id] = self.bikeSpots.popleft()
        self.__updateDashBoard(VehicleType.Bike)
        return spot


    def freeBikeSpot(self,spot):
        spot.removeVehicle()
        del self.occupiedSpots[spot.id]
        self.bikeSpots.append(spot)
        return


    def removeSpots(self,type,count):
        while(count):
            if type == VehicleType.Bike and self.bikeSpots:
                self.bikeSpots.popleft()
                self.__updateDashBoard()
            
            if type == VehicleType.Car and self.carSpots:
                self.carSpots.popleft()
                self.__updateDashBoard()
            
            if type == VehicleType.Truck and self.truckSpots:
                self.truckSpots.popleft()
                self.__updateDashBoard()
            else:
                break
            
            count -=1


    def addSpot(self,type,count):
        for i in range(count):
            if type == VehicleType.Bike:
                self.__addBikeSpot()
            elif type == VehicleType.Car:
                self.__addCarSpot()
            elif type == VehicleType.Truck:
                self.__addTruckSpot()


    def __updateDashBoard(self,type):
        if type == VehicleType.Bike:
            if self.bikeSpots:
                self.dashBoard.bikeSpot = self.bikeSpots.popleft()
        #same for everytype
    
    def __addBikeSpot(self):
        self.bikeSpots.append(BikeParkingSpot())
        return
    

    def __addCarSpot(self):
        self.bikeSpots.append(CarParkingSpot())
        return


    def __addTruckSpot(self):
        self.bikeSpots.append(TruckParkingSpot())
        return
