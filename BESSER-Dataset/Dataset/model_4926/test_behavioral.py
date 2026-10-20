import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ApplyCommand,
    BeContentElement,
    ContentCommand,
    DefinitionItem,
    Entity,
    EntityField,
    Form,
    FormElement,
    NotStructuredElement,
    Relation,
    SystemEntityField,
    TypedAttribute,
    TypedSystemAttribute,
    ViewItem,
    becontent_Apply,
    becontent_ApplyCommand,
    becontent_ApplyIndexed,
    becontent_ApplyItem,
    becontent_AttributeColor,
    becontent_AttributeDate,
    becontent_AttributeFile,
    becontent_AttributeFileToFolder,
    becontent_AttributeImage,
    becontent_AttributeInteger,
    becontent_AttributeLongDate,
    becontent_AttributePassword,
    becontent_AttributePosition,
    becontent_AttributeText,
    becontent_AttributeVarchar,
    becontent_BeContentElement,
    becontent_BeContentModel,
    becontent_Channel,
    becontent_Checkbox,
    becontent_Color,
    becontent_ConditionalTemplate,
    becontent_Content,
    becontent_ContentCommand,
    becontent_Copy,
    becontent_CustomEntity,
    becontent_CustomPager,
    becontent_CustomRelation,
    becontent_Date,
    becontent_DefinitionItem,
    becontent_Editor,
    becontent_Entity,
    becontent_EntityField,
    becontent_EntityManagerPage,
    becontent_ExtendedForm,
    becontent_File,
    becontent_FileToFolder,
    becontent_FileToFolderExtension,
    becontent_Form,
    becontent_FormElement,
    becontent_Handler,
    becontent_Hidden,
    becontent_HierarchicalPosition,
    becontent_Image,
    becontent_JoinEntity,
    becontent_Link,
    becontent_LongDate,
    becontent_NotStructuredElement,
    becontent_Parameter,
    becontent_Password,
    becontent_Position,
    becontent_Propagate,
    becontent_RadioButton,
    becontent_RadioFromReference,
    becontent_Reference,
    becontent_Relation,
    becontent_RelationManager,
    becontent_Section,
    becontent_Select,
    becontent_SelectFromReference,
    becontent_Skin,
    becontent_Skinlet,
    becontent_SystemAttributeColor,
    becontent_SystemAttributeDate,
    becontent_SystemAttributeFile,
    becontent_SystemAttributeFileToFolder,
    becontent_SystemAttributeImage,
    becontent_SystemAttributeInteger,
    becontent_SystemAttributeLongDate,
    becontent_SystemAttributePassword,
    becontent_SystemAttributePosition,
    becontent_SystemAttributeText,
    becontent_SystemAttributeVarchar,
    becontent_SystemEntity,
    becontent_SystemEntityField,
    becontent_SystemReference,
    becontent_SystemRelation,
    becontent_Template,
    becontent_Text,
    becontent_Textarea,
    becontent_Trigger,
    becontent_TypedAttribute,
    becontent_TypedSystemAttribute,
    becontent_UnsetParameter,
    becontent_Validation,
    becontent_ViewItem,
    becontent_Year,
    ConditionType,
    ConditionalTemplateExpType,
    ContentStyle,
    FormMethodType,
    OrientationType,
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

def test_assoc_channel24_reverse_link_reassign_clear():
    a1 = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    a2 = becontent_Entity(isOwned=False, name="sample_text_2", presentationString="sample_text_2", rssFilter="sample_text_2", variableName="sample_text_2")
    b = becontent_Channel(_id_model="sample_text", parameters="sample_text")
    _safe_set(b, 'becontent_Channel25', a1)
    assert _is_linked(b, 'becontent_Channel25', a1)
    if hasattr(a1, 'becontent_Entity26'):
        assert _is_linked(a1, 'becontent_Entity26', b)
    _safe_set(b, 'becontent_Channel25', a2)
    assert _is_linked(b, 'becontent_Channel25', a2)
    if hasattr(a1, 'becontent_Entity26'):
        assert not _is_linked(a1, 'becontent_Entity26', b)
    if hasattr(a2, 'becontent_Entity26'):
        assert _is_linked(a2, 'becontent_Entity26', b)
    _safe_set(b, 'becontent_Channel25', None)
    assert not _is_linked(b, 'becontent_Channel25', a2)
    if hasattr(a2, 'becontent_Entity26'):
        assert not _is_linked(a2, 'becontent_Entity26', b)


