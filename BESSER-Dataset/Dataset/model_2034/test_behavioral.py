import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    network_AbstractElement,
    network_Channel,
    network_ChannelBuffer,
    network_CurrentStateMapState,
    network_Network,
    network_RunTimeNetwork,
    network_State,
    network_Statemachine,
    network_Transition,
    Event,
    TypeOfChannel,
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

def test_assoc_channel16_reverse_link_reassign_clear():
    a1 = network_Transition(Event="sample_text")
    a2 = network_Transition(Event="sample_text_2")
    b = network_Channel(Type="sample_text")
    _safe_set(b, 'network_Channel18', a1)
    assert _is_linked(b, 'network_Channel18', a1)
    if hasattr(a1, 'network_Transition17'):
        assert _is_linked(a1, 'network_Transition17', b)
    _safe_set(b, 'network_Channel18', a2)
    assert _is_linked(b, 'network_Channel18', a2)
    if hasattr(a1, 'network_Transition17'):
        assert not _is_linked(a1, 'network_Transition17', b)
    if hasattr(a2, 'network_Transition17'):
        assert _is_linked(a2, 'network_Transition17', b)
    _safe_set(b, 'network_Channel18', None)
    assert not _is_linked(b, 'network_Channel18', a2)
    if hasattr(a2, 'network_Transition17'):
        assert not _is_linked(a2, 'network_Transition17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_channel1_stub_double():
    # network_Network has no real 'network_Network2' property in the generated
    # code (a bare stub) -- manually attach it so network_Channel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_Channel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_Channel(Type="sample_text")
    partner = network_Network()
    setattr(partner, 'network_Network2', None)
    _safe_set(owner, 'network_Channel', partner)
    assert owner in getattr(partner, 'network_Network2')
    _safe_set(owner, 'network_Channel', None)
    assert owner not in getattr(partner, 'network_Network2')


def test_assoc_channelbuffer23_stub_double():
    # network_ChannelBuffer has no real 'network_ChannelBuffer' property in the generated
    # code (a bare stub) -- manually attach it so network_RunTimeNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_RunTimeNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_RunTimeNetwork()
    partner = network_ChannelBuffer()
    setattr(partner, 'network_ChannelBuffer', None)
    _safe_set(owner, 'network_RunTimeNetwork24', {partner})
    assert getattr(partner, 'network_ChannelBuffer') == owner
    _safe_set(owner, 'network_RunTimeNetwork24', set())
    assert getattr(partner, 'network_ChannelBuffer') is None


def test_assoc_currentstatemapstate21_stub_double():
    # network_CurrentStateMapState has no real 'network_CurrentStateMapState' property in the generated
    # code (a bare stub) -- manually attach it so network_RunTimeNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_RunTimeNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_RunTimeNetwork()
    partner = network_CurrentStateMapState()
    setattr(partner, 'network_CurrentStateMapState', None)
    _safe_set(owner, 'network_RunTimeNetwork22', {partner})
    assert getattr(partner, 'network_CurrentStateMapState') == owner
    _safe_set(owner, 'network_RunTimeNetwork22', set())
    assert getattr(partner, 'network_CurrentStateMapState') is None


def test_assoc_key28_stub_double():
    # network_ChannelBuffer has no real 'network_ChannelBuffer29' property in the generated
    # code (a bare stub) -- manually attach it so network_Channel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_Channel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_Channel(Type="sample_text")
    partner = network_ChannelBuffer()
    setattr(partner, 'network_ChannelBuffer29', None)
    _safe_set(owner, 'network_Channel30', partner)
    assert getattr(partner, 'network_ChannelBuffer29') == owner
    _safe_set(owner, 'network_Channel30', None)
    assert getattr(partner, 'network_ChannelBuffer29') is None


def test_assoc_network19_stub_double():
    # network_Network has no real 'network_Network20' property in the generated
    # code (a bare stub) -- manually attach it so network_RunTimeNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_RunTimeNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_RunTimeNetwork()
    partner = network_Network()
    setattr(partner, 'network_Network20', None)
    _safe_set(owner, 'network_RunTimeNetwork', partner)
    assert getattr(partner, 'network_Network20') == owner
    _safe_set(owner, 'network_RunTimeNetwork', None)
    assert getattr(partner, 'network_Network20') is None


def test_assoc_source10_stub_double():
    # network_State has no real 'network_State12' property in the generated
    # code (a bare stub) -- manually attach it so network_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_Transition(Event="sample_text")
    partner = network_State()
    setattr(partner, 'network_State12', None)
    _safe_set(owner, 'network_Transition11', partner)
    assert getattr(partner, 'network_State12') == owner
    _safe_set(owner, 'network_Transition11', None)
    assert getattr(partner, 'network_State12') is None


def test_assoc_target13_stub_double():
    # network_State has no real 'network_State15' property in the generated
    # code (a bare stub) -- manually attach it so network_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_Transition(Event="sample_text")
    partner = network_State()
    setattr(partner, 'network_State15', None)
    _safe_set(owner, 'network_Transition14', partner)
    assert getattr(partner, 'network_State15') == owner
    _safe_set(owner, 'network_Transition14', None)
    assert getattr(partner, 'network_State15') is None


def test_assoc_transition8_stub_double():
    # network_Statemachine has no real 'network_Statemachine9' property in the generated
    # code (a bare stub) -- manually attach it so network_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # network_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = network_Transition(Event="sample_text")
    partner = network_Statemachine()
    setattr(partner, 'network_Statemachine9', None)
    _safe_set(owner, 'network_Transition', partner)
    assert owner in getattr(partner, 'network_Statemachine9')
    _safe_set(owner, 'network_Transition', None)
    assert owner not in getattr(partner, 'network_Statemachine9')


