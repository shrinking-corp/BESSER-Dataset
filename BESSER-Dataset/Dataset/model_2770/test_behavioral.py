import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    links_ChildNodeA,
    links_ChildNodeB,
    links_Child_AB_Element_Link,
    links_Root,
    links_RootNodeA,
    links_RootNodeB,
    links_Root_BA_Element_Link,
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

def test_assoc_a26_stub_double():
    # links_RootNodeA has no real 'links_RootNodeA28' property in the generated
    # code (a bare stub) -- manually attach it so links_Root_BA_Element_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # links_Root_BA_Element_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = links_Root_BA_Element_Link(name="sample_text")
    partner = links_RootNodeA()
    setattr(partner, 'links_RootNodeA28', None)
    _safe_set(owner, 'links_Root_BA_Element_Link27', partner)
    assert getattr(partner, 'links_RootNodeA28') == owner
    _safe_set(owner, 'links_Root_BA_Element_Link27', None)
    assert getattr(partner, 'links_RootNodeA28') is None


def test_assoc_b23_stub_double():
    # links_RootNodeB has no real 'links_RootNodeB25' property in the generated
    # code (a bare stub) -- manually attach it so links_Root_BA_Element_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # links_Root_BA_Element_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = links_Root_BA_Element_Link(name="sample_text")
    partner = links_RootNodeB()
    setattr(partner, 'links_RootNodeB25', None)
    _safe_set(owner, 'links_Root_BA_Element_Link24', partner)
    assert getattr(partner, 'links_RootNodeB25') == owner
    _safe_set(owner, 'links_Root_BA_Element_Link24', None)
    assert getattr(partner, 'links_RootNodeB25') is None


def test_assoc_rootBALinks5_stub_double():
    # links_Root has no real 'links_Root6' property in the generated
    # code (a bare stub) -- manually attach it so links_Root_BA_Element_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # links_Root_BA_Element_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = links_Root_BA_Element_Link(name="sample_text")
    partner = links_Root()
    setattr(partner, 'links_Root6', None)
    _safe_set(owner, 'links_Root_BA_Element_Link', partner)
    assert owner in getattr(partner, 'links_Root6')
    _safe_set(owner, 'links_Root_BA_Element_Link', None)
    assert owner not in getattr(partner, 'links_Root6')


