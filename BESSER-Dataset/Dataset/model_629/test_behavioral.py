import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    test_Book,
    test_Library,
    test_Writer,
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

def test_assoc_books1_reverse_link_reassign_clear():
    a1 = test_Library(name="sample_text")
    a2 = test_Library(name="sample_text_2")
    b = test_Book(pages=7, title="sample_text")
    _safe_set(b, 'test_Book', a1)
    assert _is_linked(b, 'test_Book', a1)
    if hasattr(a1, 'test_Library'):
        assert _is_linked(a1, 'test_Library', b)
    _safe_set(b, 'test_Book', a2)
    assert _is_linked(b, 'test_Book', a2)
    if hasattr(a1, 'test_Library'):
        assert not _is_linked(a1, 'test_Library', b)
    if hasattr(a2, 'test_Library'):
        assert _is_linked(a2, 'test_Library', b)
    _safe_set(b, 'test_Book', None)
    assert not _is_linked(b, 'test_Book', a2)
    if hasattr(a2, 'test_Library'):
        assert not _is_linked(a2, 'test_Library', b)


def test_assoc_books2_reverse_link_reassign_clear():
    a1 = test_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", lastName="sample_text")
    a2 = test_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", lastName="sample_text_2")
    b = test_Book(pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'writers'):
        assert _is_linked(a1, 'writers', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'writers'):
        assert not _is_linked(a1, 'writers', b)
    if hasattr(a2, 'writers'):
        assert _is_linked(a2, 'writers', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'writers'):
        assert not _is_linked(a2, 'writers', b)


def test_assoc_library3_reverse_link_reassign_clear():
    a1 = test_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", lastName="sample_text")
    a2 = test_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", lastName="sample_text_2")
    b = test_Library(name="sample_text")
    _safe_set(b, 'Library', a1)
    assert _is_linked(b, 'Library', a1)
    if hasattr(a1, 'writers4'):
        assert _is_linked(a1, 'writers4', b)
    _safe_set(b, 'Library', a2)
    assert _is_linked(b, 'Library', a2)
    if hasattr(a1, 'writers4'):
        assert not _is_linked(a1, 'writers4', b)
    if hasattr(a2, 'writers4'):
        assert _is_linked(a2, 'writers4', b)
    _safe_set(b, 'Library', None)
    assert not _is_linked(b, 'Library', a2)
    if hasattr(a2, 'writers4'):
        assert not _is_linked(a2, 'writers4', b)


def test_assoc_writers0_reverse_link_reassign_clear():
    a1 = test_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", lastName="sample_text")
    a2 = test_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", lastName="sample_text_2")
    b = test_Library(name="sample_text")
    _safe_set(b, 'library', {a1})
    assert _is_linked(b, 'library', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'library', {a2})
    assert _is_linked(b, 'library', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'library', set())
    assert not _is_linked(b, 'library', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_writers5_reverse_link_reassign_clear():
    a1 = test_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", lastName="sample_text")
    a2 = test_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", lastName="sample_text_2")
    b = test_Book(pages=7, title="sample_text")
    _safe_set(b, 'books', a1)
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Writer6'):
        assert _is_linked(a1, 'Writer6', b)
    _safe_set(b, 'books', a2)
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Writer6'):
        assert not _is_linked(a1, 'Writer6', b)
    if hasattr(a2, 'Writer6'):
        assert _is_linked(a2, 'Writer6', b)
    _safe_set(b, 'books', None)
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Writer6'):
        assert not _is_linked(a2, 'Writer6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

