"""
Init file to make tests directory a Python package
"""

from .q1_test_prop_support_resolve import TestPropSupportResolve
from .q2_test_resolve_node_prop_generate_successors import TestResolveNodePropGenerateSuccessors
from .q3_test_resolution_prover_prove import TestResolutionProverProve
from .q4_test_fol_atom_unify import TestFOLAtomUnify
from .q5_test_fol_bindings import TestFOLBindings
from .q6_test_fol_support_resolve import TestFOLSupportResolve
from .q7_test_resolve_node_fol_generate_successors import TestResolveNodeFOLGenerateSuccessors
from .q8_test_resolve_fol_prove import TestResolveFOLProve


__all__ = [
    'TestPropSupportResolve',
    'TestResolveNodePropGenerateSuccessors',
    'TestResolutionProverProve',
    'TestFOLAtomUnify',
    'TestFOLBindings',
    'TestFOLSupportResolve',
    'TestResolveNodeFOLGenerateSuccessors',
    'TestResolveFOLProve'
]
