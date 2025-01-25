import math 
class Shape:
    def area(self):
        raise NotImplementedError("not yet implemented")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area (self):
        value1= self.length * self.width
        return f"The area of the Rectangle is: {value1}"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self):
        value2= float(math.pi * self.radius ** 2)
        return f"The area of the Circle is: {value2}"    
           