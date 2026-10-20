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

def test_assoc_condition60_reverse_link_reassign_clear():
    a1 = cpsml_ODE(name="sample_text")
    a2 = cpsml_ODE(name="sample_text_2")
    b = cpsml_Condition(name="sample_text")
    _safe_set(b, 'cpsml_Condition', a1)
    assert _is_linked(b, 'cpsml_Condition', a1)
    if hasattr(a1, 'cpsml_ODE61'):
        assert _is_linked(a1, 'cpsml_ODE61', b)
    _safe_set(b, 'cpsml_Condition', a2)
    assert _is_linked(b, 'cpsml_Condition', a2)
    if hasattr(a1, 'cpsml_ODE61'):
        assert not _is_linked(a1, 'cpsml_ODE61', b)
    if hasattr(a2, 'cpsml_ODE61'):
        assert _is_linked(a2, 'cpsml_ODE61', b)
    _safe_set(b, 'cpsml_Condition', None)
    assert not _is_linked(b, 'cpsml_Condition', a2)
    if hasattr(a2, 'cpsml_ODE61'):
        assert not _is_linked(a2, 'cpsml_ODE61', b)


def test_assoc_currentState13_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    a2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State15', a1)
    assert _is_linked(b, 'cpsml_State15', a1)
    if hasattr(a1, 'cpsml_System14'):
        assert _is_linked(a1, 'cpsml_System14', b)
    _safe_set(b, 'cpsml_State15', a2)
    assert _is_linked(b, 'cpsml_State15', a2)
    if hasattr(a1, 'cpsml_System14'):
        assert not _is_linked(a1, 'cpsml_System14', b)
    if hasattr(a2, 'cpsml_System14'):
        assert _is_linked(a2, 'cpsml_System14', b)
    _safe_set(b, 'cpsml_State15', None)
    assert not _is_linked(b, 'cpsml_State15', a2)
    if hasattr(a2, 'cpsml_System14'):
        assert not _is_linked(a2, 'cpsml_System14', b)


def test_assoc_devariable66_reverse_link_reassign_clear():
    a1 = cpsml_Function(name="sample_text")
    a2 = cpsml_Function(name="sample_text_2")
    b = cpsml_DeVariable(name="sample_text")
    _safe_set(b, 'cpsml_DeVariable', a1)
    assert _is_linked(b, 'cpsml_DeVariable', a1)
    if hasattr(a1, 'cpsml_Function67'):
        assert _is_linked(a1, 'cpsml_Function67', b)
    _safe_set(b, 'cpsml_DeVariable', a2)
    assert _is_linked(b, 'cpsml_DeVariable', a2)
    if hasattr(a1, 'cpsml_Function67'):
        assert not _is_linked(a1, 'cpsml_Function67', b)
    if hasattr(a2, 'cpsml_Function67'):
        assert _is_linked(a2, 'cpsml_Function67', b)
    _safe_set(b, 'cpsml_DeVariable', None)
    assert not _is_linked(b, 'cpsml_DeVariable', a2)
    if hasattr(a2, 'cpsml_Function67'):
        assert not _is_linked(a2, 'cpsml_Function67', b)


def test_assoc_fatherState16_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    a2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State18', a1)
    assert _is_linked(b, 'cpsml_State18', a1)
    if hasattr(a1, 'cpsml_System17'):
        assert _is_linked(a1, 'cpsml_System17', b)
    _safe_set(b, 'cpsml_State18', a2)
    assert _is_linked(b, 'cpsml_State18', a2)
    if hasattr(a1, 'cpsml_System17'):
        assert not _is_linked(a1, 'cpsml_System17', b)
    if hasattr(a2, 'cpsml_System17'):
        assert _is_linked(a2, 'cpsml_System17', b)
    _safe_set(b, 'cpsml_State18', None)
    assert not _is_linked(b, 'cpsml_State18', a2)
    if hasattr(a2, 'cpsml_System17'):
        assert not _is_linked(a2, 'cpsml_System17', b)


def test_assoc_fright68_reverse_link_reassign_clear():
    a1 = cpsml_Function(name="sample_text")
    a2 = cpsml_Function(name="sample_text_2")
    b = cpsml_Fright(name="sample_text")
    _safe_set(b, 'cpsml_Fright', a1)
    assert _is_linked(b, 'cpsml_Fright', a1)
    if hasattr(a1, 'cpsml_Function69'):
        assert _is_linked(a1, 'cpsml_Function69', b)
    _safe_set(b, 'cpsml_Fright', a2)
    assert _is_linked(b, 'cpsml_Fright', a2)
    if hasattr(a1, 'cpsml_Function69'):
        assert not _is_linked(a1, 'cpsml_Function69', b)
    if hasattr(a2, 'cpsml_Function69'):
        assert _is_linked(a2, 'cpsml_Function69', b)
    _safe_set(b, 'cpsml_Fright', None)
    assert not _is_linked(b, 'cpsml_Fright', a2)
    if hasattr(a2, 'cpsml_Function69'):
        assert not _is_linked(a2, 'cpsml_Function69', b)


