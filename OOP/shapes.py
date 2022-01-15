from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__ (self,color : str,filled : bool):
        self._color = color
        self._filled = filled
    
    @abstractmethod
    def shape(self):
        pass

    def get_color(self):
        return self._color

    def set_color(self, color : str):
        self._color = color

    def get_filled(self):
        return self._filled

    def set_filled(self, filled : bool):
        self._filled = filled

    @abstractmethod
    def get_area():
        pass

    @abstractmethod
    def get_perimeter():
        pass

    @abstractmethod
    def __str__():
        pass