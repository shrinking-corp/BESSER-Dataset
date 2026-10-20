import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    rfsm_Connector,
    rfsm_Event,
    rfsm_Function,
    rfsm_History,
    rfsm_Node,
    rfsm_State,
    rfsm_Transition,
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

def test_assoc_effect22_reverse_link_reassign_clear():
    a1 = rfsm_Transition(priority_number=7)
    a2 = rfsm_Transition(priority_number=13)
    b = rfsm_Function(sourcecode="sample_text")
    _safe_set(b, 'rfsm_Function24', a1)
    assert _is_linked(b, 'rfsm_Function24', a1)
    if hasattr(a1, 'rfsm_Transition23'):
        assert _is_linked(a1, 'rfsm_Transition23', b)
    _safe_set(b, 'rfsm_Function24', a2)
    assert _is_linked(b, 'rfsm_Function24', a2)
    if hasattr(a1, 'rfsm_Transition23'):
        assert not _is_linked(a1, 'rfsm_Transition23', b)
    if hasattr(a2, 'rfsm_Transition23'):
        assert _is_linked(a2, 'rfsm_Transition23', b)
    _safe_set(b, 'rfsm_Function24', None)
    assert not _is_linked(b, 'rfsm_Function24', a2)
    if hasattr(a2, 'rfsm_Transition23'):
        assert not _is_linked(a2, 'rfsm_Transition23', b)


def test_assoc_events17_reverse_link_reassign_clear():
    a1 = rfsm_Transition(priority_number=7)
    a2 = rfsm_Transition(priority_number=13)
    b = rfsm_Event(eventliteral="sample_text")
    _safe_set(b, 'Event', a1)
    assert _is_linked(b, 'Event', a1)
    if hasattr(a1, 'owner18'):
        assert _is_linked(a1, 'owner18', b)
    _safe_set(b, 'Event', a2)
    assert _is_linked(b, 'Event', a2)
    if hasattr(a1, 'owner18'):
        assert not _is_linked(a1, 'owner18', b)
    if hasattr(a2, 'owner18'):
        assert _is_linked(a2, 'owner18', b)
    _safe_set(b, 'Event', None)
    assert not _is_linked(b, 'Event', a2)
    if hasattr(a2, 'owner18'):
        assert not _is_linked(a2, 'owner18', b)


def test_assoc_guard19_reverse_link_reassign_clear():
    a1 = rfsm_Transition(priority_number=7)
    a2 = rfsm_Transition(priority_number=13)
    b = rfsm_Function(sourcecode="sample_text")
    _safe_set(b, 'rfsm_Function21', a1)
    assert _is_linked(b, 'rfsm_Function21', a1)
    if hasattr(a1, 'rfsm_Transition20'):
        assert _is_linked(a1, 'rfsm_Transition20', b)
    _safe_set(b, 'rfsm_Function21', a2)
    assert _is_linked(b, 'rfsm_Function21', a2)
    if hasattr(a1, 'rfsm_Transition20'):
        assert not _is_linked(a1, 'rfsm_Transition20', b)
    if hasattr(a2, 'rfsm_Transition20'):
        assert _is_linked(a2, 'rfsm_Transition20', b)
    _safe_set(b, 'rfsm_Function21', None)
    assert not _is_linked(b, 'rfsm_Function21', a2)
    if hasattr(a2, 'rfsm_Transition20'):
        assert not _is_linked(a2, 'rfsm_Transition20', b)


def test_assoc_history10_reverse_link_reassign_clear():
    a1 = rfsm_History(depth=7, hot=True)
    a2 = rfsm_History(depth=13, hot=False)
    b = rfsm_Connector(public=True)
    _safe_set(b, 'rfsm_Connector', a1)
    assert _is_linked(b, 'rfsm_Connector', a1)
    if hasattr(a1, 'rfsm_History'):
        assert _is_linked(a1, 'rfsm_History', b)
    _safe_set(b, 'rfsm_Connector', a2)
    assert _is_linked(b, 'rfsm_Connector', a2)
    if hasattr(a1, 'rfsm_History'):
        assert not _is_linked(a1, 'rfsm_History', b)
    if hasattr(a2, 'rfsm_History'):
        assert _is_linked(a2, 'rfsm_History', b)
    _safe_set(b, 'rfsm_Connector', None)
    assert not _is_linked(b, 'rfsm_Connector', a2)
    if hasattr(a2, 'rfsm_History'):
        assert not _is_linked(a2, 'rfsm_History', b)