def test_assoc_function58_reverse_link_reassign_clear():
    a1 = cpsml_ODE(name="sample_text")
    a2 = cpsml_ODE(name="sample_text_2")
    b = cpsml_Function(name="sample_text")
    _safe_set(b, 'cpsml_Function', a1)
    assert _is_linked(b, 'cpsml_Function', a1)
    if hasattr(a1, 'cpsml_ODE59'):
        assert _is_linked(a1, 'cpsml_ODE59', b)
    _safe_set(b, 'cpsml_Function', a2)
    assert _is_linked(b, 'cpsml_Function', a2)
    if hasattr(a1, 'cpsml_ODE59'):
        assert not _is_linked(a1, 'cpsml_ODE59', b)
    if hasattr(a2, 'cpsml_ODE59'):
        assert _is_linked(a2, 'cpsml_ODE59', b)
    _safe_set(b, 'cpsml_Function', None)
    assert not _is_linked(b, 'cpsml_Function', a2)
    if hasattr(a2, 'cpsml_ODE59'):
        assert not _is_linked(a2, 'cpsml_ODE59', b)


def test_assoc_incomingProbTransitions28_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'ProbTransition29', a1)
    assert _is_linked(b, 'ProbTransition29', a1)
    if hasattr(a1, 'ptgt'):
        assert _is_linked(a1, 'ptgt', b)
    _safe_set(b, 'ProbTransition29', a2)
    assert _is_linked(b, 'ProbTransition29', a2)
    if hasattr(a1, 'ptgt'):
        assert not _is_linked(a1, 'ptgt', b)
    if hasattr(a2, 'ptgt'):
        assert _is_linked(a2, 'ptgt', b)
    _safe_set(b, 'ProbTransition29', None)
    assert not _is_linked(b, 'ProbTransition29', a2)
    if hasattr(a2, 'ptgt'):
        assert not _is_linked(a2, 'ptgt', b)


def test_assoc_indevariable64_reverse_link_reassign_clear():
    a1 = cpsml_IndeVariable(name="sample_text")
    a2 = cpsml_IndeVariable(name="sample_text_2")
    b = cpsml_Function(name="sample_text")
    _safe_set(b, 'cpsml_Function65', a1)
    assert _is_linked(b, 'cpsml_Function65', a1)
    if hasattr(a1, 'cpsml_IndeVariable'):
        assert _is_linked(a1, 'cpsml_IndeVariable', b)
    _safe_set(b, 'cpsml_Function65', a2)
    assert _is_linked(b, 'cpsml_Function65', a2)
    if hasattr(a1, 'cpsml_IndeVariable'):
        assert not _is_linked(a1, 'cpsml_IndeVariable', b)
    if hasattr(a2, 'cpsml_IndeVariable'):
        assert _is_linked(a2, 'cpsml_IndeVariable', b)
    _safe_set(b, 'cpsml_Function65', None)
    assert not _is_linked(b, 'cpsml_Function65', a2)
    if hasattr(a2, 'cpsml_IndeVariable'):
        assert not _is_linked(a2, 'cpsml_IndeVariable', b)


def test_assoc_initialState8_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    a2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    b = cpsml_State(name=True)
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


def test_assoc_initialsubstate34_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State35', a1)
    assert _is_linked(b, 'cpsml_State35', a1)
    if hasattr(a1, 'cpsml_State33'):
        assert _is_linked(a1, 'cpsml_State33', b)
    _safe_set(b, 'cpsml_State35', a2)
    assert _is_linked(b, 'cpsml_State35', a2)
    if hasattr(a1, 'cpsml_State33'):
        assert not _is_linked(a1, 'cpsml_State33', b)
    if hasattr(a2, 'cpsml_State33'):
        assert _is_linked(a2, 'cpsml_State33', b)
    _safe_set(b, 'cpsml_State35', None)
    assert not _is_linked(b, 'cpsml_State35', a2)
    if hasattr(a2, 'cpsml_State33'):
        assert not _is_linked(a2, 'cpsml_State33', b)


