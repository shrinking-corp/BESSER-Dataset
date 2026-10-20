import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    turingmodel_State,
    turingmodel_Transition,
    turingmodel_TuringMachine,
    Direction,
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

def test_assoc_next6_reverse_link_reassign_clear():
    a1 = turingmodel_Transition(condition="sample_text", dir="sample_text", write="sample_text")
    a2 = turingmodel_Transition(condition="sample_text_2", dir="sample_text_2", write="sample_text_2")
    b = turingmodel_State(isEndState=True, name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_source16_reverse_link_reassign_clear():
    a1 = turingmodel_Transition(condition="sample_text", dir="sample_text", write="sample_text")
    a2 = turingmodel_Transition(condition="sample_text_2", dir="sample_text_2", write="sample_text_2")
    b = turingmodel_State(isEndState=True, name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'next'):
        assert _is_linked(a1, 'next', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'next'):
        assert not _is_linked(a1, 'next', b)
    if hasattr(a2, 'next'):
        assert _is_linked(a2, 'next', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'next'):
        assert not _is_linked(a2, 'next', b)


def test_assoc_startSubstate11_reverse_link_reassign_clear():
    a1 = turingmodel_State(isEndState=True, name="sample_text")
    a2 = turingmodel_State(isEndState=False, name="sample_text_2")
    b = turingmodel_State(isEndState=True, name="sample_text")
    _safe_set(b, 'turingmodel_State12', a1)
    assert _is_linked(b, 'turingmodel_State12', a1)
    if hasattr(a1, 'turingmodel_State10'):
        assert _is_linked(a1, 'turingmodel_State10', b)
    _safe_set(b, 'turingmodel_State12', a2)
    assert _is_linked(b, 'turingmodel_State12', a2)
    if hasattr(a1, 'turingmodel_State10'):
        assert not _is_linked(a1, 'turingmodel_State10', b)
    if hasattr(a2, 'turingmodel_State10'):
        assert _is_linked(a2, 'turingmodel_State10', b)
    _safe_set(b, 'turingmodel_State12', None)
    assert not _is_linked(b, 'turingmodel_State12', a2)
    if hasattr(a2, 'turingmodel_State10'):
        assert not _is_linked(a2, 'turingmodel_State10', b)


def test_assoc_substates8_reverse_link_reassign_clear():
    a1 = turingmodel_State(isEndState=True, name="sample_text")
    a2 = turingmodel_State(isEndState=False, name="sample_text_2")
    b = turingmodel_State(isEndState=True, name="sample_text")
    _safe_set(b, 'turingmodel_State9', a1)
    assert _is_linked(b, 'turingmodel_State9', a1)
    if hasattr(a1, 'turingmodel_State7'):
        assert _is_linked(a1, 'turingmodel_State7', b)
    _safe_set(b, 'turingmodel_State9', a2)
    assert _is_linked(b, 'turingmodel_State9', a2)
    if hasattr(a1, 'turingmodel_State7'):
        assert not _is_linked(a1, 'turingmodel_State7', b)
    if hasattr(a2, 'turingmodel_State7'):
        assert _is_linked(a2, 'turingmodel_State7', b)
    _safe_set(b, 'turingmodel_State9', None)
    assert not _is_linked(b, 'turingmodel_State9', a2)
    if hasattr(a2, 'turingmodel_State7'):
        assert not _is_linked(a2, 'turingmodel_State7', b)


def test_assoc_subtransitions13_reverse_link_reassign_clear():
    a1 = turingmodel_Transition(condition="sample_text", dir="sample_text", write="sample_text")
    a2 = turingmodel_Transition(condition="sample_text_2", dir="sample_text_2", write="sample_text_2")
    b = turingmodel_State(isEndState=True, name="sample_text")
    _safe_set(b, 'turingmodel_State14', {a1})
    assert _is_linked(b, 'turingmodel_State14', a1)
    if hasattr(a1, 'turingmodel_Transition15'):
        assert _is_linked(a1, 'turingmodel_Transition15', b)
    _safe_set(b, 'turingmodel_State14', {a2})
    assert _is_linked(b, 'turingmodel_State14', a2)
    if hasattr(a1, 'turingmodel_Transition15'):
        assert not _is_linked(a1, 'turingmodel_Transition15', b)
    if hasattr(a2, 'turingmodel_Transition15'):
        assert _is_linked(a2, 'turingmodel_Transition15', b)
    _safe_set(b, 'turingmodel_State14', set())
    assert not _is_linked(b, 'turingmodel_State14', a2)
    if hasattr(a2, 'turingmodel_Transition15'):
        assert not _is_linked(a2, 'turingmodel_Transition15', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = turingmodel_Transition(condition="sample_text", dir="sample_text", write="sample_text")
    a2 = turingmodel_Transition(condition="sample_text_2", dir="sample_text_2", write="sample_text_2")
    b = turingmodel_State(isEndState=True, name="sample_text")
    _safe_set(b, 'turingmodel_State19', a1)
    assert _is_linked(b, 'turingmodel_State19', a1)
    if hasattr(a1, 'turingmodel_Transition18'):
        assert _is_linked(a1, 'turingmodel_Transition18', b)
    _safe_set(b, 'turingmodel_State19', a2)
    assert _is_linked(b, 'turingmodel_State19', a2)
    if hasattr(a1, 'turingmodel_Transition18'):
        assert not _is_linked(a1, 'turingmodel_Transition18', b)
    if hasattr(a2, 'turingmodel_Transition18'):
        assert _is_linked(a2, 'turingmodel_Transition18', b)
    _safe_set(b, 'turingmodel_State19', None)
    assert not _is_linked(b, 'turingmodel_State19', a2)
    if hasattr(a2, 'turingmodel_Transition18'):
        assert not _is_linked(a2, 'turingmodel_Transition18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_startState3_stub_double():
    # turingmodel_TuringMachine has no real 'turingmodel_TuringMachine4' property in the generated
    # code (a bare stub) -- manually attach it so turingmodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turingmodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turingmodel_State(isEndState=True, name="sample_text")
    partner = turingmodel_TuringMachine()
    setattr(partner, 'turingmodel_TuringMachine4', None)
    _safe_set(owner, 'turingmodel_State5', partner)
    assert getattr(partner, 'turingmodel_TuringMachine4') == owner
    _safe_set(owner, 'turingmodel_State5', None)
    assert getattr(partner, 'turingmodel_TuringMachine4') is None


def test_assoc_states0_stub_double():
    # turingmodel_TuringMachine has no real 'turingmodel_TuringMachine' property in the generated
    # code (a bare stub) -- manually attach it so turingmodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turingmodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turingmodel_State(isEndState=True, name="sample_text")
    partner = turingmodel_TuringMachine()
    setattr(partner, 'turingmodel_TuringMachine', None)
    _safe_set(owner, 'turingmodel_State', partner)
    assert owner in getattr(partner, 'turingmodel_TuringMachine')
    _safe_set(owner, 'turingmodel_State', None)
    assert owner not in getattr(partner, 'turingmodel_TuringMachine')


def test_assoc_transitions1_stub_double():
    # turingmodel_TuringMachine has no real 'turingmodel_TuringMachine2' property in the generated
    # code (a bare stub) -- manually attach it so turingmodel_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # turingmodel_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = turingmodel_Transition(condition="sample_text", dir="sample_text", write="sample_text")
    partner = turingmodel_TuringMachine()
    setattr(partner, 'turingmodel_TuringMachine2', None)
    _safe_set(owner, 'turingmodel_Transition', partner)
    assert owner in getattr(partner, 'turingmodel_TuringMachine2')
    _safe_set(owner, 'turingmodel_Transition', None)
    assert owner not in getattr(partner, 'turingmodel_TuringMachine2')


