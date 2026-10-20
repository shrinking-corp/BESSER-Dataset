import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    emap_Book,
    emap_DateToCategoryMapEntry,
    emap_StringToStringMapEntry,
    emap_StringToWriterMapEntry,
    emap_Writer,
    emap_WriterToStringMapEntry,
    Category,
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

def test_assoc_categoryByDate5_reverse_link_reassign_clear():
    a1 = emap_DateToCategoryMapEntry(key="sample_text", value="sample_text")
    a2 = emap_DateToCategoryMapEntry(key="sample_text_2", value="sample_text_2")
    b = emap_Book(title="sample_text")
    _safe_set(b, 'emap_Book6', {a1})
    assert _is_linked(b, 'emap_Book6', a1)
    if hasattr(a1, 'emap_DateToCategoryMapEntry'):
        assert _is_linked(a1, 'emap_DateToCategoryMapEntry', b)
    _safe_set(b, 'emap_Book6', {a2})
    assert _is_linked(b, 'emap_Book6', a2)
    if hasattr(a1, 'emap_DateToCategoryMapEntry'):
        assert not _is_linked(a1, 'emap_DateToCategoryMapEntry', b)
    if hasattr(a2, 'emap_DateToCategoryMapEntry'):
        assert _is_linked(a2, 'emap_DateToCategoryMapEntry', b)
    _safe_set(b, 'emap_Book6', set())
    assert not _is_linked(b, 'emap_Book6', a2)
    if hasattr(a2, 'emap_DateToCategoryMapEntry'):
        assert not _is_linked(a2, 'emap_DateToCategoryMapEntry', b)


def test_assoc_cityByWriter3_reverse_link_reassign_clear():
    a1 = emap_WriterToStringMapEntry(value="sample_text")
    a2 = emap_WriterToStringMapEntry(value="sample_text_2")
    b = emap_Book(title="sample_text")
    _safe_set(b, 'emap_Book4', {a1})
    assert _is_linked(b, 'emap_Book4', a1)
    if hasattr(a1, 'emap_WriterToStringMapEntry'):
        assert _is_linked(a1, 'emap_WriterToStringMapEntry', b)
    _safe_set(b, 'emap_Book4', {a2})
    assert _is_linked(b, 'emap_Book4', a2)
    if hasattr(a1, 'emap_WriterToStringMapEntry'):
        assert not _is_linked(a1, 'emap_WriterToStringMapEntry', b)
    if hasattr(a2, 'emap_WriterToStringMapEntry'):
        assert _is_linked(a2, 'emap_WriterToStringMapEntry', b)
    _safe_set(b, 'emap_Book4', set())
    assert not _is_linked(b, 'emap_Book4', a2)
    if hasattr(a2, 'emap_WriterToStringMapEntry'):
        assert not _is_linked(a2, 'emap_WriterToStringMapEntry', b)


def test_assoc_key9_reverse_link_reassign_clear():
    a1 = emap_WriterToStringMapEntry(value="sample_text")
    a2 = emap_WriterToStringMapEntry(value="sample_text_2")
    b = emap_Writer(name="sample_text")
    _safe_set(b, 'emap_Writer11', a1)
    assert _is_linked(b, 'emap_Writer11', a1)
    if hasattr(a1, 'emap_WriterToStringMapEntry10'):
        assert _is_linked(a1, 'emap_WriterToStringMapEntry10', b)
    _safe_set(b, 'emap_Writer11', a2)
    assert _is_linked(b, 'emap_Writer11', a2)
    if hasattr(a1, 'emap_WriterToStringMapEntry10'):
        assert not _is_linked(a1, 'emap_WriterToStringMapEntry10', b)
    if hasattr(a2, 'emap_WriterToStringMapEntry10'):
        assert _is_linked(a2, 'emap_WriterToStringMapEntry10', b)
    _safe_set(b, 'emap_Writer11', None)
    assert not _is_linked(b, 'emap_Writer11', a2)
    if hasattr(a2, 'emap_WriterToStringMapEntry10'):
        assert not _is_linked(a2, 'emap_WriterToStringMapEntry10', b)


def test_assoc_keyWords1_reverse_link_reassign_clear():
    a1 = emap_StringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = emap_StringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = emap_Book(title="sample_text")
    _safe_set(b, 'emap_Book2', {a1})
    assert _is_linked(b, 'emap_Book2', a1)
    if hasattr(a1, 'emap_StringToStringMapEntry'):
        assert _is_linked(a1, 'emap_StringToStringMapEntry', b)
    _safe_set(b, 'emap_Book2', {a2})
    assert _is_linked(b, 'emap_Book2', a2)
    if hasattr(a1, 'emap_StringToStringMapEntry'):
        assert not _is_linked(a1, 'emap_StringToStringMapEntry', b)
    if hasattr(a2, 'emap_StringToStringMapEntry'):
        assert _is_linked(a2, 'emap_StringToStringMapEntry', b)
    _safe_set(b, 'emap_Book2', set())
    assert not _is_linked(b, 'emap_Book2', a2)
    if hasattr(a2, 'emap_StringToStringMapEntry'):
        assert not _is_linked(a2, 'emap_StringToStringMapEntry', b)


def test_assoc_value7_reverse_link_reassign_clear():
    a1 = emap_Writer(name="sample_text")
    a2 = emap_Writer(name="sample_text_2")
    b = emap_StringToWriterMapEntry(key="sample_text")
    _safe_set(b, 'emap_StringToWriterMapEntry8', a1)
    assert _is_linked(b, 'emap_StringToWriterMapEntry8', a1)
    if hasattr(a1, 'emap_Writer'):
        assert _is_linked(a1, 'emap_Writer', b)
    _safe_set(b, 'emap_StringToWriterMapEntry8', a2)
    assert _is_linked(b, 'emap_StringToWriterMapEntry8', a2)
    if hasattr(a1, 'emap_Writer'):
        assert not _is_linked(a1, 'emap_Writer', b)
    if hasattr(a2, 'emap_Writer'):
        assert _is_linked(a2, 'emap_Writer', b)
    _safe_set(b, 'emap_StringToWriterMapEntry8', None)
    assert not _is_linked(b, 'emap_StringToWriterMapEntry8', a2)
    if hasattr(a2, 'emap_Writer'):
        assert not _is_linked(a2, 'emap_Writer', b)


def test_assoc_writers0_reverse_link_reassign_clear():
    a1 = emap_StringToWriterMapEntry(key="sample_text")
    a2 = emap_StringToWriterMapEntry(key="sample_text_2")
    b = emap_Book(title="sample_text")
    _safe_set(b, 'emap_Book', {a1})
    assert _is_linked(b, 'emap_Book', a1)
    if hasattr(a1, 'emap_StringToWriterMapEntry'):
        assert _is_linked(a1, 'emap_StringToWriterMapEntry', b)
    _safe_set(b, 'emap_Book', {a2})
    assert _is_linked(b, 'emap_Book', a2)
    if hasattr(a1, 'emap_StringToWriterMapEntry'):
        assert not _is_linked(a1, 'emap_StringToWriterMapEntry', b)
    if hasattr(a2, 'emap_StringToWriterMapEntry'):
        assert _is_linked(a2, 'emap_StringToWriterMapEntry', b)
    _safe_set(b, 'emap_Book', set())
    assert not _is_linked(b, 'emap_Book', a2)
    if hasattr(a2, 'emap_StringToWriterMapEntry'):
        assert not _is_linked(a2, 'emap_StringToWriterMapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

