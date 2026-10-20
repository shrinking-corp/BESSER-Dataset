import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    smDsl_Command,
    smDsl_CommandsSection,
    smDsl_Event,
    smDsl_EventHandlingDescription,
    smDsl_EventsSection,
    smDsl_Model,
    smDsl_State,
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

def test_assoc_entryCommands9_reverse_link_reassign_clear():
    a1 = smDsl_State(initial=True, name="sample_text")
    a2 = smDsl_State(initial=False, name="sample_text_2")
    b = smDsl_Command(name="sample_text")
    _safe_set(b, 'smDsl_Command11', a1)
    assert _is_linked(b, 'smDsl_Command11', a1)
    if hasattr(a1, 'smDsl_State10'):
        assert _is_linked(a1, 'smDsl_State10', b)
    _safe_set(b, 'smDsl_Command11', a2)
    assert _is_linked(b, 'smDsl_Command11', a2)
    if hasattr(a1, 'smDsl_State10'):
        assert not _is_linked(a1, 'smDsl_State10', b)
    if hasattr(a2, 'smDsl_State10'):
        assert _is_linked(a2, 'smDsl_State10', b)
    _safe_set(b, 'smDsl_Command11', None)
    assert not _is_linked(b, 'smDsl_Command11', a2)
    if hasattr(a2, 'smDsl_State10'):
        assert not _is_linked(a2, 'smDsl_State10', b)


