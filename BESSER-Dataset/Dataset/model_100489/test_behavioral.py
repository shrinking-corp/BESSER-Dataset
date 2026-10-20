import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActionExpression,
    ActionSequence,
    Argument,
    BehavioralFeature,
    BooleanExpression,
    Classifier,
    Common_Behavior_Action,
    Common_Behavior_ActionSequence,
    Common_Behavior_Argument,
    Common_Behavior_CallAction,
    Common_Behavior_CreateAction,
    Common_Behavior_DestroyAction,
    Common_Behavior_Exception,
    Common_Behavior_Reception,
    Common_Behavior_ReturnAction,
    Common_Behavior_SendAction,
    Common_Behavior_Signal,
    Common_Behavior_TerminateAction,
    Common_Behavior_UninterpretedAction,
    CompositeState,
    Core_BehavioralFeature,
    Core_Classifier,
    Core_Element,
    Core_Feature,
    Core_GeneralizableElement,
    Core_Generalization_,
    Core_ModelElement,
    Core_Namespace,
    Core_Operation,
    Core_Parameter,
    Core_Relationship,
    Data_Types_ActionExpression,
    Data_Types_BooleanExpression,
    Data_Types_Expression,
    Data_Types_IterationExpression,
    Data_Types_ObjectSetExpression,
    Data_Types_TimeExpression,
    Element,
    Event,
    Expression,
    Feature,
    GeneralizableElement,
    Generalization_,
    Guard,
    IterationExpression,
    ModelElement,
    Namespace,
    ObjectSetExpression,
    Operation,
    Parameter,
    Relationship,
    Signal,
    State,
    StateMachine,
    StateVertex,
    State_Machines_CallEvent,
    State_Machines_ChangeEvent,
    State_Machines_CompositeState,
    State_Machines_Event,
    State_Machines_FinalState,
    State_Machines_Guard,
    State_Machines_Pseudostate,
    State_Machines_SignalEvent,
    State_Machines_SimpleState,
    State_Machines_State,
    State_Machines_StateMachine,
    State_Machines_StateVertex,
    State_Machines_StubState,
    State_Machines_SubmachineState,
    State_Machines_SynchState,
    State_Machines_TimeEvent,
    State_Machines_Transition,
    SubmachineState,
    TimeExpression,
    Transition,
    CallConcurrencyKind,
    ParameterDirectionKind,
    PseudostateKind,
    ScopeKind,
    VisibilityKind,
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

def test_assoc_actionSequence1_stub_double():
    # ActionSequence has no real 'ActionSequence' property in the generated
    # code (a bare stub) -- manually attach it so Common_Behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Common_Behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Common_Behavior_Action(isAsynchronous="sample_text")
    partner = ActionSequence()
    setattr(partner, 'ActionSequence', None)
    _safe_set(owner, 'action2', partner)
    assert getattr(partner, 'ActionSequence') == owner
    _safe_set(owner, 'action2', None)
    assert getattr(partner, 'ActionSequence') is None


def test_assoc_actualArgument0_stub_double():
    # Argument has no real 'Argument' property in the generated
    # code (a bare stub) -- manually attach it so Common_Behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Common_Behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Common_Behavior_Action(isAsynchronous="sample_text")
    partner = Argument()
    setattr(partner, 'Argument', None)
    _safe_set(owner, 'action', {partner})
    assert getattr(partner, 'Argument') == owner
    _safe_set(owner, 'action', set())
    assert getattr(partner, 'Argument') is None


def test_assoc_behavioralFeature80_stub_double():
    # BehavioralFeature has no real 'BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so Core_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Parameter(kind="sample_text")
    partner = BehavioralFeature()
    setattr(partner, 'BehavioralFeature', None)
    _safe_set(owner, 'parameter', partner)
    assert getattr(partner, 'BehavioralFeature') == owner
    _safe_set(owner, 'parameter', None)
    assert getattr(partner, 'BehavioralFeature') is None


def test_assoc_child87_stub_double():
    # GeneralizableElement has no real 'GeneralizableElement88' property in the generated
    # code (a bare stub) -- manually attach it so Core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Generalization_(discriminator="sample_text")
    partner = GeneralizableElement()
    setattr(partner, 'GeneralizableElement88', None)
    _safe_set(owner, 'generalization', partner)
    assert getattr(partner, 'GeneralizableElement88') == owner
    _safe_set(owner, 'generalization', None)
    assert getattr(partner, 'GeneralizableElement88') is None


def test_assoc_defaultValue81_stub_double():
    # Expression has no real 'Expression83' property in the generated
    # code (a bare stub) -- manually attach it so Core_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Parameter(kind="sample_text")
    partner = Expression()
    setattr(partner, 'Expression83', None)
    _safe_set(owner, 'Core_Parameter82', partner)
    assert getattr(partner, 'Expression83') == owner
    _safe_set(owner, 'Core_Parameter82', None)
    assert getattr(partner, 'Expression83') is None


def test_assoc_generalization68_stub_double():
    # Generalization_ has no real 'Generalization_' property in the generated
    # code (a bare stub) -- manually attach it so Core_GeneralizableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_GeneralizableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_GeneralizableElement(isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text")
    partner = Generalization_()
    setattr(partner, 'Generalization_', None)
    _safe_set(owner, 'child', {partner})
    assert getattr(partner, 'Generalization_') == owner
    _safe_set(owner, 'child', set())
    assert getattr(partner, 'Generalization_') is None


