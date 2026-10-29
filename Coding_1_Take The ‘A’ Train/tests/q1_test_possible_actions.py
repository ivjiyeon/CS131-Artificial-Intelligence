import unittest
from YardSearcher import YardSearcher

class TestPossibleActions(unittest.TestCase):
    def _test_action_helper(self, searcher, correct_actions):
        # There's no guarantee that the actions will be ordered the same way
        # So we sort both of them first to make sure

        sorted_correct_actions = sorted(correct_actions, key=lambda tup: (tup[0],tup[1],tup[2]))
        generated_actions = searcher.possible_actions(searcher.init)
        sorted_generated_actions = sorted(generated_actions, key=lambda tup: (tup[0],tup[1],tup[2]))
        self.assertEqual(sorted_correct_actions, sorted_generated_actions)
    
    def test_possible_actions_1(self):
        searcher = YardSearcher("./yards/yard_1_EASY.json")
        correct_actions = [('LEFT', 2, 1), ('LEFT', 3, 1), ('RIGHT', 1, 2), ('RIGHT', 1, 3)]
        self._test_action_helper(searcher, correct_actions)

    def test_possible_actions_2(self):
        searcher = YardSearcher("./yards/yard_2_EASY.json")
        correct_actions = [('LEFT', 2, 1), ('LEFT', 3, 1), ('LEFT', 4, 1), ('RIGHT', 1, 2), ('RIGHT', 1, 3), ('RIGHT', 1, 4)]
        self._test_action_helper(searcher, correct_actions)
    
    def test_possible_actions_3(self):
        searcher = YardSearcher("./yards/yard_3_EASY.json")
        correct_actions = [('LEFT', 2, 1), ('LEFT', 3, 1), ('LEFT', 4, 1), ('RIGHT', 1, 2), ('RIGHT', 1, 3), ('RIGHT', 1, 4)]
        self._test_action_helper(searcher, correct_actions)

    def test_possible_actions_4(self):
        searcher = YardSearcher("./yards/yard_4_MEDIUM.json")
        correct_actions = [('LEFT', 2, 1), ('LEFT', 5, 1), ('RIGHT', 1, 2), ('RIGHT', 1, 5)]
        self._test_action_helper(searcher, correct_actions)

    def test_possible_actions_5(self):
        searcher = YardSearcher("./yards/yard_5_HARD.json")
        correct_actions = [('RIGHT', 1, 2), ('LEFT', 2, 1), ('RIGHT', 1, 3)]
        self._test_action_helper(searcher, correct_actions)