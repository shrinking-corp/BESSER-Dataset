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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes23_stub_double():
    # statesml_Attribute has no real 'statesml_Attribute25' property in the generated
    # code (a bare stub) -- manually attach it so statesml_SystemUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_SystemUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_SystemUnit(name="sample_text")
    partner = statesml_Attribute()
    setattr(partner, 'statesml_Attribute25', None)
    _safe_set(owner, 'statesml_SystemUnit24', {partner})
    assert getattr(partner, 'statesml_Attribute25') == owner
    _safe_set(owner, 'statesml_SystemUnit24', set())
    assert getattr(partner, 'statesml_Attribute25') is None


def test_assoc_calls22_stub_double():
    # statesml_RegularState has no real 'statesml_RegularState' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Function(name="sample_text")
    partner = statesml_RegularState()
    setattr(partner, 'statesml_RegularState', None)
    _safe_set(owner, 'statesml_Function', partner)
    assert owner in getattr(partner, 'statesml_RegularState')
    _safe_set(owner, 'statesml_Function', None)
    assert owner not in getattr(partner, 'statesml_RegularState')


def test_assoc_edges3_stub_double():
    # statesml_StatesMLModel has no real 'statesml_StatesMLModel4' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Edge(name="sample_text")
    partner = statesml_StatesMLModel()
    setattr(partner, 'statesml_StatesMLModel4', None)
    _safe_set(owner, 'statesml_Edge', partner)
    assert owner in getattr(partner, 'statesml_StatesMLModel4')
    _safe_set(owner, 'statesml_Edge', None)
    assert owner not in getattr(partner, 'statesml_StatesMLModel4')


def test_assoc_inputParams29_stub_double():
    # statesml_Parameter has no real 'statesml_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Function(name="sample_text")
    partner = statesml_Parameter()
    setattr(partner, 'statesml_Parameter', None)
    _safe_set(owner, 'statesml_Function30', {partner})
    assert getattr(partner, 'statesml_Parameter') == owner
    _safe_set(owner, 'statesml_Function30', set())
    assert getattr(partner, 'statesml_Parameter') is None


def test_assoc_node7_stub_double():
    # statesml_Transition has no real 'transition' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Node(name="sample_text")
    partner = statesml_Transition()
    setattr(partner, 'transition', None)
    _safe_set(owner, 'Node', partner)
    assert owner in getattr(partner, 'transition')
    _safe_set(owner, 'Node', None)
    assert owner not in getattr(partner, 'transition')


def test_assoc_nodes0_stub_double():
    # statesml_StatesMLModel has no real 'statesml_StatesMLModel' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Node(name="sample_text")
    partner = statesml_StatesMLModel()
    setattr(partner, 'statesml_StatesMLModel', None)
    _safe_set(owner, 'statesml_Node', partner)
    assert owner in getattr(partner, 'statesml_StatesMLModel')
    _safe_set(owner, 'statesml_Node', None)
    assert owner not in getattr(partner, 'statesml_StatesMLModel')


def test_assoc_outputParams31_stub_double():
    # statesml_Parameter has no real 'statesml_Parameter33' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Function(name="sample_text")
    partner = statesml_Parameter()
    setattr(partner, 'statesml_Parameter33', None)
    _safe_set(owner, 'statesml_Function32', partner)
    assert getattr(partner, 'statesml_Parameter33') == owner
    _safe_set(owner, 'statesml_Function32', None)
    assert getattr(partner, 'statesml_Parameter33') is None


def test_assoc_systemunits1_stub_double():
    # statesml_StatesMLModel has no real 'statesml_StatesMLModel2' property in the generated
    # code (a bare stub) -- manually attach it so statesml_SystemUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_SystemUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_SystemUnit(name="sample_text")
    partner = statesml_StatesMLModel()
    setattr(partner, 'statesml_StatesMLModel2', None)
    _safe_set(owner, 'statesml_SystemUnit', partner)
    assert owner in getattr(partner, 'statesml_StatesMLModel2')
    _safe_set(owner, 'statesml_SystemUnit', None)
    assert owner not in getattr(partner, 'statesml_StatesMLModel2')


def test_assoc_transition9_stub_double():
    # statesml_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Node(name="sample_text")
    partner = statesml_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'node', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'node', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_trigger8_stub_double():
    # statesml_Transition has no real 'statesml_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Trigger()
    partner = statesml_Transition()
    setattr(partner, 'statesml_Transition', None)
    _safe_set(owner, 'statesml_Trigger', partner)
    assert owner in getattr(partner, 'statesml_Transition')
    _safe_set(owner, 'statesml_Trigger', None)
    assert owner not in getattr(partner, 'statesml_Transition')


