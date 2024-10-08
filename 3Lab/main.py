from position import Position
from bounding_box import BoundingBox
from geometry_constants import GeometryConstants
from ellipse import Ellipse

def display_properties(ellipse: Ellipse):
    print(ellipse)

def change_color(ellipse: Ellipse, new_color: str):
    ellipse.color = new_color

if __name__ == "__main__":
    bounding_box = BoundingBox(0, 100, 0, 100)
    position = Position(50, 50)

    if GeometryConstants.is_within_bounds(position, bounding_box):
        ellipse = Ellipse(position, 30, 20, "blue", True)
        display_properties(ellipse)

        change_color(ellipse, "red")
        display_properties(ellipse)
