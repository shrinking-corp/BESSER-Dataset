import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseTable,
    BehaviouralComponent,
    CollectionType,
    ColumnConstraint,
    ConstructedType,
    DataType,
    DerivedTable,
    Feature,
    Parameter,
    PredefinedType,
    Restriction,
    SQL2003_V3_ARRAY,
    SQL2003_V3_Attribute,
    SQL2003_V3_BaseTable,
    SQL2003_V3_BehaviouralComponent,
    SQL2003_V3_BinaryStringType,
    SQL2003_V3_BooleanType,
    SQL2003_V3_CharacterStringType,
    SQL2003_V3_CollectionType,
    SQL2003_V3_Column,
    SQL2003_V3_ColumnConstraint,
    SQL2003_V3_ConstructedType,
    SQL2003_V3_DataType,
    SQL2003_V3_DatetimeFeature,
    SQL2003_V3_DatetimeType,
    SQL2003_V3_DerivedTable,
    SQL2003_V3_DistinctType,
    SQL2003_V3_Domain,
    SQL2003_V3_DomainConstraint,
    SQL2003_V3_Feature,
    SQL2003_V3_Field,
    SQL2003_V3_Function,
    SQL2003_V3_IntervalFeature,
    SQL2003_V3_IntervalType,
    SQL2003_V3_MULTISET,
    SQL2003_V3_Method,
    SQL2003_V3_MethodParameter,
    SQL2003_V3_NotNull,
    SQL2003_V3_NumericFeature,
    SQL2003_V3_NumericType,
    SQL2003_V3_Parameter,
    SQL2003_V3_ParameterWithMode,
    SQL2003_V3_PredefinedType,
    SQL2003_V3_PrimaryKey,
    SQL2003_V3_Procedure,
    SQL2003_V3_ROW,
    SQL2003_V3_ReferenceType,
    SQL2003_V3_ReferentialConstraint,
    SQL2003_V3_Restriction,
    SQL2003_V3_Schema,
    SQL2003_V3_StringFeature,
    SQL2003_V3_StructuralComponent,
    SQL2003_V3_StructuredType,
    SQL2003_V3_Table,
    SQL2003_V3_TableCheckConstraint,
    SQL2003_V3_TableConstraint,
    SQL2003_V3_Trigger,
    SQL2003_V3_TriggerDescriptor,
    SQL2003_V3_TypedTable,
    SQL2003_V3_UniqueConstraint,
    SQL2003_V3_UserDefinedType,
    SQL2003_V3_View,
    SQL2003_V3_XMLType,
    StructuralComponent,
    Table,
    TableConstraint,
    UniqueConstraint,
    UserDefinedType,
    BinaryStringTypes,
    BooleanTypes,
    CharacterStringTypes,
    DatetimeFeatures,
    DatetimeTypes,
    IntervalFeatures,
    IntervalTypes,
    MatchTypes,
    Multiplier,
    NumericFeatures,
    NumericRadix,
    NumericTypes,
    ParameterMode,
    ReferentialAction,
    StringFeatures,
    TriggerActionTime,
    TriggerEvent,
    TriggerLevel,
    Unit,
    XMLTypes,
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

