"""
Init file to make tests directory a Python package
"""

from .q1_test_addition import TestAddition
from .q2_test_fruit import TestFruit
from .q3_test_shop_smart import TestShopSmart

__all__ = ['TestAddition', 'TestFruit', 'TestShopSmart']
