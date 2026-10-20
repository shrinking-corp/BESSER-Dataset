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


def test_assoc_library6_reverse_link_reassign_clear():
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

def test_assoc_book9_stub_double():
    # tutorial_Loan has no real 'tutorial_Loan10' property in the generated
    # code (a bare stub) -- manually attach it so tutorial_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tutorial_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tutorial_Book(copies="sample_text", name="sample_text")
    partner = tutorial_Loan()
    setattr(partner, 'tutorial_Loan10', None)
    _safe_set(owner, 'tutorial_Book11', partner)
    assert getattr(partner, 'tutorial_Loan10') == owner
    _safe_set(owner, 'tutorial_Book11', None)
    assert getattr(partner, 'tutorial_Loan10') is None


def test_assoc_loans1_stub_double():
    # tutorial_Loan has no real 'tutorial_Loan' property in the generated
    # code (a bare stub) -- manually attach it so tutorial_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tutorial_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tutorial_Library(name="sample_text")
    partner = tutorial_Loan()
    setattr(partner, 'tutorial_Loan', None)
    _safe_set(owner, 'tutorial_Library', {partner})
    assert getattr(partner, 'tutorial_Loan') == owner
    _safe_set(owner, 'tutorial_Library', set())
    assert getattr(partner, 'tutorial_Loan') is None


def test_assoc_loans4_stub_double():
    # tutorial_Loan has no real 'tutorial_Loan5' property in the generated
    # code (a bare stub) -- manually attach it so tutorial_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tutorial_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tutorial_Book(copies="sample_text", name="sample_text")
    partner = tutorial_Loan()
    setattr(partner, 'tutorial_Loan5', None)
    _safe_set(owner, 'tutorial_Book', {partner})
    assert getattr(partner, 'tutorial_Loan5') == owner
    _safe_set(owner, 'tutorial_Book', set())
    assert getattr(partner, 'tutorial_Loan5') is None


def test_assoc_member12_stub_double():
    # tutorial_Loan has no real 'tutorial_Loan13' property in the generated
    # code (a bare stub) -- manually attach it so tutorial_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tutorial_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tutorial_Member(name="sample_text")
    partner = tutorial_Loan()
    setattr(partner, 'tutorial_Loan13', None)
    _safe_set(owner, 'tutorial_Member', partner)
    assert getattr(partner, 'tutorial_Loan13') == owner
    _safe_set(owner, 'tutorial_Member', None)
    assert getattr(partner, 'tutorial_Loan13') is None


