import unittest
from areaclcu.geometry import circle_area, triangle_area

class TestGeometryFunctions(unittest.TestCase):

    def test_circle_area_positive(self):
        self.assertAlmostEqual(circle_area(5), 78.53981633974483)

    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_circle_area_raises(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_triangle_area_positive(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6)

    def test_triangle_area_zero(self):
        with self.assertRaises(ValueError):
            triangle_area(0, 0, 0)

    def test_triangle_area_raises(self):
        with self.assertRaises(ValueError):
            triangle_area(3, 4, 8)
        with self.assertRaises(ValueError):
            triangle_area(-1, 2, 3)
        with self.assertRaises(ValueError):
            triangle_area(1, 2, 3)  # Тест для проверки невозможности существования треугольника

if __name__ == '__main__':
    unittest.main()
