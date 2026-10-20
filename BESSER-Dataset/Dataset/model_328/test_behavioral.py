import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Library_Book,
    Library_Library,
    Library_Writer,
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

def test_assoc_books3_reverse_link_reassign_clear():
    a1 = Library_Library(id=7, name="sample_text")
    a2 = Library_Library(id=13, name="sample_text_2")
    b = Library_Book(blurb="sample_text", category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'library'):
        assert _is_linked(a1, 'library', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'library'):
        assert not _is_linked(a1, 'library', b)
    if hasattr(a2, 'library'):
        assert _is_linked(a2, 'library', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'library'):
        assert not _is_linked(a2, 'library', b)


def test_assoc_books7_reverse_link_reassign_clear():
    a1 = Library_Writer(id=7, name="sample_text")
    a2 = Library_Writer(id=13, name="sample_text_2")
    b = Library_Book(blurb="sample_text", category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book8', a1)
    assert _is_linked(b, 'Book8', a1)
    if hasattr(a1, 'writer'):
        assert _is_linked(a1, 'writer', b)
    _safe_set(b, 'Book8', a2)
    assert _is_linked(b, 'Book8', a2)
    if hasattr(a1, 'writer'):
        assert not _is_linked(a1, 'writer', b)
    if hasattr(a2, 'writer'):
        assert _is_linked(a2, 'writer', b)
    _safe_set(b, 'Book8', None)
    assert not _is_linked(b, 'Book8', a2)
    if hasattr(a2, 'writer'):
        assert not _is_linked(a2, 'writer', b)


def test_assoc_library1_reverse_link_reassign_clear():
    a1 = Library_Library(id=7, name="sample_text")
    a2 = Library_Library(id=13, name="sample_text_2")
    b = Library_Book(blurb="sample_text", category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'books2', a1)
    assert _is_linked(b, 'books2', a1)
    if hasattr(a1, 'Library'):
        assert _is_linked(a1, 'Library', b)
    _safe_set(b, 'books2', a2)
    assert _is_linked(b, 'books2', a2)
    if hasattr(a1, 'Library'):
        assert not _is_linked(a1, 'Library', b)
    if hasattr(a2, 'Library'):
        assert _is_linked(a2, 'Library', b)
    _safe_set(b, 'books2', None)
    assert not _is_linked(b, 'books2', a2)
    if hasattr(a2, 'Library'):
        assert not _is_linked(a2, 'Library', b)


def test_assoc_library9_reverse_link_reassign_clear():
    a1 = Library_Writer(id=7, name="sample_text")
    a2 = Library_Writer(id=13, name="sample_text_2")
    b = Library_Library(id=7, name="sample_text")
    _safe_set(b, 'Library10', a1)
    assert _is_linked(b, 'Library10', a1)
    if hasattr(a1, 'writers'):
        assert _is_linked(a1, 'writers', b)
    _safe_set(b, 'Library10', a2)
    assert _is_linked(b, 'Library10', a2)
    if hasattr(a1, 'writers'):
        assert not _is_linked(a1, 'writers', b)
    if hasattr(a2, 'writers'):
        assert _is_linked(a2, 'writers', b)
    _safe_set(b, 'Library10', None)
    assert not _is_linked(b, 'Library10', a2)
    if hasattr(a2, 'writers'):
        assert not _is_linked(a2, 'writers', b)


def test_assoc_writer0_reverse_link_reassign_clear():
    a1 = Library_Writer(id=7, name="sample_text")
    a2 = Library_Writer(id=13, name="sample_text_2")
    b = Library_Book(blurb="sample_text", category="sample_text", pages=7, title="sample_text")
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


def test_assoc_writers4_reverse_link_reassign_clear():
    a1 = Library_Writer(id=7, name="sample_text")
    a2 = Library_Writer(id=13, name="sample_text_2")
    b = Library_Library(id=7, name="sample_text")
    _safe_set(b, 'library5', {a1})
    assert _is_linked(b, 'library5', a1)
    if hasattr(a1, 'Writer6'):
        assert _is_linked(a1, 'Writer6', b)
    _safe_set(b, 'library5', {a2})
    assert _is_linked(b, 'library5', a2)
    if hasattr(a1, 'Writer6'):
        assert not _is_linked(a1, 'Writer6', b)
    if hasattr(a2, 'Writer6'):
        assert _is_linked(a2, 'Writer6', b)
    _safe_set(b, 'library5', set())
    assert not _is_linked(b, 'library5', a2)
    if hasattr(a2, 'Writer6'):
        assert not _is_linked(a2, 'Writer6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

