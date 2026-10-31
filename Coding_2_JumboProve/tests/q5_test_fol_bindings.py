import unittest
from FOLClauses import FOLAtom, FOLClause

class TestFOLBindings(unittest.TestCase):
    # Tests for get_terminal_binding
    def test_get_terminal_binding_direct(self):
        """Test getting terminal binding for direct mapping"""
        bindings = {'?x': 'John', '?y': 'Mary'}

        result = FOLAtom.get_terminal_binding('?x', bindings)

        self.assertEqual(result, 'John')

    def test_get_terminal_binding_chain(self):
        """Test getting terminal binding through chain"""
        bindings = {'?x': '?y', '?y': '?z', '?z': 'John'}

        result = FOLAtom.get_terminal_binding('?x', bindings)

        self.assertEqual(result, 'John')

    def test_get_terminal_binding_long_chain(self):
        """Test getting terminal binding through long chain"""
        bindings = {
            '?a': '?b',
            '?b': '?c',
            '?c': '?d',
            '?d': '?e',
            '?e': 'FinalValue'
        }

        result = FOLAtom.get_terminal_binding('?a', bindings)

        self.assertEqual(result, 'FinalValue')

    # Tests for get_final_bindings
    def test_get_final_bindings_simple(self):
        """Test getting final bindings for simple clause"""
        clause = FOLClause(
            FOLAtom('Parent', '?x', '?y')
        )

        intermediate_bindings = {'?x': 'John', '?y': 'Mary'}

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result, {'?x': 'John', '?y': 'Mary'})

    def test_get_final_bindings_with_chains(self):
        """Test getting final bindings with variable chains"""
        clause = FOLClause(
            FOLAtom('Parent', '?x', '?y')
        )

        intermediate_bindings = {'?x': '?z', '?z': 'John', '?y': 'Mary'}

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result['?x'], 'John')
        self.assertEqual(result['?y'], 'Mary')

    def test_get_final_bindings_multiple_atoms(self):
        """Test getting final bindings for clause with multiple atoms"""
        clause = FOLClause(
            FOLAtom('Parent', '?x', '?y'),
            FOLAtom('Sibling', '?y', '?z')
        )

        intermediate_bindings = {'?x': 'John', '?y': 'Mary', '?z': 'Bob'}

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result, {'?x': 'John', '?y': 'Mary', '?z': 'Bob'})

    def test_get_final_bindings_partial(self):
        """Test getting final bindings when some variables unbound"""
        clause = FOLClause(
            FOLAtom('Parent', '?x', '?y')
        )

        intermediate_bindings = {'?x': 'John'}

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result['?x'], 'John')
        self.assertEqual(result['?y'], '?y')

    def test_get_final_bindings_no_variables(self):
        """Test getting final bindings for clause with no variables"""
        clause = FOLClause(
            FOLAtom('Parent', 'John', 'Mary')
        )

        intermediate_bindings = {}

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result, {})

    def test_get_final_bindings_complex_chain(self):
        """Test getting final bindings with complex chains"""
        clause = FOLClause(
            FOLAtom('Ancestor', '?x', '?y'),
            FOLAtom('Human', '?z')
        )

        intermediate_bindings = {
            '?x': '?a',
            '?a': 'John',
            '?y': '?b',
            '?b': '?c',
            '?c': 'Mary',
            '?z': 'Bob'
        }

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result['?x'], 'John')
        self.assertEqual(result['?y'], 'Mary')
        self.assertEqual(result['?z'], 'Bob')

    def test_get_final_bindings_empty_clause(self):
        """Test getting final bindings for empty clause"""
        clause = FOLClause()

        intermediate_bindings = {'?x': 'John'}

        result = clause.get_final_bindings(intermediate_bindings)

        self.assertEqual(result, {})
