import unittest
from PropClauses import PropClause

class TestPropSupportResolve(unittest.TestCase):
    def test_support_resolve_basic_1(self):
        """Test basic resolution with matching literals"""
        kb_clause = PropClause('A', 'B', 'C')
        support_clause = PropClause('A', 'D')

        result = PropClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        self.assertEqual(result.literals, ['B', 'C', 'D'])

    def test_support_resolve_basic_2(self):
        """Test resolution with single literals"""
        kb_clause = PropClause('P')
        support_clause = PropClause('P')

        result = PropClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        self.assertTrue(result.is_empty())

    def test_support_resolve_no_match(self):
        """Test resolution with non-matching literals"""
        kb_clause = PropClause('A', 'B')
        support_clause = PropClause('C', 'D')

        result = PropClause.support_resolve(support_clause, kb_clause)

        self.assertIsNone(result)

    def test_support_resolve_multiple_literals(self):
        """Test resolution with multiple remaining literals"""
        kb_clause = PropClause('X', 'Y', 'Z', 'W')
        support_clause = PropClause('X', 'A', 'B', 'C')

        result = PropClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        self.assertEqual(result.literals, ['Y', 'Z', 'W', 'A', 'B', 'C'])

    def test_support_resolve_empty_remainder(self):
        """Test resolution resulting in empty clause"""
        kb_clause = PropClause('Q')
        support_clause = PropClause('Q')

        result = PropClause.support_resolve(support_clause, kb_clause)

        self.assertIsNotNone(result)
        self.assertTrue(result.is_empty())
