from enum import Enum

class VehicleType(Enum):
    Bike,Car,Truck = 1,2,3

class TicketStatus(Enum):
    Inactive,Active,Expired = 1,2,3

class Person:
    def __init__(self,name,age,phone) -> None:
        self.name = name
        self.age = age
        self.phone = phone
    

class Address:
    def __init__(self,pin,floor,nearby):
        pass