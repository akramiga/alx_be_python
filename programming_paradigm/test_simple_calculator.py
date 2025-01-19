import unittest
from simple_calculator import SimpleCalculator

#this is our tester
class TestOperator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,2), 4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,2), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,4), 8)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = self.calc.divide(1 , 0)      
if __name__ == "__main__":
    unittest.main()