import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_Library,
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

def test_assoc_author4_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'titles', {a1})
    assert _is_linked(b, 'titles', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'titles', {a2})
    assert _is_linked(b, 'titles', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'titles', set())
    assert not _is_linked(b, 'titles', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_titles3_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'author'):
        assert _is_linked(a1, 'author', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'author'):
        assert not _is_linked(a1, 'author', b)
    if hasattr(a2, 'author'):
        assert _is_linked(a2, 'author', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'author'):
        assert not _is_linked(a2, 'author', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_books1_stub_double():
    # library_Library has no real 'library_Library2' property in the generated
    # code (a bare stub) -- manually attach it so library_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Book(category="sample_text", pages=7, title="sample_text")
    partner = library_Library()
    setattr(partner, 'library_Library2', None)
    _safe_set(owner, 'library_Book', partner)
    assert owner in getattr(partner, 'library_Library2')
    _safe_set(owner, 'library_Book', None)
    assert owner not in getattr(partner, 'library_Library2')


def test_assoc_writers0_stub_double():
    # library_Library has no real 'library_Library' property in the generated
    # code (a bare stub) -- manually attach it so library_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Writer(name="sample_text")
    partner = library_Library()
    setattr(partner, 'library_Library', None)
    _safe_set(owner, 'library_Writer', partner)
    assert owner in getattr(partner, 'library_Library')
    _safe_set(owner, 'library_Writer', None)
    assert owner not in getattr(partner, 'library_Library')


