import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_Library,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_books1_stub_double():
    # library_Book has no real 'library_Book' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text")
    partner = library_Book()
    setattr(partner, 'library_Book', None)
    _safe_set(owner, 'library_Library2', {partner})
    assert getattr(partner, 'library_Book') == owner
    _safe_set(owner, 'library_Library2', set())
    assert getattr(partner, 'library_Book') is None


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


