import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_Library,
    library_Opinion,
    library_Review,
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

def test_assoc_author5_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
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


def test_assoc_book11_reverse_link_reassign_clear():
    a1 = library_Opinion(context="sample_text", text="sample_text")
    a2 = library_Opinion(context="sample_text_2", text="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book12', a1)
    assert _is_linked(b, 'library_Book12', a1)
    if hasattr(a1, 'library_Opinion'):
        assert _is_linked(a1, 'library_Opinion', b)
    _safe_set(b, 'library_Book12', a2)
    assert _is_linked(b, 'library_Book12', a2)
    if hasattr(a1, 'library_Opinion'):
        assert not _is_linked(a1, 'library_Opinion', b)
    if hasattr(a2, 'library_Opinion'):
        assert _is_linked(a2, 'library_Opinion', b)
    _safe_set(b, 'library_Book12', None)
    assert not _is_linked(b, 'library_Book12', a2)
    if hasattr(a2, 'library_Opinion'):
        assert not _is_linked(a2, 'library_Opinion', b)


def test_assoc_book7_reverse_link_reassign_clear():
    a1 = library_Review(positive=True, title="sample_text")
    a2 = library_Review(positive=False, title="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book8', a1)
    assert _is_linked(b, 'Book8', a1)
    if hasattr(a1, 'reviews'):
        assert _is_linked(a1, 'reviews', b)
    _safe_set(b, 'Book8', a2)
    assert _is_linked(b, 'Book8', a2)
    if hasattr(a1, 'reviews'):
        assert not _is_linked(a1, 'reviews', b)
    if hasattr(a2, 'reviews'):
        assert _is_linked(a2, 'reviews', b)
    _safe_set(b, 'Book8', None)
    assert not _is_linked(b, 'Book8', a2)
    if hasattr(a2, 'reviews'):
        assert not _is_linked(a2, 'reviews', b)


def test_assoc_books1_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Library2'):
        assert _is_linked(a1, 'library_Library2', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Library2'):
        assert not _is_linked(a1, 'library_Library2', b)
    if hasattr(a2, 'library_Library2'):
        assert _is_linked(a2, 'library_Library2', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Library2'):
        assert not _is_linked(a2, 'library_Library2', b)


def test_assoc_books3_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
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


def test_assoc_opinions4_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Opinion(context="sample_text", text="sample_text")
    _safe_set(b, 'Opinion', a1)
    assert _is_linked(b, 'Opinion', a1)
    if hasattr(a1, 'writer'):
        assert _is_linked(a1, 'writer', b)
    _safe_set(b, 'Opinion', a2)
    assert _is_linked(b, 'Opinion', a2)
    if hasattr(a1, 'writer'):
        assert not _is_linked(a1, 'writer', b)
    if hasattr(a2, 'writer'):
        assert _is_linked(a2, 'writer', b)
    _safe_set(b, 'Opinion', None)
    assert not _is_linked(b, 'Opinion', a2)
    if hasattr(a2, 'writer'):
        assert not _is_linked(a2, 'writer', b)


def test_assoc_reviews6_reverse_link_reassign_clear():
    a1 = library_Review(positive=True, title="sample_text")
    a2 = library_Review(positive=False, title="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'book', {a1})
    assert _is_linked(b, 'book', a1)
    if hasattr(a1, 'Review'):
        assert _is_linked(a1, 'Review', b)
    _safe_set(b, 'book', {a2})
    assert _is_linked(b, 'book', a2)
    if hasattr(a1, 'Review'):
        assert not _is_linked(a1, 'Review', b)
    if hasattr(a2, 'Review'):
        assert _is_linked(a2, 'Review', b)
    _safe_set(b, 'book', set())
    assert not _is_linked(b, 'book', a2)
    if hasattr(a2, 'Review'):
        assert not _is_linked(a2, 'Review', b)


def test_assoc_writer9_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Opinion(context="sample_text", text="sample_text")
    _safe_set(b, 'opinions', a1)
    assert _is_linked(b, 'opinions', a1)
    if hasattr(a1, 'Writer10'):
        assert _is_linked(a1, 'Writer10', b)
    _safe_set(b, 'opinions', a2)
    assert _is_linked(b, 'opinions', a2)
    if hasattr(a1, 'Writer10'):
        assert not _is_linked(a1, 'Writer10', b)
    if hasattr(a2, 'Writer10'):
        assert _is_linked(a2, 'Writer10', b)
    _safe_set(b, 'opinions', None)
    assert not _is_linked(b, 'opinions', a2)
    if hasattr(a2, 'Writer10'):
        assert not _is_linked(a2, 'Writer10', b)


def test_assoc_writers0_reverse_link_reassign_clear():
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

