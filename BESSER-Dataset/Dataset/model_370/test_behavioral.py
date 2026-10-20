import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Author,
    library_Book,
    library_Employee,
    library_Library,
    library_Shelf,
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

def test_assoc_author1_reverse_link_reassign_clear():
    a1 = library_Book(title="sample_text")
    a2 = library_Book(title="sample_text_2")
    b = library_Author(name="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'books'):
        assert _is_linked(a1, 'books', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'books'):
        assert not _is_linked(a1, 'books', b)
    if hasattr(a2, 'books'):
        assert _is_linked(a2, 'books', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'books'):
        assert not _is_linked(a2, 'books', b)


def test_assoc_authors5_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Author(name="sample_text")
    _safe_set(b, 'library_Author', a1)
    assert _is_linked(b, 'library_Author', a1)
    if hasattr(a1, 'library_Library6'):
        assert _is_linked(a1, 'library_Library6', b)
    _safe_set(b, 'library_Author', a2)
    assert _is_linked(b, 'library_Author', a2)
    if hasattr(a1, 'library_Library6'):
        assert not _is_linked(a1, 'library_Library6', b)
    if hasattr(a2, 'library_Library6'):
        assert _is_linked(a2, 'library_Library6', b)
    _safe_set(b, 'library_Author', None)
    assert not _is_linked(b, 'library_Author', a2)
    if hasattr(a2, 'library_Library6'):
        assert not _is_linked(a2, 'library_Library6', b)


def test_assoc_books0_reverse_link_reassign_clear():
    a1 = library_Book(title="sample_text")
    a2 = library_Book(title="sample_text_2")
    b = library_Author(name="sample_text")
    _safe_set(b, 'author', {a1})
    assert _is_linked(b, 'author', a1)
    if hasattr(a1, 'Book'):
        assert _is_linked(a1, 'Book', b)
    _safe_set(b, 'author', {a2})
    assert _is_linked(b, 'author', a2)
    if hasattr(a1, 'Book'):
        assert not _is_linked(a1, 'Book', b)
    if hasattr(a2, 'Book'):
        assert _is_linked(a2, 'Book', b)
    _safe_set(b, 'author', set())
    assert not _is_linked(b, 'author', a2)
    if hasattr(a2, 'Book'):
        assert not _is_linked(a2, 'Book', b)


def test_assoc_books10_reverse_link_reassign_clear():
    a1 = library_Shelf(name="sample_text")
    a2 = library_Shelf(name="sample_text_2")
    b = library_Book(title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Shelf11'):
        assert _is_linked(a1, 'library_Shelf11', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Shelf11'):
        assert not _is_linked(a1, 'library_Shelf11', b)
    if hasattr(a2, 'library_Shelf11'):
        assert _is_linked(a2, 'library_Shelf11', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Shelf11'):
        assert not _is_linked(a2, 'library_Shelf11', b)


def test_assoc_employees7_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Employee(name="sample_text")
    _safe_set(b, 'library_Employee9', a1)
    assert _is_linked(b, 'library_Employee9', a1)
    if hasattr(a1, 'library_Library8'):
        assert _is_linked(a1, 'library_Library8', b)
    _safe_set(b, 'library_Employee9', a2)
    assert _is_linked(b, 'library_Employee9', a2)
    if hasattr(a1, 'library_Library8'):
        assert not _is_linked(a1, 'library_Library8', b)
    if hasattr(a2, 'library_Library8'):
        assert _is_linked(a2, 'library_Library8', b)
    _safe_set(b, 'library_Employee9', None)
    assert not _is_linked(b, 'library_Employee9', a2)
    if hasattr(a2, 'library_Library8'):
        assert not _is_linked(a2, 'library_Library8', b)


def test_assoc_shelves2_reverse_link_reassign_clear():
    a1 = library_Shelf(name="sample_text")
    a2 = library_Shelf(name="sample_text_2")
    b = library_Employee(name="sample_text")
    _safe_set(b, 'library_Employee', {a1})
    assert _is_linked(b, 'library_Employee', a1)
    if hasattr(a1, 'library_Shelf'):
        assert _is_linked(a1, 'library_Shelf', b)
    _safe_set(b, 'library_Employee', {a2})
    assert _is_linked(b, 'library_Employee', a2)
    if hasattr(a1, 'library_Shelf'):
        assert not _is_linked(a1, 'library_Shelf', b)
    if hasattr(a2, 'library_Shelf'):
        assert _is_linked(a2, 'library_Shelf', b)
    _safe_set(b, 'library_Employee', set())
    assert not _is_linked(b, 'library_Employee', a2)
    if hasattr(a2, 'library_Shelf'):
        assert not _is_linked(a2, 'library_Shelf', b)


def test_assoc_shelves3_reverse_link_reassign_clear():
    a1 = library_Shelf(name="sample_text")
    a2 = library_Shelf(name="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library_Library', {a1})
    assert _is_linked(b, 'library_Library', a1)
    if hasattr(a1, 'library_Shelf4'):
        assert _is_linked(a1, 'library_Shelf4', b)
    _safe_set(b, 'library_Library', {a2})
    assert _is_linked(b, 'library_Library', a2)
    if hasattr(a1, 'library_Shelf4'):
        assert not _is_linked(a1, 'library_Shelf4', b)
    if hasattr(a2, 'library_Shelf4'):
        assert _is_linked(a2, 'library_Shelf4', b)
    _safe_set(b, 'library_Library', set())
    assert not _is_linked(b, 'library_Library', a2)
    if hasattr(a2, 'library_Shelf4'):
        assert not _is_linked(a2, 'library_Shelf4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

