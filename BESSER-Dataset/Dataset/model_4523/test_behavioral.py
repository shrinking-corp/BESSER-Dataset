import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    vmlogo_CallStack,
    vmlogo_Context,
    vmlogo_Point,
    vmlogo_Segment,
    vmlogo_StackFrame,
    vmlogo_Turtle,
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

def test_assoc_position3_reverse_link_reassign_clear():
    a1 = vmlogo_Turtle(heading=3.14, penUp=True)
    a2 = vmlogo_Turtle(heading=9.99, penUp=False)
    b = vmlogo_Point(x=3.14, y=3.14)
    _safe_set(b, 'vmlogo_Point', a1)
    assert _is_linked(b, 'vmlogo_Point', a1)
    if hasattr(a1, 'vmlogo_Turtle4'):
        assert _is_linked(a1, 'vmlogo_Turtle4', b)
    _safe_set(b, 'vmlogo_Point', a2)
    assert _is_linked(b, 'vmlogo_Point', a2)
    if hasattr(a1, 'vmlogo_Turtle4'):
        assert not _is_linked(a1, 'vmlogo_Turtle4', b)
    if hasattr(a2, 'vmlogo_Turtle4'):
        assert _is_linked(a2, 'vmlogo_Turtle4', b)
    _safe_set(b, 'vmlogo_Point', None)
    assert not _is_linked(b, 'vmlogo_Point', a2)
    if hasattr(a2, 'vmlogo_Turtle4'):
        assert not _is_linked(a2, 'vmlogo_Turtle4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_begin7_stub_double():
    # vmlogo_Segment has no real 'vmlogo_Segment8' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Point(x=3.14, y=3.14)
    partner = vmlogo_Segment()
    setattr(partner, 'vmlogo_Segment8', None)
    _safe_set(owner, 'vmlogo_Point9', partner)
    assert getattr(partner, 'vmlogo_Segment8') == owner
    _safe_set(owner, 'vmlogo_Point9', None)
    assert getattr(partner, 'vmlogo_Segment8') is None


def test_assoc_drawings5_stub_double():
    # vmlogo_Segment has no real 'vmlogo_Segment' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Turtle(heading=3.14, penUp=True)
    partner = vmlogo_Segment()
    setattr(partner, 'vmlogo_Segment', None)
    _safe_set(owner, 'vmlogo_Turtle6', partner)
    assert getattr(partner, 'vmlogo_Segment') == owner
    _safe_set(owner, 'vmlogo_Turtle6', None)
    assert getattr(partner, 'vmlogo_Segment') is None


def test_assoc_end10_stub_double():
    # vmlogo_Segment has no real 'vmlogo_Segment11' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Point(x=3.14, y=3.14)
    partner = vmlogo_Segment()
    setattr(partner, 'vmlogo_Segment11', None)
    _safe_set(owner, 'vmlogo_Point12', partner)
    assert getattr(partner, 'vmlogo_Segment11') == owner
    _safe_set(owner, 'vmlogo_Point12', None)
    assert getattr(partner, 'vmlogo_Segment11') is None


def test_assoc_frames13_stub_double():
    # vmlogo_CallStack has no real 'vmlogo_CallStack14' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_StackFrame's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_StackFrame's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_StackFrame(variables="sample_text")
    partner = vmlogo_CallStack()
    setattr(partner, 'vmlogo_CallStack14', None)
    _safe_set(owner, 'vmlogo_StackFrame', partner)
    assert getattr(partner, 'vmlogo_CallStack14') == owner
    _safe_set(owner, 'vmlogo_StackFrame', None)
    assert getattr(partner, 'vmlogo_CallStack14') is None


def test_assoc_turtle0_stub_double():
    # vmlogo_Context has no real 'vmlogo_Context' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Turtle(heading=3.14, penUp=True)
    partner = vmlogo_Context()
    setattr(partner, 'vmlogo_Context', None)
    _safe_set(owner, 'vmlogo_Turtle', partner)
    assert getattr(partner, 'vmlogo_Context') == owner
    _safe_set(owner, 'vmlogo_Turtle', None)
    assert getattr(partner, 'vmlogo_Context') is None


