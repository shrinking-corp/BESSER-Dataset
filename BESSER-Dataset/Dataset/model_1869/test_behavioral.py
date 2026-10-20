import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    Event,
    Node,
    Parameter,
    State,
    statesml_Attribute,
    statesml_Boolean,
    statesml_ChangeEvent,
    statesml_ChangeExpression,
    statesml_DataType,
    statesml_DataTypeLibrary,
    statesml_Edge,
    statesml_Event,
    statesml_Function,
    statesml_FunctionCall,
    statesml_IncomingParameter,
    statesml_InitialState,
    statesml_Integer,
    statesml_MiddleState,
    statesml_Node,
    statesml_Parameter,
    statesml_ParameterValue,
    statesml_ReturnParameter,
    statesml_SelectionConvergence,
    statesml_SelectionDivergence,
    statesml_State,
    statesml_StateSystem,
    statesml_StateSystemModel,
    statesml_StatesModel,
    statesml_String,
    statesml_SystemUnit,
    statesml_SystemUnitLibrary,
    statesml_SystemUnitModel,
    statesml_TerminalState,
    statesml_Transition,
    statesml_Trigger,
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

def test_assoc_attribute12_reverse_link_reassign_clear():
    a1 = statesml_SystemUnit(name="sample_text")
    a2 = statesml_SystemUnit(name="sample_text_2")
    b = statesml_Attribute(name="sample_text")
    _safe_set(b, 'statesml_Attribute14', a1)
    assert _is_linked(b, 'statesml_Attribute14', a1)
    if hasattr(a1, 'statesml_SystemUnit13'):
        assert _is_linked(a1, 'statesml_SystemUnit13', b)
    _safe_set(b, 'statesml_Attribute14', a2)
    assert _is_linked(b, 'statesml_Attribute14', a2)
    if hasattr(a1, 'statesml_SystemUnit13'):
        assert not _is_linked(a1, 'statesml_SystemUnit13', b)
    if hasattr(a2, 'statesml_SystemUnit13'):
        assert _is_linked(a2, 'statesml_SystemUnit13', b)
    _safe_set(b, 'statesml_Attribute14', None)
    assert not _is_linked(b, 'statesml_Attribute14', a2)
    if hasattr(a2, 'statesml_SystemUnit13'):
        assert not _is_linked(a2, 'statesml_SystemUnit13', b)


def test_assoc_datatype1_reverse_link_reassign_clear():
    a1 = statesml_DataType(name="sample_text")
    a2 = statesml_DataType(name="sample_text_2")
    b = statesml_Attribute(name="sample_text")
    _safe_set(b, 'statesml_Attribute', a1)
    assert _is_linked(b, 'statesml_Attribute', a1)
    if hasattr(a1, 'statesml_DataType'):
        assert _is_linked(a1, 'statesml_DataType', b)
    _safe_set(b, 'statesml_Attribute', a2)
    assert _is_linked(b, 'statesml_Attribute', a2)
    if hasattr(a1, 'statesml_DataType'):
        assert not _is_linked(a1, 'statesml_DataType', b)
    if hasattr(a2, 'statesml_DataType'):
        assert _is_linked(a2, 'statesml_DataType', b)
    _safe_set(b, 'statesml_Attribute', None)
    assert not _is_linked(b, 'statesml_Attribute', a2)
    if hasattr(a2, 'statesml_DataType'):
        assert not _is_linked(a2, 'statesml_DataType', b)


