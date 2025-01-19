import unittest
from simple_calculator import SimpleCalculator

#this is our tester
class TestOperator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2,2), 4)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2,2), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2,4), 8)

    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = self.calculator.divide(1 , 0)      
if __name__ == "__main__":
    unittest.main()