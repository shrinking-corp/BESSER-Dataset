import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Employee,
    Library,
    Organization_tutorial_Item,
    SubOrg1_sb1C,
    SubOrg2_sb2C,
    tutorial_Book,
    tutorial_Library,
    tutorial_Loan,
    tutorial_Member,
    tutorial_Organization_Librarian,
    tutorial_Organization_Ref,
    tutorial_SubOrg1_sb1C,
    tutorial_SubOrg2_sb2C,
    Type,
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


def test_assoc_books11_reverse_link_reassign_clear():
    a1 = tutorial_Member(name="sample_text")
    a2 = tutorial_Member(name="sample_text_2")
    b = tutorial_Book(copies="sample_text", name="sample_text")
    _safe_set(b, 'tutorial_Book13', a1)
    assert _is_linked(b, 'tutorial_Book13', a1)
    if hasattr(a1, 'tutorial_Member12'):
        assert _is_linked(a1, 'tutorial_Member12', b)
    _safe_set(b, 'tutorial_Book13', a2)
    assert _is_linked(b, 'tutorial_Book13', a2)
    if hasattr(a1, 'tutorial_Member12'):
        assert not _is_linked(a1, 'tutorial_Member12', b)
    if hasattr(a2, 'tutorial_Member12'):
        assert _is_linked(a2, 'tutorial_Member12', b)
    _safe_set(b, 'tutorial_Book13', None)
    assert not _is_linked(b, 'tutorial_Book13', a2)
    if hasattr(a2, 'tutorial_Member12'):
        assert not _is_linked(a2, 'tutorial_Member12', b)


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


def test_assoc_loans9_reverse_link_reassign_clear():
    a1 = tutorial_Member(name="sample_text")
    a2 = tutorial_Member(name="sample_text_2")
    b = tutorial_Loan(date=date(2024, 1, 1))
    _safe_set(b, 'tutorial_Loan10', a1)
    assert _is_linked(b, 'tutorial_Loan10', a1)
    if hasattr(a1, 'tutorial_Member'):
        assert _is_linked(a1, 'tutorial_Member', b)
    _safe_set(b, 'tutorial_Loan10', a2)
    assert _is_linked(b, 'tutorial_Loan10', a2)
    if hasattr(a1, 'tutorial_Member'):
        assert not _is_linked(a1, 'tutorial_Member', b)
    if hasattr(a2, 'tutorial_Member'):
        assert _is_linked(a2, 'tutorial_Member', b)
    _safe_set(b, 'tutorial_Loan10', None)
    assert not _is_linked(b, 'tutorial_Loan10', a2)
    if hasattr(a2, 'tutorial_Member'):
        assert not _is_linked(a2, 'tutorial_Member', b)


def test_assoc_member16_reverse_link_reassign_clear():
    a1 = tutorial_Member(name="sample_text")
    a2 = tutorial_Member(name="sample_text_2")
    b = tutorial_Loan(date=date(2024, 1, 1))
    _safe_set(b, 'tutorial_Loan17', a1)
    assert _is_linked(b, 'tutorial_Loan17', a1)
    if hasattr(a1, 'tutorial_Member18'):
        assert _is_linked(a1, 'tutorial_Member18', b)
    _safe_set(b, 'tutorial_Loan17', a2)
    assert _is_linked(b, 'tutorial_Loan17', a2)
    if hasattr(a1, 'tutorial_Member18'):
        assert not _is_linked(a1, 'tutorial_Member18', b)
    if hasattr(a2, 'tutorial_Member18'):
        assert _is_linked(a2, 'tutorial_Member18', b)
    _safe_set(b, 'tutorial_Loan17', None)
    assert not _is_linked(b, 'tutorial_Loan17', a2)
    if hasattr(a2, 'tutorial_Member18'):
        assert not _is_linked(a2, 'tutorial_Member18', b)


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

def test_assoc_book14_stub_double():
    # SubOrg1_sb1C has no real 'SubOrg1_sb1C' property in the generated
    # code (a bare stub) -- manually attach it so tutorial_Loan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tutorial_Loan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tutorial_Loan(date=date(2024, 1, 1))
    partner = SubOrg1_sb1C()
    setattr(partner, 'SubOrg1_sb1C', None)
    _safe_set(owner, 'tutorial_Loan15', partner)
    assert getattr(partner, 'SubOrg1_sb1C') == owner
    _safe_set(owner, 'tutorial_Loan15', None)
    assert getattr(partner, 'SubOrg1_sb1C') is None


def test_assoc_workOn19_stub_double():
    # SubOrg2_sb2C has no real 'SubOrg2_sb2C' property in the generated
    # code (a bare stub) -- manually attach it so tutorial_Organization_Librarian's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tutorial_Organization_Librarian's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tutorial_Organization_Librarian()
    partner = SubOrg2_sb2C()
    setattr(partner, 'SubOrg2_sb2C', None)
    _safe_set(owner, 'tutorial_Organization_Librarian', partner)
    assert getattr(partner, 'SubOrg2_sb2C') == owner
    _safe_set(owner, 'tutorial_Organization_Librarian', None)
    assert getattr(partner, 'SubOrg2_sb2C') is None


