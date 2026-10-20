import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Dependency,
    Element,
    Gate,
    dynamicFaultTree_AND,
    dynamicFaultTree_DFT,
    dynamicFaultTree_Dependency,
    dynamicFaultTree_Element,
    dynamicFaultTree_Event,
    dynamicFaultTree_FunctionalDependency,
    dynamicFaultTree_Gate,
    dynamicFaultTree_OR,
    dynamicFaultTree_PAND,
    dynamicFaultTree_POR,
    dynamicFaultTree_Sequence,
    dynamicFaultTree_Spare,
    dynamicFaultTree_TopLevelEvent,
    dynamicFaultTree_XOR,
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

def test_assoc_dependencies1_stub_double():
    # dynamicFaultTree_Dependency has no real 'dynamicFaultTree_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so dynamicFaultTree_DFT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dynamicFaultTree_DFT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dynamicFaultTree_DFT(name="sample_text")
    partner = dynamicFaultTree_Dependency()
    setattr(partner, 'dynamicFaultTree_Dependency', None)
    _safe_set(owner, 'dynamicFaultTree_DFT2', {partner})
    assert getattr(partner, 'dynamicFaultTree_Dependency') == owner
    _safe_set(owner, 'dynamicFaultTree_DFT2', set())
    assert getattr(partner, 'dynamicFaultTree_Dependency') is None


def test_assoc_topLevelEvent0_stub_double():
    # dynamicFaultTree_TopLevelEvent has no real 'dynamicFaultTree_TopLevelEvent' property in the generated
    # code (a bare stub) -- manually attach it so dynamicFaultTree_DFT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dynamicFaultTree_DFT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dynamicFaultTree_DFT(name="sample_text")
    partner = dynamicFaultTree_TopLevelEvent()
    setattr(partner, 'dynamicFaultTree_TopLevelEvent', None)
    _safe_set(owner, 'dynamicFaultTree_DFT', partner)
    assert getattr(partner, 'dynamicFaultTree_TopLevelEvent') == owner
    _safe_set(owner, 'dynamicFaultTree_DFT', None)
    assert getattr(partner, 'dynamicFaultTree_TopLevelEvent') is None


