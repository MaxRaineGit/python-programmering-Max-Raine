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
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("New points must be numeric, either int or float")
        else:
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
    
    def __repr__(self):
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y}, lenght = {self.length}, width = {self.width})"
    
    def __str__(self):
        return f"{self.__class__.__name__} at cordinates x = {self.x}, y = {self.y} and the object has a length of {self.length} and a width of {self.width})"
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.length, self.width) == (other.length, other.width)
        return False
    
    def is_point_inside(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("New points must be numeric, either int or float")
        else:
            return (
                self.x - self.length / 2 <= x <= self.x + self.length / 2
                and 
                self.y - self.width / 2 <= y <= self.y + self.width / 2
            )
        
    def is_square(self):
        return math.isclose(self.length, self.width, rel_tol=1e-9, abs_tol=1e-9)
    
    

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
    
    def __repr__(self):
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y}, Radius = {self.radius})"
    
    def __str__(self):
        return f"{self.__class__.__name__} at cordinates x = {self.x}, y = {self.y} and a radius of {self.radius})"
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.radius) == (other.radius)
        return False
    
    def is_point_inside(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
           raise ValueError("New points must be numeric, either int or float") 
        else:
            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            return distance <= self.radius
        
    def is_unit_circle(self):
        return math.isclose(self.radius, 1, rel_tol=1e-9, abs_tol=1e-9)
    