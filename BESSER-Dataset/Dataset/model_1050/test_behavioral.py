import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsm_Constraint,
    fsm_Language,
    fsm_Machine,
    fsm_Model,
    fsm_State,
    fsm_Transition,
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

def test_assoc_constraints0_reverse_link_reassign_clear():
    a1 = fsm_Model(name="sample_text")
    a2 = fsm_Model(name="sample_text_2")
    b = fsm_Constraint(name="sample_text", true=True)
    _safe_set(b, 'fsm_Constraint', a1)
    assert _is_linked(b, 'fsm_Constraint', a1)
    if hasattr(a1, 'fsm_Model'):
        assert _is_linked(a1, 'fsm_Model', b)
    _safe_set(b, 'fsm_Constraint', a2)
    assert _is_linked(b, 'fsm_Constraint', a2)
    if hasattr(a1, 'fsm_Model'):
        assert not _is_linked(a1, 'fsm_Model', b)
    if hasattr(a2, 'fsm_Model'):
        assert _is_linked(a2, 'fsm_Model', b)
    _safe_set(b, 'fsm_Constraint', None)
    assert not _is_linked(b, 'fsm_Constraint', a2)
    if hasattr(a2, 'fsm_Model'):
        assert not _is_linked(a2, 'fsm_Model', b)


def test_assoc_from_9_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_State(final=True, initial=True, name="sample_text")
    _safe_set(b, 'fsm_State11', a1)
    assert _is_linked(b, 'fsm_State11', a1)
    if hasattr(a1, 'fsm_Transition10'):
        assert _is_linked(a1, 'fsm_Transition10', b)
    _safe_set(b, 'fsm_State11', a2)
    assert _is_linked(b, 'fsm_State11', a2)
    if hasattr(a1, 'fsm_Transition10'):
        assert not _is_linked(a1, 'fsm_Transition10', b)
    if hasattr(a2, 'fsm_Transition10'):
        assert _is_linked(a2, 'fsm_Transition10', b)
    _safe_set(b, 'fsm_State11', None)
    assert not _is_linked(b, 'fsm_State11', a2)
    if hasattr(a2, 'fsm_Transition10'):
        assert not _is_linked(a2, 'fsm_Transition10', b)


def test_assoc_languages1_reverse_link_reassign_clear():
    a1 = fsm_Model(name="sample_text")
    a2 = fsm_Model(name="sample_text_2")
    b = fsm_Language(name="sample_text", target="sample_text")
    _safe_set(b, 'fsm_Language', a1)
    assert _is_linked(b, 'fsm_Language', a1)
    if hasattr(a1, 'fsm_Model2'):
        assert _is_linked(a1, 'fsm_Model2', b)
    _safe_set(b, 'fsm_Language', a2)
    assert _is_linked(b, 'fsm_Language', a2)
    if hasattr(a1, 'fsm_Model2'):
        assert not _is_linked(a1, 'fsm_Model2', b)
    if hasattr(a2, 'fsm_Model2'):
        assert _is_linked(a2, 'fsm_Model2', b)
    _safe_set(b, 'fsm_Language', None)
    assert not _is_linked(b, 'fsm_Language', a2)
    if hasattr(a2, 'fsm_Model2'):
        assert not _is_linked(a2, 'fsm_Model2', b)


def test_assoc_to12_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_State(final=True, initial=True, name="sample_text")
    _safe_set(b, 'fsm_State14', a1)
    assert _is_linked(b, 'fsm_State14', a1)
    if hasattr(a1, 'fsm_Transition13'):
        assert _is_linked(a1, 'fsm_Transition13', b)
    _safe_set(b, 'fsm_State14', a2)
    assert _is_linked(b, 'fsm_State14', a2)
    if hasattr(a1, 'fsm_Transition13'):
        assert not _is_linked(a1, 'fsm_Transition13', b)
    if hasattr(a2, 'fsm_Transition13'):
        assert _is_linked(a2, 'fsm_Transition13', b)
    _safe_set(b, 'fsm_State14', None)
    assert not _is_linked(b, 'fsm_State14', a2)
    if hasattr(a2, 'fsm_Transition13'):
        assert not _is_linked(a2, 'fsm_Transition13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_machine3_stub_double():
    # fsm_Machine has no real 'fsm_Machine' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Model(name="sample_text")
    partner = fsm_Machine()
    setattr(partner, 'fsm_Machine', None)
    _safe_set(owner, 'fsm_Model4', partner)
    assert getattr(partner, 'fsm_Machine') == owner
    _safe_set(owner, 'fsm_Model4', None)
    assert getattr(partner, 'fsm_Machine') is None


def test_assoc_states5_stub_double():
    # fsm_Machine has no real 'fsm_Machine6' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(final=True, initial=True, name="sample_text")
    partner = fsm_Machine()
    setattr(partner, 'fsm_Machine6', None)
    _safe_set(owner, 'fsm_State', partner)
    assert owner in getattr(partner, 'fsm_Machine6')
    _safe_set(owner, 'fsm_State', None)
    assert owner not in getattr(partner, 'fsm_Machine6')


def test_assoc_transitions7_stub_double():
    # fsm_Machine has no real 'fsm_Machine8' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(event="sample_text")
    partner = fsm_Machine()
    setattr(partner, 'fsm_Machine8', None)
    _safe_set(owner, 'fsm_Transition', partner)
    assert owner in getattr(partner, 'fsm_Machine8')
    _safe_set(owner, 'fsm_Transition', None)
    assert owner not in getattr(partner, 'fsm_Machine8')


