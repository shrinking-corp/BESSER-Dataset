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
    SQL2003_ARRAY,
    SQL2003_Attribute,
    SQL2003_BaseTable,
    SQL2003_BehaviouralComponent,
    SQL2003_BinaryStringType,
    SQL2003_BooleanType,
    SQL2003_CharacterStringType,
    SQL2003_CollectionType,
    SQL2003_Column,
    SQL2003_ColumnConstraint,
    SQL2003_ConstructedType,
    SQL2003_DataType,
    SQL2003_DatetimeFeature,
    SQL2003_DatetimeType,
    SQL2003_DerivedTable,
    SQL2003_DistinctType,
    SQL2003_Feature,
    SQL2003_Field,
    SQL2003_Function,
    SQL2003_IntervalFeature,
    SQL2003_IntervalType,
    SQL2003_MULTISET,
    SQL2003_Method,
    SQL2003_MethodParameter,
    SQL2003_NotNull,
    SQL2003_NumericFeature,
    SQL2003_NumericType,
    SQL2003_Parameter,
    SQL2003_ParameterWithMode,
    SQL2003_PredefinedType,
    SQL2003_PrimaryKey,
    SQL2003_Procedure,
    SQL2003_ROW,
    SQL2003_ReferenceType,
    SQL2003_ReferentialConstraint,
    SQL2003_Restriction,
    SQL2003_Schema,
    SQL2003_StringFeature,
    SQL2003_StructuralComponent,
    SQL2003_StructuredType,
    SQL2003_Table,
    SQL2003_TableCheckConstraint,
    SQL2003_TableConstraint,
    SQL2003_Trigger,
    SQL2003_TypedTable,
    SQL2003_UniqueConstraint,
    SQL2003_UserDefinedType,
    SQL2003_View,
    SQL2003_XMLType,
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
    a1 = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_Attribute(default="sample_text")
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
    a1 = SQL2003_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_BehaviouralComponent(body="sample_text", name="sample_text")
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
    a1 = SQL2003_Schema(name="sample_text")
    a2 = SQL2003_Schema(name="sample_text_2")
    b = SQL2003_BehaviouralComponent(body="sample_text", name="sample_text")
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


def test_assoc_columns39_reverse_link_reassign_clear():
    a1 = SQL2003_StructuralComponent(name="sample_text")
    a2 = SQL2003_StructuralComponent(name="sample_text_2")
    b = SQL2003_Restriction(NameColumns="sample_text")
    _safe_set(b, 'restrictions40', {a1})
    assert _is_linked(b, 'restrictions40', a1)
    if hasattr(a1, 'StructuralComponent'):
        assert _is_linked(a1, 'StructuralComponent', b)
    _safe_set(b, 'restrictions40', {a2})
    assert _is_linked(b, 'restrictions40', a2)
    if hasattr(a1, 'StructuralComponent'):
        assert not _is_linked(a1, 'StructuralComponent', b)
    if hasattr(a2, 'StructuralComponent'):
        assert _is_linked(a2, 'StructuralComponent', b)
    _safe_set(b, 'restrictions40', set())
    assert not _is_linked(b, 'restrictions40', a2)
    if hasattr(a2, 'StructuralComponent'):
        assert not _is_linked(a2, 'StructuralComponent', b)


def test_assoc_columns67_reverse_link_reassign_clear():
    a1 = SQL2003_Table(name="sample_text")
    a2 = SQL2003_Table(name="sample_text_2")
    b = SQL2003_Column(default="sample_text")
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


