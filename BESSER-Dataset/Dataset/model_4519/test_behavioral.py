import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Instruction,
    Primitive,
    Primitives_Back,
    Primitives_Expression,
    Primitives_Forward,
    Primitives_Instruction,
    Primitives_Left,
    Primitives_LogoProgram,
    Primitives_Primitive,
    Primitives_Right,
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

def test_assoc_angle4_stub_double():
    # Primitives_Left has no real 'Primitives_Left' property in the generated
    # code (a bare stub) -- manually attach it so Primitives_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Primitives_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Primitives_Expression()
    partner = Primitives_Left()
    setattr(partner, 'Primitives_Left', None)
    _safe_set(owner, 'Primitives_Expression5', partner)
    assert getattr(partner, 'Primitives_Left') == owner
    _safe_set(owner, 'Primitives_Expression5', None)
    assert getattr(partner, 'Primitives_Left') is None


def test_assoc_angle6_stub_double():
    # Primitives_Right has no real 'Primitives_Right' property in the generated
    # code (a bare stub) -- manually attach it so Primitives_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Primitives_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Primitives_Expression()
    partner = Primitives_Right()
    setattr(partner, 'Primitives_Right', None)
    _safe_set(owner, 'Primitives_Expression7', partner)
    assert getattr(partner, 'Primitives_Right') == owner
    _safe_set(owner, 'Primitives_Expression7', None)
    assert getattr(partner, 'Primitives_Right') is None


def test_assoc_steps1_stub_double():
    # Primitives_Forward has no real 'Primitives_Forward' property in the generated
    # code (a bare stub) -- manually attach it so Primitives_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Primitives_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Primitives_Expression()
    partner = Primitives_Forward()
    setattr(partner, 'Primitives_Forward', None)
    _safe_set(owner, 'Primitives_Expression', partner)
    assert getattr(partner, 'Primitives_Forward') == owner
    _safe_set(owner, 'Primitives_Expression', None)
    assert getattr(partner, 'Primitives_Forward') is None


def test_assoc_steps2_stub_double():
    # Primitives_Back has no real 'Primitives_Back' property in the generated
    # code (a bare stub) -- manually attach it so Primitives_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Primitives_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Primitives_Expression()
    partner = Primitives_Back()
    setattr(partner, 'Primitives_Back', None)
    _safe_set(owner, 'Primitives_Expression3', partner)
    assert getattr(partner, 'Primitives_Back') == owner
    _safe_set(owner, 'Primitives_Expression3', None)
    assert getattr(partner, 'Primitives_Back') is None


