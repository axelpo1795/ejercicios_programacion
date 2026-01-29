import math


class Circle:
    "Clase que representa un círculo con un radio específico."
    
    def __init__(self, radius):
        """
        constructor del círculo.
        """
        self.radius = radius
    
    def get_area(self):
        """
        Calcula y retorna el área del círculo.
        """
        return math.pi * self.radius ** 2
