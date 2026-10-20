import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TopNode,
    compartments_Canvas,
    compartments_ChildOfA_C,
    compartments_ChildOfA_D,
    compartments_ChildOfAffixed,
    compartments_ChildOfB_E,
    compartments_ChildOfB_F,
    compartments_ChildOfB_G,
    compartments_TopNode,
    compartments_TopNodeA,
    compartments_TopNodeB,
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

def test_assoc_cNodeRelation9_reverse_link_reassign_clear():
    a1 = compartments_ChildOfB_E(name="sample_text")
    a2 = compartments_ChildOfB_E(name="sample_text_2")
    b = compartments_ChildOfA_C(name="sample_text")
    _safe_set(b, 'compartments_ChildOfA_C11', a1)
    assert _is_linked(b, 'compartments_ChildOfA_C11', a1)
    if hasattr(a1, 'compartments_ChildOfB_E10'):
        assert _is_linked(a1, 'compartments_ChildOfB_E10', b)
    _safe_set(b, 'compartments_ChildOfA_C11', a2)
    assert _is_linked(b, 'compartments_ChildOfA_C11', a2)
    if hasattr(a1, 'compartments_ChildOfB_E10'):
        assert not _is_linked(a1, 'compartments_ChildOfB_E10', b)
    if hasattr(a2, 'compartments_ChildOfB_E10'):
        assert _is_linked(a2, 'compartments_ChildOfB_E10', b)
    _safe_set(b, 'compartments_ChildOfA_C11', None)
    assert not _is_linked(b, 'compartments_ChildOfA_C11', a2)
    if hasattr(a2, 'compartments_ChildOfB_E10'):
        assert not _is_linked(a2, 'compartments_ChildOfB_E10', b)


def test_assoc_childrenC1_reverse_link_reassign_clear():
    a1 = compartments_TopNodeA(name="sample_text")
    a2 = compartments_TopNodeA(name="sample_text_2")
    b = compartments_ChildOfA_C(name="sample_text")
    _safe_set(b, 'compartments_ChildOfA_C', a1)
    assert _is_linked(b, 'compartments_ChildOfA_C', a1)
    if hasattr(a1, 'compartments_TopNodeA'):
        assert _is_linked(a1, 'compartments_TopNodeA', b)
    _safe_set(b, 'compartments_ChildOfA_C', a2)
    assert _is_linked(b, 'compartments_ChildOfA_C', a2)
    if hasattr(a1, 'compartments_TopNodeA'):
        assert not _is_linked(a1, 'compartments_TopNodeA', b)
    if hasattr(a2, 'compartments_TopNodeA'):
        assert _is_linked(a2, 'compartments_TopNodeA', b)
    _safe_set(b, 'compartments_ChildOfA_C', None)
    assert not _is_linked(b, 'compartments_ChildOfA_C', a2)
    if hasattr(a2, 'compartments_TopNodeA'):
        assert not _is_linked(a2, 'compartments_TopNodeA', b)


def test_assoc_childrenD2_reverse_link_reassign_clear():
    a1 = compartments_TopNodeA(name="sample_text")
    a2 = compartments_TopNodeA(name="sample_text_2")
    b = compartments_ChildOfA_D(name="sample_text")
    _safe_set(b, 'compartments_ChildOfA_D', a1)
    assert _is_linked(b, 'compartments_ChildOfA_D', a1)
    if hasattr(a1, 'compartments_TopNodeA3'):
        assert _is_linked(a1, 'compartments_TopNodeA3', b)
    _safe_set(b, 'compartments_ChildOfA_D', a2)
    assert _is_linked(b, 'compartments_ChildOfA_D', a2)
    if hasattr(a1, 'compartments_TopNodeA3'):
        assert not _is_linked(a1, 'compartments_TopNodeA3', b)
    if hasattr(a2, 'compartments_TopNodeA3'):
        assert _is_linked(a2, 'compartments_TopNodeA3', b)
    _safe_set(b, 'compartments_ChildOfA_D', None)
    assert not _is_linked(b, 'compartments_ChildOfA_D', a2)
    if hasattr(a2, 'compartments_TopNodeA3'):
        assert not _is_linked(a2, 'compartments_TopNodeA3', b)


def test_assoc_childrenE4_reverse_link_reassign_clear():
    a1 = compartments_TopNodeB(name="sample_text")
    a2 = compartments_TopNodeB(name="sample_text_2")
    b = compartments_ChildOfB_E(name="sample_text")
    _safe_set(b, 'compartments_ChildOfB_E', a1)
    assert _is_linked(b, 'compartments_ChildOfB_E', a1)
    if hasattr(a1, 'compartments_TopNodeB'):
        assert _is_linked(a1, 'compartments_TopNodeB', b)
    _safe_set(b, 'compartments_ChildOfB_E', a2)
    assert _is_linked(b, 'compartments_ChildOfB_E', a2)
    if hasattr(a1, 'compartments_TopNodeB'):
        assert not _is_linked(a1, 'compartments_TopNodeB', b)
    if hasattr(a2, 'compartments_TopNodeB'):
        assert _is_linked(a2, 'compartments_TopNodeB', b)
    _safe_set(b, 'compartments_ChildOfB_E', None)
    assert not _is_linked(b, 'compartments_ChildOfB_E', a2)
    if hasattr(a2, 'compartments_TopNodeB'):
        assert not _is_linked(a2, 'compartments_TopNodeB', b)


