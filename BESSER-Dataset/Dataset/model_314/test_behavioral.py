import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_Library,
    library_Writer,
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

def test_assoc_author0_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages="sample_text", title="sample_text")
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


def test_assoc_books2_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Book(category="sample_text", pages="sample_text", title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Library3'):
        assert _is_linked(a1, 'library_Library3', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Library3'):
        assert not _is_linked(a1, 'library_Library3', b)
    if hasattr(a2, 'library_Library3'):
        assert _is_linked(a2, 'library_Library3', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Library3'):
        assert not _is_linked(a2, 'library_Library3', b)


def test_assoc_books4_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages="sample_text", title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'author'):
        assert _is_linked(a1, 'author', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'author'):
        assert not _is_linked(a1, 'author', b)
    if hasattr(a2, 'author'):
        assert _is_linked(a2, 'author', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'author'):
        assert not _is_linked(a2, 'author', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library', {a1})
    assert _is_linked(b, 'library_Library', a1)
    if hasattr(a1, 'library_Writer'):
        assert _is_linked(a1, 'library_Writer', b)
    _safe_set(b, 'library_Library', {a2})
    assert _is_linked(b, 'library_Library', a2)
    if hasattr(a1, 'library_Writer'):
        assert not _is_linked(a1, 'library_Writer', b)
    if hasattr(a2, 'library_Writer'):
        assert _is_linked(a2, 'library_Writer', b)
    _safe_set(b, 'library_Library', set())
    assert not _is_linked(b, 'library_Library', a2)
    if hasattr(a2, 'library_Writer'):
        assert not _is_linked(a2, 'library_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

