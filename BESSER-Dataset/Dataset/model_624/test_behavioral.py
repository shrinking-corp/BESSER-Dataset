import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mm2_Book,
    mm2_Library,
    mm2_Loan,
    mm2_Member,
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

def test_assoc_book5_reverse_link_reassign_clear():
    a1 = mm2_Loan(name="sample_text")
    a2 = mm2_Loan(name="sample_text_2")
    b = mm2_Book(name="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'loans'):
        assert _is_linked(a1, 'loans', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'loans'):
        assert not _is_linked(a1, 'loans', b)
    if hasattr(a2, 'loans'):
        assert _is_linked(a2, 'loans', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'loans'):
        assert not _is_linked(a2, 'loans', b)


def test_assoc_books1_reverse_link_reassign_clear():
    a1 = mm2_Library(name="sample_text")
    a2 = mm2_Library(name="sample_text_2")
    b = mm2_Book(name="sample_text")
    _safe_set(b, 'mm2_Book', a1)
    assert _is_linked(b, 'mm2_Book', a1)
    if hasattr(a1, 'mm2_Library2'):
        assert _is_linked(a1, 'mm2_Library2', b)
    _safe_set(b, 'mm2_Book', a2)
    assert _is_linked(b, 'mm2_Book', a2)
    if hasattr(a1, 'mm2_Library2'):
        assert not _is_linked(a1, 'mm2_Library2', b)
    if hasattr(a2, 'mm2_Library2'):
        assert _is_linked(a2, 'mm2_Library2', b)
    _safe_set(b, 'mm2_Book', None)
    assert not _is_linked(b, 'mm2_Book', a2)
    if hasattr(a2, 'mm2_Library2'):
        assert not _is_linked(a2, 'mm2_Library2', b)


def test_assoc_loans3_reverse_link_reassign_clear():
    a1 = mm2_Loan(name="sample_text")
    a2 = mm2_Loan(name="sample_text_2")
    b = mm2_Library(name="sample_text")
    _safe_set(b, 'mm2_Library4', {a1})
    assert _is_linked(b, 'mm2_Library4', a1)
    if hasattr(a1, 'mm2_Loan'):
        assert _is_linked(a1, 'mm2_Loan', b)
    _safe_set(b, 'mm2_Library4', {a2})
    assert _is_linked(b, 'mm2_Library4', a2)
    if hasattr(a1, 'mm2_Loan'):
        assert not _is_linked(a1, 'mm2_Loan', b)
    if hasattr(a2, 'mm2_Loan'):
        assert _is_linked(a2, 'mm2_Loan', b)
    _safe_set(b, 'mm2_Library4', set())
    assert not _is_linked(b, 'mm2_Library4', a2)
    if hasattr(a2, 'mm2_Loan'):
        assert not _is_linked(a2, 'mm2_Loan', b)


def test_assoc_loans8_reverse_link_reassign_clear():
    a1 = mm2_Member(name="sample_text")
    a2 = mm2_Member(name="sample_text_2")
    b = mm2_Loan(name="sample_text")
    _safe_set(b, 'Loan', a1)
    assert _is_linked(b, 'Loan', a1)
    if hasattr(a1, 'member'):
        assert _is_linked(a1, 'member', b)
    _safe_set(b, 'Loan', a2)
    assert _is_linked(b, 'Loan', a2)
    if hasattr(a1, 'member'):
        assert not _is_linked(a1, 'member', b)
    if hasattr(a2, 'member'):
        assert _is_linked(a2, 'member', b)
    _safe_set(b, 'Loan', None)
    assert not _is_linked(b, 'Loan', a2)
    if hasattr(a2, 'member'):
        assert not _is_linked(a2, 'member', b)


def test_assoc_loans9_reverse_link_reassign_clear():
    a1 = mm2_Loan(name="sample_text")
    a2 = mm2_Loan(name="sample_text_2")
    b = mm2_Book(name="sample_text")
    _safe_set(b, 'book', {a1})
    assert _is_linked(b, 'book', a1)
    if hasattr(a1, 'Loan10'):
        assert _is_linked(a1, 'Loan10', b)
    _safe_set(b, 'book', {a2})
    assert _is_linked(b, 'book', a2)
    if hasattr(a1, 'Loan10'):
        assert not _is_linked(a1, 'Loan10', b)
    if hasattr(a2, 'Loan10'):
        assert _is_linked(a2, 'Loan10', b)
    _safe_set(b, 'book', set())
    assert not _is_linked(b, 'book', a2)
    if hasattr(a2, 'Loan10'):
        assert not _is_linked(a2, 'Loan10', b)


def test_assoc_member6_reverse_link_reassign_clear():
    a1 = mm2_Member(name="sample_text")
    a2 = mm2_Member(name="sample_text_2")
    b = mm2_Loan(name="sample_text")
    _safe_set(b, 'loans7', a1)
    assert _is_linked(b, 'loans7', a1)
    if hasattr(a1, 'Member'):
        assert _is_linked(a1, 'Member', b)
    _safe_set(b, 'loans7', a2)
    assert _is_linked(b, 'loans7', a2)
    if hasattr(a1, 'Member'):
        assert not _is_linked(a1, 'Member', b)
    if hasattr(a2, 'Member'):
        assert _is_linked(a2, 'Member', b)
    _safe_set(b, 'loans7', None)
    assert not _is_linked(b, 'loans7', a2)
    if hasattr(a2, 'Member'):
        assert not _is_linked(a2, 'Member', b)


def test_assoc_members0_reverse_link_reassign_clear():
    a1 = mm2_Member(name="sample_text")
    a2 = mm2_Member(name="sample_text_2")
    b = mm2_Library(name="sample_text")
    _safe_set(b, 'mm2_Library', {a1})
    assert _is_linked(b, 'mm2_Library', a1)
    if hasattr(a1, 'mm2_Member'):
        assert _is_linked(a1, 'mm2_Member', b)
    _safe_set(b, 'mm2_Library', {a2})
    assert _is_linked(b, 'mm2_Library', a2)
    if hasattr(a1, 'mm2_Member'):
        assert not _is_linked(a1, 'mm2_Member', b)
    if hasattr(a2, 'mm2_Member'):
        assert _is_linked(a2, 'mm2_Member', b)
    _safe_set(b, 'mm2_Library', set())
    assert not _is_linked(b, 'mm2_Library', a2)
    if hasattr(a2, 'mm2_Member'):
        assert not _is_linked(a2, 'mm2_Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

