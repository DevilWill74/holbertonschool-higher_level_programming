#!/usr/bin/python3
"""Unittest pour max_integer([..])."""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases pour la fonction max_integer."""

    def test_normal_cases(self):
        """Tests avec des listes normales."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_empty_list(self):
        """Test avec une liste vide."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test avec une liste contenant un seul élément."""
        self.assertEqual(max_integer([5]), 5)

    def test_all_same_elements(self):
        """Test avec tous les éléments identiques."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        """Test avec des nombres négatifs."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test avec une liste contenant des nombres positifs et négatifs."""
        self.assertEqual(max_integer([-10, 0, 10, -20, 5]), 10)

    def test_floating_point_numbers(self):
        """Test avec des nombres flottants."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_positions_of_max(self):
        """Test lorsque le maximum est à différentes positions."""
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)  # Max au début
        self.assertEqual(max_integer([1, 5, 10, 2]), 10)  # Max au milieu
        self.assertEqual(max_integer([1, 2, 5, 10]), 10)  # Max à la fin

if __name__ == '__main__':
    unittest.main()
