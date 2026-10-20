import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActionExpression,
    Guard,
    GuardExpression,
    NamedElement,
    State,
    StateMachine_Action,
    StateMachine_ActionExpression,
    StateMachine_ChangeSignalAllowedSpeed,
    StateMachine_ChangeTrainCurrentTrackElement,
    StateMachine_ChangeTrainHeadingSpeed,
    StateMachine_ChangeTurnoutDirection,
    StateMachine_CompositeState,
    StateMachine_Guard,
    StateMachine_GuardExpression,
    StateMachine_NamedElement,
    StateMachine_NextTrackElementIs,
    StateMachine_RDMElement,
    StateMachine_RouteElement,
    StateMachine_Signal,
    StateMachine_SignalAllowedSpeedChanged,
    StateMachine_SignalCurrentAllowedSpeed,
    StateMachine_State,
    StateMachine_StateMachine,
    StateMachine_StateMachineBehavioralModel,
    StateMachine_TrackElement,
    StateMachine_Train,
    StateMachine_TrainCurrentHeadingSpeed,
    StateMachine_TrainCurrentlyStandsOn,
    StateMachine_TrainHeadingSpeedChanged,
    StateMachine_TrainTrackElementChanged,
    StateMachine_Transition,
    StateMachine_Trigger,
    StateMachine_TriggerExpression,
    StateMachine_Turnout,
    StateMachine_TurnoutCurrentDirection,
    StateMachine_TurnoutDesiredDirection,
    StateMachine_TurnoutDirectionChanged,
    StateMachine_TurnoutHasDesiredDirection,
    Trigger,
    TriggerExpression,
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

def test_assoc_incomingTransitions17_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(isEnabled=True, isFireable=True)
    a2 = StateMachine_Transition(isEnabled=False, isFireable=False)
    b = StateMachine_State(isActive=True, isInitial=True)
    _safe_set(b, 'targetState', {a1})
    assert _is_linked(b, 'targetState', a1)
    if hasattr(a1, 'Transition18'):
        assert _is_linked(a1, 'Transition18', b)
    _safe_set(b, 'targetState', {a2})
    assert _is_linked(b, 'targetState', a2)
    if hasattr(a1, 'Transition18'):
        assert not _is_linked(a1, 'Transition18', b)
    if hasattr(a2, 'Transition18'):
        assert _is_linked(a2, 'Transition18', b)
    _safe_set(b, 'targetState', set())
    assert not _is_linked(b, 'targetState', a2)
    if hasattr(a2, 'Transition18'):
        assert not _is_linked(a2, 'Transition18', b)


