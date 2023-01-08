from geom2d.point import Point
from geom2d.vector import Vector

#create vector between two points
def make_vector_between(p: Point, q: Point):
    return q-p

#create a versor (vector of unit length)
def make_versor(u:float, v:float):
    return Vector (u,v).normalized()

#create a versor between two points
def make_versor_between(p: Point, q: Point):
    return make_vector_between(p,q).normalized()