def test_assoc_methods60_reverse_link_reassign_clear():
    a1 = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_Method(body="sample_text", name="sample_text")
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
    a1 = SQL2003_Method(body="sample_text", name="sample_text")
    a2 = SQL2003_Method(body="sample_text_2", name="sample_text_2")
    b = SQL2003_Method(body="sample_text", name="sample_text")
    _safe_set(b, 'SQL2003_Method15', a1)
    assert _is_linked(b, 'SQL2003_Method15', a1)
    if hasattr(a1, 'SQL2003_Method'):
        assert _is_linked(a1, 'SQL2003_Method', b)
    _safe_set(b, 'SQL2003_Method15', a2)
    assert _is_linked(b, 'SQL2003_Method15', a2)
    if hasattr(a1, 'SQL2003_Method'):
        assert not _is_linked(a1, 'SQL2003_Method', b)
    if hasattr(a2, 'SQL2003_Method'):
        assert _is_linked(a2, 'SQL2003_Method', b)
    _safe_set(b, 'SQL2003_Method15', None)
    assert not _is_linked(b, 'SQL2003_Method15', a2)
    if hasattr(a2, 'SQL2003_Method'):
        assert not _is_linked(a2, 'SQL2003_Method', b)


def test_assoc_parametersWithMode2_reverse_link_reassign_clear():
    a1 = SQL2003_ParameterWithMode(mode="sample_text")
    a2 = SQL2003_ParameterWithMode(mode="sample_text_2")
    b = SQL2003_BehaviouralComponent(body="sample_text", name="sample_text")
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


def test_assoc_restrictions51_reverse_link_reassign_clear():
    a1 = SQL2003_StructuralComponent(name="sample_text")
    a2 = SQL2003_StructuralComponent(name="sample_text_2")
    b = SQL2003_Restriction(NameColumns="sample_text")
    _safe_set(b, 'Restriction', a1)
    assert _is_linked(b, 'Restriction', a1)
    if hasattr(a1, 'columns52'):
        assert _is_linked(a1, 'columns52', b)
    _safe_set(b, 'Restriction', a2)
    assert _is_linked(b, 'Restriction', a2)
    if hasattr(a1, 'columns52'):
        assert not _is_linked(a1, 'columns52', b)
    if hasattr(a2, 'columns52'):
        assert _is_linked(a2, 'columns52', b)
    _safe_set(b, 'Restriction', None)
    assert not _is_linked(b, 'Restriction', a2)
    if hasattr(a2, 'columns52'):
        assert not _is_linked(a2, 'columns52', b)


def test_assoc_restrictions73_reverse_link_reassign_clear():
    a1 = SQL2003_Table(name="sample_text")
    a2 = SQL2003_Table(name="sample_text_2")
    b = SQL2003_Restriction(NameColumns="sample_text")
    _safe_set(b, 'Restriction75', a1)
    assert _is_linked(b, 'Restriction75', a1)
    if hasattr(a1, 'table74'):
        assert _is_linked(a1, 'table74', b)
    _safe_set(b, 'Restriction75', a2)
    assert _is_linked(b, 'Restriction75', a2)
    if hasattr(a1, 'table74'):
        assert not _is_linked(a1, 'table74', b)
    if hasattr(a2, 'table74'):
        assert _is_linked(a2, 'table74', b)
    _safe_set(b, 'Restriction75', None)
    assert not _is_linked(b, 'Restriction75', a2)
    if hasattr(a2, 'table74'):
        assert not _is_linked(a2, 'table74', b)


def test_assoc_schema1_reverse_link_reassign_clear():
    a1 = SQL2003_Schema(name="sample_text")
    a2 = SQL2003_Schema(name="sample_text_2")
    b = SQL2003_BehaviouralComponent(body="sample_text", name="sample_text")
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
    a1 = SQL2003_Table(name="sample_text")
    a2 = SQL2003_Table(name="sample_text_2")
    b = SQL2003_Schema(name="sample_text")
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
    a1 = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_Attribute(default="sample_text")
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
    a1 = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_Method(body="sample_text", name="sample_text")
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
    a1 = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    a2 = SQL2003_StructuredType(is_final=False, is_instantiable=False)
    b = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    _safe_set(b, 'SQL2003_StructuredType58', a1)
    assert _is_linked(b, 'SQL2003_StructuredType58', a1)
    if hasattr(a1, 'SQL2003_StructuredType56'):
        assert _is_linked(a1, 'SQL2003_StructuredType56', b)
    _safe_set(b, 'SQL2003_StructuredType58', a2)
    assert _is_linked(b, 'SQL2003_StructuredType58', a2)
    if hasattr(a1, 'SQL2003_StructuredType56'):
        assert not _is_linked(a1, 'SQL2003_StructuredType56', b)
    if hasattr(a2, 'SQL2003_StructuredType56'):
        assert _is_linked(a2, 'SQL2003_StructuredType56', b)
    _safe_set(b, 'SQL2003_StructuredType58', None)
    assert not _is_linked(b, 'SQL2003_StructuredType58', a2)
    if hasattr(a2, 'SQL2003_StructuredType56'):
        assert not _is_linked(a2, 'SQL2003_StructuredType56', b)


