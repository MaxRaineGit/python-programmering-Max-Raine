# To get access to math.pi to calculate circle area and omkrets
import math

# Added a parent class so i can use isinstance to limit comparing between just rectangle and circle and raise an error if tried otherwise
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def area(self):
        pass

    @property
    def omkrets(self):
        pass

    def move_point(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
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
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width
    
     
    @property
    def omkrets(self):
        return (self.length + self.width) * 2
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.length, self.width) == (other.length, other.width)
        return False
    
    def is_point_inside(self, x, y):
        return (
            self.x - self.length / 2 <= x <= self.x - self.length / 2
            and 
            self.y - self.width / 2 <= y <= self.y - self.width / 2
        )
    
    

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @property
    def omkrets(self):
        return math.pi * self.radius * 2
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.radius) == (other.radius)
        return False
    
    def is_point_inside(self, x, y):
        distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return distance <= self.radius
    