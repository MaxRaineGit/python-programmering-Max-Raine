# To get access to math.pi to calculate circle area and omkrets
import math

# Added a parent class so i can use isinstance to limit comparing between just rectangle and circle and raise an error if tried otherwise
class Shape:
    def __init__(self):
        pass

    @property
    def area(self):
        pass

    @property
    def omkrets(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.length, self.width) == (other.length, other.width)
        return False
    
    def __lt__(self, other):
        if isinstance(other, Shape):
            return (self.area, self.omkrets) < (other.area, other.omkrets)
        raise ValueError("Please only compare objects from the class Shape or it's subclasses")
    
    def __le__(self, other):
        if isinstance(other, Shape):
            return (self.area, self.omkrets) <= (other.area, other.omkrets)
        raise ValueError("Please only compare objects from the class Shape or it's subclasses")
    
    def __gt__(self, other):
        if isinstance(other, Shape):
            return (self.area, self.omkrets) > (other.area, other.omkrets)
        raise ValueError("Please only compare objects from the class Shape or it's subclasses")
    
    def __ge__(self, other):
        if isinstance(other, Shape):
            return (self.area, self.omkrets) >= (other.area, other.omkrets)
        raise ValueError("Please only compare objects from the class Shape or it's subclasses")
        



class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width
    
     
    @property
    def omkrets(self):
        return (self.length + self.width) * 2
    
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @property
    def omkrets(self):
        return math.pi * self.radius * 2
    