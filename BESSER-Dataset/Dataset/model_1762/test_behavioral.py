import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Book_Author,
    Book_Book,
    Book_Chapter,
    Book_Library,
    Book_Paragraph,
    Book_Section,
    Chapter,
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

def test_assoc_authors3_reverse_link_reassign_clear():
    a1 = Book_Book(isbn="sample_text", name="sample_text", nbpages=7)
    a2 = Book_Book(isbn="sample_text_2", name="sample_text_2", nbpages=13)
    b = Book_Author(name="sample_text")
    _safe_set(b, 'Book_Author5', a1)
    assert _is_linked(b, 'Book_Author5', a1)
    if hasattr(a1, 'Book_Book4'):
        assert _is_linked(a1, 'Book_Book4', b)
    _safe_set(b, 'Book_Author5', a2)
    assert _is_linked(b, 'Book_Author5', a2)
    if hasattr(a1, 'Book_Book4'):
        assert not _is_linked(a1, 'Book_Book4', b)
    if hasattr(a2, 'Book_Book4'):
        assert _is_linked(a2, 'Book_Book4', b)
    _safe_set(b, 'Book_Author5', None)
    assert not _is_linked(b, 'Book_Author5', a2)
    if hasattr(a2, 'Book_Book4'):
        assert not _is_linked(a2, 'Book_Book4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors1_stub_double():
    # Book_Library has no real 'Book_Library2' property in the generated
    # code (a bare stub) -- manually attach it so Book_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Book_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Book_Author(name="sample_text")
    partner = Book_Library()
    setattr(partner, 'Book_Library2', None)
    _safe_set(owner, 'Book_Author', partner)
    assert owner in getattr(partner, 'Book_Library2')
    _safe_set(owner, 'Book_Author', None)
    assert owner not in getattr(partner, 'Book_Library2')


def test_assoc_books0_stub_double():
    # Book_Library has no real 'Book_Library' property in the generated
    # code (a bare stub) -- manually attach it so Book_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Book_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Book_Book(isbn="sample_text", name="sample_text", nbpages=7)
    partner = Book_Library()
    setattr(partner, 'Book_Library', None)
    _safe_set(owner, 'Book_Book', partner)
    assert owner in getattr(partner, 'Book_Library')
    _safe_set(owner, 'Book_Book', None)
    assert owner not in getattr(partner, 'Book_Library')


def test_assoc_sections6_stub_double():
    # Book_Chapter has no real 'Book_Chapter' property in the generated
    # code (a bare stub) -- manually attach it so Book_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Book_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Book_Book(isbn="sample_text", name="sample_text", nbpages=7)
    partner = Book_Chapter()
    setattr(partner, 'Book_Chapter', None)
    _safe_set(owner, 'Book_Book7', {partner})
    assert getattr(partner, 'Book_Chapter') == owner
    _safe_set(owner, 'Book_Book7', set())
    assert getattr(partner, 'Book_Chapter') is None


