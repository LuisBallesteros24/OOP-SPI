from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__ (self,color,filled):
        self._color= color
        self._filled= filled
    
    @abstractmethod
    def Shape(self):
        pass

    def getColor(self):
        return self._color

    def setColor(self, color : str):
        self._color = color

    def getFilled(self):
        return self._filled

    def setFilled(self, filled : bool):
        self._filled = filled

    @abstractmethod
    def getArea():
        pass

    @abstractmethod
    def getPerimeter():
        pass

    @abstractmethod
    def toString():
        pass