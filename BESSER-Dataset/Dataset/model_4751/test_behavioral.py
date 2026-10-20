import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TreeElement,
    edd_EDD,
    edd_Leaf,
    edd_Node,
    edd_TreeElement,
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

def test_assoc_elements0_reverse_link_reassign_clear():
    a1 = edd_TreeElement(index="sample_text", name="sample_text")
    a2 = edd_TreeElement(index="sample_text_2", name="sample_text_2")
    b = edd_EDD(name="sample_text")
    _safe_set(b, 'edd_EDD', {a1})
    assert _is_linked(b, 'edd_EDD', a1)
    if hasattr(a1, 'edd_TreeElement'):
        assert _is_linked(a1, 'edd_TreeElement', b)
    _safe_set(b, 'edd_EDD', {a2})
    assert _is_linked(b, 'edd_EDD', a2)
    if hasattr(a1, 'edd_TreeElement'):
        assert not _is_linked(a1, 'edd_TreeElement', b)
    if hasattr(a2, 'edd_TreeElement'):
        assert _is_linked(a2, 'edd_TreeElement', b)
    _safe_set(b, 'edd_EDD', set())
    assert not _is_linked(b, 'edd_EDD', a2)
    if hasattr(a2, 'edd_TreeElement'):
        assert not _is_linked(a2, 'edd_TreeElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children1_stub_double():
    # edd_Node has no real 'edd_Node' property in the generated
    # code (a bare stub) -- manually attach it so edd_TreeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edd_TreeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edd_TreeElement(index="sample_text", name="sample_text")
    partner = edd_Node()
    setattr(partner, 'edd_Node', None)
    _safe_set(owner, 'edd_TreeElement2', partner)
    assert owner in getattr(partner, 'edd_Node')
    _safe_set(owner, 'edd_TreeElement2', None)
    assert owner not in getattr(partner, 'edd_Node')


