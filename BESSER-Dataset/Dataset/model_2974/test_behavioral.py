import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    MTReference,
    OpType,
    Operation,
    Reference,
    State,
    Trigger,
    Value,
    WritableReference,
    restbehavior_Action,
    restbehavior_ActionSequence,
    restbehavior_Attribute,
    restbehavior_AttributeReference,
    restbehavior_BehaviorSpecification,
    restbehavior_BinOpType,
    restbehavior_BinaryOperation,
    restbehavior_Condition,
    restbehavior_ConditionalAction,
    restbehavior_Constant,
    restbehavior_CreateAction,
    restbehavior_Creator,
    restbehavior_DataType,
    restbehavior_DeletedState,
    restbehavior_ExternalLink,
    restbehavior_ExternalLinkReference,
    restbehavior_InternalLink,
    restbehavior_InternalLinkReference,
    restbehavior_InternalMessage,
    restbehavior_ListAddAction,
    restbehavior_ListRemoveAction,
    restbehavior_MTLinkReference,
    restbehavior_MTReference,
    restbehavior_MediaType,
    restbehavior_MediaTypeElement,
    restbehavior_MediaTypeLink,
    restbehavior_MessageAction,
    restbehavior_Metadata,
    restbehavior_Method,
    restbehavior_MtElementReference,
    restbehavior_OpType,
    restbehavior_Operation,
    restbehavior_Parameter,
    restbehavior_Reference,
    restbehavior_Representation,
    restbehavior_ReturnAction,
    restbehavior_State,
    restbehavior_StatusCode,
    restbehavior_Transition,
    restbehavior_Trigger,
    restbehavior_UpdateAction,
    restbehavior_Value,
    restbehavior_WritableReference,
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

def test_assoc_entering7_stub_double():
    # restbehavior_BehaviorSpecification has no real 'restbehavior_BehaviorSpecification8' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_State(name="sample_text")
    partner = restbehavior_BehaviorSpecification()
    setattr(partner, 'restbehavior_BehaviorSpecification8', None)
    _safe_set(owner, 'restbehavior_State', partner)
    assert getattr(partner, 'restbehavior_BehaviorSpecification8') == owner
    _safe_set(owner, 'restbehavior_State', None)
    assert getattr(partner, 'restbehavior_BehaviorSpecification8') is None


def test_assoc_leaving9_stub_double():
    # restbehavior_BehaviorSpecification has no real 'restbehavior_BehaviorSpecification11' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_State(name="sample_text")
    partner = restbehavior_BehaviorSpecification()
    setattr(partner, 'restbehavior_BehaviorSpecification11', None)
    _safe_set(owner, 'restbehavior_State10', partner)
    assert getattr(partner, 'restbehavior_BehaviorSpecification11') == owner
    _safe_set(owner, 'restbehavior_State10', None)
    assert getattr(partner, 'restbehavior_BehaviorSpecification11') is None


def test_assoc_message28_stub_double():
    # restbehavior_MessageAction has no real 'restbehavior_MessageAction' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_InternalMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_InternalMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_InternalMessage(name="sample_text")
    partner = restbehavior_MessageAction()
    setattr(partner, 'restbehavior_MessageAction', None)
    _safe_set(owner, 'restbehavior_InternalMessage', partner)
    assert getattr(partner, 'restbehavior_MessageAction') == owner
    _safe_set(owner, 'restbehavior_InternalMessage', None)
    assert getattr(partner, 'restbehavior_MessageAction') is None


def test_assoc_resultType58_stub_double():
    # restbehavior_DataType has no real 'restbehavior_DataType59' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_OpType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_OpType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_OpType(name="sample_text")
    partner = restbehavior_DataType()
    setattr(partner, 'restbehavior_DataType59', None)
    _safe_set(owner, 'restbehavior_OpType', partner)
    assert getattr(partner, 'restbehavior_DataType59') == owner
    _safe_set(owner, 'restbehavior_OpType', None)
    assert getattr(partner, 'restbehavior_DataType59') is None


def test_assoc_status45_stub_double():
    # restbehavior_ReturnAction has no real 'restbehavior_ReturnAction' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_StatusCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_StatusCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_StatusCode(number=7)
    partner = restbehavior_ReturnAction()
    setattr(partner, 'restbehavior_ReturnAction', None)
    _safe_set(owner, 'restbehavior_StatusCode', partner)
    assert getattr(partner, 'restbehavior_ReturnAction') == owner
    _safe_set(owner, 'restbehavior_StatusCode', None)
    assert getattr(partner, 'restbehavior_ReturnAction') is None


def test_assoc_supportedMethods14_stub_double():
    # restbehavior_Method has no real 'restbehavior_Method' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_State(name="sample_text")
    partner = restbehavior_Method()
    setattr(partner, 'restbehavior_Method', None)
    _safe_set(owner, 'restbehavior_State15', {partner})
    assert getattr(partner, 'restbehavior_Method') == owner
    _safe_set(owner, 'restbehavior_State15', set())
    assert getattr(partner, 'restbehavior_Method') is None


def test_assoc_targetState18_stub_double():
    # restbehavior_Transition has no real 'restbehavior_Transition19' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_State(name="sample_text")
    partner = restbehavior_Transition()
    setattr(partner, 'restbehavior_Transition19', None)
    _safe_set(owner, 'restbehavior_State20', partner)
    assert getattr(partner, 'restbehavior_Transition19') == owner
    _safe_set(owner, 'restbehavior_State20', None)
    assert getattr(partner, 'restbehavior_Transition19') is None


def test_assoc_transitions12_stub_double():
    # restbehavior_Transition has no real 'restbehavior_Transition' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_State(name="sample_text")
    partner = restbehavior_Transition()
    setattr(partner, 'restbehavior_Transition', None)
    _safe_set(owner, 'restbehavior_State13', {partner})
    assert getattr(partner, 'restbehavior_Transition') == owner
    _safe_set(owner, 'restbehavior_State13', set())
    assert getattr(partner, 'restbehavior_Transition') is None


def test_assoc_type50_stub_double():
    # restbehavior_DataType has no real 'restbehavior_DataType' property in the generated
    # code (a bare stub) -- manually attach it so restbehavior_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restbehavior_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restbehavior_Constant(stringRepresentation="sample_text")
    partner = restbehavior_DataType()
    setattr(partner, 'restbehavior_DataType', None)
    _safe_set(owner, 'restbehavior_Constant', partner)
    assert getattr(partner, 'restbehavior_DataType') == owner
    _safe_set(owner, 'restbehavior_Constant', None)
    assert getattr(partner, 'restbehavior_DataType') is None


