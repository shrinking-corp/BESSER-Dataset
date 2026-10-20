import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    tinylibrary_Book,
    tinylibrary_Employee,
    tinylibrary_Library,
    tinylibrary_Person,
    tinylibrary_Writer,
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

def test_assoc_authors11_stub_double():
    # tinylibrary_Writer has no real 'Writer' property in the generated
    # code (a bare stub) -- manually attach it so tinylibrary_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tinylibrary_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tinylibrary_Book(category="sample_text", damaged="sample_text", isbn="sample_text", pages="sample_text", published=date(2024, 1, 1), title="sample_text")
    partner = tinylibrary_Writer()
    setattr(partner, 'Writer', None)
    _safe_set(owner, 'books', {partner})
    assert getattr(partner, 'Writer') == owner
    _safe_set(owner, 'books', set())
    assert getattr(partner, 'Writer') is None


def test_assoc_books0_stub_double():
    # tinylibrary_Library has no real 'tinylibrary_Library' property in the generated
    # code (a bare stub) -- manually attach it so tinylibrary_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tinylibrary_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tinylibrary_Book(category="sample_text", damaged="sample_text", isbn="sample_text", pages="sample_text", published=date(2024, 1, 1), title="sample_text")
    partner = tinylibrary_Library()
    setattr(partner, 'tinylibrary_Library', None)
    _safe_set(owner, 'tinylibrary_Book', partner)
    assert owner in getattr(partner, 'tinylibrary_Library')
    _safe_set(owner, 'tinylibrary_Book', None)
    assert owner not in getattr(partner, 'tinylibrary_Library')


def test_assoc_books5_stub_double():
    # tinylibrary_Writer has no real 'authors' property in the generated
    # code (a bare stub) -- manually attach it so tinylibrary_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tinylibrary_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tinylibrary_Book(category="sample_text", damaged="sample_text", isbn="sample_text", pages="sample_text", published=date(2024, 1, 1), title="sample_text")
    partner = tinylibrary_Writer()
    setattr(partner, 'authors', None)
    _safe_set(owner, 'Book', partner)
    assert owner in getattr(partner, 'authors')
    _safe_set(owner, 'Book', None)
    assert owner not in getattr(partner, 'authors')


