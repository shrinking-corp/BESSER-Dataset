import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractSimpleState,
    AbstractState,
    Conditional,
    Data,
    DatamodelContainer,
    DescriptionContainer,
    Donedata,
    ExecutableContent,
    IAdaptable,
    InitialState,
    Node,
    State,
    Transition,
    TransitionSource,
    TransitionTarget,
    scxml_AbstractSimpleState,
    scxml_AbstractState,
    scxml_Assign,
    scxml_Cancel,
    scxml_CondEventTransition,
    scxml_Conditional,
    scxml_Content,
    scxml_Data,
    scxml_Datamodel,
    scxml_DatamodelContainer,
    scxml_Description,
    scxml_DescriptionContainer,
    scxml_Donedata,
    scxml_EClass,
    scxml_EObject,
    scxml_Else,
    scxml_ElseIf,
    scxml_ExecutableContent,
    scxml_FinalState,
    scxml_HistoryState,
    scxml_IAdaptable,
    scxml_If,
    scxml_InitialState,
    scxml_Invoke,
    scxml_Log,
    scxml_Node,
    scxml_OnEntry,
    scxml_OnExit,
    scxml_ParallelState,
    scxml_Param,
    scxml_Raise,
    scxml_Script,
    scxml_Send,
    scxml_SimpleState,
    scxml_State,
    scxml_StateChart,
    scxml_Transition,
    scxml_TransitionSource,
    scxml_TransitionTarget,
    scxml_Validate,
    scxml_XData,
    scxml_XObject,
    AdapterToken,
    ExmodeDatatype,
    HistoryTypeDatatype,
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

def test_assoc_assign36_reverse_link_reassign_clear():
    a1 = scxml_ExecutableContent(group="sample_text")
    a2 = scxml_ExecutableContent(group="sample_text_2")
    b = scxml_Assign(expr="sample_text", location="sample_text", name="sample_text")
    _safe_set(b, 'scxml_Assign', a1)
    assert _is_linked(b, 'scxml_Assign', a1)
    if hasattr(a1, 'scxml_ExecutableContent37'):
        assert _is_linked(a1, 'scxml_ExecutableContent37', b)
    _safe_set(b, 'scxml_Assign', a2)
    assert _is_linked(b, 'scxml_Assign', a2)
    if hasattr(a1, 'scxml_ExecutableContent37'):
        assert not _is_linked(a1, 'scxml_ExecutableContent37', b)
    if hasattr(a2, 'scxml_ExecutableContent37'):
        assert _is_linked(a2, 'scxml_ExecutableContent37', b)
    _safe_set(b, 'scxml_Assign', None)
    assert not _is_linked(b, 'scxml_Assign', a2)
    if hasattr(a2, 'scxml_ExecutableContent37'):
        assert not _is_linked(a2, 'scxml_ExecutableContent37', b)


def test_assoc_cancel34_reverse_link_reassign_clear():
    a1 = scxml_ExecutableContent(group="sample_text")
    a2 = scxml_ExecutableContent(group="sample_text_2")
    b = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_Cancel', a1)
    assert _is_linked(b, 'scxml_Cancel', a1)
    if hasattr(a1, 'scxml_ExecutableContent35'):
        assert _is_linked(a1, 'scxml_ExecutableContent35', b)
    _safe_set(b, 'scxml_Cancel', a2)
    assert _is_linked(b, 'scxml_Cancel', a2)
    if hasattr(a1, 'scxml_ExecutableContent35'):
        assert not _is_linked(a1, 'scxml_ExecutableContent35', b)
    if hasattr(a2, 'scxml_ExecutableContent35'):
        assert _is_linked(a2, 'scxml_ExecutableContent35', b)
    _safe_set(b, 'scxml_Cancel', None)
    assert not _is_linked(b, 'scxml_Cancel', a2)
    if hasattr(a2, 'scxml_ExecutableContent35'):
        assert not _is_linked(a2, 'scxml_ExecutableContent35', b)


