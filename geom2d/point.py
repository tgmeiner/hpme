import math

from geom2d.vector import Vector
from geom2d import nums

class Point:

    #method for represent 2D points; coordinates stored as attributes of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #method for computing the distance between two points
    def distance_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x ** 2 + delta_y **2)

    #methods for addition and subtraction operations asdf
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self,other):
        return Vector(
            self.x - other.x, 
            self.y - other.y
        )
    
    #displacing a point by a vector a given number of times
    def displaced(self, vector: Vector, times=1):
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

    #are two defined points equal?
    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other,Point):
            return False

        return nums.are_close_enough(self.x, other.x) and \
            nums.are_close_enough(self.y, other.y)

    

