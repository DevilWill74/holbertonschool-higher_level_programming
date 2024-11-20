#!/usr/bin/python3
<<<<<<< HEAD
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_unsorted_list(self):
        """Test with an unsorted list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test where max is at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_in_middle(self):
        """Test where max is in the middle"""
        self.assertEqual(max_integer([1, 5, 2, 3]), 5)

    def test_all_same(self):
        """Test with all elements the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_with_floats(self):
        """Test with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_with_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_with_mixed_types(self):
        """Test with mixed types should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

if __name__ == '__main__':
    unittest.main()
=======
"""
    unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class for unittests """
    def test_max_integer(self):
        """ check possible cases edge cases """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([15, 10, 5]), 15)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)

    def test_type_error(self):
        """ type_errors """
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])
>>>>>>> 52f3e4f8f65df1385be3ead4611d152f7f38167a
