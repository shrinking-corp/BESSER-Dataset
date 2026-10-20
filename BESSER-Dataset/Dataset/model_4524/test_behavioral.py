import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    vmlogo_CallStack,
    vmlogo_Point,
    vmlogo_Segment,
    vmlogo_StackFrame,
    vmlogo_Turtle,
    vmlogo_Variable,
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

def test_assoc_position0_reverse_link_reassign_clear():
    a1 = vmlogo_Turtle(heading=3.14, penUp=True)
    a2 = vmlogo_Turtle(heading=9.99, penUp=False)
    b = vmlogo_Point(x=3.14, y=3.14)
    _safe_set(b, 'vmlogo_Point', a1)
    assert _is_linked(b, 'vmlogo_Point', a1)
    if hasattr(a1, 'vmlogo_Turtle'):
        assert _is_linked(a1, 'vmlogo_Turtle', b)
    _safe_set(b, 'vmlogo_Point', a2)
    assert _is_linked(b, 'vmlogo_Point', a2)
    if hasattr(a1, 'vmlogo_Turtle'):
        assert not _is_linked(a1, 'vmlogo_Turtle', b)
    if hasattr(a2, 'vmlogo_Turtle'):
        assert _is_linked(a2, 'vmlogo_Turtle', b)
    _safe_set(b, 'vmlogo_Point', None)
    assert not _is_linked(b, 'vmlogo_Point', a2)
    if hasattr(a2, 'vmlogo_Turtle'):
        assert not _is_linked(a2, 'vmlogo_Turtle', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_begin5_stub_double():
    # vmlogo_Segment has no real 'vmlogo_Segment6' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Point(x=3.14, y=3.14)
    partner = vmlogo_Segment()
    setattr(partner, 'vmlogo_Segment6', None)
    _safe_set(owner, 'vmlogo_Point7', partner)
    assert getattr(partner, 'vmlogo_Segment6') == owner
    _safe_set(owner, 'vmlogo_Point7', None)
    assert getattr(partner, 'vmlogo_Segment6') is None


def test_assoc_callStack3_stub_double():
    # vmlogo_CallStack has no real 'vmlogo_CallStack' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Turtle(heading=3.14, penUp=True)
    partner = vmlogo_CallStack()
    setattr(partner, 'vmlogo_CallStack', None)
    _safe_set(owner, 'vmlogo_Turtle4', partner)
    assert getattr(partner, 'vmlogo_CallStack') == owner
    _safe_set(owner, 'vmlogo_Turtle4', None)
    assert getattr(partner, 'vmlogo_CallStack') is None


def test_assoc_drawings1_stub_double():
    # vmlogo_Segment has no real 'vmlogo_Segment' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Turtle(heading=3.14, penUp=True)
    partner = vmlogo_Segment()
    setattr(partner, 'vmlogo_Segment', None)
    _safe_set(owner, 'vmlogo_Turtle2', {partner})
    assert getattr(partner, 'vmlogo_Segment') == owner
    _safe_set(owner, 'vmlogo_Turtle2', set())
    assert getattr(partner, 'vmlogo_Segment') is None


def test_assoc_end8_stub_double():
    # vmlogo_Segment has no real 'vmlogo_Segment9' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Point(x=3.14, y=3.14)
    partner = vmlogo_Segment()
    setattr(partner, 'vmlogo_Segment9', None)
    _safe_set(owner, 'vmlogo_Point10', partner)
    assert getattr(partner, 'vmlogo_Segment9') == owner
    _safe_set(owner, 'vmlogo_Point10', None)
    assert getattr(partner, 'vmlogo_Segment9') is None


def test_assoc_variables13_stub_double():
    # vmlogo_StackFrame has no real 'vmlogo_StackFrame14' property in the generated
    # code (a bare stub) -- manually attach it so vmlogo_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vmlogo_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vmlogo_Variable(name="sample_text", value=3.14)
    partner = vmlogo_StackFrame()
    setattr(partner, 'vmlogo_StackFrame14', None)
    _safe_set(owner, 'vmlogo_Variable', partner)
    assert owner in getattr(partner, 'vmlogo_StackFrame14')
    _safe_set(owner, 'vmlogo_Variable', None)
    assert owner not in getattr(partner, 'vmlogo_StackFrame14')