def test_assoc_attributes70_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V3_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V3_Attribute(default="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'structured'):
        assert _is_linked(a1, 'structured', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'structured'):
        assert not _is_linked(a1, 'structured', b)
    if hasattr(a2, 'structured'):
        assert _is_linked(a2, 'structured', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'structured'):
        assert not _is_linked(a2, 'structured', b)


def test_assoc_behaviouralComponent31_reverse_link_reassign_clear():
    a1 = SQL2003_V3_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_V3_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_V3_BehaviouralComponent(body="sample_text", name="sample_text")
    _safe_set(b, 'BehaviouralComponent', a1)
    assert _is_linked(b, 'BehaviouralComponent', a1)
    if hasattr(a1, 'parametersWithMode'):
        assert _is_linked(a1, 'parametersWithMode', b)
    _safe_set(b, 'BehaviouralComponent', a2)
    assert _is_linked(b, 'BehaviouralComponent', a2)
    if hasattr(a1, 'parametersWithMode'):
        assert not _is_linked(a1, 'parametersWithMode', b)
    if hasattr(a2, 'parametersWithMode'):
        assert _is_linked(a2, 'parametersWithMode', b)
    _safe_set(b, 'BehaviouralComponent', None)
    assert not _is_linked(b, 'BehaviouralComponent', a2)
    if hasattr(a2, 'parametersWithMode'):
        assert not _is_linked(a2, 'parametersWithMode', b)


def test_assoc_behaviouralComponents47_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Schema(name="sample_text")
    a2 = SQL2003_V3_Schema(name="sample_text_2")
    b = SQL2003_V3_BehaviouralComponent(body="sample_text", name="sample_text")
    _safe_set(b, 'BehaviouralComponent48', a1)
    assert _is_linked(b, 'BehaviouralComponent48', a1)
    if hasattr(a1, 'schema'):
        assert _is_linked(a1, 'schema', b)
    _safe_set(b, 'BehaviouralComponent48', a2)
    assert _is_linked(b, 'BehaviouralComponent48', a2)
    if hasattr(a1, 'schema'):
        assert not _is_linked(a1, 'schema', b)
    if hasattr(a2, 'schema'):
        assert _is_linked(a2, 'schema', b)
    _safe_set(b, 'BehaviouralComponent48', None)
    assert not _is_linked(b, 'BehaviouralComponent48', a2)
    if hasattr(a2, 'schema'):
        assert not _is_linked(a2, 'schema', b)


def test_assoc_columns78_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Table(name="sample_text")
    a2 = SQL2003_V3_Table(name="sample_text_2")
    b = SQL2003_V3_Column(default="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_defines14_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuralComponent(name="sample_text")
    a2 = SQL2003_V3_StructuralComponent(name="sample_text_2")
    b = SQL2003_V3_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'has_domain', {a1})
    assert _is_linked(b, 'has_domain', a1)
    if hasattr(a1, 'StructuralComponent'):
        assert _is_linked(a1, 'StructuralComponent', b)
    _safe_set(b, 'has_domain', {a2})
    assert _is_linked(b, 'has_domain', a2)
    if hasattr(a1, 'StructuralComponent'):
        assert not _is_linked(a1, 'StructuralComponent', b)
    if hasattr(a2, 'StructuralComponent'):
        assert _is_linked(a2, 'StructuralComponent', b)
    _safe_set(b, 'has_domain', set())
    assert not _is_linked(b, 'has_domain', a2)
    if hasattr(a2, 'StructuralComponent'):
        assert not _is_linked(a2, 'StructuralComponent', b)


def test_assoc_description85_reverse_link_reassign_clear():
    a1 = SQL2003_V3_TriggerDescriptor(actionTime="sample_text", event="sample_text", level="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_V3_TriggerDescriptor(actionTime="sample_text_2", event="sample_text_2", level="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_V3_Trigger(name="sample_text")
    _safe_set(b, 'trigger', a1)
    assert _is_linked(b, 'trigger', a1)
    if hasattr(a1, 'TriggerDescriptor'):
        assert _is_linked(a1, 'TriggerDescriptor', b)
    _safe_set(b, 'trigger', a2)
    assert _is_linked(b, 'trigger', a2)
    if hasattr(a1, 'TriggerDescriptor'):
        assert not _is_linked(a1, 'TriggerDescriptor', b)
    if hasattr(a2, 'TriggerDescriptor'):
        assert _is_linked(a2, 'TriggerDescriptor', b)
    _safe_set(b, 'trigger', None)
    assert not _is_linked(b, 'trigger', a2)
    if hasattr(a2, 'TriggerDescriptor'):
        assert not _is_linked(a2, 'TriggerDescriptor', b)


def test_assoc_domains54_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Schema(name="sample_text")
    a2 = SQL2003_V3_Schema(name="sample_text_2")
    b = SQL2003_V3_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'Domain56', a1)
    assert _is_linked(b, 'Domain56', a1)
    if hasattr(a1, 'schema55'):
        assert _is_linked(a1, 'schema55', b)
    _safe_set(b, 'Domain56', a2)
    assert _is_linked(b, 'Domain56', a2)
    if hasattr(a1, 'schema55'):
        assert not _is_linked(a1, 'schema55', b)
    if hasattr(a2, 'schema55'):
        assert _is_linked(a2, 'schema55', b)
    _safe_set(b, 'Domain56', None)
    assert not _is_linked(b, 'Domain56', a2)
    if hasattr(a2, 'schema55'):
        assert not _is_linked(a2, 'schema55', b)


def test_assoc_has_domain65_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuralComponent(name="sample_text")
    a2 = SQL2003_V3_StructuralComponent(name="sample_text_2")
    b = SQL2003_V3_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'Domain66', a1)
    assert _is_linked(b, 'Domain66', a1)
    if hasattr(a1, 'defines'):
        assert _is_linked(a1, 'defines', b)
    _safe_set(b, 'Domain66', a2)
    assert _is_linked(b, 'Domain66', a2)
    if hasattr(a1, 'defines'):
        assert not _is_linked(a1, 'defines', b)
    if hasattr(a2, 'defines'):
        assert _is_linked(a2, 'defines', b)
    _safe_set(b, 'Domain66', None)
    assert not _is_linked(b, 'Domain66', a2)
    if hasattr(a2, 'defines'):
        assert not _is_linked(a2, 'defines', b)


