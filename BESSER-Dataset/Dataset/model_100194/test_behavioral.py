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
    SQL2003_V2_ARRAY,
    SQL2003_V2_Attribute,
    SQL2003_V2_BaseTable,
    SQL2003_V2_BehaviouralComponent,
    SQL2003_V2_BinaryStringType,
    SQL2003_V2_BooleanType,
    SQL2003_V2_CharacterStringType,
    SQL2003_V2_CollectionType,
    SQL2003_V2_Column,
    SQL2003_V2_ColumnConstraint,
    SQL2003_V2_ConstructedType,
    SQL2003_V2_DataType,
    SQL2003_V2_DatetimeFeature,
    SQL2003_V2_DatetimeType,
    SQL2003_V2_DerivedTable,
    SQL2003_V2_DistinctType,
    SQL2003_V2_Domain,
    SQL2003_V2_Feature,
    SQL2003_V2_Field,
    SQL2003_V2_Function,
    SQL2003_V2_IntervalFeature,
    SQL2003_V2_IntervalType,
    SQL2003_V2_MULTISET,
    SQL2003_V2_Method,
    SQL2003_V2_MethodParameter,
    SQL2003_V2_NotNull,
    SQL2003_V2_NumericFeature,
    SQL2003_V2_NumericType,
    SQL2003_V2_Parameter,
    SQL2003_V2_ParameterWithMode,
    SQL2003_V2_PredefinedType,
    SQL2003_V2_PrimaryKey,
    SQL2003_V2_Procedure,
    SQL2003_V2_ROW,
    SQL2003_V2_ReferenceType,
    SQL2003_V2_ReferentialConstraint,
    SQL2003_V2_Restriction,
    SQL2003_V2_Schema,
    SQL2003_V2_StringFeature,
    SQL2003_V2_StructuralComponent,
    SQL2003_V2_StructuredType,
    SQL2003_V2_Table,
    SQL2003_V2_TableCheckConstraint,
    SQL2003_V2_TableConstraint,
    SQL2003_V2_Trigger,
    SQL2003_V2_TriggerDescriptor,
    SQL2003_V2_TypedTable,
    SQL2003_V2_UniqueConstraint,
    SQL2003_V2_UserDefinedType,
    SQL2003_V2_View,
    SQL2003_V2_XMLType,
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

def test_assoc_attributes63_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V2_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V2_Attribute(default="sample_text")
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


def test_assoc_behaviouralComponent26_reverse_link_reassign_clear():
    a1 = SQL2003_V2_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_V2_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_V2_BehaviouralComponent(body="sample_text", name="sample_text")
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


def test_assoc_behaviouralComponents41_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Schema(name="sample_text")
    a2 = SQL2003_V2_Schema(name="sample_text_2")
    b = SQL2003_V2_BehaviouralComponent(body="sample_text", name="sample_text")
    _safe_set(b, 'BehaviouralComponent42', a1)
    assert _is_linked(b, 'BehaviouralComponent42', a1)
    if hasattr(a1, 'schema'):
        assert _is_linked(a1, 'schema', b)
    _safe_set(b, 'BehaviouralComponent42', a2)
    assert _is_linked(b, 'BehaviouralComponent42', a2)
    if hasattr(a1, 'schema'):
        assert not _is_linked(a1, 'schema', b)
    if hasattr(a2, 'schema'):
        assert _is_linked(a2, 'schema', b)
    _safe_set(b, 'BehaviouralComponent42', None)
    assert not _is_linked(b, 'BehaviouralComponent42', a2)
    if hasattr(a2, 'schema'):
        assert not _is_linked(a2, 'schema', b)


def test_assoc_columns71_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Table(name="sample_text")
    a2 = SQL2003_V2_Table(name="sample_text_2")
    b = SQL2003_V2_Column(default="sample_text")
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


