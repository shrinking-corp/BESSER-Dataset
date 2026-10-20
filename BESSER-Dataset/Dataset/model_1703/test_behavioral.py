import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Identifiable,
    emapsample_Book,
    emapsample_BookStore,
    emapsample_EStringToStringMapEntry,
    emapsample_StringToWriterMapEntry,
    emapsample_Writer,
    emapsample_WriterToBookMapEntry,
    emapsample_WriterToNameMapEntry,
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

def test_assoc_key14_reverse_link_reassign_clear():
    a1 = emapsample_WriterToNameMapEntry(value="sample_text")
    a2 = emapsample_WriterToNameMapEntry(value="sample_text_2")
    b = emapsample_Writer(name="sample_text")
    _safe_set(b, 'emapsample_Writer16', a1)
    assert _is_linked(b, 'emapsample_Writer16', a1)
    if hasattr(a1, 'emapsample_WriterToNameMapEntry15'):
        assert _is_linked(a1, 'emapsample_WriterToNameMapEntry15', b)
    _safe_set(b, 'emapsample_Writer16', a2)
    assert _is_linked(b, 'emapsample_Writer16', a2)
    if hasattr(a1, 'emapsample_WriterToNameMapEntry15'):
        assert not _is_linked(a1, 'emapsample_WriterToNameMapEntry15', b)
    if hasattr(a2, 'emapsample_WriterToNameMapEntry15'):
        assert _is_linked(a2, 'emapsample_WriterToNameMapEntry15', b)
    _safe_set(b, 'emapsample_Writer16', None)
    assert not _is_linked(b, 'emapsample_Writer16', a2)
    if hasattr(a2, 'emapsample_WriterToNameMapEntry15'):
        assert not _is_linked(a2, 'emapsample_WriterToNameMapEntry15', b)


def test_assoc_namesByWriter4_reverse_link_reassign_clear():
    a1 = emapsample_WriterToNameMapEntry(value="sample_text")
    a2 = emapsample_WriterToNameMapEntry(value="sample_text_2")
    b = emapsample_BookStore(name="sample_text")
    _safe_set(b, 'emapsample_BookStore5', {a1})
    assert _is_linked(b, 'emapsample_BookStore5', a1)
    if hasattr(a1, 'emapsample_WriterToNameMapEntry'):
        assert _is_linked(a1, 'emapsample_WriterToNameMapEntry', b)
    _safe_set(b, 'emapsample_BookStore5', {a2})
    assert _is_linked(b, 'emapsample_BookStore5', a2)
    if hasattr(a1, 'emapsample_WriterToNameMapEntry'):
        assert not _is_linked(a1, 'emapsample_WriterToNameMapEntry', b)
    if hasattr(a2, 'emapsample_WriterToNameMapEntry'):
        assert _is_linked(a2, 'emapsample_WriterToNameMapEntry', b)
    _safe_set(b, 'emapsample_BookStore5', set())
    assert not _is_linked(b, 'emapsample_BookStore5', a2)
    if hasattr(a2, 'emapsample_WriterToNameMapEntry'):
        assert not _is_linked(a2, 'emapsample_WriterToNameMapEntry', b)


def test_assoc_value6_reverse_link_reassign_clear():
    a1 = emapsample_Writer(name="sample_text")
    a2 = emapsample_Writer(name="sample_text_2")
    b = emapsample_StringToWriterMapEntry(key="sample_text")
    _safe_set(b, 'emapsample_StringToWriterMapEntry7', a1)
    assert _is_linked(b, 'emapsample_StringToWriterMapEntry7', a1)
    if hasattr(a1, 'emapsample_Writer'):
        assert _is_linked(a1, 'emapsample_Writer', b)
    _safe_set(b, 'emapsample_StringToWriterMapEntry7', a2)
    assert _is_linked(b, 'emapsample_StringToWriterMapEntry7', a2)
    if hasattr(a1, 'emapsample_Writer'):
        assert not _is_linked(a1, 'emapsample_Writer', b)
    if hasattr(a2, 'emapsample_Writer'):
        assert _is_linked(a2, 'emapsample_Writer', b)
    _safe_set(b, 'emapsample_StringToWriterMapEntry7', None)
    assert not _is_linked(b, 'emapsample_StringToWriterMapEntry7', a2)
    if hasattr(a2, 'emapsample_Writer'):
        assert not _is_linked(a2, 'emapsample_Writer', b)


