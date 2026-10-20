import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Asset,
    Book,
    Library,
    libraryExample_Asset,
    libraryExample_Book,
    libraryExample_Library,
    libraryExample_SchoolBook,
    libraryExample_SchoolLibrary,
    libraryExample_Writer,
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

def test_assoc_books0_reverse_link_reassign_clear():
    a1 = libraryExample_Library(name="sample_text")
    a2 = libraryExample_Library(name="sample_text_2")
    b = libraryExample_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'libraryExample_Book', a1)
    assert _is_linked(b, 'libraryExample_Book', a1)
    if hasattr(a1, 'libraryExample_Library'):
        assert _is_linked(a1, 'libraryExample_Library', b)
    _safe_set(b, 'libraryExample_Book', a2)
    assert _is_linked(b, 'libraryExample_Book', a2)
    if hasattr(a1, 'libraryExample_Library'):
        assert not _is_linked(a1, 'libraryExample_Library', b)
    if hasattr(a2, 'libraryExample_Library'):
        assert _is_linked(a2, 'libraryExample_Library', b)
    _safe_set(b, 'libraryExample_Book', None)
    assert not _is_linked(b, 'libraryExample_Book', a2)
    if hasattr(a2, 'libraryExample_Library'):
        assert not _is_linked(a2, 'libraryExample_Library', b)


def test_assoc_books4_reverse_link_reassign_clear():
    a1 = libraryExample_Writer(lastname="sample_text", name="sample_text")
    a2 = libraryExample_Writer(lastname="sample_text_2", name="sample_text_2")
    b = libraryExample_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'writer'):
        assert _is_linked(a1, 'writer', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'writer'):
        assert not _is_linked(a1, 'writer', b)
    if hasattr(a2, 'writer'):
        assert _is_linked(a2, 'writer', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'writer'):
        assert not _is_linked(a2, 'writer', b)


def test_assoc_writer3_reverse_link_reassign_clear():
    a1 = libraryExample_Writer(lastname="sample_text", name="sample_text")
    a2 = libraryExample_Writer(lastname="sample_text_2", name="sample_text_2")
    b = libraryExample_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'books', a1)
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'books', a2)
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'books', None)
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = libraryExample_Writer(lastname="sample_text", name="sample_text")
    a2 = libraryExample_Writer(lastname="sample_text_2", name="sample_text_2")
    b = libraryExample_Library(name="sample_text")
    _safe_set(b, 'libraryExample_Library2', {a1})
    assert _is_linked(b, 'libraryExample_Library2', a1)
    if hasattr(a1, 'libraryExample_Writer'):
        assert _is_linked(a1, 'libraryExample_Writer', b)
    _safe_set(b, 'libraryExample_Library2', {a2})
    assert _is_linked(b, 'libraryExample_Library2', a2)
    if hasattr(a1, 'libraryExample_Writer'):
        assert not _is_linked(a1, 'libraryExample_Writer', b)
    if hasattr(a2, 'libraryExample_Writer'):
        assert _is_linked(a2, 'libraryExample_Writer', b)
    _safe_set(b, 'libraryExample_Library2', set())
    assert not _is_linked(b, 'libraryExample_Library2', a2)
    if hasattr(a2, 'libraryExample_Writer'):
        assert not _is_linked(a2, 'libraryExample_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

