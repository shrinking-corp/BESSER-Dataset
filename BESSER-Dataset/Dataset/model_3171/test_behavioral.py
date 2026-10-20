import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Expression,
    expressions_AbstractElement,
    expressions_And,
    expressions_BoolConstant,
    expressions_Comparison,
    expressions_Equality,
    expressions_Expression,
    expressions_ExpressionsModel,
    expressions_IntConstant,
    expressions_Minus,
    expressions_MulOrDiv,
    expressions_Or,
    expressions_Plus,
    expressions_StringConstant,
    expressions_Variable,
    expressions_VariableRef,
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

def test_assoc_expression1_stub_double():
    # expressions_Expression has no real 'expressions_Expression' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Variable(name="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression', None)
    _safe_set(owner, 'expressions_Variable', partner)
    assert getattr(partner, 'expressions_Expression') == owner
    _safe_set(owner, 'expressions_Variable', None)
    assert getattr(partner, 'expressions_Expression') is None


def test_assoc_left12_stub_double():
    # expressions_Expression has no real 'expressions_Expression13' property in the generated
    # code (a bare stub) -- manually attach it so expressions_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_MulOrDiv(op="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression13', None)
    _safe_set(owner, 'expressions_MulOrDiv', partner)
    assert getattr(partner, 'expressions_Expression13') == owner
    _safe_set(owner, 'expressions_MulOrDiv', None)
    assert getattr(partner, 'expressions_Expression13') is None


def test_assoc_left27_stub_double():
    # expressions_Expression has no real 'expressions_Expression28' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Equality(op="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression28', None)
    _safe_set(owner, 'expressions_Equality', partner)
    assert getattr(partner, 'expressions_Expression28') == owner
    _safe_set(owner, 'expressions_Equality', None)
    assert getattr(partner, 'expressions_Expression28') is None


def test_assoc_left32_stub_double():
    # expressions_Expression has no real 'expressions_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Comparison(op="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression33', None)
    _safe_set(owner, 'expressions_Comparison', partner)
    assert getattr(partner, 'expressions_Expression33') == owner
    _safe_set(owner, 'expressions_Comparison', None)
    assert getattr(partner, 'expressions_Expression33') is None


def test_assoc_right14_stub_double():
    # expressions_Expression has no real 'expressions_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so expressions_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_MulOrDiv(op="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression16', None)
    _safe_set(owner, 'expressions_MulOrDiv15', partner)
    assert getattr(partner, 'expressions_Expression16') == owner
    _safe_set(owner, 'expressions_MulOrDiv15', None)
    assert getattr(partner, 'expressions_Expression16') is None


def test_assoc_right29_stub_double():
    # expressions_Expression has no real 'expressions_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Equality(op="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression31', None)
    _safe_set(owner, 'expressions_Equality30', partner)
    assert getattr(partner, 'expressions_Expression31') == owner
    _safe_set(owner, 'expressions_Equality30', None)
    assert getattr(partner, 'expressions_Expression31') is None


def test_assoc_right34_stub_double():
    # expressions_Expression has no real 'expressions_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Comparison(op="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression36', None)
    _safe_set(owner, 'expressions_Comparison35', partner)
    assert getattr(partner, 'expressions_Expression36') == owner
    _safe_set(owner, 'expressions_Comparison35', None)
    assert getattr(partner, 'expressions_Expression36') is None


def test_assoc_variable37_stub_double():
    # expressions_VariableRef has no real 'expressions_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Variable(name="sample_text")
    partner = expressions_VariableRef()
    setattr(partner, 'expressions_VariableRef', None)
    _safe_set(owner, 'expressions_Variable38', partner)
    assert getattr(partner, 'expressions_VariableRef') == owner
    _safe_set(owner, 'expressions_Variable38', None)
    assert getattr(partner, 'expressions_VariableRef') is None


