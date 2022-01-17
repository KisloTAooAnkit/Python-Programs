import datetime
import Show
class Ticket:

    def __init__(self) -> None:
        self.__id = None
        self.__bookingTime : datetime = None
        self.__noOfSeats : int = None
        self.__bookedShow : Show = None