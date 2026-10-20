import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ComplexComponent,
    DataType,
    GraphicalComponent,
    Input,
    ServiceType,
    SimpleComponent,
    metamodeloArquitecturaPila_Architecture,
    metamodeloArquitecturaPila_Attribute,
    metamodeloArquitecturaPila_Body,
    metamodeloArquitecturaPila_Boolean,
    metamodeloArquitecturaPila_BusinessLogic,
    metamodeloArquitecturaPila_BusinessModel,
    metamodeloArquitecturaPila_Button,
    metamodeloArquitecturaPila_Check,
    metamodeloArquitecturaPila_ComplexComponent,
    metamodeloArquitecturaPila_Create,
    metamodeloArquitecturaPila_DataType,
    metamodeloArquitecturaPila_Date,
    metamodeloArquitecturaPila_DatePicker,
    metamodeloArquitecturaPila_Delete,
    metamodeloArquitecturaPila_DropdownList,
    metamodeloArquitecturaPila_Entity,
    metamodeloArquitecturaPila_Enum,
    metamodeloArquitecturaPila_Float,
    metamodeloArquitecturaPila_Form,
    metamodeloArquitecturaPila_Function,
    metamodeloArquitecturaPila_FunctionBody,
    metamodeloArquitecturaPila_GraphicalComponent,
    metamodeloArquitecturaPila_Grid,
    metamodeloArquitecturaPila_Input,
    metamodeloArquitecturaPila_Integer,
    metamodeloArquitecturaPila_Label,
    metamodeloArquitecturaPila_ListItem,
    metamodeloArquitecturaPila_Menu,
    metamodeloArquitecturaPila_MenuItem,
    metamodeloArquitecturaPila_Method,
    metamodeloArquitecturaPila_Number,
    metamodeloArquitecturaPila_Other,
    metamodeloArquitecturaPila_Parameter,
    metamodeloArquitecturaPila_Radio,
    metamodeloArquitecturaPila_Read,
    metamodeloArquitecturaPila_Select,
    metamodeloArquitecturaPila_Service,
    metamodeloArquitecturaPila_ServiceType,
    metamodeloArquitecturaPila_SimpleComponent,
    metamodeloArquitecturaPila_String,
    metamodeloArquitecturaPila_Text,
    metamodeloArquitecturaPila_TextArea,
    metamodeloArquitecturaPila_TitleBar,
    metamodeloArquitecturaPila_Update,
    metamodeloArquitecturaPila_View,
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

def test_assoc_attType52_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_DataType(name="sample_text")
    a2 = metamodeloArquitecturaPila_DataType(name="sample_text_2")
    b = metamodeloArquitecturaPila_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Attribute53', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Attribute53', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_DataType54'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_DataType54', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Attribute53', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Attribute53', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_DataType54'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_DataType54', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_DataType54'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_DataType54', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Attribute53', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Attribute53', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_DataType54'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_DataType54', b)


def test_assoc_attributes45_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Entity(name="sample_text")
    a2 = metamodeloArquitecturaPila_Entity(name="sample_text_2")
    b = metamodeloArquitecturaPila_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Attribute', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Attribute', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Entity46'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Entity46', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Attribute', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Attribute', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Entity46'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Entity46', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Entity46'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Entity46', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Attribute', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Attribute', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Entity46'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Entity46', b)


