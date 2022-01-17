from typing import List
from Show import Show
class Theatre:
    def __init__(self) -> None:
        self.__id = None
        self.__name = None
        self.__location = None
        self.__capacity = None
        self.__shows : List[Show] = list()
    