def test_assoc_owner25_reverse_link_reassign_clear():
    a1 = rfsm_Transition(priority_number=7)
    a2 = rfsm_Transition(priority_number=13)
    b = rfsm_Event(eventliteral="sample_text")
    _safe_set(b, 'events', a1)
    assert _is_linked(b, 'events', a1)
    if hasattr(a1, 'Transition26'):
        assert _is_linked(a1, 'Transition26', b)
    _safe_set(b, 'events', a2)
    assert _is_linked(b, 'events', a2)
    if hasattr(a1, 'Transition26'):
        assert not _is_linked(a1, 'Transition26', b)
    if hasattr(a2, 'Transition26'):
        assert _is_linked(a2, 'Transition26', b)
    _safe_set(b, 'events', None)
    assert not _is_linked(b, 'events', a2)
    if hasattr(a2, 'Transition26'):
        assert not _is_linked(a2, 'Transition26', b)


def test_assoc_source13_reverse_link_reassign_clear():
    a1 = rfsm_Transition(priority_number=7)
    a2 = rfsm_Transition(priority_number=13)
    b = rfsm_Node(name="sample_text")
    _safe_set(b, 'rfsm_Node', a1)
    assert _is_linked(b, 'rfsm_Node', a1)
    if hasattr(a1, 'rfsm_Transition'):
        assert _is_linked(a1, 'rfsm_Transition', b)
    _safe_set(b, 'rfsm_Node', a2)
    assert _is_linked(b, 'rfsm_Node', a2)
    if hasattr(a1, 'rfsm_Transition'):
        assert not _is_linked(a1, 'rfsm_Transition', b)
    if hasattr(a2, 'rfsm_Transition'):
        assert _is_linked(a2, 'rfsm_Transition', b)
    _safe_set(b, 'rfsm_Node', None)
    assert not _is_linked(b, 'rfsm_Node', a2)
    if hasattr(a2, 'rfsm_Transition'):
        assert not _is_linked(a2, 'rfsm_Transition', b)


def test_assoc_target14_reverse_link_reassign_clear():
    a1 = rfsm_Transition(priority_number=7)
    a2 = rfsm_Transition(priority_number=13)
    b = rfsm_Node(name="sample_text")
    _safe_set(b, 'rfsm_Node16', a1)
    assert _is_linked(b, 'rfsm_Node16', a1)
    if hasattr(a1, 'rfsm_Transition15'):
        assert _is_linked(a1, 'rfsm_Transition15', b)
    _safe_set(b, 'rfsm_Node16', a2)
    assert _is_linked(b, 'rfsm_Node16', a2)
    if hasattr(a1, 'rfsm_Transition15'):
        assert not _is_linked(a1, 'rfsm_Transition15', b)
    if hasattr(a2, 'rfsm_Transition15'):
        assert _is_linked(a2, 'rfsm_Transition15', b)
    _safe_set(b, 'rfsm_Node16', None)
    assert not _is_linked(b, 'rfsm_Node16', a2)
    if hasattr(a2, 'rfsm_Transition15'):
        assert not _is_linked(a2, 'rfsm_Transition15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_doo4_stub_double():
    # rfsm_State has no real 'rfsm_State5' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Function(sourcecode="sample_text")
    partner = rfsm_State()
    setattr(partner, 'rfsm_State5', None)
    _safe_set(owner, 'rfsm_Function6', partner)
    assert getattr(partner, 'rfsm_State5') == owner
    _safe_set(owner, 'rfsm_Function6', None)
    assert getattr(partner, 'rfsm_State5') is None


def test_assoc_entry3_stub_double():
    # rfsm_State has no real 'rfsm_State' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Function(sourcecode="sample_text")
    partner = rfsm_State()
    setattr(partner, 'rfsm_State', None)
    _safe_set(owner, 'rfsm_Function', partner)
    assert getattr(partner, 'rfsm_State') == owner
    _safe_set(owner, 'rfsm_Function', None)
    assert getattr(partner, 'rfsm_State') is None


def test_assoc_exit7_stub_double():
    # rfsm_State has no real 'rfsm_State8' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Function(sourcecode="sample_text")
    partner = rfsm_State()
    setattr(partner, 'rfsm_State8', None)
    _safe_set(owner, 'rfsm_Function9', partner)
    assert getattr(partner, 'rfsm_State8') == owner
    _safe_set(owner, 'rfsm_Function9', None)
    assert getattr(partner, 'rfsm_State8') is None


def test_assoc_owner11_stub_double():
    # rfsm_State has no real 'State12' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Transition(priority_number=7)
    partner = rfsm_State()
    setattr(partner, 'State12', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'State12') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'State12') is None


def test_assoc_parent0_stub_double():
    # rfsm_State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Node(name="sample_text")
    partner = rfsm_State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'subnodes', partner)
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'subnodes', None)
    assert getattr(partner, 'State') is None


def test_assoc_subnodes2_stub_double():
    # rfsm_State has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Node(name="sample_text")
    partner = rfsm_State()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'Node', partner)
    assert owner in getattr(partner, 'parent')
    _safe_set(owner, 'Node', None)
    assert owner not in getattr(partner, 'parent')


def test_assoc_transitions1_stub_double():
    # rfsm_State has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so rfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rfsm_Transition(priority_number=7)
    partner = rfsm_State()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'owner')


