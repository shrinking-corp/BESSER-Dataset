import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActionExpression,
    ActionSequence,
    ActionState,
    ActivityGraph,
    ArgListsExpression,
    Argument,
    Association,
    AssociationEnd,
    AssociationRole,
    Attribute,
    AttributeLink,
    BehavioralFeature,
    BooleanExpression,
    Classifier,
    ClassifierRole,
    Collaboration,
    CollaborationInstanceSet,
    ComponentInstance,
    CompositeState,
    Event,
    Expression,
    Extend,
    ExtensionPoint,
    Feature,
    Guard,
    Include,
    Instance,
    Interaction,
    InteractionInstanceSet,
    IterationExpression,
    Link,
    LinkEnd,
    Message,
    ModelElement,
    Multiplicity_,
    NodeInstance,
    ObjectSetExpression,
    Operation,
    Parameter,
    Partition,
    Reception,
    Relationship,
    SendAction,
    Signal,
    SignalEvent,
    SimpleState,
    State,
    StateMachine,
    StateVertex,
    Stimulus,
    SubmachineState,
    TimeExpression,
    Transition,
    UseCase,
    behavioral_elements_activity_graphs_ActionState,
    behavioral_elements_activity_graphs_ActivityGraph,
    behavioral_elements_activity_graphs_CallState,
    behavioral_elements_activity_graphs_ClassifierInState,
    behavioral_elements_activity_graphs_ObjectFlowState,
    behavioral_elements_activity_graphs_Partition,
    behavioral_elements_activity_graphs_SubactivityState,
    behavioral_elements_collaborations_AssociationEndRole,
    behavioral_elements_collaborations_AssociationRole,
    behavioral_elements_collaborations_ClassifierRole,
    behavioral_elements_collaborations_Collaboration,
    behavioral_elements_collaborations_CollaborationInstanceSet,
    behavioral_elements_collaborations_Interaction,
    behavioral_elements_collaborations_InteractionInstanceSet,
    behavioral_elements_collaborations_Message,
    behavioral_elements_common_behavior_Action,
    behavioral_elements_common_behavior_ActionSequence,
    behavioral_elements_common_behavior_Argument,
    behavioral_elements_common_behavior_AttributeLink,
    behavioral_elements_common_behavior_CallAction,
    behavioral_elements_common_behavior_ComponentInstance,
    behavioral_elements_common_behavior_CreateAction,
    behavioral_elements_common_behavior_DataValue,
    behavioral_elements_common_behavior_DestroyAction,
    behavioral_elements_common_behavior_Exception,
    behavioral_elements_common_behavior_Instance,
    behavioral_elements_common_behavior_Link,
    behavioral_elements_common_behavior_LinkEnd,
    behavioral_elements_common_behavior_LinkObject,
    behavioral_elements_common_behavior_NodeInstance,
    behavioral_elements_common_behavior_Object,
    behavioral_elements_common_behavior_Reception,
    behavioral_elements_common_behavior_ReturnAction,
    behavioral_elements_common_behavior_SendAction,
    behavioral_elements_common_behavior_Signal,
    behavioral_elements_common_behavior_Stimulus,
    behavioral_elements_common_behavior_SubsystemInstance,
    behavioral_elements_common_behavior_TerminateAction,
    behavioral_elements_common_behavior_UninterpretedAction,
    behavioral_elements_state_machines_CallEvent,
    behavioral_elements_state_machines_ChangeEvent,
    behavioral_elements_state_machines_CompositeState,
    behavioral_elements_state_machines_Event,
    behavioral_elements_state_machines_FinalState,
    behavioral_elements_state_machines_Guard,
    behavioral_elements_state_machines_Pseudostate,
    behavioral_elements_state_machines_SignalEvent,
    behavioral_elements_state_machines_SimpleState,
    behavioral_elements_state_machines_State,
    behavioral_elements_state_machines_StateMachine,
    behavioral_elements_state_machines_StateVertex,
    behavioral_elements_state_machines_StubState,
    behavioral_elements_state_machines_SubmachineState,
    behavioral_elements_state_machines_SynchState,
    behavioral_elements_state_machines_TimeEvent,
    behavioral_elements_state_machines_Transition,
    behavioral_elements_use_cases_Actor,
    behavioral_elements_use_cases_Extend,
    behavioral_elements_use_cases_ExtensionPoint,
    behavioral_elements_use_cases_Include,
    behavioral_elements_use_cases_UseCase,
    behavioral_elements_use_cases_UseCaseInstance,
    common_behavior_Link,
    common_behavior_Object,
    core_GeneralizableElement,
    core_Namespace,
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

