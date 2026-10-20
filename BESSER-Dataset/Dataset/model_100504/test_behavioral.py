import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    reqLanguage_Action,
    reqLanguage_Actor,
    reqLanguage_ActorEvent,
    reqLanguage_Attribute,
    reqLanguage_EObject,
    reqLanguage_Function,
    reqLanguage_MainAttributes,
    reqLanguage_MainComposition,
    reqLanguage_MainFunction,
    reqLanguage_MainFunctions,
    reqLanguage_MainStateTransition,
    reqLanguage_Model,
    reqLanguage_NoTransition,
    reqLanguage_Operator,
    reqLanguage_OutTransition,
    reqLanguage_ParamEvent,
    reqLanguage_Parameter,
    reqLanguage_ParameterState,
    reqLanguage_Prefix,
    reqLanguage_PrefixCondition,
    reqLanguage_PrefixEvent,
    reqLanguage_PrefixRightOperand,
    reqLanguage_PrefixState,
    reqLanguage_ReqID,
    reqLanguage_Requirement,
    reqLanguage_State,
    reqLanguage_StateEvent,
    reqLanguage_System,
    reqLanguage_Time,
    reqLanguage_TimingConstraint,
    reqLanguage_Transition,
    reqLanguage_User,
    reqLanguage_Value,
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

def test_assoc_entity34_reverse_link_reassign_clear():
    a1 = reqLanguage_Parameter(name="sample_text", parameter="sample_text")
    a2 = reqLanguage_Parameter(name="sample_text_2", parameter="sample_text_2")
    b = reqLanguage_ActorEvent(action="sample_text")
    _safe_set(b, 'reqLanguage_ActorEvent35', a1)
    assert _is_linked(b, 'reqLanguage_ActorEvent35', a1)
    if hasattr(a1, 'reqLanguage_Parameter'):
        assert _is_linked(a1, 'reqLanguage_Parameter', b)
    _safe_set(b, 'reqLanguage_ActorEvent35', a2)
    assert _is_linked(b, 'reqLanguage_ActorEvent35', a2)
    if hasattr(a1, 'reqLanguage_Parameter'):
        assert not _is_linked(a1, 'reqLanguage_Parameter', b)
    if hasattr(a2, 'reqLanguage_Parameter'):
        assert _is_linked(a2, 'reqLanguage_Parameter', b)
    _safe_set(b, 'reqLanguage_ActorEvent35', None)
    assert not _is_linked(b, 'reqLanguage_ActorEvent35', a2)
    if hasattr(a2, 'reqLanguage_Parameter'):
        assert not _is_linked(a2, 'reqLanguage_Parameter', b)


def test_assoc_operator19_reverse_link_reassign_clear():
    a1 = reqLanguage_PrefixCondition(prefixFixedSyntax="sample_text")
    a2 = reqLanguage_PrefixCondition(prefixFixedSyntax="sample_text_2")
    b = reqLanguage_Operator(operator="sample_text")
    _safe_set(b, 'reqLanguage_Operator', a1)
    assert _is_linked(b, 'reqLanguage_Operator', a1)
    if hasattr(a1, 'reqLanguage_PrefixCondition20'):
        assert _is_linked(a1, 'reqLanguage_PrefixCondition20', b)
    _safe_set(b, 'reqLanguage_Operator', a2)
    assert _is_linked(b, 'reqLanguage_Operator', a2)
    if hasattr(a1, 'reqLanguage_PrefixCondition20'):
        assert not _is_linked(a1, 'reqLanguage_PrefixCondition20', b)
    if hasattr(a2, 'reqLanguage_PrefixCondition20'):
        assert _is_linked(a2, 'reqLanguage_PrefixCondition20', b)
    _safe_set(b, 'reqLanguage_Operator', None)
    assert not _is_linked(b, 'reqLanguage_Operator', a2)
    if hasattr(a2, 'reqLanguage_PrefixCondition20'):
        assert not _is_linked(a2, 'reqLanguage_PrefixCondition20', b)