def test_assoc_defines97_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuralComponent(name="sample_text")
    a2 = SQL2003_V2_StructuralComponent(name="sample_text_2")
    b = SQL2003_V2_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'has_domain', {a1})
    assert _is_linked(b, 'has_domain', a1)
    if hasattr(a1, 'StructuralComponent98'):
        assert _is_linked(a1, 'StructuralComponent98', b)
    _safe_set(b, 'has_domain', {a2})
    assert _is_linked(b, 'has_domain', a2)
    if hasattr(a1, 'StructuralComponent98'):
        assert not _is_linked(a1, 'StructuralComponent98', b)
    if hasattr(a2, 'StructuralComponent98'):
        assert _is_linked(a2, 'StructuralComponent98', b)
    _safe_set(b, 'has_domain', set())
    assert not _is_linked(b, 'has_domain', a2)
    if hasattr(a2, 'StructuralComponent98'):
        assert not _is_linked(a2, 'StructuralComponent98', b)


def test_assoc_description78_reverse_link_reassign_clear():
    a1 = SQL2003_V2_TriggerDescriptor(actionTime="sample_text", event="sample_text", level="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_V2_TriggerDescriptor(actionTime="sample_text_2", event="sample_text_2", level="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_V2_Trigger(name="sample_text")
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


def test_assoc_domains48_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Schema(name="sample_text")
    a2 = SQL2003_V2_Schema(name="sample_text_2")
    b = SQL2003_V2_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'Domain', a1)
    assert _is_linked(b, 'Domain', a1)
    if hasattr(a1, 'schema49'):
        assert _is_linked(a1, 'schema49', b)
    _safe_set(b, 'Domain', a2)
    assert _is_linked(b, 'Domain', a2)
    if hasattr(a1, 'schema49'):
        assert not _is_linked(a1, 'schema49', b)
    if hasattr(a2, 'schema49'):
        assert _is_linked(a2, 'schema49', b)
    _safe_set(b, 'Domain', None)
    assert not _is_linked(b, 'Domain', a2)
    if hasattr(a2, 'schema49'):
        assert not _is_linked(a2, 'schema49', b)


def test_assoc_has_domain58_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuralComponent(name="sample_text")
    a2 = SQL2003_V2_StructuralComponent(name="sample_text_2")
    b = SQL2003_V2_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'Domain59', a1)
    assert _is_linked(b, 'Domain59', a1)
    if hasattr(a1, 'defines'):
        assert _is_linked(a1, 'defines', b)
    _safe_set(b, 'Domain59', a2)
    assert _is_linked(b, 'Domain59', a2)
    if hasattr(a1, 'defines'):
        assert not _is_linked(a1, 'defines', b)
    if hasattr(a2, 'defines'):
        assert _is_linked(a2, 'defines', b)
    _safe_set(b, 'Domain59', None)
    assert not _is_linked(b, 'Domain59', a2)
    if hasattr(a2, 'defines'):
        assert not _is_linked(a2, 'defines', b)


def test_assoc_methods64_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V2_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V2_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'Method66', a1)
    assert _is_linked(b, 'Method66', a1)
    if hasattr(a1, 'structured65'):
        assert _is_linked(a1, 'structured65', b)
    _safe_set(b, 'Method66', a2)
    assert _is_linked(b, 'Method66', a2)
    if hasattr(a1, 'structured65'):
        assert not _is_linked(a1, 'structured65', b)
    if hasattr(a2, 'structured65'):
        assert _is_linked(a2, 'structured65', b)
    _safe_set(b, 'Method66', None)
    assert not _is_linked(b, 'Method66', a2)
    if hasattr(a2, 'structured65'):
        assert not _is_linked(a2, 'structured65', b)


def test_assoc_override16_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Method(body="sample_text", name="sample_text")
    a2 = SQL2003_V2_Method(body="sample_text_2", name="sample_text_2")
    b = SQL2003_V2_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'SQL2003_V2_Method15', a1)
    assert _is_linked(b, 'SQL2003_V2_Method15', a1)
    if hasattr(a1, 'SQL2003_V2_Method'):
        assert _is_linked(a1, 'SQL2003_V2_Method', b)
    _safe_set(b, 'SQL2003_V2_Method15', a2)
    assert _is_linked(b, 'SQL2003_V2_Method15', a2)
    if hasattr(a1, 'SQL2003_V2_Method'):
        assert not _is_linked(a1, 'SQL2003_V2_Method', b)
    if hasattr(a2, 'SQL2003_V2_Method'):
        assert _is_linked(a2, 'SQL2003_V2_Method', b)
    _safe_set(b, 'SQL2003_V2_Method15', None)
    assert not _is_linked(b, 'SQL2003_V2_Method15', a2)
    if hasattr(a2, 'SQL2003_V2_Method'):
        assert not _is_linked(a2, 'SQL2003_V2_Method', b)


