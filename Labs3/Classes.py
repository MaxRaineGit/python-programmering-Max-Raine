# To get access to math.pi to calculate circle area and omkrets
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width
    
     
    @property
    def omkrets(self):
        return (self.length + self.width) * 2
    

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @property
    def omkrets(self):
        return math.pi * self.radius * 2