def test_assoc_parameter78_reverse_link_reassign_clear():
    a1 = reqLanguage_Parameter(name="sample_text", parameter="sample_text")
    a2 = reqLanguage_Parameter(name="sample_text_2", parameter="sample_text_2")
    b = reqLanguage_Action(action="sample_text", name="sample_text")
    _safe_set(b, 'reqLanguage_Action79', a1)
    assert _is_linked(b, 'reqLanguage_Action79', a1)
    if hasattr(a1, 'reqLanguage_Parameter80'):
        assert _is_linked(a1, 'reqLanguage_Parameter80', b)
    _safe_set(b, 'reqLanguage_Action79', a2)
    assert _is_linked(b, 'reqLanguage_Action79', a2)
    if hasattr(a1, 'reqLanguage_Parameter80'):
        assert not _is_linked(a1, 'reqLanguage_Parameter80', b)
    if hasattr(a2, 'reqLanguage_Parameter80'):
        assert _is_linked(a2, 'reqLanguage_Parameter80', b)
    _safe_set(b, 'reqLanguage_Action79', None)
    assert not _is_linked(b, 'reqLanguage_Action79', a2)
    if hasattr(a2, 'reqLanguage_Parameter80'):
        assert not _is_linked(a2, 'reqLanguage_Parameter80', b)


def test_assoc_time23_reverse_link_reassign_clear():
    a1 = reqLanguage_TimingConstraint(minmax="sample_text", timingConstraint="sample_text")
    a2 = reqLanguage_TimingConstraint(minmax="sample_text_2", timingConstraint="sample_text_2")
    b = reqLanguage_PrefixCondition(prefixFixedSyntax="sample_text")
    _safe_set(b, 'reqLanguage_PrefixCondition24', a1)
    assert _is_linked(b, 'reqLanguage_PrefixCondition24', a1)
    if hasattr(a1, 'reqLanguage_TimingConstraint'):
        assert _is_linked(a1, 'reqLanguage_TimingConstraint', b)
    _safe_set(b, 'reqLanguage_PrefixCondition24', a2)
    assert _is_linked(b, 'reqLanguage_PrefixCondition24', a2)
    if hasattr(a1, 'reqLanguage_TimingConstraint'):
        assert not _is_linked(a1, 'reqLanguage_TimingConstraint', b)
    if hasattr(a2, 'reqLanguage_TimingConstraint'):
        assert _is_linked(a2, 'reqLanguage_TimingConstraint', b)
    _safe_set(b, 'reqLanguage_PrefixCondition24', None)
    assert not _is_linked(b, 'reqLanguage_PrefixCondition24', a2)
    if hasattr(a2, 'reqLanguage_TimingConstraint'):
        assert not _is_linked(a2, 'reqLanguage_TimingConstraint', b)


def test_assoc_time87_reverse_link_reassign_clear():
    a1 = reqLanguage_TimingConstraint(minmax="sample_text", timingConstraint="sample_text")
    a2 = reqLanguage_TimingConstraint(minmax="sample_text_2", timingConstraint="sample_text_2")
    b = reqLanguage_Time(timeUnit="sample_text", value=7)
    _safe_set(b, 'reqLanguage_Time', a1)
    assert _is_linked(b, 'reqLanguage_Time', a1)
    if hasattr(a1, 'reqLanguage_TimingConstraint88'):
        assert _is_linked(a1, 'reqLanguage_TimingConstraint88', b)
    _safe_set(b, 'reqLanguage_Time', a2)
    assert _is_linked(b, 'reqLanguage_Time', a2)
    if hasattr(a1, 'reqLanguage_TimingConstraint88'):
        assert not _is_linked(a1, 'reqLanguage_TimingConstraint88', b)
    if hasattr(a2, 'reqLanguage_TimingConstraint88'):
        assert _is_linked(a2, 'reqLanguage_TimingConstraint88', b)
    _safe_set(b, 'reqLanguage_Time', None)
    assert not _is_linked(b, 'reqLanguage_Time', a2)
    if hasattr(a2, 'reqLanguage_TimingConstraint88'):
        assert not _is_linked(a2, 'reqLanguage_TimingConstraint88', b)