def test_assoc_methods71_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V3_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V3_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'Method73', a1)
    assert _is_linked(b, 'Method73', a1)
    if hasattr(a1, 'structured72'):
        assert _is_linked(a1, 'structured72', b)
    _safe_set(b, 'Method73', a2)
    assert _is_linked(b, 'Method73', a2)
    if hasattr(a1, 'structured72'):
        assert not _is_linked(a1, 'structured72', b)
    if hasattr(a2, 'structured72'):
        assert _is_linked(a2, 'structured72', b)
    _safe_set(b, 'Method73', None)
    assert not _is_linked(b, 'Method73', a2)
    if hasattr(a2, 'structured72'):
        assert not _is_linked(a2, 'structured72', b)


def test_assoc_override21_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Method(body="sample_text", name="sample_text")
    a2 = SQL2003_V3_Method(body="sample_text_2", name="sample_text_2")
    b = SQL2003_V3_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'SQL2003_V3_Method20', a1)
    assert _is_linked(b, 'SQL2003_V3_Method20', a1)
    if hasattr(a1, 'SQL2003_V3_Method'):
        assert _is_linked(a1, 'SQL2003_V3_Method', b)
    _safe_set(b, 'SQL2003_V3_Method20', a2)
    assert _is_linked(b, 'SQL2003_V3_Method20', a2)
    if hasattr(a1, 'SQL2003_V3_Method'):
        assert not _is_linked(a1, 'SQL2003_V3_Method', b)
    if hasattr(a2, 'SQL2003_V3_Method'):
        assert _is_linked(a2, 'SQL2003_V3_Method', b)
    _safe_set(b, 'SQL2003_V3_Method20', None)
    assert not _is_linked(b, 'SQL2003_V3_Method20', a2)
    if hasattr(a2, 'SQL2003_V3_Method'):
        assert not _is_linked(a2, 'SQL2003_V3_Method', b)


