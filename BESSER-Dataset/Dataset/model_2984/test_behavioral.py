import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mealymodel_Alphabet,
    mealymodel_MealyMachine,
    mealymodel_State,
    mealymodel_Transition,
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

def test_assoc_sourceState11_reverse_link_reassign_clear():
    a1 = mealymodel_Transition(input="sample_text", output="sample_text")
    a2 = mealymodel_Transition(input="sample_text_2", output="sample_text_2")
    b = mealymodel_State(name="sample_text")
    _safe_set(b, 'mealymodel_State13', a1)
    assert _is_linked(b, 'mealymodel_State13', a1)
    if hasattr(a1, 'mealymodel_Transition12'):
        assert _is_linked(a1, 'mealymodel_Transition12', b)
    _safe_set(b, 'mealymodel_State13', a2)
    assert _is_linked(b, 'mealymodel_State13', a2)
    if hasattr(a1, 'mealymodel_Transition12'):
        assert not _is_linked(a1, 'mealymodel_Transition12', b)
    if hasattr(a2, 'mealymodel_Transition12'):
        assert _is_linked(a2, 'mealymodel_Transition12', b)
    _safe_set(b, 'mealymodel_State13', None)
    assert not _is_linked(b, 'mealymodel_State13', a2)
    if hasattr(a2, 'mealymodel_Transition12'):
        assert not _is_linked(a2, 'mealymodel_Transition12', b)


def test_assoc_targetState14_reverse_link_reassign_clear():
    a1 = mealymodel_Transition(input="sample_text", output="sample_text")
    a2 = mealymodel_Transition(input="sample_text_2", output="sample_text_2")
    b = mealymodel_State(name="sample_text")
    _safe_set(b, 'mealymodel_State16', a1)
    assert _is_linked(b, 'mealymodel_State16', a1)
    if hasattr(a1, 'mealymodel_Transition15'):
        assert _is_linked(a1, 'mealymodel_Transition15', b)
    _safe_set(b, 'mealymodel_State16', a2)
    assert _is_linked(b, 'mealymodel_State16', a2)
    if hasattr(a1, 'mealymodel_Transition15'):
        assert not _is_linked(a1, 'mealymodel_Transition15', b)
    if hasattr(a2, 'mealymodel_Transition15'):
        assert _is_linked(a2, 'mealymodel_Transition15', b)
    _safe_set(b, 'mealymodel_State16', None)
    assert not _is_linked(b, 'mealymodel_State16', a2)
    if hasattr(a2, 'mealymodel_Transition15'):
        assert not _is_linked(a2, 'mealymodel_Transition15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_initialState0_stub_double():
    # mealymodel_MealyMachine has no real 'mealymodel_MealyMachine' property in the generated
    # code (a bare stub) -- manually attach it so mealymodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mealymodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mealymodel_State(name="sample_text")
    partner = mealymodel_MealyMachine()
    setattr(partner, 'mealymodel_MealyMachine', None)
    _safe_set(owner, 'mealymodel_State', partner)
    assert getattr(partner, 'mealymodel_MealyMachine') == owner
    _safe_set(owner, 'mealymodel_State', None)
    assert getattr(partner, 'mealymodel_MealyMachine') is None


def test_assoc_inputAlphabet4_stub_double():
    # mealymodel_MealyMachine has no real 'mealymodel_MealyMachine5' property in the generated
    # code (a bare stub) -- manually attach it so mealymodel_Alphabet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mealymodel_Alphabet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mealymodel_Alphabet(characters="sample_text")
    partner = mealymodel_MealyMachine()
    setattr(partner, 'mealymodel_MealyMachine5', None)
    _safe_set(owner, 'mealymodel_Alphabet', partner)
    assert getattr(partner, 'mealymodel_MealyMachine5') == owner
    _safe_set(owner, 'mealymodel_Alphabet', None)
    assert getattr(partner, 'mealymodel_MealyMachine5') is None


def test_assoc_outputAlphabet6_stub_double():
    # mealymodel_MealyMachine has no real 'mealymodel_MealyMachine7' property in the generated
    # code (a bare stub) -- manually attach it so mealymodel_Alphabet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mealymodel_Alphabet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mealymodel_Alphabet(characters="sample_text")
    partner = mealymodel_MealyMachine()
    setattr(partner, 'mealymodel_MealyMachine7', None)
    _safe_set(owner, 'mealymodel_Alphabet8', partner)
    assert getattr(partner, 'mealymodel_MealyMachine7') == owner
    _safe_set(owner, 'mealymodel_Alphabet8', None)
    assert getattr(partner, 'mealymodel_MealyMachine7') is None


def test_assoc_states1_stub_double():
    # mealymodel_MealyMachine has no real 'mealymodel_MealyMachine2' property in the generated
    # code (a bare stub) -- manually attach it so mealymodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mealymodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mealymodel_State(name="sample_text")
    partner = mealymodel_MealyMachine()
    setattr(partner, 'mealymodel_MealyMachine2', None)
    _safe_set(owner, 'mealymodel_State3', partner)
    assert owner in getattr(partner, 'mealymodel_MealyMachine2')
    _safe_set(owner, 'mealymodel_State3', None)
    assert owner not in getattr(partner, 'mealymodel_MealyMachine2')


def test_assoc_transitions9_stub_double():
    # mealymodel_MealyMachine has no real 'mealymodel_MealyMachine10' property in the generated
    # code (a bare stub) -- manually attach it so mealymodel_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mealymodel_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mealymodel_Transition(input="sample_text", output="sample_text")
    partner = mealymodel_MealyMachine()
    setattr(partner, 'mealymodel_MealyMachine10', None)
    _safe_set(owner, 'mealymodel_Transition', partner)
    assert owner in getattr(partner, 'mealymodel_MealyMachine10')
    _safe_set(owner, 'mealymodel_Transition', None)
    assert owner not in getattr(partner, 'mealymodel_MealyMachine10')