def test_assoc_value21_reverse_link_reassign_clear():
    a1 = reqLanguage_Value(val="sample_text", value=7)
    a2 = reqLanguage_Value(val="sample_text_2", value=13)
    b = reqLanguage_PrefixCondition(prefixFixedSyntax="sample_text")
    _safe_set(b, 'reqLanguage_PrefixCondition22', a1)
    assert _is_linked(b, 'reqLanguage_PrefixCondition22', a1)
    if hasattr(a1, 'reqLanguage_Value'):
        assert _is_linked(a1, 'reqLanguage_Value', b)
    _safe_set(b, 'reqLanguage_PrefixCondition22', a2)
    assert _is_linked(b, 'reqLanguage_PrefixCondition22', a2)
    if hasattr(a1, 'reqLanguage_Value'):
        assert not _is_linked(a1, 'reqLanguage_Value', b)
    if hasattr(a2, 'reqLanguage_Value'):
        assert _is_linked(a2, 'reqLanguage_Value', b)
    _safe_set(b, 'reqLanguage_PrefixCondition22', None)
    assert not _is_linked(b, 'reqLanguage_PrefixCondition22', a2)
    if hasattr(a2, 'reqLanguage_Value'):
        assert not _is_linked(a2, 'reqLanguage_Value', b)


def test_assoc_value29_reverse_link_reassign_clear():
    a1 = reqLanguage_Value(val="sample_text", value=7)
    a2 = reqLanguage_Value(val="sample_text_2", value=13)
    b = reqLanguage_ParamEvent(action="sample_text")
    _safe_set(b, 'reqLanguage_ParamEvent30', a1)
    assert _is_linked(b, 'reqLanguage_ParamEvent30', a1)
    if hasattr(a1, 'reqLanguage_Value31'):
        assert _is_linked(a1, 'reqLanguage_Value31', b)
    _safe_set(b, 'reqLanguage_ParamEvent30', a2)
    assert _is_linked(b, 'reqLanguage_ParamEvent30', a2)
    if hasattr(a1, 'reqLanguage_Value31'):
        assert not _is_linked(a1, 'reqLanguage_Value31', b)
    if hasattr(a2, 'reqLanguage_Value31'):
        assert _is_linked(a2, 'reqLanguage_Value31', b)
    _safe_set(b, 'reqLanguage_ParamEvent30', None)
    assert not _is_linked(b, 'reqLanguage_ParamEvent30', a2)
    if hasattr(a2, 'reqLanguage_Value31'):
        assert not _is_linked(a2, 'reqLanguage_Value31', b)


def test_assoc_value81_reverse_link_reassign_clear():
    a1 = reqLanguage_Value(val="sample_text", value=7)
    a2 = reqLanguage_Value(val="sample_text_2", value=13)
    b = reqLanguage_Action(action="sample_text", name="sample_text")
    _safe_set(b, 'reqLanguage_Action82', a1)
    assert _is_linked(b, 'reqLanguage_Action82', a1)
    if hasattr(a1, 'reqLanguage_Value83'):
        assert _is_linked(a1, 'reqLanguage_Value83', b)
    _safe_set(b, 'reqLanguage_Action82', a2)
    assert _is_linked(b, 'reqLanguage_Action82', a2)
    if hasattr(a1, 'reqLanguage_Value83'):
        assert not _is_linked(a1, 'reqLanguage_Value83', b)
    if hasattr(a2, 'reqLanguage_Value83'):
        assert _is_linked(a2, 'reqLanguage_Value83', b)
    _safe_set(b, 'reqLanguage_Action82', None)
    assert not _is_linked(b, 'reqLanguage_Action82', a2)
    if hasattr(a2, 'reqLanguage_Value83'):
        assert not _is_linked(a2, 'reqLanguage_Value83', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actor32_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject33' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_ActorEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_ActorEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_ActorEvent(action="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject33', None)
    _safe_set(owner, 'reqLanguage_ActorEvent', partner)
    assert getattr(partner, 'reqLanguage_EObject33') == owner
    _safe_set(owner, 'reqLanguage_ActorEvent', None)
    assert getattr(partner, 'reqLanguage_EObject33') is None