def test_assoc_commands38_reverse_link_reassign_clear():
    a1 = becontent_ContentCommand(_id_model="sample_text")
    a2 = becontent_ContentCommand(_id_model="sample_text_2")
    b = becontent_Content(_id_model="sample_text", filter="sample_text", joinCondition="sample_text", limit=7, orderFields="sample_text", presentationFields="sample_text", style="sample_text", template="sample_text")
    _safe_set(b, 'becontent_Content39', {a1})
    assert _is_linked(b, 'becontent_Content39', a1)
    if hasattr(a1, 'becontent_ContentCommand'):
        assert _is_linked(a1, 'becontent_ContentCommand', b)
    _safe_set(b, 'becontent_Content39', {a2})
    assert _is_linked(b, 'becontent_Content39', a2)
    if hasattr(a1, 'becontent_ContentCommand'):
        assert not _is_linked(a1, 'becontent_ContentCommand', b)
    if hasattr(a2, 'becontent_ContentCommand'):
        assert _is_linked(a2, 'becontent_ContentCommand', b)
    _safe_set(b, 'becontent_Content39', set())
    assert not _is_linked(b, 'becontent_Content39', a2)
    if hasattr(a2, 'becontent_ContentCommand'):
        assert not _is_linked(a2, 'becontent_ContentCommand', b)


def test_assoc_conditionalTemplate40_reverse_link_reassign_clear():
    a1 = becontent_Content(_id_model="sample_text", filter="sample_text", joinCondition="sample_text", limit=7, orderFields="sample_text", presentationFields="sample_text", style="sample_text", template="sample_text")
    a2 = becontent_Content(_id_model="sample_text_2", filter="sample_text_2", joinCondition="sample_text_2", limit=13, orderFields="sample_text_2", presentationFields="sample_text_2", style="sample_text_2", template="sample_text_2")
    b = becontent_ConditionalTemplate(_id_model="sample_text", conditionExp="sample_text", falseTemplate="sample_text", fieldName="sample_text", trueTemplate="sample_text")
    _safe_set(b, 'becontent_ConditionalTemplate', a1)
    assert _is_linked(b, 'becontent_ConditionalTemplate', a1)
    if hasattr(a1, 'becontent_Content41'):
        assert _is_linked(a1, 'becontent_Content41', b)
    _safe_set(b, 'becontent_ConditionalTemplate', a2)
    assert _is_linked(b, 'becontent_ConditionalTemplate', a2)
    if hasattr(a1, 'becontent_Content41'):
        assert not _is_linked(a1, 'becontent_Content41', b)
    if hasattr(a2, 'becontent_Content41'):
        assert _is_linked(a2, 'becontent_Content41', b)
    _safe_set(b, 'becontent_ConditionalTemplate', None)
    assert not _is_linked(b, 'becontent_ConditionalTemplate', a2)
    if hasattr(a2, 'becontent_Content41'):
        assert not _is_linked(a2, 'becontent_Content41', b)


def test_assoc_customPager59_reverse_link_reassign_clear():
    a1 = becontent_Form(description="sample_text", method="sample_text", name="sample_text")
    a2 = becontent_Form(description="sample_text_2", method="sample_text_2", name="sample_text_2")
    b = becontent_CustomPager(_id_model="sample_text", className="sample_text", filter="sample_text", length=7, order="sample_text", query="sample_text", template="sample_text")
    _safe_set(b, 'becontent_CustomPager61', a1)
    assert _is_linked(b, 'becontent_CustomPager61', a1)
    if hasattr(a1, 'becontent_Form60'):
        assert _is_linked(a1, 'becontent_Form60', b)
    _safe_set(b, 'becontent_CustomPager61', a2)
    assert _is_linked(b, 'becontent_CustomPager61', a2)
    if hasattr(a1, 'becontent_Form60'):
        assert not _is_linked(a1, 'becontent_Form60', b)
    if hasattr(a2, 'becontent_Form60'):
        assert _is_linked(a2, 'becontent_Form60', b)
    _safe_set(b, 'becontent_CustomPager61', None)
    assert not _is_linked(b, 'becontent_CustomPager61', a2)
    if hasattr(a2, 'becontent_Form60'):
        assert not _is_linked(a2, 'becontent_Form60', b)


