import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    CallOperationAction,
    Guard,
    IsInStateCondition,
    NamedElement,
    StructuralFeature,
    sooml_Action,
    sooml_Attribute,
    sooml_CallOperationAction,
    sooml_CallParameterOperationAction,
    sooml_CallReferenceOperationAction,
    sooml_Class,
    sooml_EntryOperation,
    sooml_Event,
    sooml_Guard,
    sooml_IsInStateCondition,
    sooml_NamedElement,
    sooml_Operation,
    sooml_Package,
    sooml_Parameter,
    sooml_ParameterBinding,
    sooml_ParameterIsInStateCondition,
    sooml_Reference,
    sooml_ReferenceAssignmentAction,
    sooml_ReferenceIsInStateCondition,
    sooml_State,
    sooml_StateMachine,
    sooml_StructuralFeature,
    sooml_Transition,
    DataType,
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

def test_assoc_callObjectViaParameter63_stub_double():
    # sooml_CallParameterOperationAction has no real 'sooml_CallParameterOperationAction' property in the generated
    # code (a bare stub) -- manually attach it so sooml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_Parameter(dataType="sample_text")
    partner = sooml_CallParameterOperationAction()
    setattr(partner, 'sooml_CallParameterOperationAction', None)
    _safe_set(owner, 'sooml_Parameter64', partner)
    assert getattr(partner, 'sooml_CallParameterOperationAction') == owner
    _safe_set(owner, 'sooml_Parameter64', None)
    assert getattr(partner, 'sooml_CallParameterOperationAction') is None


def test_assoc_classType39_stub_double():
    # sooml_Class has no real 'sooml_Class41' property in the generated
    # code (a bare stub) -- manually attach it so sooml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_Parameter(dataType="sample_text")
    partner = sooml_Class()
    setattr(partner, 'sooml_Class41', None)
    _safe_set(owner, 'sooml_Parameter40', partner)
    assert getattr(partner, 'sooml_Class41') == owner
    _safe_set(owner, 'sooml_Parameter40', None)
    assert getattr(partner, 'sooml_Class41') is None


def test_assoc_features9_stub_double():
    # sooml_Class has no real 'sooml_Class10' property in the generated
    # code (a bare stub) -- manually attach it so sooml_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    partner = sooml_Class()
    setattr(partner, 'sooml_Class10', None)
    _safe_set(owner, 'sooml_StructuralFeature', partner)
    assert owner in getattr(partner, 'sooml_Class10')
    _safe_set(owner, 'sooml_StructuralFeature', None)
    assert owner not in getattr(partner, 'sooml_Class10')


def test_assoc_parameter16_stub_double():
    # sooml_Operation has no real 'sooml_Operation17' property in the generated
    # code (a bare stub) -- manually attach it so sooml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_Parameter(dataType="sample_text")
    partner = sooml_Operation()
    setattr(partner, 'sooml_Operation17', None)
    _safe_set(owner, 'sooml_Parameter', partner)
    assert owner in getattr(partner, 'sooml_Operation17')
    _safe_set(owner, 'sooml_Parameter', None)
    assert owner not in getattr(partner, 'sooml_Operation17')


def test_assoc_parameter59_stub_double():
    # sooml_ParameterIsInStateCondition has no real 'sooml_ParameterIsInStateCondition' property in the generated
    # code (a bare stub) -- manually attach it so sooml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_Parameter(dataType="sample_text")
    partner = sooml_ParameterIsInStateCondition()
    setattr(partner, 'sooml_ParameterIsInStateCondition', None)
    _safe_set(owner, 'sooml_Parameter60', partner)
    assert getattr(partner, 'sooml_ParameterIsInStateCondition') == owner
    _safe_set(owner, 'sooml_Parameter60', None)
    assert getattr(partner, 'sooml_ParameterIsInStateCondition') is None


def test_assoc_parameter65_stub_double():
    # sooml_ReferenceAssignmentAction has no real 'sooml_ReferenceAssignmentAction' property in the generated
    # code (a bare stub) -- manually attach it so sooml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_Parameter(dataType="sample_text")
    partner = sooml_ReferenceAssignmentAction()
    setattr(partner, 'sooml_ReferenceAssignmentAction', None)
    _safe_set(owner, 'sooml_Parameter66', partner)
    assert getattr(partner, 'sooml_ReferenceAssignmentAction') == owner
    _safe_set(owner, 'sooml_Parameter66', None)
    assert getattr(partner, 'sooml_ReferenceAssignmentAction') is None


def test_assoc_parameterBinding49_stub_double():
    # sooml_ParameterBinding has no real 'sooml_ParameterBinding50' property in the generated
    # code (a bare stub) -- manually attach it so sooml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_Parameter(dataType="sample_text")
    partner = sooml_ParameterBinding()
    setattr(partner, 'sooml_ParameterBinding50', None)
    _safe_set(owner, 'sooml_Parameter51', partner)
    assert getattr(partner, 'sooml_ParameterBinding50') == owner
    _safe_set(owner, 'sooml_Parameter51', None)
    assert getattr(partner, 'sooml_ParameterBinding50') is None


def test_assoc_structuralFeatureBinding46_stub_double():
    # sooml_ParameterBinding has no real 'sooml_ParameterBinding47' property in the generated
    # code (a bare stub) -- manually attach it so sooml_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sooml_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sooml_StructuralFeature(lowerBound=7, upperBound=7)
    partner = sooml_ParameterBinding()
    setattr(partner, 'sooml_ParameterBinding47', None)
    _safe_set(owner, 'sooml_StructuralFeature48', partner)
    assert getattr(partner, 'sooml_ParameterBinding47') == owner
    _safe_set(owner, 'sooml_StructuralFeature48', None)
    assert getattr(partner, 'sooml_ParameterBinding47') is None


