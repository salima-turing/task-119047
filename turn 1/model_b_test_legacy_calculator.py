# test_legacy_calculator.py
import unittest
from legacy_calculator import calculate

class TestLegacyCalculator(unittest.TestCase):

    def test_calculate_addition(self):
        self.assertEqual(calculate('add', 10, 20), 30)

    def test_calculate_subtraction(self):
        self.assertEqual(calculate('subtract', 20, 10), 10)

    def test_calculate_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate('invalid', 10, 20)

if __name__ == '__main__':
    unittest.main()
