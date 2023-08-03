from geom2d.point import Point
from geom2d.vectors import make_vector_between, make_versor_between


class Segment:

    #initialze segment
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end 

    #calculate a segments direction vecture and versor
    @property
    def direction_vector(self):
        return make_vector_between(self.start, self.end)
    
    @property
    def direction_versor(self):
        return make_versor_between(self.start, self.end)
    
    #compute a vector perpendicularto segments direction
    @property
    def normal_versor(self):
        return self.direction_versor.perpendicular()
    

    #calculate length of segment
    @property
    def length(self):
        return self.start.distance_to(self.end)
    

    #Obtaining a point from a segment using parametr t
    def point_at(self, t:float):
        return self.start.displaced(self.direction_vector,t)
    
    #segment's middle point
    @property
    def middle(self):
        return self.point_at(0.5)
    

    

        