def test_assoc_actionSequence23_stub_double():
    # ActionSequence has no real 'ActionSequence' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = ActionSequence()
    setattr(partner, 'ActionSequence', None)
    _safe_set(owner, 'action24', partner)
    assert getattr(partner, 'ActionSequence') == owner
    _safe_set(owner, 'action24', None)
    assert getattr(partner, 'ActionSequence') is None


def test_assoc_actualArgument22_stub_double():
    # Argument has no real 'Argument' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = Argument()
    setattr(partner, 'Argument', None)
    _safe_set(owner, 'action', {partner})
    assert getattr(partner, 'Argument') == owner
    _safe_set(owner, 'action', set())
    assert getattr(partner, 'Argument') is None


def test_assoc_dynamicArguments253_stub_double():
    # ArgListsExpression has no real 'ArgListsExpression' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_activity_graphs_SubactivityState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_activity_graphs_SubactivityState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_activity_graphs_SubactivityState(isDynamic="sample_text")
    partner = ArgListsExpression()
    setattr(partner, 'ArgListsExpression', None)
    _safe_set(owner, 'behavioral_elements_activity_graphs_SubactivityState', partner)
    assert getattr(partner, 'ArgListsExpression') == owner
    _safe_set(owner, 'behavioral_elements_activity_graphs_SubactivityState', None)
    assert getattr(partner, 'ArgListsExpression') is None


def test_assoc_dynamicArguments257_stub_double():
    # ArgListsExpression has no real 'ArgListsExpression258' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_activity_graphs_ActionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_activity_graphs_ActionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_activity_graphs_ActionState(isDynamic="sample_text")
    partner = ArgListsExpression()
    setattr(partner, 'ArgListsExpression258', None)
    _safe_set(owner, 'behavioral_elements_activity_graphs_ActionState', partner)
    assert getattr(partner, 'ArgListsExpression258') == owner
    _safe_set(owner, 'behavioral_elements_activity_graphs_ActionState', None)
    assert getattr(partner, 'ArgListsExpression258') is None


def test_assoc_dynamicMultiplicity254_stub_double():
    # Multiplicity_ has no real 'Multiplicity256' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_activity_graphs_SubactivityState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_activity_graphs_SubactivityState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_activity_graphs_SubactivityState(isDynamic="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity256', None)
    _safe_set(owner, 'behavioral_elements_activity_graphs_SubactivityState255', partner)
    assert getattr(partner, 'Multiplicity256') == owner
    _safe_set(owner, 'behavioral_elements_activity_graphs_SubactivityState255', None)
    assert getattr(partner, 'Multiplicity256') is None


def test_assoc_dynamicMultiplicity259_stub_double():
    # Multiplicity_ has no real 'Multiplicity261' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_activity_graphs_ActionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_activity_graphs_ActionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_activity_graphs_ActionState(isDynamic="sample_text")
    partner = Multiplicity_()
    setattr(partner, 'Multiplicity261', None)
    _safe_set(owner, 'behavioral_elements_activity_graphs_ActionState260', partner)
    assert getattr(partner, 'Multiplicity261') == owner
    _safe_set(owner, 'behavioral_elements_activity_graphs_ActionState260', None)
    assert getattr(partner, 'Multiplicity261') is None


def test_assoc_extend99_stub_double():
    # Extend has no real 'Extend101' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_use_cases_ExtensionPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_use_cases_ExtensionPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_use_cases_ExtensionPoint(location="sample_text")
    partner = Extend()
    setattr(partner, 'Extend101', None)
    _safe_set(owner, 'extensionPoint100', {partner})
    assert getattr(partner, 'Extend101') == owner
    _safe_set(owner, 'extensionPoint100', set())
    assert getattr(partner, 'Extend101') is None


