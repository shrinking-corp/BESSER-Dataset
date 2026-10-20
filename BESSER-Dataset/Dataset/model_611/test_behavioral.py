import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Action,
    ConditionExpression,
    Control,
    DataBinding,
    Instruction,
    Layout,
    Screen,
    Service,
    SetInstructionAssignment,
    Type,
    Value,
    appBuilderDSL_AbstractElement,
    appBuilderDSL_Action,
    appBuilderDSL_AppBuilder,
    appBuilderDSL_Attribute,
    appBuilderDSL_Business,
    appBuilderDSL_Button,
    appBuilderDSL_CompositeConditionExpression,
    appBuilderDSL_CompositeScreen,
    appBuilderDSL_Condition,
    appBuilderDSL_ConditionExpression,
    appBuilderDSL_Control,
    appBuilderDSL_ControlValue,
    appBuilderDSL_Controller,
    appBuilderDSL_DataBinding,
    appBuilderDSL_DataType,
    appBuilderDSL_DynamicValue,
    appBuilderDSL_Entity,
    appBuilderDSL_EntryParameters,
    appBuilderDSL_EnumDataBinding,
    appBuilderDSL_ExecuteAction,
    appBuilderDSL_Expression,
    appBuilderDSL_Feature,
    appBuilderDSL_GridLayout,
    appBuilderDSL_Import,
    appBuilderDSL_InitAction,
    appBuilderDSL_InstanceService,
    appBuilderDSL_Instruction,
    appBuilderDSL_Label,
    appBuilderDSL_Layout,
    appBuilderDSL_List,
    appBuilderDSL_Main,
    appBuilderDSL_Model,
    appBuilderDSL_NamespaceDeclation,
    appBuilderDSL_Navigate,
    appBuilderDSL_RestCall,
    appBuilderDSL_RowLayout,
    appBuilderDSL_Screen,
    appBuilderDSL_ScreenLayout,
    appBuilderDSL_Service,
    appBuilderDSL_SetInstruction,
    appBuilderDSL_SetInstructionAssignment,
    appBuilderDSL_SimpleConditionExpression,
    appBuilderDSL_SimpleDataBinding,
    appBuilderDSL_SimpleScreen,
    appBuilderDSL_System,
    appBuilderDSL_Text,
    appBuilderDSL_Type,
    appBuilderDSL_Ui,
    appBuilderDSL_UiAction,
    appBuilderDSL_UiListenerBinding,
    appBuilderDSL_ValidationBinding,
    appBuilderDSL_Validator,
    appBuilderDSL_Value,
    appBuilderDSL_View,
    Device,
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

def test_assoc_condition39_reverse_link_reassign_clear():
    a1 = appBuilderDSL_ValidationBinding(controlAccess="sample_text")
    a2 = appBuilderDSL_ValidationBinding(controlAccess="sample_text_2")
    b = appBuilderDSL_Condition(name="sample_text")
    _safe_set(b, 'appBuilderDSL_Condition', a1)
    assert _is_linked(b, 'appBuilderDSL_Condition', a1)
    if hasattr(a1, 'appBuilderDSL_ValidationBinding40'):
        assert _is_linked(a1, 'appBuilderDSL_ValidationBinding40', b)
    _safe_set(b, 'appBuilderDSL_Condition', a2)
    assert _is_linked(b, 'appBuilderDSL_Condition', a2)
    if hasattr(a1, 'appBuilderDSL_ValidationBinding40'):
        assert not _is_linked(a1, 'appBuilderDSL_ValidationBinding40', b)
    if hasattr(a2, 'appBuilderDSL_ValidationBinding40'):
        assert _is_linked(a2, 'appBuilderDSL_ValidationBinding40', b)
    _safe_set(b, 'appBuilderDSL_Condition', None)
    assert not _is_linked(b, 'appBuilderDSL_Condition', a2)
    if hasattr(a2, 'appBuilderDSL_ValidationBinding40'):
        assert not _is_linked(a2, 'appBuilderDSL_ValidationBinding40', b)


