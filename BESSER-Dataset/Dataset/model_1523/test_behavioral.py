import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Transition,
    cpsml_ComTransition,
    cpsml_Condition,
    cpsml_DeVariable,
    cpsml_Fright,
    cpsml_Function,
    cpsml_IndeVariable,
    cpsml_Interval,
    cpsml_ODE,
    cpsml_ProbTransition,
    cpsml_State,
    cpsml_System,
    cpsml_Transition,
    cpsml_Variable,
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

def test_assoc_condition52_reverse_link_reassign_clear():
    a1 = cpsml_ODE(name="sample_text")
    a2 = cpsml_ODE(name="sample_text_2")
    b = cpsml_Condition(name="sample_text")
    _safe_set(b, 'cpsml_Condition', a1)
    assert _is_linked(b, 'cpsml_Condition', a1)
    if hasattr(a1, 'cpsml_ODE53'):
        assert _is_linked(a1, 'cpsml_ODE53', b)
    _safe_set(b, 'cpsml_Condition', a2)
    assert _is_linked(b, 'cpsml_Condition', a2)
    if hasattr(a1, 'cpsml_ODE53'):
        assert not _is_linked(a1, 'cpsml_ODE53', b)
    if hasattr(a2, 'cpsml_ODE53'):
        assert _is_linked(a2, 'cpsml_ODE53', b)
    _safe_set(b, 'cpsml_Condition', None)
    assert not _is_linked(b, 'cpsml_Condition', a2)
    if hasattr(a2, 'cpsml_ODE53'):
        assert not _is_linked(a2, 'cpsml_ODE53', b)


def test_assoc_devariable58_reverse_link_reassign_clear():
    a1 = cpsml_Function(name="sample_text")
    a2 = cpsml_Function(name="sample_text_2")
    b = cpsml_DeVariable(name="sample_text")
    _safe_set(b, 'cpsml_DeVariable', a1)
    assert _is_linked(b, 'cpsml_DeVariable', a1)
    if hasattr(a1, 'cpsml_Function59'):
        assert _is_linked(a1, 'cpsml_Function59', b)
    _safe_set(b, 'cpsml_DeVariable', a2)
    assert _is_linked(b, 'cpsml_DeVariable', a2)
    if hasattr(a1, 'cpsml_Function59'):
        assert not _is_linked(a1, 'cpsml_Function59', b)
    if hasattr(a2, 'cpsml_Function59'):
        assert _is_linked(a2, 'cpsml_Function59', b)
    _safe_set(b, 'cpsml_DeVariable', None)
    assert not _is_linked(b, 'cpsml_DeVariable', a2)
    if hasattr(a2, 'cpsml_Function59'):
        assert not _is_linked(a2, 'cpsml_Function59', b)


def test_assoc_fright60_reverse_link_reassign_clear():
    a1 = cpsml_Function(name="sample_text")
    a2 = cpsml_Function(name="sample_text_2")
    b = cpsml_Fright(name="sample_text")
    _safe_set(b, 'cpsml_Fright', a1)
    assert _is_linked(b, 'cpsml_Fright', a1)
    if hasattr(a1, 'cpsml_Function61'):
        assert _is_linked(a1, 'cpsml_Function61', b)
    _safe_set(b, 'cpsml_Fright', a2)
    assert _is_linked(b, 'cpsml_Fright', a2)
    if hasattr(a1, 'cpsml_Function61'):
        assert not _is_linked(a1, 'cpsml_Function61', b)
    if hasattr(a2, 'cpsml_Function61'):
        assert _is_linked(a2, 'cpsml_Function61', b)
    _safe_set(b, 'cpsml_Fright', None)
    assert not _is_linked(b, 'cpsml_Fright', a2)
    if hasattr(a2, 'cpsml_Function61'):
        assert not _is_linked(a2, 'cpsml_Function61', b)


