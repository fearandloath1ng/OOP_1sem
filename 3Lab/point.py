from position import Position
from geometric_primitive import GeometricPrimitive

class Point(GeometricPrimitive, Position):
    def __init__(self, x: float, y: float, color: str, visible: bool):
        GeometricPrimitive.__init__(self, color, visible)
        Position.__init__(self, x, y)

    def __str__(self):
        return f"Point({self.x}, {self.y}, Color: {self.color}, Visible: {self.visible})"
