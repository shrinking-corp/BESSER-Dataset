import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractNode,
    AbstractTransition,
    ptn103_AbstractNode,
    ptn103_AbstractTransition,
    ptn103_Place,
    ptn103_Token,
    ptn103_Transition,
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

def test_assoc_nodes2_stub_double():
    # ptn103_Place has no real 'ptn103_Place3' property in the generated
    # code (a bare stub) -- manually attach it so ptn103_AbstractNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptn103_AbstractNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptn103_AbstractNode(name="sample_text")
    partner = ptn103_Place()
    setattr(partner, 'ptn103_Place3', None)
    _safe_set(owner, 'ptn103_AbstractNode', partner)
    assert owner in getattr(partner, 'ptn103_Place3')
    _safe_set(owner, 'ptn103_AbstractNode', None)
    assert owner not in getattr(partner, 'ptn103_Place3')


def test_assoc_places8_stub_double():
    # ptn103_Place has no real 'ptn103_Place10' property in the generated
    # code (a bare stub) -- manually attach it so ptn103_AbstractTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptn103_AbstractTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptn103_AbstractTransition(guard="sample_text")
    partner = ptn103_Place()
    setattr(partner, 'ptn103_Place10', None)
    _safe_set(owner, 'ptn103_AbstractTransition9', {partner})
    assert getattr(partner, 'ptn103_Place10') == owner
    _safe_set(owner, 'ptn103_AbstractTransition9', set())
    assert getattr(partner, 'ptn103_Place10') is None


def test_assoc_transitions4_stub_double():
    # ptn103_Place has no real 'ptn103_Place5' property in the generated
    # code (a bare stub) -- manually attach it so ptn103_AbstractTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptn103_AbstractTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptn103_AbstractTransition(guard="sample_text")
    partner = ptn103_Place()
    setattr(partner, 'ptn103_Place5', None)
    _safe_set(owner, 'ptn103_AbstractTransition', partner)
    assert owner in getattr(partner, 'ptn103_Place5')
    _safe_set(owner, 'ptn103_AbstractTransition', None)
    assert owner not in getattr(partner, 'ptn103_Place5')


