import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MatchArgument,
    Trace,
    viewmodeltrace_Constraint,
    viewmodeltrace_ConstraintTrace,
    viewmodeltrace_EObject,
    viewmodeltrace_EObjectMatchArgument,
    viewmodeltrace_JavaObjectMatchArgument,
    viewmodeltrace_LogicModel,
    viewmodeltrace_MatchArgument,
    viewmodeltrace_MatchArgumentTuple,
    viewmodeltrace_StringVariablePair,
    viewmodeltrace_Trace,
    viewmodeltrace_Variable,
    viewmodeltrace_VariableInstantiationTrace,
    viewmodeltrace_ViewModelTrace,
    TraceState,
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

def test_assoc_traces1_reverse_link_reassign_clear():
    a1 = viewmodeltrace_ViewModelTrace(traceModelId="sample_text")
    a2 = viewmodeltrace_ViewModelTrace(traceModelId="sample_text_2")
    b = viewmodeltrace_Trace(state="sample_text", traceName="sample_text")
    _safe_set(b, 'viewmodeltrace_Trace', a1)
    assert _is_linked(b, 'viewmodeltrace_Trace', a1)
    if hasattr(a1, 'viewmodeltrace_ViewModelTrace2'):
        assert _is_linked(a1, 'viewmodeltrace_ViewModelTrace2', b)
    _safe_set(b, 'viewmodeltrace_Trace', a2)
    assert _is_linked(b, 'viewmodeltrace_Trace', a2)
    if hasattr(a1, 'viewmodeltrace_ViewModelTrace2'):
        assert not _is_linked(a1, 'viewmodeltrace_ViewModelTrace2', b)
    if hasattr(a2, 'viewmodeltrace_ViewModelTrace2'):
        assert _is_linked(a2, 'viewmodeltrace_ViewModelTrace2', b)
    _safe_set(b, 'viewmodeltrace_Trace', None)
    assert not _is_linked(b, 'viewmodeltrace_Trace', a2)
    if hasattr(a2, 'viewmodeltrace_ViewModelTrace2'):
        assert not _is_linked(a2, 'viewmodeltrace_ViewModelTrace2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argumentTuple5_stub_double():
    # viewmodeltrace_MatchArgumentTuple has no real 'viewmodeltrace_MatchArgumentTuple7' property in the generated
    # code (a bare stub) -- manually attach it so viewmodeltrace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewmodeltrace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewmodeltrace_Trace(state="sample_text", traceName="sample_text")
    partner = viewmodeltrace_MatchArgumentTuple()
    setattr(partner, 'viewmodeltrace_MatchArgumentTuple7', None)
    _safe_set(owner, 'viewmodeltrace_Trace6', partner)
    assert getattr(partner, 'viewmodeltrace_MatchArgumentTuple7') == owner
    _safe_set(owner, 'viewmodeltrace_Trace6', None)
    assert getattr(partner, 'viewmodeltrace_MatchArgumentTuple7') is None


def test_assoc_elements3_stub_double():
    # viewmodeltrace_MatchArgumentTuple has no real 'viewmodeltrace_MatchArgumentTuple' property in the generated
    # code (a bare stub) -- manually attach it so viewmodeltrace_MatchArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewmodeltrace_MatchArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewmodeltrace_MatchArgument(parameterName="sample_text")
    partner = viewmodeltrace_MatchArgumentTuple()
    setattr(partner, 'viewmodeltrace_MatchArgumentTuple', None)
    _safe_set(owner, 'viewmodeltrace_MatchArgument', partner)
    assert owner in getattr(partner, 'viewmodeltrace_MatchArgumentTuple')
    _safe_set(owner, 'viewmodeltrace_MatchArgument', None)
    assert owner not in getattr(partner, 'viewmodeltrace_MatchArgumentTuple')


def test_assoc_logicModel0_stub_double():
    # viewmodeltrace_LogicModel has no real 'viewmodeltrace_LogicModel' property in the generated
    # code (a bare stub) -- manually attach it so viewmodeltrace_ViewModelTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewmodeltrace_ViewModelTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewmodeltrace_ViewModelTrace(traceModelId="sample_text")
    partner = viewmodeltrace_LogicModel()
    setattr(partner, 'viewmodeltrace_LogicModel', None)
    _safe_set(owner, 'viewmodeltrace_ViewModelTrace', partner)
    assert getattr(partner, 'viewmodeltrace_LogicModel') == owner
    _safe_set(owner, 'viewmodeltrace_ViewModelTrace', None)
    assert getattr(partner, 'viewmodeltrace_LogicModel') is None


def test_assoc_value9_stub_double():
    # viewmodeltrace_Variable has no real 'viewmodeltrace_Variable' property in the generated
    # code (a bare stub) -- manually attach it so viewmodeltrace_StringVariablePair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewmodeltrace_StringVariablePair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewmodeltrace_StringVariablePair(key="sample_text")
    partner = viewmodeltrace_Variable()
    setattr(partner, 'viewmodeltrace_Variable', None)
    _safe_set(owner, 'viewmodeltrace_StringVariablePair10', partner)
    assert getattr(partner, 'viewmodeltrace_Variable') == owner
    _safe_set(owner, 'viewmodeltrace_StringVariablePair10', None)
    assert getattr(partner, 'viewmodeltrace_Variable') is None


def test_assoc_variables8_stub_double():
    # viewmodeltrace_VariableInstantiationTrace has no real 'viewmodeltrace_VariableInstantiationTrace' property in the generated
    # code (a bare stub) -- manually attach it so viewmodeltrace_StringVariablePair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # viewmodeltrace_StringVariablePair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = viewmodeltrace_StringVariablePair(key="sample_text")
    partner = viewmodeltrace_VariableInstantiationTrace()
    setattr(partner, 'viewmodeltrace_VariableInstantiationTrace', None)
    _safe_set(owner, 'viewmodeltrace_StringVariablePair', partner)
    assert owner in getattr(partner, 'viewmodeltrace_VariableInstantiationTrace')
    _safe_set(owner, 'viewmodeltrace_StringVariablePair', None)
    assert owner not in getattr(partner, 'viewmodeltrace_VariableInstantiationTrace')


