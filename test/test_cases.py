"""Test Cases for X_power_y"""

import unittest
from src.code import function_x_power_y


class MyTestCase(unittest.TestCase):
    """functions are defined for checking the test cases"""

    def test_pos_pos(self):
        """When both the input is positive"""
        self.assertEqual(function_x_power_y.x_power_y(2, 2), pow(2, 2))

    def test_neg_pos(self):
        """When power is positive and base is negative"""
        self.assertEqual(function_x_power_y.x_power_y(-2, 2), pow(-2, 2))

    def test_neg_neg(self):
        """When both the input is negative"""
        self.assertEqual(function_x_power_y.x_power_y(-2, -2), pow(-2, -2))

    def test_pos_neg(self):
        """When power is negative and base is positive"""
        self.assertEqual(function_x_power_y.x_power_y(2, -2), pow(2, -2))


if __name__ == '__main__':
    unittest.main()