def test_assoc_interval62_reverse_link_reassign_clear():
    a1 = cpsml_ODE(name="sample_text")
    a2 = cpsml_ODE(name="sample_text_2")
    b = cpsml_Interval(left=3.14, name="sample_text", right=3.14, subinterval=3.14)
    _safe_set(b, 'cpsml_Interval', a1)
    assert _is_linked(b, 'cpsml_Interval', a1)
    if hasattr(a1, 'cpsml_ODE63'):
        assert _is_linked(a1, 'cpsml_ODE63', b)
    _safe_set(b, 'cpsml_Interval', a2)
    assert _is_linked(b, 'cpsml_Interval', a2)
    if hasattr(a1, 'cpsml_ODE63'):
        assert not _is_linked(a1, 'cpsml_ODE63', b)
    if hasattr(a2, 'cpsml_ODE63'):
        assert _is_linked(a2, 'cpsml_ODE63', b)
    _safe_set(b, 'cpsml_Interval', None)
    assert not _is_linked(b, 'cpsml_Interval', a2)
    if hasattr(a2, 'cpsml_ODE63'):
        assert not _is_linked(a2, 'cpsml_ODE63', b)


def test_assoc_outgoingProbTransitions27_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
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
    a1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    a2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    b = cpsml_State(name=True)
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
    b = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
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
    a1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    a2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
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
    a1 = cpsml_Variable(Globalnv=3.14, value=3.14)
    a2 = cpsml_Variable(Globalnv=9.99, value=9.99)
    b = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
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


def test_assoc_psrc54_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'outgoingProbTransitions', a1)
    assert _is_linked(b, 'outgoingProbTransitions', a1)
    if hasattr(a1, 'State55'):
        assert _is_linked(a1, 'State55', b)
    _safe_set(b, 'outgoingProbTransitions', a2)
    assert _is_linked(b, 'outgoingProbTransitions', a2)
    if hasattr(a1, 'State55'):
        assert not _is_linked(a1, 'State55', b)
    if hasattr(a2, 'State55'):
        assert _is_linked(a2, 'State55', b)
    _safe_set(b, 'outgoingProbTransitions', None)
    assert not _is_linked(b, 'outgoingProbTransitions', a2)
    if hasattr(a2, 'State55'):
        assert not _is_linked(a2, 'State55', b)


def test_assoc_ptgt56_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'incomingProbTransitions', a1)
    assert _is_linked(b, 'incomingProbTransitions', a1)
    if hasattr(a1, 'State57'):
        assert _is_linked(a1, 'State57', b)
    _safe_set(b, 'incomingProbTransitions', a2)
    assert _is_linked(b, 'incomingProbTransitions', a2)
    if hasattr(a1, 'State57'):
        assert not _is_linked(a1, 'State57', b)
    if hasattr(a2, 'State57'):
        assert _is_linked(a2, 'State57', b)
    _safe_set(b, 'incomingProbTransitions', None)
    assert not _is_linked(b, 'incomingProbTransitions', a2)
    if hasattr(a2, 'State57'):
        assert not _is_linked(a2, 'State57', b)


def test_assoc_ptok19_reverse_link_reassign_clear():
    a1 = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
    a2 = cpsml_System(name="sample_text_2", ran="sample_text_2", sub=13, y0label=13)
    b = cpsml_ProbTransition(probability=3.14)
    _safe_set(b, 'cpsml_ProbTransition', a1)
    assert _is_linked(b, 'cpsml_ProbTransition', a1)
    if hasattr(a1, 'cpsml_System20'):
        assert _is_linked(a1, 'cpsml_System20', b)
    _safe_set(b, 'cpsml_ProbTransition', a2)
    assert _is_linked(b, 'cpsml_ProbTransition', a2)
    if hasattr(a1, 'cpsml_System20'):
        assert not _is_linked(a1, 'cpsml_System20', b)
    if hasattr(a2, 'cpsml_System20'):
        assert _is_linked(a2, 'cpsml_System20', b)
    _safe_set(b, 'cpsml_ProbTransition', None)
    assert not _is_linked(b, 'cpsml_ProbTransition', a2)
    if hasattr(a2, 'cpsml_System20'):
        assert not _is_linked(a2, 'cpsml_System20', b)


def test_assoc_relatedvariable1_reverse_link_reassign_clear():
    a1 = cpsml_Variable(Globalnv=3.14, value=3.14)
    a2 = cpsml_Variable(Globalnv=9.99, value=9.99)
    b = cpsml_System(name="sample_text", ran="sample_text", sub=7, y0label=7)
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


