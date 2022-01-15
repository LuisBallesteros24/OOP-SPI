from shapes import Shape
from math import pi

class Circle(Shape):
    def __init__(self,color :str, filled: bool, radius : float):
        Shape.__init__(self, color, filled)
        self._radius = radius
    
    def get_radius(self):
        return self._radius

    def set_radius(self, radius : float):
        self._radius = radius


    def get_area(self):
        return pi*(self._radius**2)

    def get_perimeter(self):
        return 2*pi*self._radius

    def __str__(self):
        if (self._filled):
            print ("the rectangle is color ", self._color, 
            "is filled and has a radius of ", self._radius )
        else:
            print("the rectangle is color ", self._color, 
            "is not filled and has a radius of ", self._radius )