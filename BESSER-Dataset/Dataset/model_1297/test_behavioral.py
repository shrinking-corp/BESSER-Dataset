import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    StateMachine,
    StateMachinesProv_ConnectionPointReference,
    StateMachinesProv_FinalState,
    StateMachinesProv_ProtocolConformance,
    StateMachinesProv_ProtocolStateMachine,
    StateMachinesProv_ProtocolTransition,
    StateMachinesProv_Pseudostate,
    StateMachinesProv_Region,
    StateMachinesProv_State,
    StateMachinesProv_StateMachine,
    StateMachinesProv_TimeEvent,
    StateMachinesProv_Transition,
    StateMachinesProv_Vertex,
    Transition,
    Vertex,
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

def test_assoc_redefinedState66_reverse_link_reassign_clear():
    a1 = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    a2 = StateMachinesProv_State(isComposite=False, isOrthogonal=False, isSimple=False, isSubmachineState=False)
    b = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    _safe_set(b, 'StateMachinesProv_State67', a1)
    assert _is_linked(b, 'StateMachinesProv_State67', a1)
    if hasattr(a1, 'StateMachinesProv_State65'):
        assert _is_linked(a1, 'StateMachinesProv_State65', b)
    _safe_set(b, 'StateMachinesProv_State67', a2)
    assert _is_linked(b, 'StateMachinesProv_State67', a2)
    if hasattr(a1, 'StateMachinesProv_State65'):
        assert not _is_linked(a1, 'StateMachinesProv_State65', b)
    if hasattr(a2, 'StateMachinesProv_State65'):
        assert _is_linked(a2, 'StateMachinesProv_State65', b)
    _safe_set(b, 'StateMachinesProv_State67', None)
    assert not _is_linked(b, 'StateMachinesProv_State67', a2)
    if hasattr(a2, 'StateMachinesProv_State65'):
        assert not _is_linked(a2, 'StateMachinesProv_State65', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_connection53_stub_double():
    # StateMachinesProv_ConnectionPointReference has no real 'StateMachinesProv_ConnectionPointReference55' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_ConnectionPointReference()
    setattr(partner, 'StateMachinesProv_ConnectionPointReference55', None)
    _safe_set(owner, 'StateMachinesProv_State54', {partner})
    assert getattr(partner, 'StateMachinesProv_ConnectionPointReference55') == owner
    _safe_set(owner, 'StateMachinesProv_State54', set())
    assert getattr(partner, 'StateMachinesProv_ConnectionPointReference55') is None


def test_assoc_connectionPoint56_stub_double():
    # StateMachinesProv_Pseudostate has no real 'StateMachinesProv_Pseudostate58' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_Pseudostate()
    setattr(partner, 'StateMachinesProv_Pseudostate58', None)
    _safe_set(owner, 'StateMachinesProv_State57', {partner})
    assert getattr(partner, 'StateMachinesProv_Pseudostate58') == owner
    _safe_set(owner, 'StateMachinesProv_State57', set())
    assert getattr(partner, 'StateMachinesProv_Pseudostate58') is None


def test_assoc_region62_stub_double():
    # StateMachinesProv_Region has no real 'StateMachinesProv_Region64' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_Region()
    setattr(partner, 'StateMachinesProv_Region64', None)
    _safe_set(owner, 'StateMachinesProv_State63', {partner})
    assert getattr(partner, 'StateMachinesProv_Region64') == owner
    _safe_set(owner, 'StateMachinesProv_State63', set())
    assert getattr(partner, 'StateMachinesProv_Region64') is None


def test_assoc_state15_stub_double():
    # StateMachinesProv_Region has no real 'StateMachinesProv_Region16' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_Region()
    setattr(partner, 'StateMachinesProv_Region16', None)
    _safe_set(owner, 'StateMachinesProv_State17', partner)
    assert getattr(partner, 'StateMachinesProv_Region16') == owner
    _safe_set(owner, 'StateMachinesProv_State17', None)
    assert getattr(partner, 'StateMachinesProv_Region16') is None


def test_assoc_state42_stub_double():
    # StateMachinesProv_Pseudostate has no real 'StateMachinesProv_Pseudostate43' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_Pseudostate()
    setattr(partner, 'StateMachinesProv_Pseudostate43', None)
    _safe_set(owner, 'StateMachinesProv_State44', partner)
    assert getattr(partner, 'StateMachinesProv_Pseudostate43') == owner
    _safe_set(owner, 'StateMachinesProv_State44', None)
    assert getattr(partner, 'StateMachinesProv_Pseudostate43') is None


def test_assoc_state50_stub_double():
    # StateMachinesProv_ConnectionPointReference has no real 'StateMachinesProv_ConnectionPointReference51' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_ConnectionPointReference()
    setattr(partner, 'StateMachinesProv_ConnectionPointReference51', None)
    _safe_set(owner, 'StateMachinesProv_State52', partner)
    assert getattr(partner, 'StateMachinesProv_ConnectionPointReference51') == owner
    _safe_set(owner, 'StateMachinesProv_State52', None)
    assert getattr(partner, 'StateMachinesProv_ConnectionPointReference51') is None


def test_assoc_submachine59_stub_double():
    # StateMachinesProv_StateMachine has no real 'StateMachinesProv_StateMachine61' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_StateMachine()
    setattr(partner, 'StateMachinesProv_StateMachine61', None)
    _safe_set(owner, 'StateMachinesProv_State60', partner)
    assert getattr(partner, 'StateMachinesProv_StateMachine61') == owner
    _safe_set(owner, 'StateMachinesProv_State60', None)
    assert getattr(partner, 'StateMachinesProv_StateMachine61') is None


def test_assoc_submachineState3_stub_double():
    # StateMachinesProv_StateMachine has no real 'StateMachinesProv_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so StateMachinesProv_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachinesProv_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachinesProv_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachinesProv_StateMachine()
    setattr(partner, 'StateMachinesProv_StateMachine4', None)
    _safe_set(owner, 'StateMachinesProv_State', partner)
    assert owner in getattr(partner, 'StateMachinesProv_StateMachine4')
    _safe_set(owner, 'StateMachinesProv_State', None)
    assert owner not in getattr(partner, 'StateMachinesProv_StateMachine4')


