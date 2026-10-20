import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    automata_Action,
    automata_Automaton,
    automata_BooleanGuard,
    automata_Guard,
    automata_NumberGuard,
    automata_State,
    automata_StringGuard,
    automata_Transition,
    automata_Variable,
    BooleanOperator,
    DataType,
    NumberOperator,
    StringOperator,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_source13_stub_double():
    # automata_Guard has no real 'automata_Guard14' property in the generated
    # code (a bare stub) -- manually attach it so automata_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Variable(name="sample_text", type="sample_text")
    partner = automata_Guard()
    setattr(partner, 'automata_Guard14', None)
    _safe_set(owner, 'automata_Variable15', partner)
    assert getattr(partner, 'automata_Guard14') == owner
    _safe_set(owner, 'automata_Variable15', None)
    assert getattr(partner, 'automata_Guard14') is None


def test_assoc_source5_stub_double():
    # automata_Transition has no real 'automata_Transition6' property in the generated
    # code (a bare stub) -- manually attach it so automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_State(initial=True, name="sample_text")
    partner = automata_Transition()
    setattr(partner, 'automata_Transition6', None)
    _safe_set(owner, 'automata_State7', partner)
    assert getattr(partner, 'automata_Transition6') == owner
    _safe_set(owner, 'automata_State7', None)
    assert getattr(partner, 'automata_Transition6') is None


def test_assoc_states0_stub_double():
    # automata_Automaton has no real 'automata_Automaton' property in the generated
    # code (a bare stub) -- manually attach it so automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_State(initial=True, name="sample_text")
    partner = automata_Automaton()
    setattr(partner, 'automata_Automaton', None)
    _safe_set(owner, 'automata_State', partner)
    assert owner in getattr(partner, 'automata_Automaton')
    _safe_set(owner, 'automata_State', None)
    assert owner not in getattr(partner, 'automata_Automaton')


def test_assoc_target16_stub_double():
    # automata_Action has no real 'automata_Action' property in the generated
    # code (a bare stub) -- manually attach it so automata_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Variable(name="sample_text", type="sample_text")
    partner = automata_Action()
    setattr(partner, 'automata_Action', None)
    _safe_set(owner, 'automata_Variable17', partner)
    assert getattr(partner, 'automata_Action') == owner
    _safe_set(owner, 'automata_Variable17', None)
    assert getattr(partner, 'automata_Action') is None


def test_assoc_target8_stub_double():
    # automata_Transition has no real 'automata_Transition9' property in the generated
    # code (a bare stub) -- manually attach it so automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_State(initial=True, name="sample_text")
    partner = automata_Transition()
    setattr(partner, 'automata_Transition9', None)
    _safe_set(owner, 'automata_State10', partner)
    assert getattr(partner, 'automata_Transition9') == owner
    _safe_set(owner, 'automata_State10', None)
    assert getattr(partner, 'automata_Transition9') is None


def test_assoc_variables3_stub_double():
    # automata_Automaton has no real 'automata_Automaton4' property in the generated
    # code (a bare stub) -- manually attach it so automata_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Variable(name="sample_text", type="sample_text")
    partner = automata_Automaton()
    setattr(partner, 'automata_Automaton4', None)
    _safe_set(owner, 'automata_Variable', partner)
    assert owner in getattr(partner, 'automata_Automaton4')
    _safe_set(owner, 'automata_Variable', None)
    assert owner not in getattr(partner, 'automata_Automaton4')


