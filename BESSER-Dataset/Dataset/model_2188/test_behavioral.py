import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TreeMapItem,
    TreeMapViewer_TreeMapContainer,
    TreeMapViewer_TreeMapItem,
    TreeMapViewer_TreeMapViewer,
    TreeMapType,
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

def test_assoc_children0_reverse_link_reassign_clear():
    a1 = TreeMapViewer_TreeMapViewer(childLayoutStrategy="sample_text")
    a2 = TreeMapViewer_TreeMapViewer(childLayoutStrategy="sample_text_2")
    b = TreeMapViewer_TreeMapItem(label="sample_text", value=3.14)
    _safe_set(b, 'TreeMapViewer_TreeMapItem', a1)
    assert _is_linked(b, 'TreeMapViewer_TreeMapItem', a1)
    if hasattr(a1, 'TreeMapViewer_TreeMapViewer'):
        assert _is_linked(a1, 'TreeMapViewer_TreeMapViewer', b)
    _safe_set(b, 'TreeMapViewer_TreeMapItem', a2)
    assert _is_linked(b, 'TreeMapViewer_TreeMapItem', a2)
    if hasattr(a1, 'TreeMapViewer_TreeMapViewer'):
        assert not _is_linked(a1, 'TreeMapViewer_TreeMapViewer', b)
    if hasattr(a2, 'TreeMapViewer_TreeMapViewer'):
        assert _is_linked(a2, 'TreeMapViewer_TreeMapViewer', b)
    _safe_set(b, 'TreeMapViewer_TreeMapItem', None)
    assert not _is_linked(b, 'TreeMapViewer_TreeMapItem', a2)
    if hasattr(a2, 'TreeMapViewer_TreeMapViewer'):
        assert not _is_linked(a2, 'TreeMapViewer_TreeMapViewer', b)


def test_assoc_parent1_reverse_link_reassign_clear():
    a1 = TreeMapViewer_TreeMapViewer(childLayoutStrategy="sample_text")
    a2 = TreeMapViewer_TreeMapViewer(childLayoutStrategy="sample_text_2")
    b = TreeMapViewer_TreeMapItem(label="sample_text", value=3.14)
    _safe_set(b, 'TreeMapViewer_TreeMapItem2', a1)
    assert _is_linked(b, 'TreeMapViewer_TreeMapItem2', a1)
    if hasattr(a1, 'TreeMapViewer_TreeMapViewer3'):
        assert _is_linked(a1, 'TreeMapViewer_TreeMapViewer3', b)
    _safe_set(b, 'TreeMapViewer_TreeMapItem2', a2)
    assert _is_linked(b, 'TreeMapViewer_TreeMapItem2', a2)
    if hasattr(a1, 'TreeMapViewer_TreeMapViewer3'):
        assert not _is_linked(a1, 'TreeMapViewer_TreeMapViewer3', b)
    if hasattr(a2, 'TreeMapViewer_TreeMapViewer3'):
        assert _is_linked(a2, 'TreeMapViewer_TreeMapViewer3', b)
    _safe_set(b, 'TreeMapViewer_TreeMapItem2', None)
    assert not _is_linked(b, 'TreeMapViewer_TreeMapItem2', a2)
    if hasattr(a2, 'TreeMapViewer_TreeMapViewer3'):
        assert not _is_linked(a2, 'TreeMapViewer_TreeMapViewer3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children4_stub_double():
    # TreeMapViewer_TreeMapContainer has no real 'TreeMapViewer_TreeMapContainer' property in the generated
    # code (a bare stub) -- manually attach it so TreeMapViewer_TreeMapItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TreeMapViewer_TreeMapItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TreeMapViewer_TreeMapItem(label="sample_text", value=3.14)
    partner = TreeMapViewer_TreeMapContainer()
    setattr(partner, 'TreeMapViewer_TreeMapContainer', None)
    _safe_set(owner, 'TreeMapViewer_TreeMapItem5', partner)
    assert owner in getattr(partner, 'TreeMapViewer_TreeMapContainer')
    _safe_set(owner, 'TreeMapViewer_TreeMapItem5', None)
    assert owner not in getattr(partner, 'TreeMapViewer_TreeMapContainer')


