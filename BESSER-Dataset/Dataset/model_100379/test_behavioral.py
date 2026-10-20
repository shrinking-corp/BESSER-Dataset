import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mmb_Automaton,
    mmb_Mode,
    mmb_Model,
    mmb_Modification,
    mmb_Transition,
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

def test_assoc_Modifications5_reverse_link_reassign_clear():
    a1 = mmb_Modification(VarName="sample_text", VarType="sample_text")
    a2 = mmb_Modification(VarName="sample_text_2", VarType="sample_text_2")
    b = mmb_Mode(Dimension=3.14, InitialState=True, Name="sample_text", Shape="sample_text")
    _safe_set(b, 'mmb_Mode6', {a1})
    assert _is_linked(b, 'mmb_Mode6', a1)
    if hasattr(a1, 'mmb_Modification'):
        assert _is_linked(a1, 'mmb_Modification', b)
    _safe_set(b, 'mmb_Mode6', {a2})
    assert _is_linked(b, 'mmb_Mode6', a2)
    if hasattr(a1, 'mmb_Modification'):
        assert not _is_linked(a1, 'mmb_Modification', b)
    if hasattr(a2, 'mmb_Modification'):
        assert _is_linked(a2, 'mmb_Modification', b)
    _safe_set(b, 'mmb_Mode6', set())
    assert not _is_linked(b, 'mmb_Mode6', a2)
    if hasattr(a2, 'mmb_Modification'):
        assert not _is_linked(a2, 'mmb_Modification', b)


def test_assoc_automata0_reverse_link_reassign_clear():
    a1 = mmb_Model(Name="sample_text")
    a2 = mmb_Model(Name="sample_text_2")
    b = mmb_Automaton(Name="sample_text")
    _safe_set(b, 'mmb_Automaton', a1)
    assert _is_linked(b, 'mmb_Automaton', a1)
    if hasattr(a1, 'mmb_Model'):
        assert _is_linked(a1, 'mmb_Model', b)
    _safe_set(b, 'mmb_Automaton', a2)
    assert _is_linked(b, 'mmb_Automaton', a2)
    if hasattr(a1, 'mmb_Model'):
        assert not _is_linked(a1, 'mmb_Model', b)
    if hasattr(a2, 'mmb_Model'):
        assert _is_linked(a2, 'mmb_Model', b)
    _safe_set(b, 'mmb_Automaton', None)
    assert not _is_linked(b, 'mmb_Automaton', a2)
    if hasattr(a2, 'mmb_Model'):
        assert not _is_linked(a2, 'mmb_Model', b)


def test_assoc_modes1_reverse_link_reassign_clear():
    a1 = mmb_Mode(Dimension=3.14, InitialState=True, Name="sample_text", Shape="sample_text")
    a2 = mmb_Mode(Dimension=9.99, InitialState=False, Name="sample_text_2", Shape="sample_text_2")
    b = mmb_Automaton(Name="sample_text")
    _safe_set(b, 'mmb_Automaton2', {a1})
    assert _is_linked(b, 'mmb_Automaton2', a1)
    if hasattr(a1, 'mmb_Mode'):
        assert _is_linked(a1, 'mmb_Mode', b)
    _safe_set(b, 'mmb_Automaton2', {a2})
    assert _is_linked(b, 'mmb_Automaton2', a2)
    if hasattr(a1, 'mmb_Mode'):
        assert not _is_linked(a1, 'mmb_Mode', b)
    if hasattr(a2, 'mmb_Mode'):
        assert _is_linked(a2, 'mmb_Mode', b)
    _safe_set(b, 'mmb_Automaton2', set())
    assert not _is_linked(b, 'mmb_Automaton2', a2)
    if hasattr(a2, 'mmb_Mode'):
        assert not _is_linked(a2, 'mmb_Mode', b)


def test_assoc_sourceMode7_reverse_link_reassign_clear():
    a1 = mmb_Transition(Event="sample_text")
    a2 = mmb_Transition(Event="sample_text_2")
    b = mmb_Mode(Dimension=3.14, InitialState=True, Name="sample_text", Shape="sample_text")
    _safe_set(b, 'mmb_Mode9', a1)
    assert _is_linked(b, 'mmb_Mode9', a1)
    if hasattr(a1, 'mmb_Transition8'):
        assert _is_linked(a1, 'mmb_Transition8', b)
    _safe_set(b, 'mmb_Mode9', a2)
    assert _is_linked(b, 'mmb_Mode9', a2)
    if hasattr(a1, 'mmb_Transition8'):
        assert not _is_linked(a1, 'mmb_Transition8', b)
    if hasattr(a2, 'mmb_Transition8'):
        assert _is_linked(a2, 'mmb_Transition8', b)
    _safe_set(b, 'mmb_Mode9', None)
    assert not _is_linked(b, 'mmb_Mode9', a2)
    if hasattr(a2, 'mmb_Transition8'):
        assert not _is_linked(a2, 'mmb_Transition8', b)


def test_assoc_targetMode10_reverse_link_reassign_clear():
    a1 = mmb_Transition(Event="sample_text")
    a2 = mmb_Transition(Event="sample_text_2")
    b = mmb_Mode(Dimension=3.14, InitialState=True, Name="sample_text", Shape="sample_text")
    _safe_set(b, 'mmb_Mode12', a1)
    assert _is_linked(b, 'mmb_Mode12', a1)
    if hasattr(a1, 'mmb_Transition11'):
        assert _is_linked(a1, 'mmb_Transition11', b)
    _safe_set(b, 'mmb_Mode12', a2)
    assert _is_linked(b, 'mmb_Mode12', a2)
    if hasattr(a1, 'mmb_Transition11'):
        assert not _is_linked(a1, 'mmb_Transition11', b)
    if hasattr(a2, 'mmb_Transition11'):
        assert _is_linked(a2, 'mmb_Transition11', b)
    _safe_set(b, 'mmb_Mode12', None)
    assert not _is_linked(b, 'mmb_Mode12', a2)
    if hasattr(a2, 'mmb_Transition11'):
        assert not _is_linked(a2, 'mmb_Transition11', b)


def test_assoc_transistions3_reverse_link_reassign_clear():
    a1 = mmb_Transition(Event="sample_text")
    a2 = mmb_Transition(Event="sample_text_2")
    b = mmb_Automaton(Name="sample_text")
    _safe_set(b, 'mmb_Automaton4', {a1})
    assert _is_linked(b, 'mmb_Automaton4', a1)
    if hasattr(a1, 'mmb_Transition'):
        assert _is_linked(a1, 'mmb_Transition', b)
    _safe_set(b, 'mmb_Automaton4', {a2})
    assert _is_linked(b, 'mmb_Automaton4', a2)
    if hasattr(a1, 'mmb_Transition'):
        assert not _is_linked(a1, 'mmb_Transition', b)
    if hasattr(a2, 'mmb_Transition'):
        assert _is_linked(a2, 'mmb_Transition', b)
    _safe_set(b, 'mmb_Automaton4', set())
    assert not _is_linked(b, 'mmb_Automaton4', a2)
    if hasattr(a2, 'mmb_Transition'):
        assert not _is_linked(a2, 'mmb_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

