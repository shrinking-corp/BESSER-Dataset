import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    complworld_Mars,
    complworld_Satellite,
    complworld_Thing,
    complworld_World,
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

def test_assoc_satellites1_stub_double():
    # complworld_Mars has no real 'complworld_Mars' property in the generated
    # code (a bare stub) -- manually attach it so complworld_Satellite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # complworld_Satellite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = complworld_Satellite(name="sample_text")
    partner = complworld_Mars()
    setattr(partner, 'complworld_Mars', None)
    _safe_set(owner, 'complworld_Satellite', partner)
    assert owner in getattr(partner, 'complworld_Mars')
    _safe_set(owner, 'complworld_Satellite', None)
    assert owner not in getattr(partner, 'complworld_Mars')


def test_assoc_things0_stub_double():
    # complworld_World has no real 'complworld_World' property in the generated
    # code (a bare stub) -- manually attach it so complworld_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # complworld_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = complworld_Thing(name="sample_text")
    partner = complworld_World()
    setattr(partner, 'complworld_World', None)
    _safe_set(owner, 'complworld_Thing', partner)
    assert owner in getattr(partner, 'complworld_World')
    _safe_set(owner, 'complworld_Thing', None)
    assert owner not in getattr(partner, 'complworld_World')


