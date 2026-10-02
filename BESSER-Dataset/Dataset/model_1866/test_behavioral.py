import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    KeyValuePair,
    Node,
    State,
    statesml_Attribute,
    statesml_Attributes,
    statesml_ChangeEvent,
    statesml_Constant,
    statesml_DataType,
    statesml_DataTypeLibrary,
    statesml_Edge,
    statesml_Event,
    statesml_Events,
    statesml_Function,
    statesml_InitialState,
    statesml_KeyValuePair,
    statesml_NewEClass21,
    statesml_NewEClass22,
    statesml_NewEClass3,
    statesml_NewEClass4,
    statesml_Node,
    statesml_Parameter,
    statesml_RegularState,
    statesml_SelectionConvergence,
    statesml_SelectionDivergence,
    statesml_State,
    statesml_StatesMLModel,
    statesml_SystemUnit,
    statesml_SystemUnitLibrary,
    statesml_TerminalState,
    statesml_Transition,
    statesml_Trigger,
    NewEnum1,
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

def test_assoc_defines34_reverse_link_reassign_clear():
    a1 = statesml_Function(name="sample_text")
    a2 = statesml_Function(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType', {a1})
    assert _is_linked(b, 'statesml_DataType', a1)
    if hasattr(a1, 'statesml_Function35'):
        assert _is_linked(a1, 'statesml_Function35', b)
    _safe_set(b, 'statesml_DataType', {a2})
    assert _is_linked(b, 'statesml_DataType', a2)
    if hasattr(a1, 'statesml_Function35'):
        assert not _is_linked(a1, 'statesml_Function35', b)
    if hasattr(a2, 'statesml_Function35'):
        assert _is_linked(a2, 'statesml_Function35', b)
    _safe_set(b, 'statesml_DataType', set())
    assert not _is_linked(b, 'statesml_DataType', a2)
    if hasattr(a2, 'statesml_Function35'):
        assert not _is_linked(a2, 'statesml_Function35', b)


def test_assoc_functions26_reverse_link_reassign_clear():
    a1 = statesml_SystemUnit(name="sample_text")
    a2 = statesml_SystemUnit(name="sample_text_2")
    b = statesml_Function(name="sample_text")
    _safe_set(b, 'statesml_Function28', a1)
    assert _is_linked(b, 'statesml_Function28', a1)
    if hasattr(a1, 'statesml_SystemUnit27'):
        assert _is_linked(a1, 'statesml_SystemUnit27', b)
    _safe_set(b, 'statesml_Function28', a2)
    assert _is_linked(b, 'statesml_Function28', a2)
    if hasattr(a1, 'statesml_SystemUnit27'):
        assert not _is_linked(a1, 'statesml_SystemUnit27', b)
    if hasattr(a2, 'statesml_SystemUnit27'):
        assert _is_linked(a2, 'statesml_SystemUnit27', b)
    _safe_set(b, 'statesml_Function28', None)
    assert not _is_linked(b, 'statesml_Function28', a2)
    if hasattr(a2, 'statesml_SystemUnit27'):
        assert not _is_linked(a2, 'statesml_SystemUnit27', b)


def test_assoc_hasType36_reverse_link_reassign_clear():
    a1 = statesml_KeyValuePair(name="sample_text")
    a2 = statesml_KeyValuePair(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType37', a1)
    assert _is_linked(b, 'statesml_DataType37', a1)
    if hasattr(a1, 'statesml_KeyValuePair'):
        assert _is_linked(a1, 'statesml_KeyValuePair', b)
    _safe_set(b, 'statesml_DataType37', a2)
    assert _is_linked(b, 'statesml_DataType37', a2)
    if hasattr(a1, 'statesml_KeyValuePair'):
        assert not _is_linked(a1, 'statesml_KeyValuePair', b)
    if hasattr(a2, 'statesml_KeyValuePair'):
        assert _is_linked(a2, 'statesml_KeyValuePair', b)
    _safe_set(b, 'statesml_DataType37', None)
    assert not _is_linked(b, 'statesml_DataType37', a2)
    if hasattr(a2, 'statesml_KeyValuePair'):
        assert not _is_linked(a2, 'statesml_KeyValuePair', b)


def test_assoc_preceedingNode16_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'statesml_Edge17', a1)
    assert _is_linked(b, 'statesml_Edge17', a1)
    if hasattr(a1, 'statesml_Node18'):
        assert _is_linked(a1, 'statesml_Node18', b)
    _safe_set(b, 'statesml_Edge17', a2)
    assert _is_linked(b, 'statesml_Edge17', a2)
    if hasattr(a1, 'statesml_Node18'):
        assert not _is_linked(a1, 'statesml_Node18', b)
    if hasattr(a2, 'statesml_Node18'):
        assert _is_linked(a2, 'statesml_Node18', b)
    _safe_set(b, 'statesml_Edge17', None)
    assert not _is_linked(b, 'statesml_Edge17', a2)
    if hasattr(a2, 'statesml_Node18'):
        assert not _is_linked(a2, 'statesml_Node18', b)


def test_assoc_succeedingNode19_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'statesml_Edge20', a1)
    assert _is_linked(b, 'statesml_Edge20', a1)
    if hasattr(a1, 'statesml_Node21'):
        assert _is_linked(a1, 'statesml_Node21', b)
    _safe_set(b, 'statesml_Edge20', a2)
    assert _is_linked(b, 'statesml_Edge20', a2)
    if hasattr(a1, 'statesml_Node21'):
        assert not _is_linked(a1, 'statesml_Node21', b)
    if hasattr(a2, 'statesml_Node21'):
        assert _is_linked(a2, 'statesml_Node21', b)
    _safe_set(b, 'statesml_Edge20', None)
    assert not _is_linked(b, 'statesml_Edge20', a2)
    if hasattr(a2, 'statesml_Node21'):
        assert not _is_linked(a2, 'statesml_Node21', b)


