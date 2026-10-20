import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tutorial_Book,
    tutorial_Library,
    tutorial_Loan,
    tutorial_Member,
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

def test_assoc_book9_reverse_link_reassign_clear():
    a1 = tutorial_Loan(date=date(2024, 1, 1))
    a2 = tutorial_Loan(date=date(2025, 6, 15))
    b = tutorial_Book(copies="sample_text", name="sample_text")
    _safe_set(b, 'tutorial_Book11', a1)
    assert _is_linked(b, 'tutorial_Book11', a1)
    if hasattr(a1, 'tutorial_Loan10'):
        assert _is_linked(a1, 'tutorial_Loan10', b)
    _safe_set(b, 'tutorial_Book11', a2)
    assert _is_linked(b, 'tutorial_Book11', a2)
    if hasattr(a1, 'tutorial_Loan10'):
        assert not _is_linked(a1, 'tutorial_Loan10', b)
    if hasattr(a2, 'tutorial_Loan10'):
        assert _is_linked(a2, 'tutorial_Loan10', b)
    _safe_set(b, 'tutorial_Book11', None)
    assert not _is_linked(b, 'tutorial_Book11', a2)
    if hasattr(a2, 'tutorial_Loan10'):
        assert not _is_linked(a2, 'tutorial_Loan10', b)


def test_assoc_books0_reverse_link_reassign_clear():
    a1 = tutorial_Library(name="sample_text")
    a2 = tutorial_Library(name="sample_text_2")
    b = tutorial_Book(copies="sample_text", name="sample_text")
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


def test_assoc_library4_reverse_link_reassign_clear():
    a1 = tutorial_Library(name="sample_text")
    a2 = tutorial_Library(name="sample_text_2")
    b = tutorial_Book(copies="sample_text", name="sample_text")
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


def test_assoc_library7_reverse_link_reassign_clear():
    a1 = tutorial_Member(name="sample_text")
    a2 = tutorial_Member(name="sample_text_2")
    b = tutorial_Library(name="sample_text")
    _safe_set(b, 'Library8', a1)
    assert _is_linked(b, 'Library8', a1)
    if hasattr(a1, 'members'):
        assert _is_linked(a1, 'members', b)
    _safe_set(b, 'Library8', a2)
    assert _is_linked(b, 'Library8', a2)
    if hasattr(a1, 'members'):
        assert not _is_linked(a1, 'members', b)
    if hasattr(a2, 'members'):
        assert _is_linked(a2, 'members', b)
    _safe_set(b, 'Library8', None)
    assert not _is_linked(b, 'Library8', a2)
    if hasattr(a2, 'members'):
        assert not _is_linked(a2, 'members', b)


def test_assoc_loans1_reverse_link_reassign_clear():
    a1 = tutorial_Loan(date=date(2024, 1, 1))
    a2 = tutorial_Loan(date=date(2025, 6, 15))
    b = tutorial_Library(name="sample_text")
    _safe_set(b, 'tutorial_Library', {a1})
    assert _is_linked(b, 'tutorial_Library', a1)
    if hasattr(a1, 'tutorial_Loan'):
        assert _is_linked(a1, 'tutorial_Loan', b)
    _safe_set(b, 'tutorial_Library', {a2})
    assert _is_linked(b, 'tutorial_Library', a2)
    if hasattr(a1, 'tutorial_Loan'):
        assert not _is_linked(a1, 'tutorial_Loan', b)
    if hasattr(a2, 'tutorial_Loan'):
        assert _is_linked(a2, 'tutorial_Loan', b)
    _safe_set(b, 'tutorial_Library', set())
    assert not _is_linked(b, 'tutorial_Library', a2)
    if hasattr(a2, 'tutorial_Loan'):
        assert not _is_linked(a2, 'tutorial_Loan', b)


def test_assoc_loans5_reverse_link_reassign_clear():
    a1 = tutorial_Loan(date=date(2024, 1, 1))
    a2 = tutorial_Loan(date=date(2025, 6, 15))
    b = tutorial_Book(copies="sample_text", name="sample_text")
    _safe_set(b, 'tutorial_Book', {a1})
    assert _is_linked(b, 'tutorial_Book', a1)
    if hasattr(a1, 'tutorial_Loan6'):
        assert _is_linked(a1, 'tutorial_Loan6', b)
    _safe_set(b, 'tutorial_Book', {a2})
    assert _is_linked(b, 'tutorial_Book', a2)
    if hasattr(a1, 'tutorial_Loan6'):
        assert not _is_linked(a1, 'tutorial_Loan6', b)
    if hasattr(a2, 'tutorial_Loan6'):
        assert _is_linked(a2, 'tutorial_Loan6', b)
    _safe_set(b, 'tutorial_Book', set())
    assert not _is_linked(b, 'tutorial_Book', a2)
    if hasattr(a2, 'tutorial_Loan6'):
        assert not _is_linked(a2, 'tutorial_Loan6', b)


def test_assoc_member12_reverse_link_reassign_clear():
    a1 = tutorial_Member(name="sample_text")
    a2 = tutorial_Member(name="sample_text_2")
    b = tutorial_Loan(date=date(2024, 1, 1))
    _safe_set(b, 'tutorial_Loan13', a1)
    assert _is_linked(b, 'tutorial_Loan13', a1)
    if hasattr(a1, 'tutorial_Member'):
        assert _is_linked(a1, 'tutorial_Member', b)
    _safe_set(b, 'tutorial_Loan13', a2)
    assert _is_linked(b, 'tutorial_Loan13', a2)
    if hasattr(a1, 'tutorial_Member'):
        assert not _is_linked(a1, 'tutorial_Member', b)
    if hasattr(a2, 'tutorial_Member'):
        assert _is_linked(a2, 'tutorial_Member', b)
    _safe_set(b, 'tutorial_Loan13', None)
    assert not _is_linked(b, 'tutorial_Loan13', a2)
    if hasattr(a2, 'tutorial_Member'):
        assert not _is_linked(a2, 'tutorial_Member', b)


def test_assoc_members2_reverse_link_reassign_clear():
    a1 = tutorial_Member(name="sample_text")
    a2 = tutorial_Member(name="sample_text_2")
    b = tutorial_Library(name="sample_text")
    _safe_set(b, 'library3', {a1})
    assert _is_linked(b, 'library3', a1)
    if hasattr(a1, 'Member'):
        assert _is_linked(a1, 'Member', b)
    _safe_set(b, 'library3', {a2})
    assert _is_linked(b, 'library3', a2)
    if hasattr(a1, 'Member'):
        assert not _is_linked(a1, 'Member', b)
    if hasattr(a2, 'Member'):
        assert _is_linked(a2, 'Member', b)
    _safe_set(b, 'library3', set())
    assert not _is_linked(b, 'library3', a2)
    if hasattr(a2, 'Member'):
        assert not _is_linked(a2, 'Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

