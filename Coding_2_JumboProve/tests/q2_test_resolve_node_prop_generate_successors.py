import unittest
from PropClauses import PropClause, ResolveNodeProp

class TestResolveNodePropGenerateSuccessors(unittest.TestCase):
    def test_generate_successors_basic(self):
        """Test generating successors with simple KB"""
        kb = [
            PropClause('A', 'B'),
            PropClause('A', 'C'),
            PropClause('D', 'E')
        ]

        support = PropClause('A', 'F')
        node = ResolveNodeProp(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 2)
        self.assertEqual(successors[0].support.literals, ['B', 'F'])
        self.assertEqual(successors[1].support.literals, ['C', 'F'])

    def test_generate_successors_no_matches(self):
        """Test generating successors with no matching clauses"""
        kb = [
            PropClause('B', 'C'),
            PropClause('D', 'E')
        ]

        support = PropClause('A', 'F')
        node = ResolveNodeProp(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 0)

    def test_generate_successors_empty_kb(self):
        """Test generating successors with empty KB"""
        kb = []

        support = PropClause('A', 'B')
        node = ResolveNodeProp(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 0)

    def test_generate_successors_single_literal(self):
        """Test generating successors with single literal clauses"""
        kb = [
            PropClause('P'),
            PropClause('P', 'Q'),
            PropClause('R')
        ]

        support = PropClause('P')
        node = ResolveNodeProp(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 2)
        self.assertTrue(successors[0].support.is_empty())
        self.assertEqual(successors[1].support.literals, ['Q'])

    def test_generate_successors_complex(self):
        """Test generating successors with complex KB"""
        kb = [
            PropClause('X', 'Y', 'Z'),
            PropClause('X', 'A', 'B'),
            PropClause('W', 'V'),
            PropClause('X')
        ]

        support = PropClause('X', 'M', 'N')
        node = ResolveNodeProp(support)

        successors = node.generate_successors(kb)

        self.assertEqual(len(successors), 3)
        self.assertEqual(successors[0].support.literals, ['Y', 'Z', 'M', 'N'])
        self.assertEqual(successors[1].support.literals, ['A', 'B', 'M', 'N'])
        self.assertEqual(successors[2].support.literals, ['M', 'N'])
