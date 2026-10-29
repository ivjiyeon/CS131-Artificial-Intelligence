"""
Test module for fruit purchasing functionality (Question 2)
"""

import unittest
from buyLotsOfFruit import buyLotsOfFruit


class TestFruit(unittest.TestCase):
    
    def test_fruit_1(self):
        order_list = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
        result = buyLotsOfFruit(order_list)
        self.assertEqual(result, 12.25)

    def test_fruit_2(self):
        order_list = [('pears', 3.0), ('grapes', 1.5), ('limes', 3.0)]
        result = buyLotsOfFruit(order_list)
        self.assertEqual(result, None)

    def test_fruit_3(self):
        order_list = [('strawberries', 1.5), ('oranges', 2.0)]
        result = buyLotsOfFruit(order_list)
        self.assertEqual(result, 4.5)