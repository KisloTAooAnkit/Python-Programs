from abc import ABC,abstractmethod
from asyncio import constants
import uuid
from constants import VehicleType

class ParkingSpot(ABC):
    def __init__(self,spotType) -> None:
        self.vehicle = None
        self.isAssinged = False
        self.spotType = spotType
        self.id = uuid.uuid4()
    
    @abstractmethod
    def assignVehicle(self):
        pass

    @abstractmethod
    def removeVehicle(self):
        pass

    def isFree(self):
        return self.isAssinged


class BikeParkingSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__(VehicleType.Bike)

    def assignVehicle(self,vehicle):
        if vehicle.type != self.spotType:
            raise("Wrong Parking spot type")
            
        self.vehicle = vehicle
        self.isAssinged = True
    
    def removeVehicle(self):
        self.vehicle = None
        self.isAssinged = False

class CarParkingSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__(VehicleType.Car)

    def assignVehicle(self,vehicle):
        if vehicle.type != self.spotType:
            raise("Wrong Parking spot type")
            return
        self.vehicle = vehicle
        self.isAssinged = True
    
    def removeVehicle(self):
        self.vehicle = None
        self.isAssinged = False

class TruckParkingSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__(VehicleType.Truck)

    def assignVehicle(self,vehicle):
        if vehicle.type != self.spotType:
            raise("Wrong Parking spot type")
            return
        self.vehicle = vehicle
        self.isAssinged = True
    
    def removeVehicle(self):
        self.vehicle = None
        self.isAssinged = False