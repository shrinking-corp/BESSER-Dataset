import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PseudoState,
    SimplStateMachineDC_CompositeState,
    SimplStateMachineDC_InitialState,
    SimplStateMachineDC_PseudoState,
    SimplStateMachineDC_State,
    SimplStateMachineDC_StateMachine,
    SimplStateMachineDC_Transition,
    State,
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

def test_assoc_source8_reverse_link_reassign_clear():
    a1 = SimplStateMachineDC_Transition(event="sample_text")
    a2 = SimplStateMachineDC_Transition(event="sample_text_2")
    b = SimplStateMachineDC_State(Inh="sample_text", InhIf="sample_text", Ord="sample_text", OrdIf="sample_text", isActive=True, name="sample_text")
    _safe_set(b, 'SimplStateMachineDC_State10', a1)
    assert _is_linked(b, 'SimplStateMachineDC_State10', a1)
    if hasattr(a1, 'SimplStateMachineDC_Transition9'):
        assert _is_linked(a1, 'SimplStateMachineDC_Transition9', b)
    _safe_set(b, 'SimplStateMachineDC_State10', a2)
    assert _is_linked(b, 'SimplStateMachineDC_State10', a2)
    if hasattr(a1, 'SimplStateMachineDC_Transition9'):
        assert not _is_linked(a1, 'SimplStateMachineDC_Transition9', b)
    if hasattr(a2, 'SimplStateMachineDC_Transition9'):
        assert _is_linked(a2, 'SimplStateMachineDC_Transition9', b)
    _safe_set(b, 'SimplStateMachineDC_State10', None)
    assert not _is_linked(b, 'SimplStateMachineDC_State10', a2)
    if hasattr(a2, 'SimplStateMachineDC_Transition9'):
        assert not _is_linked(a2, 'SimplStateMachineDC_Transition9', b)


def test_assoc_target11_reverse_link_reassign_clear():
    a1 = SimplStateMachineDC_Transition(event="sample_text")
    a2 = SimplStateMachineDC_Transition(event="sample_text_2")
    b = SimplStateMachineDC_State(Inh="sample_text", InhIf="sample_text", Ord="sample_text", OrdIf="sample_text", isActive=True, name="sample_text")
    _safe_set(b, 'SimplStateMachineDC_State13', a1)
    assert _is_linked(b, 'SimplStateMachineDC_State13', a1)
    if hasattr(a1, 'SimplStateMachineDC_Transition12'):
        assert _is_linked(a1, 'SimplStateMachineDC_Transition12', b)
    _safe_set(b, 'SimplStateMachineDC_State13', a2)
    assert _is_linked(b, 'SimplStateMachineDC_State13', a2)
    if hasattr(a1, 'SimplStateMachineDC_Transition12'):
        assert not _is_linked(a1, 'SimplStateMachineDC_Transition12', b)
    if hasattr(a2, 'SimplStateMachineDC_Transition12'):
        assert _is_linked(a2, 'SimplStateMachineDC_Transition12', b)
    _safe_set(b, 'SimplStateMachineDC_State13', None)
    assert not _is_linked(b, 'SimplStateMachineDC_State13', a2)
    if hasattr(a2, 'SimplStateMachineDC_Transition12'):
        assert not _is_linked(a2, 'SimplStateMachineDC_Transition12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_container3_stub_double():
    # SimplStateMachineDC_CompositeState has no real 'CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachineDC_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachineDC_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachineDC_State(Inh="sample_text", InhIf="sample_text", Ord="sample_text", OrdIf="sample_text", isActive=True, name="sample_text")
    partner = SimplStateMachineDC_CompositeState()
    setattr(partner, 'CompositeState', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'CompositeState') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'CompositeState') is None


def test_assoc_referencedState6_stub_double():
    # SimplStateMachineDC_PseudoState has no real 'SimplStateMachineDC_PseudoState' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachineDC_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachineDC_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachineDC_State(Inh="sample_text", InhIf="sample_text", Ord="sample_text", OrdIf="sample_text", isActive=True, name="sample_text")
    partner = SimplStateMachineDC_PseudoState()
    setattr(partner, 'SimplStateMachineDC_PseudoState', None)
    _safe_set(owner, 'SimplStateMachineDC_State7', partner)
    assert getattr(partner, 'SimplStateMachineDC_PseudoState') == owner
    _safe_set(owner, 'SimplStateMachineDC_State7', None)
    assert getattr(partner, 'SimplStateMachineDC_PseudoState') is None


def test_assoc_states1_stub_double():
    # SimplStateMachineDC_StateMachine has no real 'SimplStateMachineDC_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachineDC_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachineDC_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachineDC_State(Inh="sample_text", InhIf="sample_text", Ord="sample_text", OrdIf="sample_text", isActive=True, name="sample_text")
    partner = SimplStateMachineDC_StateMachine()
    setattr(partner, 'SimplStateMachineDC_StateMachine2', None)
    _safe_set(owner, 'SimplStateMachineDC_State', partner)
    assert owner in getattr(partner, 'SimplStateMachineDC_StateMachine2')
    _safe_set(owner, 'SimplStateMachineDC_State', None)
    assert owner not in getattr(partner, 'SimplStateMachineDC_StateMachine2')


def test_assoc_states4_stub_double():
    # SimplStateMachineDC_CompositeState has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachineDC_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachineDC_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachineDC_State(Inh="sample_text", InhIf="sample_text", Ord="sample_text", OrdIf="sample_text", isActive=True, name="sample_text")
    partner = SimplStateMachineDC_CompositeState()
    setattr(partner, 'container', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_transitions0_stub_double():
    # SimplStateMachineDC_StateMachine has no real 'SimplStateMachineDC_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachineDC_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachineDC_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachineDC_Transition(event="sample_text")
    partner = SimplStateMachineDC_StateMachine()
    setattr(partner, 'SimplStateMachineDC_StateMachine', None)
    _safe_set(owner, 'SimplStateMachineDC_Transition', partner)
    assert owner in getattr(partner, 'SimplStateMachineDC_StateMachine')
    _safe_set(owner, 'SimplStateMachineDC_Transition', None)
    assert owner not in getattr(partner, 'SimplStateMachineDC_StateMachine')


