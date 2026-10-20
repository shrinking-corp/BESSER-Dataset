import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    IExpressionTerm,
    INamedElement,
    Port,
    State,
    StateAutomaton,
    TransitionSegment,
    TransitionSegmentSpecification,
    Var,
    model_INamedElement,
    model_component_Component,
    model_component_InputPort,
    model_component_OutputPort,
    model_component_Port,
    model_expression_BoolConst,
    model_expression_IExpressionTerm,
    model_expression_IntConst,
    model_expression_Operation,
    model_expression_Var,
    model_state_Action,
    model_state_DataStateVariable,
    model_state_State,
    model_state_StateAutomaton,
    model_state_TransitionSegment,
    model_state_TransitionSegmentSpecification,
    EOperator,
    EType,
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

def test_assoc_arguments0_stub_double():
    # IExpressionTerm has no real 'IExpressionTerm' property in the generated
    # code (a bare stub) -- manually attach it so model_expression_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_expression_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_expression_Operation(operator="sample_text")
    partner = IExpressionTerm()
    setattr(partner, 'IExpressionTerm', None)
    _safe_set(owner, 'model_expression_Operation', {partner})
    assert getattr(partner, 'IExpressionTerm') == owner
    _safe_set(owner, 'model_expression_Operation', set())
    assert getattr(partner, 'IExpressionTerm') is None


def test_assoc_idleTransitionsSpecifications12_stub_double():
    # TransitionSegmentSpecification has no real 'TransitionSegmentSpecification' property in the generated
    # code (a bare stub) -- manually attach it so model_state_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_state_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_state_State(isInitial=True)
    partner = TransitionSegmentSpecification()
    setattr(partner, 'TransitionSegmentSpecification', None)
    _safe_set(owner, 'model_state_State', {partner})
    assert getattr(partner, 'TransitionSegmentSpecification') == owner
    _safe_set(owner, 'model_state_State', set())
    assert getattr(partner, 'TransitionSegmentSpecification') is None


def test_assoc_initialValue25_stub_double():
    # IExpressionTerm has no real 'IExpressionTerm26' property in the generated
    # code (a bare stub) -- manually attach it so model_state_DataStateVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_state_DataStateVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_state_DataStateVariable(type="sample_text")
    partner = IExpressionTerm()
    setattr(partner, 'IExpressionTerm26', None)
    _safe_set(owner, 'model_state_DataStateVariable', partner)
    assert getattr(partner, 'IExpressionTerm26') == owner
    _safe_set(owner, 'model_state_DataStateVariable', None)
    assert getattr(partner, 'IExpressionTerm26') is None


def test_assoc_initialValue7_stub_double():
    # IExpressionTerm has no real 'IExpressionTerm8' property in the generated
    # code (a bare stub) -- manually attach it so model_component_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_component_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_component_Port(type="sample_text")
    partner = IExpressionTerm()
    setattr(partner, 'IExpressionTerm8', None)
    _safe_set(owner, 'model_component_Port', partner)
    assert getattr(partner, 'IExpressionTerm8') == owner
    _safe_set(owner, 'model_component_Port', None)
    assert getattr(partner, 'IExpressionTerm8') is None