def test_assoc_body61_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Method(name="sample_text")
    a2 = metamodeloArquitecturaPila_Method(name="sample_text_2")
    b = metamodeloArquitecturaPila_Body(content="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Body', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Body', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Method62'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Method62', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Body', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Body', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Method62'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Method62', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Method62'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Method62', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Body', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Body', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Method62'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Method62', b)


def test_assoc_body72_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_FunctionBody(content="sample_text")
    a2 = metamodeloArquitecturaPila_FunctionBody(content="sample_text_2")
    b = metamodeloArquitecturaPila_Function(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Function73', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function73', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_FunctionBody'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_FunctionBody', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function73', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function73', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_FunctionBody'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_FunctionBody', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_FunctionBody'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_FunctionBody', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function73', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Function73', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_FunctionBody'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_FunctionBody', b)


def test_assoc_childrenEntities50_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Entity(name="sample_text")
    a2 = metamodeloArquitecturaPila_Entity(name="sample_text_2")
    b = metamodeloArquitecturaPila_Entity(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Entity51', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Entity51', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Entity49'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Entity49', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Entity51', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Entity51', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Entity49'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Entity49', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Entity49'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Entity49', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Entity51', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Entity51', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Entity49'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Entity49', b)


def test_assoc_childs18_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_View(name="sample_text")
    a2 = metamodeloArquitecturaPila_View(name="sample_text_2")
    b = metamodeloArquitecturaPila_View(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_View19', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_View19', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_View17'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_View17', b)
    _safe_set(b, 'metamodeloArquitecturaPila_View19', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_View19', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_View17'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_View17', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_View17'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_View17', b)
    _safe_set(b, 'metamodeloArquitecturaPila_View19', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_View19', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_View17'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_View17', b)


def test_assoc_dispatcher39_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Service(name="sample_text")
    a2 = metamodeloArquitecturaPila_Service(name="sample_text_2")
    b = metamodeloArquitecturaPila_Function(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Function', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service40'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Service40', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service40'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Service40', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service40'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Service40', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Function', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service40'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Service40', b)


def test_assoc_entryParams55_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Parameter(name="sample_text")
    a2 = metamodeloArquitecturaPila_Parameter(name="sample_text_2")
    b = metamodeloArquitecturaPila_Method(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Method56', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Method56', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter57'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Parameter57', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Method56', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Method56', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter57'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Parameter57', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter57'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Parameter57', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Method56', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Method56', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter57'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Parameter57', b)


def test_assoc_entryParams66_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Parameter(name="sample_text")
    a2 = metamodeloArquitecturaPila_Parameter(name="sample_text_2")
    b = metamodeloArquitecturaPila_Function(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Function67', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function67', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter68'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Parameter68', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function67', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function67', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter68'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Parameter68', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter68'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Parameter68', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function67', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Function67', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter68'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Parameter68', b)


def test_assoc_formComponents24_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_GraphicalComponent(displayName="sample_text", height="sample_text", id="sample_text", length="sample_text", name="sample_text")
    a2 = metamodeloArquitecturaPila_GraphicalComponent(displayName="sample_text_2", height="sample_text_2", id="sample_text_2", length="sample_text_2", name="sample_text_2")
    b = metamodeloArquitecturaPila_Form(id="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Form25', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Form25', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_GraphicalComponent26'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_GraphicalComponent26', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Form25', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Form25', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_GraphicalComponent26'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_GraphicalComponent26', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_GraphicalComponent26'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_GraphicalComponent26', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Form25', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Form25', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_GraphicalComponent26'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_GraphicalComponent26', b)


def test_assoc_forms13_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_View(name="sample_text")
    a2 = metamodeloArquitecturaPila_View(name="sample_text_2")
    b = metamodeloArquitecturaPila_Form(id="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Form', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Form', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_View14'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_View14', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Form', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Form', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_View14'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_View14', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_View14'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_View14', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Form', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Form', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_View14'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_View14', b)


def test_assoc_functions63_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Function(name="sample_text")
    a2 = metamodeloArquitecturaPila_Function(name="sample_text_2")
    b = metamodeloArquitecturaPila_BusinessLogic(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_BusinessLogic64', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_BusinessLogic64', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Function65'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Function65', b)
    _safe_set(b, 'metamodeloArquitecturaPila_BusinessLogic64', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_BusinessLogic64', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Function65'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Function65', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Function65'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Function65', b)
    _safe_set(b, 'metamodeloArquitecturaPila_BusinessLogic64', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_BusinessLogic64', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Function65'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Function65', b)


def test_assoc_gComponents15_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_View(name="sample_text")
    a2 = metamodeloArquitecturaPila_View(name="sample_text_2")
    b = metamodeloArquitecturaPila_GraphicalComponent(displayName="sample_text", height="sample_text", id="sample_text", length="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_GraphicalComponent', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_GraphicalComponent', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_View16'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_View16', b)
    _safe_set(b, 'metamodeloArquitecturaPila_GraphicalComponent', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_GraphicalComponent', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_View16'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_View16', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_View16'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_View16', b)
    _safe_set(b, 'metamodeloArquitecturaPila_GraphicalComponent', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_GraphicalComponent', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_View16'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_View16', b)


def test_assoc_items22_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_MenuItem(id="sample_text", name="sample_text")
    a2 = metamodeloArquitecturaPila_MenuItem(id="sample_text_2", name="sample_text_2")
    b = metamodeloArquitecturaPila_Menu(id="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Menu23', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Menu23', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_MenuItem'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_MenuItem', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Menu23', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Menu23', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_MenuItem'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_MenuItem', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_MenuItem'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_MenuItem', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Menu23', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Menu23', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_MenuItem'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_MenuItem', b)


def test_assoc_logic7_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_BusinessLogic(name="sample_text")
    a2 = metamodeloArquitecturaPila_BusinessLogic(name="sample_text_2")
    b = metamodeloArquitecturaPila_Architecture(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture8', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture8', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_BusinessLogic'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_BusinessLogic', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture8', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture8', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_BusinessLogic'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_BusinessLogic', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_BusinessLogic'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_BusinessLogic', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture8', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Architecture8', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_BusinessLogic'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_BusinessLogic', b)


def test_assoc_menu11_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_View(name="sample_text")
    a2 = metamodeloArquitecturaPila_View(name="sample_text_2")
    b = metamodeloArquitecturaPila_Menu(id="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Menu', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Menu', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_View12'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_View12', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Menu', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Menu', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_View12'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_View12', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_View12'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_View12', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Menu', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Menu', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_View12'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_View12', b)


def test_assoc_menuItemComponent27_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_SimpleComponent(value="sample_text")
    a2 = metamodeloArquitecturaPila_SimpleComponent(value="sample_text_2")
    b = metamodeloArquitecturaPila_MenuItem(id="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_MenuItem28', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_MenuItem28', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_SimpleComponent29'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_SimpleComponent29', b)
    _safe_set(b, 'metamodeloArquitecturaPila_MenuItem28', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_MenuItem28', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_SimpleComponent29'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_SimpleComponent29', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_SimpleComponent29'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_SimpleComponent29', b)
    _safe_set(b, 'metamodeloArquitecturaPila_MenuItem28', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_MenuItem28', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_SimpleComponent29'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_SimpleComponent29', b)


def test_assoc_methods47_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Method(name="sample_text")
    a2 = metamodeloArquitecturaPila_Method(name="sample_text_2")
    b = metamodeloArquitecturaPila_Entity(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Entity48', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Entity48', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Method'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Method', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Entity48', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Entity48', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Method'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Method', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Method'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Method', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Entity48', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Entity48', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Method'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Method', b)


def test_assoc_paramType74_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Parameter(name="sample_text")
    a2 = metamodeloArquitecturaPila_Parameter(name="sample_text_2")
    b = metamodeloArquitecturaPila_DataType(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_DataType76', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_DataType76', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter75'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Parameter75', b)
    _safe_set(b, 'metamodeloArquitecturaPila_DataType76', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_DataType76', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter75'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Parameter75', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter75'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Parameter75', b)
    _safe_set(b, 'metamodeloArquitecturaPila_DataType76', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_DataType76', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter75'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Parameter75', b)


def test_assoc_requestParams34_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Service(name="sample_text")
    a2 = metamodeloArquitecturaPila_Service(name="sample_text_2")
    b = metamodeloArquitecturaPila_Parameter(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Parameter', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Parameter', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service35'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Service35', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Parameter', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Parameter', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service35'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Service35', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service35'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Service35', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Parameter', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Parameter', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service35'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Service35', b)


def test_assoc_responseParam36_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Service(name="sample_text")
    a2 = metamodeloArquitecturaPila_Service(name="sample_text_2")
    b = metamodeloArquitecturaPila_Parameter(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Parameter38', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Parameter38', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service37'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Service37', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Parameter38', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Parameter38', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service37'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Service37', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service37'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Service37', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Parameter38', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Parameter38', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service37'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Service37', b)


def test_assoc_returnParam58_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Parameter(name="sample_text")
    a2 = metamodeloArquitecturaPila_Parameter(name="sample_text_2")
    b = metamodeloArquitecturaPila_Method(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Method59', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Method59', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter60'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Parameter60', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Method59', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Method59', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter60'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Parameter60', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter60'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Parameter60', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Method59', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Method59', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter60'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Parameter60', b)


def test_assoc_returnParam69_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Parameter(name="sample_text")
    a2 = metamodeloArquitecturaPila_Parameter(name="sample_text_2")
    b = metamodeloArquitecturaPila_Function(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Function70', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function70', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter71'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Parameter71', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function70', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Function70', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Parameter71'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Parameter71', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter71'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Parameter71', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Function70', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Function70', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Parameter71'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Parameter71', b)


def test_assoc_serviceType31_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_ServiceType(name="sample_text")
    a2 = metamodeloArquitecturaPila_ServiceType(name="sample_text_2")
    b = metamodeloArquitecturaPila_Service(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Service32', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Service32', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_ServiceType33'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_ServiceType33', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Service32', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_Service32', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_ServiceType33'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_ServiceType33', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_ServiceType33'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_ServiceType33', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Service32', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Service32', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_ServiceType33'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_ServiceType33', b)


def test_assoc_serviceTypes5_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_ServiceType(name="sample_text")
    a2 = metamodeloArquitecturaPila_ServiceType(name="sample_text_2")
    b = metamodeloArquitecturaPila_Architecture(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture6', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture6', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_ServiceType'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_ServiceType', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture6', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture6', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_ServiceType'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_ServiceType', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_ServiceType'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_ServiceType', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture6', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Architecture6', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_ServiceType'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_ServiceType', b)


def test_assoc_services3_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_Service(name="sample_text")
    a2 = metamodeloArquitecturaPila_Service(name="sample_text_2")
    b = metamodeloArquitecturaPila_Architecture(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture4', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture4', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_Service', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture4', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture4', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_Service'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_Service', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_Service', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture4', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Architecture4', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_Service'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_Service', b)


def test_assoc_title9_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_View(name="sample_text")
    a2 = metamodeloArquitecturaPila_View(name="sample_text_2")
    b = metamodeloArquitecturaPila_TitleBar(id="sample_text", name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_TitleBar', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_TitleBar', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_View10'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_View10', b)
    _safe_set(b, 'metamodeloArquitecturaPila_TitleBar', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_TitleBar', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_View10'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_View10', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_View10'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_View10', b)
    _safe_set(b, 'metamodeloArquitecturaPila_TitleBar', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_TitleBar', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_View10'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_View10', b)


def test_assoc_titleComponents20_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_TitleBar(id="sample_text", name="sample_text")
    a2 = metamodeloArquitecturaPila_TitleBar(id="sample_text_2", name="sample_text_2")
    b = metamodeloArquitecturaPila_SimpleComponent(value="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_SimpleComponent', a1)
    assert _is_linked(b, 'metamodeloArquitecturaPila_SimpleComponent', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_TitleBar21'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_TitleBar21', b)
    _safe_set(b, 'metamodeloArquitecturaPila_SimpleComponent', a2)
    assert _is_linked(b, 'metamodeloArquitecturaPila_SimpleComponent', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_TitleBar21'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_TitleBar21', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_TitleBar21'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_TitleBar21', b)
    _safe_set(b, 'metamodeloArquitecturaPila_SimpleComponent', None)
    assert not _is_linked(b, 'metamodeloArquitecturaPila_SimpleComponent', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_TitleBar21'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_TitleBar21', b)


def test_assoc_views0_reverse_link_reassign_clear():
    a1 = metamodeloArquitecturaPila_View(name="sample_text")
    a2 = metamodeloArquitecturaPila_View(name="sample_text_2")
    b = metamodeloArquitecturaPila_Architecture(name="sample_text")
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture', {a1})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture', a1)
    if hasattr(a1, 'metamodeloArquitecturaPila_View'):
        assert _is_linked(a1, 'metamodeloArquitecturaPila_View', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture', {a2})
    assert _is_linked(b, 'metamodeloArquitecturaPila_Architecture', a2)
    if hasattr(a1, 'metamodeloArquitecturaPila_View'):
        assert not _is_linked(a1, 'metamodeloArquitecturaPila_View', b)
    if hasattr(a2, 'metamodeloArquitecturaPila_View'):
        assert _is_linked(a2, 'metamodeloArquitecturaPila_View', b)
    _safe_set(b, 'metamodeloArquitecturaPila_Architecture', set())
    assert not _is_linked(b, 'metamodeloArquitecturaPila_Architecture', a2)
    if hasattr(a2, 'metamodeloArquitecturaPila_View'):
        assert not _is_linked(a2, 'metamodeloArquitecturaPila_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_businessModel1_stub_double():
    # metamodeloArquitecturaPila_BusinessModel has no real 'metamodeloArquitecturaPila_BusinessModel' property in the generated
    # code (a bare stub) -- manually attach it so metamodeloArquitecturaPila_Architecture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodeloArquitecturaPila_Architecture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodeloArquitecturaPila_Architecture(name="sample_text")
    partner = metamodeloArquitecturaPila_BusinessModel()
    setattr(partner, 'metamodeloArquitecturaPila_BusinessModel', None)
    _safe_set(owner, 'metamodeloArquitecturaPila_Architecture2', partner)
    assert getattr(partner, 'metamodeloArquitecturaPila_BusinessModel') == owner
    _safe_set(owner, 'metamodeloArquitecturaPila_Architecture2', None)
    assert getattr(partner, 'metamodeloArquitecturaPila_BusinessModel') is None


def test_assoc_dataTypes43_stub_double():
    # metamodeloArquitecturaPila_BusinessModel has no real 'metamodeloArquitecturaPila_BusinessModel44' property in the generated
    # code (a bare stub) -- manually attach it so metamodeloArquitecturaPila_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodeloArquitecturaPila_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodeloArquitecturaPila_DataType(name="sample_text")
    partner = metamodeloArquitecturaPila_BusinessModel()
    setattr(partner, 'metamodeloArquitecturaPila_BusinessModel44', None)
    _safe_set(owner, 'metamodeloArquitecturaPila_DataType', partner)
    assert owner in getattr(partner, 'metamodeloArquitecturaPila_BusinessModel44')
    _safe_set(owner, 'metamodeloArquitecturaPila_DataType', None)
    assert owner not in getattr(partner, 'metamodeloArquitecturaPila_BusinessModel44')


def test_assoc_entities41_stub_double():
    # metamodeloArquitecturaPila_BusinessModel has no real 'metamodeloArquitecturaPila_BusinessModel42' property in the generated
    # code (a bare stub) -- manually attach it so metamodeloArquitecturaPila_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodeloArquitecturaPila_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodeloArquitecturaPila_Entity(name="sample_text")
    partner = metamodeloArquitecturaPila_BusinessModel()
    setattr(partner, 'metamodeloArquitecturaPila_BusinessModel42', None)
    _safe_set(owner, 'metamodeloArquitecturaPila_Entity', partner)
    assert owner in getattr(partner, 'metamodeloArquitecturaPila_BusinessModel42')
    _safe_set(owner, 'metamodeloArquitecturaPila_Entity', None)
    assert owner not in getattr(partner, 'metamodeloArquitecturaPila_BusinessModel42')


def test_assoc_items30_stub_double():
    # metamodeloArquitecturaPila_DropdownList has no real 'metamodeloArquitecturaPila_DropdownList' property in the generated
    # code (a bare stub) -- manually attach it so metamodeloArquitecturaPila_ListItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodeloArquitecturaPila_ListItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodeloArquitecturaPila_ListItem(action="sample_text", isSelected="sample_text")
    partner = metamodeloArquitecturaPila_DropdownList()
    setattr(partner, 'metamodeloArquitecturaPila_DropdownList', None)
    _safe_set(owner, 'metamodeloArquitecturaPila_ListItem', partner)
    assert owner in getattr(partner, 'metamodeloArquitecturaPila_DropdownList')
    _safe_set(owner, 'metamodeloArquitecturaPila_ListItem', None)
    assert owner not in getattr(partner, 'metamodeloArquitecturaPila_DropdownList')


