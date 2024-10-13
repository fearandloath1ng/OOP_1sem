import unittest
import math
from position import Position
from bounding_box import BoundingBox
from geometric_primitive import GeometricPrimitive
from geometry_constants import GeometryConstants
from point import Point
from ellipse import Ellipse

class TestPosition(unittest.TestCase):
    def test_initialization(self):
        pos = Position(5.0, 10.0)
        self.assertEqual(pos.x, 5.0)
        self.assertEqual(pos.y, 10.0)

    def test_str(self):
        pos = Position(5, 10)
        self.assertEqual(str(pos), "Position(5, 10)")

class TestBoundingBox(unittest.TestCase):
    def test_contains(self):
        bbox = BoundingBox(0, 10, 0, 10)
        point_inside = Position(5, 5)
        point_outside = Position(11, 5)
        self.assertTrue(bbox.contains(point_inside))
        self.assertFalse(bbox.contains(point_outside))

    def test_str(self):
        bbox = BoundingBox(0, 10, 0, 10)
        self.assertEqual(str(bbox), "BoundingBox(0, 10, 0, 10)")

class TestGeometricPrimitive(unittest.TestCase):
    def test_initialization(self):
        geom = GeometricPrimitive("red", True)
        self.assertEqual(geom.color, "red")
        self.assertTrue(geom.visible)

    def test_toggle_visibility(self):
        geom = GeometricPrimitive("red", True)
        geom.toggle_visibility()
        self.assertFalse(geom.visible)

class TestGeometryConstants(unittest.TestCase):
    def test_is_within_bounds(self):
        bbox = BoundingBox(0, 10, 0, 10)
        pos_inside = Position(5, 5)
        pos_outside = Position(15, 15)
        self.assertTrue(GeometryConstants.is_within_bounds(pos_inside, bbox))
        self.assertFalse(GeometryConstants.is_within_bounds(pos_outside, bbox))

class TestPoint(unittest.TestCase):
    def test_initialization(self):
        point = Point(1, 2, "blue", True)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.color, "blue")
        self.assertTrue(point.visible)

    def test_str(self):
        point = Point(1, 2, "blue", True)
        self.assertEqual(str(point), "Point(1, 2, Color: blue, Visible: True)")

class TestEllipse(unittest.TestCase):
    def test_area(self):
        ellipse = Ellipse(Position(0, 0), 3, 2, "green", True)
        self.assertAlmostEqual(ellipse.area(), math.pi * 3 * 2)

    def test_perimeter(self):
        ellipse = Ellipse(Position(0, 0), 3, 2, "green", True)
        expected_perimeter = math.pi * (3 + 2) * (1 + ((3 - 2) ** 2 / (3 + 2) ** 2) / 4)
        self.assertAlmostEqual(ellipse.perimeter(), expected_perimeter)

    def test_str(self):
        ellipse = Ellipse(Position(0, 0), 3, 2, "green", True)
        self.assertIn("Ellipse(Center:", str(ellipse))

if __name__ == "__main__":
    unittest.main()
