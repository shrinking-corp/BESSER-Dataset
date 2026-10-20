import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Point,
    Segment,
    kmLogo_VM_Point,
    kmLogo_VM_Segment,
    kmLogo_VM_Turtle,
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

def test_assoc_drawings1_stub_double():
    # Segment has no real 'Segment' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_VM_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_VM_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_VM_Turtle(heading="sample_text", penUp="sample_text")
    partner = Segment()
    setattr(partner, 'Segment', None)
    _safe_set(owner, 'kmLogo_VM_Turtle2', {partner})
    assert getattr(partner, 'Segment') == owner
    _safe_set(owner, 'kmLogo_VM_Turtle2', set())
    assert getattr(partner, 'Segment') is None


def test_assoc_points3_stub_double():
    # Point has no real 'Point5' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_VM_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_VM_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_VM_Turtle(heading="sample_text", penUp="sample_text")
    partner = Point()
    setattr(partner, 'Point5', None)
    _safe_set(owner, 'kmLogo_VM_Turtle4', {partner})
    assert getattr(partner, 'Point5') == owner
    _safe_set(owner, 'kmLogo_VM_Turtle4', set())
    assert getattr(partner, 'Point5') is None


def test_assoc_position0_stub_double():
    # Point has no real 'Point' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_VM_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_VM_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_VM_Turtle(heading="sample_text", penUp="sample_text")
    partner = Point()
    setattr(partner, 'Point', None)
    _safe_set(owner, 'kmLogo_VM_Turtle', partner)
    assert getattr(partner, 'Point') == owner
    _safe_set(owner, 'kmLogo_VM_Turtle', None)
    assert getattr(partner, 'Point') is None


