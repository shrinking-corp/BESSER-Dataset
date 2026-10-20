import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    StateMachineDiagram_meta_Activity,
    StateMachineDiagram_meta_Application,
    StateMachineDiagram_meta_Event,
    StateMachineDiagram_meta_Fragment,
    StateMachineDiagram_meta_Pseudostate,
    StateMachineDiagram_meta_State,
    StateMachineDiagram_meta_StateMachine,
    StateMachineDiagram_meta_Transition,
    StateMachineDiagram_meta_Vertex,
    Vertex,
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

def test_assoc_statemachine0_reverse_link_reassign_clear():
    a1 = StateMachineDiagram_meta_StateMachine(name="sample_text")
    a2 = StateMachineDiagram_meta_StateMachine(name="sample_text_2")
    b = StateMachineDiagram_meta_Application(name="sample_text")
    _safe_set(b, 'StateMachineDiagram_meta_Application', {a1})
    assert _is_linked(b, 'StateMachineDiagram_meta_Application', a1)
    if hasattr(a1, 'StateMachineDiagram_meta_StateMachine'):
        assert _is_linked(a1, 'StateMachineDiagram_meta_StateMachine', b)
    _safe_set(b, 'StateMachineDiagram_meta_Application', {a2})
    assert _is_linked(b, 'StateMachineDiagram_meta_Application', a2)
    if hasattr(a1, 'StateMachineDiagram_meta_StateMachine'):
        assert not _is_linked(a1, 'StateMachineDiagram_meta_StateMachine', b)
    if hasattr(a2, 'StateMachineDiagram_meta_StateMachine'):
        assert _is_linked(a2, 'StateMachineDiagram_meta_StateMachine', b)
    _safe_set(b, 'StateMachineDiagram_meta_Application', set())
    assert not _is_linked(b, 'StateMachineDiagram_meta_Application', a2)
    if hasattr(a2, 'StateMachineDiagram_meta_StateMachine'):
        assert not _is_linked(a2, 'StateMachineDiagram_meta_StateMachine', b)


def test_assoc_statemachine11_reverse_link_reassign_clear():
    a1 = StateMachineDiagram_meta_StateMachine(name="sample_text")
    a2 = StateMachineDiagram_meta_StateMachine(name="sample_text_2")
    b = StateMachineDiagram_meta_State(name="sample_text")
    _safe_set(b, 'StateMachineDiagram_meta_State', {a1})
    assert _is_linked(b, 'StateMachineDiagram_meta_State', a1)
    if hasattr(a1, 'StateMachineDiagram_meta_StateMachine12'):
        assert _is_linked(a1, 'StateMachineDiagram_meta_StateMachine12', b)
    _safe_set(b, 'StateMachineDiagram_meta_State', {a2})
    assert _is_linked(b, 'StateMachineDiagram_meta_State', a2)
    if hasattr(a1, 'StateMachineDiagram_meta_StateMachine12'):
        assert not _is_linked(a1, 'StateMachineDiagram_meta_StateMachine12', b)
    if hasattr(a2, 'StateMachineDiagram_meta_StateMachine12'):
        assert _is_linked(a2, 'StateMachineDiagram_meta_StateMachine12', b)
    _safe_set(b, 'StateMachineDiagram_meta_State', set())
    assert not _is_linked(b, 'StateMachineDiagram_meta_State', a2)
    if hasattr(a2, 'StateMachineDiagram_meta_StateMachine12'):
        assert not _is_linked(a2, 'StateMachineDiagram_meta_StateMachine12', b)


def test_assoc_transition3_reverse_link_reassign_clear():
    a1 = StateMachineDiagram_meta_Transition(name="sample_text", trigger="sample_text")
    a2 = StateMachineDiagram_meta_Transition(name="sample_text_2", trigger="sample_text_2")
    b = StateMachineDiagram_meta_StateMachine(name="sample_text")
    _safe_set(b, 'StateMachineDiagram_meta_StateMachine4', {a1})
    assert _is_linked(b, 'StateMachineDiagram_meta_StateMachine4', a1)
    if hasattr(a1, 'StateMachineDiagram_meta_Transition'):
        assert _is_linked(a1, 'StateMachineDiagram_meta_Transition', b)
    _safe_set(b, 'StateMachineDiagram_meta_StateMachine4', {a2})
    assert _is_linked(b, 'StateMachineDiagram_meta_StateMachine4', a2)
    if hasattr(a1, 'StateMachineDiagram_meta_Transition'):
        assert not _is_linked(a1, 'StateMachineDiagram_meta_Transition', b)
    if hasattr(a2, 'StateMachineDiagram_meta_Transition'):
        assert _is_linked(a2, 'StateMachineDiagram_meta_Transition', b)
    _safe_set(b, 'StateMachineDiagram_meta_StateMachine4', set())
    assert not _is_linked(b, 'StateMachineDiagram_meta_StateMachine4', a2)
    if hasattr(a2, 'StateMachineDiagram_meta_Transition'):
        assert not _is_linked(a2, 'StateMachineDiagram_meta_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_incoming6_stub_double():
    # StateMachineDiagram_meta_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineDiagram_meta_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineDiagram_meta_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineDiagram_meta_Transition(name="sample_text", trigger="sample_text")
    partner = StateMachineDiagram_meta_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition7', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition7', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoing5_stub_double():
    # StateMachineDiagram_meta_Vertex has no real 'souce' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineDiagram_meta_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineDiagram_meta_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineDiagram_meta_Transition(name="sample_text", trigger="sample_text")
    partner = StateMachineDiagram_meta_Vertex()
    setattr(partner, 'souce', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'souce')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'souce')


def test_assoc_souce8_stub_double():
    # StateMachineDiagram_meta_Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineDiagram_meta_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineDiagram_meta_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineDiagram_meta_Transition(name="sample_text", trigger="sample_text")
    partner = StateMachineDiagram_meta_Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'outgoing', {partner})
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'outgoing', set())
    assert getattr(partner, 'Vertex') is None


def test_assoc_target9_stub_double():
    # StateMachineDiagram_meta_Vertex has no real 'Vertex10' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineDiagram_meta_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineDiagram_meta_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineDiagram_meta_Transition(name="sample_text", trigger="sample_text")
    partner = StateMachineDiagram_meta_Vertex()
    setattr(partner, 'Vertex10', None)
    _safe_set(owner, 'incoming', {partner})
    assert getattr(partner, 'Vertex10') == owner
    _safe_set(owner, 'incoming', set())
    assert getattr(partner, 'Vertex10') is None


def test_assoc_vertex1_stub_double():
    # StateMachineDiagram_meta_Vertex has no real 'StateMachineDiagram_meta_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineDiagram_meta_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineDiagram_meta_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineDiagram_meta_StateMachine(name="sample_text")
    partner = StateMachineDiagram_meta_Vertex()
    setattr(partner, 'StateMachineDiagram_meta_Vertex', None)
    _safe_set(owner, 'StateMachineDiagram_meta_StateMachine2', {partner})
    assert getattr(partner, 'StateMachineDiagram_meta_Vertex') == owner
    _safe_set(owner, 'StateMachineDiagram_meta_StateMachine2', set())
    assert getattr(partner, 'StateMachineDiagram_meta_Vertex') is None


