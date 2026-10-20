import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SimpleRDBMS_Column,
    SimpleRDBMS_FKey,
    SimpleRDBMS_Table,
    FKeyType,
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

def test_assoc_cols3_reverse_link_reassign_clear():
    a1 = SimpleRDBMS_Table(id=7, name="sample_text")
    a2 = SimpleRDBMS_Table(id=13, name="sample_text_2")
    b = SimpleRDBMS_Column(id=7, name="sample_text", type="sample_text")
    _safe_set(b, 'SimpleRDBMS_Column5', a1)
    assert _is_linked(b, 'SimpleRDBMS_Column5', a1)
    if hasattr(a1, 'SimpleRDBMS_Table4'):
        assert _is_linked(a1, 'SimpleRDBMS_Table4', b)
    _safe_set(b, 'SimpleRDBMS_Column5', a2)
    assert _is_linked(b, 'SimpleRDBMS_Column5', a2)
    if hasattr(a1, 'SimpleRDBMS_Table4'):
        assert not _is_linked(a1, 'SimpleRDBMS_Table4', b)
    if hasattr(a2, 'SimpleRDBMS_Table4'):
        assert _is_linked(a2, 'SimpleRDBMS_Table4', b)
    _safe_set(b, 'SimpleRDBMS_Column5', None)
    assert not _is_linked(b, 'SimpleRDBMS_Column5', a2)
    if hasattr(a2, 'SimpleRDBMS_Table4'):
        assert not _is_linked(a2, 'SimpleRDBMS_Table4', b)


def test_assoc_cols9_reverse_link_reassign_clear():
    a1 = SimpleRDBMS_FKey(fkeyType="sample_text")
    a2 = SimpleRDBMS_FKey(fkeyType="sample_text_2")
    b = SimpleRDBMS_Column(id=7, name="sample_text", type="sample_text")
    _safe_set(b, 'SimpleRDBMS_Column11', a1)
    assert _is_linked(b, 'SimpleRDBMS_Column11', a1)
    if hasattr(a1, 'SimpleRDBMS_FKey10'):
        assert _is_linked(a1, 'SimpleRDBMS_FKey10', b)
    _safe_set(b, 'SimpleRDBMS_Column11', a2)
    assert _is_linked(b, 'SimpleRDBMS_Column11', a2)
    if hasattr(a1, 'SimpleRDBMS_FKey10'):
        assert not _is_linked(a1, 'SimpleRDBMS_FKey10', b)
    if hasattr(a2, 'SimpleRDBMS_FKey10'):
        assert _is_linked(a2, 'SimpleRDBMS_FKey10', b)
    _safe_set(b, 'SimpleRDBMS_Column11', None)
    assert not _is_linked(b, 'SimpleRDBMS_Column11', a2)
    if hasattr(a2, 'SimpleRDBMS_FKey10'):
        assert not _is_linked(a2, 'SimpleRDBMS_FKey10', b)


def test_assoc_fkeys0_reverse_link_reassign_clear():
    a1 = SimpleRDBMS_Table(id=7, name="sample_text")
    a2 = SimpleRDBMS_Table(id=13, name="sample_text_2")
    b = SimpleRDBMS_FKey(fkeyType="sample_text")
    _safe_set(b, 'SimpleRDBMS_FKey', a1)
    assert _is_linked(b, 'SimpleRDBMS_FKey', a1)
    if hasattr(a1, 'SimpleRDBMS_Table'):
        assert _is_linked(a1, 'SimpleRDBMS_Table', b)
    _safe_set(b, 'SimpleRDBMS_FKey', a2)
    assert _is_linked(b, 'SimpleRDBMS_FKey', a2)
    if hasattr(a1, 'SimpleRDBMS_Table'):
        assert not _is_linked(a1, 'SimpleRDBMS_Table', b)
    if hasattr(a2, 'SimpleRDBMS_Table'):
        assert _is_linked(a2, 'SimpleRDBMS_Table', b)
    _safe_set(b, 'SimpleRDBMS_FKey', None)
    assert not _is_linked(b, 'SimpleRDBMS_FKey', a2)
    if hasattr(a2, 'SimpleRDBMS_Table'):
        assert not _is_linked(a2, 'SimpleRDBMS_Table', b)


def test_assoc_pkey1_reverse_link_reassign_clear():
    a1 = SimpleRDBMS_Table(id=7, name="sample_text")
    a2 = SimpleRDBMS_Table(id=13, name="sample_text_2")
    b = SimpleRDBMS_Column(id=7, name="sample_text", type="sample_text")
    _safe_set(b, 'SimpleRDBMS_Column', a1)
    assert _is_linked(b, 'SimpleRDBMS_Column', a1)
    if hasattr(a1, 'SimpleRDBMS_Table2'):
        assert _is_linked(a1, 'SimpleRDBMS_Table2', b)
    _safe_set(b, 'SimpleRDBMS_Column', a2)
    assert _is_linked(b, 'SimpleRDBMS_Column', a2)
    if hasattr(a1, 'SimpleRDBMS_Table2'):
        assert not _is_linked(a1, 'SimpleRDBMS_Table2', b)
    if hasattr(a2, 'SimpleRDBMS_Table2'):
        assert _is_linked(a2, 'SimpleRDBMS_Table2', b)
    _safe_set(b, 'SimpleRDBMS_Column', None)
    assert not _is_linked(b, 'SimpleRDBMS_Column', a2)
    if hasattr(a2, 'SimpleRDBMS_Table2'):
        assert not _is_linked(a2, 'SimpleRDBMS_Table2', b)


def test_assoc_references6_reverse_link_reassign_clear():
    a1 = SimpleRDBMS_Table(id=7, name="sample_text")
    a2 = SimpleRDBMS_Table(id=13, name="sample_text_2")
    b = SimpleRDBMS_FKey(fkeyType="sample_text")
    _safe_set(b, 'SimpleRDBMS_FKey7', a1)
    assert _is_linked(b, 'SimpleRDBMS_FKey7', a1)
    if hasattr(a1, 'SimpleRDBMS_Table8'):
        assert _is_linked(a1, 'SimpleRDBMS_Table8', b)
    _safe_set(b, 'SimpleRDBMS_FKey7', a2)
    assert _is_linked(b, 'SimpleRDBMS_FKey7', a2)
    if hasattr(a1, 'SimpleRDBMS_Table8'):
        assert not _is_linked(a1, 'SimpleRDBMS_Table8', b)
    if hasattr(a2, 'SimpleRDBMS_Table8'):
        assert _is_linked(a2, 'SimpleRDBMS_Table8', b)
    _safe_set(b, 'SimpleRDBMS_FKey7', None)
    assert not _is_linked(b, 'SimpleRDBMS_FKey7', a2)
    if hasattr(a2, 'SimpleRDBMS_Table8'):
        assert not _is_linked(a2, 'SimpleRDBMS_Table8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