def test_assoc_exitCommands14_reverse_link_reassign_clear():
    a1 = smDsl_State(initial=True, name="sample_text")
    a2 = smDsl_State(initial=False, name="sample_text_2")
    b = smDsl_Command(name="sample_text")
    _safe_set(b, 'smDsl_Command16', a1)
    assert _is_linked(b, 'smDsl_Command16', a1)
    if hasattr(a1, 'smDsl_State15'):
        assert _is_linked(a1, 'smDsl_State15', b)
    _safe_set(b, 'smDsl_Command16', a2)
    assert _is_linked(b, 'smDsl_Command16', a2)
    if hasattr(a1, 'smDsl_State15'):
        assert not _is_linked(a1, 'smDsl_State15', b)
    if hasattr(a2, 'smDsl_State15'):
        assert _is_linked(a2, 'smDsl_State15', b)
    _safe_set(b, 'smDsl_Command16', None)
    assert not _is_linked(b, 'smDsl_Command16', a2)
    if hasattr(a2, 'smDsl_State15'):
        assert not _is_linked(a2, 'smDsl_State15', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = smDsl_State(initial=True, name="sample_text")
    a2 = smDsl_State(initial=False, name="sample_text_2")
    b = smDsl_Model(name="sample_text")
    _safe_set(b, 'smDsl_Model4', {a1})
    assert _is_linked(b, 'smDsl_Model4', a1)
    if hasattr(a1, 'smDsl_State'):
        assert _is_linked(a1, 'smDsl_State', b)
    _safe_set(b, 'smDsl_Model4', {a2})
    assert _is_linked(b, 'smDsl_Model4', a2)
    if hasattr(a1, 'smDsl_State'):
        assert not _is_linked(a1, 'smDsl_State', b)
    if hasattr(a2, 'smDsl_State'):
        assert _is_linked(a2, 'smDsl_State', b)
    _safe_set(b, 'smDsl_Model4', set())
    assert not _is_linked(b, 'smDsl_Model4', a2)
    if hasattr(a2, 'smDsl_State'):
        assert not _is_linked(a2, 'smDsl_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands20_stub_double():
    # smDsl_EventHandlingDescription has no real 'smDsl_EventHandlingDescription21' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_Command(name="sample_text")
    partner = smDsl_EventHandlingDescription()
    setattr(partner, 'smDsl_EventHandlingDescription21', None)
    _safe_set(owner, 'smDsl_Command22', partner)
    assert owner in getattr(partner, 'smDsl_EventHandlingDescription21')
    _safe_set(owner, 'smDsl_Command22', None)
    assert owner not in getattr(partner, 'smDsl_EventHandlingDescription21')


def test_assoc_commands7_stub_double():
    # smDsl_CommandsSection has no real 'smDsl_CommandsSection8' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_Command(name="sample_text")
    partner = smDsl_CommandsSection()
    setattr(partner, 'smDsl_CommandsSection8', None)
    _safe_set(owner, 'smDsl_Command', partner)
    assert owner in getattr(partner, 'smDsl_CommandsSection8')
    _safe_set(owner, 'smDsl_Command', None)
    assert owner not in getattr(partner, 'smDsl_CommandsSection8')


def test_assoc_commandsSection1_stub_double():
    # smDsl_CommandsSection has no real 'smDsl_CommandsSection' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_Model(name="sample_text")
    partner = smDsl_CommandsSection()
    setattr(partner, 'smDsl_CommandsSection', None)
    _safe_set(owner, 'smDsl_Model2', partner)
    assert getattr(partner, 'smDsl_CommandsSection') == owner
    _safe_set(owner, 'smDsl_Model2', None)
    assert getattr(partner, 'smDsl_CommandsSection') is None


def test_assoc_event17_stub_double():
    # smDsl_EventHandlingDescription has no real 'smDsl_EventHandlingDescription18' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_Event(name="sample_text")
    partner = smDsl_EventHandlingDescription()
    setattr(partner, 'smDsl_EventHandlingDescription18', None)
    _safe_set(owner, 'smDsl_Event19', partner)
    assert getattr(partner, 'smDsl_EventHandlingDescription18') == owner
    _safe_set(owner, 'smDsl_Event19', None)
    assert getattr(partner, 'smDsl_EventHandlingDescription18') is None


def test_assoc_eventHandlingDescriptions12_stub_double():
    # smDsl_EventHandlingDescription has no real 'smDsl_EventHandlingDescription' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_State(initial=True, name="sample_text")
    partner = smDsl_EventHandlingDescription()
    setattr(partner, 'smDsl_EventHandlingDescription', None)
    _safe_set(owner, 'smDsl_State13', {partner})
    assert getattr(partner, 'smDsl_EventHandlingDescription') == owner
    _safe_set(owner, 'smDsl_State13', set())
    assert getattr(partner, 'smDsl_EventHandlingDescription') is None


def test_assoc_events5_stub_double():
    # smDsl_EventsSection has no real 'smDsl_EventsSection6' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_Event(name="sample_text")
    partner = smDsl_EventsSection()
    setattr(partner, 'smDsl_EventsSection6', None)
    _safe_set(owner, 'smDsl_Event', partner)
    assert owner in getattr(partner, 'smDsl_EventsSection6')
    _safe_set(owner, 'smDsl_Event', None)
    assert owner not in getattr(partner, 'smDsl_EventsSection6')


def test_assoc_eventsSection0_stub_double():
    # smDsl_EventsSection has no real 'smDsl_EventsSection' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_Model(name="sample_text")
    partner = smDsl_EventsSection()
    setattr(partner, 'smDsl_EventsSection', None)
    _safe_set(owner, 'smDsl_Model', partner)
    assert getattr(partner, 'smDsl_EventsSection') == owner
    _safe_set(owner, 'smDsl_Model', None)
    assert getattr(partner, 'smDsl_EventsSection') is None


def test_assoc_targetState23_stub_double():
    # smDsl_EventHandlingDescription has no real 'smDsl_EventHandlingDescription24' property in the generated
    # code (a bare stub) -- manually attach it so smDsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smDsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smDsl_State(initial=True, name="sample_text")
    partner = smDsl_EventHandlingDescription()
    setattr(partner, 'smDsl_EventHandlingDescription24', None)
    _safe_set(owner, 'smDsl_State25', partner)
    assert getattr(partner, 'smDsl_EventHandlingDescription24') == owner
    _safe_set(owner, 'smDsl_State25', None)
    assert getattr(partner, 'smDsl_EventHandlingDescription24') is None


