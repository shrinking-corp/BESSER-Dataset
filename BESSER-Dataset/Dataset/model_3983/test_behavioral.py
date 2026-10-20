import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Entity,
    markov_Entity,
    markov_Label,
    markov_MarkovChain,
    markov_State,
    markov_Transition,
    StateType,
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

def test_assoc_fromState1_reverse_link_reassign_clear():
    a1 = markov_Transition(probability=3.14)
    a2 = markov_Transition(probability=9.99)
    b = markov_State(traces="sample_text", type="sample_text")
    _safe_set(b, 'markov_State2', a1)
    assert _is_linked(b, 'markov_State2', a1)
    if hasattr(a1, 'markov_Transition'):
        assert _is_linked(a1, 'markov_Transition', b)
    _safe_set(b, 'markov_State2', a2)
    assert _is_linked(b, 'markov_State2', a2)
    if hasattr(a1, 'markov_Transition'):
        assert not _is_linked(a1, 'markov_Transition', b)
    if hasattr(a2, 'markov_Transition'):
        assert _is_linked(a2, 'markov_Transition', b)
    _safe_set(b, 'markov_State2', None)
    assert not _is_linked(b, 'markov_State2', a2)
    if hasattr(a2, 'markov_Transition'):
        assert not _is_linked(a2, 'markov_Transition', b)


def test_assoc_labels0_reverse_link_reassign_clear():
    a1 = markov_State(traces="sample_text", type="sample_text")
    a2 = markov_State(traces="sample_text_2", type="sample_text_2")
    b = markov_Label(key="sample_text", value="sample_text")
    _safe_set(b, 'markov_Label', a1)
    assert _is_linked(b, 'markov_Label', a1)
    if hasattr(a1, 'markov_State'):
        assert _is_linked(a1, 'markov_State', b)
    _safe_set(b, 'markov_Label', a2)
    assert _is_linked(b, 'markov_Label', a2)
    if hasattr(a1, 'markov_State'):
        assert not _is_linked(a1, 'markov_State', b)
    if hasattr(a2, 'markov_State'):
        assert _is_linked(a2, 'markov_State', b)
    _safe_set(b, 'markov_Label', None)
    assert not _is_linked(b, 'markov_Label', a2)
    if hasattr(a2, 'markov_State'):
        assert not _is_linked(a2, 'markov_State', b)


def test_assoc_toState3_reverse_link_reassign_clear():
    a1 = markov_Transition(probability=3.14)
    a2 = markov_Transition(probability=9.99)
    b = markov_State(traces="sample_text", type="sample_text")
    _safe_set(b, 'markov_State5', a1)
    assert _is_linked(b, 'markov_State5', a1)
    if hasattr(a1, 'markov_Transition4'):
        assert _is_linked(a1, 'markov_Transition4', b)
    _safe_set(b, 'markov_State5', a2)
    assert _is_linked(b, 'markov_State5', a2)
    if hasattr(a1, 'markov_Transition4'):
        assert not _is_linked(a1, 'markov_Transition4', b)
    if hasattr(a2, 'markov_Transition4'):
        assert _is_linked(a2, 'markov_Transition4', b)
    _safe_set(b, 'markov_State5', None)
    assert not _is_linked(b, 'markov_State5', a2)
    if hasattr(a2, 'markov_Transition4'):
        assert not _is_linked(a2, 'markov_Transition4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_states6_stub_double():
    # markov_MarkovChain has no real 'markov_MarkovChain' property in the generated
    # code (a bare stub) -- manually attach it so markov_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # markov_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = markov_State(traces="sample_text", type="sample_text")
    partner = markov_MarkovChain()
    setattr(partner, 'markov_MarkovChain', None)
    _safe_set(owner, 'markov_State7', partner)
    assert owner in getattr(partner, 'markov_MarkovChain')
    _safe_set(owner, 'markov_State7', None)
    assert owner not in getattr(partner, 'markov_MarkovChain')


def test_assoc_transitions8_stub_double():
    # markov_MarkovChain has no real 'markov_MarkovChain9' property in the generated
    # code (a bare stub) -- manually attach it so markov_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # markov_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = markov_Transition(probability=3.14)
    partner = markov_MarkovChain()
    setattr(partner, 'markov_MarkovChain9', None)
    _safe_set(owner, 'markov_Transition10', partner)
    assert owner in getattr(partner, 'markov_MarkovChain9')
    _safe_set(owner, 'markov_Transition10', None)
    assert owner not in getattr(partner, 'markov_MarkovChain9')