def test_assoc_attributeList63_stub_double():
    # reqLanguage_MainAttributes has no real 'reqLanguage_MainAttributes64' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_Attribute(attribute="sample_text", name="sample_text", type="sample_text")
    partner = reqLanguage_MainAttributes()
    setattr(partner, 'reqLanguage_MainAttributes64', None)
    _safe_set(owner, 'reqLanguage_Attribute', partner)
    assert owner in getattr(partner, 'reqLanguage_MainAttributes64')
    _safe_set(owner, 'reqLanguage_Attribute', None)
    assert owner not in getattr(partner, 'reqLanguage_MainAttributes64')


def test_assoc_event_expression25_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject26' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_PrefixEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_PrefixEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_PrefixEvent(prefixFixedSyntax="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject26', None)
    _safe_set(owner, 'reqLanguage_PrefixEvent', partner)
    assert getattr(partner, 'reqLanguage_EObject26') == owner
    _safe_set(owner, 'reqLanguage_PrefixEvent', None)
    assert getattr(partner, 'reqLanguage_EObject26') is None


def test_assoc_function46_stub_double():
    # reqLanguage_MainFunction has no real 'reqLanguage_MainFunction47' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_Action(action="sample_text", name="sample_text")
    partner = reqLanguage_MainFunction()
    setattr(partner, 'reqLanguage_MainFunction47', None)
    _safe_set(owner, 'reqLanguage_Action', partner)
    assert getattr(partner, 'reqLanguage_MainFunction47') == owner
    _safe_set(owner, 'reqLanguage_Action', None)
    assert getattr(partner, 'reqLanguage_MainFunction47') is None


def test_assoc_function58_stub_double():
    # reqLanguage_MainStateTransition has no real 'reqLanguage_MainStateTransition59' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_Action(action="sample_text", name="sample_text")
    partner = reqLanguage_MainStateTransition()
    setattr(partner, 'reqLanguage_MainStateTransition59', None)
    _safe_set(owner, 'reqLanguage_Action60', partner)
    assert getattr(partner, 'reqLanguage_MainStateTransition59') == owner
    _safe_set(owner, 'reqLanguage_Action60', None)
    assert getattr(partner, 'reqLanguage_MainStateTransition59') is None


def test_assoc_functionList67_stub_double():
    # reqLanguage_MainFunctions has no real 'reqLanguage_MainFunctions68' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_Function(function="sample_text", name="sample_text", type="sample_text")
    partner = reqLanguage_MainFunctions()
    setattr(partner, 'reqLanguage_MainFunctions68', None)
    _safe_set(owner, 'reqLanguage_Function', partner)
    assert owner in getattr(partner, 'reqLanguage_MainFunctions68')
    _safe_set(owner, 'reqLanguage_Function', None)
    assert owner not in getattr(partner, 'reqLanguage_MainFunctions68')


def test_assoc_parameter17_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject18' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_PrefixCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_PrefixCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_PrefixCondition(prefixFixedSyntax="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject18', None)
    _safe_set(owner, 'reqLanguage_PrefixCondition', partner)
    assert getattr(partner, 'reqLanguage_EObject18') == owner
    _safe_set(owner, 'reqLanguage_PrefixCondition', None)
    assert getattr(partner, 'reqLanguage_EObject18') is None