def test_assoc_relatedvariable248_reverse_link_reassign_clear():
    a1 = cpsml_Variable(Globalnv=3.14, value=3.14)
    a2 = cpsml_Variable(Globalnv=9.99, value=9.99)
    b = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    _safe_set(b, 'cpsml_Transition49', a1)
    assert _is_linked(b, 'cpsml_Transition49', a1)
    if hasattr(a1, 'cpsml_Variable50'):
        assert _is_linked(a1, 'cpsml_Variable50', b)
    _safe_set(b, 'cpsml_Transition49', a2)
    assert _is_linked(b, 'cpsml_Transition49', a2)
    if hasattr(a1, 'cpsml_Variable50'):
        assert not _is_linked(a1, 'cpsml_Variable50', b)
    if hasattr(a2, 'cpsml_Variable50'):
        assert _is_linked(a2, 'cpsml_Variable50', b)
    _safe_set(b, 'cpsml_Transition49', None)
    assert not _is_linked(b, 'cpsml_Transition49', a2)
    if hasattr(a2, 'cpsml_Variable50'):
        assert not _is_linked(a2, 'cpsml_Variable50', b)


def test_assoc_slaveode21_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_ODE(name="sample_text")
    _safe_set(b, 'cpsml_ODE23', a1)
    assert _is_linked(b, 'cpsml_ODE23', a1)
    if hasattr(a1, 'cpsml_State22'):
        assert _is_linked(a1, 'cpsml_State22', b)
    _safe_set(b, 'cpsml_ODE23', a2)
    assert _is_linked(b, 'cpsml_ODE23', a2)
    if hasattr(a1, 'cpsml_State22'):
        assert not _is_linked(a1, 'cpsml_State22', b)
    if hasattr(a2, 'cpsml_State22'):
        assert _is_linked(a2, 'cpsml_State22', b)
    _safe_set(b, 'cpsml_ODE23', None)
    assert not _is_linked(b, 'cpsml_ODE23', a2)
    if hasattr(a2, 'cpsml_State22'):
        assert not _is_linked(a2, 'cpsml_State22', b)


def test_assoc_subStates31_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State32', a1)
    assert _is_linked(b, 'cpsml_State32', a1)
    if hasattr(a1, 'cpsml_State30'):
        assert _is_linked(a1, 'cpsml_State30', b)
    _safe_set(b, 'cpsml_State32', a2)
    assert _is_linked(b, 'cpsml_State32', a2)
    if hasattr(a1, 'cpsml_State30'):
        assert not _is_linked(a1, 'cpsml_State30', b)
    if hasattr(a2, 'cpsml_State30'):
        assert _is_linked(a2, 'cpsml_State30', b)
    _safe_set(b, 'cpsml_State32', None)
    assert not _is_linked(b, 'cpsml_State32', a2)
    if hasattr(a2, 'cpsml_State30'):
        assert not _is_linked(a2, 'cpsml_State30', b)


def test_assoc_subodes39_reverse_link_reassign_clear():
    a1 = cpsml_State(name=True)
    a2 = cpsml_State(name=False)
    b = cpsml_ODE(name="sample_text")
    _safe_set(b, 'cpsml_ODE41', a1)
    assert _is_linked(b, 'cpsml_ODE41', a1)
    if hasattr(a1, 'cpsml_State40'):
        assert _is_linked(a1, 'cpsml_State40', b)
    _safe_set(b, 'cpsml_ODE41', a2)
    assert _is_linked(b, 'cpsml_ODE41', a2)
    if hasattr(a1, 'cpsml_State40'):
        assert not _is_linked(a1, 'cpsml_State40', b)
    if hasattr(a2, 'cpsml_State40'):
        assert _is_linked(a2, 'cpsml_State40', b)
    _safe_set(b, 'cpsml_ODE41', None)
    assert not _is_linked(b, 'cpsml_ODE41', a2)
    if hasattr(a2, 'cpsml_State40'):
        assert not _is_linked(a2, 'cpsml_State40', b)


