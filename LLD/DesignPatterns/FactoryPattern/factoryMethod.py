from math import *
from enum import Enum


class CoordinateSystem(Enum):
    Cartesian,Polar = 1,2

class Point:

    def __init__(self,a,b) -> None:
        self.x = a
        self.y = b
#we extracted factory outside 
class PointFactory:
    @staticmethod
    def newCartesianPoint(x,y):
        return Point(x,y)

    @staticmethod
    def newPolarPoint(rho,theta):
        return Point(rho*sin(theta), rho*cos(theta))

p1 = PointFactory.newCartesianPoint(2,4)
p2 = PointFactory.newPolarPoint(20,40)
p3 = Point(2,4) #due to constructor being public this we can still create obj which is disadv
print(p1,p2)