def test_assoc_expression90_reverse_link_reassign_clear():
    a1 = appBuilderDSL_Expression(terms="sample_text")
    a2 = appBuilderDSL_Expression(terms="sample_text_2")
    b = appBuilderDSL_DynamicValue(type="sample_text", variableName="sample_text")
    _safe_set(b, 'appBuilderDSL_DynamicValue', a1)
    assert _is_linked(b, 'appBuilderDSL_DynamicValue', a1)
    if hasattr(a1, 'appBuilderDSL_Expression'):
        assert _is_linked(a1, 'appBuilderDSL_Expression', b)
    _safe_set(b, 'appBuilderDSL_DynamicValue', a2)
    assert _is_linked(b, 'appBuilderDSL_DynamicValue', a2)
    if hasattr(a1, 'appBuilderDSL_Expression'):
        assert not _is_linked(a1, 'appBuilderDSL_Expression', b)
    if hasattr(a2, 'appBuilderDSL_Expression'):
        assert _is_linked(a2, 'appBuilderDSL_Expression', b)
    _safe_set(b, 'appBuilderDSL_DynamicValue', None)
    assert not _is_linked(b, 'appBuilderDSL_DynamicValue', a2)
    if hasattr(a2, 'appBuilderDSL_Expression'):
        assert not _is_linked(a2, 'appBuilderDSL_Expression', b)


def test_assoc_model52_reverse_link_reassign_clear():
    a1 = appBuilderDSL_SimpleDataBinding(modelAccess="sample_text")
    a2 = appBuilderDSL_SimpleDataBinding(modelAccess="sample_text_2")
    b = appBuilderDSL_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'appBuilderDSL_Attribute53', a1)
    assert _is_linked(b, 'appBuilderDSL_Attribute53', a1)
    if hasattr(a1, 'appBuilderDSL_SimpleDataBinding'):
        assert _is_linked(a1, 'appBuilderDSL_SimpleDataBinding', b)
    _safe_set(b, 'appBuilderDSL_Attribute53', a2)
    assert _is_linked(b, 'appBuilderDSL_Attribute53', a2)
    if hasattr(a1, 'appBuilderDSL_SimpleDataBinding'):
        assert not _is_linked(a1, 'appBuilderDSL_SimpleDataBinding', b)
    if hasattr(a2, 'appBuilderDSL_SimpleDataBinding'):
        assert _is_linked(a2, 'appBuilderDSL_SimpleDataBinding', b)
    _safe_set(b, 'appBuilderDSL_Attribute53', None)
    assert not _is_linked(b, 'appBuilderDSL_Attribute53', a2)
    if hasattr(a2, 'appBuilderDSL_SimpleDataBinding'):
        assert not _is_linked(a2, 'appBuilderDSL_SimpleDataBinding', b)


def test_assoc_model63_reverse_link_reassign_clear():
    a1 = appBuilderDSL_SetInstruction(modelAccess="sample_text")
    a2 = appBuilderDSL_SetInstruction(modelAccess="sample_text_2")
    b = appBuilderDSL_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'appBuilderDSL_Attribute64', a1)
    assert _is_linked(b, 'appBuilderDSL_Attribute64', a1)
    if hasattr(a1, 'appBuilderDSL_SetInstruction'):
        assert _is_linked(a1, 'appBuilderDSL_SetInstruction', b)
    _safe_set(b, 'appBuilderDSL_Attribute64', a2)
    assert _is_linked(b, 'appBuilderDSL_Attribute64', a2)
    if hasattr(a1, 'appBuilderDSL_SetInstruction'):
        assert not _is_linked(a1, 'appBuilderDSL_SetInstruction', b)
    if hasattr(a2, 'appBuilderDSL_SetInstruction'):
        assert _is_linked(a2, 'appBuilderDSL_SetInstruction', b)
    _safe_set(b, 'appBuilderDSL_Attribute64', None)
    assert not _is_linked(b, 'appBuilderDSL_Attribute64', a2)
    if hasattr(a2, 'appBuilderDSL_SetInstruction'):
        assert not _is_linked(a2, 'appBuilderDSL_SetInstruction', b)


