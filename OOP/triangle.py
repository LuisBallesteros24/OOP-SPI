from shapes import Shape

class Triangle(Shape):
    def __init__(self,color :str, filled: bool, side : float):
        Shape.__init__(self, color, filled)
        self._side = side
    
    def getSideLength(self):
        return self._side

    def setSideLength(self, side : float):
        self._side = side


    def getArea(self):
        return ((3**0.5)/4)*(self.getSideLength()**2)

    def getPerimeter(self):
        return 3*self.getSideLength()

    def __str__(self):
        return "Circle[Shape[color="+self.getColor()+",filled="+str(self.getFilled())+"],radius="+str(self.getRadius())+"]"