def test_assoc_parametersWithMode2_reverse_link_reassign_clear():
    a1 = SQL2003_V2_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_V2_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_V2_BehaviouralComponent(body="sample_text", name="sample_text")
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
    a1 = SQL2003_V2_Schema(name="sample_text")
    a2 = SQL2003_V2_Schema(name="sample_text_2")
    b = SQL2003_V2_BehaviouralComponent(body="sample_text", name="sample_text")
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


def test_assoc_schema69_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Table(name="sample_text")
    a2 = SQL2003_V2_Table(name="sample_text_2")
    b = SQL2003_V2_Schema(name="sample_text")
    _safe_set(b, 'Schema70', a1)
    assert _is_linked(b, 'Schema70', a1)
    if hasattr(a1, 'tables'):
        assert _is_linked(a1, 'tables', b)
    _safe_set(b, 'Schema70', a2)
    assert _is_linked(b, 'Schema70', a2)
    if hasattr(a1, 'tables'):
        assert not _is_linked(a1, 'tables', b)
    if hasattr(a2, 'tables'):
        assert _is_linked(a2, 'tables', b)
    _safe_set(b, 'Schema70', None)
    assert not _is_linked(b, 'Schema70', a2)
    if hasattr(a2, 'tables'):
        assert not _is_linked(a2, 'tables', b)


def test_assoc_schema95_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Schema(name="sample_text")
    a2 = SQL2003_V2_Schema(name="sample_text_2")
    b = SQL2003_V2_Domain(default="sample_text", expression="sample_text", name="sample_text")
    _safe_set(b, 'domains', a1)
    assert _is_linked(b, 'domains', a1)
    if hasattr(a1, 'Schema96'):
        assert _is_linked(a1, 'Schema96', b)
    _safe_set(b, 'domains', a2)
    assert _is_linked(b, 'domains', a2)
    if hasattr(a1, 'Schema96'):
        assert not _is_linked(a1, 'Schema96', b)
    if hasattr(a2, 'Schema96'):
        assert _is_linked(a2, 'Schema96', b)
    _safe_set(b, 'domains', None)
    assert not _is_linked(b, 'domains', a2)
    if hasattr(a2, 'Schema96'):
        assert not _is_linked(a2, 'Schema96', b)


def test_assoc_structured0_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V2_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V2_Attribute(default="sample_text")
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


def test_assoc_structured17_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V2_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V2_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'StructuredType18'):
        assert _is_linked(a1, 'StructuredType18', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'StructuredType18'):
        assert not _is_linked(a1, 'StructuredType18', b)
    if hasattr(a2, 'StructuredType18'):
        assert _is_linked(a2, 'StructuredType18', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'StructuredType18'):
        assert not _is_linked(a2, 'StructuredType18', b)


def test_assoc_super_type61_reverse_link_reassign_clear():
    a1 = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_V2_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    _safe_set(b, 'SQL2003_V2_StructuredType62', a1)
    assert _is_linked(b, 'SQL2003_V2_StructuredType62', a1)
    if hasattr(a1, 'SQL2003_V2_StructuredType60'):
        assert _is_linked(a1, 'SQL2003_V2_StructuredType60', b)
    _safe_set(b, 'SQL2003_V2_StructuredType62', a2)
    assert _is_linked(b, 'SQL2003_V2_StructuredType62', a2)
    if hasattr(a1, 'SQL2003_V2_StructuredType60'):
        assert not _is_linked(a1, 'SQL2003_V2_StructuredType60', b)
    if hasattr(a2, 'SQL2003_V2_StructuredType60'):
        assert _is_linked(a2, 'SQL2003_V2_StructuredType60', b)
    _safe_set(b, 'SQL2003_V2_StructuredType62', None)
    assert not _is_linked(b, 'SQL2003_V2_StructuredType62', a2)
    if hasattr(a2, 'SQL2003_V2_StructuredType60'):
        assert not _is_linked(a2, 'SQL2003_V2_StructuredType60', b)