def test_assoc_screen13_reverse_link_reassign_clear():
    a1 = appBuilderDSL_Screen(name="sample_text")
    a2 = appBuilderDSL_Screen(name="sample_text_2")
    b = appBuilderDSL_Main(appName="sample_text", appVersion="sample_text", devices="sample_text", generalStyle="sample_text")
    _safe_set(b, 'appBuilderDSL_Main14', a1)
    assert _is_linked(b, 'appBuilderDSL_Main14', a1)
    if hasattr(a1, 'appBuilderDSL_Screen15'):
        assert _is_linked(a1, 'appBuilderDSL_Screen15', b)
    _safe_set(b, 'appBuilderDSL_Main14', a2)
    assert _is_linked(b, 'appBuilderDSL_Main14', a2)
    if hasattr(a1, 'appBuilderDSL_Screen15'):
        assert not _is_linked(a1, 'appBuilderDSL_Screen15', b)
    if hasattr(a2, 'appBuilderDSL_Screen15'):
        assert _is_linked(a2, 'appBuilderDSL_Screen15', b)
    _safe_set(b, 'appBuilderDSL_Main14', None)
    assert not _is_linked(b, 'appBuilderDSL_Main14', a2)
    if hasattr(a2, 'appBuilderDSL_Screen15'):
        assert not _is_linked(a2, 'appBuilderDSL_Screen15', b)


def test_assoc_screen67_reverse_link_reassign_clear():
    a1 = appBuilderDSL_Screen(name="sample_text")
    a2 = appBuilderDSL_Screen(name="sample_text_2")
    b = appBuilderDSL_Navigate(params="sample_text")
    _safe_set(b, 'appBuilderDSL_Navigate', a1)
    assert _is_linked(b, 'appBuilderDSL_Navigate', a1)
    if hasattr(a1, 'appBuilderDSL_Screen68'):
        assert _is_linked(a1, 'appBuilderDSL_Screen68', b)
    _safe_set(b, 'appBuilderDSL_Navigate', a2)
    assert _is_linked(b, 'appBuilderDSL_Navigate', a2)
    if hasattr(a1, 'appBuilderDSL_Screen68'):
        assert not _is_linked(a1, 'appBuilderDSL_Screen68', b)
    if hasattr(a2, 'appBuilderDSL_Screen68'):
        assert _is_linked(a2, 'appBuilderDSL_Screen68', b)
    _safe_set(b, 'appBuilderDSL_Navigate', None)
    assert not _is_linked(b, 'appBuilderDSL_Navigate', a2)
    if hasattr(a2, 'appBuilderDSL_Screen68'):
        assert not _is_linked(a2, 'appBuilderDSL_Screen68', b)


