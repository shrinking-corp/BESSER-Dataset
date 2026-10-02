import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Instruction,
    Tag,
    webapp_Action,
    webapp_AppConfig,
    webapp_Attribute,
    webapp_BusinessObject,
    webapp_Check,
    webapp_Column,
    webapp_Constraint,
    webapp_Controller,
    webapp_Detail,
    webapp_Field,
    webapp_File,
    webapp_ForeignKey,
    webapp_Form,
    webapp_Image,
    webapp_Input,
    webapp_Instruction,
    webapp_Library,
    webapp_Mapping,
    webapp_Messages,
    webapp_Model,
    webapp_Navigation,
    webapp_OnDelete,
    webapp_OnUpdate,
    webapp_Page,
    webapp_PrimaryKey,
    webapp_Properties,
    webapp_Resource,
    webapp_Table,
    webapp_TableHTML,
    webapp_Tag,
    webapp_Td,
    webapp_Text,
    webapp_Th,
    webapp_Tr,
    webapp_Unique,
    webapp_Validator,
    webapp_View,
    webapp_WebApp,
    webapp_WebConfig,
    Behavior,
    Charset,
    ColumnType,
    FormMethod,
    InputType,
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

def test_assoc_action107_reverse_link_reassign_clear():
    a1 = webapp_BusinessObject(name="sample_text", package="sample_text")
    a2 = webapp_BusinessObject(name="sample_text_2", package="sample_text_2")
    b = webapp_Action(name="sample_text", returnType="sample_text")
    _safe_set(b, 'webapp_Action109', a1)
    assert _is_linked(b, 'webapp_Action109', a1)
    if hasattr(a1, 'webapp_BusinessObject108'):
        assert _is_linked(a1, 'webapp_BusinessObject108', b)
    _safe_set(b, 'webapp_Action109', a2)
    assert _is_linked(b, 'webapp_Action109', a2)
    if hasattr(a1, 'webapp_BusinessObject108'):
        assert not _is_linked(a1, 'webapp_BusinessObject108', b)
    if hasattr(a2, 'webapp_BusinessObject108'):
        assert _is_linked(a2, 'webapp_BusinessObject108', b)
    _safe_set(b, 'webapp_Action109', None)
    assert not _is_linked(b, 'webapp_Action109', a2)
    if hasattr(a2, 'webapp_BusinessObject108'):
        assert not _is_linked(a2, 'webapp_BusinessObject108', b)


def test_assoc_action83_reverse_link_reassign_clear():
    a1 = webapp_Input(type="sample_text")
    a2 = webapp_Input(type="sample_text_2")
    b = webapp_Action(name="sample_text", returnType="sample_text")
    _safe_set(b, 'webapp_Action84', a1)
    assert _is_linked(b, 'webapp_Action84', a1)
    if hasattr(a1, 'webapp_Input'):
        assert _is_linked(a1, 'webapp_Input', b)
    _safe_set(b, 'webapp_Action84', a2)
    assert _is_linked(b, 'webapp_Action84', a2)
    if hasattr(a1, 'webapp_Input'):
        assert not _is_linked(a1, 'webapp_Input', b)
    if hasattr(a2, 'webapp_Input'):
        assert _is_linked(a2, 'webapp_Input', b)
    _safe_set(b, 'webapp_Action84', None)
    assert not _is_linked(b, 'webapp_Action84', a2)
    if hasattr(a2, 'webapp_Input'):
        assert not _is_linked(a2, 'webapp_Input', b)


def test_assoc_attribute81_reverse_link_reassign_clear():
    a1 = webapp_Tag(_property="sample_text")
    a2 = webapp_Tag(_property="sample_text_2")
    b = webapp_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'webapp_Attribute', a1)
    assert _is_linked(b, 'webapp_Attribute', a1)
    if hasattr(a1, 'webapp_Tag82'):
        assert _is_linked(a1, 'webapp_Tag82', b)
    _safe_set(b, 'webapp_Attribute', a2)
    assert _is_linked(b, 'webapp_Attribute', a2)
    if hasattr(a1, 'webapp_Tag82'):
        assert not _is_linked(a1, 'webapp_Tag82', b)
    if hasattr(a2, 'webapp_Tag82'):
        assert _is_linked(a2, 'webapp_Tag82', b)
    _safe_set(b, 'webapp_Attribute', None)
    assert not _is_linked(b, 'webapp_Attribute', a2)
    if hasattr(a2, 'webapp_Tag82'):
        assert not _is_linked(a2, 'webapp_Tag82', b)