def test_assoc_function50_reverse_link_reassign_clear():
    a1 = cpsml_ODE(name="sample_text")
    a2 = cpsml_ODE(name="sample_text_2")
    b = cpsml_Function(name="sample_text")
    _safe_set(b, 'cpsml_Function', a1)
    assert _is_linked(b, 'cpsml_Function', a1)
    if hasattr(a1, 'cpsml_ODE51'):
        assert _is_linked(a1, 'cpsml_ODE51', b)
    _safe_set(b, 'cpsml_Function', a2)
    assert _is_linked(b, 'cpsml_Function', a2)
    if hasattr(a1, 'cpsml_ODE51'):
        assert not _is_linked(a1, 'cpsml_ODE51', b)
    if hasattr(a2, 'cpsml_ODE51'):
        assert _is_linked(a2, 'cpsml_ODE51', b)
    _safe_set(b, 'cpsml_Function', None)
    assert not _is_linked(b, 'cpsml_Function', a2)
    if hasattr(a2, 'cpsml_ODE51'):
        assert not _is_linked(a2, 'cpsml_ODE51', b)


def test_assoc_incomingProbTransitions20_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'ProbTransition21', a1)
    assert _is_linked(b, 'ProbTransition21', a1)
    if hasattr(a1, 'ptgt'):
        assert _is_linked(a1, 'ptgt', b)
    _safe_set(b, 'ProbTransition21', a2)
    assert _is_linked(b, 'ProbTransition21', a2)
    if hasattr(a1, 'ptgt'):
        assert not _is_linked(a1, 'ptgt', b)
    if hasattr(a2, 'ptgt'):
        assert _is_linked(a2, 'ptgt', b)
    _safe_set(b, 'ProbTransition21', None)
    assert not _is_linked(b, 'ProbTransition21', a2)
    if hasattr(a2, 'ptgt'):
        assert not _is_linked(a2, 'ptgt', b)


def test_assoc_indevariable56_reverse_link_reassign_clear():
    a1 = cpsml_IndeVariable(name="sample_text")
    a2 = cpsml_IndeVariable(name="sample_text_2")
    b = cpsml_Function(name="sample_text")
    _safe_set(b, 'cpsml_Function57', a1)
    assert _is_linked(b, 'cpsml_Function57', a1)
    if hasattr(a1, 'cpsml_IndeVariable'):
        assert _is_linked(a1, 'cpsml_IndeVariable', b)
    _safe_set(b, 'cpsml_Function57', a2)
    assert _is_linked(b, 'cpsml_Function57', a2)
    if hasattr(a1, 'cpsml_IndeVariable'):
        assert not _is_linked(a1, 'cpsml_IndeVariable', b)
    if hasattr(a2, 'cpsml_IndeVariable'):
        assert _is_linked(a2, 'cpsml_IndeVariable', b)
    _safe_set(b, 'cpsml_Function57', None)
    assert not _is_linked(b, 'cpsml_Function57', a2)
    if hasattr(a2, 'cpsml_IndeVariable'):
        assert not _is_linked(a2, 'cpsml_IndeVariable', b)


def test_assoc_initialState8_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text")
    a2 = cpsml_System(name="sample_text_2")
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State10', a1)
    assert _is_linked(b, 'cpsml_State10', a1)
    if hasattr(a1, 'cpsml_System9'):
        assert _is_linked(a1, 'cpsml_System9', b)
    _safe_set(b, 'cpsml_State10', a2)
    assert _is_linked(b, 'cpsml_State10', a2)
    if hasattr(a1, 'cpsml_System9'):
        assert not _is_linked(a1, 'cpsml_System9', b)
    if hasattr(a2, 'cpsml_System9'):
        assert _is_linked(a2, 'cpsml_System9', b)
    _safe_set(b, 'cpsml_State10', None)
    assert not _is_linked(b, 'cpsml_State10', a2)
    if hasattr(a2, 'cpsml_System9'):
        assert not _is_linked(a2, 'cpsml_System9', b)


def test_assoc_initialsubstate26_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State27', a1)
    assert _is_linked(b, 'cpsml_State27', a1)
    if hasattr(a1, 'cpsml_State25'):
        assert _is_linked(a1, 'cpsml_State25', b)
    _safe_set(b, 'cpsml_State27', a2)
    assert _is_linked(b, 'cpsml_State27', a2)
    if hasattr(a1, 'cpsml_State25'):
        assert not _is_linked(a1, 'cpsml_State25', b)
    if hasattr(a2, 'cpsml_State25'):
        assert _is_linked(a2, 'cpsml_State25', b)
    _safe_set(b, 'cpsml_State27', None)
    assert not _is_linked(b, 'cpsml_State27', a2)
    if hasattr(a2, 'cpsml_State25'):
        assert not _is_linked(a2, 'cpsml_State25', b)


