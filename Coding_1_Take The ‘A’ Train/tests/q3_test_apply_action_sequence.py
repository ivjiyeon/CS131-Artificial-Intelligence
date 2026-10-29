import unittest
from YardSearcher import YardSearcher

class TestApplyActionSequence(unittest.TestCase):
    # Testing move sequences on yard 1...
    # Init state: "init": [["*"], ["a"], ["b"]]


    def test_apply_action_sequence_1(self):
        searcher = YardSearcher("./yards/yard_1_EASY.json")
        
        actions = [('LEFT', 2, 1), ('RIGHT', 1, 2)]
        
        final_state = searcher.apply_action_sequence(actions, searcher.init)
        self.assertEqual(final_state, searcher.init)

    def test_apply_action_sequence_2(self):
        searcher = YardSearcher("./yards/yard_1_EASY.json")
        
        actions = [('LEFT', 2, 1), ('LEFT', 3, 1), ("RIGHT", 1, 2)]
        end_state = [["*", "a"], ["b"], []]
        
        final_state = searcher.apply_action_sequence(actions, searcher.init)
        self.assertEqual(final_state, end_state)

    def test_apply_action_sequence_3(self):
        searcher = YardSearcher("./yards/yard_1_EASY.json")
        
        actions = [('LEFT', 3, 1), ('LEFT', 2, 1), ("RIGHT", 1, 2)]
        end_state = [["*", "b"], ["a"], []]
        
        final_state = searcher.apply_action_sequence(actions, searcher.init)
        self.assertEqual(final_state, end_state)

    def test_apply_action_sequence_4(self):
        searcher = YardSearcher("./yards/yard_1_EASY.json")
        
        actions = [('LEFT', 2, 1), ('LEFT', 3, 1), ("RIGHT", 1, 2), ("RIGHT", 1, 3)]
        end_state = [["*"], ["b"], ["a"]]
        
        final_state = searcher.apply_action_sequence(actions, searcher.init)
        self.assertEqual(final_state, end_state)

    def test_apply_action_sequence_5(self):
        searcher = YardSearcher("./yards/yard_1_EASY.json")
        
        actions = [('LEFT', 2, 1), ('LEFT', 3, 1)]
        
        final_state = searcher.apply_action_sequence(actions, searcher.init)
        self.assertEqual(final_state, searcher.goal)