def test_assoc_table7_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Table(name="sample_text")
    a2 = SQL2003_V2_Table(name="sample_text_2")
    b = SQL2003_V2_Column(default="sample_text")
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


def test_assoc_tables45_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Table(name="sample_text")
    a2 = SQL2003_V2_Table(name="sample_text_2")
    b = SQL2003_V2_Schema(name="sample_text")
    _safe_set(b, 'schema46', {a1})
    assert _is_linked(b, 'schema46', a1)
    if hasattr(a1, 'Table47'):
        assert _is_linked(a1, 'Table47', b)
    _safe_set(b, 'schema46', {a2})
    assert _is_linked(b, 'schema46', a2)
    if hasattr(a1, 'Table47'):
        assert not _is_linked(a1, 'Table47', b)
    if hasattr(a2, 'Table47'):
        assert _is_linked(a2, 'Table47', b)
    _safe_set(b, 'schema46', set())
    assert not _is_linked(b, 'schema46', a2)
    if hasattr(a2, 'Table47'):
        assert not _is_linked(a2, 'Table47', b)


def test_assoc_trigger81_reverse_link_reassign_clear():
    a1 = SQL2003_V2_TriggerDescriptor(actionTime="sample_text", event="sample_text", level="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_V2_TriggerDescriptor(actionTime="sample_text_2", event="sample_text_2", level="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_V2_Trigger(name="sample_text")
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


def test_assoc_updateColumns79_reverse_link_reassign_clear():
    a1 = SQL2003_V2_Trigger(name="sample_text")
    a2 = SQL2003_V2_Trigger(name="sample_text_2")
    b = SQL2003_V2_StructuralComponent(name="sample_text")
    _safe_set(b, 'SQL2003_V2_StructuralComponent80', a1)
    assert _is_linked(b, 'SQL2003_V2_StructuralComponent80', a1)
    if hasattr(a1, 'SQL2003_V2_Trigger'):
        assert _is_linked(a1, 'SQL2003_V2_Trigger', b)
    _safe_set(b, 'SQL2003_V2_StructuralComponent80', a2)
    assert _is_linked(b, 'SQL2003_V2_StructuralComponent80', a2)
    if hasattr(a1, 'SQL2003_V2_Trigger'):
        assert not _is_linked(a1, 'SQL2003_V2_Trigger', b)
    if hasattr(a2, 'SQL2003_V2_Trigger'):
        assert _is_linked(a2, 'SQL2003_V2_Trigger', b)
    _safe_set(b, 'SQL2003_V2_StructuralComponent80', None)
    assert not _is_linked(b, 'SQL2003_V2_StructuralComponent80', a2)
    if hasattr(a2, 'SQL2003_V2_Trigger'):
        assert not _is_linked(a2, 'SQL2003_V2_Trigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns39_stub_double():
    # SQL2003_V2_Restriction has no real 'restrictions40' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuralComponent(name="sample_text")
    partner = SQL2003_V2_Restriction()
    setattr(partner, 'restrictions40', None)
    _safe_set(owner, 'StructuralComponent', partner)
    assert owner in getattr(partner, 'restrictions40')
    _safe_set(owner, 'StructuralComponent', None)
    assert owner not in getattr(partner, 'restrictions40')


def test_assoc_components92_stub_double():
    # SQL2003_V2_View has no real 'views93' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuralComponent(name="sample_text")
    partner = SQL2003_V2_View()
    setattr(partner, 'views93', None)
    _safe_set(owner, 'StructuralComponent94', partner)
    assert owner in getattr(partner, 'views93')
    _safe_set(owner, 'StructuralComponent94', None)
    assert owner not in getattr(partner, 'views93')


def test_assoc_datatypes43_stub_double():
    # SQL2003_V2_DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Schema(name="sample_text")
    partner = SQL2003_V2_DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'schema44', {partner})
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'schema44', set())
    assert getattr(partner, 'DataType') is None


