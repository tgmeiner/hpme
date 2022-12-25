import math

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
        return Point(
            self.x - other.x, 
            self.y - other.y
        )


