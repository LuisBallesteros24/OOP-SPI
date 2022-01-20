from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,color : str,filled : bool,side : float):
        Rectangle.__init__(self,color,filled,side,side)
    
    def getSide(self):
        self.getLength()
    
    def setSide(self, side : float):
        self.setLength(side)
        self.setWidth(side)

    def setLength(self, length: float):
        self.setSide(length)
    
    def setWidth(self, width: float):
        self.setWidth(width)

    def __str__(self):
        return "Square[Rectangle[color="+self.getColor()+",filled="+str(self.getFilled())+"],width="+str(self.getWidth())+",length="+str(self.getLength)+"]"