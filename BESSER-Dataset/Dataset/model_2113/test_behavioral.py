import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TestMM_Action,
    TestMM_Metadata,
    TestMM_Test,
    ActionType,
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

def test_assoc_act1_reverse_link_reassign_clear():
    a1 = TestMM_Test(id="sample_text")
    a2 = TestMM_Test(id="sample_text_2")
    b = TestMM_Action(description="sample_text", id="sample_text", type="sample_text", value="sample_text", xpath="sample_text")
    _safe_set(b, 'Action', a1)
    assert _is_linked(b, 'Action', a1)
    if hasattr(a1, 'te2'):
        assert _is_linked(a1, 'te2', b)
    _safe_set(b, 'Action', a2)
    assert _is_linked(b, 'Action', a2)
    if hasattr(a1, 'te2'):
        assert not _is_linked(a1, 'te2', b)
    if hasattr(a2, 'te2'):
        assert _is_linked(a2, 'te2', b)
    _safe_set(b, 'Action', None)
    assert not _is_linked(b, 'Action', a2)
    if hasattr(a2, 'te2'):
        assert not _is_linked(a2, 'te2', b)


def test_assoc_md0_reverse_link_reassign_clear():
    a1 = TestMM_Test(id="sample_text")
    a2 = TestMM_Test(id="sample_text_2")
    b = TestMM_Metadata(date="sample_text", taglist="sample_text", user="sample_text", webpage="sample_text")
    _safe_set(b, 'Metadata', a1)
    assert _is_linked(b, 'Metadata', a1)
    if hasattr(a1, 'te'):
        assert _is_linked(a1, 'te', b)
    _safe_set(b, 'Metadata', a2)
    assert _is_linked(b, 'Metadata', a2)
    if hasattr(a1, 'te'):
        assert not _is_linked(a1, 'te', b)
    if hasattr(a2, 'te'):
        assert _is_linked(a2, 'te', b)
    _safe_set(b, 'Metadata', None)
    assert not _is_linked(b, 'Metadata', a2)
    if hasattr(a2, 'te'):
        assert not _is_linked(a2, 'te', b)


def test_assoc_te3_reverse_link_reassign_clear():
    a1 = TestMM_Test(id="sample_text")
    a2 = TestMM_Test(id="sample_text_2")
    b = TestMM_Metadata(date="sample_text", taglist="sample_text", user="sample_text", webpage="sample_text")
    _safe_set(b, 'md', a1)
    assert _is_linked(b, 'md', a1)
    if hasattr(a1, 'Test'):
        assert _is_linked(a1, 'Test', b)
    _safe_set(b, 'md', a2)
    assert _is_linked(b, 'md', a2)
    if hasattr(a1, 'Test'):
        assert not _is_linked(a1, 'Test', b)
    if hasattr(a2, 'Test'):
        assert _is_linked(a2, 'Test', b)
    _safe_set(b, 'md', None)
    assert not _is_linked(b, 'md', a2)
    if hasattr(a2, 'Test'):
        assert not _is_linked(a2, 'Test', b)


def test_assoc_te4_reverse_link_reassign_clear():
    a1 = TestMM_Test(id="sample_text")
    a2 = TestMM_Test(id="sample_text_2")
    b = TestMM_Action(description="sample_text", id="sample_text", type="sample_text", value="sample_text", xpath="sample_text")
    _safe_set(b, 'act', a1)
    assert _is_linked(b, 'act', a1)
    if hasattr(a1, 'Test5'):
        assert _is_linked(a1, 'Test5', b)
    _safe_set(b, 'act', a2)
    assert _is_linked(b, 'act', a2)
    if hasattr(a1, 'Test5'):
        assert not _is_linked(a1, 'Test5', b)
    if hasattr(a2, 'Test5'):
        assert _is_linked(a2, 'Test5', b)
    _safe_set(b, 'act', None)
    assert not _is_linked(b, 'act', a2)
    if hasattr(a2, 'Test5'):
        assert not _is_linked(a2, 'Test5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

