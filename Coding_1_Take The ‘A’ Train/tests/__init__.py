"""
Init file to make tests directory a Python package
"""

from .q1_test_possible_actions import TestPossibleActions
from .q2_test_result import TestResult
from .q3_test_apply_action_sequence import TestApplyActionSequence
from .q4_test_uninformed_search import TestUninformedSearch
from .q6_test_a_star import TestAStar


__all__ = ['TestPossibleActions', 'TestResult', 'TestApplyActionSequence', 'TestUninformedSearch', 'TestAStar']