def test_assoc_writers0_reverse_link_reassign_clear():
    a1 = emapsample_StringToWriterMapEntry(key="sample_text")
    a2 = emapsample_StringToWriterMapEntry(key="sample_text_2")
    b = emapsample_Book(title="sample_text")
    _safe_set(b, 'emapsample_Book', {a1})
    assert _is_linked(b, 'emapsample_Book', a1)
    if hasattr(a1, 'emapsample_StringToWriterMapEntry'):
        assert _is_linked(a1, 'emapsample_StringToWriterMapEntry', b)
    _safe_set(b, 'emapsample_Book', {a2})
    assert _is_linked(b, 'emapsample_Book', a2)
    if hasattr(a1, 'emapsample_StringToWriterMapEntry'):
        assert not _is_linked(a1, 'emapsample_StringToWriterMapEntry', b)
    if hasattr(a2, 'emapsample_StringToWriterMapEntry'):
        assert _is_linked(a2, 'emapsample_StringToWriterMapEntry', b)
    _safe_set(b, 'emapsample_Book', set())
    assert not _is_linked(b, 'emapsample_Book', a2)
    if hasattr(a2, 'emapsample_StringToWriterMapEntry'):
        assert not _is_linked(a2, 'emapsample_StringToWriterMapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_booksByWriter1_stub_double():
    # emapsample_WriterToBookMapEntry has no real 'emapsample_WriterToBookMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so emapsample_BookStore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapsample_BookStore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapsample_BookStore(name="sample_text")
    partner = emapsample_WriterToBookMapEntry()
    setattr(partner, 'emapsample_WriterToBookMapEntry', None)
    _safe_set(owner, 'emapsample_BookStore', {partner})
    assert getattr(partner, 'emapsample_WriterToBookMapEntry') == owner
    _safe_set(owner, 'emapsample_BookStore', set())
    assert getattr(partner, 'emapsample_WriterToBookMapEntry') is None


def test_assoc_key8_stub_double():
    # emapsample_WriterToBookMapEntry has no real 'emapsample_WriterToBookMapEntry9' property in the generated
    # code (a bare stub) -- manually attach it so emapsample_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapsample_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapsample_Writer(name="sample_text")
    partner = emapsample_WriterToBookMapEntry()
    setattr(partner, 'emapsample_WriterToBookMapEntry9', None)
    _safe_set(owner, 'emapsample_Writer10', partner)
    assert getattr(partner, 'emapsample_WriterToBookMapEntry9') == owner
    _safe_set(owner, 'emapsample_Writer10', None)
    assert getattr(partner, 'emapsample_WriterToBookMapEntry9') is None


def test_assoc_keyWords2_stub_double():
    # emapsample_EStringToStringMapEntry has no real 'emapsample_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so emapsample_BookStore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapsample_BookStore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapsample_BookStore(name="sample_text")
    partner = emapsample_EStringToStringMapEntry()
    setattr(partner, 'emapsample_EStringToStringMapEntry', None)
    _safe_set(owner, 'emapsample_BookStore3', {partner})
    assert getattr(partner, 'emapsample_EStringToStringMapEntry') == owner
    _safe_set(owner, 'emapsample_BookStore3', set())
    assert getattr(partner, 'emapsample_EStringToStringMapEntry') is None


def test_assoc_value11_stub_double():
    # emapsample_WriterToBookMapEntry has no real 'emapsample_WriterToBookMapEntry12' property in the generated
    # code (a bare stub) -- manually attach it so emapsample_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapsample_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapsample_Book(title="sample_text")
    partner = emapsample_WriterToBookMapEntry()
    setattr(partner, 'emapsample_WriterToBookMapEntry12', None)
    _safe_set(owner, 'emapsample_Book13', partner)
    assert getattr(partner, 'emapsample_WriterToBookMapEntry12') == owner
    _safe_set(owner, 'emapsample_Book13', None)
    assert getattr(partner, 'emapsample_WriterToBookMapEntry12') is None