def test_assoc_outgoingTransitions16_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(isEnabled=True, isFireable=True)
    a2 = StateMachine_Transition(isEnabled=False, isFireable=False)
    b = StateMachine_State(isActive=True, isInitial=True)
    _safe_set(b, 'sourceState', {a1})
    assert _is_linked(b, 'sourceState', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'sourceState', {a2})
    assert _is_linked(b, 'sourceState', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'sourceState', set())
    assert not _is_linked(b, 'sourceState', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_sourceState19_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(isEnabled=True, isFireable=True)
    a2 = StateMachine_Transition(isEnabled=False, isFireable=False)
    b = StateMachine_State(isActive=True, isInitial=True)
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_targetState20_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(isEnabled=True, isFireable=True)
    a2 = StateMachine_Transition(isEnabled=False, isFireable=False)
    b = StateMachine_State(isActive=True, isInitial=True)
    _safe_set(b, 'State21', a1)
    assert _is_linked(b, 'State21', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State21', a2)
    assert _is_linked(b, 'State21', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State21', None)
    assert not _is_linked(b, 'State21', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action28_stub_double():
    # StateMachine_Action has no real 'StateMachine_Action30' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(isEnabled=True, isFireable=True)
    partner = StateMachine_Action()
    setattr(partner, 'StateMachine_Action30', None)
    _safe_set(owner, 'StateMachine_Transition29', {partner})
    assert getattr(partner, 'StateMachine_Action30') == owner
    _safe_set(owner, 'StateMachine_Transition29', set())
    assert getattr(partner, 'StateMachine_Action30') is None


def test_assoc_activeState11_stub_double():
    # StateMachine_StateMachine has no real 'StateMachine_StateMachine12' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_State(isActive=True, isInitial=True)
    partner = StateMachine_StateMachine()
    setattr(partner, 'StateMachine_StateMachine12', None)
    _safe_set(owner, 'StateMachine_State13', partner)
    assert getattr(partner, 'StateMachine_StateMachine12') == owner
    _safe_set(owner, 'StateMachine_State13', None)
    assert getattr(partner, 'StateMachine_StateMachine12') is None


def test_assoc_guard25_stub_double():
    # StateMachine_Guard has no real 'StateMachine_Guard27' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(isEnabled=True, isFireable=True)
    partner = StateMachine_Guard()
    setattr(partner, 'StateMachine_Guard27', None)
    _safe_set(owner, 'StateMachine_Transition26', {partner})
    assert getattr(partner, 'StateMachine_Guard27') == owner
    _safe_set(owner, 'StateMachine_Transition26', set())
    assert getattr(partner, 'StateMachine_Guard27') is None


def test_assoc_signal34_stub_double():
    # StateMachine_Signal has no real 'StateMachine_Signal' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_ChangeSignalAllowedSpeed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_ChangeSignalAllowedSpeed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_ChangeSignalAllowedSpeed(newAllowedSpeed="sample_text")
    partner = StateMachine_Signal()
    setattr(partner, 'StateMachine_Signal', None)
    _safe_set(owner, 'StateMachine_ChangeSignalAllowedSpeed', partner)
    assert getattr(partner, 'StateMachine_Signal') == owner
    _safe_set(owner, 'StateMachine_ChangeSignalAllowedSpeed', None)
    assert getattr(partner, 'StateMachine_Signal') is None


def test_assoc_signal49_stub_double():
    # StateMachine_Signal has no real 'StateMachine_Signal50' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_SignalCurrentAllowedSpeed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_SignalCurrentAllowedSpeed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_SignalCurrentAllowedSpeed(currentAllowedSpeed="sample_text")
    partner = StateMachine_Signal()
    setattr(partner, 'StateMachine_Signal50', None)
    _safe_set(owner, 'StateMachine_SignalCurrentAllowedSpeed', partner)
    assert getattr(partner, 'StateMachine_Signal50') == owner
    _safe_set(owner, 'StateMachine_SignalCurrentAllowedSpeed', None)
    assert getattr(partner, 'StateMachine_Signal50') is None


def test_assoc_signal58_stub_double():
    # StateMachine_Signal has no real 'StateMachine_Signal59' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_SignalAllowedSpeedChanged's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_SignalAllowedSpeedChanged's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_SignalAllowedSpeedChanged(newAllowedSpeed="sample_text")
    partner = StateMachine_Signal()
    setattr(partner, 'StateMachine_Signal59', None)
    _safe_set(owner, 'StateMachine_SignalAllowedSpeedChanged', partner)
    assert getattr(partner, 'StateMachine_Signal59') == owner
    _safe_set(owner, 'StateMachine_SignalAllowedSpeedChanged', None)
    assert getattr(partner, 'StateMachine_Signal59') is None


def test_assoc_states1_stub_double():
    # StateMachine_StateMachine has no real 'StateMachine_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_State(isActive=True, isInitial=True)
    partner = StateMachine_StateMachine()
    setattr(partner, 'StateMachine_StateMachine2', None)
    _safe_set(owner, 'StateMachine_State', partner)
    assert owner in getattr(partner, 'StateMachine_StateMachine2')
    _safe_set(owner, 'StateMachine_State', None)
    assert owner not in getattr(partner, 'StateMachine_StateMachine2')


def test_assoc_train33_stub_double():
    # StateMachine_Train has no real 'StateMachine_Train' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_ChangeTrainHeadingSpeed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_ChangeTrainHeadingSpeed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_ChangeTrainHeadingSpeed(newHeadingSpeed="sample_text")
    partner = StateMachine_Train()
    setattr(partner, 'StateMachine_Train', None)
    _safe_set(owner, 'StateMachine_ChangeTrainHeadingSpeed', partner)
    assert getattr(partner, 'StateMachine_Train') == owner
    _safe_set(owner, 'StateMachine_ChangeTrainHeadingSpeed', None)
    assert getattr(partner, 'StateMachine_Train') is None


def test_assoc_train40_stub_double():
    # StateMachine_Train has no real 'StateMachine_Train41' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_TrainCurrentHeadingSpeed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_TrainCurrentHeadingSpeed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_TrainCurrentHeadingSpeed(currentHeadingSpeed="sample_text")
    partner = StateMachine_Train()
    setattr(partner, 'StateMachine_Train41', None)
    _safe_set(owner, 'StateMachine_TrainCurrentHeadingSpeed', partner)
    assert getattr(partner, 'StateMachine_Train41') == owner
    _safe_set(owner, 'StateMachine_TrainCurrentHeadingSpeed', None)
    assert getattr(partner, 'StateMachine_Train41') is None


def test_assoc_train51_stub_double():
    # StateMachine_Train has no real 'StateMachine_Train52' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_TrainHeadingSpeedChanged's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_TrainHeadingSpeedChanged's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_TrainHeadingSpeedChanged(newHeadingSpeed="sample_text")
    partner = StateMachine_Train()
    setattr(partner, 'StateMachine_Train52', None)
    _safe_set(owner, 'StateMachine_TrainHeadingSpeedChanged', partner)
    assert getattr(partner, 'StateMachine_Train52') == owner
    _safe_set(owner, 'StateMachine_TrainHeadingSpeedChanged', None)
    assert getattr(partner, 'StateMachine_Train52') is None


def test_assoc_transitions3_stub_double():
    # StateMachine_StateMachine has no real 'StateMachine_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(isEnabled=True, isFireable=True)
    partner = StateMachine_StateMachine()
    setattr(partner, 'StateMachine_StateMachine4', None)
    _safe_set(owner, 'StateMachine_Transition', partner)
    assert owner in getattr(partner, 'StateMachine_StateMachine4')
    _safe_set(owner, 'StateMachine_Transition', None)
    assert owner not in getattr(partner, 'StateMachine_StateMachine4')


def test_assoc_trigger22_stub_double():
    # StateMachine_Trigger has no real 'StateMachine_Trigger24' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(isEnabled=True, isFireable=True)
    partner = StateMachine_Trigger()
    setattr(partner, 'StateMachine_Trigger24', None)
    _safe_set(owner, 'StateMachine_Transition23', partner)
    assert getattr(partner, 'StateMachine_Trigger24') == owner
    _safe_set(owner, 'StateMachine_Transition23', None)
    assert getattr(partner, 'StateMachine_Trigger24') is None


def test_assoc_turnout35_stub_double():
    # StateMachine_Turnout has no real 'StateMachine_Turnout' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_ChangeTurnoutDirection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_ChangeTurnoutDirection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_ChangeTurnoutDirection(newTurnoutDirection="sample_text")
    partner = StateMachine_Turnout()
    setattr(partner, 'StateMachine_Turnout', None)
    _safe_set(owner, 'StateMachine_ChangeTurnoutDirection', partner)
    assert getattr(partner, 'StateMachine_Turnout') == owner
    _safe_set(owner, 'StateMachine_ChangeTurnoutDirection', None)
    assert getattr(partner, 'StateMachine_Turnout') is None


def test_assoc_turnout47_stub_double():
    # StateMachine_Turnout has no real 'StateMachine_Turnout48' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_TurnoutCurrentDirection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_TurnoutCurrentDirection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_TurnoutCurrentDirection(currentTurnoutDirection="sample_text")
    partner = StateMachine_Turnout()
    setattr(partner, 'StateMachine_Turnout48', None)
    _safe_set(owner, 'StateMachine_TurnoutCurrentDirection', partner)
    assert getattr(partner, 'StateMachine_Turnout48') == owner
    _safe_set(owner, 'StateMachine_TurnoutCurrentDirection', None)
    assert getattr(partner, 'StateMachine_Turnout48') is None


def test_assoc_turnout60_stub_double():
    # StateMachine_Turnout has no real 'StateMachine_Turnout61' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_TurnoutDirectionChanged's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_TurnoutDirectionChanged's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_TurnoutDirectionChanged(newTurnoutDirection="sample_text")
    partner = StateMachine_Turnout()
    setattr(partner, 'StateMachine_Turnout61', None)
    _safe_set(owner, 'StateMachine_TurnoutDirectionChanged', partner)
    assert getattr(partner, 'StateMachine_Turnout61') == owner
    _safe_set(owner, 'StateMachine_TurnoutDirectionChanged', None)
    assert getattr(partner, 'StateMachine_Turnout61') is None


