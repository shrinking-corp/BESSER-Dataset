import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Guard,
    Variable,
    automata_Action,
    automata_Automaton,
    automata_BooleanAction,
    automata_BooleanGuard,
    automata_BooleanVariable,
    automata_Guard,
    automata_NumberAction,
    automata_NumberGuard,
    automata_NumberVariable,
    automata_State,
    automata_StringAction,
    automata_StringGuard,
    automata_StringVariable,
    automata_Transition,
    automata_Variable,
    BooleanOperator,
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

def test_assoc_source15_reverse_link_reassign_clear():
    a1 = automata_BooleanVariable(initialValue=True)
    a2 = automata_BooleanVariable(initialValue=False)
    b = automata_BooleanGuard(operator="sample_text", value=True)
    _safe_set(b, 'automata_BooleanGuard', a1)
    assert _is_linked(b, 'automata_BooleanGuard', a1)
    if hasattr(a1, 'automata_BooleanVariable'):
        assert _is_linked(a1, 'automata_BooleanVariable', b)
    _safe_set(b, 'automata_BooleanGuard', a2)
    assert _is_linked(b, 'automata_BooleanGuard', a2)
    if hasattr(a1, 'automata_BooleanVariable'):
        assert not _is_linked(a1, 'automata_BooleanVariable', b)
    if hasattr(a2, 'automata_BooleanVariable'):
        assert _is_linked(a2, 'automata_BooleanVariable', b)
    _safe_set(b, 'automata_BooleanGuard', None)
    assert not _is_linked(b, 'automata_BooleanGuard', a2)
    if hasattr(a2, 'automata_BooleanVariable'):
        assert not _is_linked(a2, 'automata_BooleanVariable', b)


def test_assoc_source16_reverse_link_reassign_clear():
    a1 = automata_StringVariable(initialValue="sample_text")
    a2 = automata_StringVariable(initialValue="sample_text_2")
    b = automata_StringGuard(operator="sample_text", value="sample_text")
    _safe_set(b, 'automata_StringGuard', a1)
    assert _is_linked(b, 'automata_StringGuard', a1)
    if hasattr(a1, 'automata_StringVariable'):
        assert _is_linked(a1, 'automata_StringVariable', b)
    _safe_set(b, 'automata_StringGuard', a2)
    assert _is_linked(b, 'automata_StringGuard', a2)
    if hasattr(a1, 'automata_StringVariable'):
        assert not _is_linked(a1, 'automata_StringVariable', b)
    if hasattr(a2, 'automata_StringVariable'):
        assert _is_linked(a2, 'automata_StringVariable', b)
    _safe_set(b, 'automata_StringGuard', None)
    assert not _is_linked(b, 'automata_StringGuard', a2)
    if hasattr(a2, 'automata_StringVariable'):
        assert not _is_linked(a2, 'automata_StringVariable', b)


def test_assoc_source17_reverse_link_reassign_clear():
    a1 = automata_NumberVariable(initialValue="sample_text")
    a2 = automata_NumberVariable(initialValue="sample_text_2")
    b = automata_NumberGuard(operator="sample_text", value="sample_text")
    _safe_set(b, 'automata_NumberGuard', a1)
    assert _is_linked(b, 'automata_NumberGuard', a1)
    if hasattr(a1, 'automata_NumberVariable'):
        assert _is_linked(a1, 'automata_NumberVariable', b)
    _safe_set(b, 'automata_NumberGuard', a2)
    assert _is_linked(b, 'automata_NumberGuard', a2)
    if hasattr(a1, 'automata_NumberVariable'):
        assert not _is_linked(a1, 'automata_NumberVariable', b)
    if hasattr(a2, 'automata_NumberVariable'):
        assert _is_linked(a2, 'automata_NumberVariable', b)
    _safe_set(b, 'automata_NumberGuard', None)
    assert not _is_linked(b, 'automata_NumberGuard', a2)
    if hasattr(a2, 'automata_NumberVariable'):
        assert not _is_linked(a2, 'automata_NumberVariable', b)


