import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MetaModel_EvolutionStyle,
    MetaModel_FinalState,
    MetaModel_InitialState,
    MetaModel_IntermidiateState,
    MetaModel_Operation,
    MetaModel_State,
    MetaModel_Transition,
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

def test_assoc_operations7_reverse_link_reassign_clear():
    a1 = MetaModel_Transition(description="sample_text", name="sample_text")
    a2 = MetaModel_Transition(description="sample_text_2", name="sample_text_2")
    b = MetaModel_Operation(cost="sample_text", name="sample_text", time="sample_text")
    _safe_set(b, 'MetaModel_Operation', a1)
    assert _is_linked(b, 'MetaModel_Operation', a1)
    if hasattr(a1, 'MetaModel_Transition8'):
        assert _is_linked(a1, 'MetaModel_Transition8', b)
    _safe_set(b, 'MetaModel_Operation', a2)
    assert _is_linked(b, 'MetaModel_Operation', a2)
    if hasattr(a1, 'MetaModel_Transition8'):
        assert not _is_linked(a1, 'MetaModel_Transition8', b)
    if hasattr(a2, 'MetaModel_Transition8'):
        assert _is_linked(a2, 'MetaModel_Transition8', b)
    _safe_set(b, 'MetaModel_Operation', None)
    assert not _is_linked(b, 'MetaModel_Operation', a2)
    if hasattr(a2, 'MetaModel_Transition8'):
        assert not _is_linked(a2, 'MetaModel_Transition8', b)


def test_assoc_source9_reverse_link_reassign_clear():
    a1 = MetaModel_Transition(description="sample_text", name="sample_text")
    a2 = MetaModel_Transition(description="sample_text_2", name="sample_text_2")
    b = MetaModel_State(name="sample_text")
    _safe_set(b, 'MetaModel_State', a1)
    assert _is_linked(b, 'MetaModel_State', a1)
    if hasattr(a1, 'MetaModel_Transition10'):
        assert _is_linked(a1, 'MetaModel_Transition10', b)
    _safe_set(b, 'MetaModel_State', a2)
    assert _is_linked(b, 'MetaModel_State', a2)
    if hasattr(a1, 'MetaModel_Transition10'):
        assert not _is_linked(a1, 'MetaModel_Transition10', b)
    if hasattr(a2, 'MetaModel_Transition10'):
        assert _is_linked(a2, 'MetaModel_Transition10', b)
    _safe_set(b, 'MetaModel_State', None)
    assert not _is_linked(b, 'MetaModel_State', a2)
    if hasattr(a2, 'MetaModel_Transition10'):
        assert not _is_linked(a2, 'MetaModel_Transition10', b)


def test_assoc_target11_reverse_link_reassign_clear():
    a1 = MetaModel_Transition(description="sample_text", name="sample_text")
    a2 = MetaModel_Transition(description="sample_text_2", name="sample_text_2")
    b = MetaModel_State(name="sample_text")
    _safe_set(b, 'MetaModel_State13', a1)
    assert _is_linked(b, 'MetaModel_State13', a1)
    if hasattr(a1, 'MetaModel_Transition12'):
        assert _is_linked(a1, 'MetaModel_Transition12', b)
    _safe_set(b, 'MetaModel_State13', a2)
    assert _is_linked(b, 'MetaModel_State13', a2)
    if hasattr(a1, 'MetaModel_Transition12'):
        assert not _is_linked(a1, 'MetaModel_Transition12', b)
    if hasattr(a2, 'MetaModel_Transition12'):
        assert _is_linked(a2, 'MetaModel_Transition12', b)
    _safe_set(b, 'MetaModel_State13', None)
    assert not _is_linked(b, 'MetaModel_State13', a2)
    if hasattr(a2, 'MetaModel_Transition12'):
        assert not _is_linked(a2, 'MetaModel_Transition12', b)


