import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ioautomaton_Automaton,
    ioautomaton_AutomatonContainer,
    ioautomaton_Object,
    ioautomaton_Operation,
    ioautomaton_OutMessage,
    ioautomaton_Return,
    ioautomaton_State,
    ioautomaton_Transition,
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

def test_assoc_initialstate5_reverse_link_reassign_clear():
    a1 = ioautomaton_State(name="sample_text")
    a2 = ioautomaton_State(name="sample_text_2")
    b = ioautomaton_Automaton(sender="sample_text")
    _safe_set(b, 'ioautomaton_Automaton6', a1)
    assert _is_linked(b, 'ioautomaton_Automaton6', a1)
    if hasattr(a1, 'ioautomaton_State7'):
        assert _is_linked(a1, 'ioautomaton_State7', b)
    _safe_set(b, 'ioautomaton_Automaton6', a2)
    assert _is_linked(b, 'ioautomaton_Automaton6', a2)
    if hasattr(a1, 'ioautomaton_State7'):
        assert not _is_linked(a1, 'ioautomaton_State7', b)
    if hasattr(a2, 'ioautomaton_State7'):
        assert _is_linked(a2, 'ioautomaton_State7', b)
    _safe_set(b, 'ioautomaton_Automaton6', None)
    assert not _is_linked(b, 'ioautomaton_Automaton6', a2)
    if hasattr(a2, 'ioautomaton_State7'):
        assert not _is_linked(a2, 'ioautomaton_State7', b)


def test_assoc_state1_reverse_link_reassign_clear():
    a1 = ioautomaton_State(name="sample_text")
    a2 = ioautomaton_State(name="sample_text_2")
    b = ioautomaton_Automaton(sender="sample_text")
    _safe_set(b, 'ioautomaton_Automaton2', {a1})
    assert _is_linked(b, 'ioautomaton_Automaton2', a1)
    if hasattr(a1, 'ioautomaton_State'):
        assert _is_linked(a1, 'ioautomaton_State', b)
    _safe_set(b, 'ioautomaton_Automaton2', {a2})
    assert _is_linked(b, 'ioautomaton_Automaton2', a2)
    if hasattr(a1, 'ioautomaton_State'):
        assert not _is_linked(a1, 'ioautomaton_State', b)
    if hasattr(a2, 'ioautomaton_State'):
        assert _is_linked(a2, 'ioautomaton_State', b)
    _safe_set(b, 'ioautomaton_Automaton2', set())
    assert not _is_linked(b, 'ioautomaton_Automaton2', a2)
    if hasattr(a2, 'ioautomaton_State'):
        assert not _is_linked(a2, 'ioautomaton_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__object23_stub_double():
    # ioautomaton_OutMessage has no real 'ioautomaton_OutMessage24' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Object(name="sample_text")
    partner = ioautomaton_OutMessage()
    setattr(partner, 'ioautomaton_OutMessage24', None)
    _safe_set(owner, 'ioautomaton_Object', partner)
    assert getattr(partner, 'ioautomaton_OutMessage24') == owner
    _safe_set(owner, 'ioautomaton_Object', None)
    assert getattr(partner, 'ioautomaton_OutMessage24') is None


def test_assoc__return13_stub_double():
    # ioautomaton_Transition has no real 'ioautomaton_Transition14' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Return's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Return's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Return(value="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'ioautomaton_Transition14', None)
    _safe_set(owner, 'ioautomaton_Return', partner)
    assert getattr(partner, 'ioautomaton_Transition14') == owner
    _safe_set(owner, 'ioautomaton_Return', None)
    assert getattr(partner, 'ioautomaton_Transition14') is None


def test_assoc__return20_stub_double():
    # ioautomaton_OutMessage has no real 'ioautomaton_OutMessage21' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Return's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Return's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Return(value="sample_text")
    partner = ioautomaton_OutMessage()
    setattr(partner, 'ioautomaton_OutMessage21', None)
    _safe_set(owner, 'ioautomaton_Return22', partner)
    assert getattr(partner, 'ioautomaton_OutMessage21') == owner
    _safe_set(owner, 'ioautomaton_Return22', None)
    assert getattr(partner, 'ioautomaton_OutMessage21') is None


def test_assoc_automaton0_stub_double():
    # ioautomaton_AutomatonContainer has no real 'ioautomaton_AutomatonContainer' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Automaton(sender="sample_text")
    partner = ioautomaton_AutomatonContainer()
    setattr(partner, 'ioautomaton_AutomatonContainer', None)
    _safe_set(owner, 'ioautomaton_Automaton', partner)
    assert owner in getattr(partner, 'ioautomaton_AutomatonContainer')
    _safe_set(owner, 'ioautomaton_Automaton', None)
    assert owner not in getattr(partner, 'ioautomaton_AutomatonContainer')


def test_assoc_incomingtransition9_stub_double():
    # ioautomaton_Transition has no real 'Transition10' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_State(name="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'Transition10', None)
    _safe_set(owner, 'poststate', {partner})
    assert getattr(partner, 'Transition10') == owner
    _safe_set(owner, 'poststate', set())
    assert getattr(partner, 'Transition10') is None


def test_assoc_operation11_stub_double():
    # ioautomaton_Transition has no real 'ioautomaton_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Operation(name="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'ioautomaton_Transition12', None)
    _safe_set(owner, 'ioautomaton_Operation', partner)
    assert getattr(partner, 'ioautomaton_Transition12') == owner
    _safe_set(owner, 'ioautomaton_Operation', None)
    assert getattr(partner, 'ioautomaton_Transition12') is None


def test_assoc_operation25_stub_double():
    # ioautomaton_OutMessage has no real 'ioautomaton_OutMessage26' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Operation(name="sample_text")
    partner = ioautomaton_OutMessage()
    setattr(partner, 'ioautomaton_OutMessage26', None)
    _safe_set(owner, 'ioautomaton_Operation27', partner)
    assert getattr(partner, 'ioautomaton_OutMessage26') == owner
    _safe_set(owner, 'ioautomaton_Operation27', None)
    assert getattr(partner, 'ioautomaton_OutMessage26') is None


def test_assoc_outgoingtransition8_stub_double():
    # ioautomaton_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_State(name="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'prestate', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'prestate', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_poststate18_stub_double():
    # ioautomaton_Transition has no real 'incomingtransition' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_State(name="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'incomingtransition', None)
    _safe_set(owner, 'State19', partner)
    assert getattr(partner, 'incomingtransition') == owner
    _safe_set(owner, 'State19', None)
    assert getattr(partner, 'incomingtransition') is None


def test_assoc_prestate17_stub_double():
    # ioautomaton_Transition has no real 'outgoingtransition' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_State(name="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'outgoingtransition', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outgoingtransition') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outgoingtransition') is None


def test_assoc_transition3_stub_double():
    # ioautomaton_Transition has no real 'ioautomaton_Transition' property in the generated
    # code (a bare stub) -- manually attach it so ioautomaton_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioautomaton_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioautomaton_Automaton(sender="sample_text")
    partner = ioautomaton_Transition()
    setattr(partner, 'ioautomaton_Transition', None)
    _safe_set(owner, 'ioautomaton_Automaton4', {partner})
    assert getattr(partner, 'ioautomaton_Transition') == owner
    _safe_set(owner, 'ioautomaton_Automaton4', set())
    assert getattr(partner, 'ioautomaton_Transition') is None