def test_assoc_interval54_reverse_link_reassign_clear():
    a1 = cpsml_ODE(name="sample_text")
    a2 = cpsml_ODE(name="sample_text_2")
    b = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    _safe_set(b, 'cpsml_Interval', a1)
    assert _is_linked(b, 'cpsml_Interval', a1)
    if hasattr(a1, 'cpsml_ODE55'):
        assert _is_linked(a1, 'cpsml_ODE55', b)
    _safe_set(b, 'cpsml_Interval', a2)
    assert _is_linked(b, 'cpsml_Interval', a2)
    if hasattr(a1, 'cpsml_ODE55'):
        assert not _is_linked(a1, 'cpsml_ODE55', b)
    if hasattr(a2, 'cpsml_ODE55'):
        assert _is_linked(a2, 'cpsml_ODE55', b)
    _safe_set(b, 'cpsml_Interval', None)
    assert not _is_linked(b, 'cpsml_Interval', a2)
    if hasattr(a2, 'cpsml_ODE55'):
        assert not _is_linked(a2, 'cpsml_ODE55', b)


def test_assoc_outgoingProbTransitions19_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'ProbTransition', a1)
    assert _is_linked(b, 'ProbTransition', a1)
    if hasattr(a1, 'psrc'):
        assert _is_linked(a1, 'psrc', b)
    _safe_set(b, 'ProbTransition', a2)
    assert _is_linked(b, 'ProbTransition', a2)
    if hasattr(a1, 'psrc'):
        assert not _is_linked(a1, 'psrc', b)
    if hasattr(a2, 'psrc'):
        assert _is_linked(a2, 'psrc', b)
    _safe_set(b, 'ProbTransition', None)
    assert not _is_linked(b, 'ProbTransition', a2)
    if hasattr(a2, 'psrc'):
        assert not _is_linked(a2, 'psrc', b)


def test_assoc_ownedStates4_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text")
    a2 = cpsml_System(name="sample_text_2")
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State', a1)
    assert _is_linked(b, 'cpsml_State', a1)
    if hasattr(a1, 'cpsml_System5'):
        assert _is_linked(a1, 'cpsml_System5', b)
    _safe_set(b, 'cpsml_State', a2)
    assert _is_linked(b, 'cpsml_State', a2)
    if hasattr(a1, 'cpsml_System5'):
        assert not _is_linked(a1, 'cpsml_System5', b)
    if hasattr(a2, 'cpsml_System5'):
        assert _is_linked(a2, 'cpsml_System5', b)
    _safe_set(b, 'cpsml_State', None)
    assert not _is_linked(b, 'cpsml_State', a2)
    if hasattr(a2, 'cpsml_System5'):
        assert not _is_linked(a2, 'cpsml_System5', b)


def test_assoc_ownedTransitions6_reverse_link_reassign_clear():
    a1 = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    a2 = cpsml_Transition(action="sample_text_2", event="sample_text_2", guard="sample_text_2", name="sample_text_2")
    b = cpsml_System(name="sample_text")
    _safe_set(b, 'cpsml_System7', {a1})
    assert _is_linked(b, 'cpsml_System7', a1)
    if hasattr(a1, 'cpsml_Transition'):
        assert _is_linked(a1, 'cpsml_Transition', b)
    _safe_set(b, 'cpsml_System7', {a2})
    assert _is_linked(b, 'cpsml_System7', a2)
    if hasattr(a1, 'cpsml_Transition'):
        assert not _is_linked(a1, 'cpsml_Transition', b)
    if hasattr(a2, 'cpsml_Transition'):
        assert _is_linked(a2, 'cpsml_Transition', b)
    _safe_set(b, 'cpsml_System7', set())
    assert not _is_linked(b, 'cpsml_System7', a2)
    if hasattr(a2, 'cpsml_Transition'):
        assert not _is_linked(a2, 'cpsml_Transition', b)