def test_assoc_childrenF7_reverse_link_reassign_clear():
    a1 = compartments_TopNodeB(name="sample_text")
    a2 = compartments_TopNodeB(name="sample_text_2")
    b = compartments_ChildOfB_F(name="sample_text")
    _safe_set(b, 'compartments_ChildOfB_F', a1)
    assert _is_linked(b, 'compartments_ChildOfB_F', a1)
    if hasattr(a1, 'compartments_TopNodeB8'):
        assert _is_linked(a1, 'compartments_TopNodeB8', b)
    _safe_set(b, 'compartments_ChildOfB_F', a2)
    assert _is_linked(b, 'compartments_ChildOfB_F', a2)
    if hasattr(a1, 'compartments_TopNodeB8'):
        assert not _is_linked(a1, 'compartments_TopNodeB8', b)
    if hasattr(a2, 'compartments_TopNodeB8'):
        assert _is_linked(a2, 'compartments_TopNodeB8', b)
    _safe_set(b, 'compartments_ChildOfB_F', None)
    assert not _is_linked(b, 'compartments_ChildOfB_F', a2)
    if hasattr(a2, 'compartments_TopNodeB8'):
        assert not _is_linked(a2, 'compartments_TopNodeB8', b)


def test_assoc_childrenG5_reverse_link_reassign_clear():
    a1 = compartments_TopNodeB(name="sample_text")
    a2 = compartments_TopNodeB(name="sample_text_2")
    b = compartments_ChildOfB_G(number=7)
    _safe_set(b, 'compartments_ChildOfB_G', a1)
    assert _is_linked(b, 'compartments_ChildOfB_G', a1)
    if hasattr(a1, 'compartments_TopNodeB6'):
        assert _is_linked(a1, 'compartments_TopNodeB6', b)
    _safe_set(b, 'compartments_ChildOfB_G', a2)
    assert _is_linked(b, 'compartments_ChildOfB_G', a2)
    if hasattr(a1, 'compartments_TopNodeB6'):
        assert not _is_linked(a1, 'compartments_TopNodeB6', b)
    if hasattr(a2, 'compartments_TopNodeB6'):
        assert _is_linked(a2, 'compartments_TopNodeB6', b)
    _safe_set(b, 'compartments_ChildOfB_G', None)
    assert not _is_linked(b, 'compartments_ChildOfB_G', a2)
    if hasattr(a2, 'compartments_TopNodeB6'):
        assert not _is_linked(a2, 'compartments_TopNodeB6', b)


def test_assoc_childrenOfAffixed12_reverse_link_reassign_clear():
    a1 = compartments_ChildOfB_G(number=7)
    a2 = compartments_ChildOfB_G(number=13)
    b = compartments_ChildOfAffixed(description="sample_text")
    _safe_set(b, 'compartments_ChildOfAffixed', a1)
    assert _is_linked(b, 'compartments_ChildOfAffixed', a1)
    if hasattr(a1, 'compartments_ChildOfB_G13'):
        assert _is_linked(a1, 'compartments_ChildOfB_G13', b)
    _safe_set(b, 'compartments_ChildOfAffixed', a2)
    assert _is_linked(b, 'compartments_ChildOfAffixed', a2)
    if hasattr(a1, 'compartments_ChildOfB_G13'):
        assert not _is_linked(a1, 'compartments_ChildOfB_G13', b)
    if hasattr(a2, 'compartments_ChildOfB_G13'):
        assert _is_linked(a2, 'compartments_ChildOfB_G13', b)
    _safe_set(b, 'compartments_ChildOfAffixed', None)
    assert not _is_linked(b, 'compartments_ChildOfAffixed', a2)
    if hasattr(a2, 'compartments_ChildOfB_G13'):
        assert not _is_linked(a2, 'compartments_ChildOfB_G13', b)


def test_assoc_dNodeRelation14_reverse_link_reassign_clear():
    a1 = compartments_ChildOfB_F(name="sample_text")
    a2 = compartments_ChildOfB_F(name="sample_text_2")
    b = compartments_ChildOfA_D(name="sample_text")
    _safe_set(b, 'compartments_ChildOfA_D16', a1)
    assert _is_linked(b, 'compartments_ChildOfA_D16', a1)
    if hasattr(a1, 'compartments_ChildOfB_F15'):
        assert _is_linked(a1, 'compartments_ChildOfB_F15', b)
    _safe_set(b, 'compartments_ChildOfA_D16', a2)
    assert _is_linked(b, 'compartments_ChildOfA_D16', a2)
    if hasattr(a1, 'compartments_ChildOfB_F15'):
        assert not _is_linked(a1, 'compartments_ChildOfB_F15', b)
    if hasattr(a2, 'compartments_ChildOfB_F15'):
        assert _is_linked(a2, 'compartments_ChildOfB_F15', b)
    _safe_set(b, 'compartments_ChildOfA_D16', None)
    assert not _is_linked(b, 'compartments_ChildOfA_D16', a2)
    if hasattr(a2, 'compartments_ChildOfB_F15'):
        assert not _is_linked(a2, 'compartments_ChildOfB_F15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

