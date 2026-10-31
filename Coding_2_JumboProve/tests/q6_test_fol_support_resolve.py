import unittest
from FOLClauses import FOLAtom, FOLClause

class TestFOLSupportResolve(unittest.TestCase):
    def test_support_resolve_basic_unification(self):
        """Test basic resolution with unification"""
        kb_clause = FOLClause(
            FOLAtom('Parent', 'John', 'Mary'),
            FOLAtom('Human', 'Mary')
        )
        support_clause = FOLClause(
            FOLAtom('Parent', 'John', 'Mary'),
            FOLAtom('Mortal', 'John')
        )

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        new_clause, bindings = result
        self.assertEqual(len(new_clause.atoms), 2)

    def test_support_resolve_with_variables(self):
        """Test resolution with variables"""
        kb_clause = FOLClause(
            FOLAtom('Parent', '?x', '?y'),
            FOLAtom('Human', '?y')
        )
        support_clause = FOLClause(
            FOLAtom('Parent', 'John', 'Mary')
        )

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        new_clause, bindings = result
        # Check structure: should have 1 atom remaining
        self.assertEqual(len(new_clause.atoms), 1)
        # Check the remaining atom is Human predicate
        self.assertEqual(new_clause.atoms[0].atom[0], 'Human')
        # Check we have 2 bindings (for the two variables in kb_clause)
        self.assertEqual(len(bindings), 2)
        # Check that 'John' and 'Mary' are in the binding values
        binding_values = set(bindings.values())
        self.assertIn('John', binding_values)
        self.assertIn('Mary', binding_values)

    def test_support_resolve_empty_result(self):
        """Test resolution resulting in empty clause"""
        kb_clause = FOLClause(FOLAtom('Parent', 'John', 'Mary'))
        support_clause = FOLClause(FOLAtom('Parent', 'John', 'Mary'))

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        new_clause, bindings = result
        self.assertTrue(new_clause.is_empty())

    def test_support_resolve_fail_no_unification(self):
        """Test resolution fails when atoms don't unify"""
        kb_clause = FOLClause(
            FOLAtom('Parent', 'John', 'Mary'),
            FOLAtom('Human', 'Mary')
        )
        support_clause = FOLClause(
            FOLAtom('Parent', 'Bob', 'Alice'),
            FOLAtom('Mortal', 'Bob')
        )

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNone(result)

    def test_support_resolve_fail_no_unification_2(self):
        """Test resolution fails when atoms don't unify 2"""
        kb_clause = FOLClause(FOLAtom('Parent', 'John', 'Mary'))
        support_clause = FOLClause(FOLAtom('Parent', 'Mary', 'Mary'))

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNone(result)

    def test_support_resolve_with_existing_bindings(self):
        """Test resolution with existing bindings"""
        kb_clause = FOLClause(
            FOLAtom('Parent', '?x', '?y'),
            FOLAtom('Human', '?y')
        )
        support_clause = FOLClause(
            FOLAtom('Parent', '?z', 'Mary')
        )

        existing_bindings = {'?z': 'John'}
        result = FOLClause.support_resolve(support_clause, kb_clause, existing_bindings)

        self.assertIsNotNone(result)
        new_clause, bindings = result
        # Check structure: should have 1 atom remaining (Human)
        self.assertEqual(len(new_clause.atoms), 1)
        self.assertEqual(new_clause.atoms[0].atom[0], 'Human')
        # Check we have correct number of bindings (at least 2 from kb_clause variables)
        self.assertGreaterEqual(len(bindings), 2)
        # Check that 'John' and 'Mary' are in the binding values
        binding_values = set(bindings.values())
        self.assertIn('John', binding_values)
        self.assertIn('Mary', binding_values)

    def test_support_resolve_multiple_variables(self):
        """Test resolution with multiple variables"""
        kb_clause = FOLClause(
            FOLAtom('Grandparent', '?x', '?z'),
            FOLAtom('Parent', '?x', '?y'),
            FOLAtom('Parent', '?y', '?z')
        )
        support_clause = FOLClause(
            FOLAtom('Grandparent', 'John', 'Bob')
        )

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        new_clause, bindings = result

        # Check structure: should have 2 atoms remaining (the two Parent atoms)
        self.assertEqual(len(new_clause.atoms), 2)
        # Check both atoms are Parent predicates
        self.assertEqual(new_clause.atoms[0].atom[0], 'Parent')
        self.assertEqual(new_clause.atoms[1].atom[0], 'Parent')
        # Check we have correct number of bindings (3 variables: ?x, ?z)
        self.assertEqual(len(bindings), 2)
        # Check that 'John' and 'Bob' are in the binding values
        binding_values = set(bindings.values())
        self.assertIn('John', binding_values)
        self.assertIn('Bob', binding_values)

    def test_support_resolve_single_atom(self):
        """Test resolution with single atom clauses"""
        kb_clause = FOLClause(FOLAtom('Human', '?x'))
        support_clause = FOLClause(FOLAtom('Human', 'Socrates'))

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        new_clause, bindings = result
        # Check that clause is empty (both atoms resolved)
        self.assertTrue(new_clause.is_empty())
        # Check we have 1 binding (for ?x)
        self.assertEqual(len(bindings), 1)
        # Check that 'Socrates' is in the binding values
        self.assertIn('Socrates', bindings.values())

    def test_support_resolve_different_predicates(self):
        """Test resolution fails with different predicates"""
        kb_clause = FOLClause(FOLAtom('Parent', 'John', 'Mary'))
        support_clause = FOLClause(FOLAtom('Sibling', 'John', 'Mary'))

        result = FOLClause.support_resolve(support_clause, kb_clause)

        self.assertIsNone(result)


    def test_support_resolve_complex_unification(self):
        """Test resolution with complex unification"""
        kb_clause = FOLClause(
            FOLAtom('Ancestor', '?x', '?y'),
                FOLAtom('Parent', '?x', '?z'),
                FOLAtom('Ancestor', '?z', '?y')
        )
        support_clause = FOLClause(
            FOLAtom('Ancestor', 'John', '?w')
        )

        result = FOLClause.support_resolve(support_clause, kb_clause)


        self.assertIsNotNone(result)
        new_clause, bindings = result



        # Check structure: should have 2 atoms remaining (Parent and Ancestor)
        self.assertEqual(len(new_clause.atoms), 2)
        # Check predicates of remaining atoms
        predicates = [atom.atom[0] for atom in new_clause.atoms]
        self.assertIn('Parent', predicates)
        self.assertIn('Ancestor', predicates)
        # Check we have at least 2 bindings (for kb_clause variables: ?x, ?y)
        self.assertGreaterEqual(len(bindings), 2)
        # Check that 'John' is in the binding values
        self.assertIn('John', bindings.values())
