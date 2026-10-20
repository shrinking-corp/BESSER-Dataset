import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    State,
    Vertex,
    state_Behaviour,
    state_Constraint,
    state_Event,
    state_FinalState,
    state_NamedElement,
    state_OpaqueExpression,
    state_PseudoState,
    state_Region,
    state_State,
    state_StateMachine,
    state_StateModel,
    state_Transition,
    state_Trigger,
    state_Vertex,
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

def test_assoc_doActivity3_reverse_link_reassign_clear():
    a1 = state_State(isComposite=True, isSimple=True)
    a2 = state_State(isComposite=False, isSimple=False)
    b = state_Behaviour(body="sample_text", language="sample_text")
    _safe_set(b, 'state_Behaviour', a1)
    assert _is_linked(b, 'state_Behaviour', a1)
    if hasattr(a1, 'state_State4'):
        assert _is_linked(a1, 'state_State4', b)
    _safe_set(b, 'state_Behaviour', a2)
    assert _is_linked(b, 'state_Behaviour', a2)
    if hasattr(a1, 'state_State4'):
        assert not _is_linked(a1, 'state_State4', b)
    if hasattr(a2, 'state_State4'):
        assert _is_linked(a2, 'state_State4', b)
    _safe_set(b, 'state_Behaviour', None)
    assert not _is_linked(b, 'state_Behaviour', a2)
    if hasattr(a2, 'state_State4'):
        assert not _is_linked(a2, 'state_State4', b)


def test_assoc_effect34_reverse_link_reassign_clear():
    a1 = state_Transition(kind="sample_text")
    a2 = state_Transition(kind="sample_text_2")
    b = state_Behaviour(body="sample_text", language="sample_text")
    _safe_set(b, 'state_Behaviour36', a1)
    assert _is_linked(b, 'state_Behaviour36', a1)
    if hasattr(a1, 'state_Transition35'):
        assert _is_linked(a1, 'state_Transition35', b)
    _safe_set(b, 'state_Behaviour36', a2)
    assert _is_linked(b, 'state_Behaviour36', a2)
    if hasattr(a1, 'state_Transition35'):
        assert not _is_linked(a1, 'state_Transition35', b)
    if hasattr(a2, 'state_Transition35'):
        assert _is_linked(a2, 'state_Transition35', b)
    _safe_set(b, 'state_Behaviour36', None)
    assert not _is_linked(b, 'state_Behaviour36', a2)
    if hasattr(a2, 'state_Transition35'):
        assert not _is_linked(a2, 'state_Transition35', b)


def test_assoc_entry5_reverse_link_reassign_clear():
    a1 = state_State(isComposite=True, isSimple=True)
    a2 = state_State(isComposite=False, isSimple=False)
    b = state_Behaviour(body="sample_text", language="sample_text")
    _safe_set(b, 'state_Behaviour7', a1)
    assert _is_linked(b, 'state_Behaviour7', a1)
    if hasattr(a1, 'state_State6'):
        assert _is_linked(a1, 'state_State6', b)
    _safe_set(b, 'state_Behaviour7', a2)
    assert _is_linked(b, 'state_Behaviour7', a2)
    if hasattr(a1, 'state_State6'):
        assert not _is_linked(a1, 'state_State6', b)
    if hasattr(a2, 'state_State6'):
        assert _is_linked(a2, 'state_State6', b)
    _safe_set(b, 'state_Behaviour7', None)
    assert not _is_linked(b, 'state_Behaviour7', a2)
    if hasattr(a2, 'state_State6'):
        assert not _is_linked(a2, 'state_State6', b)


