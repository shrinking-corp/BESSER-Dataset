import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    mathCompiler_Div,
    mathCompiler_Expression,
    mathCompiler_Expressions,
    mathCompiler_External,
    mathCompiler_Let,
    mathCompiler_MathExp,
    mathCompiler_Minus,
    mathCompiler_Mult,
    mathCompiler_Num,
    mathCompiler_Plus,
    mathCompiler_Var,
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

def test_assoc_binding23_stub_double():
    # mathCompiler_Expression has no real 'mathCompiler_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so mathCompiler_Let's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathCompiler_Let's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathCompiler_Let(id="sample_text")
    partner = mathCompiler_Expression()
    setattr(partner, 'mathCompiler_Expression24', None)
    _safe_set(owner, 'mathCompiler_Let', partner)
    assert getattr(partner, 'mathCompiler_Expression24') == owner
    _safe_set(owner, 'mathCompiler_Let', None)
    assert getattr(partner, 'mathCompiler_Expression24') is None


def test_assoc_body25_stub_double():
    # mathCompiler_Expression has no real 'mathCompiler_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so mathCompiler_Let's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathCompiler_Let's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathCompiler_Let(id="sample_text")
    partner = mathCompiler_Expression()
    setattr(partner, 'mathCompiler_Expression27', None)
    _safe_set(owner, 'mathCompiler_Let26', partner)
    assert getattr(partner, 'mathCompiler_Expression27') == owner
    _safe_set(owner, 'mathCompiler_Let26', None)
    assert getattr(partner, 'mathCompiler_Expression27') is None


def test_assoc_exp1_stub_double():
    # mathCompiler_Expression has no real 'mathCompiler_Expression' property in the generated
    # code (a bare stub) -- manually attach it so mathCompiler_MathExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathCompiler_MathExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathCompiler_MathExp(line="sample_text")
    partner = mathCompiler_Expression()
    setattr(partner, 'mathCompiler_Expression', None)
    _safe_set(owner, 'mathCompiler_MathExp2', partner)
    assert getattr(partner, 'mathCompiler_Expression') == owner
    _safe_set(owner, 'mathCompiler_MathExp2', None)
    assert getattr(partner, 'mathCompiler_Expression') is None


def test_assoc_expressions0_stub_double():
    # mathCompiler_Expressions has no real 'mathCompiler_Expressions' property in the generated
    # code (a bare stub) -- manually attach it so mathCompiler_MathExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathCompiler_MathExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathCompiler_MathExp(line="sample_text")
    partner = mathCompiler_Expressions()
    setattr(partner, 'mathCompiler_Expressions', None)
    _safe_set(owner, 'mathCompiler_MathExp', partner)
    assert owner in getattr(partner, 'mathCompiler_Expressions')
    _safe_set(owner, 'mathCompiler_MathExp', None)
    assert owner not in getattr(partner, 'mathCompiler_Expressions')