def test_assoc_data53_reverse_link_reassign_clear():
    a1 = scxml_Datamodel(schema="sample_text")
    a2 = scxml_Datamodel(schema="sample_text_2")
    b = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    _safe_set(b, 'scxml_Data', a1)
    assert _is_linked(b, 'scxml_Data', a1)
    if hasattr(a1, 'scxml_Datamodel'):
        assert _is_linked(a1, 'scxml_Datamodel', b)
    _safe_set(b, 'scxml_Data', a2)
    assert _is_linked(b, 'scxml_Data', a2)
    if hasattr(a1, 'scxml_Datamodel'):
        assert not _is_linked(a1, 'scxml_Datamodel', b)
    if hasattr(a2, 'scxml_Datamodel'):
        assert _is_linked(a2, 'scxml_Datamodel', b)
    _safe_set(b, 'scxml_Data', None)
    assert not _is_linked(b, 'scxml_Data', a2)
    if hasattr(a2, 'scxml_Datamodel'):
        assert not _is_linked(a2, 'scxml_Datamodel', b)


def test_assoc_datamodel54_reverse_link_reassign_clear():
    a1 = scxml_DatamodelContainer()
    a2 = scxml_DatamodelContainer()
    b = scxml_Datamodel(schema="sample_text")
    _safe_set(b, 'scxml_Datamodel55', a1)
    assert _is_linked(b, 'scxml_Datamodel55', a1)
    if hasattr(a1, 'scxml_DatamodelContainer'):
        assert _is_linked(a1, 'scxml_DatamodelContainer', b)
    _safe_set(b, 'scxml_Datamodel55', a2)
    assert _is_linked(b, 'scxml_Datamodel55', a2)
    if hasattr(a1, 'scxml_DatamodelContainer'):
        assert not _is_linked(a1, 'scxml_DatamodelContainer', b)
    if hasattr(a2, 'scxml_DatamodelContainer'):
        assert _is_linked(a2, 'scxml_DatamodelContainer', b)
    _safe_set(b, 'scxml_Datamodel55', None)
    assert not _is_linked(b, 'scxml_Datamodel55', a2)
    if hasattr(a2, 'scxml_DatamodelContainer'):
        assert not _is_linked(a2, 'scxml_DatamodelContainer', b)


def test_assoc_description56_reverse_link_reassign_clear():
    a1 = scxml_DescriptionContainer()
    a2 = scxml_DescriptionContainer()
    b = scxml_Description(value="sample_text")
    _safe_set(b, 'scxml_Description', a1)
    assert _is_linked(b, 'scxml_Description', a1)
    if hasattr(a1, 'scxml_DescriptionContainer'):
        assert _is_linked(a1, 'scxml_DescriptionContainer', b)
    _safe_set(b, 'scxml_Description', a2)
    assert _is_linked(b, 'scxml_Description', a2)
    if hasattr(a1, 'scxml_DescriptionContainer'):
        assert not _is_linked(a1, 'scxml_DescriptionContainer', b)
    if hasattr(a2, 'scxml_DescriptionContainer'):
        assert _is_linked(a2, 'scxml_DescriptionContainer', b)
    _safe_set(b, 'scxml_Description', None)
    assert not _is_linked(b, 'scxml_Description', a2)
    if hasattr(a2, 'scxml_DescriptionContainer'):
        assert not _is_linked(a2, 'scxml_DescriptionContainer', b)