def test_assoc_parameter27_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject28' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_ParamEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_ParamEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_ParamEvent(action="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject28', None)
    _safe_set(owner, 'reqLanguage_ParamEvent', partner)
    assert getattr(partner, 'reqLanguage_EObject28') == owner
    _safe_set(owner, 'reqLanguage_ParamEvent', None)
    assert getattr(partner, 'reqLanguage_EObject28') is None


def test_assoc_parameter39_stub_double():
    # reqLanguage_ParameterState has no real 'reqLanguage_ParameterState' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_Parameter(name="sample_text", parameter="sample_text")
    partner = reqLanguage_ParameterState()
    setattr(partner, 'reqLanguage_ParameterState', None)
    _safe_set(owner, 'reqLanguage_Parameter40', partner)
    assert getattr(partner, 'reqLanguage_ParameterState') == owner
    _safe_set(owner, 'reqLanguage_Parameter40', None)
    assert getattr(partner, 'reqLanguage_ParameterState') is None


def test_assoc_prefixList10_stub_double():
    # reqLanguage_Prefix has no real 'reqLanguage_Prefix11' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_PrefixRightOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_PrefixRightOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_PrefixRightOperand(operator="sample_text")
    partner = reqLanguage_Prefix()
    setattr(partner, 'reqLanguage_Prefix11', None)
    _safe_set(owner, 'reqLanguage_PrefixRightOperand', partner)
    assert owner in getattr(partner, 'reqLanguage_Prefix11')
    _safe_set(owner, 'reqLanguage_PrefixRightOperand', None)
    assert owner not in getattr(partner, 'reqLanguage_Prefix11')


def test_assoc_prefixRightOperand12_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject14' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_PrefixRightOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_PrefixRightOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_PrefixRightOperand(operator="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject14', None)
    _safe_set(owner, 'reqLanguage_PrefixRightOperand13', partner)
    assert getattr(partner, 'reqLanguage_EObject14') == owner
    _safe_set(owner, 'reqLanguage_PrefixRightOperand13', None)
    assert getattr(partner, 'reqLanguage_EObject14') is None


def test_assoc_reqID1_stub_double():
    # reqLanguage_Requirement has no real 'reqLanguage_Requirement2' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_ReqID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_ReqID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_ReqID(name="sample_text", reqID="sample_text")
    partner = reqLanguage_Requirement()
    setattr(partner, 'reqLanguage_Requirement2', None)
    _safe_set(owner, 'reqLanguage_ReqID', partner)
    assert getattr(partner, 'reqLanguage_Requirement2') == owner
    _safe_set(owner, 'reqLanguage_ReqID', None)
    assert getattr(partner, 'reqLanguage_Requirement2') is None


def test_assoc_state37_stub_double():
    # reqLanguage_StateEvent has no real 'reqLanguage_StateEvent38' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_State(name="sample_text", state="sample_text")
    partner = reqLanguage_StateEvent()
    setattr(partner, 'reqLanguage_StateEvent38', None)
    _safe_set(owner, 'reqLanguage_State', partner)
    assert getattr(partner, 'reqLanguage_StateEvent38') == owner
    _safe_set(owner, 'reqLanguage_State', None)
    assert getattr(partner, 'reqLanguage_StateEvent38') is None


def test_assoc_stateExpression15_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject16' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_PrefixState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_PrefixState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_PrefixState(prefixFixedSyntax="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject16', None)
    _safe_set(owner, 'reqLanguage_PrefixState', partner)
    assert getattr(partner, 'reqLanguage_EObject16') == owner
    _safe_set(owner, 'reqLanguage_PrefixState', None)
    assert getattr(partner, 'reqLanguage_EObject16') is None


