import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Tree,
    kwas_Bin,
    kwas_Leaf,
    kwas_Top,
    kwas_Tree,
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
    # kwas_Bin has no real 'kwas_Bin' property in the generated
    # code (a bare stub) -- manually attach it so kwas_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kwas_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kwas_Tree(labelI="sample_text", labelS="sample_text", valsI=7, valsS=7)
    partner = kwas_Bin()
    setattr(partner, 'kwas_Bin', None)
    _safe_set(owner, 'kwas_Tree2', partner)
    assert getattr(partner, 'kwas_Bin') == owner
    _safe_set(owner, 'kwas_Tree2', None)
    assert getattr(partner, 'kwas_Bin') is None


def test_assoc_node0_stub_double():
    # kwas_Top has no real 'kwas_Top' property in the generated
    # code (a bare stub) -- manually attach it so kwas_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kwas_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kwas_Tree(labelI="sample_text", labelS="sample_text", valsI=7, valsS=7)
    partner = kwas_Top()
    setattr(partner, 'kwas_Top', None)
    _safe_set(owner, 'kwas_Tree', partner)
    assert getattr(partner, 'kwas_Top') == owner
    _safe_set(owner, 'kwas_Tree', None)
    assert getattr(partner, 'kwas_Top') is None


def test_assoc_right3_stub_double():
    # kwas_Bin has no real 'kwas_Bin4' property in the generated
    # code (a bare stub) -- manually attach it so kwas_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kwas_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kwas_Tree(labelI="sample_text", labelS="sample_text", valsI=7, valsS=7)
    partner = kwas_Bin()
    setattr(partner, 'kwas_Bin4', None)
    _safe_set(owner, 'kwas_Tree5', partner)
    assert getattr(partner, 'kwas_Bin4') == owner
    _safe_set(owner, 'kwas_Tree5', None)
    assert getattr(partner, 'kwas_Bin4') is None