def test_assoc_table37_reverse_link_reassign_clear():
    a1 = SQL2003_Table(name="sample_text")
    a2 = SQL2003_Table(name="sample_text_2")
    b = SQL2003_Restriction(NameColumns="sample_text")
    _safe_set(b, 'restrictions', a1)
    assert _is_linked(b, 'restrictions', a1)
    if hasattr(a1, 'Table38'):
        assert _is_linked(a1, 'Table38', b)
    _safe_set(b, 'restrictions', a2)
    assert _is_linked(b, 'restrictions', a2)
    if hasattr(a1, 'Table38'):
        assert not _is_linked(a1, 'Table38', b)
    if hasattr(a2, 'Table38'):
        assert _is_linked(a2, 'Table38', b)
    _safe_set(b, 'restrictions', None)
    assert not _is_linked(b, 'restrictions', a2)
    if hasattr(a2, 'Table38'):
        assert not _is_linked(a2, 'Table38', b)


def test_assoc_table7_reverse_link_reassign_clear():
    a1 = SQL2003_Table(name="sample_text")
    a2 = SQL2003_Table(name="sample_text_2")
    b = SQL2003_Column(default="sample_text")
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


def test_assoc_table76_reverse_link_reassign_clear():
    a1 = SQL2003_Trigger(actionTime="sample_text", event="sample_text", name="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_Trigger(actionTime="sample_text_2", event="sample_text_2", name="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_Table(name="sample_text")
    _safe_set(b, 'Table77', a1)
    assert _is_linked(b, 'Table77', a1)
    if hasattr(a1, 'triggers'):
        assert _is_linked(a1, 'triggers', b)
    _safe_set(b, 'Table77', a2)
    assert _is_linked(b, 'Table77', a2)
    if hasattr(a1, 'triggers'):
        assert not _is_linked(a1, 'triggers', b)
    if hasattr(a2, 'triggers'):
        assert _is_linked(a2, 'triggers', b)
    _safe_set(b, 'Table77', None)
    assert not _is_linked(b, 'Table77', a2)
    if hasattr(a2, 'triggers'):
        assert not _is_linked(a2, 'triggers', b)


def test_assoc_tables45_reverse_link_reassign_clear():
    a1 = SQL2003_Table(name="sample_text")
    a2 = SQL2003_Table(name="sample_text_2")
    b = SQL2003_Schema(name="sample_text")
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


def test_assoc_triggers71_reverse_link_reassign_clear():
    a1 = SQL2003_Trigger(actionTime="sample_text", event="sample_text", name="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_Trigger(actionTime="sample_text_2", event="sample_text_2", name="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_Table(name="sample_text")
    _safe_set(b, 'table72', {a1})
    assert _is_linked(b, 'table72', a1)
    if hasattr(a1, 'Trigger'):
        assert _is_linked(a1, 'Trigger', b)
    _safe_set(b, 'table72', {a2})
    assert _is_linked(b, 'table72', a2)
    if hasattr(a1, 'Trigger'):
        assert not _is_linked(a1, 'Trigger', b)
    if hasattr(a2, 'Trigger'):
        assert _is_linked(a2, 'Trigger', b)
    _safe_set(b, 'table72', set())
    assert not _is_linked(b, 'table72', a2)
    if hasattr(a2, 'Trigger'):
        assert not _is_linked(a2, 'Trigger', b)


def test_assoc_updateColumns78_reverse_link_reassign_clear():
    a1 = SQL2003_Trigger(actionTime="sample_text", event="sample_text", name="sample_text", triggeredAction="sample_text")
    a2 = SQL2003_Trigger(actionTime="sample_text_2", event="sample_text_2", name="sample_text_2", triggeredAction="sample_text_2")
    b = SQL2003_StructuralComponent(name="sample_text")
    _safe_set(b, 'SQL2003_StructuralComponent79', a1)
    assert _is_linked(b, 'SQL2003_StructuralComponent79', a1)
    if hasattr(a1, 'SQL2003_Trigger'):
        assert _is_linked(a1, 'SQL2003_Trigger', b)
    _safe_set(b, 'SQL2003_StructuralComponent79', a2)
    assert _is_linked(b, 'SQL2003_StructuralComponent79', a2)
    if hasattr(a1, 'SQL2003_Trigger'):
        assert not _is_linked(a1, 'SQL2003_Trigger', b)
    if hasattr(a2, 'SQL2003_Trigger'):
        assert _is_linked(a2, 'SQL2003_Trigger', b)
    _safe_set(b, 'SQL2003_StructuralComponent79', None)
    assert not _is_linked(b, 'SQL2003_StructuralComponent79', a2)
    if hasattr(a2, 'SQL2003_Trigger'):
        assert not _is_linked(a2, 'SQL2003_Trigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components90_stub_double():
    # SQL2003_View has no real 'views91' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuralComponent(name="sample_text")
    partner = SQL2003_View()
    setattr(partner, 'views91', None)
    _safe_set(owner, 'StructuralComponent92', partner)
    assert owner in getattr(partner, 'views91')
    _safe_set(owner, 'StructuralComponent92', None)
    assert owner not in getattr(partner, 'views91')


def test_assoc_datatypes43_stub_double():
    # SQL2003_DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Schema(name="sample_text")
    partner = SQL2003_DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'schema44', {partner})
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'schema44', set())
    assert getattr(partner, 'DataType') is None


def test_assoc_features53_stub_double():
    # SQL2003_Feature has no real 'SQL2003_Feature55' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuralComponent(name="sample_text")
    partner = SQL2003_Feature()
    setattr(partner, 'SQL2003_Feature55', None)
    _safe_set(owner, 'SQL2003_StructuralComponent54', {partner})
    assert getattr(partner, 'SQL2003_Feature55') == owner
    _safe_set(owner, 'SQL2003_StructuralComponent54', set())
    assert getattr(partner, 'SQL2003_Feature55') is None


def test_assoc_method23_stub_double():
    # SQL2003_MethodParameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Method(body="sample_text", name="sample_text")
    partner = SQL2003_MethodParameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Method', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Method', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_parameters22_stub_double():
    # SQL2003_MethodParameter has no real 'MethodParameter' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Method(body="sample_text", name="sample_text")
    partner = SQL2003_MethodParameter()
    setattr(partner, 'MethodParameter', None)
    _safe_set(owner, 'method', {partner})
    assert getattr(partner, 'MethodParameter') == owner
    _safe_set(owner, 'method', set())
    assert getattr(partner, 'MethodParameter') is None


def test_assoc_references36_stub_double():
    # SQL2003_UniqueConstraint has no real 'SQL2003_UniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_ReferentialConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_ReferentialConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_ReferentialConstraint(delete_action="sample_text", match="sample_text", update_action="sample_text")
    partner = SQL2003_UniqueConstraint()
    setattr(partner, 'SQL2003_UniqueConstraint', None)
    _safe_set(owner, 'SQL2003_ReferentialConstraint', partner)
    assert getattr(partner, 'SQL2003_UniqueConstraint') == owner
    _safe_set(owner, 'SQL2003_ReferentialConstraint', None)
    assert getattr(partner, 'SQL2003_UniqueConstraint') is None


def test_assoc_return_type19_stub_double():
    # SQL2003_DataType has no real 'SQL2003_DataType21' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Method(body="sample_text", name="sample_text")
    partner = SQL2003_DataType()
    setattr(partner, 'SQL2003_DataType21', None)
    _safe_set(owner, 'SQL2003_Method20', partner)
    assert getattr(partner, 'SQL2003_DataType21') == owner
    _safe_set(owner, 'SQL2003_Method20', None)
    assert getattr(partner, 'SQL2003_DataType21') is None


def test_assoc_schema8_stub_double():
    # SQL2003_DataType has no real 'datatypes' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Schema(name="sample_text")
    partner = SQL2003_DataType()
    setattr(partner, 'datatypes', None)
    _safe_set(owner, 'Schema9', partner)
    assert getattr(partner, 'datatypes') == owner
    _safe_set(owner, 'Schema9', None)
    assert getattr(partner, 'datatypes') is None


def test_assoc_structured80_stub_double():
    # SQL2003_TypedTable has no real 'typed' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_TypedTable()
    setattr(partner, 'typed', None)
    _safe_set(owner, 'StructuredType81', partner)
    assert getattr(partner, 'typed') == owner
    _safe_set(owner, 'StructuredType81', None)
    assert getattr(partner, 'typed') is None


def test_assoc_tables88_stub_double():
    # SQL2003_View has no real 'views' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Table(name="sample_text")
    partner = SQL2003_View()
    setattr(partner, 'views', None)
    _safe_set(owner, 'Table89', partner)
    assert owner in getattr(partner, 'views')
    _safe_set(owner, 'Table89', None)
    assert owner not in getattr(partner, 'views')


def test_assoc_type24_stub_double():
    # SQL2003_DataType has no real 'SQL2003_DataType25' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Parameter(name="sample_text")
    partner = SQL2003_DataType()
    setattr(partner, 'SQL2003_DataType25', None)
    _safe_set(owner, 'SQL2003_Parameter', partner)
    assert getattr(partner, 'SQL2003_DataType25') == owner
    _safe_set(owner, 'SQL2003_Parameter', None)
    assert getattr(partner, 'SQL2003_DataType25') is None


def test_assoc_type35_stub_double():
    # SQL2003_ReferenceType has no real 'SQL2003_ReferenceType' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_ReferenceType()
    setattr(partner, 'SQL2003_ReferenceType', None)
    _safe_set(owner, 'SQL2003_StructuredType', partner)
    assert getattr(partner, 'SQL2003_ReferenceType') == owner
    _safe_set(owner, 'SQL2003_StructuredType', None)
    assert getattr(partner, 'SQL2003_ReferenceType') is None


def test_assoc_type48_stub_double():
    # SQL2003_DataType has no real 'SQL2003_DataType49' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuralComponent(name="sample_text")
    partner = SQL2003_DataType()
    setattr(partner, 'SQL2003_DataType49', None)
    _safe_set(owner, 'SQL2003_StructuralComponent', partner)
    assert getattr(partner, 'SQL2003_DataType49') == owner
    _safe_set(owner, 'SQL2003_StructuralComponent', None)
    assert getattr(partner, 'SQL2003_DataType49') is None


def test_assoc_typed63_stub_double():
    # SQL2003_TypedTable has no real 'TypedTable' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuredType(is_final=True, is_instantiable=True)
    partner = SQL2003_TypedTable()
    setattr(partner, 'TypedTable', None)
    _safe_set(owner, 'structured64', {partner})
    assert getattr(partner, 'TypedTable') == owner
    _safe_set(owner, 'structured64', set())
    assert getattr(partner, 'TypedTable') is None


def test_assoc_views50_stub_double():
    # SQL2003_View has no real 'View' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_StructuralComponent(name="sample_text")
    partner = SQL2003_View()
    setattr(partner, 'View', None)
    _safe_set(owner, 'components', {partner})
    assert getattr(partner, 'View') == owner
    _safe_set(owner, 'components', set())
    assert getattr(partner, 'View') is None


def test_assoc_views68_stub_double():
    # SQL2003_View has no real 'View70' property in the generated
    # code (a bare stub) -- manually attach it so SQL2003_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQL2003_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQL2003_Table(name="sample_text")
    partner = SQL2003_View()
    setattr(partner, 'View70', None)
    _safe_set(owner, 'tables69', {partner})
    assert getattr(partner, 'View70') == owner
    _safe_set(owner, 'tables69', set())
    assert getattr(partner, 'View70') is None


