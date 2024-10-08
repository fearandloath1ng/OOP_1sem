from position import Position

class BoundingBox:
    def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def contains(self, position: Position) -> bool:
        return self.x_min <= position.x <= self.x_max and self.y_min <= position.y <= self.y_max

    def __str__(self):
        return f"BoundingBox({self.x_min}, {self.x_max}, {self.y_min}, {self.y_max})"
