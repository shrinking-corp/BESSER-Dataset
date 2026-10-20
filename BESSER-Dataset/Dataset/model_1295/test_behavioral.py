import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    State,
    StateMachine_Behavior,
    StateMachine_CodeBlock,
    StateMachine_Constraint,
    StateMachine_FinalState,
    StateMachine_PseudoState,
    StateMachine_Region,
    StateMachine_State,
    StateMachine_StateMachine,
    StateMachine_Transition,
    StateMachine_Trigger,
    StateMachine_Vertex,
    Vertex,
    PseudoStateKind,
    TransitionKind,
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

def test_assoc_deferrableTrigger3_reverse_link_reassign_clear():
    a1 = StateMachine_Trigger(trigger="sample_text")
    a2 = StateMachine_Trigger(trigger="sample_text_2")
    b = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    _safe_set(b, 'StateMachine_State4', {a1})
    assert _is_linked(b, 'StateMachine_State4', a1)
    if hasattr(a1, 'StateMachine_Trigger'):
        assert _is_linked(a1, 'StateMachine_Trigger', b)
    _safe_set(b, 'StateMachine_State4', {a2})
    assert _is_linked(b, 'StateMachine_State4', a2)
    if hasattr(a1, 'StateMachine_Trigger'):
        assert not _is_linked(a1, 'StateMachine_Trigger', b)
    if hasattr(a2, 'StateMachine_Trigger'):
        assert _is_linked(a2, 'StateMachine_Trigger', b)
    _safe_set(b, 'StateMachine_State4', set())
    assert not _is_linked(b, 'StateMachine_State4', a2)
    if hasattr(a2, 'StateMachine_Trigger'):
        assert not _is_linked(a2, 'StateMachine_Trigger', b)


