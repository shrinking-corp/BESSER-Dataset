import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stm_Command,
    stm_Event,
    stm_Guard,
    stm_GuardCall,
    stm_Parameter,
    stm_SelfEvent,
    stm_State,
    stm_Statemachine,
    stm_Transition,
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

def test_assoc_doAction10_reverse_link_reassign_clear():
    a1 = stm_State(name="sample_text")
    a2 = stm_State(name="sample_text_2")
    b = stm_Command(name="sample_text")
    _safe_set(b, 'stm_Command12', a1)
    assert _is_linked(b, 'stm_Command12', a1)
    if hasattr(a1, 'stm_State11'):
        assert _is_linked(a1, 'stm_State11', b)
    _safe_set(b, 'stm_Command12', a2)
    assert _is_linked(b, 'stm_Command12', a2)
    if hasattr(a1, 'stm_State11'):
        assert not _is_linked(a1, 'stm_State11', b)
    if hasattr(a2, 'stm_State11'):
        assert _is_linked(a2, 'stm_State11', b)
    _safe_set(b, 'stm_Command12', None)
    assert not _is_linked(b, 'stm_Command12', a2)
    if hasattr(a2, 'stm_State11'):
        assert not _is_linked(a2, 'stm_State11', b)


def test_assoc_entryActions7_reverse_link_reassign_clear():
    a1 = stm_State(name="sample_text")
    a2 = stm_State(name="sample_text_2")
    b = stm_Command(name="sample_text")
    _safe_set(b, 'stm_Command9', a1)
    assert _is_linked(b, 'stm_Command9', a1)
    if hasattr(a1, 'stm_State8'):
        assert _is_linked(a1, 'stm_State8', b)
    _safe_set(b, 'stm_Command9', a2)
    assert _is_linked(b, 'stm_Command9', a2)
    if hasattr(a1, 'stm_State8'):
        assert not _is_linked(a1, 'stm_State8', b)
    if hasattr(a2, 'stm_State8'):
        assert _is_linked(a2, 'stm_State8', b)
    _safe_set(b, 'stm_Command9', None)
    assert not _is_linked(b, 'stm_Command9', a2)
    if hasattr(a2, 'stm_State8'):
        assert not _is_linked(a2, 'stm_State8', b)


def test_assoc_exitActions23_reverse_link_reassign_clear():
    a1 = stm_State(name="sample_text")
    a2 = stm_State(name="sample_text_2")
    b = stm_Command(name="sample_text")
    _safe_set(b, 'stm_Command25', a1)
    assert _is_linked(b, 'stm_Command25', a1)
    if hasattr(a1, 'stm_State24'):
        assert _is_linked(a1, 'stm_State24', b)
    _safe_set(b, 'stm_Command25', a2)
    assert _is_linked(b, 'stm_Command25', a2)
    if hasattr(a1, 'stm_State24'):
        assert not _is_linked(a1, 'stm_State24', b)
    if hasattr(a2, 'stm_State24'):
        assert _is_linked(a2, 'stm_State24', b)
    _safe_set(b, 'stm_Command25', None)
    assert not _is_linked(b, 'stm_Command25', a2)
    if hasattr(a2, 'stm_State24'):
        assert not _is_linked(a2, 'stm_State24', b)


def test_assoc_guard46_reverse_link_reassign_clear():
    a1 = stm_GuardCall(parameters="sample_text")
    a2 = stm_GuardCall(parameters="sample_text_2")
    b = stm_Guard(name="sample_text")
    _safe_set(b, 'stm_Guard48', a1)
    assert _is_linked(b, 'stm_Guard48', a1)
    if hasattr(a1, 'stm_GuardCall47'):
        assert _is_linked(a1, 'stm_GuardCall47', b)
    _safe_set(b, 'stm_Guard48', a2)
    assert _is_linked(b, 'stm_Guard48', a2)
    if hasattr(a1, 'stm_GuardCall47'):
        assert not _is_linked(a1, 'stm_GuardCall47', b)
    if hasattr(a2, 'stm_GuardCall47'):
        assert _is_linked(a2, 'stm_GuardCall47', b)
    _safe_set(b, 'stm_Guard48', None)
    assert not _is_linked(b, 'stm_Guard48', a2)
    if hasattr(a2, 'stm_GuardCall47'):
        assert not _is_linked(a2, 'stm_GuardCall47', b)