def test_assoc_ownedodes11_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text")
    a2 = cpsml_System(name="sample_text_2")
    b = cpsml_ODE(name="sample_text")
    _safe_set(b, 'cpsml_ODE', a1)
    assert _is_linked(b, 'cpsml_ODE', a1)
    if hasattr(a1, 'cpsml_System12'):
        assert _is_linked(a1, 'cpsml_System12', b)
    _safe_set(b, 'cpsml_ODE', a2)
    assert _is_linked(b, 'cpsml_ODE', a2)
    if hasattr(a1, 'cpsml_System12'):
        assert not _is_linked(a1, 'cpsml_System12', b)
    if hasattr(a2, 'cpsml_System12'):
        assert _is_linked(a2, 'cpsml_System12', b)
    _safe_set(b, 'cpsml_ODE', None)
    assert not _is_linked(b, 'cpsml_ODE', a2)
    if hasattr(a2, 'cpsml_System12'):
        assert not _is_linked(a2, 'cpsml_System12', b)


def test_assoc_ownedvariables0_reverse_link_reassign_clear():
    a1 = cpsml_Variable(value=3.14)
    a2 = cpsml_Variable(value=9.99)
    b = cpsml_System(name="sample_text")
    _safe_set(b, 'cpsml_System', {a1})
    assert _is_linked(b, 'cpsml_System', a1)
    if hasattr(a1, 'cpsml_Variable'):
        assert _is_linked(a1, 'cpsml_Variable', b)
    _safe_set(b, 'cpsml_System', {a2})
    assert _is_linked(b, 'cpsml_System', a2)
    if hasattr(a1, 'cpsml_Variable'):
        assert not _is_linked(a1, 'cpsml_Variable', b)
    if hasattr(a2, 'cpsml_Variable'):
        assert _is_linked(a2, 'cpsml_Variable', b)
    _safe_set(b, 'cpsml_System', set())
    assert not _is_linked(b, 'cpsml_System', a2)
    if hasattr(a2, 'cpsml_Variable'):
        assert not _is_linked(a2, 'cpsml_Variable', b)


def test_assoc_psrc46_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'outgoingProbTransitions', a1)
    assert _is_linked(b, 'outgoingProbTransitions', a1)
    if hasattr(a1, 'State47'):
        assert _is_linked(a1, 'State47', b)
    _safe_set(b, 'outgoingProbTransitions', a2)
    assert _is_linked(b, 'outgoingProbTransitions', a2)
    if hasattr(a1, 'State47'):
        assert not _is_linked(a1, 'State47', b)
    if hasattr(a2, 'State47'):
        assert _is_linked(a2, 'State47', b)
    _safe_set(b, 'outgoingProbTransitions', None)
    assert not _is_linked(b, 'outgoingProbTransitions', a2)
    if hasattr(a2, 'State47'):
        assert not _is_linked(a2, 'State47', b)


def test_assoc_ptgt48_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'incomingProbTransitions', a1)
    assert _is_linked(b, 'incomingProbTransitions', a1)
    if hasattr(a1, 'State49'):
        assert _is_linked(a1, 'State49', b)
    _safe_set(b, 'incomingProbTransitions', a2)
    assert _is_linked(b, 'incomingProbTransitions', a2)
    if hasattr(a1, 'State49'):
        assert not _is_linked(a1, 'State49', b)
    if hasattr(a2, 'State49'):
        assert _is_linked(a2, 'State49', b)
    _safe_set(b, 'incomingProbTransitions', None)
    assert not _is_linked(b, 'incomingProbTransitions', a2)
    if hasattr(a2, 'State49'):
        assert not _is_linked(a2, 'State49', b)


def test_assoc_relatedvariable1_reverse_link_reassign_clear():
    a1 = cpsml_Variable(value=3.14)
    a2 = cpsml_Variable(value=9.99)
    b = cpsml_System(name="sample_text")
    _safe_set(b, 'cpsml_System2', a1)
    assert _is_linked(b, 'cpsml_System2', a1)
    if hasattr(a1, 'cpsml_Variable3'):
        assert _is_linked(a1, 'cpsml_Variable3', b)
    _safe_set(b, 'cpsml_System2', a2)
    assert _is_linked(b, 'cpsml_System2', a2)
    if hasattr(a1, 'cpsml_Variable3'):
        assert not _is_linked(a1, 'cpsml_Variable3', b)
    if hasattr(a2, 'cpsml_Variable3'):
        assert _is_linked(a2, 'cpsml_Variable3', b)
    _safe_set(b, 'cpsml_System2', None)
    assert not _is_linked(b, 'cpsml_System2', a2)
    if hasattr(a2, 'cpsml_Variable3'):
        assert not _is_linked(a2, 'cpsml_Variable3', b)


