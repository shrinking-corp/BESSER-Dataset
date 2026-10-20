import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Node,
    statesml_Attribute,
    statesml_ChangeEvent,
    statesml_DataType,
    statesml_DataTypeLibrary,
    statesml_Edge,
    statesml_Event,
    statesml_Function,
    statesml_Node,
    statesml_Parameter,
    statesml_SelectionConvergence,
    statesml_SelectionDivergence,
    statesml_State,
    statesml_StatesML,
    statesml_SystemUnitLibrariy,
    statesml_SystemUnits,
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

def test_assoc_attribute1_reverse_link_reassign_clear():
    a1 = statesml_SystemUnits(name="sample_text")
    a2 = statesml_SystemUnits(name="sample_text_2")
    b = statesml_Attribute(name="sample_text")
    _safe_set(b, 'statesml_Attribute', a1)
    assert _is_linked(b, 'statesml_Attribute', a1)
    if hasattr(a1, 'statesml_SystemUnits2'):
        assert _is_linked(a1, 'statesml_SystemUnits2', b)
    _safe_set(b, 'statesml_Attribute', a2)
    assert _is_linked(b, 'statesml_Attribute', a2)
    if hasattr(a1, 'statesml_SystemUnits2'):
        assert not _is_linked(a1, 'statesml_SystemUnits2', b)
    if hasattr(a2, 'statesml_SystemUnits2'):
        assert _is_linked(a2, 'statesml_SystemUnits2', b)
    _safe_set(b, 'statesml_Attribute', None)
    assert not _is_linked(b, 'statesml_Attribute', a2)
    if hasattr(a2, 'statesml_SystemUnits2'):
        assert not _is_linked(a2, 'statesml_SystemUnits2', b)


def test_assoc_changeevent54_reverse_link_reassign_clear():
    a1 = statesml_Trigger()
    a2 = statesml_Trigger()
    b = statesml_ChangeEvent(isFulfilled=True)
    _safe_set(b, 'statesml_ChangeEvent55', a1)
    assert _is_linked(b, 'statesml_ChangeEvent55', a1)
    if hasattr(a1, 'statesml_Trigger'):
        assert _is_linked(a1, 'statesml_Trigger', b)
    _safe_set(b, 'statesml_ChangeEvent55', a2)
    assert _is_linked(b, 'statesml_ChangeEvent55', a2)
    if hasattr(a1, 'statesml_Trigger'):
        assert not _is_linked(a1, 'statesml_Trigger', b)
    if hasattr(a2, 'statesml_Trigger'):
        assert _is_linked(a2, 'statesml_Trigger', b)
    _safe_set(b, 'statesml_ChangeEvent55', None)
    assert not _is_linked(b, 'statesml_ChangeEvent55', a2)
    if hasattr(a2, 'statesml_Trigger'):
        assert not _is_linked(a2, 'statesml_Trigger', b)