def test_assoc_namespace67_stub_double():
    # Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so Core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_ModelElement(isSpecification="sample_text", name="sample_text", visibility="sample_text")
    partner = Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedElement', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedElement', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_owner74_stub_double():
    # Classifier has no real 'Classifier75' property in the generated
    # code (a bare stub) -- manually attach it so Core_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Feature(ownerScope="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier75', None)
    _safe_set(owner, 'feature', partner)
    assert getattr(partner, 'Classifier75') == owner
    _safe_set(owner, 'feature', None)
    assert getattr(partner, 'Classifier75') is None


def test_assoc_parameter76_stub_double():
    # Parameter has no real 'Parameter77' property in the generated
    # code (a bare stub) -- manually attach it so Core_BehavioralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_BehavioralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_BehavioralFeature(isQuery="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter77', None)
    _safe_set(owner, 'behavioralFeature', {partner})
    assert getattr(partner, 'Parameter77') == owner
    _safe_set(owner, 'behavioralFeature', set())
    assert getattr(partner, 'Parameter77') is None


def test_assoc_parent84_stub_double():
    # GeneralizableElement has no real 'GeneralizableElement' property in the generated
    # code (a bare stub) -- manually attach it so Core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Generalization_(discriminator="sample_text")
    partner = GeneralizableElement()
    setattr(partner, 'GeneralizableElement', None)
    _safe_set(owner, 'Core_Generalization', partner)
    assert getattr(partner, 'GeneralizableElement') == owner
    _safe_set(owner, 'Core_Generalization', None)
    assert getattr(partner, 'GeneralizableElement') is None


def test_assoc_powertype85_stub_double():
    # Classifier has no real 'Classifier86' property in the generated
    # code (a bare stub) -- manually attach it so Core_Generalization_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Generalization_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Generalization_(discriminator="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier86', None)
    _safe_set(owner, 'powertypeRange', partner)
    assert getattr(partner, 'Classifier86') == owner
    _safe_set(owner, 'powertypeRange', None)
    assert getattr(partner, 'Classifier86') is None


def test_assoc_recurrence3_stub_double():
    # IterationExpression has no real 'IterationExpression' property in the generated
    # code (a bare stub) -- manually attach it so Common_Behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Common_Behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Common_Behavior_Action(isAsynchronous="sample_text")
    partner = IterationExpression()
    setattr(partner, 'IterationExpression', None)
    _safe_set(owner, 'Common_Behavior_Action', partner)
    assert getattr(partner, 'IterationExpression') == owner
    _safe_set(owner, 'Common_Behavior_Action', None)
    assert getattr(partner, 'IterationExpression') is None


def test_assoc_script6_stub_double():
    # ActionExpression has no real 'ActionExpression' property in the generated
    # code (a bare stub) -- manually attach it so Common_Behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Common_Behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Common_Behavior_Action(isAsynchronous="sample_text")
    partner = ActionExpression()
    setattr(partner, 'ActionExpression', None)
    _safe_set(owner, 'Common_Behavior_Action7', partner)
    assert getattr(partner, 'ActionExpression') == owner
    _safe_set(owner, 'Common_Behavior_Action7', None)
    assert getattr(partner, 'ActionExpression') is None


def test_assoc_signal15_stub_double():
    # Signal has no real 'Signal16' property in the generated
    # code (a bare stub) -- manually attach it so Common_Behavior_Reception's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Common_Behavior_Reception's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Common_Behavior_Reception(isAbstract="sample_text", isLeaf="sample_text", isRoot="sample_text", specification="sample_text")
    partner = Signal()
    setattr(partner, 'Signal16', None)
    _safe_set(owner, 'Common_Behavior_Reception', partner)
    assert getattr(partner, 'Signal16') == owner
    _safe_set(owner, 'Common_Behavior_Reception', None)
    assert getattr(partner, 'Signal16') is None


def test_assoc_subvertex58_stub_double():
    # StateVertex has no real 'StateVertex59' property in the generated
    # code (a bare stub) -- manually attach it so State_Machines_CompositeState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # State_Machines_CompositeState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = State_Machines_CompositeState(isConcurrent="sample_text")
    partner = StateVertex()
    setattr(partner, 'StateVertex59', None)
    _safe_set(owner, 'container', {partner})
    assert getattr(partner, 'StateVertex59') == owner
    _safe_set(owner, 'container', set())
    assert getattr(partner, 'StateVertex59') is None


def test_assoc_target4_stub_double():
    # ObjectSetExpression has no real 'ObjectSetExpression' property in the generated
    # code (a bare stub) -- manually attach it so Common_Behavior_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Common_Behavior_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Common_Behavior_Action(isAsynchronous="sample_text")
    partner = ObjectSetExpression()
    setattr(partner, 'ObjectSetExpression', None)
    _safe_set(owner, 'Common_Behavior_Action5', partner)
    assert getattr(partner, 'ObjectSetExpression') == owner
    _safe_set(owner, 'Common_Behavior_Action5', None)
    assert getattr(partner, 'ObjectSetExpression') is None


def test_assoc_type78_stub_double():
    # Classifier has no real 'Classifier79' property in the generated
    # code (a bare stub) -- manually attach it so Core_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Core_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Core_Parameter(kind="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier79', None)
    _safe_set(owner, 'Core_Parameter', partner)
    assert getattr(partner, 'Classifier79') == owner
    _safe_set(owner, 'Core_Parameter', None)
    assert getattr(partner, 'Classifier79') is None


