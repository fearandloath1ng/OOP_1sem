import math
from geometric_primitive import GeometricPrimitive
from position import Position

class Ellipse(GeometricPrimitive):
    def __init__(self, center: Position, semi_major_axis: float, semi_minor_axis: float, color: str, visible: bool):
        super().__init__(color, visible)
        self.center = center
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def area(self) -> float:
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def perimeter(self) -> float:
        # Приближенная формула для периметра эллипса
        h = (self.semi_major_axis - self.semi_minor_axis) ** 2 / (self.semi_major_axis + self.semi_minor_axis) ** 2
        return math.pi * (self.semi_major_axis + self.semi_minor_axis) * (1 + h / 4)

    def __str__(self):
        return f"Ellipse(Center: {self.center}, Semi-major: {self.semi_major_axis}, Semi-minor: {self.semi_minor_axis}, Color: {self.color}, Visible: {self.visible})"