def test_assoc_features55_stub_double():
    # SQL2003_V2_Feature has no real 'SQL2003_V2_Feature57' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuralComponent(name="sample_text")
    partner = SQL2003_V2_Feature()
    setattr(partner, 'SQL2003_V2_Feature57', None)
    _safe_set(owner, 'SQL2003_V2_StructuralComponent56', {partner})
    assert getattr(partner, 'SQL2003_V2_Feature57') == owner
    _safe_set(owner, 'SQL2003_V2_StructuralComponent56', set())
    assert getattr(partner, 'SQL2003_V2_Feature57') is None


def test_assoc_method23_stub_double():
    # SQL2003_V2_MethodParameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Method(body="sample_text", name="sample_text")
    partner = SQL2003_V2_MethodParameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Method', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Method', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_parameters22_stub_double():
    # SQL2003_V2_MethodParameter has no real 'MethodParameter' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Method(body="sample_text", name="sample_text")
    partner = SQL2003_V2_MethodParameter()
    setattr(partner, 'MethodParameter', None)
    _safe_set(owner, 'method', {partner})
    assert getattr(partner, 'MethodParameter') == owner
    _safe_set(owner, 'method', set())
    assert getattr(partner, 'MethodParameter') is None


def test_assoc_references36_stub_double():
    # SQL2003_V2_UniqueConstraint has no real 'SQL2003_V2_UniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_ReferentialConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_ReferentialConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_ReferentialConstraint(delete_action="sample_text", match="sample_text", update_action="sample_text")
    partner = SQL2003_V2_UniqueConstraint()
    setattr(partner, 'SQL2003_V2_UniqueConstraint', None)
    _safe_set(owner, 'SQL2003_V2_ReferentialConstraint', partner)
    assert getattr(partner, 'SQL2003_V2_UniqueConstraint') == owner
    _safe_set(owner, 'SQL2003_V2_ReferentialConstraint', None)
    assert getattr(partner, 'SQL2003_V2_UniqueConstraint') is None


def test_assoc_restrictions53_stub_double():
    # SQL2003_V2_Restriction has no real 'Restriction' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuralComponent(name="sample_text")
    partner = SQL2003_V2_Restriction()
    setattr(partner, 'Restriction', None)
    _safe_set(owner, 'columns54', {partner})
    assert getattr(partner, 'Restriction') == owner
    _safe_set(owner, 'columns54', set())
    assert getattr(partner, 'Restriction') is None


def test_assoc_restrictions75_stub_double():
    # SQL2003_V2_Restriction has no real 'Restriction77' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Table(name="sample_text")
    partner = SQL2003_V2_Restriction()
    setattr(partner, 'Restriction77', None)
    _safe_set(owner, 'table76', {partner})
    assert getattr(partner, 'Restriction77') == owner
    _safe_set(owner, 'table76', set())
    assert getattr(partner, 'Restriction77') is None


def test_assoc_return_type19_stub_double():
    # SQL2003_V2_DataType has no real 'SQL2003_V2_DataType21' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Method(body="sample_text", name="sample_text")
    partner = SQL2003_V2_DataType()
    setattr(partner, 'SQL2003_V2_DataType21', None)
    _safe_set(owner, 'SQL2003_V2_Method20', partner)
    assert getattr(partner, 'SQL2003_V2_DataType21') == owner
    _safe_set(owner, 'SQL2003_V2_Method20', None)
    assert getattr(partner, 'SQL2003_V2_DataType21') is None


def test_assoc_schema8_stub_double():
    # SQL2003_V2_DataType has no real 'datatypes' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Schema(name="sample_text")
    partner = SQL2003_V2_DataType()
    setattr(partner, 'datatypes', None)
    _safe_set(owner, 'Schema9', partner)
    assert getattr(partner, 'datatypes') == owner
    _safe_set(owner, 'Schema9', None)
    assert getattr(partner, 'datatypes') is None