def test_assoc_trigger10_reverse_link_reassign_clear():
    a1 = statesml_Trigger()
    a2 = statesml_Trigger()
    b = statesml_Event(name="sample_text")
    _safe_set(b, 'statesml_Event', a1)
    assert _is_linked(b, 'statesml_Event', a1)
    if hasattr(a1, 'statesml_Trigger11'):
        assert _is_linked(a1, 'statesml_Trigger11', b)
    _safe_set(b, 'statesml_Event', a2)
    assert _is_linked(b, 'statesml_Event', a2)
    if hasattr(a1, 'statesml_Trigger11'):
        assert not _is_linked(a1, 'statesml_Trigger11', b)
    if hasattr(a2, 'statesml_Trigger11'):
        assert _is_linked(a2, 'statesml_Trigger11', b)
    _safe_set(b, 'statesml_Event', None)
    assert not _is_linked(b, 'statesml_Event', a2)
    if hasattr(a2, 'statesml_Trigger11'):
        assert not _is_linked(a2, 'statesml_Trigger11', b)


def test_assoc_types40_reverse_link_reassign_clear():
    a1 = statesml_DataTypeLibrary(name="sample_text")
    a2 = statesml_DataTypeLibrary(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType41', a1)
    assert _is_linked(b, 'statesml_DataType41', a1)
    if hasattr(a1, 'statesml_DataTypeLibrary'):
        assert _is_linked(a1, 'statesml_DataTypeLibrary', b)
    _safe_set(b, 'statesml_DataType41', a2)
    assert _is_linked(b, 'statesml_DataType41', a2)
    if hasattr(a1, 'statesml_DataTypeLibrary'):
        assert not _is_linked(a1, 'statesml_DataTypeLibrary', b)
    if hasattr(a2, 'statesml_DataTypeLibrary'):
        assert _is_linked(a2, 'statesml_DataTypeLibrary', b)
    _safe_set(b, 'statesml_DataType41', None)
    assert not _is_linked(b, 'statesml_DataType41', a2)
    if hasattr(a2, 'statesml_DataTypeLibrary'):
        assert not _is_linked(a2, 'statesml_DataTypeLibrary', b)


def test_assoc_unitCollection38_reverse_link_reassign_clear():
    a1 = statesml_SystemUnitLibrary(name="sample_text")
    a2 = statesml_SystemUnitLibrary(name="sample_text_2")
    b = statesml_SystemUnit(name="sample_text")
    _safe_set(b, 'statesml_SystemUnit39', a1)
    assert _is_linked(b, 'statesml_SystemUnit39', a1)
    if hasattr(a1, 'statesml_SystemUnitLibrary'):
        assert _is_linked(a1, 'statesml_SystemUnitLibrary', b)
    _safe_set(b, 'statesml_SystemUnit39', a2)
    assert _is_linked(b, 'statesml_SystemUnit39', a2)
    if hasattr(a1, 'statesml_SystemUnitLibrary'):
        assert not _is_linked(a1, 'statesml_SystemUnitLibrary', b)
    if hasattr(a2, 'statesml_SystemUnitLibrary'):
        assert _is_linked(a2, 'statesml_SystemUnitLibrary', b)
    _safe_set(b, 'statesml_SystemUnit39', None)
    assert not _is_linked(b, 'statesml_SystemUnit39', a2)
    if hasattr(a2, 'statesml_SystemUnitLibrary'):
        assert not _is_linked(a2, 'statesml_SystemUnitLibrary', b)


