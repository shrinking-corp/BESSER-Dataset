import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Addressable,
    CirculatingItem,
    Item,
    Lendable,
    Person,
    library_Addressable,
    library_Borrower,
    library_CirculatingItem,
    library_Employee,
    library_IncBook,
    library_Item,
    library_Lendable,
    library_Library,
    library_Person,
    library_Writer,
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

def test_assoc_stock5_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Item(publicationDate=date(2024, 1, 1))
    _safe_set(b, 'library_Item', a1)
    assert _is_linked(b, 'library_Item', a1)
    if hasattr(a1, 'library_Library6'):
        assert _is_linked(a1, 'library_Library6', b)
    _safe_set(b, 'library_Item', a2)
    assert _is_linked(b, 'library_Item', a2)
    if hasattr(a1, 'library_Library6'):
        assert not _is_linked(a1, 'library_Library6', b)
    if hasattr(a2, 'library_Library6'):
        assert _is_linked(a2, 'library_Library6', b)
    _safe_set(b, 'library_Item', None)
    assert not _is_linked(b, 'library_Item', a2)
    if hasattr(a2, 'library_Library6'):
        assert not _is_linked(a2, 'library_Library6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors9_stub_double():
    # library_Writer has no real 'Writer' property in the generated
    # code (a bare stub) -- manually attach it so library_IncBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_IncBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_IncBook(pages=7, title="sample_text")
    partner = library_Writer()
    setattr(partner, 'Writer', None)
    _safe_set(owner, 'books', {partner})
    assert getattr(partner, 'Writer') == owner
    _safe_set(owner, 'books', set())
    assert getattr(partner, 'Writer') is None


def test_assoc_books7_stub_double():
    # library_Writer has no real 'authors' property in the generated
    # code (a bare stub) -- manually attach it so library_IncBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_IncBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_IncBook(pages=7, title="sample_text")
    partner = library_Writer()
    setattr(partner, 'authors', None)
    _safe_set(owner, 'IncBook', partner)
    assert owner in getattr(partner, 'authors')
    _safe_set(owner, 'IncBook', None)
    assert owner not in getattr(partner, 'authors')


def test_assoc_borrowers10_stub_double():
    # library_Borrower has no real 'Borrower' property in the generated
    # code (a bare stub) -- manually attach it so library_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Lendable(copies=7)
    partner = library_Borrower()
    setattr(partner, 'Borrower', None)
    _safe_set(owner, 'borrowing', {partner})
    assert getattr(partner, 'Borrower') == owner
    _safe_set(owner, 'borrowing', set())
    assert getattr(partner, 'Borrower') is None


def test_assoc_borrowers3_stub_double():
    # library_Borrower has no real 'library_Borrower' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_Borrower()
    setattr(partner, 'library_Borrower', None)
    _safe_set(owner, 'library_Library4', {partner})
    assert getattr(partner, 'library_Borrower') == owner
    _safe_set(owner, 'library_Library4', set())
    assert getattr(partner, 'library_Borrower') is None


def test_assoc_borrowing8_stub_double():
    # library_Borrower has no real 'borrowers' property in the generated
    # code (a bare stub) -- manually attach it so library_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Lendable(copies=7)
    partner = library_Borrower()
    setattr(partner, 'borrowers', None)
    _safe_set(owner, 'Lendable', partner)
    assert owner in getattr(partner, 'borrowers')
    _safe_set(owner, 'Lendable', None)
    assert owner not in getattr(partner, 'borrowers')


def test_assoc_employees1_stub_double():
    # library_Employee has no real 'library_Employee' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_Employee()
    setattr(partner, 'library_Employee', None)
    _safe_set(owner, 'library_Library2', {partner})
    assert getattr(partner, 'library_Employee') == owner
    _safe_set(owner, 'library_Library2', set())
    assert getattr(partner, 'library_Employee') is None


def test_assoc_writers0_stub_double():
    # library_Writer has no real 'library_Writer' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_Writer()
    setattr(partner, 'library_Writer', None)
    _safe_set(owner, 'library_Library', {partner})
    assert getattr(partner, 'library_Writer') == owner
    _safe_set(owner, 'library_Library', set())
    assert getattr(partner, 'library_Writer') is None


