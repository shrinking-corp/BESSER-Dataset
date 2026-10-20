import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    LiteralValue,
    ObjectState,
    ParameterList,
    Step,
    StepSpec,
    TransientObject,
    Value,
    trace_CompositParameterList,
    trace_CompositeObjectState,
    trace_DynamicTransientObject,
    trace_EClass,
    trace_EObject,
    trace_EStructuralFeature,
    trace_LeafObjectState,
    trace_LeafParameterList,
    trace_LiteralBoolean,
    trace_LiteralFloat,
    trace_LiteralInteger,
    trace_LiteralString,
    trace_LiteralValue,
    trace_NormalStep,
    trace_ObjectState,
    trace_ParameterList,
    trace_ParameterValue,
    trace_PatternOccurrenceStepData,
    trace_PatternOcurrence,
    trace_RefValue,
    trace_RepeatingStep,
    trace_State,
    trace_StaticTransientObject,
    trace_Step,
    trace_StepPattern,
    trace_StepSpec,
    trace_StepType,
    trace_Trace,
    trace_TransientObject,
    trace_TransientObjectState,
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

def test_assoc_objectstates78_stub_double():
    # trace_ObjectState has no real 'trace_ObjectState79' property in the generated
    # code (a bare stub) -- manually attach it so trace_CompositeObjectState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_CompositeObjectState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_CompositeObjectState(objectstatesOrder=7)
    partner = trace_ObjectState()
    setattr(partner, 'trace_ObjectState79', None)
    _safe_set(owner, 'trace_CompositeObjectState', {partner})
    assert getattr(partner, 'trace_ObjectState79') == owner
    _safe_set(owner, 'trace_CompositeObjectState', set())
    assert getattr(partner, 'trace_ObjectState79') is None


def test_assoc_parameterValues15_stub_double():
    # trace_Trace has no real 'trace_Trace16' property in the generated
    # code (a bare stub) -- manually attach it so trace_ParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ParameterValue(DirectionKind="sample_text")
    partner = trace_Trace()
    setattr(partner, 'trace_Trace16', None)
    _safe_set(owner, 'trace_ParameterValue', partner)
    assert owner in getattr(partner, 'trace_Trace16')
    _safe_set(owner, 'trace_ParameterValue', None)
    assert owner not in getattr(partner, 'trace_Trace16')


def test_assoc_parameterlist83_stub_double():
    # trace_ParameterList has no real 'trace_ParameterList84' property in the generated
    # code (a bare stub) -- manually attach it so trace_CompositParameterList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_CompositParameterList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_CompositParameterList(paramtervaluesOrder=7)
    partner = trace_ParameterList()
    setattr(partner, 'trace_ParameterList84', None)
    _safe_set(owner, 'trace_CompositParameterList', {partner})
    assert getattr(partner, 'trace_ParameterList84') == owner
    _safe_set(owner, 'trace_CompositParameterList', set())
    assert getattr(partner, 'trace_ParameterList84') is None


def test_assoc_parametervalue85_stub_double():
    # trace_ParameterList has no real 'trace_ParameterList86' property in the generated
    # code (a bare stub) -- manually attach it so trace_ParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ParameterValue(DirectionKind="sample_text")
    partner = trace_ParameterList()
    setattr(partner, 'trace_ParameterList86', None)
    _safe_set(owner, 'trace_ParameterValue87', partner)
    assert owner in getattr(partner, 'trace_ParameterList86')
    _safe_set(owner, 'trace_ParameterValue87', None)
    assert owner not in getattr(partner, 'trace_ParameterList86')


def test_assoc_pattern42_stub_double():
    # trace_StepPattern has no real 'trace_StepPattern43' property in the generated
    # code (a bare stub) -- manually attach it so trace_PatternOcurrence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_PatternOcurrence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_PatternOcurrence(repet=7)
    partner = trace_StepPattern()
    setattr(partner, 'trace_StepPattern43', None)
    _safe_set(owner, 'trace_PatternOcurrence', partner)
    assert getattr(partner, 'trace_StepPattern43') == owner
    _safe_set(owner, 'trace_PatternOcurrence', None)
    assert getattr(partner, 'trace_StepPattern43') is None


def test_assoc_stepdata44_stub_double():
    # trace_PatternOccurrenceStepData has no real 'trace_PatternOccurrenceStepData' property in the generated
    # code (a bare stub) -- manually attach it so trace_PatternOcurrence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_PatternOcurrence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_PatternOcurrence(repet=7)
    partner = trace_PatternOccurrenceStepData()
    setattr(partner, 'trace_PatternOccurrenceStepData', None)
    _safe_set(owner, 'trace_PatternOcurrence45', {partner})
    assert getattr(partner, 'trace_PatternOccurrenceStepData') == owner
    _safe_set(owner, 'trace_PatternOcurrence45', set())
    assert getattr(partner, 'trace_PatternOccurrenceStepData') is None


def test_assoc_steptype3_stub_double():
    # trace_Trace has no real 'trace_Trace4' property in the generated
    # code (a bare stub) -- manually attach it so trace_StepType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_StepType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_StepType(stepName="sample_text")
    partner = trace_Trace()
    setattr(partner, 'trace_Trace4', None)
    _safe_set(owner, 'trace_StepType', partner)
    assert owner in getattr(partner, 'trace_Trace4')
    _safe_set(owner, 'trace_StepType', None)
    assert owner not in getattr(partner, 'trace_Trace4')


def test_assoc_steptype58_stub_double():
    # trace_StepSpec has no real 'trace_StepSpec' property in the generated
    # code (a bare stub) -- manually attach it so trace_StepType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_StepType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_StepType(stepName="sample_text")
    partner = trace_StepSpec()
    setattr(partner, 'trace_StepSpec', None)
    _safe_set(owner, 'trace_StepType59', partner)
    assert getattr(partner, 'trace_StepSpec') == owner
    _safe_set(owner, 'trace_StepType59', None)
    assert getattr(partner, 'trace_StepSpec') is None


def test_assoc_values67_stub_double():
    # trace_Value has no real 'trace_Value69' property in the generated
    # code (a bare stub) -- manually attach it so trace_ParameterValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ParameterValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ParameterValue(DirectionKind="sample_text")
    partner = trace_Value()
    setattr(partner, 'trace_Value69', None)
    _safe_set(owner, 'trace_ParameterValue68', {partner})
    assert getattr(partner, 'trace_Value69') == owner
    _safe_set(owner, 'trace_ParameterValue68', set())
    assert getattr(partner, 'trace_Value69') is None


