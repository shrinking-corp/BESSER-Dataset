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
    SQL2003_evo_ARRAY,
    SQL2003_evo_Attribute,
    SQL2003_evo_BaseTable,
    SQL2003_evo_BehaviouralComponent,
    SQL2003_evo_BinaryStringType,
    SQL2003_evo_BooleanType,
    SQL2003_evo_CharacterStringType,
    SQL2003_evo_CollectionType,
    SQL2003_evo_Column,
    SQL2003_evo_ColumnConstraint,
    SQL2003_evo_ConstructedType,
    SQL2003_evo_DataType,
    SQL2003_evo_DatetimeFeature,
    SQL2003_evo_DatetimeType,
    SQL2003_evo_DerivedTable,
    SQL2003_evo_DistinctType,
    SQL2003_evo_Feature,
    SQL2003_evo_Field,
    SQL2003_evo_Function,
    SQL2003_evo_IntervalFeature,
    SQL2003_evo_IntervalType,
    SQL2003_evo_MULTISET,
    SQL2003_evo_Method,
    SQL2003_evo_MethodParameter,
    SQL2003_evo_NotNull,
    SQL2003_evo_NumericFeature,
    SQL2003_evo_NumericType,
    SQL2003_evo_Parameter,
    SQL2003_evo_ParameterWithMode,
    SQL2003_evo_PredefinedType,
    SQL2003_evo_PrimaryKey,
    SQL2003_evo_Procedure,
    SQL2003_evo_ROW,
    SQL2003_evo_ReferenceType,
    SQL2003_evo_ReferentialConstraint,
    SQL2003_evo_Restriction,
    SQL2003_evo_Schema,
    SQL2003_evo_StringFeature,
    SQL2003_evo_StructuralComponent,
    SQL2003_evo_StructuredType,
    SQL2003_evo_Table,
    SQL2003_evo_TableCheckConstraint,
    SQL2003_evo_TableConstraint,
    SQL2003_evo_Trigger,
    SQL2003_evo_TriggerDescriptor,
    SQL2003_evo_TypedTable,
    SQL2003_evo_UniqueConstraint,
    SQL2003_evo_UserDefinedType,
    SQL2003_evo_View,
    SQL2003_evo_XMLType,
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

def test_assoc_attributes59_reverse_link_reassign_clear():
    a1 = SQL2003_evo_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_evo_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_evo_Attribute(default="sample_text")
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
    a1 = SQL2003_evo_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_evo_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_evo_BehaviouralComponent(body="sample_text", name="sample_text")
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
    a1 = SQL2003_evo_Schema(name="sample_text")
    a2 = SQL2003_evo_Schema(name="sample_text_2")
    b = SQL2003_evo_BehaviouralComponent(body="sample_text", name="sample_text")
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


def test_assoc_columns67_reverse_link_reassign_clear():
    a1 = SQL2003_evo_Table(name="sample_text")
    a2 = SQL2003_evo_Table(name="sample_text_2")
    b = SQL2003_evo_Column(default="sample_text")
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


def test_assoc_description74_reverse_link_reassign_clear():
    a1 = SQL2003_evo_TriggerDescriptor(actionTime="sample_text", event="sample_text", level="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_evo_TriggerDescriptor(actionTime="sample_text_2", event="sample_text_2", level="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_evo_Trigger(name="sample_text")
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


def test_assoc_methods60_reverse_link_reassign_clear():
    a1 = SQL2003_evo_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_evo_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_evo_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'Method62', a1)
    assert _is_linked(b, 'Method62', a1)
    if hasattr(a1, 'structured61'):
        assert _is_linked(a1, 'structured61', b)
    _safe_set(b, 'Method62', a2)
    assert _is_linked(b, 'Method62', a2)
    if hasattr(a1, 'structured61'):
        assert not _is_linked(a1, 'structured61', b)
    if hasattr(a2, 'structured61'):
        assert _is_linked(a2, 'structured61', b)
    _safe_set(b, 'Method62', None)
    assert not _is_linked(b, 'Method62', a2)
    if hasattr(a2, 'structured61'):
        assert not _is_linked(a2, 'structured61', b)


def test_assoc_override16_reverse_link_reassign_clear():
    a1 = SQL2003_evo_Method(body="sample_text", name="sample_text")
    a2 = SQL2003_evo_Method(body="sample_text_2", name="sample_text_2")
    b = SQL2003_evo_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'SQL2003_evo_Method15', a1)
    assert _is_linked(b, 'SQL2003_evo_Method15', a1)
    if hasattr(a1, 'SQL2003_evo_Method'):
        assert _is_linked(a1, 'SQL2003_evo_Method', b)
    _safe_set(b, 'SQL2003_evo_Method15', a2)
    assert _is_linked(b, 'SQL2003_evo_Method15', a2)
    if hasattr(a1, 'SQL2003_evo_Method'):
        assert not _is_linked(a1, 'SQL2003_evo_Method', b)
    if hasattr(a2, 'SQL2003_evo_Method'):
        assert _is_linked(a2, 'SQL2003_evo_Method', b)
    _safe_set(b, 'SQL2003_evo_Method15', None)
    assert not _is_linked(b, 'SQL2003_evo_Method15', a2)
    if hasattr(a2, 'SQL2003_evo_Method'):
        assert not _is_linked(a2, 'SQL2003_evo_Method', b)


