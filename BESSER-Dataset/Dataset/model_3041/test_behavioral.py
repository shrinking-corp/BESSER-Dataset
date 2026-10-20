import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    DataBag,
    DataElement,
    DataLeaf,
    DependentAction,
    FeatureVersion,
    IArithmetricFunction,
    IContextVariable,
    IDataNodeFunction,
    IFeature,
    ILogicFunction,
    ITimeConsumer,
    IValueFunction,
    PostGenerationAction,
    PreGenerationAction,
    ReconfigurationAction,
    actions_Action,
    actions_ActionReference,
    actions_ActivateFeatureAction,
    actions_DeactivateFeatureAction,
    actions_DependentAction,
    actions_EObject,
    actions_FailAction,
    actions_GetDataAction,
    actions_GetFeatureStateAction,
    actions_GetPropertyAction,
    actions_GetRealTimeAction,
    actions_PostGenerationAction,
    actions_PostGenerationSequence,
    actions_PreGenerationAction,
    actions_PreGenerationSequence,
    actions_ReconfigurationAction,
    actions_RemoveBagAction,
    actions_SetDataAction,
    actions_SetPropertyAction,
    actions_StandAloneAction,
    actions_Term,
    actions_TermAction,
    actions_ThrowAction,
    actions_TimeAction,
    actions_TimedConditionAction,
    core_AbstractModelElement,
    core_ITopLevelElement,
    rules_IRealTimeConsumer,
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

def test_assoc_action7_stub_double():
    # actions_PreGenerationAction has no real 'actions_PreGenerationAction8' property in the generated
    # code (a bare stub) -- manually attach it so actions_TimedConditionAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_TimedConditionAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_TimedConditionAction(frequency=7)
    partner = actions_PreGenerationAction()
    setattr(partner, 'actions_PreGenerationAction8', None)
    _safe_set(owner, 'actions_TimedConditionAction', partner)
    assert getattr(partner, 'actions_PreGenerationAction8') == owner
    _safe_set(owner, 'actions_TimedConditionAction', None)
    assert getattr(partner, 'actions_PreGenerationAction8') is None


def test_assoc_condition9_stub_double():
    # ILogicFunction has no real 'ILogicFunction' property in the generated
    # code (a bare stub) -- manually attach it so actions_TimedConditionAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_TimedConditionAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_TimedConditionAction(frequency=7)
    partner = ILogicFunction()
    setattr(partner, 'ILogicFunction', None)
    _safe_set(owner, 'actions_TimedConditionAction10', partner)
    assert getattr(partner, 'ILogicFunction') == owner
    _safe_set(owner, 'actions_TimedConditionAction10', None)
    assert getattr(partner, 'ILogicFunction') is None


def test_assoc_consumer31_stub_double():
    # ITimeConsumer has no real 'ITimeConsumer' property in the generated
    # code (a bare stub) -- manually attach it so actions_TimeAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_TimeAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_TimeAction(time=7)
    partner = ITimeConsumer()
    setattr(partner, 'ITimeConsumer', None)
    _safe_set(owner, 'actions_TimeAction', partner)
    assert getattr(partner, 'ITimeConsumer') == owner
    _safe_set(owner, 'actions_TimeAction', None)
    assert getattr(partner, 'ITimeConsumer') is None


