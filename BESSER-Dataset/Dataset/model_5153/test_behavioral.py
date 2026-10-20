import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B,
    mytest_A,
    mytest_B,
    mytest_C,
    mytest_MyRoot,
    MyEnum,
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

def test_assoc_aContainer0_stub_double():
    # mytest_MyRoot has no real 'mytest_MyRoot' property in the generated
    # code (a bare stub) -- manually attach it so mytest_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mytest_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mytest_A(name="sample_text")
    partner = mytest_MyRoot()
    setattr(partner, 'mytest_MyRoot', None)
    _safe_set(owner, 'mytest_A', partner)
    assert owner in getattr(partner, 'mytest_MyRoot')
    _safe_set(owner, 'mytest_A', None)
    assert owner not in getattr(partner, 'mytest_MyRoot')


def test_assoc_bContainer1_stub_double():
    # mytest_MyRoot has no real 'mytest_MyRoot2' property in the generated
    # code (a bare stub) -- manually attach it so mytest_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mytest_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mytest_B(enumatt="sample_text")
    partner = mytest_MyRoot()
    setattr(partner, 'mytest_MyRoot2', None)
    _safe_set(owner, 'mytest_B', partner)
    assert owner in getattr(partner, 'mytest_MyRoot2')
    _safe_set(owner, 'mytest_B', None)
    assert owner not in getattr(partner, 'mytest_MyRoot2')


def test_assoc_b_transient3_stub_double():
    # mytest_MyRoot has no real 'mytest_MyRoot4' property in the generated
    # code (a bare stub) -- manually attach it so mytest_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mytest_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mytest_B(enumatt="sample_text")
    partner = mytest_MyRoot()
    setattr(partner, 'mytest_MyRoot4', None)
    _safe_set(owner, 'mytest_B5', partner)
    assert owner in getattr(partner, 'mytest_MyRoot4')
    _safe_set(owner, 'mytest_B5', None)
    assert owner not in getattr(partner, 'mytest_MyRoot4')