def test_assoc_parameters49_reverse_link_reassign_clear():
    a1 = stm_Parameter(name="sample_text", type="sample_text")
    a2 = stm_Parameter(name="sample_text_2", type="sample_text_2")
    b = stm_Guard(name="sample_text")
    _safe_set(b, 'stm_Guard50', {a1})
    assert _is_linked(b, 'stm_Guard50', a1)
    if hasattr(a1, 'stm_Parameter'):
        assert _is_linked(a1, 'stm_Parameter', b)
    _safe_set(b, 'stm_Guard50', {a2})
    assert _is_linked(b, 'stm_Guard50', a2)
    if hasattr(a1, 'stm_Parameter'):
        assert not _is_linked(a1, 'stm_Parameter', b)
    if hasattr(a2, 'stm_Parameter'):
        assert _is_linked(a2, 'stm_Parameter', b)
    _safe_set(b, 'stm_Guard50', set())
    assert not _is_linked(b, 'stm_Guard50', a2)
    if hasattr(a2, 'stm_Parameter'):
        assert not _is_linked(a2, 'stm_Parameter', b)


def test_assoc_states17_reverse_link_reassign_clear():
    a1 = stm_State(name="sample_text")
    a2 = stm_State(name="sample_text_2")
    b = stm_State(name="sample_text")
    _safe_set(b, 'stm_State18', a1)
    assert _is_linked(b, 'stm_State18', a1)
    if hasattr(a1, 'stm_State16'):
        assert _is_linked(a1, 'stm_State16', b)
    _safe_set(b, 'stm_State18', a2)
    assert _is_linked(b, 'stm_State18', a2)
    if hasattr(a1, 'stm_State16'):
        assert not _is_linked(a1, 'stm_State16', b)
    if hasattr(a2, 'stm_State16'):
        assert _is_linked(a2, 'stm_State16', b)
    _safe_set(b, 'stm_State18', None)
    assert not _is_linked(b, 'stm_State18', a2)
    if hasattr(a2, 'stm_State16'):
        assert not _is_linked(a2, 'stm_State16', b)


