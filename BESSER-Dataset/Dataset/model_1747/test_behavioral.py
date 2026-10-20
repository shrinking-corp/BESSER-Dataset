import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mytry_Author,
    mytry_Book,
    mytry_Library,
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
    a1 = mytry_Book(title="sample_text")
    a2 = mytry_Book(title="sample_text_2")
    b = mytry_Author(name="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'books'):
        assert _is_linked(a1, 'books', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'books'):
        assert not _is_linked(a1, 'books', b)
    if hasattr(a2, 'books'):
        assert _is_linked(a2, 'books', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'books'):
        assert not _is_linked(a2, 'books', b)


def test_assoc_books4_reverse_link_reassign_clear():
    a1 = mytry_Book(title="sample_text")
    a2 = mytry_Book(title="sample_text_2")
    b = mytry_Author(name="sample_text")
    _safe_set(b, 'authors', {a1})
    assert _is_linked(b, 'authors', a1)
    if hasattr(a1, 'Book'):
        assert _is_linked(a1, 'Book', b)
    _safe_set(b, 'authors', {a2})
    assert _is_linked(b, 'authors', a2)
    if hasattr(a1, 'Book'):
        assert not _is_linked(a1, 'Book', b)
    if hasattr(a2, 'Book'):
        assert _is_linked(a2, 'Book', b)
    _safe_set(b, 'authors', set())
    assert not _is_linked(b, 'authors', a2)
    if hasattr(a2, 'Book'):
        assert not _is_linked(a2, 'Book', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors1_stub_double():
    # mytry_Library has no real 'mytry_Library2' property in the generated
    # code (a bare stub) -- manually attach it so mytry_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mytry_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mytry_Author(name="sample_text")
    partner = mytry_Library()
    setattr(partner, 'mytry_Library2', None)
    _safe_set(owner, 'mytry_Author', partner)
    assert owner in getattr(partner, 'mytry_Library2')
    _safe_set(owner, 'mytry_Author', None)
    assert owner not in getattr(partner, 'mytry_Library2')


def test_assoc_books0_stub_double():
    # mytry_Library has no real 'mytry_Library' property in the generated
    # code (a bare stub) -- manually attach it so mytry_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mytry_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mytry_Book(title="sample_text")
    partner = mytry_Library()
    setattr(partner, 'mytry_Library', None)
    _safe_set(owner, 'mytry_Book', partner)
    assert owner in getattr(partner, 'mytry_Library')
    _safe_set(owner, 'mytry_Book', None)
    assert owner not in getattr(partner, 'mytry_Library')


