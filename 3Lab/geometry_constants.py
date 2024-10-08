from position import Position
from bounding_box import BoundingBox

class GeometryConstants:
    @staticmethod
    def is_within_bounds(position: Position, bounding_box: BoundingBox) -> bool:
        return bounding_box.contains(position)
