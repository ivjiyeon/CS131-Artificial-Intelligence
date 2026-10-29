"""
Test module for addition functionality (Question 1)
"""

import unittest
from addition import add


class TestAddition(unittest.TestCase):

    def test_add_1(self):
        """Check that 2+2 is 4"""
        result = add(2,2)
        self.assertEqual(result, 4, f"Expected 4, got {result}")

    def test_add_2(self):
        """Check that 2+6 is 8"""
        result = add(2,6)
        self.assertEqual(result, 8, f"Expected 8, got {result}")

    def test_add_3(self):
        """Check that 3+3 is 6"""
        result = add(3,3)
        self.assertEqual(result, 6, f"Expected 6, got {result}")