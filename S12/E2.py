class Shape:
    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError("La subclase debe implementar este método")

    @abstractmethod
    def calculate_perimeter(self):
        raise NotImplementedError("La subclase debe implementar este método")  

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1416 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length
    