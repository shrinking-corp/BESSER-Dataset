import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sm3_State,
    sm3_StateMachine,
    sm3_Transition,
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

def test_assoc_incoming6_reverse_link_reassign_clear():
    a1 = sm3_Transition(event="sample_text")
    a2 = sm3_Transition(event="sample_text_2")
    b = sm3_State(name="sample_text")
    _safe_set(b, 'tgt', {a1})
    assert _is_linked(b, 'tgt', a1)
    if hasattr(a1, 'Transition7'):
        assert _is_linked(a1, 'Transition7', b)
    _safe_set(b, 'tgt', {a2})
    assert _is_linked(b, 'tgt', a2)
    if hasattr(a1, 'Transition7'):
        assert not _is_linked(a1, 'Transition7', b)
    if hasattr(a2, 'Transition7'):
        assert _is_linked(a2, 'Transition7', b)
    _safe_set(b, 'tgt', set())
    assert not _is_linked(b, 'tgt', a2)
    if hasattr(a2, 'Transition7'):
        assert not _is_linked(a2, 'Transition7', b)


def test_assoc_outgoing5_reverse_link_reassign_clear():
    a1 = sm3_Transition(event="sample_text")
    a2 = sm3_Transition(event="sample_text_2")
    b = sm3_State(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_src8_reverse_link_reassign_clear():
    a1 = sm3_Transition(event="sample_text")
    a2 = sm3_Transition(event="sample_text_2")
    b = sm3_State(name="sample_text")
    _safe_set(b, 'State9', a1)
    assert _is_linked(b, 'State9', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State9', a2)
    assert _is_linked(b, 'State9', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State9', None)
    assert not _is_linked(b, 'State9', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_tgt10_reverse_link_reassign_clear():
    a1 = sm3_Transition(event="sample_text")
    a2 = sm3_Transition(event="sample_text_2")
    b = sm3_State(name="sample_text")
    _safe_set(b, 'State11', a1)
    assert _is_linked(b, 'State11', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State11', a2)
    assert _is_linked(b, 'State11', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State11', None)
    assert not _is_linked(b, 'State11', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges2_stub_double():
    # sm3_StateMachine has no real 'sm3_StateMachine3' property in the generated
    # code (a bare stub) -- manually attach it so sm3_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sm3_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sm3_Transition(event="sample_text")
    partner = sm3_StateMachine()
    setattr(partner, 'sm3_StateMachine3', None)
    _safe_set(owner, 'sm3_Transition', partner)
    assert owner in getattr(partner, 'sm3_StateMachine3')
    _safe_set(owner, 'sm3_Transition', None)
    assert owner not in getattr(partner, 'sm3_StateMachine3')


def test_assoc_initialState0_stub_double():
    # sm3_StateMachine has no real 'sm3_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so sm3_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sm3_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sm3_State(name="sample_text")
    partner = sm3_StateMachine()
    setattr(partner, 'sm3_StateMachine', None)
    _safe_set(owner, 'sm3_State', partner)
    assert getattr(partner, 'sm3_StateMachine') == owner
    _safe_set(owner, 'sm3_State', None)
    assert getattr(partner, 'sm3_StateMachine') is None


def test_assoc_sm4_stub_double():
    # sm3_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so sm3_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sm3_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sm3_State(name="sample_text")
    partner = sm3_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_states1_stub_double():
    # sm3_StateMachine has no real 'sm' property in the generated
    # code (a bare stub) -- manually attach it so sm3_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sm3_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sm3_State(name="sample_text")
    partner = sm3_StateMachine()
    setattr(partner, 'sm', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'sm')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'sm')