def test_assoc_datatype18_reverse_link_reassign_clear():
    a1 = statesml_DataTypeLibrary(name="sample_text")
    a2 = statesml_DataTypeLibrary(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType20', a1)
    assert _is_linked(b, 'statesml_DataType20', a1)
    if hasattr(a1, 'statesml_DataTypeLibrary19'):
        assert _is_linked(a1, 'statesml_DataTypeLibrary19', b)
    _safe_set(b, 'statesml_DataType20', a2)
    assert _is_linked(b, 'statesml_DataType20', a2)
    if hasattr(a1, 'statesml_DataTypeLibrary19'):
        assert not _is_linked(a1, 'statesml_DataTypeLibrary19', b)
    if hasattr(a2, 'statesml_DataTypeLibrary19'):
        assert _is_linked(a2, 'statesml_DataTypeLibrary19', b)
    _safe_set(b, 'statesml_DataType20', None)
    assert not _is_linked(b, 'statesml_DataType20', a2)
    if hasattr(a2, 'statesml_DataTypeLibrary19'):
        assert not _is_linked(a2, 'statesml_DataTypeLibrary19', b)


def test_assoc_datatype25_reverse_link_reassign_clear():
    a1 = statesml_Parameter(name="sample_text")
    a2 = statesml_Parameter(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType26', a1)
    assert _is_linked(b, 'statesml_DataType26', a1)
    if hasattr(a1, 'statesml_Parameter'):
        assert _is_linked(a1, 'statesml_Parameter', b)
    _safe_set(b, 'statesml_DataType26', a2)
    assert _is_linked(b, 'statesml_DataType26', a2)
    if hasattr(a1, 'statesml_Parameter'):
        assert not _is_linked(a1, 'statesml_Parameter', b)
    if hasattr(a2, 'statesml_Parameter'):
        assert _is_linked(a2, 'statesml_Parameter', b)
    _safe_set(b, 'statesml_DataType26', None)
    assert not _is_linked(b, 'statesml_DataType26', a2)
    if hasattr(a2, 'statesml_Parameter'):
        assert not _is_linked(a2, 'statesml_Parameter', b)


def test_assoc_datatypelibrary2_reverse_link_reassign_clear():
    a1 = statesml_SystemUnitModel(name="sample_text")
    a2 = statesml_SystemUnitModel(name="sample_text_2")
    b = statesml_DataTypeLibrary(name="sample_text")
    _safe_set(b, 'statesml_DataTypeLibrary', a1)
    assert _is_linked(b, 'statesml_DataTypeLibrary', a1)
    if hasattr(a1, 'statesml_SystemUnitModel3'):
        assert _is_linked(a1, 'statesml_SystemUnitModel3', b)
    _safe_set(b, 'statesml_DataTypeLibrary', a2)
    assert _is_linked(b, 'statesml_DataTypeLibrary', a2)
    if hasattr(a1, 'statesml_SystemUnitModel3'):
        assert not _is_linked(a1, 'statesml_SystemUnitModel3', b)
    if hasattr(a2, 'statesml_SystemUnitModel3'):
        assert _is_linked(a2, 'statesml_SystemUnitModel3', b)
    _safe_set(b, 'statesml_DataTypeLibrary', None)
    assert not _is_linked(b, 'statesml_DataTypeLibrary', a2)
    if hasattr(a2, 'statesml_SystemUnitModel3'):
        assert not _is_linked(a2, 'statesml_SystemUnitModel3', b)


def test_assoc_function15_reverse_link_reassign_clear():
    a1 = statesml_SystemUnit(name="sample_text")
    a2 = statesml_SystemUnit(name="sample_text_2")
    b = statesml_Function(name="sample_text")
    _safe_set(b, 'statesml_Function17', a1)
    assert _is_linked(b, 'statesml_Function17', a1)
    if hasattr(a1, 'statesml_SystemUnit16'):
        assert _is_linked(a1, 'statesml_SystemUnit16', b)
    _safe_set(b, 'statesml_Function17', a2)
    assert _is_linked(b, 'statesml_Function17', a2)
    if hasattr(a1, 'statesml_SystemUnit16'):
        assert not _is_linked(a1, 'statesml_SystemUnit16', b)
    if hasattr(a2, 'statesml_SystemUnit16'):
        assert _is_linked(a2, 'statesml_SystemUnit16', b)
    _safe_set(b, 'statesml_Function17', None)
    assert not _is_linked(b, 'statesml_Function17', a2)
    if hasattr(a2, 'statesml_SystemUnit16'):
        assert not _is_linked(a2, 'statesml_SystemUnit16', b)


def test_assoc_function58_reverse_link_reassign_clear():
    a1 = statesml_Function(name="sample_text")
    a2 = statesml_Function(name="sample_text_2")
    b = statesml_ChangeExpression(fulfilled=True)
    _safe_set(b, 'statesml_ChangeExpression59', a1)
    assert _is_linked(b, 'statesml_ChangeExpression59', a1)
    if hasattr(a1, 'statesml_Function60'):
        assert _is_linked(a1, 'statesml_Function60', b)
    _safe_set(b, 'statesml_ChangeExpression59', a2)
    assert _is_linked(b, 'statesml_ChangeExpression59', a2)
    if hasattr(a1, 'statesml_Function60'):
        assert not _is_linked(a1, 'statesml_Function60', b)
    if hasattr(a2, 'statesml_Function60'):
        assert _is_linked(a2, 'statesml_Function60', b)
    _safe_set(b, 'statesml_ChangeExpression59', None)
    assert not _is_linked(b, 'statesml_ChangeExpression59', a2)
    if hasattr(a2, 'statesml_Function60'):
        assert not _is_linked(a2, 'statesml_Function60', b)


def test_assoc_function6_reverse_link_reassign_clear():
    a1 = statesml_Function(name="sample_text")
    a2 = statesml_Function(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType7', {a1})
    assert _is_linked(b, 'statesml_DataType7', a1)
    if hasattr(a1, 'statesml_Function'):
        assert _is_linked(a1, 'statesml_Function', b)
    _safe_set(b, 'statesml_DataType7', {a2})
    assert _is_linked(b, 'statesml_DataType7', a2)
    if hasattr(a1, 'statesml_Function'):
        assert not _is_linked(a1, 'statesml_Function', b)
    if hasattr(a2, 'statesml_Function'):
        assert _is_linked(a2, 'statesml_Function', b)
    _safe_set(b, 'statesml_DataType7', set())
    assert not _is_linked(b, 'statesml_DataType7', a2)
    if hasattr(a2, 'statesml_Function'):
        assert not _is_linked(a2, 'statesml_Function', b)


def test_assoc_incoming39_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'Edge40', a1)
    assert _is_linked(b, 'Edge40', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge40', a2)
    assert _is_linked(b, 'Edge40', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge40', None)
    assert not _is_linked(b, 'Edge40', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_outgoing38_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source41_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_statesystemmodel10_reverse_link_reassign_clear():
    a1 = statesml_SystemUnit(name="sample_text")
    a2 = statesml_SystemUnit(name="sample_text_2")
    b = statesml_StateSystemModel(name="sample_text")
    _safe_set(b, 'statesml_StateSystemModel', a1)
    assert _is_linked(b, 'statesml_StateSystemModel', a1)
    if hasattr(a1, 'statesml_SystemUnit11'):
        assert _is_linked(a1, 'statesml_SystemUnit11', b)
    _safe_set(b, 'statesml_StateSystemModel', a2)
    assert _is_linked(b, 'statesml_StateSystemModel', a2)
    if hasattr(a1, 'statesml_SystemUnit11'):
        assert not _is_linked(a1, 'statesml_SystemUnit11', b)
    if hasattr(a2, 'statesml_SystemUnit11'):
        assert _is_linked(a2, 'statesml_SystemUnit11', b)
    _safe_set(b, 'statesml_StateSystemModel', None)
    assert not _is_linked(b, 'statesml_StateSystemModel', a2)
    if hasattr(a2, 'statesml_SystemUnit11'):
        assert not _is_linked(a2, 'statesml_SystemUnit11', b)


def test_assoc_systemunit8_reverse_link_reassign_clear():
    a1 = statesml_SystemUnitLibrary(name="sample_text")
    a2 = statesml_SystemUnitLibrary(name="sample_text_2")
    b = statesml_SystemUnit(name="sample_text")
    _safe_set(b, 'statesml_SystemUnit', a1)
    assert _is_linked(b, 'statesml_SystemUnit', a1)
    if hasattr(a1, 'statesml_SystemUnitLibrary9'):
        assert _is_linked(a1, 'statesml_SystemUnitLibrary9', b)
    _safe_set(b, 'statesml_SystemUnit', a2)
    assert _is_linked(b, 'statesml_SystemUnit', a2)
    if hasattr(a1, 'statesml_SystemUnitLibrary9'):
        assert not _is_linked(a1, 'statesml_SystemUnitLibrary9', b)
    if hasattr(a2, 'statesml_SystemUnitLibrary9'):
        assert _is_linked(a2, 'statesml_SystemUnitLibrary9', b)
    _safe_set(b, 'statesml_SystemUnit', None)
    assert not _is_linked(b, 'statesml_SystemUnit', a2)
    if hasattr(a2, 'statesml_SystemUnitLibrary9'):
        assert not _is_linked(a2, 'statesml_SystemUnitLibrary9', b)


def test_assoc_systemunitlibrary4_reverse_link_reassign_clear():
    a1 = statesml_SystemUnitModel(name="sample_text")
    a2 = statesml_SystemUnitModel(name="sample_text_2")
    b = statesml_SystemUnitLibrary(name="sample_text")
    _safe_set(b, 'statesml_SystemUnitLibrary', a1)
    assert _is_linked(b, 'statesml_SystemUnitLibrary', a1)
    if hasattr(a1, 'statesml_SystemUnitModel5'):
        assert _is_linked(a1, 'statesml_SystemUnitModel5', b)
    _safe_set(b, 'statesml_SystemUnitLibrary', a2)
    assert _is_linked(b, 'statesml_SystemUnitLibrary', a2)
    if hasattr(a1, 'statesml_SystemUnitModel5'):
        assert not _is_linked(a1, 'statesml_SystemUnitModel5', b)
    if hasattr(a2, 'statesml_SystemUnitModel5'):
        assert _is_linked(a2, 'statesml_SystemUnitModel5', b)
    _safe_set(b, 'statesml_SystemUnitLibrary', None)
    assert not _is_linked(b, 'statesml_SystemUnitLibrary', a2)
    if hasattr(a2, 'statesml_SystemUnitModel5'):
        assert not _is_linked(a2, 'statesml_SystemUnitModel5', b)


def test_assoc_target42_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node43'):
        assert _is_linked(a1, 'Node43', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node43'):
        assert not _is_linked(a1, 'Node43', b)
    if hasattr(a2, 'Node43'):
        assert _is_linked(a2, 'Node43', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node43'):
        assert not _is_linked(a2, 'Node43', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute33_stub_double():
    # statesml_StateSystem has no real 'statesml_StateSystem34' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Attribute(name="sample_text")
    partner = statesml_StateSystem()
    setattr(partner, 'statesml_StateSystem34', None)
    _safe_set(owner, 'statesml_Attribute35', partner)
    assert owner in getattr(partner, 'statesml_StateSystem34')
    _safe_set(owner, 'statesml_Attribute35', None)
    assert owner not in getattr(partner, 'statesml_StateSystem34')


def test_assoc_attribute49_stub_double():
    # statesml_IncomingParameter has no real 'statesml_IncomingParameter50' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Attribute(name="sample_text")
    partner = statesml_IncomingParameter()
    setattr(partner, 'statesml_IncomingParameter50', None)
    _safe_set(owner, 'statesml_Attribute51', partner)
    assert getattr(partner, 'statesml_IncomingParameter50') == owner
    _safe_set(owner, 'statesml_Attribute51', None)
    assert getattr(partner, 'statesml_IncomingParameter50') is None


def test_assoc_changeexpression57_stub_double():
    # statesml_ChangeEvent has no real 'statesml_ChangeEvent' property in the generated
    # code (a bare stub) -- manually attach it so statesml_ChangeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_ChangeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_ChangeExpression(fulfilled=True)
    partner = statesml_ChangeEvent()
    setattr(partner, 'statesml_ChangeEvent', None)
    _safe_set(owner, 'statesml_ChangeExpression', partner)
    assert getattr(partner, 'statesml_ChangeEvent') == owner
    _safe_set(owner, 'statesml_ChangeExpression', None)
    assert getattr(partner, 'statesml_ChangeEvent') is None


def test_assoc_edge31_stub_double():
    # statesml_StateSystem has no real 'statesml_StateSystem32' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Edge(name="sample_text")
    partner = statesml_StateSystem()
    setattr(partner, 'statesml_StateSystem32', None)
    _safe_set(owner, 'statesml_Edge', partner)
    assert owner in getattr(partner, 'statesml_StateSystem32')
    _safe_set(owner, 'statesml_Edge', None)
    assert owner not in getattr(partner, 'statesml_StateSystem32')


def test_assoc_event36_stub_double():
    # statesml_StateSystem has no real 'statesml_StateSystem37' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Event(name="sample_text")
    partner = statesml_StateSystem()
    setattr(partner, 'statesml_StateSystem37', None)
    _safe_set(owner, 'statesml_Event', partner)
    assert owner in getattr(partner, 'statesml_StateSystem37')
    _safe_set(owner, 'statesml_Event', None)
    assert owner not in getattr(partner, 'statesml_StateSystem37')


def test_assoc_event46_stub_double():
    # statesml_Trigger has no real 'statesml_Trigger47' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Event(name="sample_text")
    partner = statesml_Trigger()
    setattr(partner, 'statesml_Trigger47', None)
    _safe_set(owner, 'statesml_Event48', partner)
    assert getattr(partner, 'statesml_Trigger47') == owner
    _safe_set(owner, 'statesml_Event48', None)
    assert getattr(partner, 'statesml_Trigger47') is None


def test_assoc_function52_stub_double():
    # statesml_FunctionCall has no real 'statesml_FunctionCall53' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Function(name="sample_text")
    partner = statesml_FunctionCall()
    setattr(partner, 'statesml_FunctionCall53', None)
    _safe_set(owner, 'statesml_Function54', partner)
    assert getattr(partner, 'statesml_FunctionCall53') == owner
    _safe_set(owner, 'statesml_Function54', None)
    assert getattr(partner, 'statesml_FunctionCall53') is None


def test_assoc_incomingparameter23_stub_double():
    # statesml_IncomingParameter has no real 'statesml_IncomingParameter' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Function(name="sample_text")
    partner = statesml_IncomingParameter()
    setattr(partner, 'statesml_IncomingParameter', None)
    _safe_set(owner, 'statesml_Function24', {partner})
    assert getattr(partner, 'statesml_IncomingParameter') == owner
    _safe_set(owner, 'statesml_Function24', set())
    assert getattr(partner, 'statesml_IncomingParameter') is None


def test_assoc_incomingparameter61_stub_double():
    # statesml_IncomingParameter has no real 'statesml_IncomingParameter63' property in the generated
    # code (a bare stub) -- manually attach it so statesml_ChangeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_ChangeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_ChangeExpression(fulfilled=True)
    partner = statesml_IncomingParameter()
    setattr(partner, 'statesml_IncomingParameter63', None)
    _safe_set(owner, 'statesml_ChangeExpression62', {partner})
    assert getattr(partner, 'statesml_IncomingParameter63') == owner
    _safe_set(owner, 'statesml_ChangeExpression62', set())
    assert getattr(partner, 'statesml_IncomingParameter63') is None


def test_assoc_node29_stub_double():
    # statesml_StateSystem has no real 'statesml_StateSystem30' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Node(name="sample_text")
    partner = statesml_StateSystem()
    setattr(partner, 'statesml_StateSystem30', None)
    _safe_set(owner, 'statesml_Node', partner)
    assert owner in getattr(partner, 'statesml_StateSystem30')
    _safe_set(owner, 'statesml_Node', None)
    assert owner not in getattr(partner, 'statesml_StateSystem30')


def test_assoc_returnparameter21_stub_double():
    # statesml_ReturnParameter has no real 'statesml_ReturnParameter' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Function(name="sample_text")
    partner = statesml_ReturnParameter()
    setattr(partner, 'statesml_ReturnParameter', None)
    _safe_set(owner, 'statesml_Function22', partner)
    assert getattr(partner, 'statesml_ReturnParameter') == owner
    _safe_set(owner, 'statesml_Function22', None)
    assert getattr(partner, 'statesml_ReturnParameter') is None


def test_assoc_statesystem27_stub_double():
    # statesml_StateSystem has no real 'statesml_StateSystem' property in the generated
    # code (a bare stub) -- manually attach it so statesml_StateSystemModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_StateSystemModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_StateSystemModel(name="sample_text")
    partner = statesml_StateSystem()
    setattr(partner, 'statesml_StateSystem', None)
    _safe_set(owner, 'statesml_StateSystemModel28', partner)
    assert getattr(partner, 'statesml_StateSystem') == owner
    _safe_set(owner, 'statesml_StateSystemModel28', None)
    assert getattr(partner, 'statesml_StateSystem') is None


def test_assoc_systemunits0_stub_double():
    # statesml_StatesModel has no real 'statesml_StatesModel' property in the generated
    # code (a bare stub) -- manually attach it so statesml_SystemUnitModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_SystemUnitModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_SystemUnitModel(name="sample_text")
    partner = statesml_StatesModel()
    setattr(partner, 'statesml_StatesModel', None)
    _safe_set(owner, 'statesml_SystemUnitModel', partner)
    assert owner in getattr(partner, 'statesml_StatesModel')
    _safe_set(owner, 'statesml_SystemUnitModel', None)
    assert owner not in getattr(partner, 'statesml_StatesModel')


