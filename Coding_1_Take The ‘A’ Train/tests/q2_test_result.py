import unittest
from YardSearcher import YardSearcher

class TestResult(unittest.TestCase):
    def test_result_1(self):
        searcher = YardSearcher()

        init_state = [['*'],['e']]
        goal_state = [[],['*','e']]
        
        action = ('RIGHT', 1, 2)
        new_state = searcher.result(action, init_state)

        self.assertEqual(new_state[0], goal_state[0])
        self.assertEqual(new_state[1], goal_state[1])

    def test_result_2(self):
        searcher = YardSearcher()

        init_state = [['a','*','b'], ['c','d']]
        goal_state = [['a','*'], ['b','c','d']]
        
        action = ('RIGHT', 1, 2)
        new_state = searcher.result(action, init_state)

        self.assertEqual(new_state[0], goal_state[0])
        self.assertEqual(new_state[1], goal_state[1])

    def test_result_3(self):
        searcher = YardSearcher()

        init_state = [['a'], ['*','e']]
        goal_state = [[], ['a','*','e']]
        
        action = ('RIGHT', 1, 2)
        new_state = searcher.result(action, init_state)

        self.assertEqual(new_state[0], goal_state[0])
        self.assertEqual(new_state[1], goal_state[1])

    def test_result_4(self):
        searcher = YardSearcher()

        init_state = [['*'], ['e']]
        goal_state = [['*','e'], []]
        
        action = ('LEFT', 2, 1)
        new_state = searcher.result(action, init_state)

        self.assertEqual(new_state[0], goal_state[0])
        self.assertEqual(new_state[1], goal_state[1])

    def test_result_5(self):
        searcher = YardSearcher()

        init_state = [['a','*','b'], ['c','d']]
        goal_state = [['a','*','b','c'], ['d']]
        
        action = ('LEFT', 2, 1)
        new_state = searcher.result(action, init_state)

        self.assertEqual(new_state[0], goal_state[0])
        self.assertEqual(new_state[1], goal_state[1])
        