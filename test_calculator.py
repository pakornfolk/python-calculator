import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(6, 9), 3)

    # Add the following test methods to the TestCalculator class:

# add() --- (2 test cases)
    def test_add_positive(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-5, 3), -2)

# subtract() --- (2 test cases)
    def test_subtract_basic(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-2, -5), 3)

# multiply() --- (2 test cases)
    def test_multiply_normal(self):
        self.assertEqual(self.calc.multiply(7, 4), 28)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

# divide() --- (2 test cases)
    def test_divide_basic(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_equal_case(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

# modulo() --- (2 test cases)
    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(17, 5), 2)

    def test_modulo_equal_case(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)


if __name__ == '__main__':
    unittest.main()
