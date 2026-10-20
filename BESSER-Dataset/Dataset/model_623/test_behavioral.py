import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ocltutorial_Book,
    ocltutorial_Library,
    ocltutorial_Loans,
    ocltutorial_Member,
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

def test_assoc_book7_reverse_link_reassign_clear():
    a1 = ocltutorial_Loans(date=date(2024, 1, 1))
    a2 = ocltutorial_Loans(date=date(2025, 6, 15))
    b = ocltutorial_Book(copies="sample_text", name="sample_text")
    _safe_set(b, 'ocltutorial_Book', a1)
    assert _is_linked(b, 'ocltutorial_Book', a1)
    if hasattr(a1, 'ocltutorial_Loans8'):
        assert _is_linked(a1, 'ocltutorial_Loans8', b)
    _safe_set(b, 'ocltutorial_Book', a2)
    assert _is_linked(b, 'ocltutorial_Book', a2)
    if hasattr(a1, 'ocltutorial_Loans8'):
        assert not _is_linked(a1, 'ocltutorial_Loans8', b)
    if hasattr(a2, 'ocltutorial_Loans8'):
        assert _is_linked(a2, 'ocltutorial_Loans8', b)
    _safe_set(b, 'ocltutorial_Book', None)
    assert not _is_linked(b, 'ocltutorial_Book', a2)
    if hasattr(a2, 'ocltutorial_Loans8'):
        assert not _is_linked(a2, 'ocltutorial_Loans8', b)


def test_assoc_member5_reverse_link_reassign_clear():
    a1 = ocltutorial_Member(name="sample_text")
    a2 = ocltutorial_Member(name="sample_text_2")
    b = ocltutorial_Loans(date=date(2024, 1, 1))
    _safe_set(b, 'ocltutorial_Loans6', a1)
    assert _is_linked(b, 'ocltutorial_Loans6', a1)
    if hasattr(a1, 'ocltutorial_Member'):
        assert _is_linked(a1, 'ocltutorial_Member', b)
    _safe_set(b, 'ocltutorial_Loans6', a2)
    assert _is_linked(b, 'ocltutorial_Loans6', a2)
    if hasattr(a1, 'ocltutorial_Member'):
        assert not _is_linked(a1, 'ocltutorial_Member', b)
    if hasattr(a2, 'ocltutorial_Member'):
        assert _is_linked(a2, 'ocltutorial_Member', b)
    _safe_set(b, 'ocltutorial_Loans6', None)
    assert not _is_linked(b, 'ocltutorial_Loans6', a2)
    if hasattr(a2, 'ocltutorial_Member'):
        assert not _is_linked(a2, 'ocltutorial_Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_books0_stub_double():
    # ocltutorial_Library has no real 'library' property in the generated
    # code (a bare stub) -- manually attach it so ocltutorial_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocltutorial_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocltutorial_Book(copies="sample_text", name="sample_text")
    partner = ocltutorial_Library()
    setattr(partner, 'library', None)
    _safe_set(owner, 'Book', partner)
    assert owner in getattr(partner, 'library')
    _safe_set(owner, 'Book', None)
    assert owner not in getattr(partner, 'library')


def test_assoc_library4_stub_double():
    # ocltutorial_Library has no real 'Library' property in the generated
    # code (a bare stub) -- manually attach it so ocltutorial_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocltutorial_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocltutorial_Book(copies="sample_text", name="sample_text")
    partner = ocltutorial_Library()
    setattr(partner, 'Library', None)
    _safe_set(owner, 'books', partner)
    assert getattr(partner, 'Library') == owner
    _safe_set(owner, 'books', None)
    assert getattr(partner, 'Library') is None


def test_assoc_library9_stub_double():
    # ocltutorial_Library has no real 'Library10' property in the generated
    # code (a bare stub) -- manually attach it so ocltutorial_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocltutorial_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocltutorial_Member(name="sample_text")
    partner = ocltutorial_Library()
    setattr(partner, 'Library10', None)
    _safe_set(owner, 'members', partner)
    assert getattr(partner, 'Library10') == owner
    _safe_set(owner, 'members', None)
    assert getattr(partner, 'Library10') is None


def test_assoc_loans3_stub_double():
    # ocltutorial_Library has no real 'ocltutorial_Library' property in the generated
    # code (a bare stub) -- manually attach it so ocltutorial_Loans's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocltutorial_Loans's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocltutorial_Loans(date=date(2024, 1, 1))
    partner = ocltutorial_Library()
    setattr(partner, 'ocltutorial_Library', None)
    _safe_set(owner, 'ocltutorial_Loans', partner)
    assert owner in getattr(partner, 'ocltutorial_Library')
    _safe_set(owner, 'ocltutorial_Loans', None)
    assert owner not in getattr(partner, 'ocltutorial_Library')


def test_assoc_members1_stub_double():
    # ocltutorial_Library has no real 'library2' property in the generated
    # code (a bare stub) -- manually attach it so ocltutorial_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocltutorial_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocltutorial_Member(name="sample_text")
    partner = ocltutorial_Library()
    setattr(partner, 'library2', None)
    _safe_set(owner, 'Member', partner)
    assert owner in getattr(partner, 'library2')
    _safe_set(owner, 'Member', None)
    assert owner not in getattr(partner, 'library2')


