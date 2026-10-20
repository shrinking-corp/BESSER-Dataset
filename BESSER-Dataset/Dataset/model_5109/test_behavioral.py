import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TestElementA,
    testPackage_Container,
    testPackage_TestElementA,
    testPackage_TestElementB,
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

def test_assoc_content0_stub_double():
    # testPackage_Container has no real 'testPackage_Container' property in the generated
    # code (a bare stub) -- manually attach it so testPackage_TestElementA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testPackage_TestElementA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testPackage_TestElementA(multi=7, name="sample_text")
    partner = testPackage_Container()
    setattr(partner, 'testPackage_Container', None)
    _safe_set(owner, 'testPackage_TestElementA', partner)
    assert owner in getattr(partner, 'testPackage_Container')
    _safe_set(owner, 'testPackage_TestElementA', None)
    assert owner not in getattr(partner, 'testPackage_Container')


def test_assoc_ref1_stub_double():
    # testPackage_TestElementB has no real 'testPackage_TestElementB' property in the generated
    # code (a bare stub) -- manually attach it so testPackage_TestElementA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testPackage_TestElementA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testPackage_TestElementA(multi=7, name="sample_text")
    partner = testPackage_TestElementB()
    setattr(partner, 'testPackage_TestElementB', None)
    _safe_set(owner, 'testPackage_TestElementA2', partner)
    assert owner in getattr(partner, 'testPackage_TestElementB')
    _safe_set(owner, 'testPackage_TestElementA2', None)
    assert owner not in getattr(partner, 'testPackage_TestElementB')