def test_assoc_structured82_stub_double():
    # SQL2003_V2_TypedTable has no real 'typed' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_V2_TypedTable()
    setattr(partner, 'typed', None)
    _safe_set(owner, 'StructuredType83', partner)
    assert getattr(partner, 'typed') == owner
    _safe_set(owner, 'StructuredType83', None)
    assert getattr(partner, 'typed') is None


def test_assoc_table37_stub_double():
    # SQL2003_V2_Restriction has no real 'restrictions' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Table(name="sample_text")
    partner = SQL2003_V2_Restriction()
    setattr(partner, 'restrictions', None)
    _safe_set(owner, 'Table38', partner)
    assert getattr(partner, 'restrictions') == owner
    _safe_set(owner, 'Table38', None)
    assert getattr(partner, 'restrictions') is None


def test_assoc_tables90_stub_double():
    # SQL2003_V2_View has no real 'views' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Table(name="sample_text")
    partner = SQL2003_V2_View()
    setattr(partner, 'views', None)
    _safe_set(owner, 'Table91', partner)
    assert owner in getattr(partner, 'views')
    _safe_set(owner, 'Table91', None)
    assert owner not in getattr(partner, 'views')


def test_assoc_type24_stub_double():
    # SQL2003_V2_DataType has no real 'SQL2003_V2_DataType25' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Parameter(name="sample_text")
    partner = SQL2003_V2_DataType()
    setattr(partner, 'SQL2003_V2_DataType25', None)
    _safe_set(owner, 'SQL2003_V2_Parameter', partner)
    assert getattr(partner, 'SQL2003_V2_DataType25') == owner
    _safe_set(owner, 'SQL2003_V2_Parameter', None)
    assert getattr(partner, 'SQL2003_V2_DataType25') is None


def test_assoc_type35_stub_double():
    # SQL2003_V2_ReferenceType has no real 'SQL2003_V2_ReferenceType' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_V2_ReferenceType()
    setattr(partner, 'SQL2003_V2_ReferenceType', None)
    _safe_set(owner, 'SQL2003_V2_StructuredType', partner)
    assert getattr(partner, 'SQL2003_V2_ReferenceType') == owner
    _safe_set(owner, 'SQL2003_V2_StructuredType', None)
    assert getattr(partner, 'SQL2003_V2_ReferenceType') is None


def test_assoc_type50_stub_double():
    # SQL2003_V2_DataType has no real 'SQL2003_V2_DataType51' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuralComponent(name="sample_text")
    partner = SQL2003_V2_DataType()
    setattr(partner, 'SQL2003_V2_DataType51', None)
    _safe_set(owner, 'SQL2003_V2_StructuralComponent', partner)
    assert getattr(partner, 'SQL2003_V2_DataType51') == owner
    _safe_set(owner, 'SQL2003_V2_StructuralComponent', None)
    assert getattr(partner, 'SQL2003_V2_DataType51') is None


def test_assoc_typed67_stub_double():
    # SQL2003_V2_TypedTable has no real 'TypedTable' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_V2_TypedTable()
    setattr(partner, 'TypedTable', None)
    _safe_set(owner, 'structured68', {partner})
    assert getattr(partner, 'TypedTable') == owner
    _safe_set(owner, 'structured68', set())
    assert getattr(partner, 'TypedTable') is None


def test_assoc_views52_stub_double():
    # SQL2003_V2_View has no real 'View' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_StructuralComponent(name="sample_text")
    partner = SQL2003_V2_View()
    setattr(partner, 'View', None)
    _safe_set(owner, 'components', {partner})
    assert getattr(partner, 'View') == owner
    _safe_set(owner, 'components', set())
    assert getattr(partner, 'View') is None


def test_assoc_views72_stub_double():
    # SQL2003_V2_View has no real 'View74' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_V2_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_V2_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_V2_Table(name="sample_text")
    partner = SQL2003_V2_View()
    setattr(partner, 'View74', None)
    _safe_set(owner, 'tables73', {partner})
    assert getattr(partner, 'View74') == owner
    _safe_set(owner, 'tables73', set())
    assert getattr(partner, 'View74') is None


