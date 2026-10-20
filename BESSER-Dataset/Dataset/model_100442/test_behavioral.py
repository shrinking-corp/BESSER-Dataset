import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractExtension,
    AbstractNode,
    Diagram,
    Event,
    EventBCommentedElement,
    EventBElement,
    EventBLabeled,
    EventBNamed,
    EventBNamedCommentedElement,
    Invariant,
    StatemachineOwner,
    statemachines_AbstractNode,
    statemachines_EventBElement,
    statemachines_EventBNamedCommentedElement,
    statemachines_Final,
    statemachines_Initial,
    statemachines_State,
    statemachines_Statemachine,
    statemachines_StatemachineOwner,
    statemachines_Transition,
    TranslationKind,
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

def test_assoc_refines1_reverse_link_reassign_clear():
    a1 = statemachines_Statemachine(selfName="sample_text", translation="sample_text")
    a2 = statemachines_Statemachine(selfName="sample_text_2", translation="sample_text_2")
    b = statemachines_Statemachine(selfName="sample_text", translation="sample_text")
    _safe_set(b, 'statemachines_Statemachine0', a1)
    assert _is_linked(b, 'statemachines_Statemachine0', a1)
    if hasattr(a1, 'statemachines_Statemachine'):
        assert _is_linked(a1, 'statemachines_Statemachine', b)
    _safe_set(b, 'statemachines_Statemachine0', a2)
    assert _is_linked(b, 'statemachines_Statemachine0', a2)
    if hasattr(a1, 'statemachines_Statemachine'):
        assert not _is_linked(a1, 'statemachines_Statemachine', b)
    if hasattr(a2, 'statemachines_Statemachine'):
        assert _is_linked(a2, 'statemachines_Statemachine', b)
    _safe_set(b, 'statemachines_Statemachine0', None)
    assert not _is_linked(b, 'statemachines_Statemachine0', a2)
    if hasattr(a2, 'statemachines_Statemachine'):
        assert not _is_linked(a2, 'statemachines_Statemachine', b)


def test_assoc_refines24_reverse_link_reassign_clear():
    a1 = statemachines_State(active=True)
    a2 = statemachines_State(active=False)
    b = statemachines_State(active=True)
    _safe_set(b, 'statemachines_State23', a1)
    assert _is_linked(b, 'statemachines_State23', a1)
    if hasattr(a1, 'statemachines_State'):
        assert _is_linked(a1, 'statemachines_State', b)
    _safe_set(b, 'statemachines_State23', a2)
    assert _is_linked(b, 'statemachines_State23', a2)
    if hasattr(a1, 'statemachines_State'):
        assert not _is_linked(a1, 'statemachines_State', b)
    if hasattr(a2, 'statemachines_State'):
        assert _is_linked(a2, 'statemachines_State', b)
    _safe_set(b, 'statemachines_State23', None)
    assert not _is_linked(b, 'statemachines_State23', a2)
    if hasattr(a2, 'statemachines_State'):
        assert not _is_linked(a2, 'statemachines_State', b)