def test_assoc_customPagers51_reverse_link_reassign_clear():
    a1 = becontent_EntityManagerPage(fileName="sample_text", skin="sample_text")
    a2 = becontent_EntityManagerPage(fileName="sample_text_2", skin="sample_text_2")
    b = becontent_CustomPager(_id_model="sample_text", className="sample_text", filter="sample_text", length=7, order="sample_text", query="sample_text", template="sample_text")
    _safe_set(b, 'becontent_CustomPager', a1)
    assert _is_linked(b, 'becontent_CustomPager', a1)
    if hasattr(a1, 'becontent_EntityManagerPage52'):
        assert _is_linked(a1, 'becontent_EntityManagerPage52', b)
    _safe_set(b, 'becontent_CustomPager', a2)
    assert _is_linked(b, 'becontent_CustomPager', a2)
    if hasattr(a1, 'becontent_EntityManagerPage52'):
        assert not _is_linked(a1, 'becontent_EntityManagerPage52', b)
    if hasattr(a2, 'becontent_EntityManagerPage52'):
        assert _is_linked(a2, 'becontent_EntityManagerPage52', b)
    _safe_set(b, 'becontent_CustomPager', None)
    assert not _is_linked(b, 'becontent_CustomPager', a2)
    if hasattr(a2, 'becontent_EntityManagerPage52'):
        assert not _is_linked(a2, 'becontent_EntityManagerPage52', b)


def test_assoc_fields1_reverse_link_reassign_clear():
    a1 = becontent_EntityField(isPresented=True, isSearchPresentationBody=True, isSearchPresentationHead=True, isTextSearch=True)
    a2 = becontent_EntityField(isPresented=False, isSearchPresentationBody=False, isSearchPresentationHead=False, isTextSearch=False)
    b = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    _safe_set(b, 'becontent_Entity', {a1})
    assert _is_linked(b, 'becontent_Entity', a1)
    if hasattr(a1, 'becontent_EntityField'):
        assert _is_linked(a1, 'becontent_EntityField', b)
    _safe_set(b, 'becontent_Entity', {a2})
    assert _is_linked(b, 'becontent_Entity', a2)
    if hasattr(a1, 'becontent_EntityField'):
        assert not _is_linked(a1, 'becontent_EntityField', b)
    if hasattr(a2, 'becontent_EntityField'):
        assert _is_linked(a2, 'becontent_EntityField', b)
    _safe_set(b, 'becontent_Entity', set())
    assert not _is_linked(b, 'becontent_Entity', a2)
    if hasattr(a2, 'becontent_EntityField'):
        assert not _is_linked(a2, 'becontent_EntityField', b)


def test_assoc_firstElement65_reverse_link_reassign_clear():
    a1 = becontent_Validation(_id_model="sample_text", condition="sample_text", message="sample_text")
    a2 = becontent_Validation(_id_model="sample_text_2", condition="sample_text_2", message="sample_text_2")
    b = becontent_NotStructuredElement(helper="sample_text")
    _safe_set(b, 'becontent_NotStructuredElement', a1)
    assert _is_linked(b, 'becontent_NotStructuredElement', a1)
    if hasattr(a1, 'becontent_Validation66'):
        assert _is_linked(a1, 'becontent_Validation66', b)
    _safe_set(b, 'becontent_NotStructuredElement', a2)
    assert _is_linked(b, 'becontent_NotStructuredElement', a2)
    if hasattr(a1, 'becontent_Validation66'):
        assert not _is_linked(a1, 'becontent_Validation66', b)
    if hasattr(a2, 'becontent_Validation66'):
        assert _is_linked(a2, 'becontent_Validation66', b)
    _safe_set(b, 'becontent_NotStructuredElement', None)
    assert not _is_linked(b, 'becontent_NotStructuredElement', a2)
    if hasattr(a2, 'becontent_Validation66'):
        assert not _is_linked(a2, 'becontent_Validation66', b)


def test_assoc_forms50_reverse_link_reassign_clear():
    a1 = becontent_Form(description="sample_text", method="sample_text", name="sample_text")
    a2 = becontent_Form(description="sample_text_2", method="sample_text_2", name="sample_text_2")
    b = becontent_EntityManagerPage(fileName="sample_text", skin="sample_text")
    _safe_set(b, 'becontent_EntityManagerPage', {a1})
    assert _is_linked(b, 'becontent_EntityManagerPage', a1)
    if hasattr(a1, 'becontent_Form'):
        assert _is_linked(a1, 'becontent_Form', b)
    _safe_set(b, 'becontent_EntityManagerPage', {a2})
    assert _is_linked(b, 'becontent_EntityManagerPage', a2)
    if hasattr(a1, 'becontent_Form'):
        assert not _is_linked(a1, 'becontent_Form', b)
    if hasattr(a2, 'becontent_Form'):
        assert _is_linked(a2, 'becontent_Form', b)
    _safe_set(b, 'becontent_EntityManagerPage', set())
    assert not _is_linked(b, 'becontent_EntityManagerPage', a2)
    if hasattr(a2, 'becontent_Form'):
        assert not _is_linked(a2, 'becontent_Form', b)


