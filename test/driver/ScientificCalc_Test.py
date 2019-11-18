"""Test Cases for X_power_y"""

import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
    """functions are defined for checking the main cases"""

    def test_x_power_y_pos_pos(self):
        """When both the input is positive"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.x_power_y(2, 2), pow(2, 2))

    def test_neg_pos(self):
        """When power is positive and base is negative"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.x_power_y(-2, 2), pow(-2, 2))

    def test_neg_neg(self):
        """When both the input is negative"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.x_power_y(-2, -2), pow(-2, -2))

    def test_pos_neg(self):
        """When power is negative and base is positive"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.x_power_y(2, -2), pow(2, -2))

    def test_string_num(self):
        """When power is positive and base is string"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.x_power_y("string", 2), "Value Error")

    def test_num_string(self):
        """When power is string and base is positive"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.x_power_y(2, "string"), "Value Error")
