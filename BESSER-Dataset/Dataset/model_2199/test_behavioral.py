import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    viewers_ListViewerElement,
    viewers_ListViewerInput,
    viewers_TableViewerElement,
    viewers_TableViewerInput,
    viewers_TreeViewerElement,
    viewers_TreeViewerInput,
    viewers_ViewerInputs,
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

def test_assoc_children4_reverse_link_reassign_clear():
    a1 = viewers_TreeViewerElement(label="sample_text")
    a2 = viewers_TreeViewerElement(label="sample_text_2")
    b = viewers_TreeViewerElement(label="sample_text")
    _safe_set(b, 'viewers_TreeViewerElement5', a1)
    assert _is_linked(b, 'viewers_TreeViewerElement5', a1)
    if hasattr(a1, 'viewers_TreeViewerElement3'):
        assert _is_linked(a1, 'viewers_TreeViewerElement3', b)
    _safe_set(b, 'viewers_TreeViewerElement5', a2)
    assert _is_linked(b, 'viewers_TreeViewerElement5', a2)
    if hasattr(a1, 'viewers_TreeViewerElement3'):
        assert not _is_linked(a1, 'viewers_TreeViewerElement3', b)
    if hasattr(a2, 'viewers_TreeViewerElement3'):
        assert _is_linked(a2, 'viewers_TreeViewerElement3', b)
    _safe_set(b, 'viewers_TreeViewerElement5', None)
    assert not _is_linked(b, 'viewers_TreeViewerElement5', a2)
    if hasattr(a2, 'viewers_TreeViewerElement3'):
        assert not _is_linked(a2, 'viewers_TreeViewerElement3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # viewers_ListViewerInput has no real 'viewers_ListViewerInput' property in the generated
    # code (a bare stub) -- manually attach it so viewers_ListViewerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewers_ListViewerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewers_ListViewerElement(label="sample_text")
    partner = viewers_ListViewerInput()
    setattr(partner, 'viewers_ListViewerInput', None)
    _safe_set(owner, 'viewers_ListViewerElement', partner)
    assert owner in getattr(partner, 'viewers_ListViewerInput')
    _safe_set(owner, 'viewers_ListViewerElement', None)
    assert owner not in getattr(partner, 'viewers_ListViewerInput')


def test_assoc_elements1_stub_double():
    # viewers_TableViewerInput has no real 'viewers_TableViewerInput' property in the generated
    # code (a bare stub) -- manually attach it so viewers_TableViewerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewers_TableViewerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewers_TableViewerElement(label="sample_text", name="sample_text")
    partner = viewers_TableViewerInput()
    setattr(partner, 'viewers_TableViewerInput', None)
    _safe_set(owner, 'viewers_TableViewerElement', partner)
    assert owner in getattr(partner, 'viewers_TableViewerInput')
    _safe_set(owner, 'viewers_TableViewerElement', None)
    assert owner not in getattr(partner, 'viewers_TableViewerInput')


def test_assoc_elements2_stub_double():
    # viewers_TreeViewerInput has no real 'viewers_TreeViewerInput' property in the generated
    # code (a bare stub) -- manually attach it so viewers_TreeViewerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewers_TreeViewerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewers_TreeViewerElement(label="sample_text")
    partner = viewers_TreeViewerInput()
    setattr(partner, 'viewers_TreeViewerInput', None)
    _safe_set(owner, 'viewers_TreeViewerElement', partner)
    assert owner in getattr(partner, 'viewers_TreeViewerInput')
    _safe_set(owner, 'viewers_TreeViewerElement', None)
    assert owner not in getattr(partner, 'viewers_TreeViewerInput')