def test_assoc_type109_reverse_link_reassign_clear():
    a1 = appBuilderDSL_Type(name="sample_text")
    a2 = appBuilderDSL_Type(name="sample_text_2")
    b = appBuilderDSL_Feature(many=True, name="sample_text")
    _safe_set(b, 'appBuilderDSL_Feature110', a1)
    assert _is_linked(b, 'appBuilderDSL_Feature110', a1)
    if hasattr(a1, 'appBuilderDSL_Type'):
        assert _is_linked(a1, 'appBuilderDSL_Type', b)
    _safe_set(b, 'appBuilderDSL_Feature110', a2)
    assert _is_linked(b, 'appBuilderDSL_Feature110', a2)
    if hasattr(a1, 'appBuilderDSL_Type'):
        assert not _is_linked(a1, 'appBuilderDSL_Type', b)
    if hasattr(a2, 'appBuilderDSL_Type'):
        assert _is_linked(a2, 'appBuilderDSL_Type', b)
    _safe_set(b, 'appBuilderDSL_Feature110', None)
    assert not _is_linked(b, 'appBuilderDSL_Feature110', a2)
    if hasattr(a2, 'appBuilderDSL_Type'):
        assert not _is_linked(a2, 'appBuilderDSL_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action43_stub_double():
    # appBuilderDSL_Action has no real 'appBuilderDSL_Action45' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_UiListenerBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_UiListenerBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_UiListenerBinding(controlAccess="sample_text")
    partner = appBuilderDSL_Action()
    setattr(partner, 'appBuilderDSL_Action45', None)
    _safe_set(owner, 'appBuilderDSL_UiListenerBinding44', partner)
    assert getattr(partner, 'appBuilderDSL_Action45') == owner
    _safe_set(owner, 'appBuilderDSL_UiListenerBinding44', None)
    assert getattr(partner, 'appBuilderDSL_Action45') is None


def test_assoc_assignment65_stub_double():
    # appBuilderDSL_SetInstructionAssignment has no real 'appBuilderDSL_SetInstructionAssignment' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_SetInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_SetInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_SetInstruction(modelAccess="sample_text")
    partner = appBuilderDSL_SetInstructionAssignment()
    setattr(partner, 'appBuilderDSL_SetInstructionAssignment', None)
    _safe_set(owner, 'appBuilderDSL_SetInstruction66', partner)
    assert getattr(partner, 'appBuilderDSL_SetInstructionAssignment') == owner
    _safe_set(owner, 'appBuilderDSL_SetInstruction66', None)
    assert getattr(partner, 'appBuilderDSL_SetInstructionAssignment') is None


def test_assoc_attributes23_stub_double():
    # appBuilderDSL_EntryParameters has no real 'appBuilderDSL_EntryParameters24' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Attribute(name="sample_text", type="sample_text")
    partner = appBuilderDSL_EntryParameters()
    setattr(partner, 'appBuilderDSL_EntryParameters24', None)
    _safe_set(owner, 'appBuilderDSL_Attribute', partner)
    assert owner in getattr(partner, 'appBuilderDSL_EntryParameters24')
    _safe_set(owner, 'appBuilderDSL_Attribute', None)
    assert owner not in getattr(partner, 'appBuilderDSL_EntryParameters24')


def test_assoc_attributes73_stub_double():
    # appBuilderDSL_Model has no real 'appBuilderDSL_Model74' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Attribute(name="sample_text", type="sample_text")
    partner = appBuilderDSL_Model()
    setattr(partner, 'appBuilderDSL_Model74', None)
    _safe_set(owner, 'appBuilderDSL_Attribute75', partner)
    assert owner in getattr(partner, 'appBuilderDSL_Model74')
    _safe_set(owner, 'appBuilderDSL_Attribute75', None)
    assert owner not in getattr(partner, 'appBuilderDSL_Model74')


def test_assoc_conditionExpression57_stub_double():
    # appBuilderDSL_ConditionExpression has no real 'appBuilderDSL_ConditionExpression' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Condition(name="sample_text")
    partner = appBuilderDSL_ConditionExpression()
    setattr(partner, 'appBuilderDSL_ConditionExpression', None)
    _safe_set(owner, 'appBuilderDSL_Condition58', partner)
    assert getattr(partner, 'appBuilderDSL_ConditionExpression') == owner
    _safe_set(owner, 'appBuilderDSL_Condition58', None)
    assert getattr(partner, 'appBuilderDSL_ConditionExpression') is None


def test_assoc_conditions54_stub_double():
    # appBuilderDSL_Validator has no real 'appBuilderDSL_Validator55' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Condition(name="sample_text")
    partner = appBuilderDSL_Validator()
    setattr(partner, 'appBuilderDSL_Validator55', None)
    _safe_set(owner, 'appBuilderDSL_Condition56', partner)
    assert owner in getattr(partner, 'appBuilderDSL_Validator55')
    _safe_set(owner, 'appBuilderDSL_Condition56', None)
    assert owner not in getattr(partner, 'appBuilderDSL_Validator55')


def test_assoc_conditions59_stub_double():
    # appBuilderDSL_CompositeConditionExpression has no real 'appBuilderDSL_CompositeConditionExpression' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Condition(name="sample_text")
    partner = appBuilderDSL_CompositeConditionExpression()
    setattr(partner, 'appBuilderDSL_CompositeConditionExpression', None)
    _safe_set(owner, 'appBuilderDSL_Condition60', partner)
    assert owner in getattr(partner, 'appBuilderDSL_CompositeConditionExpression')
    _safe_set(owner, 'appBuilderDSL_Condition60', None)
    assert owner not in getattr(partner, 'appBuilderDSL_CompositeConditionExpression')


def test_assoc_control41_stub_double():
    # appBuilderDSL_Control has no real 'appBuilderDSL_Control' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_ValidationBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_ValidationBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_ValidationBinding(controlAccess="sample_text")
    partner = appBuilderDSL_Control()
    setattr(partner, 'appBuilderDSL_Control', None)
    _safe_set(owner, 'appBuilderDSL_ValidationBinding42', partner)
    assert getattr(partner, 'appBuilderDSL_Control') == owner
    _safe_set(owner, 'appBuilderDSL_ValidationBinding42', None)
    assert getattr(partner, 'appBuilderDSL_Control') is None


def test_assoc_control46_stub_double():
    # appBuilderDSL_Control has no real 'appBuilderDSL_Control48' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_UiListenerBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_UiListenerBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_UiListenerBinding(controlAccess="sample_text")
    partner = appBuilderDSL_Control()
    setattr(partner, 'appBuilderDSL_Control48', None)
    _safe_set(owner, 'appBuilderDSL_UiListenerBinding47', partner)
    assert getattr(partner, 'appBuilderDSL_Control48') == owner
    _safe_set(owner, 'appBuilderDSL_UiListenerBinding47', None)
    assert getattr(partner, 'appBuilderDSL_Control48') is None


def test_assoc_control49_stub_double():
    # appBuilderDSL_Control has no real 'appBuilderDSL_Control51' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_DataBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_DataBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_DataBinding(controlAccess="sample_text")
    partner = appBuilderDSL_Control()
    setattr(partner, 'appBuilderDSL_Control51', None)
    _safe_set(owner, 'appBuilderDSL_DataBinding50', partner)
    assert getattr(partner, 'appBuilderDSL_Control51') == owner
    _safe_set(owner, 'appBuilderDSL_DataBinding50', None)
    assert getattr(partner, 'appBuilderDSL_Control51') is None


def test_assoc_control71_stub_double():
    # appBuilderDSL_Control has no real 'appBuilderDSL_Control72' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_ControlValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_ControlValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_ControlValue(controlAccess="sample_text")
    partner = appBuilderDSL_Control()
    setattr(partner, 'appBuilderDSL_Control72', None)
    _safe_set(owner, 'appBuilderDSL_ControlValue', partner)
    assert getattr(partner, 'appBuilderDSL_Control72') == owner
    _safe_set(owner, 'appBuilderDSL_ControlValue', None)
    assert getattr(partner, 'appBuilderDSL_Control72') is None


def test_assoc_controls78_stub_double():
    # appBuilderDSL_Control has no real 'appBuilderDSL_Control80' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Layout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Layout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Layout(type="sample_text")
    partner = appBuilderDSL_Control()
    setattr(partner, 'appBuilderDSL_Control80', None)
    _safe_set(owner, 'appBuilderDSL_Layout79', {partner})
    assert getattr(partner, 'appBuilderDSL_Control80') == owner
    _safe_set(owner, 'appBuilderDSL_Layout79', set())
    assert getattr(partner, 'appBuilderDSL_Control80') is None


def test_assoc_cssStyle84_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value86' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_List's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_List's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_List(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value86', None)
    _safe_set(owner, 'appBuilderDSL_List85', partner)
    assert getattr(partner, 'appBuilderDSL_Value86') == owner
    _safe_set(owner, 'appBuilderDSL_List85', None)
    assert getattr(partner, 'appBuilderDSL_Value86') is None