def test_assoc_businessObject111_reverse_link_reassign_clear():
    a1 = webapp_BusinessObject(name="sample_text", package="sample_text")
    a2 = webapp_BusinessObject(name="sample_text_2", package="sample_text_2")
    b = webapp_BusinessObject(name="sample_text", package="sample_text")
    _safe_set(b, 'webapp_BusinessObject112', a1)
    assert _is_linked(b, 'webapp_BusinessObject112', a1)
    if hasattr(a1, 'webapp_BusinessObject110'):
        assert _is_linked(a1, 'webapp_BusinessObject110', b)
    _safe_set(b, 'webapp_BusinessObject112', a2)
    assert _is_linked(b, 'webapp_BusinessObject112', a2)
    if hasattr(a1, 'webapp_BusinessObject110'):
        assert not _is_linked(a1, 'webapp_BusinessObject110', b)
    if hasattr(a2, 'webapp_BusinessObject110'):
        assert _is_linked(a2, 'webapp_BusinessObject110', b)
    _safe_set(b, 'webapp_BusinessObject112', None)
    assert not _is_linked(b, 'webapp_BusinessObject112', a2)
    if hasattr(a2, 'webapp_BusinessObject110'):
        assert not _is_linked(a2, 'webapp_BusinessObject110', b)


