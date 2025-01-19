import unittest
from simple_calculator import SimpleCalculator

#this is our tester
class TestOperator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(2,2), 4)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(2,2), 0)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(2,4), 8)

    def test_division(self):
        self.assertRaises(SimpleCalculator.divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = SimpleCalculator.divide(1 , 0)      