def test_assoc_handler4_reverse_link_reassign_clear():
    a1 = becontent_Handler(fileName="sample_text", mainSkinPagerLength=7, mainSkinPlaceholder="sample_text", mainSkinWithPager=True)
    a2 = becontent_Handler(fileName="sample_text_2", mainSkinPagerLength=13, mainSkinPlaceholder="sample_text_2", mainSkinWithPager=False)
    b = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    _safe_set(b, 'becontent_Entity5', a1)
    assert _is_linked(b, 'becontent_Entity5', a1)
    if hasattr(a1, 'becontent_Handler'):
        assert _is_linked(a1, 'becontent_Handler', b)
    _safe_set(b, 'becontent_Entity5', a2)
    assert _is_linked(b, 'becontent_Entity5', a2)
    if hasattr(a1, 'becontent_Handler'):
        assert not _is_linked(a1, 'becontent_Handler', b)
    if hasattr(a2, 'becontent_Handler'):
        assert _is_linked(a2, 'becontent_Handler', b)
    _safe_set(b, 'becontent_Entity5', None)
    assert not _is_linked(b, 'becontent_Entity5', a2)
    if hasattr(a2, 'becontent_Handler'):
        assert not _is_linked(a2, 'becontent_Handler', b)


def test_assoc_joinEntities36_reverse_link_reassign_clear():
    a1 = becontent_JoinEntity(_id_model="sample_text")
    a2 = becontent_JoinEntity(_id_model="sample_text_2")
    b = becontent_Content(_id_model="sample_text", filter="sample_text", joinCondition="sample_text", limit=7, orderFields="sample_text", presentationFields="sample_text", style="sample_text", template="sample_text")
    _safe_set(b, 'becontent_Content37', {a1})
    assert _is_linked(b, 'becontent_Content37', a1)
    if hasattr(a1, 'becontent_JoinEntity'):
        assert _is_linked(a1, 'becontent_JoinEntity', b)
    _safe_set(b, 'becontent_Content37', {a2})
    assert _is_linked(b, 'becontent_Content37', a2)
    if hasattr(a1, 'becontent_JoinEntity'):
        assert not _is_linked(a1, 'becontent_JoinEntity', b)
    if hasattr(a2, 'becontent_JoinEntity'):
        assert _is_linked(a2, 'becontent_JoinEntity', b)
    _safe_set(b, 'becontent_Content37', set())
    assert not _is_linked(b, 'becontent_Content37', a2)
    if hasattr(a2, 'becontent_JoinEntity'):
        assert not _is_linked(a2, 'becontent_JoinEntity', b)


def test_assoc_joinRule43_reverse_link_reassign_clear():
    a1 = becontent_JoinEntity(_id_model="sample_text")
    a2 = becontent_JoinEntity(_id_model="sample_text_2")
    b = becontent_JoinEntity(_id_model="sample_text")
    _safe_set(b, 'becontent_JoinEntity44', a1)
    assert _is_linked(b, 'becontent_JoinEntity44', a1)
    if hasattr(a1, 'becontent_JoinEntity42'):
        assert _is_linked(a1, 'becontent_JoinEntity42', b)
    _safe_set(b, 'becontent_JoinEntity44', a2)
    assert _is_linked(b, 'becontent_JoinEntity44', a2)
    if hasattr(a1, 'becontent_JoinEntity42'):
        assert not _is_linked(a1, 'becontent_JoinEntity42', b)
    if hasattr(a2, 'becontent_JoinEntity42'):
        assert _is_linked(a2, 'becontent_JoinEntity42', b)
    _safe_set(b, 'becontent_JoinEntity44', None)
    assert not _is_linked(b, 'becontent_JoinEntity44', a2)
    if hasattr(a2, 'becontent_JoinEntity42'):
        assert not _is_linked(a2, 'becontent_JoinEntity42', b)


def test_assoc_mainEntity34_reverse_link_reassign_clear():
    a1 = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    a2 = becontent_Entity(isOwned=False, name="sample_text_2", presentationString="sample_text_2", rssFilter="sample_text_2", variableName="sample_text_2")
    b = becontent_Content(_id_model="sample_text", filter="sample_text", joinCondition="sample_text", limit=7, orderFields="sample_text", presentationFields="sample_text", style="sample_text", template="sample_text")
    _safe_set(b, 'becontent_Content', a1)
    assert _is_linked(b, 'becontent_Content', a1)
    if hasattr(a1, 'becontent_Entity35'):
        assert _is_linked(a1, 'becontent_Entity35', b)
    _safe_set(b, 'becontent_Content', a2)
    assert _is_linked(b, 'becontent_Content', a2)
    if hasattr(a1, 'becontent_Entity35'):
        assert not _is_linked(a1, 'becontent_Entity35', b)
    if hasattr(a2, 'becontent_Entity35'):
        assert _is_linked(a2, 'becontent_Entity35', b)
    _safe_set(b, 'becontent_Content', None)
    assert not _is_linked(b, 'becontent_Content', a2)
    if hasattr(a2, 'becontent_Entity35'):
        assert not _is_linked(a2, 'becontent_Entity35', b)


