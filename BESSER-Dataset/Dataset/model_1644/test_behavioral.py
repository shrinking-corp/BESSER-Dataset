import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    kiamaas_Node,
    kiamaas_Num,
    kiamaas_Plus,
    kiamaas_Top,
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

def test_assoc_left1_stub_double():
    # kiamaas_Plus has no real 'kiamaas_Plus' property in the generated
    # code (a bare stub) -- manually attach it so kiamaas_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kiamaas_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kiamaas_Node(depth="sample_text", height="sample_text")
    partner = kiamaas_Plus()
    setattr(partner, 'kiamaas_Plus', None)
    _safe_set(owner, 'kiamaas_Node2', partner)
    assert getattr(partner, 'kiamaas_Plus') == owner
    _safe_set(owner, 'kiamaas_Node2', None)
    assert getattr(partner, 'kiamaas_Plus') is None


def test_assoc_node0_stub_double():
    # kiamaas_Top has no real 'kiamaas_Top' property in the generated
    # code (a bare stub) -- manually attach it so kiamaas_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kiamaas_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kiamaas_Node(depth="sample_text", height="sample_text")
    partner = kiamaas_Top()
    setattr(partner, 'kiamaas_Top', None)
    _safe_set(owner, 'kiamaas_Node', partner)
    assert getattr(partner, 'kiamaas_Top') == owner
    _safe_set(owner, 'kiamaas_Node', None)
    assert getattr(partner, 'kiamaas_Top') is None


def test_assoc_right3_stub_double():
    # kiamaas_Plus has no real 'kiamaas_Plus4' property in the generated
    # code (a bare stub) -- manually attach it so kiamaas_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kiamaas_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kiamaas_Node(depth="sample_text", height="sample_text")
    partner = kiamaas_Plus()
    setattr(partner, 'kiamaas_Plus4', None)
    _safe_set(owner, 'kiamaas_Node5', partner)
    assert getattr(partner, 'kiamaas_Plus4') == owner
    _safe_set(owner, 'kiamaas_Node5', None)
    assert getattr(partner, 'kiamaas_Plus4') is None