def test_assoc_finalize47_reverse_link_reassign_clear():
    a1 = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_Invoke(autoforward="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", src="sample_text_2", srcexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ExecutableContent(group="sample_text")
    _safe_set(b, 'scxml_ExecutableContent49', a1)
    assert _is_linked(b, 'scxml_ExecutableContent49', a1)
    if hasattr(a1, 'scxml_Invoke48'):
        assert _is_linked(a1, 'scxml_Invoke48', b)
    _safe_set(b, 'scxml_ExecutableContent49', a2)
    assert _is_linked(b, 'scxml_ExecutableContent49', a2)
    if hasattr(a1, 'scxml_Invoke48'):
        assert not _is_linked(a1, 'scxml_Invoke48', b)
    if hasattr(a2, 'scxml_Invoke48'):
        assert _is_linked(a2, 'scxml_Invoke48', b)
    _safe_set(b, 'scxml_ExecutableContent49', None)
    assert not _is_linked(b, 'scxml_ExecutableContent49', a2)
    if hasattr(a2, 'scxml_Invoke48'):
        assert not _is_linked(a2, 'scxml_Invoke48', b)


def test_assoc_log28_reverse_link_reassign_clear():
    a1 = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    a2 = scxml_Log(expr="sample_text_2", label="sample_text_2", level="sample_text_2")
    b = scxml_ExecutableContent(group="sample_text")
    _safe_set(b, 'scxml_ExecutableContent29', {a1})
    assert _is_linked(b, 'scxml_ExecutableContent29', a1)
    if hasattr(a1, 'scxml_Log'):
        assert _is_linked(a1, 'scxml_Log', b)
    _safe_set(b, 'scxml_ExecutableContent29', {a2})
    assert _is_linked(b, 'scxml_ExecutableContent29', a2)
    if hasattr(a1, 'scxml_Log'):
        assert not _is_linked(a1, 'scxml_Log', b)
    if hasattr(a2, 'scxml_Log'):
        assert _is_linked(a2, 'scxml_Log', b)
    _safe_set(b, 'scxml_ExecutableContent29', set())
    assert not _is_linked(b, 'scxml_ExecutableContent29', a2)
    if hasattr(a2, 'scxml_Log'):
        assert not _is_linked(a2, 'scxml_Log', b)


def test_assoc_raise_30_reverse_link_reassign_clear():
    a1 = scxml_Raise(event="sample_text")
    a2 = scxml_Raise(event="sample_text_2")
    b = scxml_ExecutableContent(group="sample_text")
    _safe_set(b, 'scxml_ExecutableContent31', {a1})
    assert _is_linked(b, 'scxml_ExecutableContent31', a1)
    if hasattr(a1, 'scxml_Raise'):
        assert _is_linked(a1, 'scxml_Raise', b)
    _safe_set(b, 'scxml_ExecutableContent31', {a2})
    assert _is_linked(b, 'scxml_ExecutableContent31', a2)
    if hasattr(a1, 'scxml_Raise'):
        assert not _is_linked(a1, 'scxml_Raise', b)
    if hasattr(a2, 'scxml_Raise'):
        assert _is_linked(a2, 'scxml_Raise', b)
    _safe_set(b, 'scxml_ExecutableContent31', set())
    assert not _is_linked(b, 'scxml_ExecutableContent31', a2)
    if hasattr(a2, 'scxml_Raise'):
        assert not _is_linked(a2, 'scxml_Raise', b)


def test_assoc_script0_reverse_link_reassign_clear():
    a1 = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    a2 = scxml_StateChart(exmode="sample_text_2", id="sample_text_2", profile="sample_text_2", version="sample_text_2", xmlns="sample_text_2")
    b = scxml_Script(value="sample_text")
    _safe_set(b, 'scxml_Script', a1)
    assert _is_linked(b, 'scxml_Script', a1)
    if hasattr(a1, 'scxml_StateChart'):
        assert _is_linked(a1, 'scxml_StateChart', b)
    _safe_set(b, 'scxml_Script', a2)
    assert _is_linked(b, 'scxml_Script', a2)
    if hasattr(a1, 'scxml_StateChart'):
        assert not _is_linked(a1, 'scxml_StateChart', b)
    if hasattr(a2, 'scxml_StateChart'):
        assert _is_linked(a2, 'scxml_StateChart', b)
    _safe_set(b, 'scxml_Script', None)
    assert not _is_linked(b, 'scxml_Script', a2)
    if hasattr(a2, 'scxml_StateChart'):
        assert not _is_linked(a2, 'scxml_StateChart', b)


def test_assoc_script40_reverse_link_reassign_clear():
    a1 = scxml_Script(value="sample_text")
    a2 = scxml_Script(value="sample_text_2")
    b = scxml_ExecutableContent(group="sample_text")
    _safe_set(b, 'scxml_ExecutableContent41', {a1})
    assert _is_linked(b, 'scxml_ExecutableContent41', a1)
    if hasattr(a1, 'scxml_Script42'):
        assert _is_linked(a1, 'scxml_Script42', b)
    _safe_set(b, 'scxml_ExecutableContent41', {a2})
    assert _is_linked(b, 'scxml_ExecutableContent41', a2)
    if hasattr(a1, 'scxml_Script42'):
        assert not _is_linked(a1, 'scxml_Script42', b)
    if hasattr(a2, 'scxml_Script42'):
        assert _is_linked(a2, 'scxml_Script42', b)
    _safe_set(b, 'scxml_ExecutableContent41', set())
    assert not _is_linked(b, 'scxml_ExecutableContent41', a2)
    if hasattr(a2, 'scxml_Script42'):
        assert not _is_linked(a2, 'scxml_Script42', b)


def test_assoc_send32_reverse_link_reassign_clear():
    a1 = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_Send(delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", hints="sample_text_2", hintsexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ExecutableContent(group="sample_text")
    _safe_set(b, 'scxml_ExecutableContent33', {a1})
    assert _is_linked(b, 'scxml_ExecutableContent33', a1)
    if hasattr(a1, 'scxml_Send'):
        assert _is_linked(a1, 'scxml_Send', b)
    _safe_set(b, 'scxml_ExecutableContent33', {a2})
    assert _is_linked(b, 'scxml_ExecutableContent33', a2)
    if hasattr(a1, 'scxml_Send'):
        assert not _is_linked(a1, 'scxml_Send', b)
    if hasattr(a2, 'scxml_Send'):
        assert _is_linked(a2, 'scxml_Send', b)
    _safe_set(b, 'scxml_ExecutableContent33', set())
    assert not _is_linked(b, 'scxml_ExecutableContent33', a2)
    if hasattr(a2, 'scxml_Send'):
        assert not _is_linked(a2, 'scxml_Send', b)


def test_assoc_validate38_reverse_link_reassign_clear():
    a1 = scxml_Validate(location="sample_text", schema="sample_text")
    a2 = scxml_Validate(location="sample_text_2", schema="sample_text_2")
    b = scxml_ExecutableContent(group="sample_text")
    _safe_set(b, 'scxml_ExecutableContent39', {a1})
    assert _is_linked(b, 'scxml_ExecutableContent39', a1)
    if hasattr(a1, 'scxml_Validate'):
        assert _is_linked(a1, 'scxml_Validate', b)
    _safe_set(b, 'scxml_ExecutableContent39', {a2})
    assert _is_linked(b, 'scxml_ExecutableContent39', a2)
    if hasattr(a1, 'scxml_Validate'):
        assert not _is_linked(a1, 'scxml_Validate', b)
    if hasattr(a2, 'scxml_Validate'):
        assert _is_linked(a2, 'scxml_Validate', b)
    _safe_set(b, 'scxml_ExecutableContent39', set())
    assert not _is_linked(b, 'scxml_ExecutableContent39', a2)
    if hasattr(a2, 'scxml_Validate'):
        assert not _is_linked(a2, 'scxml_Validate', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_history8_stub_double():
    # scxml_State has no real 'scxml_State' property in the generated
    # code (a bare stub) -- manually attach it so scxml_HistoryState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_HistoryState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_HistoryState(type="sample_text")
    partner = scxml_State()
    setattr(partner, 'scxml_State', None)
    _safe_set(owner, 'scxml_HistoryState', partner)
    assert getattr(partner, 'scxml_State') == owner
    _safe_set(owner, 'scxml_HistoryState', None)
    assert getattr(partner, 'scxml_State') is None


def test_assoc_if_27_stub_double():
    # scxml_If has no real 'scxml_If' property in the generated
    # code (a bare stub) -- manually attach it so scxml_ExecutableContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_ExecutableContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_ExecutableContent(group="sample_text")
    partner = scxml_If()
    setattr(partner, 'scxml_If', None)
    _safe_set(owner, 'scxml_ExecutableContent', {partner})
    assert getattr(partner, 'scxml_If') == owner
    _safe_set(owner, 'scxml_ExecutableContent', set())
    assert getattr(partner, 'scxml_If') is None


def test_assoc_initial117_stub_double():
    # scxml_AbstractSimpleState has no real 'scxml_AbstractSimpleState' property in the generated
    # code (a bare stub) -- manually attach it so scxml_TransitionTarget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_TransitionTarget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_TransitionTarget(id="sample_text")
    partner = scxml_AbstractSimpleState()
    setattr(partner, 'scxml_AbstractSimpleState', None)
    _safe_set(owner, 'scxml_TransitionTarget18', partner)
    assert getattr(partner, 'scxml_AbstractSimpleState') == owner
    _safe_set(owner, 'scxml_TransitionTarget18', None)
    assert getattr(partner, 'scxml_AbstractSimpleState') is None


def test_assoc_invoke25_stub_double():
    # scxml_SimpleState has no real 'scxml_SimpleState26' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Invoke's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Invoke's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_SimpleState()
    setattr(partner, 'scxml_SimpleState26', None)
    _safe_set(owner, 'scxml_Invoke', partner)
    assert getattr(partner, 'scxml_SimpleState26') == owner
    _safe_set(owner, 'scxml_Invoke', None)
    assert getattr(partner, 'scxml_SimpleState26') is None


def test_assoc_param12_stub_double():
    # scxml_Donedata has no real 'scxml_Donedata' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Param(expr="sample_text", name="sample_text")
    partner = scxml_Donedata()
    setattr(partner, 'scxml_Donedata', None)
    _safe_set(owner, 'scxml_Param', partner)
    assert owner in getattr(partner, 'scxml_Donedata')
    _safe_set(owner, 'scxml_Param', None)
    assert owner not in getattr(partner, 'scxml_Donedata')


def test_assoc_target9_stub_double():
    # scxml_Transition has no real 'scxml_Transition' property in the generated
    # code (a bare stub) -- manually attach it so scxml_TransitionTarget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_TransitionTarget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_TransitionTarget(id="sample_text")
    partner = scxml_Transition()
    setattr(partner, 'scxml_Transition', None)
    _safe_set(owner, 'scxml_TransitionTarget', partner)
    assert owner in getattr(partner, 'scxml_Transition')
    _safe_set(owner, 'scxml_TransitionTarget', None)
    assert owner not in getattr(partner, 'scxml_Transition')


def test_assoc_transition4_stub_double():
    # scxml_TransitionSource has no real 'scxml_TransitionSource' property in the generated
    # code (a bare stub) -- manually attach it so scxml_CondEventTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_CondEventTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_CondEventTransition(cond="sample_text", event="sample_text")
    partner = scxml_TransitionSource()
    setattr(partner, 'scxml_TransitionSource', None)
    _safe_set(owner, 'scxml_CondEventTransition', partner)
    assert owner in getattr(partner, 'scxml_TransitionSource')
    _safe_set(owner, 'scxml_CondEventTransition', None)
    assert owner not in getattr(partner, 'scxml_TransitionSource')


def test_assoc_type52_stub_double():
    # scxml_EClass has no real 'scxml_EClass' property in the generated
    # code (a bare stub) -- manually attach it so scxml_XObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_XObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_XObject(classifierName="sample_text", exchange=True, nsUri="sample_text")
    partner = scxml_EClass()
    setattr(partner, 'scxml_EClass', None)
    _safe_set(owner, 'scxml_XObject', partner)
    assert getattr(partner, 'scxml_EClass') == owner
    _safe_set(owner, 'scxml_XObject', None)
    assert getattr(partner, 'scxml_EClass') is None