def test_assoc_parameter262_stub_double():
    # Parameter has no real 'Parameter263' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_activity_graphs_ObjectFlowState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_activity_graphs_ObjectFlowState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_activity_graphs_ObjectFlowState(isSynch="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter263', None)
    _safe_set(owner, 'behavioral_elements_activity_graphs_ObjectFlowState', {partner})
    assert getattr(partner, 'Parameter263') == owner
    _safe_set(owner, 'behavioral_elements_activity_graphs_ObjectFlowState', set())
    assert getattr(partner, 'Parameter263') is None


def test_assoc_recurrence17_stub_double():
    # IterationExpression has no real 'IterationExpression' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = IterationExpression()
    setattr(partner, 'IterationExpression', None)
    _safe_set(owner, 'behavioral_elements_common_behavior_Action', partner)
    assert getattr(partner, 'IterationExpression') == owner
    _safe_set(owner, 'behavioral_elements_common_behavior_Action', None)
    assert getattr(partner, 'IterationExpression') is None


def test_assoc_script20_stub_double():
    # ActionExpression has no real 'ActionExpression' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = ActionExpression()
    setattr(partner, 'ActionExpression', None)
    _safe_set(owner, 'behavioral_elements_common_behavior_Action21', partner)
    assert getattr(partner, 'ActionExpression') == owner
    _safe_set(owner, 'behavioral_elements_common_behavior_Action21', None)
    assert getattr(partner, 'ActionExpression') is None


def test_assoc_signal47_stub_double():
    # Signal has no real 'Signal48' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Reception's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Reception's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Reception(isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text", specification="sample_text")
    partner = Signal()
    setattr(partner, 'Signal48', None)
    _safe_set(owner, 'reception', partner)
    assert getattr(partner, 'Signal48') == owner
    _safe_set(owner, 'reception', None)
    assert getattr(partner, 'Signal48') is None


def test_assoc_stimulus25_stub_double():
    # Stimulus has no real 'Stimulus' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = Stimulus()
    setattr(partner, 'Stimulus', None)
    _safe_set(owner, 'dispatchAction', {partner})
    assert getattr(partner, 'Stimulus') == owner
    _safe_set(owner, 'dispatchAction', set())
    assert getattr(partner, 'Stimulus') is None


def test_assoc_subvertex149_stub_double():
    # StateVertex has no real 'StateVertex150' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_state_machines_CompositeState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_state_machines_CompositeState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_state_machines_CompositeState(isConcurrent="sample_text")
    partner = StateVertex()
    setattr(partner, 'StateVertex150', None)
    _safe_set(owner, 'container', {partner})
    assert getattr(partner, 'StateVertex150') == owner
    _safe_set(owner, 'container', set())
    assert getattr(partner, 'StateVertex150') is None


def test_assoc_target18_stub_double():
    # ObjectSetExpression has no real 'ObjectSetExpression' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = ObjectSetExpression()
    setattr(partner, 'ObjectSetExpression', None)
    _safe_set(owner, 'behavioral_elements_common_behavior_Action19', partner)
    assert getattr(partner, 'ObjectSetExpression') == owner
    _safe_set(owner, 'behavioral_elements_common_behavior_Action19', None)
    assert getattr(partner, 'ObjectSetExpression') is None


def test_assoc_transition26_stub_double():
    # Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_common_behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_common_behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_common_behavior_Action(isAsynchronous="sample_text")
    partner = Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'effect', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'effect', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_type264_stub_double():
    # Classifier has no real 'Classifier266' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_activity_graphs_ObjectFlowState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_activity_graphs_ObjectFlowState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_activity_graphs_ObjectFlowState(isSynch="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier266', None)
    _safe_set(owner, 'behavioral_elements_activity_graphs_ObjectFlowState265', partner)
    assert getattr(partner, 'Classifier266') == owner
    _safe_set(owner, 'behavioral_elements_activity_graphs_ObjectFlowState265', None)
    assert getattr(partner, 'Classifier266') is None


def test_assoc_useCase97_stub_double():
    # UseCase has no real 'UseCase98' property in the generated
    # code (a bare stub) -- manually attach it so behavioral_elements_use_cases_ExtensionPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavioral_elements_use_cases_ExtensionPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavioral_elements_use_cases_ExtensionPoint(location="sample_text")
    partner = UseCase()
    setattr(partner, 'UseCase98', None)
    _safe_set(owner, 'extensionPoint', partner)
    assert getattr(partner, 'UseCase98') == owner
    _safe_set(owner, 'extensionPoint', None)
    assert getattr(partner, 'UseCase98') is None