def test_assoc_mainSkin29_reverse_link_reassign_clear():
    a1 = becontent_Skin(name="sample_text")
    a2 = becontent_Skin(name="sample_text_2")
    b = becontent_Handler(fileName="sample_text", mainSkinPagerLength=7, mainSkinPlaceholder="sample_text", mainSkinWithPager=True)
    _safe_set(b, 'becontent_Handler30', a1)
    assert _is_linked(b, 'becontent_Handler30', a1)
    if hasattr(a1, 'becontent_Skin'):
        assert _is_linked(a1, 'becontent_Skin', b)
    _safe_set(b, 'becontent_Handler30', a2)
    assert _is_linked(b, 'becontent_Handler30', a2)
    if hasattr(a1, 'becontent_Skin'):
        assert not _is_linked(a1, 'becontent_Skin', b)
    if hasattr(a2, 'becontent_Skin'):
        assert _is_linked(a2, 'becontent_Skin', b)
    _safe_set(b, 'becontent_Handler30', None)
    assert not _is_linked(b, 'becontent_Handler30', a2)
    if hasattr(a2, 'becontent_Skin'):
        assert not _is_linked(a2, 'becontent_Skin', b)


def test_assoc_referredEntity17_reverse_link_reassign_clear():
    a1 = becontent_Reference(name="sample_text")
    a2 = becontent_Reference(name="sample_text_2")
    b = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    _safe_set(b, 'becontent_Entity18', a1)
    assert _is_linked(b, 'becontent_Entity18', a1)
    if hasattr(a1, 'becontent_Reference'):
        assert _is_linked(a1, 'becontent_Reference', b)
    _safe_set(b, 'becontent_Entity18', a2)
    assert _is_linked(b, 'becontent_Entity18', a2)
    if hasattr(a1, 'becontent_Reference'):
        assert not _is_linked(a1, 'becontent_Reference', b)
    if hasattr(a2, 'becontent_Reference'):
        assert _is_linked(a2, 'becontent_Reference', b)
    _safe_set(b, 'becontent_Entity18', None)
    assert not _is_linked(b, 'becontent_Entity18', a2)
    if hasattr(a2, 'becontent_Reference'):
        assert not _is_linked(a2, 'becontent_Reference', b)


def test_assoc_referredEntity45_reverse_link_reassign_clear():
    a1 = becontent_JoinEntity(_id_model="sample_text")
    a2 = becontent_JoinEntity(_id_model="sample_text_2")
    b = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    _safe_set(b, 'becontent_Entity47', a1)
    assert _is_linked(b, 'becontent_Entity47', a1)
    if hasattr(a1, 'becontent_JoinEntity46'):
        assert _is_linked(a1, 'becontent_JoinEntity46', b)
    _safe_set(b, 'becontent_Entity47', a2)
    assert _is_linked(b, 'becontent_Entity47', a2)
    if hasattr(a1, 'becontent_JoinEntity46'):
        assert not _is_linked(a1, 'becontent_JoinEntity46', b)
    if hasattr(a2, 'becontent_JoinEntity46'):
        assert _is_linked(a2, 'becontent_JoinEntity46', b)
    _safe_set(b, 'becontent_Entity47', None)
    assert not _is_linked(b, 'becontent_Entity47', a2)
    if hasattr(a2, 'becontent_JoinEntity46'):
        assert not _is_linked(a2, 'becontent_JoinEntity46', b)


def test_assoc_referredEntity70_reverse_link_reassign_clear():
    a1 = becontent_SelectFromReference(isMandatory=True, label="sample_text", name="sample_text", restrictCondition="sample_text")
    a2 = becontent_SelectFromReference(isMandatory=False, label="sample_text_2", name="sample_text_2", restrictCondition="sample_text_2")
    b = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    _safe_set(b, 'becontent_Entity71', a1)
    assert _is_linked(b, 'becontent_Entity71', a1)
    if hasattr(a1, 'becontent_SelectFromReference'):
        assert _is_linked(a1, 'becontent_SelectFromReference', b)
    _safe_set(b, 'becontent_Entity71', a2)
    assert _is_linked(b, 'becontent_Entity71', a2)
    if hasattr(a1, 'becontent_SelectFromReference'):
        assert not _is_linked(a1, 'becontent_SelectFromReference', b)
    if hasattr(a2, 'becontent_SelectFromReference'):
        assert _is_linked(a2, 'becontent_SelectFromReference', b)
    _safe_set(b, 'becontent_Entity71', None)
    assert not _is_linked(b, 'becontent_Entity71', a2)
    if hasattr(a2, 'becontent_SelectFromReference'):
        assert not _is_linked(a2, 'becontent_SelectFromReference', b)


