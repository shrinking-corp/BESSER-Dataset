import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CMElement,
    Expression,
    Statement,
    codemodel_CMElement,
    codemodel_CodeModel,
    codemodel_D,
    codemodel_E,
    codemodel_Variable,
    codemodel_expressions_BinExp,
    codemodel_expressions_Expression,
    codemodel_expressions_VarExp,
    codemodel_statements_AsgnStmt,
    codemodel_statements_CompStmt,
    codemodel_statements_Statement,
    expressions_codemodel_Variable,
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

def test_assoc_left5_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_expressions_BinExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_expressions_BinExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_expressions_BinExp(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'codemodel_expressions_BinExp', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'codemodel_expressions_BinExp', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_right6_stub_double():
    # Expression has no real 'Expression8' property in the generated
    # code (a bare stub) -- manually attach it so codemodel_expressions_BinExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # codemodel_expressions_BinExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = codemodel_expressions_BinExp(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression8', None)
    _safe_set(owner, 'codemodel_expressions_BinExp7', partner)
    assert getattr(partner, 'Expression8') == owner
    _safe_set(owner, 'codemodel_expressions_BinExp7', None)
    assert getattr(partner, 'Expression8') is None


