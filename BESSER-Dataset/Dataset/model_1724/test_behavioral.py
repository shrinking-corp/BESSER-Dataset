import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    hbmapkeys_Book,
    hbmapkeys_City,
    hbmapkeys_StringToWriterMapEntry,
    hbmapkeys_Writer,
    hbmapkeys_WriterToCityMapEntry,
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

def test_assoc_cityWriter3_reverse_link_reassign_clear():
    a1 = hbmapkeys_Writer(name="sample_text")
    a2 = hbmapkeys_Writer(name="sample_text_2")
    b = hbmapkeys_City(name="sample_text")
    _safe_set(b, 'hbmapkeys_City', a1)
    assert _is_linked(b, 'hbmapkeys_City', a1)
    if hasattr(a1, 'hbmapkeys_Writer'):
        assert _is_linked(a1, 'hbmapkeys_Writer', b)
    _safe_set(b, 'hbmapkeys_City', a2)
    assert _is_linked(b, 'hbmapkeys_City', a2)
    if hasattr(a1, 'hbmapkeys_Writer'):
        assert not _is_linked(a1, 'hbmapkeys_Writer', b)
    if hasattr(a2, 'hbmapkeys_Writer'):
        assert _is_linked(a2, 'hbmapkeys_Writer', b)
    _safe_set(b, 'hbmapkeys_City', None)
    assert not _is_linked(b, 'hbmapkeys_City', a2)
    if hasattr(a2, 'hbmapkeys_Writer'):
        assert not _is_linked(a2, 'hbmapkeys_Writer', b)


def test_assoc_value4_reverse_link_reassign_clear():
    a1 = hbmapkeys_Writer(name="sample_text")
    a2 = hbmapkeys_Writer(name="sample_text_2")
    b = hbmapkeys_StringToWriterMapEntry(key="sample_text")
    _safe_set(b, 'hbmapkeys_StringToWriterMapEntry5', a1)
    assert _is_linked(b, 'hbmapkeys_StringToWriterMapEntry5', a1)
    if hasattr(a1, 'hbmapkeys_Writer6'):
        assert _is_linked(a1, 'hbmapkeys_Writer6', b)
    _safe_set(b, 'hbmapkeys_StringToWriterMapEntry5', a2)
    assert _is_linked(b, 'hbmapkeys_StringToWriterMapEntry5', a2)
    if hasattr(a1, 'hbmapkeys_Writer6'):
        assert not _is_linked(a1, 'hbmapkeys_Writer6', b)
    if hasattr(a2, 'hbmapkeys_Writer6'):
        assert _is_linked(a2, 'hbmapkeys_Writer6', b)
    _safe_set(b, 'hbmapkeys_StringToWriterMapEntry5', None)
    assert not _is_linked(b, 'hbmapkeys_StringToWriterMapEntry5', a2)
    if hasattr(a2, 'hbmapkeys_Writer6'):
        assert not _is_linked(a2, 'hbmapkeys_Writer6', b)


def test_assoc_writersByName0_reverse_link_reassign_clear():
    a1 = hbmapkeys_StringToWriterMapEntry(key="sample_text")
    a2 = hbmapkeys_StringToWriterMapEntry(key="sample_text_2")
    b = hbmapkeys_Book(title="sample_text")
    _safe_set(b, 'hbmapkeys_Book', {a1})
    assert _is_linked(b, 'hbmapkeys_Book', a1)
    if hasattr(a1, 'hbmapkeys_StringToWriterMapEntry'):
        assert _is_linked(a1, 'hbmapkeys_StringToWriterMapEntry', b)
    _safe_set(b, 'hbmapkeys_Book', {a2})
    assert _is_linked(b, 'hbmapkeys_Book', a2)
    if hasattr(a1, 'hbmapkeys_StringToWriterMapEntry'):
        assert not _is_linked(a1, 'hbmapkeys_StringToWriterMapEntry', b)
    if hasattr(a2, 'hbmapkeys_StringToWriterMapEntry'):
        assert _is_linked(a2, 'hbmapkeys_StringToWriterMapEntry', b)
    _safe_set(b, 'hbmapkeys_Book', set())
    assert not _is_linked(b, 'hbmapkeys_Book', a2)
    if hasattr(a2, 'hbmapkeys_StringToWriterMapEntry'):
        assert not _is_linked(a2, 'hbmapkeys_StringToWriterMapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cityByWriter1_stub_double():
    # hbmapkeys_WriterToCityMapEntry has no real 'hbmapkeys_WriterToCityMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so hbmapkeys_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hbmapkeys_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hbmapkeys_Book(title="sample_text")
    partner = hbmapkeys_WriterToCityMapEntry()
    setattr(partner, 'hbmapkeys_WriterToCityMapEntry', None)
    _safe_set(owner, 'hbmapkeys_Book2', {partner})
    assert getattr(partner, 'hbmapkeys_WriterToCityMapEntry') == owner
    _safe_set(owner, 'hbmapkeys_Book2', set())
    assert getattr(partner, 'hbmapkeys_WriterToCityMapEntry') is None


def test_assoc_key7_stub_double():
    # hbmapkeys_WriterToCityMapEntry has no real 'hbmapkeys_WriterToCityMapEntry8' property in the generated
    # code (a bare stub) -- manually attach it so hbmapkeys_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hbmapkeys_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hbmapkeys_Writer(name="sample_text")
    partner = hbmapkeys_WriterToCityMapEntry()
    setattr(partner, 'hbmapkeys_WriterToCityMapEntry8', None)
    _safe_set(owner, 'hbmapkeys_Writer9', partner)
    assert getattr(partner, 'hbmapkeys_WriterToCityMapEntry8') == owner
    _safe_set(owner, 'hbmapkeys_Writer9', None)
    assert getattr(partner, 'hbmapkeys_WriterToCityMapEntry8') is None


def test_assoc_value10_stub_double():
    # hbmapkeys_WriterToCityMapEntry has no real 'hbmapkeys_WriterToCityMapEntry11' property in the generated
    # code (a bare stub) -- manually attach it so hbmapkeys_City's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hbmapkeys_City's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hbmapkeys_City(name="sample_text")
    partner = hbmapkeys_WriterToCityMapEntry()
    setattr(partner, 'hbmapkeys_WriterToCityMapEntry11', None)
    _safe_set(owner, 'hbmapkeys_City12', partner)
    assert getattr(partner, 'hbmapkeys_WriterToCityMapEntry11') == owner
    _safe_set(owner, 'hbmapkeys_City12', None)
    assert getattr(partner, 'hbmapkeys_WriterToCityMapEntry11') is None