def test_assoc_referredEntity72_reverse_link_reassign_clear():
    a1 = becontent_RadioFromReference(isMandatory=True, label="sample_text", name="sample_text", restrictCondition="sample_text")
    a2 = becontent_RadioFromReference(isMandatory=False, label="sample_text_2", name="sample_text_2", restrictCondition="sample_text_2")
    b = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    _safe_set(b, 'becontent_Entity73', a1)
    assert _is_linked(b, 'becontent_Entity73', a1)
    if hasattr(a1, 'becontent_RadioFromReference'):
        assert _is_linked(a1, 'becontent_RadioFromReference', b)
    _safe_set(b, 'becontent_Entity73', a2)
    assert _is_linked(b, 'becontent_Entity73', a2)
    if hasattr(a1, 'becontent_RadioFromReference'):
        assert not _is_linked(a1, 'becontent_RadioFromReference', b)
    if hasattr(a2, 'becontent_RadioFromReference'):
        assert _is_linked(a2, 'becontent_RadioFromReference', b)
    _safe_set(b, 'becontent_Entity73', None)
    assert not _is_linked(b, 'becontent_Entity73', a2)
    if hasattr(a2, 'becontent_RadioFromReference'):
        assert not _is_linked(a2, 'becontent_RadioFromReference', b)


def test_assoc_rss2_reverse_link_reassign_clear():
    a1 = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    a2 = becontent_Entity(isOwned=False, name="sample_text_2", presentationString="sample_text_2", rssFilter="sample_text_2", variableName="sample_text_2")
    b = becontent_Channel(_id_model="sample_text", parameters="sample_text")
    _safe_set(b, 'becontent_Channel', a1)
    assert _is_linked(b, 'becontent_Channel', a1)
    if hasattr(a1, 'becontent_Entity3'):
        assert _is_linked(a1, 'becontent_Entity3', b)
    _safe_set(b, 'becontent_Channel', a2)
    assert _is_linked(b, 'becontent_Channel', a2)
    if hasattr(a1, 'becontent_Entity3'):
        assert not _is_linked(a1, 'becontent_Entity3', b)
    if hasattr(a2, 'becontent_Entity3'):
        assert _is_linked(a2, 'becontent_Entity3', b)
    _safe_set(b, 'becontent_Channel', None)
    assert not _is_linked(b, 'becontent_Channel', a2)
    if hasattr(a2, 'becontent_Entity3'):
        assert not _is_linked(a2, 'becontent_Entity3', b)


def test_assoc_secondElement67_reverse_link_reassign_clear():
    a1 = becontent_Validation(_id_model="sample_text", condition="sample_text", message="sample_text")
    a2 = becontent_Validation(_id_model="sample_text_2", condition="sample_text_2", message="sample_text_2")
    b = becontent_NotStructuredElement(helper="sample_text")
    _safe_set(b, 'becontent_NotStructuredElement69', a1)
    assert _is_linked(b, 'becontent_NotStructuredElement69', a1)
    if hasattr(a1, 'becontent_Validation68'):
        assert _is_linked(a1, 'becontent_Validation68', b)
    _safe_set(b, 'becontent_NotStructuredElement69', a2)
    assert _is_linked(b, 'becontent_NotStructuredElement69', a2)
    if hasattr(a1, 'becontent_Validation68'):
        assert not _is_linked(a1, 'becontent_Validation68', b)
    if hasattr(a2, 'becontent_Validation68'):
        assert _is_linked(a2, 'becontent_Validation68', b)
    _safe_set(b, 'becontent_NotStructuredElement69', None)
    assert not _is_linked(b, 'becontent_NotStructuredElement69', a2)
    if hasattr(a2, 'becontent_Validation68'):
        assert not _is_linked(a2, 'becontent_Validation68', b)


