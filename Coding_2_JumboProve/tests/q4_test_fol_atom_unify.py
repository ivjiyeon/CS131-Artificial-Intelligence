import unittest
from FOLClauses import FOLAtom

class TestFOLAtomUnify(unittest.TestCase):
    def test_unify_identical_atoms(self):
        """Test unifying two identical atoms"""
        atom1 = FOLAtom('Parent', 'John', 'Mary')
        atom2 = FOLAtom('Parent', 'John', 'Mary')

        result = FOLAtom.unify(atom1, atom2)

        self.assertIsNotNone(result)
        self.assertEqual(result, {})

    def test_unify_with_variable(self):
        """Test unifying atom with variable"""
        atom1 = FOLAtom('Parent', '?x', 'Mary')
        atom2 = FOLAtom('Parent', 'John', 'Mary')

        result = FOLAtom.unify(atom1, atom2)

        self.assertIsNotNone(result)
        self.assertEqual(result, {'?x': 'John'})

    def test_unify_both_variables(self):
        """Test unifying two atoms with variables"""
        atom1 = FOLAtom('Parent', '?x', '?y')
        atom2 = FOLAtom('Parent', 'John', 'Mary')

        result = FOLAtom.unify(atom1, atom2)

        self.assertIsNotNone(result)
        self.assertEqual(result, {'?x': 'John', '?y': 'Mary'})

    def test_unify_variable_to_variable(self):
        """Test unifying variable to variable"""
        atom1 = FOLAtom('Parent', '?x', '?y')
        atom2 = FOLAtom('Parent', '?z', '?w')

        result = FOLAtom.unify(atom1, atom2)

        self.assertIsNotNone(result)
        self.assertIn('?x', result)
        self.assertIn('?y', result)

    def test_unify_fail_different_predicates(self):
        """Test unification fails with different predicates"""
        atom1 = FOLAtom('Parent', 'John', 'Mary')
        atom2 = FOLAtom('Sibling', 'John', 'Mary')

        result = FOLAtom.unify(atom1, atom2)

        self.assertFalse(result)

    def test_unify_fail_different_constants(self):
        """Test unification fails with different constants"""
        atom1 = FOLAtom('Parent', 'John', 'Mary')
        atom2 = FOLAtom('Parent', 'John', 'Jane')

        result = FOLAtom.unify(atom1, atom2)

        self.assertFalse(result)

    def test_unify_with_existing_bindings(self):
        """Test unification with existing bindings"""
        atom1 = FOLAtom('Parent', '?x', 'Mary')
        atom2 = FOLAtom('Parent', 'John', 'Mary')

        existing_bindings = {'?y': 'Bob'}
        result = FOLAtom.unify(atom1, atom2, existing_bindings)

        self.assertIsNotNone(result)
        self.assertEqual(result, {'?x': 'John', '?y': 'Bob'})

    def test_unify_chain_bindings(self):
        """Test unification with chained bindings"""
        atom1 = FOLAtom('Parent', '?x', '?y')
        atom2 = FOLAtom('Parent', '?z', 'Mary')

        bindings = {'?z': 'John'}
        result = FOLAtom.unify(atom1, atom2, bindings)

        self.assertIsNotNone(result)
        self.assertEqual(result['?x'], 'John')
        self.assertEqual(result['?y'], 'Mary')

    def test_unify_single_argument(self):
        """Test unifying atoms with single argument"""
        atom1 = FOLAtom('Human', '?x')
        atom2 = FOLAtom('Human', 'Socrates')

        result = FOLAtom.unify(atom1, atom2)

        self.assertIsNotNone(result)
        self.assertEqual(result, {'?x': 'Socrates'})

    def test_unify_multiple_same_variables(self):
        """Test unifying with same variable appearing multiple times"""
        atom1 = FOLAtom('Equals', '?x', '?x')
        atom2 = FOLAtom('Equals', 'John', 'John')

        result = FOLAtom.unify(atom1, atom2)

        self.assertIsNotNone(result)
        self.assertEqual(result, {'?x': 'John'})