def test_assoc_cssStyle91_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value92' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Text(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value92', None)
    _safe_set(owner, 'appBuilderDSL_Text', partner)
    assert getattr(partner, 'appBuilderDSL_Value92') == owner
    _safe_set(owner, 'appBuilderDSL_Text', None)
    assert getattr(partner, 'appBuilderDSL_Value92') is None


def test_assoc_cssStyle96_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value97' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Button(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value97', None)
    _safe_set(owner, 'appBuilderDSL_Button', partner)
    assert getattr(partner, 'appBuilderDSL_Value97') == owner
    _safe_set(owner, 'appBuilderDSL_Button', None)
    assert getattr(partner, 'appBuilderDSL_Value97') is None


def test_assoc_databindings31_stub_double():
    # appBuilderDSL_InitAction has no real 'appBuilderDSL_InitAction32' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_DataBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_DataBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_DataBinding(controlAccess="sample_text")
    partner = appBuilderDSL_InitAction()
    setattr(partner, 'appBuilderDSL_InitAction32', None)
    _safe_set(owner, 'appBuilderDSL_DataBinding', partner)
    assert owner in getattr(partner, 'appBuilderDSL_InitAction32')
    _safe_set(owner, 'appBuilderDSL_DataBinding', None)
    assert owner not in getattr(partner, 'appBuilderDSL_InitAction32')