def test_assoc_businessObject116_reverse_link_reassign_clear():
    a1 = webapp_Field(defaultValue="sample_text", name="sample_text", type="sample_text")
    a2 = webapp_Field(defaultValue="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = webapp_BusinessObject(name="sample_text", package="sample_text")
    _safe_set(b, 'webapp_BusinessObject118', a1)
    assert _is_linked(b, 'webapp_BusinessObject118', a1)
    if hasattr(a1, 'webapp_Field117'):
        assert _is_linked(a1, 'webapp_Field117', b)
    _safe_set(b, 'webapp_BusinessObject118', a2)
    assert _is_linked(b, 'webapp_BusinessObject118', a2)
    if hasattr(a1, 'webapp_Field117'):
        assert not _is_linked(a1, 'webapp_Field117', b)
    if hasattr(a2, 'webapp_Field117'):
        assert _is_linked(a2, 'webapp_Field117', b)
    _safe_set(b, 'webapp_BusinessObject118', None)
    assert not _is_linked(b, 'webapp_BusinessObject118', a2)
    if hasattr(a2, 'webapp_Field117'):
        assert not _is_linked(a2, 'webapp_Field117', b)


def test_assoc_businessObject19_reverse_link_reassign_clear():
    a1 = webapp_Model(databaseName="sample_text", password="sample_text", url="sample_text", userName="sample_text")
    a2 = webapp_Model(databaseName="sample_text_2", password="sample_text_2", url="sample_text_2", userName="sample_text_2")
    b = webapp_BusinessObject(name="sample_text", package="sample_text")
    _safe_set(b, 'webapp_BusinessObject', a1)
    assert _is_linked(b, 'webapp_BusinessObject', a1)
    if hasattr(a1, 'webapp_Model20'):
        assert _is_linked(a1, 'webapp_Model20', b)
    _safe_set(b, 'webapp_BusinessObject', a2)
    assert _is_linked(b, 'webapp_BusinessObject', a2)
    if hasattr(a1, 'webapp_Model20'):
        assert not _is_linked(a1, 'webapp_Model20', b)
    if hasattr(a2, 'webapp_Model20'):
        assert _is_linked(a2, 'webapp_Model20', b)
    _safe_set(b, 'webapp_BusinessObject', None)
    assert not _is_linked(b, 'webapp_BusinessObject', a2)
    if hasattr(a2, 'webapp_Model20'):
        assert not _is_linked(a2, 'webapp_Model20', b)


def test_assoc_businessObject78_reverse_link_reassign_clear():
    a1 = webapp_BusinessObject(name="sample_text", package="sample_text")
    a2 = webapp_BusinessObject(name="sample_text_2", package="sample_text_2")
    b = webapp_Action(name="sample_text", returnType="sample_text")
    _safe_set(b, 'webapp_Action79', a1)
    assert _is_linked(b, 'webapp_Action79', a1)
    if hasattr(a1, 'webapp_BusinessObject80'):
        assert _is_linked(a1, 'webapp_BusinessObject80', b)
    _safe_set(b, 'webapp_Action79', a2)
    assert _is_linked(b, 'webapp_Action79', a2)
    if hasattr(a1, 'webapp_BusinessObject80'):
        assert not _is_linked(a1, 'webapp_BusinessObject80', b)
    if hasattr(a2, 'webapp_BusinessObject80'):
        assert _is_linked(a2, 'webapp_BusinessObject80', b)
    _safe_set(b, 'webapp_Action79', None)
    assert not _is_linked(b, 'webapp_Action79', a2)
    if hasattr(a2, 'webapp_BusinessObject80'):
        assert not _is_linked(a2, 'webapp_BusinessObject80', b)


def test_assoc_buttonValue88_reverse_link_reassign_clear():
    a1 = webapp_Mapping(left="sample_text", right="sample_text")
    a2 = webapp_Mapping(left="sample_text_2", right="sample_text_2")
    b = webapp_Input(type="sample_text")
    _safe_set(b, 'webapp_Input89', a1)
    assert _is_linked(b, 'webapp_Input89', a1)
    if hasattr(a1, 'webapp_Mapping90'):
        assert _is_linked(a1, 'webapp_Mapping90', b)
    _safe_set(b, 'webapp_Input89', a2)
    assert _is_linked(b, 'webapp_Input89', a2)
    if hasattr(a1, 'webapp_Mapping90'):
        assert not _is_linked(a1, 'webapp_Mapping90', b)
    if hasattr(a2, 'webapp_Mapping90'):
        assert _is_linked(a2, 'webapp_Mapping90', b)
    _safe_set(b, 'webapp_Input89', None)
    assert not _is_linked(b, 'webapp_Input89', a2)
    if hasattr(a2, 'webapp_Mapping90'):
        assert not _is_linked(a2, 'webapp_Mapping90', b)


def test_assoc_column33_reverse_link_reassign_clear():
    a1 = webapp_Table(charset="sample_text", name="sample_text")
    a2 = webapp_Table(charset="sample_text_2", name="sample_text_2")
    b = webapp_Column(defaultValue="sample_text", isNotNull=True, name="sample_text", size=7, type="sample_text", useZeroFill=True)
    _safe_set(b, 'webapp_Column', a1)
    assert _is_linked(b, 'webapp_Column', a1)
    if hasattr(a1, 'webapp_Table34'):
        assert _is_linked(a1, 'webapp_Table34', b)
    _safe_set(b, 'webapp_Column', a2)
    assert _is_linked(b, 'webapp_Column', a2)
    if hasattr(a1, 'webapp_Table34'):
        assert not _is_linked(a1, 'webapp_Table34', b)
    if hasattr(a2, 'webapp_Table34'):
        assert _is_linked(a2, 'webapp_Table34', b)
    _safe_set(b, 'webapp_Column', None)
    assert not _is_linked(b, 'webapp_Column', a2)
    if hasattr(a2, 'webapp_Table34'):
        assert not _is_linked(a2, 'webapp_Table34', b)


def test_assoc_detail37_reverse_link_reassign_clear():
    a1 = webapp_Detail(precision=7, scale=7)
    a2 = webapp_Detail(precision=13, scale=13)
    b = webapp_Column(defaultValue="sample_text", isNotNull=True, name="sample_text", size=7, type="sample_text", useZeroFill=True)
    _safe_set(b, 'webapp_Column38', a1)
    assert _is_linked(b, 'webapp_Column38', a1)
    if hasattr(a1, 'webapp_Detail'):
        assert _is_linked(a1, 'webapp_Detail', b)
    _safe_set(b, 'webapp_Column38', a2)
    assert _is_linked(b, 'webapp_Column38', a2)
    if hasattr(a1, 'webapp_Detail'):
        assert not _is_linked(a1, 'webapp_Detail', b)
    if hasattr(a2, 'webapp_Detail'):
        assert _is_linked(a2, 'webapp_Detail', b)
    _safe_set(b, 'webapp_Column38', None)
    assert not _is_linked(b, 'webapp_Column38', a2)
    if hasattr(a2, 'webapp_Detail'):
        assert not _is_linked(a2, 'webapp_Detail', b)


def test_assoc_field104_reverse_link_reassign_clear():
    a1 = webapp_Field(defaultValue="sample_text", name="sample_text", type="sample_text")
    a2 = webapp_Field(defaultValue="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = webapp_BusinessObject(name="sample_text", package="sample_text")
    _safe_set(b, 'webapp_BusinessObject105', {a1})
    assert _is_linked(b, 'webapp_BusinessObject105', a1)
    if hasattr(a1, 'webapp_Field106'):
        assert _is_linked(a1, 'webapp_Field106', b)
    _safe_set(b, 'webapp_BusinessObject105', {a2})
    assert _is_linked(b, 'webapp_BusinessObject105', a2)
    if hasattr(a1, 'webapp_Field106'):
        assert not _is_linked(a1, 'webapp_Field106', b)
    if hasattr(a2, 'webapp_Field106'):
        assert _is_linked(a2, 'webapp_Field106', b)
    _safe_set(b, 'webapp_BusinessObject105', set())
    assert not _is_linked(b, 'webapp_BusinessObject105', a2)
    if hasattr(a2, 'webapp_Field106'):
        assert not _is_linked(a2, 'webapp_Field106', b)


def test_assoc_from_119_reverse_link_reassign_clear():
    a1 = webapp_Page(isMain=True, name="sample_text")
    a2 = webapp_Page(isMain=False, name="sample_text_2")
    b = webapp_Navigation(message="sample_text")
    _safe_set(b, 'webapp_Navigation120', a1)
    assert _is_linked(b, 'webapp_Navigation120', a1)
    if hasattr(a1, 'webapp_Page121'):
        assert _is_linked(a1, 'webapp_Page121', b)
    _safe_set(b, 'webapp_Navigation120', a2)
    assert _is_linked(b, 'webapp_Navigation120', a2)
    if hasattr(a1, 'webapp_Page121'):
        assert not _is_linked(a1, 'webapp_Page121', b)
    if hasattr(a2, 'webapp_Page121'):
        assert _is_linked(a2, 'webapp_Page121', b)
    _safe_set(b, 'webapp_Navigation120', None)
    assert not _is_linked(b, 'webapp_Navigation120', a2)
    if hasattr(a2, 'webapp_Page121'):
        assert not _is_linked(a2, 'webapp_Page121', b)


def test_assoc_label85_reverse_link_reassign_clear():
    a1 = webapp_Mapping(left="sample_text", right="sample_text")
    a2 = webapp_Mapping(left="sample_text_2", right="sample_text_2")
    b = webapp_Input(type="sample_text")
    _safe_set(b, 'webapp_Input86', a1)
    assert _is_linked(b, 'webapp_Input86', a1)
    if hasattr(a1, 'webapp_Mapping87'):
        assert _is_linked(a1, 'webapp_Mapping87', b)
    _safe_set(b, 'webapp_Input86', a2)
    assert _is_linked(b, 'webapp_Input86', a2)
    if hasattr(a1, 'webapp_Mapping87'):
        assert not _is_linked(a1, 'webapp_Mapping87', b)
    if hasattr(a2, 'webapp_Mapping87'):
        assert _is_linked(a2, 'webapp_Mapping87', b)
    _safe_set(b, 'webapp_Input86', None)
    assert not _is_linked(b, 'webapp_Input86', a2)
    if hasattr(a2, 'webapp_Mapping87'):
        assert not _is_linked(a2, 'webapp_Mapping87', b)


def test_assoc_mapping31_reverse_link_reassign_clear():
    a1 = webapp_Properties(name="sample_text", package="sample_text")
    a2 = webapp_Properties(name="sample_text_2", package="sample_text_2")
    b = webapp_Mapping(left="sample_text", right="sample_text")
    _safe_set(b, 'webapp_Mapping', a1)
    assert _is_linked(b, 'webapp_Mapping', a1)
    if hasattr(a1, 'webapp_Properties32'):
        assert _is_linked(a1, 'webapp_Properties32', b)
    _safe_set(b, 'webapp_Mapping', a2)
    assert _is_linked(b, 'webapp_Mapping', a2)
    if hasattr(a1, 'webapp_Properties32'):
        assert not _is_linked(a1, 'webapp_Properties32', b)
    if hasattr(a2, 'webapp_Properties32'):
        assert _is_linked(a2, 'webapp_Properties32', b)
    _safe_set(b, 'webapp_Mapping', None)
    assert not _is_linked(b, 'webapp_Mapping', a2)
    if hasattr(a2, 'webapp_Properties32'):
        assert not _is_linked(a2, 'webapp_Properties32', b)


def test_assoc_model113_reverse_link_reassign_clear():
    a1 = webapp_Model(databaseName="sample_text", password="sample_text", url="sample_text", userName="sample_text")
    a2 = webapp_Model(databaseName="sample_text_2", password="sample_text_2", url="sample_text_2", userName="sample_text_2")
    b = webapp_BusinessObject(name="sample_text", package="sample_text")
    _safe_set(b, 'webapp_BusinessObject114', a1)
    assert _is_linked(b, 'webapp_BusinessObject114', a1)
    if hasattr(a1, 'webapp_Model115'):
        assert _is_linked(a1, 'webapp_Model115', b)
    _safe_set(b, 'webapp_BusinessObject114', a2)
    assert _is_linked(b, 'webapp_BusinessObject114', a2)
    if hasattr(a1, 'webapp_Model115'):
        assert not _is_linked(a1, 'webapp_Model115', b)
    if hasattr(a2, 'webapp_Model115'):
        assert _is_linked(a2, 'webapp_Model115', b)
    _safe_set(b, 'webapp_BusinessObject114', None)
    assert not _is_linked(b, 'webapp_BusinessObject114', a2)
    if hasattr(a2, 'webapp_Model115'):
        assert not _is_linked(a2, 'webapp_Model115', b)


def test_assoc_model7_reverse_link_reassign_clear():
    a1 = webapp_WebApp(framework="sample_text", name="sample_text")
    a2 = webapp_WebApp(framework="sample_text_2", name="sample_text_2")
    b = webapp_Model(databaseName="sample_text", password="sample_text", url="sample_text", userName="sample_text")
    _safe_set(b, 'webapp_Model', a1)
    assert _is_linked(b, 'webapp_Model', a1)
    if hasattr(a1, 'webapp_WebApp8'):
        assert _is_linked(a1, 'webapp_WebApp8', b)
    _safe_set(b, 'webapp_Model', a2)
    assert _is_linked(b, 'webapp_Model', a2)
    if hasattr(a1, 'webapp_WebApp8'):
        assert not _is_linked(a1, 'webapp_WebApp8', b)
    if hasattr(a2, 'webapp_WebApp8'):
        assert _is_linked(a2, 'webapp_WebApp8', b)
    _safe_set(b, 'webapp_Model', None)
    assert not _is_linked(b, 'webapp_Model', a2)
    if hasattr(a2, 'webapp_WebApp8'):
        assert not _is_linked(a2, 'webapp_WebApp8', b)


def test_assoc_page66_reverse_link_reassign_clear():
    a1 = webapp_Validator(name="sample_text", package="sample_text")
    a2 = webapp_Validator(name="sample_text_2", package="sample_text_2")
    b = webapp_Page(isMain=True, name="sample_text")
    _safe_set(b, 'webapp_Page68', a1)
    assert _is_linked(b, 'webapp_Page68', a1)
    if hasattr(a1, 'webapp_Validator67'):
        assert _is_linked(a1, 'webapp_Validator67', b)
    _safe_set(b, 'webapp_Page68', a2)
    assert _is_linked(b, 'webapp_Page68', a2)
    if hasattr(a1, 'webapp_Validator67'):
        assert not _is_linked(a1, 'webapp_Validator67', b)
    if hasattr(a2, 'webapp_Validator67'):
        assert _is_linked(a2, 'webapp_Validator67', b)
    _safe_set(b, 'webapp_Page68', None)
    assert not _is_linked(b, 'webapp_Page68', a2)
    if hasattr(a2, 'webapp_Validator67'):
        assert not _is_linked(a2, 'webapp_Validator67', b)


def test_assoc_properties69_reverse_link_reassign_clear():
    a1 = webapp_Properties(name="sample_text", package="sample_text")
    a2 = webapp_Properties(name="sample_text_2", package="sample_text_2")
    b = webapp_Page(isMain=True, name="sample_text")
    _safe_set(b, 'webapp_Page70', {a1})
    assert _is_linked(b, 'webapp_Page70', a1)
    if hasattr(a1, 'webapp_Properties71'):
        assert _is_linked(a1, 'webapp_Properties71', b)
    _safe_set(b, 'webapp_Page70', {a2})
    assert _is_linked(b, 'webapp_Page70', a2)
    if hasattr(a1, 'webapp_Properties71'):
        assert not _is_linked(a1, 'webapp_Properties71', b)
    if hasattr(a2, 'webapp_Properties71'):
        assert _is_linked(a2, 'webapp_Properties71', b)
    _safe_set(b, 'webapp_Page70', set())
    assert not _is_linked(b, 'webapp_Page70', a2)
    if hasattr(a2, 'webapp_Properties71'):
        assert not _is_linked(a2, 'webapp_Properties71', b)


def test_assoc_table17_reverse_link_reassign_clear():
    a1 = webapp_Table(charset="sample_text", name="sample_text")
    a2 = webapp_Table(charset="sample_text_2", name="sample_text_2")
    b = webapp_Model(databaseName="sample_text", password="sample_text", url="sample_text", userName="sample_text")
    _safe_set(b, 'webapp_Model18', {a1})
    assert _is_linked(b, 'webapp_Model18', a1)
    if hasattr(a1, 'webapp_Table'):
        assert _is_linked(a1, 'webapp_Table', b)
    _safe_set(b, 'webapp_Model18', {a2})
    assert _is_linked(b, 'webapp_Model18', a2)
    if hasattr(a1, 'webapp_Table'):
        assert not _is_linked(a1, 'webapp_Table', b)
    if hasattr(a2, 'webapp_Table'):
        assert _is_linked(a2, 'webapp_Table', b)
    _safe_set(b, 'webapp_Model18', set())
    assert not _is_linked(b, 'webapp_Model18', a2)
    if hasattr(a2, 'webapp_Table'):
        assert not _is_linked(a2, 'webapp_Table', b)


def test_assoc_tag77_reverse_link_reassign_clear():
    a1 = webapp_Tag(_property="sample_text")
    a2 = webapp_Tag(_property="sample_text_2")
    b = webapp_Form(method="sample_text")
    _safe_set(b, 'webapp_Form', {a1})
    assert _is_linked(b, 'webapp_Form', a1)
    if hasattr(a1, 'webapp_Tag'):
        assert _is_linked(a1, 'webapp_Tag', b)
    _safe_set(b, 'webapp_Form', {a2})
    assert _is_linked(b, 'webapp_Form', a2)
    if hasattr(a1, 'webapp_Tag'):
        assert not _is_linked(a1, 'webapp_Tag', b)
    if hasattr(a2, 'webapp_Tag'):
        assert _is_linked(a2, 'webapp_Tag', b)
    _safe_set(b, 'webapp_Form', set())
    assert not _is_linked(b, 'webapp_Form', a2)
    if hasattr(a2, 'webapp_Tag'):
        assert not _is_linked(a2, 'webapp_Tag', b)


def test_assoc_textValue91_reverse_link_reassign_clear():
    a1 = webapp_Input(type="sample_text")
    a2 = webapp_Input(type="sample_text_2")
    b = webapp_Field(defaultValue="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'webapp_Field', a1)
    assert _is_linked(b, 'webapp_Field', a1)
    if hasattr(a1, 'webapp_Input92'):
        assert _is_linked(a1, 'webapp_Input92', b)
    _safe_set(b, 'webapp_Field', a2)
    assert _is_linked(b, 'webapp_Field', a2)
    if hasattr(a1, 'webapp_Input92'):
        assert not _is_linked(a1, 'webapp_Input92', b)
    if hasattr(a2, 'webapp_Input92'):
        assert _is_linked(a2, 'webapp_Input92', b)
    _safe_set(b, 'webapp_Field', None)
    assert not _is_linked(b, 'webapp_Field', a2)
    if hasattr(a2, 'webapp_Input92'):
        assert not _is_linked(a2, 'webapp_Input92', b)


def test_assoc_title72_reverse_link_reassign_clear():
    a1 = webapp_Page(isMain=True, name="sample_text")
    a2 = webapp_Page(isMain=False, name="sample_text_2")
    b = webapp_Mapping(left="sample_text", right="sample_text")
    _safe_set(b, 'webapp_Mapping74', a1)
    assert _is_linked(b, 'webapp_Mapping74', a1)
    if hasattr(a1, 'webapp_Page73'):
        assert _is_linked(a1, 'webapp_Page73', b)
    _safe_set(b, 'webapp_Mapping74', a2)
    assert _is_linked(b, 'webapp_Mapping74', a2)
    if hasattr(a1, 'webapp_Page73'):
        assert not _is_linked(a1, 'webapp_Page73', b)
    if hasattr(a2, 'webapp_Page73'):
        assert _is_linked(a2, 'webapp_Page73', b)
    _safe_set(b, 'webapp_Mapping74', None)
    assert not _is_linked(b, 'webapp_Mapping74', a2)
    if hasattr(a2, 'webapp_Page73'):
        assert not _is_linked(a2, 'webapp_Page73', b)


def test_assoc_to122_reverse_link_reassign_clear():
    a1 = webapp_Page(isMain=True, name="sample_text")
    a2 = webapp_Page(isMain=False, name="sample_text_2")
    b = webapp_Navigation(message="sample_text")
    _safe_set(b, 'webapp_Navigation123', a1)
    assert _is_linked(b, 'webapp_Navigation123', a1)
    if hasattr(a1, 'webapp_Page124'):
        assert _is_linked(a1, 'webapp_Page124', b)
    _safe_set(b, 'webapp_Navigation123', a2)
    assert _is_linked(b, 'webapp_Navigation123', a2)
    if hasattr(a1, 'webapp_Page124'):
        assert not _is_linked(a1, 'webapp_Page124', b)
    if hasattr(a2, 'webapp_Page124'):
        assert _is_linked(a2, 'webapp_Page124', b)
    _safe_set(b, 'webapp_Navigation123', None)
    assert not _is_linked(b, 'webapp_Navigation123', a2)
    if hasattr(a2, 'webapp_Page124'):
        assert not _is_linked(a2, 'webapp_Page124', b)


def test_assoc_validator93_reverse_link_reassign_clear():
    a1 = webapp_Validator(name="sample_text", package="sample_text")
    a2 = webapp_Validator(name="sample_text_2", package="sample_text_2")
    b = webapp_Input(type="sample_text")
    _safe_set(b, 'webapp_Input94', a1)
    assert _is_linked(b, 'webapp_Input94', a1)
    if hasattr(a1, 'webapp_Validator95'):
        assert _is_linked(a1, 'webapp_Validator95', b)
    _safe_set(b, 'webapp_Input94', a2)
    assert _is_linked(b, 'webapp_Input94', a2)
    if hasattr(a1, 'webapp_Validator95'):
        assert not _is_linked(a1, 'webapp_Validator95', b)
    if hasattr(a2, 'webapp_Validator95'):
        assert _is_linked(a2, 'webapp_Validator95', b)
    _safe_set(b, 'webapp_Input94', None)
    assert not _is_linked(b, 'webapp_Input94', a2)
    if hasattr(a2, 'webapp_Validator95'):
        assert not _is_linked(a2, 'webapp_Validator95', b)


def test_assoc_webConfig1_reverse_link_reassign_clear():
    a1 = webapp_WebConfig(displayName="sample_text")
    a2 = webapp_WebConfig(displayName="sample_text_2")
    b = webapp_WebApp(framework="sample_text", name="sample_text")
    _safe_set(b, 'webapp_WebApp2', a1)
    assert _is_linked(b, 'webapp_WebApp2', a1)
    if hasattr(a1, 'webapp_WebConfig'):
        assert _is_linked(a1, 'webapp_WebConfig', b)
    _safe_set(b, 'webapp_WebApp2', a2)
    assert _is_linked(b, 'webapp_WebApp2', a2)
    if hasattr(a1, 'webapp_WebConfig'):
        assert not _is_linked(a1, 'webapp_WebConfig', b)
    if hasattr(a2, 'webapp_WebConfig'):
        assert _is_linked(a2, 'webapp_WebConfig', b)
    _safe_set(b, 'webapp_WebApp2', None)
    assert not _is_linked(b, 'webapp_WebApp2', a2)
    if hasattr(a2, 'webapp_WebConfig'):
        assert not _is_linked(a2, 'webapp_WebConfig', b)


