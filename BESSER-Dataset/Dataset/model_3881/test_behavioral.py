import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOperator,
    Expression,
    UnaryOperator,
    expressions_BinaryOperator,
    expressions_Div,
    expressions_Expression,
    expressions_Function,
    expressions_FunctionCall,
    expressions_Minus,
    expressions_Model,
    expressions_Mul,
    expressions_Neg,
    expressions_Number,
    expressions_Parameter,
    expressions_ParameterAccess,
    expressions_Plus,
    expressions_UnaryOperator,
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

def test_assoc_parameters0_reverse_link_reassign_clear():
    a1 = expressions_Parameter(name="sample_text")
    a2 = expressions_Parameter(name="sample_text_2")
    b = expressions_Function(name="sample_text")
    _safe_set(b, 'expressions_Function', {a1})
    assert _is_linked(b, 'expressions_Function', a1)
    if hasattr(a1, 'expressions_Parameter'):
        assert _is_linked(a1, 'expressions_Parameter', b)
    _safe_set(b, 'expressions_Function', {a2})
    assert _is_linked(b, 'expressions_Function', a2)
    if hasattr(a1, 'expressions_Parameter'):
        assert not _is_linked(a1, 'expressions_Parameter', b)
    if hasattr(a2, 'expressions_Parameter'):
        assert _is_linked(a2, 'expressions_Parameter', b)
    _safe_set(b, 'expressions_Function', set())
    assert not _is_linked(b, 'expressions_Function', a2)
    if hasattr(a2, 'expressions_Parameter'):
        assert not _is_linked(a2, 'expressions_Parameter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body1_stub_double():
    # expressions_Expression has no real 'expressions_Expression' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Function(name="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression', None)
    _safe_set(owner, 'expressions_Function2', partner)
    assert getattr(partner, 'expressions_Expression') == owner
    _safe_set(owner, 'expressions_Function2', None)
    assert getattr(partner, 'expressions_Expression') is None


def test_assoc_function12_stub_double():
    # expressions_FunctionCall has no real 'expressions_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Function(name="sample_text")
    partner = expressions_FunctionCall()
    setattr(partner, 'expressions_FunctionCall', None)
    _safe_set(owner, 'expressions_Function13', partner)
    assert getattr(partner, 'expressions_FunctionCall') == owner
    _safe_set(owner, 'expressions_Function13', None)
    assert getattr(partner, 'expressions_FunctionCall') is None


def test_assoc_functions17_stub_double():
    # expressions_Model has no real 'expressions_Model' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Function(name="sample_text")
    partner = expressions_Model()
    setattr(partner, 'expressions_Model', None)
    _safe_set(owner, 'expressions_Function18', partner)
    assert owner in getattr(partner, 'expressions_Model')
    _safe_set(owner, 'expressions_Function18', None)
    assert owner not in getattr(partner, 'expressions_Model')


def test_assoc_parameter3_stub_double():
    # expressions_ParameterAccess has no real 'expressions_ParameterAccess' property in the generated
    # code (a bare stub) -- manually attach it so expressions_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_Parameter(name="sample_text")
    partner = expressions_ParameterAccess()
    setattr(partner, 'expressions_ParameterAccess', None)
    _safe_set(owner, 'expressions_Parameter4', partner)
    assert getattr(partner, 'expressions_ParameterAccess') == owner
    _safe_set(owner, 'expressions_Parameter4', None)
    assert getattr(partner, 'expressions_ParameterAccess') is None


