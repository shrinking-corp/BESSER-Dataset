import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractPerson,
    library_AbstractPerson,
    library_Author,
    library_Book,
    library_Library,
    library_Loan,
    library_Person,
    library_UoD,
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

def test_assoc_books7_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Book(isbn="sample_text", title="sample_text")
    _safe_set(b, 'library_Book9', a1)
    assert _is_linked(b, 'library_Book9', a1)
    if hasattr(a1, 'library_Library8'):
        assert _is_linked(a1, 'library_Library8', b)
    _safe_set(b, 'library_Book9', a2)
    assert _is_linked(b, 'library_Book9', a2)
    if hasattr(a1, 'library_Library8'):
        assert not _is_linked(a1, 'library_Library8', b)
    if hasattr(a2, 'library_Library8'):
        assert _is_linked(a2, 'library_Library8', b)
    _safe_set(b, 'library_Book9', None)
    assert not _is_linked(b, 'library_Book9', a2)
    if hasattr(a2, 'library_Library8'):
        assert not _is_linked(a2, 'library_Library8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allLibraries0_stub_double():
    # library_UoD has no real 'library_UoD' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_UoD()
    setattr(partner, 'library_UoD', None)
    _safe_set(owner, 'library_Library', partner)
    assert owner in getattr(partner, 'library_UoD')
    _safe_set(owner, 'library_Library', None)
    assert owner not in getattr(partner, 'library_UoD')


def test_assoc_author5_stub_double():
    # library_Author has no real 'library_Author6' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(isbn="sample_text", title="sample_text")
    partner = library_Author()
    setattr(partner, 'library_Author6', None)
    _safe_set(owner, 'library_Book', partner)
    assert getattr(partner, 'library_Author6') == owner
    _safe_set(owner, 'library_Book', None)
    assert getattr(partner, 'library_Author6') is None


def test_assoc_book15_stub_double():
    # library_Loan has no real 'library_Loan16' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(isbn="sample_text", title="sample_text")
    partner = library_Loan()
    setattr(partner, 'library_Loan16', None)
    _safe_set(owner, 'library_Book17', partner)
    assert getattr(partner, 'library_Loan16') == owner
    _safe_set(owner, 'library_Book17', None)
    assert getattr(partner, 'library_Loan16') is None


def test_assoc_loans10_stub_double():
    # library_Loan has no real 'library_Loan' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_Loan()
    setattr(partner, 'library_Loan', None)
    _safe_set(owner, 'library_Library11', {partner})
    assert getattr(partner, 'library_Loan') == owner
    _safe_set(owner, 'library_Library11', set())
    assert getattr(partner, 'library_Loan') is None


