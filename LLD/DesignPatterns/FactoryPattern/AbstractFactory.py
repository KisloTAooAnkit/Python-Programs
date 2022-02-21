

from abc import ABC, abstractmethod

class Door(ABC):
    @abstractmethod
    def getDescription(self):
        pass

class WoodenDoor(Door):
    def getDescription(self):
        print("hey i am wooden door")

class IronDoor(Door):
    def getDescription(self):
        print('hey i am iron door')

class DoorFittingExpert(ABC):
    @abstractmethod
    def getSkillDescription(self):
        pass

class Carpenter(DoorFittingExpert):
    def getSkillDescription(self):
        print("Hey i can fix wooden doors")

class Welder(DoorFittingExpert):
    def getSkillDescription(self):
        print("Hey i can fix iron doors")


class DoorFactory(ABC):
    @abstractmethod
    def makeDoor(self) -> Door:
        pass
    @abstractmethod
    def callFittingExpert(self) -> DoorFittingExpert:
        pass


class WoodenDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        door = WoodenDoor()
        return door
    
    def callFittingExpert(self) -> DoorFittingExpert:
        expert = Carpenter()
        return expert

class IronDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return IronDoor()
    def callFittingExpert(self) -> DoorFittingExpert:
        return Welder()


woodenFactory = WoodenDoorFactory()
woodenDoor = woodenFactory.makeDoor()
carpenter = woodenFactory.callFittingExpert()
woodenDoor.getDescription()
carpenter.getSkillDescription()

ironFactory = IronDoorFactory()
ironDoor = ironFactory.makeDoor()
welder = ironFactory.callFittingExpert()
ironDoor.getDescription()
welder.getSkillDescription()