from shapes import Shape

class Rectangle(Shape):
    def __init__(self,color : str,filled : bool,width : float, length : float):
        Shape.__init__(self,color,filled)
        self._width = width
        self._length = length
    
    def get_width(self):
        return self._width

    def set_width(self, width : float):
        self._width = width
    
    def get_length(self):
        return self._length

    def set_length(self, length : float):
        self._length = length

    def get_area(self):
        return self._length*self._width

    def get_perimeter(self):
        return 2*self._length+2*self._width
    
    def __str__(self):
        if (self._filled):
            print ("the rectangle is color ", self._color, 
            "is filled and has a width and lenght of ", self._width, self._length )
        else:
            print("the rectangle is color ", self._color, 
            "is not filled and has a width and lenght of ", self._width, self._length)