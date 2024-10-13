import math

# Base Class - Shape
class Shape:
    """A base class representing a generic shape."""
    
    def area(self):
        """Method to calculate the area of the shape. Should be overridden by subclasses."""
        raise NotImplementedError("The area method must be overridden in subclasses")

# Derived Class - Rectangle
class Rectangle(Shape):
    """Represents a rectangle with length and width."""
    
    def __init__(self, length, width):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    """Represents a circle with a radius."""
    
    def __init__(self, radius):
        """Initialize the Circle with its radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