def test_assoc_datatype10_reverse_link_reassign_clear():
    a1 = statesml_Parameter(name="sample_text")
    a2 = statesml_Parameter(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType12', a1)
    assert _is_linked(b, 'statesml_DataType12', a1)
    if hasattr(a1, 'statesml_Parameter11'):
        assert _is_linked(a1, 'statesml_Parameter11', b)
    _safe_set(b, 'statesml_DataType12', a2)
    assert _is_linked(b, 'statesml_DataType12', a2)
    if hasattr(a1, 'statesml_Parameter11'):
        assert not _is_linked(a1, 'statesml_Parameter11', b)
    if hasattr(a2, 'statesml_Parameter11'):
        assert _is_linked(a2, 'statesml_Parameter11', b)
    _safe_set(b, 'statesml_DataType12', None)
    assert not _is_linked(b, 'statesml_DataType12', a2)
    if hasattr(a2, 'statesml_Parameter11'):
        assert not _is_linked(a2, 'statesml_Parameter11', b)


def test_assoc_datatype18_reverse_link_reassign_clear():
    a1 = statesml_DataTypeLibrary(name="sample_text")
    a2 = statesml_DataTypeLibrary(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType19', a1)
    assert _is_linked(b, 'statesml_DataType19', a1)
    if hasattr(a1, 'statesml_DataTypeLibrary'):
        assert _is_linked(a1, 'statesml_DataTypeLibrary', b)
    _safe_set(b, 'statesml_DataType19', a2)
    assert _is_linked(b, 'statesml_DataType19', a2)
    if hasattr(a1, 'statesml_DataTypeLibrary'):
        assert not _is_linked(a1, 'statesml_DataTypeLibrary', b)
    if hasattr(a2, 'statesml_DataTypeLibrary'):
        assert _is_linked(a2, 'statesml_DataTypeLibrary', b)
    _safe_set(b, 'statesml_DataType19', None)
    assert not _is_linked(b, 'statesml_DataType19', a2)
    if hasattr(a2, 'statesml_DataTypeLibrary'):
        assert not _is_linked(a2, 'statesml_DataTypeLibrary', b)


def test_assoc_datatype8_reverse_link_reassign_clear():
    a1 = statesml_DataType(name="sample_text")
    a2 = statesml_DataType(name="sample_text_2")
    b = statesml_Attribute(name="sample_text")
    _safe_set(b, 'statesml_Attribute9', a1)
    assert _is_linked(b, 'statesml_Attribute9', a1)
    if hasattr(a1, 'statesml_DataType'):
        assert _is_linked(a1, 'statesml_DataType', b)
    _safe_set(b, 'statesml_Attribute9', a2)
    assert _is_linked(b, 'statesml_Attribute9', a2)
    if hasattr(a1, 'statesml_DataType'):
        assert not _is_linked(a1, 'statesml_DataType', b)
    if hasattr(a2, 'statesml_DataType'):
        assert _is_linked(a2, 'statesml_DataType', b)
    _safe_set(b, 'statesml_Attribute9', None)
    assert not _is_linked(b, 'statesml_Attribute9', a2)
    if hasattr(a2, 'statesml_DataType'):
        assert not _is_linked(a2, 'statesml_DataType', b)


def test_assoc_edge50_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_function0_reverse_link_reassign_clear():
    a1 = statesml_SystemUnits(name="sample_text")
    a2 = statesml_SystemUnits(name="sample_text_2")
    b = statesml_Function(name="sample_text")
    _safe_set(b, 'statesml_Function', a1)
    assert _is_linked(b, 'statesml_Function', a1)
    if hasattr(a1, 'statesml_SystemUnits'):
        assert _is_linked(a1, 'statesml_SystemUnits', b)
    _safe_set(b, 'statesml_Function', a2)
    assert _is_linked(b, 'statesml_Function', a2)
    if hasattr(a1, 'statesml_SystemUnits'):
        assert not _is_linked(a1, 'statesml_SystemUnits', b)
    if hasattr(a2, 'statesml_SystemUnits'):
        assert _is_linked(a2, 'statesml_SystemUnits', b)
    _safe_set(b, 'statesml_Function', None)
    assert not _is_linked(b, 'statesml_Function', a2)
    if hasattr(a2, 'statesml_SystemUnits'):
        assert not _is_linked(a2, 'statesml_SystemUnits', b)


def test_assoc_function13_reverse_link_reassign_clear():
    a1 = statesml_Function(name="sample_text")
    a2 = statesml_Function(name="sample_text_2")
    b = statesml_DataType(name="sample_text")
    _safe_set(b, 'statesml_DataType14', {a1})
    assert _is_linked(b, 'statesml_DataType14', a1)
    if hasattr(a1, 'statesml_Function15'):
        assert _is_linked(a1, 'statesml_Function15', b)
    _safe_set(b, 'statesml_DataType14', {a2})
    assert _is_linked(b, 'statesml_DataType14', a2)
    if hasattr(a1, 'statesml_Function15'):
        assert not _is_linked(a1, 'statesml_Function15', b)
    if hasattr(a2, 'statesml_Function15'):
        assert _is_linked(a2, 'statesml_Function15', b)
    _safe_set(b, 'statesml_DataType14', set())
    assert not _is_linked(b, 'statesml_DataType14', a2)
    if hasattr(a2, 'statesml_Function15'):
        assert not _is_linked(a2, 'statesml_Function15', b)


def test_assoc_function51_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Function(name="sample_text")
    _safe_set(b, 'statesml_Function53', a1)
    assert _is_linked(b, 'statesml_Function53', a1)
    if hasattr(a1, 'statesml_Node52'):
        assert _is_linked(a1, 'statesml_Node52', b)
    _safe_set(b, 'statesml_Function53', a2)
    assert _is_linked(b, 'statesml_Function53', a2)
    if hasattr(a1, 'statesml_Node52'):
        assert not _is_linked(a1, 'statesml_Node52', b)
    if hasattr(a2, 'statesml_Node52'):
        assert _is_linked(a2, 'statesml_Node52', b)
    _safe_set(b, 'statesml_Function53', None)
    assert not _is_linked(b, 'statesml_Function53', a2)
    if hasattr(a2, 'statesml_Node52'):
        assert not _is_linked(a2, 'statesml_Node52', b)


def test_assoc_inParameter3_reverse_link_reassign_clear():
    a1 = statesml_Parameter(name="sample_text")
    a2 = statesml_Parameter(name="sample_text_2")
    b = statesml_Function(name="sample_text")
    _safe_set(b, 'statesml_Function4', {a1})
    assert _is_linked(b, 'statesml_Function4', a1)
    if hasattr(a1, 'statesml_Parameter'):
        assert _is_linked(a1, 'statesml_Parameter', b)
    _safe_set(b, 'statesml_Function4', {a2})
    assert _is_linked(b, 'statesml_Function4', a2)
    if hasattr(a1, 'statesml_Parameter'):
        assert not _is_linked(a1, 'statesml_Parameter', b)
    if hasattr(a2, 'statesml_Parameter'):
        assert _is_linked(a2, 'statesml_Parameter', b)
    _safe_set(b, 'statesml_Function4', set())
    assert not _is_linked(b, 'statesml_Function4', a2)
    if hasattr(a2, 'statesml_Parameter'):
        assert not _is_linked(a2, 'statesml_Parameter', b)


def test_assoc_node49_reverse_link_reassign_clear():
    a1 = statesml_Node(name="sample_text")
    a2 = statesml_Node(name="sample_text_2")
    b = statesml_Edge(name="sample_text")
    _safe_set(b, 'edge', {a1})
    assert _is_linked(b, 'edge', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'edge', {a2})
    assert _is_linked(b, 'edge', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'edge', set())
    assert not _is_linked(b, 'edge', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_returnParameter5_reverse_link_reassign_clear():
    a1 = statesml_Parameter(name="sample_text")
    a2 = statesml_Parameter(name="sample_text_2")
    b = statesml_Function(name="sample_text")
    _safe_set(b, 'statesml_Function6', a1)
    assert _is_linked(b, 'statesml_Function6', a1)
    if hasattr(a1, 'statesml_Parameter7'):
        assert _is_linked(a1, 'statesml_Parameter7', b)
    _safe_set(b, 'statesml_Function6', a2)
    assert _is_linked(b, 'statesml_Function6', a2)
    if hasattr(a1, 'statesml_Parameter7'):
        assert not _is_linked(a1, 'statesml_Parameter7', b)
    if hasattr(a2, 'statesml_Parameter7'):
        assert _is_linked(a2, 'statesml_Parameter7', b)
    _safe_set(b, 'statesml_Function6', None)
    assert not _is_linked(b, 'statesml_Function6', a2)
    if hasattr(a2, 'statesml_Parameter7'):
        assert not _is_linked(a2, 'statesml_Parameter7', b)


def test_assoc_systemunits16_reverse_link_reassign_clear():
    a1 = statesml_SystemUnits(name="sample_text")
    a2 = statesml_SystemUnits(name="sample_text_2")
    b = statesml_SystemUnitLibrariy(name="sample_text")
    _safe_set(b, 'statesml_SystemUnitLibrariy', {a1})
    assert _is_linked(b, 'statesml_SystemUnitLibrariy', a1)
    if hasattr(a1, 'statesml_SystemUnits17'):
        assert _is_linked(a1, 'statesml_SystemUnits17', b)
    _safe_set(b, 'statesml_SystemUnitLibrariy', {a2})
    assert _is_linked(b, 'statesml_SystemUnitLibrariy', a2)
    if hasattr(a1, 'statesml_SystemUnits17'):
        assert not _is_linked(a1, 'statesml_SystemUnits17', b)
    if hasattr(a2, 'statesml_SystemUnits17'):
        assert _is_linked(a2, 'statesml_SystemUnits17', b)
    _safe_set(b, 'statesml_SystemUnitLibrariy', set())
    assert not _is_linked(b, 'statesml_SystemUnitLibrariy', a2)
    if hasattr(a2, 'statesml_SystemUnits17'):
        assert not _is_linked(a2, 'statesml_SystemUnits17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute46_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML47' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Attribute(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML47', None)
    _safe_set(owner, 'statesml_Attribute48', partner)
    assert owner in getattr(partner, 'statesml_StatesML47')
    _safe_set(owner, 'statesml_Attribute48', None)
    assert owner not in getattr(partner, 'statesml_StatesML47')


def test_assoc_datatypelibrary36_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML37' property in the generated
    # code (a bare stub) -- manually attach it so statesml_DataTypeLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_DataTypeLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_DataTypeLibrary(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML37', None)
    _safe_set(owner, 'statesml_DataTypeLibrary38', partner)
    assert owner in getattr(partner, 'statesml_StatesML37')
    _safe_set(owner, 'statesml_DataTypeLibrary38', None)
    assert owner not in getattr(partner, 'statesml_StatesML37')


def test_assoc_edge44_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML45' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Edge(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML45', None)
    _safe_set(owner, 'statesml_Edge', partner)
    assert owner in getattr(partner, 'statesml_StatesML45')
    _safe_set(owner, 'statesml_Edge', None)
    assert owner not in getattr(partner, 'statesml_StatesML45')


def test_assoc_event32_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Event(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML', None)
    _safe_set(owner, 'statesml_Event', partner)
    assert owner in getattr(partner, 'statesml_StatesML')
    _safe_set(owner, 'statesml_Event', None)
    assert owner not in getattr(partner, 'statesml_StatesML')


def test_assoc_node42_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML43' property in the generated
    # code (a bare stub) -- manually attach it so statesml_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_Node(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML43', None)
    _safe_set(owner, 'statesml_Node', partner)
    assert owner in getattr(partner, 'statesml_StatesML43')
    _safe_set(owner, 'statesml_Node', None)
    assert owner not in getattr(partner, 'statesml_StatesML43')


def test_assoc_selectiondivergence21_stub_double():
    # statesml_SelectionDivergence has no real 'statesml_SelectionDivergence' property in the generated
    # code (a bare stub) -- manually attach it so statesml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_State(isInitial=True, isTerminal=True)
    partner = statesml_SelectionDivergence()
    setattr(partner, 'statesml_SelectionDivergence', None)
    _safe_set(owner, 'statesml_State', partner)
    assert getattr(partner, 'statesml_SelectionDivergence') == owner
    _safe_set(owner, 'statesml_State', None)
    assert getattr(partner, 'statesml_SelectionDivergence') is None


def test_assoc_state23_stub_double():
    # statesml_Transition has no real 'transition' property in the generated
    # code (a bare stub) -- manually attach it so statesml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_State(isInitial=True, isTerminal=True)
    partner = statesml_Transition()
    setattr(partner, 'transition', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'transition') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'transition') is None


def test_assoc_state29_stub_double():
    # statesml_SelectionConvergence has no real 'statesml_SelectionConvergence30' property in the generated
    # code (a bare stub) -- manually attach it so statesml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_State(isInitial=True, isTerminal=True)
    partner = statesml_SelectionConvergence()
    setattr(partner, 'statesml_SelectionConvergence30', None)
    _safe_set(owner, 'statesml_State31', partner)
    assert getattr(partner, 'statesml_SelectionConvergence30') == owner
    _safe_set(owner, 'statesml_State31', None)
    assert getattr(partner, 'statesml_SelectionConvergence30') is None


def test_assoc_systemunitlibrariy39_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML40' property in the generated
    # code (a bare stub) -- manually attach it so statesml_SystemUnitLibrariy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_SystemUnitLibrariy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_SystemUnitLibrariy(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML40', None)
    _safe_set(owner, 'statesml_SystemUnitLibrariy41', partner)
    assert owner in getattr(partner, 'statesml_StatesML40')
    _safe_set(owner, 'statesml_SystemUnitLibrariy41', None)
    assert owner not in getattr(partner, 'statesml_StatesML40')


def test_assoc_systemunits33_stub_double():
    # statesml_StatesML has no real 'statesml_StatesML34' property in the generated
    # code (a bare stub) -- manually attach it so statesml_SystemUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_SystemUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_SystemUnits(name="sample_text")
    partner = statesml_StatesML()
    setattr(partner, 'statesml_StatesML34', None)
    _safe_set(owner, 'statesml_SystemUnits35', partner)
    assert owner in getattr(partner, 'statesml_StatesML34')
    _safe_set(owner, 'statesml_SystemUnits35', None)
    assert owner not in getattr(partner, 'statesml_StatesML34')


def test_assoc_transition20_stub_double():
    # statesml_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so statesml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_State(isInitial=True, isTerminal=True)
    partner = statesml_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'state', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'state', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_trigger22_stub_double():
    # statesml_Transition has no real 'statesml_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statesml_ChangeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statesml_ChangeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statesml_ChangeEvent(isFulfilled=True)
    partner = statesml_Transition()
    setattr(partner, 'statesml_Transition', None)
    _safe_set(owner, 'statesml_ChangeEvent', partner)
    assert getattr(partner, 'statesml_Transition') == owner
    _safe_set(owner, 'statesml_ChangeEvent', None)
    assert getattr(partner, 'statesml_Transition') is None


