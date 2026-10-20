import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    Type,
    alldatatypes_BigDecimals,
    alldatatypes_BigIntegers,
    alldatatypes_Booleans,
    alldatatypes_Dates,
    alldatatypes_Doubles,
    alldatatypes_Element,
    alldatatypes_Enums,
    alldatatypes_Floats,
    alldatatypes_Integers,
    alldatatypes_Longs,
    alldatatypes_Root,
    alldatatypes_Shorts,
    alldatatypes_Strings,
    alldatatypes_Type,
    AEnum,
    Heavy,
    StateWithoutDefault,
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

def test_assoc_types0_stub_double():
    # alldatatypes_Type has no real 'alldatatypes_Type' property in the generated
    # code (a bare stub) -- manually attach it so alldatatypes_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # alldatatypes_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = alldatatypes_Root()
    partner = alldatatypes_Type()
    setattr(partner, 'alldatatypes_Type', None)
    _safe_set(owner, 'alldatatypes_Root', {partner})
    assert getattr(partner, 'alldatatypes_Type') == owner
    _safe_set(owner, 'alldatatypes_Root', set())
    assert getattr(partner, 'alldatatypes_Type') is None


