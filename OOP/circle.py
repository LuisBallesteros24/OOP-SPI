from shapes import Shape
from math import pi

class Circle(Shape):
    def __init__(self,color :str, filled: bool, radius : float):
        Shape.__init__(self, color, filled)
        self._radius = radius
    
    def getRadius(self):
        return self._radius

    def setRadius(self, radius : float):
        self._radius = radius


    def getArea(self):
        return pi*(self.getRadius()**2)

    def getPerimeter(self):
        return 2*pi*self.getRadius()

    def __str__(self):
        return "Circle[Shape[color="+self.getColor()+",filled="+str(self.getFilled())+"],radius="+str(self.getRadius())+"]"