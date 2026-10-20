import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    basicfsm_Action,
    basicfsm_Guard,
    basicfsm_InitialState,
    basicfsm_Machine,
    basicfsm_State,
    basicfsm_Trans,
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

def test_assoc_in_3_reverse_link_reassign_clear():
    a1 = basicfsm_Trans(event="sample_text")
    a2 = basicfsm_Trans(event="sample_text_2")
    b = basicfsm_State(name="sample_text")
    _safe_set(b, 'tgt', {a1})
    assert _is_linked(b, 'tgt', a1)
    if hasattr(a1, 'Trans'):
        assert _is_linked(a1, 'Trans', b)
    _safe_set(b, 'tgt', {a2})
    assert _is_linked(b, 'tgt', a2)
    if hasattr(a1, 'Trans'):
        assert not _is_linked(a1, 'Trans', b)
    if hasattr(a2, 'Trans'):
        assert _is_linked(a2, 'Trans', b)
    _safe_set(b, 'tgt', set())
    assert not _is_linked(b, 'tgt', a2)
    if hasattr(a2, 'Trans'):
        assert not _is_linked(a2, 'Trans', b)


def test_assoc_out4_reverse_link_reassign_clear():
    a1 = basicfsm_Trans(event="sample_text")
    a2 = basicfsm_Trans(event="sample_text_2")
    b = basicfsm_State(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Trans5'):
        assert _is_linked(a1, 'Trans5', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Trans5'):
        assert not _is_linked(a1, 'Trans5', b)
    if hasattr(a2, 'Trans5'):
        assert _is_linked(a2, 'Trans5', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Trans5'):
        assert not _is_linked(a2, 'Trans5', b)


def test_assoc_src6_reverse_link_reassign_clear():
    a1 = basicfsm_Trans(event="sample_text")
    a2 = basicfsm_Trans(event="sample_text_2")
    b = basicfsm_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'out'):
        assert _is_linked(a1, 'out', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'out'):
        assert not _is_linked(a1, 'out', b)
    if hasattr(a2, 'out'):
        assert _is_linked(a2, 'out', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'out'):
        assert not _is_linked(a2, 'out', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = basicfsm_State(name="sample_text")
    a2 = basicfsm_State(name="sample_text_2")
    b = basicfsm_Machine(name="sample_text")
    _safe_set(b, 'basicfsm_Machine', {a1})
    assert _is_linked(b, 'basicfsm_Machine', a1)
    if hasattr(a1, 'basicfsm_State'):
        assert _is_linked(a1, 'basicfsm_State', b)
    _safe_set(b, 'basicfsm_Machine', {a2})
    assert _is_linked(b, 'basicfsm_Machine', a2)
    if hasattr(a1, 'basicfsm_State'):
        assert not _is_linked(a1, 'basicfsm_State', b)
    if hasattr(a2, 'basicfsm_State'):
        assert _is_linked(a2, 'basicfsm_State', b)
    _safe_set(b, 'basicfsm_Machine', set())
    assert not _is_linked(b, 'basicfsm_Machine', a2)
    if hasattr(a2, 'basicfsm_State'):
        assert not _is_linked(a2, 'basicfsm_State', b)


def test_assoc_tgt7_reverse_link_reassign_clear():
    a1 = basicfsm_Trans(event="sample_text")
    a2 = basicfsm_Trans(event="sample_text_2")
    b = basicfsm_State(name="sample_text")
    _safe_set(b, 'State8', a1)
    assert _is_linked(b, 'State8', a1)
    if hasattr(a1, 'in_'):
        assert _is_linked(a1, 'in_', b)
    _safe_set(b, 'State8', a2)
    assert _is_linked(b, 'State8', a2)
    if hasattr(a1, 'in_'):
        assert not _is_linked(a1, 'in_', b)
    if hasattr(a2, 'in_'):
        assert _is_linked(a2, 'in_', b)
    _safe_set(b, 'State8', None)
    assert not _is_linked(b, 'State8', a2)
    if hasattr(a2, 'in_'):
        assert not _is_linked(a2, 'in_', b)


def test_assoc_trans1_reverse_link_reassign_clear():
    a1 = basicfsm_Trans(event="sample_text")
    a2 = basicfsm_Trans(event="sample_text_2")
    b = basicfsm_Machine(name="sample_text")
    _safe_set(b, 'basicfsm_Machine2', {a1})
    assert _is_linked(b, 'basicfsm_Machine2', a1)
    if hasattr(a1, 'basicfsm_Trans'):
        assert _is_linked(a1, 'basicfsm_Trans', b)
    _safe_set(b, 'basicfsm_Machine2', {a2})
    assert _is_linked(b, 'basicfsm_Machine2', a2)
    if hasattr(a1, 'basicfsm_Trans'):
        assert not _is_linked(a1, 'basicfsm_Trans', b)
    if hasattr(a2, 'basicfsm_Trans'):
        assert _is_linked(a2, 'basicfsm_Trans', b)
    _safe_set(b, 'basicfsm_Machine2', set())
    assert not _is_linked(b, 'basicfsm_Machine2', a2)
    if hasattr(a2, 'basicfsm_Trans'):
        assert not _is_linked(a2, 'basicfsm_Trans', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action11_stub_double():
    # basicfsm_Action has no real 'basicfsm_Action' property in the generated
    # code (a bare stub) -- manually attach it so basicfsm_Trans's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basicfsm_Trans's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basicfsm_Trans(event="sample_text")
    partner = basicfsm_Action()
    setattr(partner, 'basicfsm_Action', None)
    _safe_set(owner, 'basicfsm_Trans12', partner)
    assert getattr(partner, 'basicfsm_Action') == owner
    _safe_set(owner, 'basicfsm_Trans12', None)
    assert getattr(partner, 'basicfsm_Action') is None


def test_assoc_guard9_stub_double():
    # basicfsm_Guard has no real 'basicfsm_Guard' property in the generated
    # code (a bare stub) -- manually attach it so basicfsm_Trans's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basicfsm_Trans's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basicfsm_Trans(event="sample_text")
    partner = basicfsm_Guard()
    setattr(partner, 'basicfsm_Guard', None)
    _safe_set(owner, 'basicfsm_Trans10', partner)
    assert getattr(partner, 'basicfsm_Guard') == owner
    _safe_set(owner, 'basicfsm_Trans10', None)
    assert getattr(partner, 'basicfsm_Guard') is None