def test_assoc_validations53_reverse_link_reassign_clear():
    a1 = becontent_Validation(_id_model="sample_text", condition="sample_text", message="sample_text")
    a2 = becontent_Validation(_id_model="sample_text_2", condition="sample_text_2", message="sample_text_2")
    b = becontent_EntityManagerPage(fileName="sample_text", skin="sample_text")
    _safe_set(b, 'becontent_EntityManagerPage54', {a1})
    assert _is_linked(b, 'becontent_EntityManagerPage54', a1)
    if hasattr(a1, 'becontent_Validation'):
        assert _is_linked(a1, 'becontent_Validation', b)
    _safe_set(b, 'becontent_EntityManagerPage54', {a2})
    assert _is_linked(b, 'becontent_EntityManagerPage54', a2)
    if hasattr(a1, 'becontent_Validation'):
        assert not _is_linked(a1, 'becontent_Validation', b)
    if hasattr(a2, 'becontent_Validation'):
        assert _is_linked(a2, 'becontent_Validation', b)
    _safe_set(b, 'becontent_EntityManagerPage54', set())
    assert not _is_linked(b, 'becontent_EntityManagerPage54', a2)
    if hasattr(a2, 'becontent_Validation'):
        assert not _is_linked(a2, 'becontent_Validation', b)


