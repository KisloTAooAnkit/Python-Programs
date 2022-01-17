import datetime
from Theatre import Theatre
from  Movie import Movie
class Show:
    
    def __init__(self) -> None:
        self.__id = None
        self.__showTime : datetime = datetime.datetime.now()
        self.__movie : Movie = None
        self.__theater : Theatre = None
    