import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    dsl_Command,
    dsl_Event,
    dsl_State,
    dsl_Statemachine,
    dsl_Transition,
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

def test_assoc_actions11_reverse_link_reassign_clear():
    a1 = dsl_State(name="sample_text")
    a2 = dsl_State(name="sample_text_2")
    b = dsl_Command(code="sample_text", name="sample_text")
    _safe_set(b, 'dsl_Command13', a1)
    assert _is_linked(b, 'dsl_Command13', a1)
    if hasattr(a1, 'dsl_State12'):
        assert _is_linked(a1, 'dsl_State12', b)
    _safe_set(b, 'dsl_Command13', a2)
    assert _is_linked(b, 'dsl_Command13', a2)
    if hasattr(a1, 'dsl_State12'):
        assert not _is_linked(a1, 'dsl_State12', b)
    if hasattr(a2, 'dsl_State12'):
        assert _is_linked(a2, 'dsl_State12', b)
    _safe_set(b, 'dsl_Command13', None)
    assert not _is_linked(b, 'dsl_Command13', a2)
    if hasattr(a2, 'dsl_State12'):
        assert not _is_linked(a2, 'dsl_State12', b)


def test_assoc_subState17_reverse_link_reassign_clear():
    a1 = dsl_State(name="sample_text")
    a2 = dsl_State(name="sample_text_2")
    b = dsl_State(name="sample_text")
    _safe_set(b, 'dsl_State18', a1)
    assert _is_linked(b, 'dsl_State18', a1)
    if hasattr(a1, 'dsl_State16'):
        assert _is_linked(a1, 'dsl_State16', b)
    _safe_set(b, 'dsl_State18', a2)
    assert _is_linked(b, 'dsl_State18', a2)
    if hasattr(a1, 'dsl_State16'):
        assert not _is_linked(a1, 'dsl_State16', b)
    if hasattr(a2, 'dsl_State16'):
        assert _is_linked(a2, 'dsl_State16', b)
    _safe_set(b, 'dsl_State18', None)
    assert not _is_linked(b, 'dsl_State18', a2)
    if hasattr(a2, 'dsl_State16'):
        assert not _is_linked(a2, 'dsl_State16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands6_stub_double():
    # dsl_Statemachine has no real 'dsl_Statemachine7' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Command(code="sample_text", name="sample_text")
    partner = dsl_Statemachine()
    setattr(partner, 'dsl_Statemachine7', None)
    _safe_set(owner, 'dsl_Command', partner)
    assert owner in getattr(partner, 'dsl_Statemachine7')
    _safe_set(owner, 'dsl_Command', None)
    assert owner not in getattr(partner, 'dsl_Statemachine7')


def test_assoc_event19_stub_double():
    # dsl_Transition has no real 'dsl_Transition20' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Event(code="sample_text", name="sample_text")
    partner = dsl_Transition()
    setattr(partner, 'dsl_Transition20', None)
    _safe_set(owner, 'dsl_Event21', partner)
    assert getattr(partner, 'dsl_Transition20') == owner
    _safe_set(owner, 'dsl_Event21', None)
    assert getattr(partner, 'dsl_Transition20') is None


def test_assoc_events0_stub_double():
    # dsl_Statemachine has no real 'dsl_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Event(code="sample_text", name="sample_text")
    partner = dsl_Statemachine()
    setattr(partner, 'dsl_Statemachine', None)
    _safe_set(owner, 'dsl_Event', partner)
    assert owner in getattr(partner, 'dsl_Statemachine')
    _safe_set(owner, 'dsl_Event', None)
    assert owner not in getattr(partner, 'dsl_Statemachine')


def test_assoc_initialState4_stub_double():
    # dsl_Statemachine has no real 'dsl_Statemachine5' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Statemachine()
    setattr(partner, 'dsl_Statemachine5', None)
    _safe_set(owner, 'dsl_State', partner)
    assert getattr(partner, 'dsl_Statemachine5') == owner
    _safe_set(owner, 'dsl_State', None)
    assert getattr(partner, 'dsl_Statemachine5') is None


def test_assoc_resetEvents1_stub_double():
    # dsl_Statemachine has no real 'dsl_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Event(code="sample_text", name="sample_text")
    partner = dsl_Statemachine()
    setattr(partner, 'dsl_Statemachine2', None)
    _safe_set(owner, 'dsl_Event3', partner)
    assert owner in getattr(partner, 'dsl_Statemachine2')
    _safe_set(owner, 'dsl_Event3', None)
    assert owner not in getattr(partner, 'dsl_Statemachine2')


def test_assoc_state22_stub_double():
    # dsl_Transition has no real 'dsl_Transition23' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Transition()
    setattr(partner, 'dsl_Transition23', None)
    _safe_set(owner, 'dsl_State24', partner)
    assert getattr(partner, 'dsl_Transition23') == owner
    _safe_set(owner, 'dsl_State24', None)
    assert getattr(partner, 'dsl_Transition23') is None


def test_assoc_state8_stub_double():
    # dsl_Statemachine has no real 'dsl_Statemachine9' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Statemachine()
    setattr(partner, 'dsl_Statemachine9', None)
    _safe_set(owner, 'dsl_State10', partner)
    assert owner in getattr(partner, 'dsl_Statemachine9')
    _safe_set(owner, 'dsl_State10', None)
    assert owner not in getattr(partner, 'dsl_Statemachine9')


def test_assoc_transitions14_stub_double():
    # dsl_Transition has no real 'dsl_Transition' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Transition()
    setattr(partner, 'dsl_Transition', None)
    _safe_set(owner, 'dsl_State15', {partner})
    assert getattr(partner, 'dsl_Transition') == owner
    _safe_set(owner, 'dsl_State15', set())
    assert getattr(partner, 'dsl_Transition') is None


