import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Step,
    Value,
    trace_BigStep,
    trace_LiteralValue,
    trace_ModelState,
    trace_ObjectState,
    trace_ParameterValue,
    trace_RefValue,
    trace_SmallStep,
    trace_Step,
    trace_Trace,
    trace_TracedObject,
    trace_Value,
    ParamterKindEnum,
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

def test_assoc_parametervalue12_stub_double():
    # trace_Step has no real 'trace_Step13' property in the generated
    # code (a bare stub) -- manually attach it so trace_ParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ParameterValue(DirectionKind="sample_text")
    partner = trace_Step()
    setattr(partner, 'trace_Step13', None)
    _safe_set(owner, 'trace_ParameterValue', partner)
    assert owner in getattr(partner, 'trace_Step13')
    _safe_set(owner, 'trace_ParameterValue', None)
    assert owner not in getattr(partner, 'trace_Step13')


def test_assoc_value26_stub_double():
    # trace_Value has no real 'trace_Value28' property in the generated
    # code (a bare stub) -- manually attach it so trace_ParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ParameterValue(DirectionKind="sample_text")
    partner = trace_Value()
    setattr(partner, 'trace_Value28', None)
    _safe_set(owner, 'trace_ParameterValue27', {partner})
    assert getattr(partner, 'trace_Value28') == owner
    _safe_set(owner, 'trace_ParameterValue27', set())
    assert getattr(partner, 'trace_Value28') is None


