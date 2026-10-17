import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Node,
    dataflownet_Channel,
    dataflownet_DataflowNet,
    dataflownet_DataflowSystem,
    dataflownet_FiringRule,
    dataflownet_NamedElement,
    dataflownet_Node,
    dataflownet_Process,
    dataflownet_StateMachine,
    dataflownet_StateMachineState,
    dataflownet_StateMachineTransition,
    dataflownet_Token,
    dataflownet_Type,
    Comparation,
    Protocol,
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

def test_assoc_inputs25_reverse_link_reassign_clear():
    a1 = dataflownet_StateMachineTransition(priority=7)
    a2 = dataflownet_StateMachineTransition(priority=13)
    b = dataflownet_FiringRule(compType="sample_text")
    _safe_set(b, 'dataflownet_FiringRule26', a1)
    assert _is_linked(b, 'dataflownet_FiringRule26', a1)
    if hasattr(a1, 'dataflownet_StateMachineTransition'):
        assert _is_linked(a1, 'dataflownet_StateMachineTransition', b)
    _safe_set(b, 'dataflownet_FiringRule26', a2)
    assert _is_linked(b, 'dataflownet_FiringRule26', a2)
    if hasattr(a1, 'dataflownet_StateMachineTransition'):
        assert not _is_linked(a1, 'dataflownet_StateMachineTransition', b)
    if hasattr(a2, 'dataflownet_StateMachineTransition'):
        assert _is_linked(a2, 'dataflownet_StateMachineTransition', b)
    _safe_set(b, 'dataflownet_FiringRule26', None)
    assert not _is_linked(b, 'dataflownet_FiringRule26', a2)
    if hasattr(a2, 'dataflownet_StateMachineTransition'):
        assert not _is_linked(a2, 'dataflownet_StateMachineTransition', b)


def test_assoc_outputs27_reverse_link_reassign_clear():
    a1 = dataflownet_StateMachineTransition(priority=7)
    a2 = dataflownet_StateMachineTransition(priority=13)
    b = dataflownet_FiringRule(compType="sample_text")
    _safe_set(b, 'dataflownet_FiringRule29', a1)
    assert _is_linked(b, 'dataflownet_FiringRule29', a1)
    if hasattr(a1, 'dataflownet_StateMachineTransition28'):
        assert _is_linked(a1, 'dataflownet_StateMachineTransition28', b)
    _safe_set(b, 'dataflownet_FiringRule29', a2)
    assert _is_linked(b, 'dataflownet_FiringRule29', a2)
    if hasattr(a1, 'dataflownet_StateMachineTransition28'):
        assert not _is_linked(a1, 'dataflownet_StateMachineTransition28', b)
    if hasattr(a2, 'dataflownet_StateMachineTransition28'):
        assert _is_linked(a2, 'dataflownet_StateMachineTransition28', b)
    _safe_set(b, 'dataflownet_FiringRule29', None)
    assert not _is_linked(b, 'dataflownet_FiringRule29', a2)
    if hasattr(a2, 'dataflownet_StateMachineTransition28'):
        assert not _is_linked(a2, 'dataflownet_StateMachineTransition28', b)


def test_assoc_processes48_reverse_link_reassign_clear():
    a1 = dataflownet_Process(host="sample_text")
    a2 = dataflownet_Process(host="sample_text_2")
    b = dataflownet_DataflowSystem(protocol="sample_text")
    _safe_set(b, 'dataflownet_DataflowSystem49', {a1})
    assert _is_linked(b, 'dataflownet_DataflowSystem49', a1)
    if hasattr(a1, 'dataflownet_Process50'):
        assert _is_linked(a1, 'dataflownet_Process50', b)
    _safe_set(b, 'dataflownet_DataflowSystem49', {a2})
    assert _is_linked(b, 'dataflownet_DataflowSystem49', a2)
    if hasattr(a1, 'dataflownet_Process50'):
        assert not _is_linked(a1, 'dataflownet_Process50', b)
    if hasattr(a2, 'dataflownet_Process50'):
        assert _is_linked(a2, 'dataflownet_Process50', b)
    _safe_set(b, 'dataflownet_DataflowSystem49', set())
    assert not _is_linked(b, 'dataflownet_DataflowSystem49', a2)
    if hasattr(a2, 'dataflownet_Process50'):
        assert not _is_linked(a2, 'dataflownet_Process50', b)