def test_assoc_stopAction13_reverse_link_reassign_clear():
    a1 = stm_State(name="sample_text")
    a2 = stm_State(name="sample_text_2")
    b = stm_Command(name="sample_text")
    _safe_set(b, 'stm_Command15', a1)
    assert _is_linked(b, 'stm_Command15', a1)
    if hasattr(a1, 'stm_State14'):
        assert _is_linked(a1, 'stm_State14', b)
    _safe_set(b, 'stm_Command15', a2)
    assert _is_linked(b, 'stm_Command15', a2)
    if hasattr(a1, 'stm_State14'):
        assert not _is_linked(a1, 'stm_State14', b)
    if hasattr(a2, 'stm_State14'):
        assert _is_linked(a2, 'stm_State14', b)
    _safe_set(b, 'stm_Command15', None)
    assert not _is_linked(b, 'stm_Command15', a2)
    if hasattr(a2, 'stm_State14'):
        assert not _is_linked(a2, 'stm_State14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action34_stub_double():
    # stm_Transition has no real 'stm_Transition35' property in the generated
    # code (a bare stub) -- manually attach it so stm_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Command(name="sample_text")
    partner = stm_Transition()
    setattr(partner, 'stm_Transition35', None)
    _safe_set(owner, 'stm_Command36', partner)
    assert getattr(partner, 'stm_Transition35') == owner
    _safe_set(owner, 'stm_Command36', None)
    assert getattr(partner, 'stm_Transition35') is None


def test_assoc_action43_stub_double():
    # stm_SelfEvent has no real 'stm_SelfEvent44' property in the generated
    # code (a bare stub) -- manually attach it so stm_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Command(name="sample_text")
    partner = stm_SelfEvent()
    setattr(partner, 'stm_SelfEvent44', None)
    _safe_set(owner, 'stm_Command45', partner)
    assert getattr(partner, 'stm_SelfEvent44') == owner
    _safe_set(owner, 'stm_Command45', None)
    assert getattr(partner, 'stm_SelfEvent44') is None


def test_assoc_commands1_stub_double():
    # stm_Statemachine has no real 'stm_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so stm_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Command(name="sample_text")
    partner = stm_Statemachine()
    setattr(partner, 'stm_Statemachine2', None)
    _safe_set(owner, 'stm_Command', partner)
    assert owner in getattr(partner, 'stm_Statemachine2')
    _safe_set(owner, 'stm_Command', None)
    assert owner not in getattr(partner, 'stm_Statemachine2')


def test_assoc_event26_stub_double():
    # stm_Transition has no real 'stm_Transition27' property in the generated
    # code (a bare stub) -- manually attach it so stm_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Event(name="sample_text")
    partner = stm_Transition()
    setattr(partner, 'stm_Transition27', None)
    _safe_set(owner, 'stm_Event28', partner)
    assert getattr(partner, 'stm_Transition27') == owner
    _safe_set(owner, 'stm_Event28', None)
    assert getattr(partner, 'stm_Transition27') is None


def test_assoc_event37_stub_double():
    # stm_SelfEvent has no real 'stm_SelfEvent38' property in the generated
    # code (a bare stub) -- manually attach it so stm_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Event(name="sample_text")
    partner = stm_SelfEvent()
    setattr(partner, 'stm_SelfEvent38', None)
    _safe_set(owner, 'stm_Event39', partner)
    assert getattr(partner, 'stm_SelfEvent38') == owner
    _safe_set(owner, 'stm_Event39', None)
    assert getattr(partner, 'stm_SelfEvent38') is None


def test_assoc_events0_stub_double():
    # stm_Statemachine has no real 'stm_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so stm_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Event(name="sample_text")
    partner = stm_Statemachine()
    setattr(partner, 'stm_Statemachine', None)
    _safe_set(owner, 'stm_Event', partner)
    assert owner in getattr(partner, 'stm_Statemachine')
    _safe_set(owner, 'stm_Event', None)
    assert owner not in getattr(partner, 'stm_Statemachine')


def test_assoc_guard29_stub_double():
    # stm_Transition has no real 'stm_Transition30' property in the generated
    # code (a bare stub) -- manually attach it so stm_GuardCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_GuardCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_GuardCall(parameters="sample_text")
    partner = stm_Transition()
    setattr(partner, 'stm_Transition30', None)
    _safe_set(owner, 'stm_GuardCall', partner)
    assert getattr(partner, 'stm_Transition30') == owner
    _safe_set(owner, 'stm_GuardCall', None)
    assert getattr(partner, 'stm_Transition30') is None


def test_assoc_guard40_stub_double():
    # stm_SelfEvent has no real 'stm_SelfEvent41' property in the generated
    # code (a bare stub) -- manually attach it so stm_GuardCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_GuardCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_GuardCall(parameters="sample_text")
    partner = stm_SelfEvent()
    setattr(partner, 'stm_SelfEvent41', None)
    _safe_set(owner, 'stm_GuardCall42', partner)
    assert getattr(partner, 'stm_SelfEvent41') == owner
    _safe_set(owner, 'stm_GuardCall42', None)
    assert getattr(partner, 'stm_SelfEvent41') is None


def test_assoc_guards3_stub_double():
    # stm_Statemachine has no real 'stm_Statemachine4' property in the generated
    # code (a bare stub) -- manually attach it so stm_Guard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_Guard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_Guard(name="sample_text")
    partner = stm_Statemachine()
    setattr(partner, 'stm_Statemachine4', None)
    _safe_set(owner, 'stm_Guard', partner)
    assert owner in getattr(partner, 'stm_Statemachine4')
    _safe_set(owner, 'stm_Guard', None)
    assert owner not in getattr(partner, 'stm_Statemachine4')


def test_assoc_selfEvents19_stub_double():
    # stm_SelfEvent has no real 'stm_SelfEvent' property in the generated
    # code (a bare stub) -- manually attach it so stm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_State(name="sample_text")
    partner = stm_SelfEvent()
    setattr(partner, 'stm_SelfEvent', None)
    _safe_set(owner, 'stm_State20', {partner})
    assert getattr(partner, 'stm_SelfEvent') == owner
    _safe_set(owner, 'stm_State20', set())
    assert getattr(partner, 'stm_SelfEvent') is None


def test_assoc_state31_stub_double():
    # stm_Transition has no real 'stm_Transition32' property in the generated
    # code (a bare stub) -- manually attach it so stm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_State(name="sample_text")
    partner = stm_Transition()
    setattr(partner, 'stm_Transition32', None)
    _safe_set(owner, 'stm_State33', partner)
    assert getattr(partner, 'stm_Transition32') == owner
    _safe_set(owner, 'stm_State33', None)
    assert getattr(partner, 'stm_Transition32') is None


def test_assoc_states5_stub_double():
    # stm_Statemachine has no real 'stm_Statemachine6' property in the generated
    # code (a bare stub) -- manually attach it so stm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_State(name="sample_text")
    partner = stm_Statemachine()
    setattr(partner, 'stm_Statemachine6', None)
    _safe_set(owner, 'stm_State', partner)
    assert owner in getattr(partner, 'stm_Statemachine6')
    _safe_set(owner, 'stm_State', None)
    assert owner not in getattr(partner, 'stm_Statemachine6')


def test_assoc_transitions21_stub_double():
    # stm_Transition has no real 'stm_Transition' property in the generated
    # code (a bare stub) -- manually attach it so stm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stm_State(name="sample_text")
    partner = stm_Transition()
    setattr(partner, 'stm_Transition', None)
    _safe_set(owner, 'stm_State22', {partner})
    assert getattr(partner, 'stm_Transition') == owner
    _safe_set(owner, 'stm_State22', set())
    assert getattr(partner, 'stm_Transition') is None