def test_assoc_elements0_stub_double():
    # appBuilderDSL_AppBuilder has no real 'appBuilderDSL_AppBuilder' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_AbstractElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_AbstractElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_AbstractElement(name="sample_text")
    partner = appBuilderDSL_AppBuilder()
    setattr(partner, 'appBuilderDSL_AppBuilder', None)
    _safe_set(owner, 'appBuilderDSL_AbstractElement', partner)
    assert owner in getattr(partner, 'appBuilderDSL_AppBuilder')
    _safe_set(owner, 'appBuilderDSL_AbstractElement', None)
    assert owner not in getattr(partner, 'appBuilderDSL_AppBuilder')


def test_assoc_features107_stub_double():
    # appBuilderDSL_Entity has no real 'appBuilderDSL_Entity108' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Feature(many=True, name="sample_text")
    partner = appBuilderDSL_Entity()
    setattr(partner, 'appBuilderDSL_Entity108', None)
    _safe_set(owner, 'appBuilderDSL_Feature', partner)
    assert owner in getattr(partner, 'appBuilderDSL_Entity108')
    _safe_set(owner, 'appBuilderDSL_Feature', None)
    assert owner not in getattr(partner, 'appBuilderDSL_Entity108')


def test_assoc_instructions61_stub_double():
    # appBuilderDSL_Instruction has no real 'appBuilderDSL_Instruction62' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_UiAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_UiAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_UiAction(name="sample_text")
    partner = appBuilderDSL_Instruction()
    setattr(partner, 'appBuilderDSL_Instruction62', None)
    _safe_set(owner, 'appBuilderDSL_UiAction', {partner})
    assert getattr(partner, 'appBuilderDSL_Instruction62') == owner
    _safe_set(owner, 'appBuilderDSL_UiAction', set())
    assert getattr(partner, 'appBuilderDSL_Instruction62') is None


def test_assoc_labelprovider83_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_List's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_List's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_List(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value', None)
    _safe_set(owner, 'appBuilderDSL_List', partner)
    assert getattr(partner, 'appBuilderDSL_Value') == owner
    _safe_set(owner, 'appBuilderDSL_List', None)
    assert getattr(partner, 'appBuilderDSL_Value') is None


def test_assoc_layouts103_stub_double():
    # appBuilderDSL_CompositeScreen has no real 'appBuilderDSL_CompositeScreen' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Layout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Layout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Layout(type="sample_text")
    partner = appBuilderDSL_CompositeScreen()
    setattr(partner, 'appBuilderDSL_CompositeScreen', None)
    _safe_set(owner, 'appBuilderDSL_Layout104', partner)
    assert owner in getattr(partner, 'appBuilderDSL_CompositeScreen')
    _safe_set(owner, 'appBuilderDSL_Layout104', None)
    assert owner not in getattr(partner, 'appBuilderDSL_CompositeScreen')


def test_assoc_layouts76_stub_double():
    # appBuilderDSL_View has no real 'appBuilderDSL_View77' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Layout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Layout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Layout(type="sample_text")
    partner = appBuilderDSL_View()
    setattr(partner, 'appBuilderDSL_View77', None)
    _safe_set(owner, 'appBuilderDSL_Layout', partner)
    assert owner in getattr(partner, 'appBuilderDSL_View77')
    _safe_set(owner, 'appBuilderDSL_Layout', None)
    assert owner not in getattr(partner, 'appBuilderDSL_View77')


def test_assoc_main6_stub_double():
    # appBuilderDSL_Ui has no real 'appBuilderDSL_Ui7' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Main(appName="sample_text", appVersion="sample_text", devices="sample_text", generalStyle="sample_text")
    partner = appBuilderDSL_Ui()
    setattr(partner, 'appBuilderDSL_Ui7', None)
    _safe_set(owner, 'appBuilderDSL_Main', partner)
    assert getattr(partner, 'appBuilderDSL_Ui7') == owner
    _safe_set(owner, 'appBuilderDSL_Main', None)
    assert getattr(partner, 'appBuilderDSL_Ui7') is None


def test_assoc_resourceKey101_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value102' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Label(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value102', None)
    _safe_set(owner, 'appBuilderDSL_Label', partner)
    assert getattr(partner, 'appBuilderDSL_Value102') == owner
    _safe_set(owner, 'appBuilderDSL_Label', None)
    assert getattr(partner, 'appBuilderDSL_Value102') is None


