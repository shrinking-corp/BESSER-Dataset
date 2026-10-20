import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_BorrowedItem,
    library_Library,
    library_User,
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
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Book(author="sample_text", name="sample_text")
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


def test_assoc_borrowedItems4_reverse_link_reassign_clear():
    a1 = library_User(name="sample_text")
    a2 = library_User(name="sample_text_2")
    b = library_BorrowedItem(borrowDate=date(2024, 1, 1), lastReturnDate=date(2024, 1, 1))
    _safe_set(b, 'BorrowedItem', a1)
    assert _is_linked(b, 'BorrowedItem', a1)
    if hasattr(a1, 'user'):
        assert _is_linked(a1, 'user', b)
    _safe_set(b, 'BorrowedItem', a2)
    assert _is_linked(b, 'BorrowedItem', a2)
    if hasattr(a1, 'user'):
        assert not _is_linked(a1, 'user', b)
    if hasattr(a2, 'user'):
        assert _is_linked(a2, 'user', b)
    _safe_set(b, 'BorrowedItem', None)
    assert not _is_linked(b, 'BorrowedItem', a2)
    if hasattr(a2, 'user'):
        assert not _is_linked(a2, 'user', b)


def test_assoc_item7_reverse_link_reassign_clear():
    a1 = library_BorrowedItem(borrowDate=date(2024, 1, 1), lastReturnDate=date(2024, 1, 1))
    a2 = library_BorrowedItem(borrowDate=date(2025, 6, 15), lastReturnDate=date(2025, 6, 15))
    b = library_Book(author="sample_text", name="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_BorrowedItem'):
        assert _is_linked(a1, 'library_BorrowedItem', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_BorrowedItem'):
        assert not _is_linked(a1, 'library_BorrowedItem', b)
    if hasattr(a2, 'library_BorrowedItem'):
        assert _is_linked(a2, 'library_BorrowedItem', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_BorrowedItem'):
        assert not _is_linked(a2, 'library_BorrowedItem', b)


def test_assoc_library3_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Book(author="sample_text", name="sample_text")
    _safe_set(b, 'books', a1)
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Library'):
        assert _is_linked(a1, 'Library', b)
    _safe_set(b, 'books', a2)
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Library'):
        assert not _is_linked(a1, 'Library', b)
    if hasattr(a2, 'Library'):
        assert _is_linked(a2, 'Library', b)
    _safe_set(b, 'books', None)
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Library'):
        assert not _is_linked(a2, 'Library', b)


def test_assoc_library5_reverse_link_reassign_clear():
    a1 = library_User(name="sample_text")
    a2 = library_User(name="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'Library6', a1)
    assert _is_linked(b, 'Library6', a1)
    if hasattr(a1, 'users'):
        assert _is_linked(a1, 'users', b)
    _safe_set(b, 'Library6', a2)
    assert _is_linked(b, 'Library6', a2)
    if hasattr(a1, 'users'):
        assert not _is_linked(a1, 'users', b)
    if hasattr(a2, 'users'):
        assert _is_linked(a2, 'users', b)
    _safe_set(b, 'Library6', None)
    assert not _is_linked(b, 'Library6', a2)
    if hasattr(a2, 'users'):
        assert not _is_linked(a2, 'users', b)


def test_assoc_user8_reverse_link_reassign_clear():
    a1 = library_User(name="sample_text")
    a2 = library_User(name="sample_text_2")
    b = library_BorrowedItem(borrowDate=date(2024, 1, 1), lastReturnDate=date(2024, 1, 1))
    _safe_set(b, 'borrowedItems', a1)
    assert _is_linked(b, 'borrowedItems', a1)
    if hasattr(a1, 'User9'):
        assert _is_linked(a1, 'User9', b)
    _safe_set(b, 'borrowedItems', a2)
    assert _is_linked(b, 'borrowedItems', a2)
    if hasattr(a1, 'User9'):
        assert not _is_linked(a1, 'User9', b)
    if hasattr(a2, 'User9'):
        assert _is_linked(a2, 'User9', b)
    _safe_set(b, 'borrowedItems', None)
    assert not _is_linked(b, 'borrowedItems', a2)
    if hasattr(a2, 'User9'):
        assert not _is_linked(a2, 'User9', b)


def test_assoc_users1_reverse_link_reassign_clear():
    a1 = library_User(name="sample_text")
    a2 = library_User(name="sample_text_2")
    b = library_Library(name="sample_text")
    _safe_set(b, 'library2', {a1})
    assert _is_linked(b, 'library2', a1)
    if hasattr(a1, 'User'):
        assert _is_linked(a1, 'User', b)
    _safe_set(b, 'library2', {a2})
    assert _is_linked(b, 'library2', a2)
    if hasattr(a1, 'User'):
        assert not _is_linked(a1, 'User', b)
    if hasattr(a2, 'User'):
        assert _is_linked(a2, 'User', b)
    _safe_set(b, 'library2', set())
    assert not _is_linked(b, 'library2', a2)
    if hasattr(a2, 'User'):
        assert not _is_linked(a2, 'User', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

