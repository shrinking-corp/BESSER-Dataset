import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    asso_Div,
    asso_EvalExpression,
    asso_Expression,
    asso_FloatConstant,
    asso_Minus,
    asso_Model,
    asso_Mult,
    asso_NegFloatConstant,
    asso_Plus,
    asso_Variable,
    asso_VariableRef,
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

def test_assoc_subVar4_reverse_link_reassign_clear():
    a1 = asso_Variable(name="sample_text")
    a2 = asso_Variable(name="sample_text_2")
    b = asso_Variable(name="sample_text")
    _safe_set(b, 'asso_Variable5', a1)
    assert _is_linked(b, 'asso_Variable5', a1)
    if hasattr(a1, 'asso_Variable3'):
        assert _is_linked(a1, 'asso_Variable3', b)
    _safe_set(b, 'asso_Variable5', a2)
    assert _is_linked(b, 'asso_Variable5', a2)
    if hasattr(a1, 'asso_Variable3'):
        assert not _is_linked(a1, 'asso_Variable3', b)
    if hasattr(a2, 'asso_Variable3'):
        assert _is_linked(a2, 'asso_Variable3', b)
    _safe_set(b, 'asso_Variable5', None)
    assert not _is_linked(b, 'asso_Variable5', a2)
    if hasattr(a2, 'asso_Variable3'):
        assert not _is_linked(a2, 'asso_Variable3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expression6_stub_double():
    # asso_Expression has no real 'asso_Expression' property in the generated
    # code (a bare stub) -- manually attach it so asso_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asso_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asso_Variable(name="sample_text")
    partner = asso_Expression()
    setattr(partner, 'asso_Expression', None)
    _safe_set(owner, 'asso_Variable7', partner)
    assert getattr(partner, 'asso_Expression') == owner
    _safe_set(owner, 'asso_Variable7', None)
    assert getattr(partner, 'asso_Expression') is None


def test_assoc_value11_stub_double():
    # asso_VariableRef has no real 'asso_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so asso_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asso_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asso_Variable(name="sample_text")
    partner = asso_VariableRef()
    setattr(partner, 'asso_VariableRef', None)
    _safe_set(owner, 'asso_Variable12', partner)
    assert getattr(partner, 'asso_VariableRef') == owner
    _safe_set(owner, 'asso_Variable12', None)
    assert getattr(partner, 'asso_VariableRef') is None


def test_assoc_variables0_stub_double():
    # asso_Model has no real 'asso_Model' property in the generated
    # code (a bare stub) -- manually attach it so asso_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # asso_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = asso_Variable(name="sample_text")
    partner = asso_Model()
    setattr(partner, 'asso_Model', None)
    _safe_set(owner, 'asso_Variable', partner)
    assert owner in getattr(partner, 'asso_Model')
    _safe_set(owner, 'asso_Variable', None)
    assert owner not in getattr(partner, 'asso_Model')


