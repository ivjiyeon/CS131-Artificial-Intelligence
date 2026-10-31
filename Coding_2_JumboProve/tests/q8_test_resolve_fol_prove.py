import unittest
from ResolutionProver import load_fol_kb, ResolutionProver
from FOLClauses import ResolveNodeFOL


class TestResolveFOLProve(unittest.TestCase):
    """
    Test the resolution prover on various FOL knowledge bases.
    Tests that the prover correctly finds all solutions and produces the expected bindings.
    """

    def test_family_tree(self):
        """Test resolution prover on family_tree.json KB"""
        kb, to_prove = load_fol_kb("./fol_kbs/family_tree.json")
        prover = ResolutionProver(kb, max_explore=500)
        goal_clause = ResolveNodeFOL(to_prove)

        proof, terminate = prover.prove(goal_clause)

        # Should complete successfully
        self.assertTrue(terminate, "Prover should complete within max_explore limit")

        # Should find exactly 2 solutions
        self.assertEqual(len(proof), 2, "Should find 2 grandparent relationships")

        # Extract final bindings
        final_bindings_list = []
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)
            final_bindings_list.append(final_bindings)

        # Expected bindings (order may vary)
        expected = [
            {'?y': 'MARY', '?x': 'BRIAN'},
            {'?y': 'SUE', '?x': 'DOUG'}
        ]

        # Check that we have the expected bindings
        for expected_binding in expected:
            self.assertIn(expected_binding, final_bindings_list,
                         f"Expected binding {expected_binding} not found in results")

    def test_ancestors(self):
        """Test resolution prover on ancestors.json KB"""
        kb, to_prove = load_fol_kb("./fol_kbs/ancestors.json")
        prover = ResolutionProver(kb, max_explore=500)
        goal_clause = ResolveNodeFOL(to_prove)

        proof, terminate = prover.prove(goal_clause)

        # Should complete successfully
        self.assertTrue(terminate, "Prover should complete within max_explore limit")

        # Should find exactly 3 ancestor relationships
        self.assertEqual(len(proof), 3, "Should find 3 ancestor relationships")

        # Extract final bindings
        final_bindings_list = []
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)
            final_bindings_list.append(final_bindings)
        
        # Expected bindings
        expected = [
            {'?x': 'MARY', '?y': 'PAUL'},
            {'?x': 'SUE', '?y': 'MARY'},
            {'?x': 'SUE', '?y': 'PAUL'}
        ]

        # Check that we have the expected bindings
        for expected_binding in expected:
            self.assertIn(expected_binding, final_bindings_list,
                         f"Expected binding {expected_binding} not found in results")

    def test_ancestors_infinite(self):
        """Test resolution prover on ancestors_infinite.json KB

        This KB has a recursive rule that can lead to infinite derivations.
        The prover should hit the max_explore limit.
        """
        kb, to_prove = load_fol_kb("./fol_kbs/ancestors_infinite.json")
        prover = ResolutionProver(kb, max_explore=500)
        goal_clause = ResolveNodeFOL(to_prove)

        proof, terminate = prover.prove(goal_clause)

        # Should NOT complete due to infinite expansion
        self.assertFalse(terminate, "Prover should hit max_explore limit due to infinite expansion")

        # Extract final bindings
        final_bindings_list = []
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)
            final_bindings_list.append(final_bindings)

        # Expected bindings
        expected = [
            {'?x': 'MARY', '?y': 'PAUL'},
            {'?x': 'SUE', '?y': 'MARY'},
            {'?x': 'SUE', '?y': 'PAUL'}
        ]

        # Check that we have the expected bindings
        for expected_binding in expected:
            self.assertIn(expected_binding, final_bindings_list,
                         f"Expected binding {expected_binding} not found in results")

    def test_family_2(self):
        """Test resolution prover on family_2.json KB"""
        kb, to_prove = load_fol_kb("./fol_kbs/family_2.json")
        prover = ResolutionProver(kb, max_explore=500)
        goal_clause = ResolveNodeFOL(to_prove)

        proof, terminate = prover.prove(goal_clause)

        # Should complete successfully
        self.assertTrue(terminate, "Prover should complete within max_explore limit")

        # Should find exactly 2 aunt relationships
        self.assertEqual(len(proof), 2, "Should find 2 aunt relationships")

        # Extract final bindings
        final_bindings_list = []
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)
            final_bindings_list.append(final_bindings)

        # Expected bindings
        expected = [
            {'?x': 'MARY', '?y': 'PAUL'},
            {'?x': 'MARY', '?y': 'JOHN'}
        ]

        # Check that we have the expected bindings
        for expected_binding in expected:
            self.assertIn(expected_binding, final_bindings_list,
                         f"Expected binding {expected_binding} not found in results")

    def test_sentences(self):
        """Test resolution prover on sentences.json KB

        This KB generates simple English sentences using grammar rules.
        """
        kb, to_prove = load_fol_kb("./fol_kbs/sentences.json")
        prover = ResolutionProver(kb, max_explore=500)
        goal_clause = ResolveNodeFOL(to_prove)

        proof, terminate = prover.prove(goal_clause)

        # Should complete successfully
        self.assertTrue(terminate, "Prover should complete within max_explore limit")

        # Should find 32 valid sentences (2 articles * 2 nouns * 2 verbs * 2 articles * 2 nouns)
        self.assertEqual(len(proof), 32, "Should find 32 valid sentence structures")

        # Extract final bindings and verify structure
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)

            # Check that all variables are bound
            self.assertIn('?a', final_bindings)
            self.assertIn('?b', final_bindings)
            self.assertIn('?c', final_bindings)
            self.assertIn('?d', final_bindings)
            self.assertIn('?e', final_bindings)

            # Check that articles are valid
            self.assertIn(final_bindings['?a'], ['A', 'THE'])
            self.assertIn(final_bindings['?d'], ['A', 'THE'])

            # Check that nouns are valid
            self.assertIn(final_bindings['?b'], ['MAN', 'DOG'])
            self.assertIn(final_bindings['?e'], ['MAN', 'DOG'])

            # Check that verb is valid
            self.assertIn(final_bindings['?c'], ['LIKES', 'BITES'])

    def test_down_under(self):
        """Test resolution prover on down_under.json KB

        This KB solves the Australian map coloring problem using 3 colors.
        """
        kb, to_prove = load_fol_kb("./fol_kbs/down_under.json")
        prover = ResolutionProver(kb, max_explore=500)
        goal_clause = ResolveNodeFOL(to_prove)

        proof, terminate = prover.prove(goal_clause)

        # Should complete successfully
        self.assertTrue(terminate, "Prover should complete within max_explore limit")

        # Should find 6 valid colorings (3! = 6 permutations of colors)
        self.assertEqual(len(proof), 6, "Should find 6 valid map colorings")

        # Extract final bindings and verify constraints
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)

            # Check that all states are colored
            self.assertIn('?wa', final_bindings)
            self.assertIn('?nt', final_bindings)
            self.assertIn('?sa', final_bindings)
            self.assertIn('?q', final_bindings)
            self.assertIn('?nsw', final_bindings)
            self.assertIn('?v', final_bindings)

            # Check that colors are valid
            colors = ['RED', 'GREEN', 'BLUE']
            for state in ['?wa', '?nt', '?sa', '?q', '?nsw', '?v']:
                self.assertIn(final_bindings[state], colors)

            # Verify the coloring constraints from the goal clause
            # WA != NT
            self.assertNotEqual(final_bindings['?wa'], final_bindings['?nt'])
            # WA != SA
            self.assertNotEqual(final_bindings['?wa'], final_bindings['?sa'])
            # NT != Q
            self.assertNotEqual(final_bindings['?nt'], final_bindings['?q'])
            # NT != SA
            self.assertNotEqual(final_bindings['?nt'], final_bindings['?sa'])
            # Q != NSW
            self.assertNotEqual(final_bindings['?q'], final_bindings['?nsw'])
            # Q != SA
            self.assertNotEqual(final_bindings['?q'], final_bindings['?sa'])
            # NSW != V
            self.assertNotEqual(final_bindings['?nsw'], final_bindings['?v'])
            # NSW != SA
            self.assertNotEqual(final_bindings['?nsw'], final_bindings['?sa'])
            # V != SA
            self.assertNotEqual(final_bindings['?v'], final_bindings['?sa'])
