import unittest
from PropClauses import PropClause, ResolveNodeProp
from ResolutionProver import ResolutionProver

class TestResolutionProverProve(unittest.TestCase):
    def test_prove_simple_success(self):
        """Test proving a simple goal that succeeds"""
        kb = [
            PropClause('A', 'B'),
            PropClause('A')
        ]

        prover = ResolutionProver(kb)
        goal = ResolveNodeProp(PropClause('A'))

        solutions, completed = prover.prove(goal)

        self.assertTrue(completed)
        self.assertEqual(len(solutions), 1)

        for solution in solutions:
            self.assertTrue(solution.support.is_empty())

    def test_prove_no_solution(self):
        """Test proving a goal with no solution"""
        kb = [
            PropClause('B', 'C'),
            PropClause('D', 'E')
        ]

        prover = ResolutionProver(kb)
        goal = ResolveNodeProp(PropClause('A'))

        solutions, completed = prover.prove(goal)

        self.assertTrue(completed)
        self.assertEqual(len(solutions), 0)

    def test_prove_max_explore_limit(self):
        """Test that prove respects max_explore limit"""
        kb = [
            PropClause('A', 'A'),  # Will generate infinite successors
            PropClause('A', 'B', 'A')
        ]

        prover = ResolutionProver(kb, max_explore=10)
        goal = ResolveNodeProp(PropClause('A'))

        solutions, completed = prover.prove(goal)

        self.assertFalse(completed)

    def test_prove_multi_step(self):
        """Test proving with multiple resolution steps"""
        kb = [
            PropClause('A', 'B'),
            PropClause('B', 'C'),
            PropClause('C')
        ]

        prover = ResolutionProver(kb)
        goal = ResolveNodeProp(PropClause('A'))

        solutions, completed = prover.prove(goal)

        self.assertTrue(completed)
        self.assertGreater(len(solutions), 0)

    def test_prove_empty_kb(self):
        """Test proving with empty KB"""
        kb = []

        prover = ResolutionProver(kb)
        goal = ResolveNodeProp(PropClause('A'))

        solutions, completed = prover.prove(goal)

        self.assertTrue(completed)
        self.assertEqual(len(solutions), 0)

    def test_prove_already_empty(self):
        """Test proving when goal is already empty clause"""
        kb = [PropClause('A')]

        prover = ResolutionProver(kb)
        goal = ResolveNodeProp(PropClause())

        solutions, completed = prover.prove(goal)

        self.assertTrue(completed)
        self.assertEqual(len(solutions), 1)
        self.assertTrue(solutions[0].support.is_empty())
