from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,color : str,filled : bool,side : float):
        Rectangle.__init__(self,color,filled,side,side)
    
    def get_side(self):
        return self._width
    
    def set_side(self, side : float):
        self._width = side
        self._length = side

    def __str__(self):
        if (self._filled):
            print ("the rectangle is color ", self._color, 
            "is filled and has a side of ", self._width)
        else:
            print("the rectangle is color ", self._color, 
            "is not filled and has a side of ", self._width)
