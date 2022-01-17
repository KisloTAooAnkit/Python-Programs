
from Genre import Genre
from Languages import Languages

class Movie:

    def __init__(self) -> None:
        self.__movieName = None
        self.__rating = None

        self.__language : Languages = None
        self.__genre : Genre = None
    