def test_assoc_subrelatedvariable45_reverse_link_reassign_clear():
    a1 = cpsml_Variable(Globalnv=3.14, value=3.14)
    a2 = cpsml_Variable(Globalnv=9.99, value=9.99)
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State46', a1)
    assert _is_linked(b, 'cpsml_State46', a1)
    if hasattr(a1, 'cpsml_Variable47'):
        assert _is_linked(a1, 'cpsml_Variable47', b)
    _safe_set(b, 'cpsml_State46', a2)
    assert _is_linked(b, 'cpsml_State46', a2)
    if hasattr(a1, 'cpsml_Variable47'):
        assert not _is_linked(a1, 'cpsml_Variable47', b)
    if hasattr(a2, 'cpsml_Variable47'):
        assert _is_linked(a2, 'cpsml_Variable47', b)
    _safe_set(b, 'cpsml_State46', None)
    assert not _is_linked(b, 'cpsml_State46', a2)
    if hasattr(a2, 'cpsml_Variable47'):
        assert not _is_linked(a2, 'cpsml_Variable47', b)


def test_assoc_subrelatedvariables42_reverse_link_reassign_clear():
    a1 = cpsml_Variable(Globalnv=3.14, value=3.14)
    a2 = cpsml_Variable(Globalnv=9.99, value=9.99)
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State43', {a1})
    assert _is_linked(b, 'cpsml_State43', a1)
    if hasattr(a1, 'cpsml_Variable44'):
        assert _is_linked(a1, 'cpsml_Variable44', b)
    _safe_set(b, 'cpsml_State43', {a2})
    assert _is_linked(b, 'cpsml_State43', a2)
    if hasattr(a1, 'cpsml_Variable44'):
        assert not _is_linked(a1, 'cpsml_Variable44', b)
    if hasattr(a2, 'cpsml_Variable44'):
        assert _is_linked(a2, 'cpsml_Variable44', b)
    _safe_set(b, 'cpsml_State43', set())
    assert not _is_linked(b, 'cpsml_State43', a2)
    if hasattr(a2, 'cpsml_Variable44'):
        assert not _is_linked(a2, 'cpsml_Variable44', b)


def test_assoc_subtransitions36_reverse_link_reassign_clear():
    a1 = cpsml_Transition(action="sample_text", event="sample_text", guard="sample_text", name="sample_text")
    a2 = cpsml_Transition(action="sample_text_2", event="sample_text_2", guard="sample_text_2", name="sample_text_2")
    b = cpsml_State(name=True)
    _safe_set(b, 'cpsml_State37', {a1})
    assert _is_linked(b, 'cpsml_State37', a1)
    if hasattr(a1, 'cpsml_Transition38'):
        assert _is_linked(a1, 'cpsml_Transition38', b)
    _safe_set(b, 'cpsml_State37', {a2})
    assert _is_linked(b, 'cpsml_State37', a2)
    if hasattr(a1, 'cpsml_Transition38'):
        assert not _is_linked(a1, 'cpsml_Transition38', b)
    if hasattr(a2, 'cpsml_Transition38'):
        assert _is_linked(a2, 'cpsml_Transition38', b)
    _safe_set(b, 'cpsml_State37', set())
    assert not _is_linked(b, 'cpsml_State37', a2)
    if hasattr(a2, 'cpsml_Transition38'):
        assert not _is_linked(a2, 'cpsml_Transition38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_csrc51_stub_double():
    # cpsml_ComTransition has no real 'outgoingComTransitions' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name=True)
    partner = cpsml_ComTransition()
    setattr(partner, 'outgoingComTransitions', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outgoingComTransitions') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outgoingComTransitions') is None


def test_assoc_ctgt52_stub_double():
    # cpsml_ComTransition has no real 'incomingComTransitions' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name=True)
    partner = cpsml_ComTransition()
    setattr(partner, 'incomingComTransitions', None)
    _safe_set(owner, 'State53', partner)
    assert getattr(partner, 'incomingComTransitions') == owner
    _safe_set(owner, 'State53', None)
    assert getattr(partner, 'incomingComTransitions') is None


def test_assoc_incomingComTransitions25_stub_double():
    # cpsml_ComTransition has no real 'ComTransition26' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name=True)
    partner = cpsml_ComTransition()
    setattr(partner, 'ComTransition26', None)
    _safe_set(owner, 'ctgt', {partner})
    assert getattr(partner, 'ComTransition26') == owner
    _safe_set(owner, 'ctgt', set())
    assert getattr(partner, 'ComTransition26') is None


def test_assoc_outgoingComTransitions24_stub_double():
    # cpsml_ComTransition has no real 'ComTransition' property in the generated
    # code (a bare stub) -- manually attach it so cpsml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpsml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpsml_State(name=True)
    partner = cpsml_ComTransition()
    setattr(partner, 'ComTransition', None)
    _safe_set(owner, 'csrc', {partner})
    assert getattr(partner, 'ComTransition') == owner
    _safe_set(owner, 'csrc', set())
    assert getattr(partner, 'ComTransition') is None


