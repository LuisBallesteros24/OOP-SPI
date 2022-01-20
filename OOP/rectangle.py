from shapes import Shape

class Rectangle(Shape):
    def __init__(self,color : str,filled : bool,width : float, length : float):
        Shape.__init__(self,color,filled)
        self._width = width
        self._length = length
    
    def getWidth(self):
        return self._width

    def setWidth(self, width : float):
        self._width = width
    
    def getLength(self):
        return self._length

    def setLength(self, length : float):
        self._length = length

    def getArea(self):
        return self.getLength()*self.getWidth()

    def getPerimeter(self):
        return 2*self.getLength()+2*self.getWidth()
    
    def __str__(self):
        return "Rectangle[Shape[color="+self.getColor()+",filled="+str(self.getFilled())+"],width="+str(self.getWidth())+",length="+str(self.getLength)+"]"