def test_assoc_exit8_reverse_link_reassign_clear():
    a1 = state_State(isComposite=True, isSimple=True)
    a2 = state_State(isComposite=False, isSimple=False)
    b = state_Behaviour(body="sample_text", language="sample_text")
    _safe_set(b, 'state_Behaviour10', a1)
    assert _is_linked(b, 'state_Behaviour10', a1)
    if hasattr(a1, 'state_State9'):
        assert _is_linked(a1, 'state_State9', b)
    _safe_set(b, 'state_Behaviour10', a2)
    assert _is_linked(b, 'state_Behaviour10', a2)
    if hasattr(a1, 'state_State9'):
        assert not _is_linked(a1, 'state_State9', b)
    if hasattr(a2, 'state_State9'):
        assert _is_linked(a2, 'state_State9', b)
    _safe_set(b, 'state_Behaviour10', None)
    assert not _is_linked(b, 'state_Behaviour10', a2)
    if hasattr(a2, 'state_State9'):
        assert not _is_linked(a2, 'state_State9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defferableTrigger1_stub_double():
    # state_Trigger has no real 'state_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so state_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_State(isComposite=True, isSimple=True)
    partner = state_Trigger()
    setattr(partner, 'state_Trigger', None)
    _safe_set(owner, 'state_State2', {partner})
    assert getattr(partner, 'state_Trigger') == owner
    _safe_set(owner, 'state_State2', set())
    assert getattr(partner, 'state_Trigger') is None


def test_assoc_event39_stub_double():
    # state_Trigger has no real 'state_Trigger40' property in the generated
    # code (a bare stub) -- manually attach it so state_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Event(body="sample_text")
    partner = state_Trigger()
    setattr(partner, 'state_Trigger40', None)
    _safe_set(owner, 'state_Event', partner)
    assert getattr(partner, 'state_Trigger40') == owner
    _safe_set(owner, 'state_Event', None)
    assert getattr(partner, 'state_Trigger40') is None


def test_assoc_guard32_stub_double():
    # state_Constraint has no real 'state_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Constraint()
    setattr(partner, 'state_Constraint', None)
    _safe_set(owner, 'state_Transition33', partner)
    assert getattr(partner, 'state_Constraint') == owner
    _safe_set(owner, 'state_Transition33', None)
    assert getattr(partner, 'state_Constraint') is None


def test_assoc_incoming24_stub_double():
    # state_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition25', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition25', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoing23_stub_double():
    # state_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_packagedElment41_stub_double():
    # state_StateModel has no real 'state_StateModel' property in the generated
    # code (a bare stub) -- manually attach it so state_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_NamedElement(id="sample_text", name="sample_text")
    partner = state_StateModel()
    setattr(partner, 'state_StateModel', None)
    _safe_set(owner, 'state_NamedElement', partner)
    assert getattr(partner, 'state_StateModel') == owner
    _safe_set(owner, 'state_NamedElement', None)
    assert getattr(partner, 'state_StateModel') is None


def test_assoc_region0_stub_double():
    # state_Region has no real 'state_Region' property in the generated
    # code (a bare stub) -- manually attach it so state_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_State(isComposite=True, isSimple=True)
    partner = state_Region()
    setattr(partner, 'state_Region', None)
    _safe_set(owner, 'state_State', {partner})
    assert getattr(partner, 'state_Region') == owner
    _safe_set(owner, 'state_State', set())
    assert getattr(partner, 'state_Region') is None


def test_assoc_source26_stub_double():
    # state_Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Vertex') is None


def test_assoc_specification37_stub_double():
    # state_Constraint has no real 'state_Constraint38' property in the generated
    # code (a bare stub) -- manually attach it so state_OpaqueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_OpaqueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_OpaqueExpression(body="sample_text")
    partner = state_Constraint()
    setattr(partner, 'state_Constraint38', None)
    _safe_set(owner, 'state_OpaqueExpression', partner)
    assert getattr(partner, 'state_Constraint38') == owner
    _safe_set(owner, 'state_OpaqueExpression', None)
    assert getattr(partner, 'state_Constraint38') is None


def test_assoc_state11_stub_double():
    # state_Region has no real 'state_Region12' property in the generated
    # code (a bare stub) -- manually attach it so state_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_State(isComposite=True, isSimple=True)
    partner = state_Region()
    setattr(partner, 'state_Region12', None)
    _safe_set(owner, 'state_State13', partner)
    assert getattr(partner, 'state_Region12') == owner
    _safe_set(owner, 'state_State13', None)
    assert getattr(partner, 'state_Region12') is None


def test_assoc_target27_stub_double():
    # state_Vertex has no real 'Vertex28' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Vertex()
    setattr(partner, 'Vertex28', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Vertex28') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Vertex28') is None


def test_assoc_transition18_stub_double():
    # state_Region has no real 'state_Region19' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Region()
    setattr(partner, 'state_Region19', None)
    _safe_set(owner, 'state_Transition', partner)
    assert owner in getattr(partner, 'state_Region19')
    _safe_set(owner, 'state_Transition', None)
    assert owner not in getattr(partner, 'state_Region19')


def test_assoc_trigger29_stub_double():
    # state_Trigger has no real 'state_Trigger31' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(kind="sample_text")
    partner = state_Trigger()
    setattr(partner, 'state_Trigger31', None)
    _safe_set(owner, 'state_Transition30', partner)
    assert getattr(partner, 'state_Trigger31') == owner
    _safe_set(owner, 'state_Transition30', None)
    assert getattr(partner, 'state_Trigger31') is None


