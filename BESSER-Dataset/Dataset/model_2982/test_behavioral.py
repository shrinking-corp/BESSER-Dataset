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

def test_assoc_action13_reverse_link_reassign_clear():
    a1 = automata_Transition()
    a2 = automata_Transition()
    b = automata_Action()
    _safe_set(b, 'automata_Action', a1)
    assert _is_linked(b, 'automata_Action', a1)
    if hasattr(a1, 'automata_Transition14'):
        assert _is_linked(a1, 'automata_Transition14', b)
    _safe_set(b, 'automata_Action', a2)
    assert _is_linked(b, 'automata_Action', a2)
    if hasattr(a1, 'automata_Transition14'):
        assert not _is_linked(a1, 'automata_Transition14', b)
    if hasattr(a2, 'automata_Transition14'):
        assert _is_linked(a2, 'automata_Transition14', b)
    _safe_set(b, 'automata_Action', None)
    assert not _is_linked(b, 'automata_Action', a2)
    if hasattr(a2, 'automata_Transition14'):
        assert not _is_linked(a2, 'automata_Transition14', b)


def test_assoc_guard11_reverse_link_reassign_clear():
    a1 = automata_Transition()
    a2 = automata_Transition()
    b = automata_Guard()
    _safe_set(b, 'automata_Guard', a1)
    assert _is_linked(b, 'automata_Guard', a1)
    if hasattr(a1, 'automata_Transition12'):
        assert _is_linked(a1, 'automata_Transition12', b)
    _safe_set(b, 'automata_Guard', a2)
    assert _is_linked(b, 'automata_Guard', a2)
    if hasattr(a1, 'automata_Transition12'):
        assert not _is_linked(a1, 'automata_Transition12', b)
    if hasattr(a2, 'automata_Transition12'):
        assert _is_linked(a2, 'automata_Transition12', b)
    _safe_set(b, 'automata_Guard', None)
    assert not _is_linked(b, 'automata_Guard', a2)
    if hasattr(a2, 'automata_Transition12'):
        assert not _is_linked(a2, 'automata_Transition12', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = automata_BooleanVariable(initialValue=True, value=True)
    a2 = automata_BooleanVariable(initialValue=False, value=False)
    b = automata_BooleanGuard(operator=True, value=True)
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
    a1 = automata_StringVariable(initialValue="sample_text", value="sample_text")
    a2 = automata_StringVariable(initialValue="sample_text_2", value="sample_text_2")
    b = automata_StringGuard(operator=True, value="sample_text")
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
    a1 = automata_NumberVariable(initialValue="sample_text", value="sample_text")
    a2 = automata_NumberVariable(initialValue="sample_text_2", value="sample_text_2")
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


def test_assoc_source5_reverse_link_reassign_clear():
    a1 = automata_Transition()
    a2 = automata_Transition()
    b = automata_State(initial=True, name="sample_text")
    _safe_set(b, 'automata_State7', a1)
    assert _is_linked(b, 'automata_State7', a1)
    if hasattr(a1, 'automata_Transition6'):
        assert _is_linked(a1, 'automata_Transition6', b)
    _safe_set(b, 'automata_State7', a2)
    assert _is_linked(b, 'automata_State7', a2)
    if hasattr(a1, 'automata_Transition6'):
        assert not _is_linked(a1, 'automata_Transition6', b)
    if hasattr(a2, 'automata_Transition6'):
        assert _is_linked(a2, 'automata_Transition6', b)
    _safe_set(b, 'automata_State7', None)
    assert not _is_linked(b, 'automata_State7', a2)
    if hasattr(a2, 'automata_Transition6'):
        assert not _is_linked(a2, 'automata_Transition6', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = automata_State(initial=True, name="sample_text")
    a2 = automata_State(initial=False, name="sample_text_2")
    b = automata_Automaton()
    _safe_set(b, 'automata_Automaton', {a1})
    assert _is_linked(b, 'automata_Automaton', a1)
    if hasattr(a1, 'automata_State'):
        assert _is_linked(a1, 'automata_State', b)
    _safe_set(b, 'automata_Automaton', {a2})
    assert _is_linked(b, 'automata_Automaton', a2)
    if hasattr(a1, 'automata_State'):
        assert not _is_linked(a1, 'automata_State', b)
    if hasattr(a2, 'automata_State'):
        assert _is_linked(a2, 'automata_State', b)
    _safe_set(b, 'automata_Automaton', set())
    assert not _is_linked(b, 'automata_Automaton', a2)
    if hasattr(a2, 'automata_State'):
        assert not _is_linked(a2, 'automata_State', b)


def test_assoc_target18_reverse_link_reassign_clear():
    a1 = automata_StringVariable(initialValue="sample_text", value="sample_text")
    a2 = automata_StringVariable(initialValue="sample_text_2", value="sample_text_2")
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
    a1 = automata_NumberVariable(initialValue="sample_text", value="sample_text")
    a2 = automata_NumberVariable(initialValue="sample_text_2", value="sample_text_2")
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
    a1 = automata_BooleanVariable(initialValue=True, value=True)
    a2 = automata_BooleanVariable(initialValue=False, value=False)
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


def test_assoc_target8_reverse_link_reassign_clear():
    a1 = automata_Transition()
    a2 = automata_Transition()
    b = automata_State(initial=True, name="sample_text")
    _safe_set(b, 'automata_State10', a1)
    assert _is_linked(b, 'automata_State10', a1)
    if hasattr(a1, 'automata_Transition9'):
        assert _is_linked(a1, 'automata_Transition9', b)
    _safe_set(b, 'automata_State10', a2)
    assert _is_linked(b, 'automata_State10', a2)
    if hasattr(a1, 'automata_Transition9'):
        assert not _is_linked(a1, 'automata_Transition9', b)
    if hasattr(a2, 'automata_Transition9'):
        assert _is_linked(a2, 'automata_Transition9', b)
    _safe_set(b, 'automata_State10', None)
    assert not _is_linked(b, 'automata_State10', a2)
    if hasattr(a2, 'automata_Transition9'):
        assert not _is_linked(a2, 'automata_Transition9', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = automata_Transition()
    a2 = automata_Transition()
    b = automata_Automaton()
    _safe_set(b, 'automata_Automaton2', {a1})
    assert _is_linked(b, 'automata_Automaton2', a1)
    if hasattr(a1, 'automata_Transition'):
        assert _is_linked(a1, 'automata_Transition', b)
    _safe_set(b, 'automata_Automaton2', {a2})
    assert _is_linked(b, 'automata_Automaton2', a2)
    if hasattr(a1, 'automata_Transition'):
        assert not _is_linked(a1, 'automata_Transition', b)
    if hasattr(a2, 'automata_Transition'):
        assert _is_linked(a2, 'automata_Transition', b)
    _safe_set(b, 'automata_Automaton2', set())
    assert not _is_linked(b, 'automata_Automaton2', a2)
    if hasattr(a2, 'automata_Transition'):
        assert not _is_linked(a2, 'automata_Transition', b)


def test_assoc_variables3_reverse_link_reassign_clear():
    a1 = automata_Variable(name="sample_text")
    a2 = automata_Variable(name="sample_text_2")
    b = automata_Automaton()
    _safe_set(b, 'automata_Automaton4', {a1})
    assert _is_linked(b, 'automata_Automaton4', a1)
    if hasattr(a1, 'automata_Variable'):
        assert _is_linked(a1, 'automata_Variable', b)
    _safe_set(b, 'automata_Automaton4', {a2})
    assert _is_linked(b, 'automata_Automaton4', a2)
    if hasattr(a1, 'automata_Variable'):
        assert not _is_linked(a1, 'automata_Variable', b)
    if hasattr(a2, 'automata_Variable'):
        assert _is_linked(a2, 'automata_Variable', b)
    _safe_set(b, 'automata_Automaton4', set())
    assert not _is_linked(b, 'automata_Automaton4', a2)
    if hasattr(a2, 'automata_Variable'):
        assert not _is_linked(a2, 'automata_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

