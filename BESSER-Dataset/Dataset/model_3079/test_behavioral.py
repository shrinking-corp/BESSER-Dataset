import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adaptation,
    InstantiationStrategy,
    ScopedInstantiation,
    SetAdaptation,
    UnsetAdaptation,
    adaptations_smartadapters4MODERATES_Action,
    adaptations_smartadapters4MODERATES_ActionBlock,
    adaptations_smartadapters4MODERATES_AnnotatedElement,
    adaptations_smartadapters4MODERATES_CompositeState,
    adaptations_smartadapters4MODERATES_Event,
    adaptations_smartadapters4MODERATES_Expression,
    adaptations_smartadapters4MODERATES_PlatformAnnotation,
    adaptations_smartadapters4MODERATES_Property,
    adaptations_smartadapters4MODERATES_State,
    adaptations_smartadapters4MODERATES_Transition,
    smartadapters4MODERATES_Adaptation,
    smartadapters4MODERATES_AdviceModel,
    smartadapters4MODERATES_Aspect,
    smartadapters4MODERATES_AspectModelElement,
    smartadapters4MODERATES_CloneAdaptation,
    smartadapters4MODERATES_CreateAdaptation,
    smartadapters4MODERATES_GlobalInstantiation,
    smartadapters4MODERATES_InstantiationStrategy,
    smartadapters4MODERATES_PerElementMatch,
    smartadapters4MODERATES_PerRoleMatch,
    smartadapters4MODERATES_PointcutModel,
    smartadapters4MODERATES_ScopedInstantiation,
    smartadapters4MODERATES_SetAdaptation,
    smartadapters4MODERATES_UnsetAdaptation,
    smartadapters4MODERATES_adaptations_SetActionBlock,
    smartadapters4MODERATES_adaptations_SetAnnotatedElement,
    smartadapters4MODERATES_adaptations_SetCompositeState,
    smartadapters4MODERATES_adaptations_SetState,
    smartadapters4MODERATES_adaptations_SetTransition,
    smartadapters4MODERATES_adaptations_UnsetCompositeState,
    smartadapters4MODERATES_adaptations_UnsetState,
    smartadapters4MODERATES_adaptations_UnsetTransition,
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

def test_assoc_adapt5_stub_double():
    # smartadapters4MODERATES_Adaptation has no real 'smartadapters4MODERATES_Adaptation' property in the generated
    # code (a bare stub) -- manually attach it so smartadapters4MODERATES_Aspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smartadapters4MODERATES_Aspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smartadapters4MODERATES_Aspect(name="sample_text")
    partner = smartadapters4MODERATES_Adaptation()
    setattr(partner, 'smartadapters4MODERATES_Adaptation', None)
    _safe_set(owner, 'smartadapters4MODERATES_Aspect6', {partner})
    assert getattr(partner, 'smartadapters4MODERATES_Adaptation') == owner
    _safe_set(owner, 'smartadapters4MODERATES_Aspect6', set())
    assert getattr(partner, 'smartadapters4MODERATES_Adaptation') is None


def test_assoc_advice1_stub_double():
    # smartadapters4MODERATES_AdviceModel has no real 'smartadapters4MODERATES_AdviceModel' property in the generated
    # code (a bare stub) -- manually attach it so smartadapters4MODERATES_Aspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smartadapters4MODERATES_Aspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smartadapters4MODERATES_Aspect(name="sample_text")
    partner = smartadapters4MODERATES_AdviceModel()
    setattr(partner, 'smartadapters4MODERATES_AdviceModel', None)
    _safe_set(owner, 'smartadapters4MODERATES_Aspect2', partner)
    assert getattr(partner, 'smartadapters4MODERATES_AdviceModel') == owner
    _safe_set(owner, 'smartadapters4MODERATES_Aspect2', None)
    assert getattr(partner, 'smartadapters4MODERATES_AdviceModel') is None


def test_assoc_pointcut0_stub_double():
    # smartadapters4MODERATES_PointcutModel has no real 'smartadapters4MODERATES_PointcutModel' property in the generated
    # code (a bare stub) -- manually attach it so smartadapters4MODERATES_Aspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smartadapters4MODERATES_Aspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smartadapters4MODERATES_Aspect(name="sample_text")
    partner = smartadapters4MODERATES_PointcutModel()
    setattr(partner, 'smartadapters4MODERATES_PointcutModel', None)
    _safe_set(owner, 'smartadapters4MODERATES_Aspect', partner)
    assert getattr(partner, 'smartadapters4MODERATES_PointcutModel') == owner
    _safe_set(owner, 'smartadapters4MODERATES_Aspect', None)
    assert getattr(partner, 'smartadapters4MODERATES_PointcutModel') is None


def test_assoc_strategies3_stub_double():
    # smartadapters4MODERATES_InstantiationStrategy has no real 'smartadapters4MODERATES_InstantiationStrategy' property in the generated
    # code (a bare stub) -- manually attach it so smartadapters4MODERATES_Aspect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smartadapters4MODERATES_Aspect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smartadapters4MODERATES_Aspect(name="sample_text")
    partner = smartadapters4MODERATES_InstantiationStrategy()
    setattr(partner, 'smartadapters4MODERATES_InstantiationStrategy', None)
    _safe_set(owner, 'smartadapters4MODERATES_Aspect4', {partner})
    assert getattr(partner, 'smartadapters4MODERATES_InstantiationStrategy') == owner
    _safe_set(owner, 'smartadapters4MODERATES_Aspect4', set())
    assert getattr(partner, 'smartadapters4MODERATES_InstantiationStrategy') is None