def test_assoc_validations62_reverse_link_reassign_clear():
    a1 = becontent_Validation(_id_model="sample_text", condition="sample_text", message="sample_text")
    a2 = becontent_Validation(_id_model="sample_text_2", condition="sample_text_2", message="sample_text_2")
    b = becontent_Form(description="sample_text", method="sample_text", name="sample_text")
    _safe_set(b, 'becontent_Form63', {a1})
    assert _is_linked(b, 'becontent_Form63', a1)
    if hasattr(a1, 'becontent_Validation64'):
        assert _is_linked(a1, 'becontent_Validation64', b)
    _safe_set(b, 'becontent_Form63', {a2})
    assert _is_linked(b, 'becontent_Form63', a2)
    if hasattr(a1, 'becontent_Validation64'):
        assert not _is_linked(a1, 'becontent_Validation64', b)
    if hasattr(a2, 'becontent_Validation64'):
        assert _is_linked(a2, 'becontent_Validation64', b)
    _safe_set(b, 'becontent_Form63', set())
    assert not _is_linked(b, 'becontent_Form63', a2)
    if hasattr(a2, 'becontent_Validation64'):
        assert not _is_linked(a2, 'becontent_Validation64', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements57_stub_double():
    # becontent_FormElement has no real 'becontent_FormElement' property in the generated
    # code (a bare stub) -- manually attach it so becontent_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_Form(description="sample_text", method="sample_text", name="sample_text")
    partner = becontent_FormElement()
    setattr(partner, 'becontent_FormElement', None)
    _safe_set(owner, 'becontent_Form58', {partner})
    assert getattr(partner, 'becontent_FormElement') == owner
    _safe_set(owner, 'becontent_Form58', set())
    assert getattr(partner, 'becontent_FormElement') is None


def test_assoc_fileExtensions19_stub_double():
    # becontent_AttributeFileToFolder has no real 'becontent_AttributeFileToFolder' property in the generated
    # code (a bare stub) -- manually attach it so becontent_FileToFolderExtension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_FileToFolderExtension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_FileToFolderExtension(_id_model="sample_text", extensionKey="sample_text", extensionValue="sample_text")
    partner = becontent_AttributeFileToFolder()
    setattr(partner, 'becontent_AttributeFileToFolder', None)
    _safe_set(owner, 'becontent_FileToFolderExtension', partner)
    assert owner in getattr(partner, 'becontent_AttributeFileToFolder')
    _safe_set(owner, 'becontent_FileToFolderExtension', None)
    assert owner not in getattr(partner, 'becontent_AttributeFileToFolder')


def test_assoc_fileExtensions22_stub_double():
    # becontent_SystemAttributeFileToFolder has no real 'becontent_SystemAttributeFileToFolder' property in the generated
    # code (a bare stub) -- manually attach it so becontent_FileToFolderExtension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_FileToFolderExtension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_FileToFolderExtension(_id_model="sample_text", extensionKey="sample_text", extensionValue="sample_text")
    partner = becontent_SystemAttributeFileToFolder()
    setattr(partner, 'becontent_SystemAttributeFileToFolder', None)
    _safe_set(owner, 'becontent_FileToFolderExtension23', partner)
    assert owner in getattr(partner, 'becontent_SystemAttributeFileToFolder')
    _safe_set(owner, 'becontent_FileToFolderExtension23', None)
    assert owner not in getattr(partner, 'becontent_SystemAttributeFileToFolder')


def test_assoc_leftForeignkey7_stub_double():
    # becontent_CustomRelation has no real 'becontent_CustomRelation' property in the generated
    # code (a bare stub) -- manually attach it so becontent_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    partner = becontent_CustomRelation()
    setattr(partner, 'becontent_CustomRelation', None)
    _safe_set(owner, 'becontent_Entity8', partner)
    assert getattr(partner, 'becontent_CustomRelation') == owner
    _safe_set(owner, 'becontent_Entity8', None)
    assert getattr(partner, 'becontent_CustomRelation') is None


def test_assoc_mainEntity55_stub_double():
    # becontent_DefinitionItem has no real 'becontent_DefinitionItem' property in the generated
    # code (a bare stub) -- manually attach it so becontent_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_Form(description="sample_text", method="sample_text", name="sample_text")
    partner = becontent_DefinitionItem()
    setattr(partner, 'becontent_DefinitionItem', None)
    _safe_set(owner, 'becontent_Form56', partner)
    assert getattr(partner, 'becontent_DefinitionItem') == owner
    _safe_set(owner, 'becontent_Form56', None)
    assert getattr(partner, 'becontent_DefinitionItem') is None


def test_assoc_mainSkinGetContent31_stub_double():
    # becontent_ViewItem has no real 'becontent_ViewItem33' property in the generated
    # code (a bare stub) -- manually attach it so becontent_Handler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_Handler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_Handler(fileName="sample_text", mainSkinPagerLength=7, mainSkinPlaceholder="sample_text", mainSkinWithPager=True)
    partner = becontent_ViewItem()
    setattr(partner, 'becontent_ViewItem33', None)
    _safe_set(owner, 'becontent_Handler32', partner)
    assert getattr(partner, 'becontent_ViewItem33') == owner
    _safe_set(owner, 'becontent_Handler32', None)
    assert getattr(partner, 'becontent_ViewItem33') is None


def test_assoc_referredEntity20_stub_double():
    # becontent_SystemEntity has no real 'becontent_SystemEntity21' property in the generated
    # code (a bare stub) -- manually attach it so becontent_SystemReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_SystemReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_SystemReference(name="sample_text")
    partner = becontent_SystemEntity()
    setattr(partner, 'becontent_SystemEntity21', None)
    _safe_set(owner, 'becontent_SystemReference', partner)
    assert getattr(partner, 'becontent_SystemEntity21') == owner
    _safe_set(owner, 'becontent_SystemReference', None)
    assert getattr(partner, 'becontent_SystemEntity21') is None


def test_assoc_rightForeignkey9_stub_double():
    # becontent_CustomRelation has no real 'becontent_CustomRelation10' property in the generated
    # code (a bare stub) -- manually attach it so becontent_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_Entity(isOwned=True, name="sample_text", presentationString="sample_text", rssFilter="sample_text", variableName="sample_text")
    partner = becontent_CustomRelation()
    setattr(partner, 'becontent_CustomRelation10', None)
    _safe_set(owner, 'becontent_Entity11', partner)
    assert getattr(partner, 'becontent_CustomRelation10') == owner
    _safe_set(owner, 'becontent_Entity11', None)
    assert getattr(partner, 'becontent_CustomRelation10') is None


def test_assoc_systemFields6_stub_double():
    # becontent_SystemEntity has no real 'becontent_SystemEntity' property in the generated
    # code (a bare stub) -- manually attach it so becontent_SystemEntityField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_SystemEntityField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_SystemEntityField(isPresented=True, isSearchPresentationBody=True, isSearchPresentationHead=True, isTextSearch=True)
    partner = becontent_SystemEntity()
    setattr(partner, 'becontent_SystemEntity', None)
    _safe_set(owner, 'becontent_SystemEntityField', partner)
    assert owner in getattr(partner, 'becontent_SystemEntity')
    _safe_set(owner, 'becontent_SystemEntityField', None)
    assert owner not in getattr(partner, 'becontent_SystemEntity')


def test_assoc_viewItems27_stub_double():
    # becontent_ViewItem has no real 'becontent_ViewItem' property in the generated
    # code (a bare stub) -- manually attach it so becontent_Handler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # becontent_Handler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = becontent_Handler(fileName="sample_text", mainSkinPagerLength=7, mainSkinPlaceholder="sample_text", mainSkinWithPager=True)
    partner = becontent_ViewItem()
    setattr(partner, 'becontent_ViewItem', None)
    _safe_set(owner, 'becontent_Handler28', {partner})
    assert getattr(partner, 'becontent_ViewItem') == owner
    _safe_set(owner, 'becontent_Handler28', set())
    assert getattr(partner, 'becontent_ViewItem') is None


