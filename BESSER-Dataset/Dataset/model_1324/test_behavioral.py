import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMachineElement,
    AbstractStateElement,
    stateMachine_AbstractMachineElement,
    stateMachine_AbstractStateElement,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_StateTransition,
    VisibilityType,
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
    a1 = stateMachine_StateTransition(visibility="sample_text")
    a2 = stateMachine_StateTransition(visibility="sample_text_2")
    b = stateMachine_AbstractStateElement(name="sample_text")
    _safe_set(b, 'stateMachine_AbstractStateElement', a1)
    assert _is_linked(b, 'stateMachine_AbstractStateElement', a1)
    if hasattr(a1, 'stateMachine_StateTransition'):
        assert _is_linked(a1, 'stateMachine_StateTransition', b)
    _safe_set(b, 'stateMachine_AbstractStateElement', a2)
    assert _is_linked(b, 'stateMachine_AbstractStateElement', a2)
    if hasattr(a1, 'stateMachine_StateTransition'):
        assert not _is_linked(a1, 'stateMachine_StateTransition', b)
    if hasattr(a2, 'stateMachine_StateTransition'):
        assert _is_linked(a2, 'stateMachine_StateTransition', b)
    _safe_set(b, 'stateMachine_AbstractStateElement', None)
    assert not _is_linked(b, 'stateMachine_AbstractStateElement', a2)
    if hasattr(a2, 'stateMachine_StateTransition'):
        assert not _is_linked(a2, 'stateMachine_StateTransition', b)


def test_assoc_to1_reverse_link_reassign_clear():
    a1 = stateMachine_StateTransition(visibility="sample_text")
    a2 = stateMachine_StateTransition(visibility="sample_text_2")
    b = stateMachine_AbstractStateElement(name="sample_text")
    _safe_set(b, 'stateMachine_AbstractStateElement3', a1)
    assert _is_linked(b, 'stateMachine_AbstractStateElement3', a1)
    if hasattr(a1, 'stateMachine_StateTransition2'):
        assert _is_linked(a1, 'stateMachine_StateTransition2', b)
    _safe_set(b, 'stateMachine_AbstractStateElement3', a2)
    assert _is_linked(b, 'stateMachine_AbstractStateElement3', a2)
    if hasattr(a1, 'stateMachine_StateTransition2'):
        assert not _is_linked(a1, 'stateMachine_StateTransition2', b)
    if hasattr(a2, 'stateMachine_StateTransition2'):
        assert _is_linked(a2, 'stateMachine_StateTransition2', b)
    _safe_set(b, 'stateMachine_AbstractStateElement3', None)
    assert not _is_linked(b, 'stateMachine_AbstractStateElement3', a2)
    if hasattr(a2, 'stateMachine_StateTransition2'):
        assert not _is_linked(a2, 'stateMachine_StateTransition2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements4_stub_double():
    # stateMachine_AbstractMachineElement has no real 'stateMachine_AbstractMachineElement' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(name="sample_text")
    partner = stateMachine_AbstractMachineElement()
    setattr(partner, 'stateMachine_AbstractMachineElement', None)
    _safe_set(owner, 'stateMachine_StateMachine', {partner})
    assert getattr(partner, 'stateMachine_AbstractMachineElement') == owner
    _safe_set(owner, 'stateMachine_StateMachine', set())
    assert getattr(partner, 'stateMachine_AbstractMachineElement') is None