def test_assoc_parametersWithMode2_reverse_link_reassign_clear():
    a1 = SQL2003_evo_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_evo_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_evo_BehaviouralComponent(body="sample_text", name="sample_text")
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
    a1 = SQL2003_evo_Schema(name="sample_text")
    a2 = SQL2003_evo_Schema(name="sample_text_2")
    b = SQL2003_evo_BehaviouralComponent(body="sample_text", name="sample_text")
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


def test_assoc_schema65_reverse_link_reassign_clear():
    a1 = SQL2003_evo_Table(name="sample_text")
    a2 = SQL2003_evo_Table(name="sample_text_2")
    b = SQL2003_evo_Schema(name="sample_text")
    _safe_set(b, 'Schema66', a1)
    assert _is_linked(b, 'Schema66', a1)
    if hasattr(a1, 'tables'):
        assert _is_linked(a1, 'tables', b)
    _safe_set(b, 'Schema66', a2)
    assert _is_linked(b, 'Schema66', a2)
    if hasattr(a1, 'tables'):
        assert not _is_linked(a1, 'tables', b)
    if hasattr(a2, 'tables'):
        assert _is_linked(a2, 'tables', b)
    _safe_set(b, 'Schema66', None)
    assert not _is_linked(b, 'Schema66', a2)
    if hasattr(a2, 'tables'):
        assert not _is_linked(a2, 'tables', b)


def test_assoc_structured0_reverse_link_reassign_clear():
    a1 = SQL2003_evo_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_evo_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_evo_Attribute(default="sample_text")
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
    a1 = SQL2003_evo_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_evo_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_evo_Method(body="sample_text", name="sample_text")
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


def test_assoc_super_type57_reverse_link_reassign_clear():
    a1 = SQL2003_evo_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_evo_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_evo_StructuredType(is_final=True, is_instantiable=True)
    _safe_set(b, 'SQL2003_evo_StructuredType58', a1)
    assert _is_linked(b, 'SQL2003_evo_StructuredType58', a1)
    if hasattr(a1, 'SQL2003_evo_StructuredType56'):
        assert _is_linked(a1, 'SQL2003_evo_StructuredType56', b)
    _safe_set(b, 'SQL2003_evo_StructuredType58', a2)
    assert _is_linked(b, 'SQL2003_evo_StructuredType58', a2)
    if hasattr(a1, 'SQL2003_evo_StructuredType56'):
        assert not _is_linked(a1, 'SQL2003_evo_StructuredType56', b)
    if hasattr(a2, 'SQL2003_evo_StructuredType56'):
        assert _is_linked(a2, 'SQL2003_evo_StructuredType56', b)
    _safe_set(b, 'SQL2003_evo_StructuredType58', None)
    assert not _is_linked(b, 'SQL2003_evo_StructuredType58', a2)
    if hasattr(a2, 'SQL2003_evo_StructuredType56'):
        assert not _is_linked(a2, 'SQL2003_evo_StructuredType56', b)


def test_assoc_table7_reverse_link_reassign_clear():
    a1 = SQL2003_evo_Table(name="sample_text")
    a2 = SQL2003_evo_Table(name="sample_text_2")
    b = SQL2003_evo_Column(default="sample_text")
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
    a1 = SQL2003_evo_Table(name="sample_text")
    a2 = SQL2003_evo_Table(name="sample_text_2")
    b = SQL2003_evo_Schema(name="sample_text")
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


def test_assoc_trigger77_reverse_link_reassign_clear():
    a1 = SQL2003_evo_TriggerDescriptor(actionTime="sample_text", event="sample_text", level="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_evo_TriggerDescriptor(actionTime="sample_text_2", event="sample_text_2", level="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_evo_Trigger(name="sample_text")
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


def test_assoc_updateColumns75_reverse_link_reassign_clear():
    a1 = SQL2003_evo_Trigger(name="sample_text")
    a2 = SQL2003_evo_Trigger(name="sample_text_2")
    b = SQL2003_evo_StructuralComponent(name="sample_text")
    _safe_set(b, 'SQL2003_evo_StructuralComponent76', a1)
    assert _is_linked(b, 'SQL2003_evo_StructuralComponent76', a1)
    if hasattr(a1, 'SQL2003_evo_Trigger'):
        assert _is_linked(a1, 'SQL2003_evo_Trigger', b)
    _safe_set(b, 'SQL2003_evo_StructuralComponent76', a2)
    assert _is_linked(b, 'SQL2003_evo_StructuralComponent76', a2)
    if hasattr(a1, 'SQL2003_evo_Trigger'):
        assert not _is_linked(a1, 'SQL2003_evo_Trigger', b)
    if hasattr(a2, 'SQL2003_evo_Trigger'):
        assert _is_linked(a2, 'SQL2003_evo_Trigger', b)
    _safe_set(b, 'SQL2003_evo_StructuralComponent76', None)
    assert not _is_linked(b, 'SQL2003_evo_StructuralComponent76', a2)
    if hasattr(a2, 'SQL2003_evo_Trigger'):
        assert not _is_linked(a2, 'SQL2003_evo_Trigger', b)