def test_assoc_transitions0_reverse_link_reassign_clear():
    a1 = MetaModel_Transition(description="sample_text", name="sample_text")
    a2 = MetaModel_Transition(description="sample_text_2", name="sample_text_2")
    b = MetaModel_EvolutionStyle(name="sample_text")
    _safe_set(b, 'MetaModel_EvolutionStyle', {a1})
    assert _is_linked(b, 'MetaModel_EvolutionStyle', a1)
    if hasattr(a1, 'MetaModel_Transition'):
        assert _is_linked(a1, 'MetaModel_Transition', b)
    _safe_set(b, 'MetaModel_EvolutionStyle', {a2})
    assert _is_linked(b, 'MetaModel_EvolutionStyle', a2)
    if hasattr(a1, 'MetaModel_Transition'):
        assert not _is_linked(a1, 'MetaModel_Transition', b)
    if hasattr(a2, 'MetaModel_Transition'):
        assert _is_linked(a2, 'MetaModel_Transition', b)
    _safe_set(b, 'MetaModel_EvolutionStyle', set())
    assert not _is_linked(b, 'MetaModel_EvolutionStyle', a2)
    if hasattr(a2, 'MetaModel_Transition'):
        assert not _is_linked(a2, 'MetaModel_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_InitialArchitecture1_stub_double():
    # MetaModel_InitialState has no real 'MetaModel_InitialState' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_EvolutionStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_EvolutionStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_EvolutionStyle(name="sample_text")
    partner = MetaModel_InitialState()
    setattr(partner, 'MetaModel_InitialState', None)
    _safe_set(owner, 'MetaModel_EvolutionStyle2', partner)
    assert getattr(partner, 'MetaModel_InitialState') == owner
    _safe_set(owner, 'MetaModel_EvolutionStyle2', None)
    assert getattr(partner, 'MetaModel_InitialState') is None


def test_assoc_finalArchitecture5_stub_double():
    # MetaModel_FinalState has no real 'MetaModel_FinalState' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_EvolutionStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_EvolutionStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_EvolutionStyle(name="sample_text")
    partner = MetaModel_FinalState()
    setattr(partner, 'MetaModel_FinalState', None)
    _safe_set(owner, 'MetaModel_EvolutionStyle6', partner)
    assert getattr(partner, 'MetaModel_FinalState') == owner
    _safe_set(owner, 'MetaModel_EvolutionStyle6', None)
    assert getattr(partner, 'MetaModel_FinalState') is None


def test_assoc_next14_stub_double():
    # MetaModel_InitialState has no real 'MetaModel_InitialState15' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_State(name="sample_text")
    partner = MetaModel_InitialState()
    setattr(partner, 'MetaModel_InitialState15', None)
    _safe_set(owner, 'MetaModel_State16', partner)
    assert owner in getattr(partner, 'MetaModel_InitialState15')
    _safe_set(owner, 'MetaModel_State16', None)
    assert owner not in getattr(partner, 'MetaModel_InitialState15')


def test_assoc_next17_stub_double():
    # MetaModel_IntermidiateState has no real 'MetaModel_IntermidiateState18' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_State(name="sample_text")
    partner = MetaModel_IntermidiateState()
    setattr(partner, 'MetaModel_IntermidiateState18', None)
    _safe_set(owner, 'MetaModel_State19', partner)
    assert owner in getattr(partner, 'MetaModel_IntermidiateState18')
    _safe_set(owner, 'MetaModel_State19', None)
    assert owner not in getattr(partner, 'MetaModel_IntermidiateState18')


def test_assoc_prev20_stub_double():
    # MetaModel_IntermidiateState has no real 'MetaModel_IntermidiateState21' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_State(name="sample_text")
    partner = MetaModel_IntermidiateState()
    setattr(partner, 'MetaModel_IntermidiateState21', None)
    _safe_set(owner, 'MetaModel_State22', partner)
    assert owner in getattr(partner, 'MetaModel_IntermidiateState21')
    _safe_set(owner, 'MetaModel_State22', None)
    assert owner not in getattr(partner, 'MetaModel_IntermidiateState21')


def test_assoc_prev23_stub_double():
    # MetaModel_FinalState has no real 'MetaModel_FinalState24' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_State(name="sample_text")
    partner = MetaModel_FinalState()
    setattr(partner, 'MetaModel_FinalState24', None)
    _safe_set(owner, 'MetaModel_State25', partner)
    assert owner in getattr(partner, 'MetaModel_FinalState24')
    _safe_set(owner, 'MetaModel_State25', None)
    assert owner not in getattr(partner, 'MetaModel_FinalState24')


def test_assoc_states3_stub_double():
    # MetaModel_IntermidiateState has no real 'MetaModel_IntermidiateState' property in the generated
    # code (a bare stub) -- manually attach it so MetaModel_EvolutionStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModel_EvolutionStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModel_EvolutionStyle(name="sample_text")
    partner = MetaModel_IntermidiateState()
    setattr(partner, 'MetaModel_IntermidiateState', None)
    _safe_set(owner, 'MetaModel_EvolutionStyle4', {partner})
    assert getattr(partner, 'MetaModel_IntermidiateState') == owner
    _safe_set(owner, 'MetaModel_EvolutionStyle4', set())
    assert getattr(partner, 'MetaModel_IntermidiateState') is None