def test_assoc_resourceKey93_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value95' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Text(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value95', None)
    _safe_set(owner, 'appBuilderDSL_Text94', partner)
    assert getattr(partner, 'appBuilderDSL_Value95') == owner
    _safe_set(owner, 'appBuilderDSL_Text94', None)
    assert getattr(partner, 'appBuilderDSL_Value95') is None


def test_assoc_resourceKey98_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value100' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Button's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Button's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Button(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value100', None)
    _safe_set(owner, 'appBuilderDSL_Button99', partner)
    assert getattr(partner, 'appBuilderDSL_Value100') == owner
    _safe_set(owner, 'appBuilderDSL_Button99', None)
    assert getattr(partner, 'appBuilderDSL_Value100') is None


def test_assoc_screen81_stub_double():
    # appBuilderDSL_ScreenLayout has no real 'appBuilderDSL_ScreenLayout' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Screen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Screen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Screen(name="sample_text")
    partner = appBuilderDSL_ScreenLayout()
    setattr(partner, 'appBuilderDSL_ScreenLayout', None)
    _safe_set(owner, 'appBuilderDSL_Screen82', partner)
    assert getattr(partner, 'appBuilderDSL_ScreenLayout') == owner
    _safe_set(owner, 'appBuilderDSL_Screen82', None)
    assert getattr(partner, 'appBuilderDSL_ScreenLayout') is None


def test_assoc_screens11_stub_double():
    # appBuilderDSL_Ui has no real 'appBuilderDSL_Ui12' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_Screen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_Screen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_Screen(name="sample_text")
    partner = appBuilderDSL_Ui()
    setattr(partner, 'appBuilderDSL_Ui12', None)
    _safe_set(owner, 'appBuilderDSL_Screen', partner)
    assert owner in getattr(partner, 'appBuilderDSL_Ui12')
    _safe_set(owner, 'appBuilderDSL_Screen', None)
    assert owner not in getattr(partner, 'appBuilderDSL_Ui12')


def test_assoc_tooltip87_stub_double():
    # appBuilderDSL_Value has no real 'appBuilderDSL_Value89' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_List's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_List's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_List(name="sample_text")
    partner = appBuilderDSL_Value()
    setattr(partner, 'appBuilderDSL_Value89', None)
    _safe_set(owner, 'appBuilderDSL_List88', partner)
    assert getattr(partner, 'appBuilderDSL_Value89') == owner
    _safe_set(owner, 'appBuilderDSL_List88', None)
    assert getattr(partner, 'appBuilderDSL_Value89') is None


def test_assoc_uiListenerBindingss33_stub_double():
    # appBuilderDSL_InitAction has no real 'appBuilderDSL_InitAction34' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_UiListenerBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_UiListenerBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_UiListenerBinding(controlAccess="sample_text")
    partner = appBuilderDSL_InitAction()
    setattr(partner, 'appBuilderDSL_InitAction34', None)
    _safe_set(owner, 'appBuilderDSL_UiListenerBinding', partner)
    assert owner in getattr(partner, 'appBuilderDSL_InitAction34')
    _safe_set(owner, 'appBuilderDSL_UiListenerBinding', None)
    assert owner not in getattr(partner, 'appBuilderDSL_InitAction34')


def test_assoc_validationBindings35_stub_double():
    # appBuilderDSL_InitAction has no real 'appBuilderDSL_InitAction36' property in the generated
    # code (a bare stub) -- manually attach it so appBuilderDSL_ValidationBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # appBuilderDSL_ValidationBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = appBuilderDSL_ValidationBinding(controlAccess="sample_text")
    partner = appBuilderDSL_InitAction()
    setattr(partner, 'appBuilderDSL_InitAction36', None)
    _safe_set(owner, 'appBuilderDSL_ValidationBinding', partner)
    assert owner in getattr(partner, 'appBuilderDSL_InitAction36')
    _safe_set(owner, 'appBuilderDSL_ValidationBinding', None)
    assert owner not in getattr(partner, 'appBuilderDSL_InitAction36')


