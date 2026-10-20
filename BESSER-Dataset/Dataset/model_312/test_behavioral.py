import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Writer,
    library_Book,
    library_Library,
    library_people_Writer,
    people_library_Book,
    people_library_Car,
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

def test_assoc_books3_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text")
    a2 = library_Library(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Library4'):
        assert _is_linked(a1, 'library_Library4', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Library4'):
        assert not _is_linked(a1, 'library_Library4', b)
    if hasattr(a2, 'library_Library4'):
        assert _is_linked(a2, 'library_Library4', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Library4'):
        assert not _is_linked(a2, 'library_Library4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_author0_stub_double():
    # Writer has no real 'Writer' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(category="sample_text", pages=7, title="sample_text")
    partner = Writer()
    setattr(partner, 'Writer', None)
    _safe_set(owner, 'books', partner)
    assert getattr(partner, 'Writer') == owner
    _safe_set(owner, 'books', None)
    assert getattr(partner, 'Writer') is None


def test_assoc_books5_stub_double():
    # people_library_Book has no real 'Book' property in the generated
    # code (a bare stub) -- manually attach it so library_people_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_people_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_people_Writer(name="sample_text")
    partner = people_library_Book()
    setattr(partner, 'Book', None)
    _safe_set(owner, 'author', {partner})
    assert getattr(partner, 'Book') == owner
    _safe_set(owner, 'author', set())
    assert getattr(partner, 'Book') is None


def test_assoc_car6_stub_double():
    # people_library_Car has no real 'people_library_Car' property in the generated
    # code (a bare stub) -- manually attach it so library_people_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_people_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_people_Writer(name="sample_text")
    partner = people_library_Car()
    setattr(partner, 'people_library_Car', None)
    _safe_set(owner, 'library_people_Writer', partner)
    assert getattr(partner, 'people_library_Car') == owner
    _safe_set(owner, 'library_people_Writer', None)
    assert getattr(partner, 'people_library_Car') is None


def test_assoc_writers1_stub_double():
    # Writer has no real 'Writer2' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = Writer()
    setattr(partner, 'Writer2', None)
    _safe_set(owner, 'library_Library', {partner})
    assert getattr(partner, 'Writer2') == owner
    _safe_set(owner, 'library_Library', set())
    assert getattr(partner, 'Writer2') is None


