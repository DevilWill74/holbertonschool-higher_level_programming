#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_all_same_elements(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10, -20, 5]), 10)

    def test_floating_point_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_max_in_different_positions(self):
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)  # Max at the beginning
        self.assertEqual(max_integer([1, 5, 10, 2]), 10)  # Max in the middle
        self.assertEqual(max_integer([1, 2, 5, 10]), 10)  # Max at the end

if __name__ == '__main__':
    unittest.main()
