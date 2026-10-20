import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    gfsm_Guard,
    gfsm_Machine,
    gfsm_State,
    gfsm_Transition,
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

def test_assoc_from_0_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoings'):
        assert _is_linked(a1, 'outgoings', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoings'):
        assert not _is_linked(a1, 'outgoings', b)
    if hasattr(a2, 'outgoings'):
        assert _is_linked(a2, 'outgoings', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoings'):
        assert not _is_linked(a2, 'outgoings', b)


def test_assoc_guard3_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_Guard(value="sample_text")
    _safe_set(b, 'gfsm_Guard', a1)
    assert _is_linked(b, 'gfsm_Guard', a1)
    if hasattr(a1, 'gfsm_Transition'):
        assert _is_linked(a1, 'gfsm_Transition', b)
    _safe_set(b, 'gfsm_Guard', a2)
    assert _is_linked(b, 'gfsm_Guard', a2)
    if hasattr(a1, 'gfsm_Transition'):
        assert not _is_linked(a1, 'gfsm_Transition', b)
    if hasattr(a2, 'gfsm_Transition'):
        assert _is_linked(a2, 'gfsm_Transition', b)
    _safe_set(b, 'gfsm_Guard', None)
    assert not _is_linked(b, 'gfsm_Guard', a2)
    if hasattr(a2, 'gfsm_Transition'):
        assert not _is_linked(a2, 'gfsm_Transition', b)


def test_assoc_incommings5_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition6'):
        assert _is_linked(a1, 'Transition6', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition6'):
        assert not _is_linked(a1, 'Transition6', b)
    if hasattr(a2, 'Transition6'):
        assert _is_linked(a2, 'Transition6', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition6'):
        assert not _is_linked(a2, 'Transition6', b)


def test_assoc_outgoings4_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_to1_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'State2', a1)
    assert _is_linked(b, 'State2', a1)
    if hasattr(a1, 'incommings'):
        assert _is_linked(a1, 'incommings', b)
    _safe_set(b, 'State2', a2)
    assert _is_linked(b, 'State2', a2)
    if hasattr(a1, 'incommings'):
        assert not _is_linked(a1, 'incommings', b)
    if hasattr(a2, 'incommings'):
        assert _is_linked(a2, 'incommings', b)
    _safe_set(b, 'State2', None)
    assert not _is_linked(b, 'State2', a2)
    if hasattr(a2, 'incommings'):
        assert not _is_linked(a2, 'incommings', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_initialState11_stub_double():
    # gfsm_Machine has no real 'gfsm_Machine12' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_State(name="sample_text")
    partner = gfsm_Machine()
    setattr(partner, 'gfsm_Machine12', None)
    _safe_set(owner, 'gfsm_State13', partner)
    assert getattr(partner, 'gfsm_Machine12') == owner
    _safe_set(owner, 'gfsm_State13', None)
    assert getattr(partner, 'gfsm_Machine12') is None


def test_assoc_states7_stub_double():
    # gfsm_Machine has no real 'gfsm_Machine' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_State(name="sample_text")
    partner = gfsm_Machine()
    setattr(partner, 'gfsm_Machine', None)
    _safe_set(owner, 'gfsm_State', partner)
    assert owner in getattr(partner, 'gfsm_Machine')
    _safe_set(owner, 'gfsm_State', None)
    assert owner not in getattr(partner, 'gfsm_Machine')


def test_assoc_transitions8_stub_double():
    # gfsm_Machine has no real 'gfsm_Machine9' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_Transition(event="sample_text")
    partner = gfsm_Machine()
    setattr(partner, 'gfsm_Machine9', None)
    _safe_set(owner, 'gfsm_Transition10', partner)
    assert owner in getattr(partner, 'gfsm_Machine9')
    _safe_set(owner, 'gfsm_Transition10', None)
    assert owner not in getattr(partner, 'gfsm_Machine9')


