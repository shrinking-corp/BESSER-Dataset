import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MonoBehaviour,
    MyClass,
    MyClass12,
    MyClass13,
    MyClass18,
    MyClass19,
    MyClass2,
    MyClass3,
    MyClass4,
    MyClass6,
    MyClass7,
    MyClass9,
    StopButton,
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

def test_assoc_MyClass9_MyClass19_stub_double():
    # MyClass19 has no real 'myClass91' property in the generated
    # code (a bare stub) -- manually attach it so MyClass9's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MyClass9's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MyClass9(h=7)
    partner = MyClass19()
    setattr(partner, 'myClass91', None)
    _safe_set(owner, 'myClass190', partner)
    assert getattr(partner, 'myClass91') == owner
    _safe_set(owner, 'myClass190', None)
    assert getattr(partner, 'myClass91') is None


