#!/usr/bin/python3
"""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit tests for the max_integer function."""

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -2, -3, -1]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_integers_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_no_arguments(self):
        self.assertIsNone(max_integer())

    def test_non_list_argument(self):
        with self.assertRaises(TypeError):
            max_integer("string")
