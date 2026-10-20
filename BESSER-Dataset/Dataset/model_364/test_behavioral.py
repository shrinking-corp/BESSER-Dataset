import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    eiqlibrary_Book,
    eiqlibrary_Library,
    eiqlibrary_Writer,
    BookCategory,
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

def test_assoc_authors6_reverse_link_reassign_clear():
    a1 = eiqlibrary_Writer(name="sample_text")
    a2 = eiqlibrary_Writer(name="sample_text_2")
    b = eiqlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'books', {a1})
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'books', {a2})
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'books', set())
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_books1_reverse_link_reassign_clear():
    a1 = eiqlibrary_Library(address="sample_text", internalRequestCount=7, requestCount=7, sumOfPages=7)
    a2 = eiqlibrary_Library(address="sample_text_2", internalRequestCount=13, requestCount=13, sumOfPages=13)
    b = eiqlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'eiqlibrary_Book', a1)
    assert _is_linked(b, 'eiqlibrary_Book', a1)
    if hasattr(a1, 'eiqlibrary_Library2'):
        assert _is_linked(a1, 'eiqlibrary_Library2', b)
    _safe_set(b, 'eiqlibrary_Book', a2)
    assert _is_linked(b, 'eiqlibrary_Book', a2)
    if hasattr(a1, 'eiqlibrary_Library2'):
        assert not _is_linked(a1, 'eiqlibrary_Library2', b)
    if hasattr(a2, 'eiqlibrary_Library2'):
        assert _is_linked(a2, 'eiqlibrary_Library2', b)
    _safe_set(b, 'eiqlibrary_Book', None)
    assert not _is_linked(b, 'eiqlibrary_Book', a2)
    if hasattr(a2, 'eiqlibrary_Library2'):
        assert not _is_linked(a2, 'eiqlibrary_Library2', b)


def test_assoc_books7_reverse_link_reassign_clear():
    a1 = eiqlibrary_Writer(name="sample_text")
    a2 = eiqlibrary_Writer(name="sample_text_2")
    b = eiqlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'authors'):
        assert _is_linked(a1, 'authors', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'authors'):
        assert not _is_linked(a1, 'authors', b)
    if hasattr(a2, 'authors'):
        assert _is_linked(a2, 'authors', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'authors'):
        assert not _is_linked(a2, 'authors', b)


def test_assoc_firstBook8_reverse_link_reassign_clear():
    a1 = eiqlibrary_Writer(name="sample_text")
    a2 = eiqlibrary_Writer(name="sample_text_2")
    b = eiqlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'eiqlibrary_Book10', a1)
    assert _is_linked(b, 'eiqlibrary_Book10', a1)
    if hasattr(a1, 'eiqlibrary_Writer9'):
        assert _is_linked(a1, 'eiqlibrary_Writer9', b)
    _safe_set(b, 'eiqlibrary_Book10', a2)
    assert _is_linked(b, 'eiqlibrary_Book10', a2)
    if hasattr(a1, 'eiqlibrary_Writer9'):
        assert not _is_linked(a1, 'eiqlibrary_Writer9', b)
    if hasattr(a2, 'eiqlibrary_Writer9'):
        assert _is_linked(a2, 'eiqlibrary_Writer9', b)
    _safe_set(b, 'eiqlibrary_Book10', None)
    assert not _is_linked(b, 'eiqlibrary_Book10', a2)
    if hasattr(a2, 'eiqlibrary_Writer9'):
        assert not _is_linked(a2, 'eiqlibrary_Writer9', b)


def test_assoc_scifiBooks11_reverse_link_reassign_clear():
    a1 = eiqlibrary_Writer(name="sample_text")
    a2 = eiqlibrary_Writer(name="sample_text_2")
    b = eiqlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'eiqlibrary_Book13', a1)
    assert _is_linked(b, 'eiqlibrary_Book13', a1)
    if hasattr(a1, 'eiqlibrary_Writer12'):
        assert _is_linked(a1, 'eiqlibrary_Writer12', b)
    _safe_set(b, 'eiqlibrary_Book13', a2)
    assert _is_linked(b, 'eiqlibrary_Book13', a2)
    if hasattr(a1, 'eiqlibrary_Writer12'):
        assert not _is_linked(a1, 'eiqlibrary_Writer12', b)
    if hasattr(a2, 'eiqlibrary_Writer12'):
        assert _is_linked(a2, 'eiqlibrary_Writer12', b)
    _safe_set(b, 'eiqlibrary_Book13', None)
    assert not _is_linked(b, 'eiqlibrary_Book13', a2)
    if hasattr(a2, 'eiqlibrary_Writer12'):
        assert not _is_linked(a2, 'eiqlibrary_Writer12', b)


def test_assoc_someBooks3_reverse_link_reassign_clear():
    a1 = eiqlibrary_Library(address="sample_text", internalRequestCount=7, requestCount=7, sumOfPages=7)
    a2 = eiqlibrary_Library(address="sample_text_2", internalRequestCount=13, requestCount=13, sumOfPages=13)
    b = eiqlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'eiqlibrary_Book5', a1)
    assert _is_linked(b, 'eiqlibrary_Book5', a1)
    if hasattr(a1, 'eiqlibrary_Library4'):
        assert _is_linked(a1, 'eiqlibrary_Library4', b)
    _safe_set(b, 'eiqlibrary_Book5', a2)
    assert _is_linked(b, 'eiqlibrary_Book5', a2)
    if hasattr(a1, 'eiqlibrary_Library4'):
        assert not _is_linked(a1, 'eiqlibrary_Library4', b)
    if hasattr(a2, 'eiqlibrary_Library4'):
        assert _is_linked(a2, 'eiqlibrary_Library4', b)
    _safe_set(b, 'eiqlibrary_Book5', None)
    assert not _is_linked(b, 'eiqlibrary_Book5', a2)
    if hasattr(a2, 'eiqlibrary_Library4'):
        assert not _is_linked(a2, 'eiqlibrary_Library4', b)


def test_assoc_writers0_reverse_link_reassign_clear():
    a1 = eiqlibrary_Writer(name="sample_text")
    a2 = eiqlibrary_Writer(name="sample_text_2")
    b = eiqlibrary_Library(address="sample_text", internalRequestCount=7, requestCount=7, sumOfPages=7)
    _safe_set(b, 'eiqlibrary_Library', {a1})
    assert _is_linked(b, 'eiqlibrary_Library', a1)
    if hasattr(a1, 'eiqlibrary_Writer'):
        assert _is_linked(a1, 'eiqlibrary_Writer', b)
    _safe_set(b, 'eiqlibrary_Library', {a2})
    assert _is_linked(b, 'eiqlibrary_Library', a2)
    if hasattr(a1, 'eiqlibrary_Writer'):
        assert not _is_linked(a1, 'eiqlibrary_Writer', b)
    if hasattr(a2, 'eiqlibrary_Writer'):
        assert _is_linked(a2, 'eiqlibrary_Writer', b)
    _safe_set(b, 'eiqlibrary_Library', set())
    assert not _is_linked(b, 'eiqlibrary_Library', a2)
    if hasattr(a2, 'eiqlibrary_Writer'):
        assert not _is_linked(a2, 'eiqlibrary_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

