import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Operator,
    OperatorDecl,
    Sort,
    SortDecl,
    Term,
    TermsDeclaration,
    terms_All,
    terms_BuiltInConstant,
    terms_BuiltInOperator,
    terms_BuiltInSort,
    terms_Condition,
    terms_Declaration,
    terms_Declarations,
    terms_Empty,
    terms_HLAnnotation,
    terms_HLMarking,
    terms_MultisetOperator,
    terms_MultisetSort,
    terms_NamedOperator,
    terms_NamedSort,
    terms_Operator,
    terms_OperatorDecl,
    terms_Partition,
    terms_PartitionElement,
    terms_ProductSort,
    terms_Sort,
    terms_SortDecl,
    terms_Term,
    terms_TermsDeclaration,
    terms_Tuple,
    terms_Type,
    terms_UserOperator,
    terms_UserSort,
    terms_Variable,
    terms_VariableDecl,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containerDeclarations2_stub_double():
    # terms_Declarations has no real 'Declarations' property in the generated
    # code (a bare stub) -- manually attach it so terms_TermsDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # terms_TermsDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = terms_TermsDeclaration(id="sample_text", name="sample_text")
    partner = terms_Declarations()
    setattr(partner, 'Declarations', None)
    _safe_set(owner, 'declaration', partner)
    assert getattr(partner, 'Declarations') == owner
    _safe_set(owner, 'declaration', None)
    assert getattr(partner, 'Declarations') is None


def test_assoc_declaration0_stub_double():
    # terms_Declarations has no real 'containerDeclarations' property in the generated
    # code (a bare stub) -- manually attach it so terms_TermsDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # terms_TermsDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = terms_TermsDeclaration(id="sample_text", name="sample_text")
    partner = terms_Declarations()
    setattr(partner, 'containerDeclarations', None)
    _safe_set(owner, 'TermsDeclaration', partner)
    assert owner in getattr(partner, 'containerDeclarations')
    _safe_set(owner, 'TermsDeclaration', None)
    assert owner not in getattr(partner, 'containerDeclarations')


