import math

from geom2d import nums

class Vector:
    def __init__(self,u,v):
        self.u = u
        self.v = v

    #add and sub are to create instances of Vector to hold addition and substraction of projections
    def __add__(self, other):
        return Vector(
            self.u + other.u, 
            self.v + other.v
        )

    def __sub__(self,other):
        return Vector(
            self.u - other.u,
            self.v - other.v
        )

    # scale a vector by multiplying it by a scalar
    def scaled_by (self,factor):
        return Vector(factor * self.u, factor * self.v)


    #return the length of a vector (aka. its norm)
    @property
    def norm(self):
        return math.sqrt(self.u ** 2 + self.v**2)

    #use our numeric comparison and pass in vector's norm
    @property
    def is_normal(self):
        return nums.is_close_to_one(self.norm)

    #normalize a vector and yield a vector with same direction but unitary length (aka. length of one)
    #normalized vector is known as a unit vector or versor
    
    #scale it by the inverse of its norm; divide vector's length by its norm
    def normalized(self):
        return self.scaled_by(1.0/self.norm)

    #to scale it, normalize it and scale by a desired length
    def with_length(self,length):
        return self.normalized().scaled_by(length)

    #implement dot product
    def dot(self,other):
        return (self.u * other.u) + (self.v * other.v)

    #projection of a vector over another vector; direction argument may not be a unit vector, so we
    #normalize it to make sure our formulat works
    def projection_over(self,direction):
        return self.dot(direction.normalized())

    #implement the cross product
    def cross(self,other):
        return (self.u * self.v )-(self.v * other.u)

    #Using the dot and cross products, it’s easy to test whether two vectors are parallel or perpendicular to each other
    #just check if their cross product is zero...

    #are they parallel?
    def is_parallel_to(self,other):
        return nums.is_close_to_zero(
            self.cross(other)
        )

    #are they perpendicular?
    def is_perpendicular_to(self,other):
        return nums.is_close_to_zero(
            self.dot(other)
        )

    #angles between vectors?
    #angle between self and other 
    def angle_value_to(self,other):
        dot_product = self.dot(other)
        norm_product = self.norm * other.norm
        return math.acos(dot_product / norm_product)

    #return value of the angle 
    def angle_to(self, other):
        value= self.angle_value_to(other)
        cross_product = self.cross(other)
        return math.copysign(value,cross_product)

    #rotating a vector returns a new vector
    def rotated_radians(self, radians):
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            self.u*cos - self.v*sin,
            self.u*sin + self.v*cos
        )
    
    #get a perpendicular vector
    def perpendicular (self):
        return Vector(-self.v, self.u)

    #get the opposite vector, rotated by 180deg (pi rads)
    def opposite(self):
        return Vector(-self.u, -self.v)

    #sine projection of vector for it's y vector quantity
    @property
    def sine(self):
        return self.v / self.norm

    #cosine projection for it's x vector quantity
    @property
    def consine(self):
        return self.u / self.norm

    #are two vectors equal?
    def __eq__(self,other):
        if self is other:
            return True
        #
        if not isinstance(other, Vector):
            return False

        return nums.are_close_enough(self.u, other.u) and \
            nums.are_close_enough(self.v, other.v)