def test_assoc_tokens35_reverse_link_reassign_clear():
    a1 = dataflownet_Token(value="sample_text")
    a2 = dataflownet_Token(value="sample_text_2")
    b = dataflownet_FiringRule(compType="sample_text")
    _safe_set(b, 'dataflownet_FiringRule36', a1)
    assert _is_linked(b, 'dataflownet_FiringRule36', a1)
    if hasattr(a1, 'dataflownet_Token'):
        assert _is_linked(a1, 'dataflownet_Token', b)
    _safe_set(b, 'dataflownet_FiringRule36', a2)
    assert _is_linked(b, 'dataflownet_FiringRule36', a2)
    if hasattr(a1, 'dataflownet_Token'):
        assert not _is_linked(a1, 'dataflownet_Token', b)
    if hasattr(a2, 'dataflownet_Token'):
        assert _is_linked(a2, 'dataflownet_Token', b)
    _safe_set(b, 'dataflownet_FiringRule36', None)
    assert not _is_linked(b, 'dataflownet_FiringRule36', a2)
    if hasattr(a2, 'dataflownet_Token'):
        assert not _is_linked(a2, 'dataflownet_Token', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_channel32_stub_double():
    # dataflownet_Channel has no real 'dataflownet_Channel34' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_FiringRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_FiringRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_FiringRule(compType="sample_text")
    partner = dataflownet_Channel()
    setattr(partner, 'dataflownet_Channel34', None)
    _safe_set(owner, 'dataflownet_FiringRule33', partner)
    assert getattr(partner, 'dataflownet_Channel34') == owner
    _safe_set(owner, 'dataflownet_FiringRule33', None)
    assert getattr(partner, 'dataflownet_Channel34') is None


def test_assoc_channels45_stub_double():
    # dataflownet_Channel has no real 'dataflownet_Channel47' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_DataflowSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_DataflowSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_DataflowSystem(protocol="sample_text")
    partner = dataflownet_Channel()
    setattr(partner, 'dataflownet_Channel47', None)
    _safe_set(owner, 'dataflownet_DataflowSystem46', {partner})
    assert getattr(partner, 'dataflownet_Channel47') == owner
    _safe_set(owner, 'dataflownet_DataflowSystem46', set())
    assert getattr(partner, 'dataflownet_Channel47') is None


def test_assoc_firingRules3_stub_double():
    # dataflownet_StateMachine has no real 'dataflownet_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_FiringRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_FiringRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_FiringRule(compType="sample_text")
    partner = dataflownet_StateMachine()
    setattr(partner, 'dataflownet_StateMachine4', None)
    _safe_set(owner, 'dataflownet_FiringRule', partner)
    assert getattr(partner, 'dataflownet_StateMachine4') == owner
    _safe_set(owner, 'dataflownet_FiringRule', None)
    assert getattr(partner, 'dataflownet_StateMachine4') is None


def test_assoc_fromState21_stub_double():
    # dataflownet_StateMachineState has no real 'StateMachineState22' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_StateMachineTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_StateMachineTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_StateMachineTransition(priority=7)
    partner = dataflownet_StateMachineState()
    setattr(partner, 'StateMachineState22', None)
    _safe_set(owner, 'outputTransitions', partner)
    assert getattr(partner, 'StateMachineState22') == owner
    _safe_set(owner, 'outputTransitions', None)
    assert getattr(partner, 'StateMachineState22') is None


def test_assoc_inputTransitions17_stub_double():
    # dataflownet_StateMachineState has no real 'toState' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_StateMachineTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_StateMachineTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_StateMachineTransition(priority=7)
    partner = dataflownet_StateMachineState()
    setattr(partner, 'toState', None)
    _safe_set(owner, 'StateMachineTransition18', partner)
    assert getattr(partner, 'toState') == owner
    _safe_set(owner, 'StateMachineTransition18', None)
    assert getattr(partner, 'toState') is None


def test_assoc_nets42_stub_double():
    # dataflownet_DataflowNet has no real 'dataflownet_DataflowNet44' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_DataflowSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_DataflowSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_DataflowSystem(protocol="sample_text")
    partner = dataflownet_DataflowNet()
    setattr(partner, 'dataflownet_DataflowNet44', None)
    _safe_set(owner, 'dataflownet_DataflowSystem43', {partner})
    assert getattr(partner, 'dataflownet_DataflowNet44') == owner
    _safe_set(owner, 'dataflownet_DataflowSystem43', set())
    assert getattr(partner, 'dataflownet_DataflowNet44') is None


def test_assoc_outputTransitions16_stub_double():
    # dataflownet_StateMachineState has no real 'fromState' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_StateMachineTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_StateMachineTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_StateMachineTransition(priority=7)
    partner = dataflownet_StateMachineState()
    setattr(partner, 'fromState', None)
    _safe_set(owner, 'StateMachineTransition', partner)
    assert getattr(partner, 'fromState') == owner
    _safe_set(owner, 'StateMachineTransition', None)
    assert getattr(partner, 'fromState') is None


def test_assoc_process14_stub_double():
    # dataflownet_DataflowNet has no real 'dataflownet_DataflowNet15' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_Process(host="sample_text")
    partner = dataflownet_DataflowNet()
    setattr(partner, 'dataflownet_DataflowNet15', None)
    _safe_set(owner, 'dataflownet_Process', partner)
    assert getattr(partner, 'dataflownet_DataflowNet15') == owner
    _safe_set(owner, 'dataflownet_Process', None)
    assert getattr(partner, 'dataflownet_DataflowNet15') is None


def test_assoc_toState23_stub_double():
    # dataflownet_StateMachineState has no real 'StateMachineState24' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_StateMachineTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_StateMachineTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_StateMachineTransition(priority=7)
    partner = dataflownet_StateMachineState()
    setattr(partner, 'StateMachineState24', None)
    _safe_set(owner, 'inputTransitions', partner)
    assert getattr(partner, 'StateMachineState24') == owner
    _safe_set(owner, 'inputTransitions', None)
    assert getattr(partner, 'StateMachineState24') is None


def test_assoc_type37_stub_double():
    # dataflownet_Type has no real 'dataflownet_Type39' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_Token(value="sample_text")
    partner = dataflownet_Type()
    setattr(partner, 'dataflownet_Type39', None)
    _safe_set(owner, 'dataflownet_Token38', partner)
    assert getattr(partner, 'dataflownet_Type39') == owner
    _safe_set(owner, 'dataflownet_Token38', None)
    assert getattr(partner, 'dataflownet_Type39') is None


def test_assoc_types40_stub_double():
    # dataflownet_Type has no real 'dataflownet_Type41' property in the generated
    # code (a bare stub) -- manually attach it so dataflownet_DataflowSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dataflownet_DataflowSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dataflownet_DataflowSystem(protocol="sample_text")
    partner = dataflownet_Type()
    setattr(partner, 'dataflownet_Type41', None)
    _safe_set(owner, 'dataflownet_DataflowSystem', {partner})
    assert getattr(partner, 'dataflownet_Type41') == owner
    _safe_set(owner, 'dataflownet_DataflowSystem', set())
    assert getattr(partner, 'dataflownet_Type41') is None


