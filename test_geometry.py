import unittest
from geometry import Circle, Triangle

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, 8)
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # Невозможный треугольник

    def test_triangle_is_right_angled(self):
            self.assertTrue(Triangle(3, 4, 5).is_right_angled())
            self.assertFalse(Triangle(3, 4, 6).is_right_angled())


if __name__ == '__main__':
    unittest.main()