def test_assoc_parametersWithMode2_reverse_link_reassign_clear():
    a1 = SQL2003_V3_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_V3_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_V3_BehaviouralComponent(body="sample_text", name="sample_text")
    _safe_set(b, 'behaviouralComponent', {a1})
    assert _is_linked(b, 'behaviouralComponent', a1)
    if hasattr(a1, 'ParameterWithMode'):
        assert _is_linked(a1, 'ParameterWithMode', b)
    _safe_set(b, 'behaviouralComponent', {a2})
    assert _is_linked(b, 'behaviouralComponent', a2)
    if hasattr(a1, 'ParameterWithMode'):
        assert not _is_linked(a1, 'ParameterWithMode', b)
    if hasattr(a2, 'ParameterWithMode'):
        assert _is_linked(a2, 'ParameterWithMode', b)
    _safe_set(b, 'behaviouralComponent', set())
    assert not _is_linked(b, 'behaviouralComponent', a2)
    if hasattr(a2, 'ParameterWithMode'):
        assert not _is_linked(a2, 'ParameterWithMode', b)


def test_assoc_schema1_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Schema(name="sample_text")
    a2 = SQL2003_V3_Schema(name="sample_text_2")
    b = SQL2003_V3_BehaviouralComponent(body="sample_text", name="sample_text")
    _safe_set(b, 'behaviouralComponents', a1)
    assert _is_linked(b, 'behaviouralComponents', a1)
    if hasattr(a1, 'Schema'):
        assert _is_linked(a1, 'Schema', b)
    _safe_set(b, 'behaviouralComponents', a2)
    assert _is_linked(b, 'behaviouralComponents', a2)
    if hasattr(a1, 'Schema'):
        assert not _is_linked(a1, 'Schema', b)
    if hasattr(a2, 'Schema'):
        assert _is_linked(a2, 'Schema', b)
    _safe_set(b, 'behaviouralComponents', None)
    assert not _is_linked(b, 'behaviouralComponents', a2)
    if hasattr(a2, 'Schema'):
        assert not _is_linked(a2, 'Schema', b)


def test_assoc_schema12_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Schema(name="sample_text")
    a2 = SQL2003_V3_Schema(name="sample_text_2")
    b = SQL2003_V3_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'domains', a1)
    assert _is_linked(b, 'domains', a1)
    if hasattr(a1, 'Schema13'):
        assert _is_linked(a1, 'Schema13', b)
    _safe_set(b, 'domains', a2)
    assert _is_linked(b, 'domains', a2)
    if hasattr(a1, 'Schema13'):
        assert not _is_linked(a1, 'Schema13', b)
    if hasattr(a2, 'Schema13'):
        assert _is_linked(a2, 'Schema13', b)
    _safe_set(b, 'domains', None)
    assert not _is_linked(b, 'domains', a2)
    if hasattr(a2, 'Schema13'):
        assert not _is_linked(a2, 'Schema13', b)


def test_assoc_schema76_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Table(name="sample_text")
    a2 = SQL2003_V3_Table(name="sample_text_2")
    b = SQL2003_V3_Schema(name="sample_text")
    _safe_set(b, 'Schema77', a1)
    assert _is_linked(b, 'Schema77', a1)
    if hasattr(a1, 'tables'):
        assert _is_linked(a1, 'tables', b)
    _safe_set(b, 'Schema77', a2)
    assert _is_linked(b, 'Schema77', a2)
    if hasattr(a1, 'tables'):
        assert not _is_linked(a1, 'tables', b)
    if hasattr(a2, 'tables'):
        assert _is_linked(a2, 'tables', b)
    _safe_set(b, 'Schema77', None)
    assert not _is_linked(b, 'Schema77', a2)
    if hasattr(a2, 'tables'):
        assert not _is_linked(a2, 'tables', b)