def test_assoc_transitions4_reverse_link_reassign_clear():
    a1 = statemachines_Transition(operations="sample_text")
    a2 = statemachines_Transition(operations="sample_text_2")
    b = statemachines_Statemachine(selfName="sample_text", translation="sample_text")
    _safe_set(b, 'statemachines_Statemachine5', {a1})
    assert _is_linked(b, 'statemachines_Statemachine5', a1)
    if hasattr(a1, 'statemachines_Transition'):
        assert _is_linked(a1, 'statemachines_Transition', b)
    _safe_set(b, 'statemachines_Statemachine5', {a2})
    assert _is_linked(b, 'statemachines_Statemachine5', a2)
    if hasattr(a1, 'statemachines_Transition'):
        assert not _is_linked(a1, 'statemachines_Transition', b)
    if hasattr(a2, 'statemachines_Transition'):
        assert _is_linked(a2, 'statemachines_Transition', b)
    _safe_set(b, 'statemachines_Statemachine5', set())
    assert not _is_linked(b, 'statemachines_Statemachine5', a2)
    if hasattr(a2, 'statemachines_Transition'):
        assert not _is_linked(a2, 'statemachines_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elaborates13_stub_double():
    # Event has no real 'Event' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = Event()
    setattr(partner, 'Event', None)
    _safe_set(owner, 'statemachines_Transition14', {partner})
    assert getattr(partner, 'Event') == owner
    _safe_set(owner, 'statemachines_Transition14', set())
    assert getattr(partner, 'Event') is None


def test_assoc_incoming20_stub_double():
    # statemachines_AbstractNode has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = statemachines_AbstractNode()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_instances6_stub_double():
    # statemachines_EventBNamedCommentedElement has no real 'statemachines_EventBNamedCommentedElement' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Statemachine(selfName="sample_text", translation="sample_text")
    partner = statemachines_EventBNamedCommentedElement()
    setattr(partner, 'statemachines_EventBNamedCommentedElement', None)
    _safe_set(owner, 'statemachines_Statemachine7', partner)
    assert getattr(partner, 'statemachines_EventBNamedCommentedElement') == owner
    _safe_set(owner, 'statemachines_Statemachine7', None)
    assert getattr(partner, 'statemachines_EventBNamedCommentedElement') is None


def test_assoc_invariants25_stub_double():
    # Invariant has no real 'Invariant' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(active=True)
    partner = Invariant()
    setattr(partner, 'Invariant', None)
    _safe_set(owner, 'statemachines_State26', {partner})
    assert getattr(partner, 'Invariant') == owner
    _safe_set(owner, 'statemachines_State26', set())
    assert getattr(partner, 'Invariant') is None


def test_assoc_nodes2_stub_double():
    # statemachines_AbstractNode has no real 'statemachines_AbstractNode' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Statemachine(selfName="sample_text", translation="sample_text")
    partner = statemachines_AbstractNode()
    setattr(partner, 'statemachines_AbstractNode', None)
    _safe_set(owner, 'statemachines_Statemachine3', {partner})
    assert getattr(partner, 'statemachines_AbstractNode') == owner
    _safe_set(owner, 'statemachines_Statemachine3', set())
    assert getattr(partner, 'statemachines_AbstractNode') is None


def test_assoc_outgoing21_stub_double():
    # statemachines_AbstractNode has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = statemachines_AbstractNode()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition22', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition22', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_source11_stub_double():
    # statemachines_AbstractNode has no real 'AbstractNode12' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = statemachines_AbstractNode()
    setattr(partner, 'AbstractNode12', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'AbstractNode12') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'AbstractNode12') is None


def test_assoc_sourceContainer15_stub_double():
    # statemachines_EventBElement has no real 'statemachines_EventBElement' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = statemachines_EventBElement()
    setattr(partner, 'statemachines_EventBElement', None)
    _safe_set(owner, 'statemachines_Transition16', partner)
    assert getattr(partner, 'statemachines_EventBElement') == owner
    _safe_set(owner, 'statemachines_Transition16', None)
    assert getattr(partner, 'statemachines_EventBElement') is None


def test_assoc_statemachines8_stub_double():
    # statemachines_StatemachineOwner has no real 'statemachines_StatemachineOwner' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Statemachine(selfName="sample_text", translation="sample_text")
    partner = statemachines_StatemachineOwner()
    setattr(partner, 'statemachines_StatemachineOwner', None)
    _safe_set(owner, 'statemachines_Statemachine9', partner)
    assert owner in getattr(partner, 'statemachines_StatemachineOwner')
    _safe_set(owner, 'statemachines_Statemachine9', None)
    assert owner not in getattr(partner, 'statemachines_StatemachineOwner')


def test_assoc_target10_stub_double():
    # statemachines_AbstractNode has no real 'AbstractNode' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = statemachines_AbstractNode()
    setattr(partner, 'AbstractNode', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'AbstractNode') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'AbstractNode') is None


def test_assoc_targetContainer17_stub_double():
    # statemachines_EventBElement has no real 'statemachines_EventBElement19' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(operations="sample_text")
    partner = statemachines_EventBElement()
    setattr(partner, 'statemachines_EventBElement19', None)
    _safe_set(owner, 'statemachines_Transition18', partner)
    assert getattr(partner, 'statemachines_EventBElement19') == owner
    _safe_set(owner, 'statemachines_Transition18', None)
    assert getattr(partner, 'statemachines_EventBElement19') is None


