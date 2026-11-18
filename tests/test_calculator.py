"""These unittest tests are also collected by pytest."""
import unittest
from src.calculator import add, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_decimal(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-4, 3), -12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_fraction(self):
        self.assertAlmostEqual(divide(1, 4), 0.25)

    def test_divide_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
