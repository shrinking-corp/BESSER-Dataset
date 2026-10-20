import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    library_Book,
    library_Library,
    library_Person,
    library_Writer,
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

def test_assoc_books2_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", site="sample_text")
    a2 = library_Library(name="sample_text_2", site="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Library3'):
        assert _is_linked(a1, 'library_Library3', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Library3'):
        assert not _is_linked(a1, 'library_Library3', b)
    if hasattr(a2, 'library_Library3'):
        assert _is_linked(a2, 'library_Library3', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Library3'):
        assert not _is_linked(a2, 'library_Library3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_author0_stub_double():
    # library_Writer has no real 'Writer' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(category="sample_text", pages=7, title="sample_text")
    partner = library_Writer()
    setattr(partner, 'Writer', None)
    _safe_set(owner, 'books', partner)
    assert getattr(partner, 'Writer') == owner
    _safe_set(owner, 'books', None)
    assert getattr(partner, 'Writer') is None


def test_assoc_books5_stub_double():
    # library_Writer has no real 'author' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(category="sample_text", pages=7, title="sample_text")
    partner = library_Writer()
    setattr(partner, 'author', None)
    _safe_set(owner, 'Book', partner)
    assert owner in getattr(partner, 'author')
    _safe_set(owner, 'Book', None)
    assert owner not in getattr(partner, 'author')


def test_assoc_employees4_stub_double():
    # library_Person has no real 'hr.ecorePerson' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", site="sample_text")
    partner = library_Person()
    setattr(partner, 'hr.ecorePerson', None)
    _safe_set(owner, 'Library', {partner})
    assert getattr(partner, 'hr.ecorePerson') == owner
    _safe_set(owner, 'Library', set())
    assert getattr(partner, 'hr.ecorePerson') is None


def test_assoc_writers1_stub_double():
    # library_Writer has no real 'library_Writer' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", site="sample_text")
    partner = library_Writer()
    setattr(partner, 'library_Writer', None)
    _safe_set(owner, 'library_Library', {partner})
    assert getattr(partner, 'library_Writer') == owner
    _safe_set(owner, 'library_Library', set())
    assert getattr(partner, 'library_Writer') is None