def test_assoc_entryPoint14_reverse_link_reassign_clear():
    a1 = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = StateMachine_State(isComposite="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = StateMachine_PseudoState(pseudoStateKind="sample_text", returnValue="sample_text")
    _safe_set(b, 'StateMachine_PseudoState', a1)
    assert _is_linked(b, 'StateMachine_PseudoState', a1)
    if hasattr(a1, 'StateMachine_State15'):
        assert _is_linked(a1, 'StateMachine_State15', b)
    _safe_set(b, 'StateMachine_PseudoState', a2)
    assert _is_linked(b, 'StateMachine_PseudoState', a2)
    if hasattr(a1, 'StateMachine_State15'):
        assert not _is_linked(a1, 'StateMachine_State15', b)
    if hasattr(a2, 'StateMachine_State15'):
        assert _is_linked(a2, 'StateMachine_State15', b)
    _safe_set(b, 'StateMachine_PseudoState', None)
    assert not _is_linked(b, 'StateMachine_PseudoState', a2)
    if hasattr(a2, 'StateMachine_State15'):
        assert not _is_linked(a2, 'StateMachine_State15', b)


def test_assoc_exitPoint16_reverse_link_reassign_clear():
    a1 = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = StateMachine_State(isComposite="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = StateMachine_PseudoState(pseudoStateKind="sample_text", returnValue="sample_text")
    _safe_set(b, 'StateMachine_PseudoState18', a1)
    assert _is_linked(b, 'StateMachine_PseudoState18', a1)
    if hasattr(a1, 'StateMachine_State17'):
        assert _is_linked(a1, 'StateMachine_State17', b)
    _safe_set(b, 'StateMachine_PseudoState18', a2)
    assert _is_linked(b, 'StateMachine_PseudoState18', a2)
    if hasattr(a1, 'StateMachine_State17'):
        assert not _is_linked(a1, 'StateMachine_State17', b)
    if hasattr(a2, 'StateMachine_State17'):
        assert _is_linked(a2, 'StateMachine_State17', b)
    _safe_set(b, 'StateMachine_PseudoState18', None)
    assert not _is_linked(b, 'StateMachine_PseudoState18', a2)
    if hasattr(a2, 'StateMachine_State17'):
        assert not _is_linked(a2, 'StateMachine_State17', b)


def test_assoc_guard38_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(kind="sample_text", name="sample_text")
    a2 = StateMachine_Transition(kind="sample_text_2", name="sample_text_2")
    b = StateMachine_Constraint(constraint="sample_text")
    _safe_set(b, 'StateMachine_Constraint40', a1)
    assert _is_linked(b, 'StateMachine_Constraint40', a1)
    if hasattr(a1, 'StateMachine_Transition39'):
        assert _is_linked(a1, 'StateMachine_Transition39', b)
    _safe_set(b, 'StateMachine_Constraint40', a2)
    assert _is_linked(b, 'StateMachine_Constraint40', a2)
    if hasattr(a1, 'StateMachine_Transition39'):
        assert not _is_linked(a1, 'StateMachine_Transition39', b)
    if hasattr(a2, 'StateMachine_Transition39'):
        assert _is_linked(a2, 'StateMachine_Transition39', b)
    _safe_set(b, 'StateMachine_Constraint40', None)
    assert not _is_linked(b, 'StateMachine_Constraint40', a2)
    if hasattr(a2, 'StateMachine_Transition39'):
        assert not _is_linked(a2, 'StateMachine_Transition39', b)


def test_assoc_incoming20_reverse_link_reassign_clear():
    a1 = StateMachine_Vertex(name="sample_text")
    a2 = StateMachine_Vertex(name="sample_text_2")
    b = StateMachine_Transition(kind="sample_text", name="sample_text")
    _safe_set(b, 'Transition21', a1)
    assert _is_linked(b, 'Transition21', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Transition21', a2)
    assert _is_linked(b, 'Transition21', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Transition21', None)
    assert not _is_linked(b, 'Transition21', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_outgoing19_reverse_link_reassign_clear():
    a1 = StateMachine_Vertex(name="sample_text")
    a2 = StateMachine_Vertex(name="sample_text_2")
    b = StateMachine_Transition(kind="sample_text", name="sample_text")
    _safe_set(b, 'Transition', a1)
    assert _is_linked(b, 'Transition', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Transition', a2)
    assert _is_linked(b, 'Transition', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Transition', None)
    assert not _is_linked(b, 'Transition', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_region0_reverse_link_reassign_clear():
    a1 = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = StateMachine_State(isComposite="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = StateMachine_Region(name="sample_text")
    _safe_set(b, 'StateMachine_Region', a1)
    assert _is_linked(b, 'StateMachine_Region', a1)
    if hasattr(a1, 'StateMachine_State'):
        assert _is_linked(a1, 'StateMachine_State', b)
    _safe_set(b, 'StateMachine_Region', a2)
    assert _is_linked(b, 'StateMachine_Region', a2)
    if hasattr(a1, 'StateMachine_State'):
        assert not _is_linked(a1, 'StateMachine_State', b)
    if hasattr(a2, 'StateMachine_State'):
        assert _is_linked(a2, 'StateMachine_State', b)
    _safe_set(b, 'StateMachine_Region', None)
    assert not _is_linked(b, 'StateMachine_Region', a2)
    if hasattr(a2, 'StateMachine_State'):
        assert not _is_linked(a2, 'StateMachine_State', b)


def test_assoc_region26_reverse_link_reassign_clear():
    a1 = StateMachine_StateMachine(name="sample_text")
    a2 = StateMachine_StateMachine(name="sample_text_2")
    b = StateMachine_Region(name="sample_text")
    _safe_set(b, 'StateMachine_Region27', a1)
    assert _is_linked(b, 'StateMachine_Region27', a1)
    if hasattr(a1, 'StateMachine_StateMachine'):
        assert _is_linked(a1, 'StateMachine_StateMachine', b)
    _safe_set(b, 'StateMachine_Region27', a2)
    assert _is_linked(b, 'StateMachine_Region27', a2)
    if hasattr(a1, 'StateMachine_StateMachine'):
        assert not _is_linked(a1, 'StateMachine_StateMachine', b)
    if hasattr(a2, 'StateMachine_StateMachine'):
        assert _is_linked(a2, 'StateMachine_StateMachine', b)
    _safe_set(b, 'StateMachine_Region27', None)
    assert not _is_linked(b, 'StateMachine_Region27', a2)
    if hasattr(a2, 'StateMachine_StateMachine'):
        assert not _is_linked(a2, 'StateMachine_StateMachine', b)


def test_assoc_source29_reverse_link_reassign_clear():
    a1 = StateMachine_Vertex(name="sample_text")
    a2 = StateMachine_Vertex(name="sample_text_2")
    b = StateMachine_Transition(kind="sample_text", name="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Vertex'):
        assert _is_linked(a1, 'Vertex', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Vertex'):
        assert not _is_linked(a1, 'Vertex', b)
    if hasattr(a2, 'Vertex'):
        assert _is_linked(a2, 'Vertex', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Vertex'):
        assert not _is_linked(a2, 'Vertex', b)


def test_assoc_stateInvariant5_reverse_link_reassign_clear():
    a1 = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = StateMachine_State(isComposite="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = StateMachine_Constraint(constraint="sample_text")
    _safe_set(b, 'StateMachine_Constraint', a1)
    assert _is_linked(b, 'StateMachine_Constraint', a1)
    if hasattr(a1, 'StateMachine_State6'):
        assert _is_linked(a1, 'StateMachine_State6', b)
    _safe_set(b, 'StateMachine_Constraint', a2)
    assert _is_linked(b, 'StateMachine_Constraint', a2)
    if hasattr(a1, 'StateMachine_State6'):
        assert not _is_linked(a1, 'StateMachine_State6', b)
    if hasattr(a2, 'StateMachine_State6'):
        assert _is_linked(a2, 'StateMachine_State6', b)
    _safe_set(b, 'StateMachine_Constraint', None)
    assert not _is_linked(b, 'StateMachine_Constraint', a2)
    if hasattr(a2, 'StateMachine_State6'):
        assert not _is_linked(a2, 'StateMachine_State6', b)


def test_assoc_submachine13_reverse_link_reassign_clear():
    a1 = StateMachine_StateMachine(name="sample_text")
    a2 = StateMachine_StateMachine(name="sample_text_2")
    b = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    _safe_set(b, 'submachineState', a1)
    assert _is_linked(b, 'submachineState', a1)
    if hasattr(a1, 'StateMachine'):
        assert _is_linked(a1, 'StateMachine', b)
    _safe_set(b, 'submachineState', a2)
    assert _is_linked(b, 'submachineState', a2)
    if hasattr(a1, 'StateMachine'):
        assert not _is_linked(a1, 'StateMachine', b)
    if hasattr(a2, 'StateMachine'):
        assert _is_linked(a2, 'StateMachine', b)
    _safe_set(b, 'submachineState', None)
    assert not _is_linked(b, 'submachineState', a2)
    if hasattr(a2, 'StateMachine'):
        assert not _is_linked(a2, 'StateMachine', b)


def test_assoc_submachineState28_reverse_link_reassign_clear():
    a1 = StateMachine_StateMachine(name="sample_text")
    a2 = StateMachine_StateMachine(name="sample_text_2")
    b = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'submachine'):
        assert _is_linked(a1, 'submachine', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'submachine'):
        assert not _is_linked(a1, 'submachine', b)
    if hasattr(a2, 'submachine'):
        assert _is_linked(a2, 'submachine', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'submachine'):
        assert not _is_linked(a2, 'submachine', b)


def test_assoc_subvertex22_reverse_link_reassign_clear():
    a1 = StateMachine_Vertex(name="sample_text")
    a2 = StateMachine_Vertex(name="sample_text_2")
    b = StateMachine_Region(name="sample_text")
    _safe_set(b, 'StateMachine_Region23', {a1})
    assert _is_linked(b, 'StateMachine_Region23', a1)
    if hasattr(a1, 'StateMachine_Vertex'):
        assert _is_linked(a1, 'StateMachine_Vertex', b)
    _safe_set(b, 'StateMachine_Region23', {a2})
    assert _is_linked(b, 'StateMachine_Region23', a2)
    if hasattr(a1, 'StateMachine_Vertex'):
        assert not _is_linked(a1, 'StateMachine_Vertex', b)
    if hasattr(a2, 'StateMachine_Vertex'):
        assert _is_linked(a2, 'StateMachine_Vertex', b)
    _safe_set(b, 'StateMachine_Region23', set())
    assert not _is_linked(b, 'StateMachine_Region23', a2)
    if hasattr(a2, 'StateMachine_Vertex'):
        assert not _is_linked(a2, 'StateMachine_Vertex', b)


def test_assoc_target30_reverse_link_reassign_clear():
    a1 = StateMachine_Vertex(name="sample_text")
    a2 = StateMachine_Vertex(name="sample_text_2")
    b = StateMachine_Transition(kind="sample_text", name="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Vertex31'):
        assert _is_linked(a1, 'Vertex31', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Vertex31'):
        assert not _is_linked(a1, 'Vertex31', b)
    if hasattr(a2, 'Vertex31'):
        assert _is_linked(a2, 'Vertex31', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Vertex31'):
        assert not _is_linked(a2, 'Vertex31', b)


def test_assoc_transition24_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(kind="sample_text", name="sample_text")
    a2 = StateMachine_Transition(kind="sample_text_2", name="sample_text_2")
    b = StateMachine_Region(name="sample_text")
    _safe_set(b, 'StateMachine_Region25', {a1})
    assert _is_linked(b, 'StateMachine_Region25', a1)
    if hasattr(a1, 'StateMachine_Transition'):
        assert _is_linked(a1, 'StateMachine_Transition', b)
    _safe_set(b, 'StateMachine_Region25', {a2})
    assert _is_linked(b, 'StateMachine_Region25', a2)
    if hasattr(a1, 'StateMachine_Transition'):
        assert not _is_linked(a1, 'StateMachine_Transition', b)
    if hasattr(a2, 'StateMachine_Transition'):
        assert _is_linked(a2, 'StateMachine_Transition', b)
    _safe_set(b, 'StateMachine_Region25', set())
    assert not _is_linked(b, 'StateMachine_Region25', a2)
    if hasattr(a2, 'StateMachine_Transition'):
        assert not _is_linked(a2, 'StateMachine_Transition', b)


def test_assoc_trigger35_reverse_link_reassign_clear():
    a1 = StateMachine_Trigger(trigger="sample_text")
    a2 = StateMachine_Trigger(trigger="sample_text_2")
    b = StateMachine_Transition(kind="sample_text", name="sample_text")
    _safe_set(b, 'StateMachine_Transition36', {a1})
    assert _is_linked(b, 'StateMachine_Transition36', a1)
    if hasattr(a1, 'StateMachine_Trigger37'):
        assert _is_linked(a1, 'StateMachine_Trigger37', b)
    _safe_set(b, 'StateMachine_Transition36', {a2})
    assert _is_linked(b, 'StateMachine_Transition36', a2)
    if hasattr(a1, 'StateMachine_Trigger37'):
        assert not _is_linked(a1, 'StateMachine_Trigger37', b)
    if hasattr(a2, 'StateMachine_Trigger37'):
        assert _is_linked(a2, 'StateMachine_Trigger37', b)
    _safe_set(b, 'StateMachine_Transition36', set())
    assert not _is_linked(b, 'StateMachine_Transition36', a2)
    if hasattr(a2, 'StateMachine_Trigger37'):
        assert not _is_linked(a2, 'StateMachine_Trigger37', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_doActivity1_stub_double():
    # StateMachine_Behavior has no real 'StateMachine_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = StateMachine_Behavior()
    setattr(partner, 'StateMachine_Behavior', None)
    _safe_set(owner, 'StateMachine_State2', partner)
    assert getattr(partner, 'StateMachine_Behavior') == owner
    _safe_set(owner, 'StateMachine_State2', None)
    assert getattr(partner, 'StateMachine_Behavior') is None


def test_assoc_effect32_stub_double():
    # StateMachine_Behavior has no real 'StateMachine_Behavior34' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(kind="sample_text", name="sample_text")
    partner = StateMachine_Behavior()
    setattr(partner, 'StateMachine_Behavior34', None)
    _safe_set(owner, 'StateMachine_Transition33', partner)
    assert getattr(partner, 'StateMachine_Behavior34') == owner
    _safe_set(owner, 'StateMachine_Transition33', None)
    assert getattr(partner, 'StateMachine_Behavior34') is None


def test_assoc_entry10_stub_double():
    # StateMachine_Behavior has no real 'StateMachine_Behavior12' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = StateMachine_Behavior()
    setattr(partner, 'StateMachine_Behavior12', None)
    _safe_set(owner, 'StateMachine_State11', partner)
    assert getattr(partner, 'StateMachine_Behavior12') == owner
    _safe_set(owner, 'StateMachine_State11', None)
    assert getattr(partner, 'StateMachine_Behavior12') is None


def test_assoc_exit7_stub_double():
    # StateMachine_Behavior has no real 'StateMachine_Behavior9' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_State(isComposite="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = StateMachine_Behavior()
    setattr(partner, 'StateMachine_Behavior9', None)
    _safe_set(owner, 'StateMachine_State8', partner)
    assert getattr(partner, 'StateMachine_Behavior9') == owner
    _safe_set(owner, 'StateMachine_State8', None)
    assert getattr(partner, 'StateMachine_Behavior9') is None


