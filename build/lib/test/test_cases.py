"""Test Cases for X_power_y"""

import unittest
from src.code.function_x_power_y import ScientificFunction


class MyTestCase(unittest.TestCase):
    """functions are defined for checking the test cases"""

    def test_pos_pos(self):
        """When both the input is positive"""
        test_obj = ScientificFunction()
        self.assertEqual(test_obj.x_power_y(2, 2), pow(2, 2))

    def test_neg_pos(self):
        """When power is positive and base is negative"""
        test_obj = ScientificFunction()
        self.assertEqual(test_obj.x_power_y(-2, 2), pow(-2, 2))

    def test_neg_neg(self):
        """When both the input is negative"""
        test_obj = ScientificFunction()
        self.assertEqual(test_obj.x_power_y(-2, -2), pow(-2, -2))

    def test_pos_neg(self):
        """When power is negative and base is positive"""
        test_obj = ScientificFunction()
        self.assertEqual(test_obj.x_power_y(2, -2), pow(2, -2))

    def test_string_num(self):
        """When power is positive and base is string"""
        test_obj = ScientificFunction()
        self.assertEqual(test_obj.x_power_y("string", 2), "Value Error")

    def test_num_string(self):
        """When power is string and base is positive"""
        test_obj = ScientificFunction()
        self.assertEqual(test_obj.x_power_y(2, "string"), "Value Error")


if __name__ == '__main__':
    unittest.main()
