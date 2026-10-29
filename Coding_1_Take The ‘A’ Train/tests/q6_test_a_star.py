import unittest
from YardSearcher import YardSearcher

class TestAStar(unittest.TestCase):

    def _test_informed_helper(self, filepath, optimal_path_length, explored_maximum):
        searcher = YardSearcher(filepath)
        action_sequence, nodes_explored = searcher.astar_search(searcher.init, searcher.goal)
        print(filepath)
        print("Explored:", nodes_explored) 

        # Verify the solution exists
        self.assertIsNotNone(action_sequence, f"No solution found for {filepath}")
        
        # Apply the action sequence and verify it reaches the goal.
        # Since there may be more than one optimal path
        state_applied_actions = searcher.apply_action_sequence(action_sequence, searcher.init)
        self.assertEqual(state_applied_actions, 
                         searcher.goal, 
                        f"Action sequence doesn't reach goal for {filepath}")
        
        # Verify the path length is optimal
        self.assertEqual(len(action_sequence), 
                         optimal_path_length,
                        f"Expected optimal path length {optimal_path_length}, got {len(action_sequence)} for {filepath}.")
        
        # Make sure the nodes explored don't exceed the explored nodes cap
        self.assertLessEqual(nodes_explored, 
                             explored_maximum, 
                             f"Expected number of explored nodes to be less than {explored_maximum}, got {nodes_explored}.")

    def test_informed_1(self):
        self._test_informed_helper("./yards/yard_4_MEDIUM.json", 
                                   optimal_path_length=14, 
                                   explored_maximum=10000)

    def test_informed_2(self):
        self._test_informed_helper("./yards/yard_5_HARD.json", 
                                   optimal_path_length=22, 
                                   explored_maximum=100000)

    def test_informed_3(self):
        self._test_informed_helper("./yards/yard_6_EXTREME.json", 
                                   optimal_path_length=25, 
                                   explored_maximum=500000)


    