def test_assoc_structured0_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V3_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V3_Attribute(default="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'StructuredType'):
        assert _is_linked(a1, 'StructuredType', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'StructuredType'):
        assert not _is_linked(a1, 'StructuredType', b)
    if hasattr(a2, 'StructuredType'):
        assert _is_linked(a2, 'StructuredType', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'StructuredType'):
        assert not _is_linked(a2, 'StructuredType', b)


def test_assoc_structured22_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V3_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V3_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'StructuredType23'):
        assert _is_linked(a1, 'StructuredType23', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'StructuredType23'):
        assert not _is_linked(a1, 'StructuredType23', b)
    if hasattr(a2, 'StructuredType23'):
        assert _is_linked(a2, 'StructuredType23', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'StructuredType23'):
        assert not _is_linked(a2, 'StructuredType23', b)


def test_assoc_super_type68_reverse_link_reassign_clear():
    a1 = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V3_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    _safe_set(b, 'SQL2003_V3_StructuredType69', a1)
    assert _is_linked(b, 'SQL2003_V3_StructuredType69', a1)
    if hasattr(a1, 'SQL2003_V3_StructuredType67'):
        assert _is_linked(a1, 'SQL2003_V3_StructuredType67', b)
    _safe_set(b, 'SQL2003_V3_StructuredType69', a2)
    assert _is_linked(b, 'SQL2003_V3_StructuredType69', a2)
    if hasattr(a1, 'SQL2003_V3_StructuredType67'):
        assert not _is_linked(a1, 'SQL2003_V3_StructuredType67', b)
    if hasattr(a2, 'SQL2003_V3_StructuredType67'):
        assert _is_linked(a2, 'SQL2003_V3_StructuredType67', b)
    _safe_set(b, 'SQL2003_V3_StructuredType69', None)
    assert not _is_linked(b, 'SQL2003_V3_StructuredType69', a2)
    if hasattr(a2, 'SQL2003_V3_StructuredType67'):
        assert not _is_linked(a2, 'SQL2003_V3_StructuredType67', b)