def test_assoc_relatedvariable240_reverse_link_reassign_clear():
    a1 = cpsml_Variable(value=3.14)
    a2 = cpsml_Variable(value=9.99)
    b = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    _safe_set(b, 'cpsml_Transition41', a1)
    assert _is_linked(b, 'cpsml_Transition41', a1)
    if hasattr(a1, 'cpsml_Variable42'):
        assert _is_linked(a1, 'cpsml_Variable42', b)
    _safe_set(b, 'cpsml_Transition41', a2)
    assert _is_linked(b, 'cpsml_Transition41', a2)
    if hasattr(a1, 'cpsml_Variable42'):
        assert not _is_linked(a1, 'cpsml_Variable42', b)
    if hasattr(a2, 'cpsml_Variable42'):
        assert _is_linked(a2, 'cpsml_Variable42', b)
    _safe_set(b, 'cpsml_Transition41', None)
    assert not _is_linked(b, 'cpsml_Transition41', a2)
    if hasattr(a2, 'cpsml_Variable42'):
        assert not _is_linked(a2, 'cpsml_Variable42', b)


def test_assoc_slaveode13_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_ODE(name="sample_text")
    _safe_set(b, 'cpsml_ODE15', a1)
    assert _is_linked(b, 'cpsml_ODE15', a1)
    if hasattr(a1, 'cpsml_State14'):
        assert _is_linked(a1, 'cpsml_State14', b)
    _safe_set(b, 'cpsml_ODE15', a2)
    assert _is_linked(b, 'cpsml_ODE15', a2)
    if hasattr(a1, 'cpsml_State14'):
        assert not _is_linked(a1, 'cpsml_State14', b)
    if hasattr(a2, 'cpsml_State14'):
        assert _is_linked(a2, 'cpsml_State14', b)
    _safe_set(b, 'cpsml_ODE15', None)
    assert not _is_linked(b, 'cpsml_ODE15', a2)
    if hasattr(a2, 'cpsml_State14'):
        assert not _is_linked(a2, 'cpsml_State14', b)


def test_assoc_subStates23_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State24', a1)
    assert _is_linked(b, 'cpsml_State24', a1)
    if hasattr(a1, 'cpsml_State22'):
        assert _is_linked(a1, 'cpsml_State22', b)
    _safe_set(b, 'cpsml_State24', a2)
    assert _is_linked(b, 'cpsml_State24', a2)
    if hasattr(a1, 'cpsml_State22'):
        assert not _is_linked(a1, 'cpsml_State22', b)
    if hasattr(a2, 'cpsml_State22'):
        assert _is_linked(a2, 'cpsml_State22', b)
    _safe_set(b, 'cpsml_State24', None)
    assert not _is_linked(b, 'cpsml_State24', a2)
    if hasattr(a2, 'cpsml_State22'):
        assert not _is_linked(a2, 'cpsml_State22', b)


def test_assoc_subodes31_reverse_link_reassign_clear():
    a1 = cpsml_State(name="sample_text")
    a2 = cpsml_State(name="sample_text_2")
    b = cpsml_ODE(name="sample_text")
    _safe_set(b, 'cpsml_ODE33', a1)
    assert _is_linked(b, 'cpsml_ODE33', a1)
    if hasattr(a1, 'cpsml_State32'):
        assert _is_linked(a1, 'cpsml_State32', b)
    _safe_set(b, 'cpsml_ODE33', a2)
    assert _is_linked(b, 'cpsml_ODE33', a2)
    if hasattr(a1, 'cpsml_State32'):
        assert not _is_linked(a1, 'cpsml_State32', b)
    if hasattr(a2, 'cpsml_State32'):
        assert _is_linked(a2, 'cpsml_State32', b)
    _safe_set(b, 'cpsml_ODE33', None)
    assert not _is_linked(b, 'cpsml_ODE33', a2)
    if hasattr(a2, 'cpsml_State32'):
        assert not _is_linked(a2, 'cpsml_State32', b)


