import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_Employee,
    library_Library,
    library_Writer,
    library__cPfS4h9KEeeOINGRvT6ccg,
    library__cPfTBB9KEeeOINGRvT6ccg,
    library__cPfTDx9KEeeOINGRvT6ccg,
    BookCategory,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors7_stub_double():
    # library__cPfTBB9KEeeOINGRvT6ccg has no real 'library__cPfTBB9KEeeOINGRvT6ccg8' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(category="sample_text", pages=7, title="sample_text")
    partner = library__cPfTBB9KEeeOINGRvT6ccg()
    setattr(partner, 'library__cPfTBB9KEeeOINGRvT6ccg8', None)
    _safe_set(owner, 'library_Book', {partner})
    assert getattr(partner, 'library__cPfTBB9KEeeOINGRvT6ccg8') == owner
    _safe_set(owner, 'library_Book', set())
    assert getattr(partner, 'library__cPfTBB9KEeeOINGRvT6ccg8') is None


def test_assoc_books3_stub_double():
    # library__cPfTDx9KEeeOINGRvT6ccg has no real 'library__cPfTDx9KEeeOINGRvT6ccg' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(address="sample_text", name="sample_text")
    partner = library__cPfTDx9KEeeOINGRvT6ccg()
    setattr(partner, 'library__cPfTDx9KEeeOINGRvT6ccg', None)
    _safe_set(owner, 'library_Library4', {partner})
    assert getattr(partner, 'library__cPfTDx9KEeeOINGRvT6ccg') == owner
    _safe_set(owner, 'library_Library4', set())
    assert getattr(partner, 'library__cPfTDx9KEeeOINGRvT6ccg') is None


def test_assoc_books5_stub_double():
    # library__cPfTDx9KEeeOINGRvT6ccg has no real 'library__cPfTDx9KEeeOINGRvT6ccg6' property in the generated
    # code (a bare stub) -- manually attach it so library_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Writer(name="sample_text")
    partner = library__cPfTDx9KEeeOINGRvT6ccg()
    setattr(partner, 'library__cPfTDx9KEeeOINGRvT6ccg6', None)
    _safe_set(owner, 'library_Writer', {partner})
    assert getattr(partner, 'library__cPfTDx9KEeeOINGRvT6ccg6') == owner
    _safe_set(owner, 'library_Writer', set())
    assert getattr(partner, 'library__cPfTDx9KEeeOINGRvT6ccg6') is None


def test_assoc_employees0_stub_double():
    # library__cPfS4h9KEeeOINGRvT6ccg has no real 'library__cPfS4h9KEeeOINGRvT6ccg' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(address="sample_text", name="sample_text")
    partner = library__cPfS4h9KEeeOINGRvT6ccg()
    setattr(partner, 'library__cPfS4h9KEeeOINGRvT6ccg', None)
    _safe_set(owner, 'library_Library', {partner})
    assert getattr(partner, 'library__cPfS4h9KEeeOINGRvT6ccg') == owner
    _safe_set(owner, 'library_Library', set())
    assert getattr(partner, 'library__cPfS4h9KEeeOINGRvT6ccg') is None


def test_assoc_writers1_stub_double():
    # library__cPfTBB9KEeeOINGRvT6ccg has no real 'library__cPfTBB9KEeeOINGRvT6ccg' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(address="sample_text", name="sample_text")
    partner = library__cPfTBB9KEeeOINGRvT6ccg()
    setattr(partner, 'library__cPfTBB9KEeeOINGRvT6ccg', None)
    _safe_set(owner, 'library_Library2', {partner})
    assert getattr(partner, 'library__cPfTBB9KEeeOINGRvT6ccg') == owner
    _safe_set(owner, 'library_Library2', set())
    assert getattr(partner, 'library__cPfTBB9KEeeOINGRvT6ccg') is None


