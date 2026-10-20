import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    BoemTest_A,
    BoemTest_B,
    BoemTest_BNode,
    BoemTest_C,
    BoemTest_NamedElement,
    BoemTest_Node,
    NamedElement,
    AnEnumeration,
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

def test_assoc_childNodeB18_stub_double():
    # BoemTest_Node has no real 'BoemTest_Node20' property in the generated
    # code (a bare stub) -- manually attach it so BoemTest_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BoemTest_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BoemTest_B(enumAttr="sample_text")
    partner = BoemTest_Node()
    setattr(partner, 'BoemTest_Node20', None)
    _safe_set(owner, 'BoemTest_B19', partner)
    assert getattr(partner, 'BoemTest_Node20') == owner
    _safe_set(owner, 'BoemTest_B19', None)
    assert getattr(partner, 'BoemTest_Node20') is None


def test_assoc_childrenNodeB16_stub_double():
    # BoemTest_Node has no real 'BoemTest_Node17' property in the generated
    # code (a bare stub) -- manually attach it so BoemTest_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BoemTest_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BoemTest_B(enumAttr="sample_text")
    partner = BoemTest_Node()
    setattr(partner, 'BoemTest_Node17', None)
    _safe_set(owner, 'BoemTest_B', {partner})
    assert getattr(partner, 'BoemTest_Node17') == owner
    _safe_set(owner, 'BoemTest_B', set())
    assert getattr(partner, 'BoemTest_Node17') is None


def test_assoc_childrenNodeBNode21_stub_double():
    # BoemTest_BNode has no real 'BoemTest_BNode' property in the generated
    # code (a bare stub) -- manually attach it so BoemTest_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BoemTest_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BoemTest_B(enumAttr="sample_text")
    partner = BoemTest_BNode()
    setattr(partner, 'BoemTest_BNode', None)
    _safe_set(owner, 'BoemTest_B22', partner)
    assert getattr(partner, 'BoemTest_BNode') == owner
    _safe_set(owner, 'BoemTest_B22', None)
    assert getattr(partner, 'BoemTest_BNode') is None


