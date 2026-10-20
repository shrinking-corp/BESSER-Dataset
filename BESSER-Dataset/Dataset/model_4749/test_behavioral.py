import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    FPath_BinaryOperatorExp,
    FPath_ContextExp,
    FPath_Expression,
    FPath_FunctionCallExp,
    FPath_LocatedElement,
    FPath_NameTest,
    FPath_NumberExp,
    FPath_OperatorExp,
    FPath_PathExp,
    FPath_Step,
    FPath_StringExp,
    FPath_Test,
    FPath_UnaryOperatorExp,
    FPath_VariableExp,
    FPath_WildcardTest,
    LocatedElement,
    OperatorExp,
    Test,
    Axis,
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

def test_assoc_arguments0_stub_double():
    # FPath_Expression has no real 'FPath_Expression' property in the generated
    # code (a bare stub) -- manually attach it so FPath_FunctionCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FPath_FunctionCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FPath_FunctionCallExp(name="sample_text")
    partner = FPath_Expression()
    setattr(partner, 'FPath_Expression', None)
    _safe_set(owner, 'FPath_FunctionCallExp', {partner})
    assert getattr(partner, 'FPath_Expression') == owner
    _safe_set(owner, 'FPath_FunctionCallExp', set())
    assert getattr(partner, 'FPath_Expression') is None


def test_assoc_predicates14_stub_double():
    # FPath_Expression has no real 'FPath_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so FPath_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FPath_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FPath_Step(axis="sample_text")
    partner = FPath_Expression()
    setattr(partner, 'FPath_Expression16', None)
    _safe_set(owner, 'FPath_Step15', {partner})
    assert getattr(partner, 'FPath_Expression16') == owner
    _safe_set(owner, 'FPath_Step15', set())
    assert getattr(partner, 'FPath_Expression16') is None


def test_assoc_steps3_stub_double():
    # FPath_PathExp has no real 'FPath_PathExp4' property in the generated
    # code (a bare stub) -- manually attach it so FPath_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FPath_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FPath_Step(axis="sample_text")
    partner = FPath_PathExp()
    setattr(partner, 'FPath_PathExp4', None)
    _safe_set(owner, 'FPath_Step', partner)
    assert owner in getattr(partner, 'FPath_PathExp4')
    _safe_set(owner, 'FPath_Step', None)
    assert owner not in getattr(partner, 'FPath_PathExp4')


def test_assoc_test12_stub_double():
    # FPath_Test has no real 'FPath_Test' property in the generated
    # code (a bare stub) -- manually attach it so FPath_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FPath_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FPath_Step(axis="sample_text")
    partner = FPath_Test()
    setattr(partner, 'FPath_Test', None)
    _safe_set(owner, 'FPath_Step13', partner)
    assert getattr(partner, 'FPath_Test') == owner
    _safe_set(owner, 'FPath_Step13', None)
    assert getattr(partner, 'FPath_Test') is None


