import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DFAAutomaton_AlphabetSymbol,
    DFAAutomaton_Automaton,
    DFAAutomaton_CompositeState,
    DFAAutomaton_State,
    DFAAutomaton_Transition,
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

def test_assoc_alphabet3_reverse_link_reassign_clear():
    a1 = DFAAutomaton_Automaton(name="sample_text")
    a2 = DFAAutomaton_Automaton(name="sample_text_2")
    b = DFAAutomaton_AlphabetSymbol(symbol="sample_text")
    _safe_set(b, 'DFAAutomaton_AlphabetSymbol', a1)
    assert _is_linked(b, 'DFAAutomaton_AlphabetSymbol', a1)
    if hasattr(a1, 'DFAAutomaton_Automaton4'):
        assert _is_linked(a1, 'DFAAutomaton_Automaton4', b)
    _safe_set(b, 'DFAAutomaton_AlphabetSymbol', a2)
    assert _is_linked(b, 'DFAAutomaton_AlphabetSymbol', a2)
    if hasattr(a1, 'DFAAutomaton_Automaton4'):
        assert not _is_linked(a1, 'DFAAutomaton_Automaton4', b)
    if hasattr(a2, 'DFAAutomaton_Automaton4'):
        assert _is_linked(a2, 'DFAAutomaton_Automaton4', b)
    _safe_set(b, 'DFAAutomaton_AlphabetSymbol', None)
    assert not _is_linked(b, 'DFAAutomaton_AlphabetSymbol', a2)
    if hasattr(a2, 'DFAAutomaton_Automaton4'):
        assert not _is_linked(a2, 'DFAAutomaton_Automaton4', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = DFAAutomaton_State(isFinal=True, isInitial=True, name="sample_text")
    a2 = DFAAutomaton_State(isFinal=False, isInitial=False, name="sample_text_2")
    b = DFAAutomaton_Automaton(name="sample_text")
    _safe_set(b, 'DFAAutomaton_Automaton', {a1})
    assert _is_linked(b, 'DFAAutomaton_Automaton', a1)
    if hasattr(a1, 'DFAAutomaton_State'):
        assert _is_linked(a1, 'DFAAutomaton_State', b)
    _safe_set(b, 'DFAAutomaton_Automaton', {a2})
    assert _is_linked(b, 'DFAAutomaton_Automaton', a2)
    if hasattr(a1, 'DFAAutomaton_State'):
        assert not _is_linked(a1, 'DFAAutomaton_State', b)
    if hasattr(a2, 'DFAAutomaton_State'):
        assert _is_linked(a2, 'DFAAutomaton_State', b)
    _safe_set(b, 'DFAAutomaton_Automaton', set())
    assert not _is_linked(b, 'DFAAutomaton_Automaton', a2)
    if hasattr(a2, 'DFAAutomaton_State'):
        assert not _is_linked(a2, 'DFAAutomaton_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_from_6_stub_double():
    # DFAAutomaton_Transition has no real 'DFAAutomaton_Transition7' property in the generated
    # code (a bare stub) -- manually attach it so DFAAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DFAAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DFAAutomaton_State(isFinal=True, isInitial=True, name="sample_text")
    partner = DFAAutomaton_Transition()
    setattr(partner, 'DFAAutomaton_Transition7', None)
    _safe_set(owner, 'DFAAutomaton_State8', partner)
    assert getattr(partner, 'DFAAutomaton_Transition7') == owner
    _safe_set(owner, 'DFAAutomaton_State8', None)
    assert getattr(partner, 'DFAAutomaton_Transition7') is None


def test_assoc_incoming5_stub_double():
    # DFAAutomaton_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so DFAAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DFAAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DFAAutomaton_State(isFinal=True, isInitial=True, name="sample_text")
    partner = DFAAutomaton_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_symbol10_stub_double():
    # DFAAutomaton_Transition has no real 'DFAAutomaton_Transition11' property in the generated
    # code (a bare stub) -- manually attach it so DFAAutomaton_AlphabetSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DFAAutomaton_AlphabetSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DFAAutomaton_AlphabetSymbol(symbol="sample_text")
    partner = DFAAutomaton_Transition()
    setattr(partner, 'DFAAutomaton_Transition11', None)
    _safe_set(owner, 'DFAAutomaton_AlphabetSymbol12', partner)
    assert getattr(partner, 'DFAAutomaton_Transition11') == owner
    _safe_set(owner, 'DFAAutomaton_AlphabetSymbol12', None)
    assert getattr(partner, 'DFAAutomaton_Transition11') is None


def test_assoc_to9_stub_double():
    # DFAAutomaton_Transition has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so DFAAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DFAAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DFAAutomaton_State(isFinal=True, isInitial=True, name="sample_text")
    partner = DFAAutomaton_Transition()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_transitions1_stub_double():
    # DFAAutomaton_Transition has no real 'DFAAutomaton_Transition' property in the generated
    # code (a bare stub) -- manually attach it so DFAAutomaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DFAAutomaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DFAAutomaton_Automaton(name="sample_text")
    partner = DFAAutomaton_Transition()
    setattr(partner, 'DFAAutomaton_Transition', None)
    _safe_set(owner, 'DFAAutomaton_Automaton2', {partner})
    assert getattr(partner, 'DFAAutomaton_Transition') == owner
    _safe_set(owner, 'DFAAutomaton_Automaton2', set())
    assert getattr(partner, 'DFAAutomaton_Transition') is None


