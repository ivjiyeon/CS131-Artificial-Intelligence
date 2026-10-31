import unittest
from FOLClauses import FOLAtom, FOLClause, ResolveNodeFOL

class TestResolveNodeFOLGenerateSuccessors(unittest.TestCase):
    def test_generate_successors_basic(self):
        """Test generating successors with simple KB"""
        kb = [
            FOLClause(FOLAtom('Parent', 'John', 'Mary')),
            FOLClause(FOLAtom('Parent', 'John', 'Bob'))
        ]

        support = FOLClause(FOLAtom('Parent', 'John', '?x'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 2)
        for successor in successors:
            self.assertTrue(successor.support.is_empty())

    def test_generate_successors_with_variables(self):
        """Test generating successors with variables in KB"""
        kb = [
            FOLClause(
                FOLAtom('Parent', '?x', '?y'),
                FOLAtom('Human', '?y')
            ),
            FOLClause(
                FOLAtom('Parent', '?a', '?b'),
                FOLAtom('Mortal', '?b')
            )
        ]

        support = FOLClause(FOLAtom('Parent', 'John', 'Mary'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        print(successors)

        self.assertEqual(len(successors), 2)
        for successor in successors:
            self.assertEqual(len(successor.support.atoms), 1)
            # Check that 'John' and 'Mary' are in the binding values
            binding_values = set(successor.bindings.values())
            self.assertIn('John', binding_values)
            self.assertIn('Mary', binding_values)

    def test_generate_successors_no_matches(self):
        """Test generating successors with no matching clauses"""
        kb = [
            FOLClause(FOLAtom('Sibling', 'Bob', 'Alice')),
            FOLClause(FOLAtom('Parent', 'Mary', 'Bob'))
        ]

        support = FOLClause(FOLAtom('Parent', 'John', 'Mary'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 0)

    def test_generate_successors_empty_kb(self):
        """Test generating successors with empty KB"""
        kb = []

        support = FOLClause(FOLAtom('Parent', 'John', 'Mary'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 0)

    def test_generate_successors_with_bindings(self):
        """Test generating successors with existing bindings"""
        kb = [
            FOLClause(
                FOLAtom('Ancestor', '?x', '?y'),
                FOLAtom('Parent', '?x', '?z'),
                FOLAtom('Ancestor', '?z', '?y')
            )
        ]

        support = FOLClause(FOLAtom('Ancestor', 'John', '?w'))
        existing_bindings = {'?w': 'Mary'}
        node = ResolveNodeFOL(support, existing_bindings)

        successors = node.generate_successors(kb)

        self.assertGreater(len(successors), 0)
        for successor in successors:
            self.assertIn('?w', successor.bindings)

    def test_generate_successors_complex(self):
        """Test generating successors with complex KB"""
        kb = [
            FOLClause(
                FOLAtom('Grandparent', '?x', '?z'),
                FOLAtom('Parent', '?x', '?y'),
                FOLAtom('Parent', '?y', '?z')
            ),
            FOLClause(
                FOLAtom('Grandparent', 'John', 'Bob'),
                FOLAtom('Happy', 'John')
            )
        ]

        support = FOLClause(FOLAtom('Grandparent', '?a', '?b'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 2)

    def test_generate_successors_multiple_atoms_support(self):
        """Test generating successors when support has multiple atoms"""
        kb = [
            FOLClause(FOLAtom('Human', 'Socrates')),
            FOLClause(FOLAtom('Human', 'Plato'))
        ]

        support = FOLClause(
            FOLAtom('Human', '?x'),
            FOLAtom('Mortal', '?x')
        )
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 2)
        for successor in successors:
            self.assertEqual(len(successor.support.atoms), 1)
            self.assertEqual(successor.support.atoms[0].atom[0], 'Mortal')

    def test_generate_successors_preserves_bindings(self):
        """Test that successors preserve and extend bindings"""
        kb = [
            FOLClause(
                FOLAtom('Parent', 'John', 'Mary'),
                FOLAtom('Human', 'Mary')
            )
        ]

        support = FOLClause(FOLAtom('Parent', '?x', '?y'))
        existing_bindings = {'?z': 'Bob'}
        node = ResolveNodeFOL(support, existing_bindings)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 1)
        self.assertIn('?z', successors[0].bindings)
        self.assertEqual(successors[0].bindings['?z'], 'Bob')
        self.assertIn('?x', successors[0].bindings)
        self.assertEqual(successors[0].bindings['?x'], 'John')

    def test_generate_successors_different_predicates(self):
        """Test generating successors with different predicates in KB"""
        kb = [
            FOLClause(FOLAtom('Parent', 'John', 'Mary')),
            FOLClause(FOLAtom('Sibling', 'Bob', 'Alice')),
            FOLClause(FOLAtom('Parent', 'Mary', 'Bob'))
        ]

        support = FOLClause(FOLAtom('Parent', '?x', '?y'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 2)

    def test_generate_successors_different_predicates_2(self):
        """Test generating successors with different predicates in KB"""
        kb = [
            FOLClause(FOLAtom('Parent', 'John', 'Mary')),
            FOLClause(FOLAtom('Parent', 'Bob', 'Alice')),
            FOLClause(FOLAtom('Parent', 'Mary', 'Bob'))
        ]

        support = FOLClause(FOLAtom('Parent', '?x', '?y'))
        node = ResolveNodeFOL(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 3)