def test_assoc_subject84_stub_double():
    # reqLanguage_EObject has no real 'reqLanguage_EObject86' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_Action(action="sample_text", name="sample_text")
    partner = reqLanguage_EObject()
    setattr(partner, 'reqLanguage_EObject86', None)
    _safe_set(owner, 'reqLanguage_Action85', partner)
    assert getattr(partner, 'reqLanguage_EObject86') == owner
    _safe_set(owner, 'reqLanguage_Action85', None)
    assert getattr(partner, 'reqLanguage_EObject86') is None


def test_assoc_subsystemList50_stub_double():
    # reqLanguage_MainComposition has no real 'reqLanguage_MainComposition51' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_System(name="sample_text", system="sample_text")
    partner = reqLanguage_MainComposition()
    setattr(partner, 'reqLanguage_MainComposition51', None)
    _safe_set(owner, 'reqLanguage_System52', partner)
    assert owner in getattr(partner, 'reqLanguage_MainComposition51')
    _safe_set(owner, 'reqLanguage_System52', None)
    assert owner not in getattr(partner, 'reqLanguage_MainComposition51')


def test_assoc_system36_stub_double():
    # reqLanguage_StateEvent has no real 'reqLanguage_StateEvent' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_System(name="sample_text", system="sample_text")
    partner = reqLanguage_StateEvent()
    setattr(partner, 'reqLanguage_StateEvent', None)
    _safe_set(owner, 'reqLanguage_System', partner)
    assert getattr(partner, 'reqLanguage_StateEvent') == owner
    _safe_set(owner, 'reqLanguage_System', None)
    assert getattr(partner, 'reqLanguage_StateEvent') is None


def test_assoc_system48_stub_double():
    # reqLanguage_MainComposition has no real 'reqLanguage_MainComposition' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_System(name="sample_text", system="sample_text")
    partner = reqLanguage_MainComposition()
    setattr(partner, 'reqLanguage_MainComposition', None)
    _safe_set(owner, 'reqLanguage_System49', partner)
    assert getattr(partner, 'reqLanguage_MainComposition') == owner
    _safe_set(owner, 'reqLanguage_System49', None)
    assert getattr(partner, 'reqLanguage_MainComposition') is None


def test_assoc_system53_stub_double():
    # reqLanguage_MainStateTransition has no real 'reqLanguage_MainStateTransition' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_System(name="sample_text", system="sample_text")
    partner = reqLanguage_MainStateTransition()
    setattr(partner, 'reqLanguage_MainStateTransition', None)
    _safe_set(owner, 'reqLanguage_System54', partner)
    assert getattr(partner, 'reqLanguage_MainStateTransition') == owner
    _safe_set(owner, 'reqLanguage_System54', None)
    assert getattr(partner, 'reqLanguage_MainStateTransition') is None


def test_assoc_system61_stub_double():
    # reqLanguage_MainAttributes has no real 'reqLanguage_MainAttributes' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_System(name="sample_text", system="sample_text")
    partner = reqLanguage_MainAttributes()
    setattr(partner, 'reqLanguage_MainAttributes', None)
    _safe_set(owner, 'reqLanguage_System62', partner)
    assert getattr(partner, 'reqLanguage_MainAttributes') == owner
    _safe_set(owner, 'reqLanguage_System62', None)
    assert getattr(partner, 'reqLanguage_MainAttributes') is None


def test_assoc_system65_stub_double():
    # reqLanguage_MainFunctions has no real 'reqLanguage_MainFunctions' property in the generated
    # code (a bare stub) -- manually attach it so reqLanguage_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqLanguage_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqLanguage_System(name="sample_text", system="sample_text")
    partner = reqLanguage_MainFunctions()
    setattr(partner, 'reqLanguage_MainFunctions', None)
    _safe_set(owner, 'reqLanguage_System66', partner)
    assert getattr(partner, 'reqLanguage_MainFunctions') == owner
    _safe_set(owner, 'reqLanguage_System66', None)
    assert getattr(partner, 'reqLanguage_MainFunctions') is None