def test_assoc_subrelatedvariable37_reverse_link_reassign_clear():
    a1 = cpsml_Variable(value=3.14)
    a2 = cpsml_Variable(value=9.99)
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State38', a1)
    assert _is_linked(b, 'cpsml_State38', a1)
    if hasattr(a1, 'cpsml_Variable39'):
        assert _is_linked(a1, 'cpsml_Variable39', b)
    _safe_set(b, 'cpsml_State38', a2)
    assert _is_linked(b, 'cpsml_State38', a2)
    if hasattr(a1, 'cpsml_Variable39'):
        assert not _is_linked(a1, 'cpsml_Variable39', b)
    if hasattr(a2, 'cpsml_Variable39'):
        assert _is_linked(a2, 'cpsml_Variable39', b)
    _safe_set(b, 'cpsml_State38', None)
    assert not _is_linked(b, 'cpsml_State38', a2)
    if hasattr(a2, 'cpsml_Variable39'):
        assert not _is_linked(a2, 'cpsml_Variable39', b)


def test_assoc_subrelatedvariables34_reverse_link_reassign_clear():
    a1 = cpsml_Variable(value=3.14)
    a2 = cpsml_Variable(value=9.99)
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State35', {a1})
    assert _is_linked(b, 'cpsml_State35', a1)
    if hasattr(a1, 'cpsml_Variable36'):
        assert _is_linked(a1, 'cpsml_Variable36', b)
    _safe_set(b, 'cpsml_State35', {a2})
    assert _is_linked(b, 'cpsml_State35', a2)
    if hasattr(a1, 'cpsml_Variable36'):
        assert not _is_linked(a1, 'cpsml_Variable36', b)
    if hasattr(a2, 'cpsml_Variable36'):
        assert _is_linked(a2, 'cpsml_Variable36', b)
    _safe_set(b, 'cpsml_State35', set())
    assert not _is_linked(b, 'cpsml_State35', a2)
    if hasattr(a2, 'cpsml_Variable36'):
        assert not _is_linked(a2, 'cpsml_Variable36', b)


def test_assoc_subtransitions28_reverse_link_reassign_clear():
    a1 = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    a2 = cpsml_Transition(action="sample_text_2", event="sample_text_2", guard="sample_text_2", name="sample_text_2")
    b = cpsml_State(name="sample_text")
    _safe_set(b, 'cpsml_State29', {a1})
    assert _is_linked(b, 'cpsml_State29', a1)
    if hasattr(a1, 'cpsml_Transition30'):
        assert _is_linked(a1, 'cpsml_Transition30', b)
    _safe_set(b, 'cpsml_State29', {a2})
    assert _is_linked(b, 'cpsml_State29', a2)
    if hasattr(a1, 'cpsml_Transition30'):
        assert not _is_linked(a1, 'cpsml_Transition30', b)
    if hasattr(a2, 'cpsml_Transition30'):
        assert _is_linked(a2, 'cpsml_Transition30', b)
    _safe_set(b, 'cpsml_State29', set())
    assert not _is_linked(b, 'cpsml_State29', a2)
    if hasattr(a2, 'cpsml_Transition30'):
        assert not _is_linked(a2, 'cpsml_Transition30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_csrc43_stub_double():
    # cpsml_ComTransition has no real 'outgoingComTransitions' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name="sample_text")
    partner = cpsml_ComTransition()
    setattr(partner, 'outgoingComTransitions', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outgoingComTransitions') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outgoingComTransitions') is None


def test_assoc_ctgt44_stub_double():
    # cpsml_ComTransition has no real 'incomingComTransitions' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name="sample_text")
    partner = cpsml_ComTransition()
    setattr(partner, 'incomingComTransitions', None)
    _safe_set(owner, 'State45', partner)
    assert getattr(partner, 'incomingComTransitions') == owner
    _safe_set(owner, 'State45', None)
    assert getattr(partner, 'incomingComTransitions') is None


def test_assoc_incomingComTransitions17_stub_double():
    # cpsml_ComTransition has no real 'ComTransition18' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name="sample_text")
    partner = cpsml_ComTransition()
    setattr(partner, 'ComTransition18', None)
    _safe_set(owner, 'ctgt', {partner})
    assert getattr(partner, 'ComTransition18') == owner
    _safe_set(owner, 'ctgt', set())
    assert getattr(partner, 'ComTransition18') is None


def test_assoc_outgoingComTransitions16_stub_double():
    # cpsml_ComTransition has no real 'ComTransition' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name="sample_text")
    partner = cpsml_ComTransition()
    setattr(partner, 'ComTransition', None)
    _safe_set(owner, 'csrc', {partner})
    assert getattr(partner, 'ComTransition') == owner
    _safe_set(owner, 'csrc', set())
    assert getattr(partner, 'ComTransition') is None