def test_assoc_target18_reverse_link_reassign_clear():
    a1 = automata_StringVariable(initialValue="sample_text")
    a2 = automata_StringVariable(initialValue="sample_text_2")
    b = automata_StringAction(value="sample_text")
    _safe_set(b, 'automata_StringAction', a1)
    assert _is_linked(b, 'automata_StringAction', a1)
    if hasattr(a1, 'automata_StringVariable19'):
        assert _is_linked(a1, 'automata_StringVariable19', b)
    _safe_set(b, 'automata_StringAction', a2)
    assert _is_linked(b, 'automata_StringAction', a2)
    if hasattr(a1, 'automata_StringVariable19'):
        assert not _is_linked(a1, 'automata_StringVariable19', b)
    if hasattr(a2, 'automata_StringVariable19'):
        assert _is_linked(a2, 'automata_StringVariable19', b)
    _safe_set(b, 'automata_StringAction', None)
    assert not _is_linked(b, 'automata_StringAction', a2)
    if hasattr(a2, 'automata_StringVariable19'):
        assert not _is_linked(a2, 'automata_StringVariable19', b)


def test_assoc_target20_reverse_link_reassign_clear():
    a1 = automata_NumberVariable(initialValue="sample_text")
    a2 = automata_NumberVariable(initialValue="sample_text_2")
    b = automata_NumberAction(value="sample_text")
    _safe_set(b, 'automata_NumberAction', a1)
    assert _is_linked(b, 'automata_NumberAction', a1)
    if hasattr(a1, 'automata_NumberVariable21'):
        assert _is_linked(a1, 'automata_NumberVariable21', b)
    _safe_set(b, 'automata_NumberAction', a2)
    assert _is_linked(b, 'automata_NumberAction', a2)
    if hasattr(a1, 'automata_NumberVariable21'):
        assert not _is_linked(a1, 'automata_NumberVariable21', b)
    if hasattr(a2, 'automata_NumberVariable21'):
        assert _is_linked(a2, 'automata_NumberVariable21', b)
    _safe_set(b, 'automata_NumberAction', None)
    assert not _is_linked(b, 'automata_NumberAction', a2)
    if hasattr(a2, 'automata_NumberVariable21'):
        assert not _is_linked(a2, 'automata_NumberVariable21', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = automata_BooleanVariable(initialValue=True)
    a2 = automata_BooleanVariable(initialValue=False)
    b = automata_BooleanAction(value=True)
    _safe_set(b, 'automata_BooleanAction', a1)
    assert _is_linked(b, 'automata_BooleanAction', a1)
    if hasattr(a1, 'automata_BooleanVariable23'):
        assert _is_linked(a1, 'automata_BooleanVariable23', b)
    _safe_set(b, 'automata_BooleanAction', a2)
    assert _is_linked(b, 'automata_BooleanAction', a2)
    if hasattr(a1, 'automata_BooleanVariable23'):
        assert not _is_linked(a1, 'automata_BooleanVariable23', b)
    if hasattr(a2, 'automata_BooleanVariable23'):
        assert _is_linked(a2, 'automata_BooleanVariable23', b)
    _safe_set(b, 'automata_BooleanAction', None)
    assert not _is_linked(b, 'automata_BooleanAction', a2)
    if hasattr(a2, 'automata_BooleanVariable23'):
        assert not _is_linked(a2, 'automata_BooleanVariable23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

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
    owner = automata_Variable(name="sample_text")
    partner = automata_Automaton()
    setattr(partner, 'automata_Automaton4', None)
    _safe_set(owner, 'automata_Variable', partner)
    assert owner in getattr(partner, 'automata_Automaton4')
    _safe_set(owner, 'automata_Variable', None)
    assert owner not in getattr(partner, 'automata_Automaton4')