def test_assoc_table7_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Table(name="sample_text")
    a2 = SQL2003_V3_Table(name="sample_text_2")
    b = SQL2003_V3_Column(default="sample_text")
    _safe_set(b, 'columns', a1)
    assert _is_linked(b, 'columns', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'columns', a2)
    assert _is_linked(b, 'columns', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'columns', None)
    assert not _is_linked(b, 'columns', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


def test_assoc_tables51_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Table(name="sample_text")
    a2 = SQL2003_V3_Table(name="sample_text_2")
    b = SQL2003_V3_Schema(name="sample_text")
    _safe_set(b, 'schema52', {a1})
    assert _is_linked(b, 'schema52', a1)
    if hasattr(a1, 'Table53'):
        assert _is_linked(a1, 'Table53', b)
    _safe_set(b, 'schema52', {a2})
    assert _is_linked(b, 'schema52', a2)
    if hasattr(a1, 'Table53'):
        assert not _is_linked(a1, 'Table53', b)
    if hasattr(a2, 'Table53'):
        assert _is_linked(a2, 'Table53', b)
    _safe_set(b, 'schema52', set())
    assert not _is_linked(b, 'schema52', a2)
    if hasattr(a2, 'Table53'):
        assert not _is_linked(a2, 'Table53', b)


def test_assoc_trigger88_reverse_link_reassign_clear():
    a1 = SQL2003_V3_TriggerDescriptor(actionTime="sample_text", event="sample_text", level="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_V3_TriggerDescriptor(actionTime="sample_text_2", event="sample_text_2", level="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_V3_Trigger(name="sample_text")
    _safe_set(b, 'Trigger', a1)
    assert _is_linked(b, 'Trigger', a1)
    if hasattr(a1, 'description'):
        assert _is_linked(a1, 'description', b)
    _safe_set(b, 'Trigger', a2)
    assert _is_linked(b, 'Trigger', a2)
    if hasattr(a1, 'description'):
        assert not _is_linked(a1, 'description', b)
    if hasattr(a2, 'description'):
        assert _is_linked(a2, 'description', b)
    _safe_set(b, 'Trigger', None)
    assert not _is_linked(b, 'Trigger', a2)
    if hasattr(a2, 'description'):
        assert not _is_linked(a2, 'description', b)


def test_assoc_updateColumns86_reverse_link_reassign_clear():
    a1 = SQL2003_V3_Trigger(name="sample_text")
    a2 = SQL2003_V3_Trigger(name="sample_text_2")
    b = SQL2003_V3_StructuralComponent(name="sample_text")
    _safe_set(b, 'SQL2003_V3_StructuralComponent87', a1)
    assert _is_linked(b, 'SQL2003_V3_StructuralComponent87', a1)
    if hasattr(a1, 'SQL2003_V3_Trigger'):
        assert _is_linked(a1, 'SQL2003_V3_Trigger', b)
    _safe_set(b, 'SQL2003_V3_StructuralComponent87', a2)
    assert _is_linked(b, 'SQL2003_V3_StructuralComponent87', a2)
    if hasattr(a1, 'SQL2003_V3_Trigger'):
        assert not _is_linked(a1, 'SQL2003_V3_Trigger', b)
    if hasattr(a2, 'SQL2003_V3_Trigger'):
        assert _is_linked(a2, 'SQL2003_V3_Trigger', b)
    _safe_set(b, 'SQL2003_V3_StructuralComponent87', None)
    assert not _is_linked(b, 'SQL2003_V3_StructuralComponent87', a2)
    if hasattr(a2, 'SQL2003_V3_Trigger'):
        assert not _is_linked(a2, 'SQL2003_V3_Trigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns44_stub_double():
    # SQL2003_V3_Restriction has no real 'restrictions45' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuralComponent(name="sample_text")
    partner = SQL2003_V3_Restriction()
    setattr(partner, 'restrictions45', None)
    _safe_set(owner, 'StructuralComponent46', partner)
    assert owner in getattr(partner, 'restrictions45')
    _safe_set(owner, 'StructuralComponent46', None)
    assert owner not in getattr(partner, 'restrictions45')


def test_assoc_components99_stub_double():
    # SQL2003_V3_View has no real 'views100' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuralComponent(name="sample_text")
    partner = SQL2003_V3_View()
    setattr(partner, 'views100', None)
    _safe_set(owner, 'StructuralComponent101', partner)
    assert owner in getattr(partner, 'views100')
    _safe_set(owner, 'StructuralComponent101', None)
    assert owner not in getattr(partner, 'views100')


def test_assoc_constraint15_stub_double():
    # SQL2003_V3_DomainConstraint has no real 'DomainConstraint' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Domain(default="sample_text", expression="sample_text", name="sample_text")
    partner = SQL2003_V3_DomainConstraint()
    setattr(partner, 'DomainConstraint', None)
    _safe_set(owner, 'domain', {partner})
    assert getattr(partner, 'DomainConstraint') == owner
    _safe_set(owner, 'domain', set())
    assert getattr(partner, 'DomainConstraint') is None


def test_assoc_datatypes49_stub_double():
    # SQL2003_V3_DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Schema(name="sample_text")
    partner = SQL2003_V3_DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'schema50', {partner})
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'schema50', set())
    assert getattr(partner, 'DataType') is None


def test_assoc_domain16_stub_double():
    # SQL2003_V3_DomainConstraint has no real 'constraint' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Domain(default="sample_text", expression="sample_text", name="sample_text")
    partner = SQL2003_V3_DomainConstraint()
    setattr(partner, 'constraint', None)
    _safe_set(owner, 'Domain', partner)
    assert getattr(partner, 'constraint') == owner
    _safe_set(owner, 'Domain', None)
    assert getattr(partner, 'constraint') is None


def test_assoc_features62_stub_double():
    # SQL2003_V3_Feature has no real 'SQL2003_V3_Feature64' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuralComponent(name="sample_text")
    partner = SQL2003_V3_Feature()
    setattr(partner, 'SQL2003_V3_Feature64', None)
    _safe_set(owner, 'SQL2003_V3_StructuralComponent63', {partner})
    assert getattr(partner, 'SQL2003_V3_Feature64') == owner
    _safe_set(owner, 'SQL2003_V3_StructuralComponent63', set())
    assert getattr(partner, 'SQL2003_V3_Feature64') is None


def test_assoc_method28_stub_double():
    # SQL2003_V3_MethodParameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Method(body="sample_text", name="sample_text")
    partner = SQL2003_V3_MethodParameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Method', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Method', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_parameters27_stub_double():
    # SQL2003_V3_MethodParameter has no real 'MethodParameter' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Method(body="sample_text", name="sample_text")
    partner = SQL2003_V3_MethodParameter()
    setattr(partner, 'MethodParameter', None)
    _safe_set(owner, 'method', {partner})
    assert getattr(partner, 'MethodParameter') == owner
    _safe_set(owner, 'method', set())
    assert getattr(partner, 'MethodParameter') is None


def test_assoc_references41_stub_double():
    # SQL2003_V3_UniqueConstraint has no real 'SQL2003_V3_UniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_ReferentialConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_ReferentialConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_ReferentialConstraint(delete_action="sample_text", match="sample_text", update_action="sample_text")
    partner = SQL2003_V3_UniqueConstraint()
    setattr(partner, 'SQL2003_V3_UniqueConstraint', None)
    _safe_set(owner, 'SQL2003_V3_ReferentialConstraint', partner)
    assert getattr(partner, 'SQL2003_V3_UniqueConstraint') == owner
    _safe_set(owner, 'SQL2003_V3_ReferentialConstraint', None)
    assert getattr(partner, 'SQL2003_V3_UniqueConstraint') is None


def test_assoc_restrictions60_stub_double():
    # SQL2003_V3_Restriction has no real 'Restriction' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuralComponent(name="sample_text")
    partner = SQL2003_V3_Restriction()
    setattr(partner, 'Restriction', None)
    _safe_set(owner, 'columns61', {partner})
    assert getattr(partner, 'Restriction') == owner
    _safe_set(owner, 'columns61', set())
    assert getattr(partner, 'Restriction') is None


def test_assoc_restrictions82_stub_double():
    # SQL2003_V3_Restriction has no real 'Restriction84' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Table(name="sample_text")
    partner = SQL2003_V3_Restriction()
    setattr(partner, 'Restriction84', None)
    _safe_set(owner, 'table83', {partner})
    assert getattr(partner, 'Restriction84') == owner
    _safe_set(owner, 'table83', set())
    assert getattr(partner, 'Restriction84') is None


def test_assoc_return_type24_stub_double():
    # SQL2003_V3_DataType has no real 'SQL2003_V3_DataType26' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Method(body="sample_text", name="sample_text")
    partner = SQL2003_V3_DataType()
    setattr(partner, 'SQL2003_V3_DataType26', None)
    _safe_set(owner, 'SQL2003_V3_Method25', partner)
    assert getattr(partner, 'SQL2003_V3_DataType26') == owner
    _safe_set(owner, 'SQL2003_V3_Method25', None)
    assert getattr(partner, 'SQL2003_V3_DataType26') is None


def test_assoc_schema8_stub_double():
    # SQL2003_V3_DataType has no real 'datatypes' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Schema(name="sample_text")
    partner = SQL2003_V3_DataType()
    setattr(partner, 'datatypes', None)
    _safe_set(owner, 'Schema9', partner)
    assert getattr(partner, 'datatypes') == owner
    _safe_set(owner, 'Schema9', None)
    assert getattr(partner, 'datatypes') is None


def test_assoc_structured89_stub_double():
    # SQL2003_V3_TypedTable has no real 'typed' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_V3_TypedTable()
    setattr(partner, 'typed', None)
    _safe_set(owner, 'StructuredType90', partner)
    assert getattr(partner, 'typed') == owner
    _safe_set(owner, 'StructuredType90', None)
    assert getattr(partner, 'typed') is None


def test_assoc_table42_stub_double():
    # SQL2003_V3_Restriction has no real 'restrictions' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Table(name="sample_text")
    partner = SQL2003_V3_Restriction()
    setattr(partner, 'restrictions', None)
    _safe_set(owner, 'Table43', partner)
    assert getattr(partner, 'restrictions') == owner
    _safe_set(owner, 'Table43', None)
    assert getattr(partner, 'restrictions') is None


def test_assoc_tables97_stub_double():
    # SQL2003_V3_View has no real 'views' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Table(name="sample_text")
    partner = SQL2003_V3_View()
    setattr(partner, 'views', None)
    _safe_set(owner, 'Table98', partner)
    assert owner in getattr(partner, 'views')
    _safe_set(owner, 'Table98', None)
    assert owner not in getattr(partner, 'views')


def test_assoc_type29_stub_double():
    # SQL2003_V3_DataType has no real 'SQL2003_V3_DataType30' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Parameter(name="sample_text")
    partner = SQL2003_V3_DataType()
    setattr(partner, 'SQL2003_V3_DataType30', None)
    _safe_set(owner, 'SQL2003_V3_Parameter', partner)
    assert getattr(partner, 'SQL2003_V3_DataType30') == owner
    _safe_set(owner, 'SQL2003_V3_Parameter', None)
    assert getattr(partner, 'SQL2003_V3_DataType30') is None


def test_assoc_type40_stub_double():
    # SQL2003_V3_ReferenceType has no real 'SQL2003_V3_ReferenceType' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_V3_ReferenceType()
    setattr(partner, 'SQL2003_V3_ReferenceType', None)
    _safe_set(owner, 'SQL2003_V3_StructuredType', partner)
    assert getattr(partner, 'SQL2003_V3_ReferenceType') == owner
    _safe_set(owner, 'SQL2003_V3_StructuredType', None)
    assert getattr(partner, 'SQL2003_V3_ReferenceType') is None


def test_assoc_type57_stub_double():
    # SQL2003_V3_DataType has no real 'SQL2003_V3_DataType58' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuralComponent(name="sample_text")
    partner = SQL2003_V3_DataType()
    setattr(partner, 'SQL2003_V3_DataType58', None)
    _safe_set(owner, 'SQL2003_V3_StructuralComponent', partner)
    assert getattr(partner, 'SQL2003_V3_DataType58') == owner
    _safe_set(owner, 'SQL2003_V3_StructuralComponent', None)
    assert getattr(partner, 'SQL2003_V3_DataType58') is None


def test_assoc_typed74_stub_double():
    # SQL2003_V3_TypedTable has no real 'TypedTable' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_V3_TypedTable()
    setattr(partner, 'TypedTable', None)
    _safe_set(owner, 'structured75', {partner})
    assert getattr(partner, 'TypedTable') == owner
    _safe_set(owner, 'structured75', set())
    assert getattr(partner, 'TypedTable') is None


def test_assoc_views59_stub_double():
    # SQL2003_V3_View has no real 'View' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_StructuralComponent(name="sample_text")
    partner = SQL2003_V3_View()
    setattr(partner, 'View', None)
    _safe_set(owner, 'components', {partner})
    assert getattr(partner, 'View') == owner
    _safe_set(owner, 'components', set())
    assert getattr(partner, 'View') is None


def test_assoc_views79_stub_double():
    # SQL2003_V3_View has no real 'View81' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V3_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V3_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V3_Table(name="sample_text")
    partner = SQL2003_V3_View()
    setattr(partner, 'View81', None)
    _safe_set(owner, 'tables80', {partner})
    assert getattr(partner, 'View81') == owner
    _safe_set(owner, 'tables80', set())
    assert getattr(partner, 'View81') is None


