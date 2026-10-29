import unittest
from YardSearcher import YardSearcher

class TestUninformedSearch(unittest.TestCase):

    def _test_uninformed_helper(self, filepath, optimal_path_length, explored_maximum):
        """Helper method to test a specific yard configuration."""
        searcher = YardSearcher(filepath)
        action_sequence, nodes_explored = searcher.uninformed_search(searcher.init, searcher.goal)
        print(filepath)
        print("Explored:", nodes_explored) 

        # Verify the solution exists
        self.assertIsNotNone(action_sequence, 
                             f"No solution found for {filepath}")
        
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

    def test_uninformed_search_1(self):
        self._test_uninformed_helper("./yards/yard_2_EASY.json", 
                                     optimal_path_length=4, 
                                     explored_maximum=100)
    
    def test_uninformed_search_2(self):
        self._test_uninformed_helper("./yards/yard_3_EASY.json", 
                                     optimal_path_length=6, 
                                     explored_maximum=1000)

    def test_uninformed_search_3(self):
        self._test_uninformed_helper("./yards/yard_4_MEDIUM.json", 
                                     optimal_path_length=14, 
                                     explored_maximum=15000)