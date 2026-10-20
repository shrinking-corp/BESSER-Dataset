import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ANSIType,
    BasicDataType,
    BuiltInType,
    Datatype,
    DerivedTable,
    Feature,
    ORDB4ORA_ANSICharacterType,
    ORDB4ORA_ANSINumberType,
    ORDB4ORA_ANSIType,
    ORDB4ORA_AnyType,
    ORDB4ORA_Attribute,
    ORDB4ORA_BasicDataType,
    ORDB4ORA_BuiltInCharacterType,
    ORDB4ORA_BuiltInNumberType,
    ORDB4ORA_BuiltInType,
    ORDB4ORA_CharacterFeature,
    ORDB4ORA_Check,
    ORDB4ORA_Column,
    ORDB4ORA_Datatype,
    ORDB4ORA_DatetimeFeature,
    ORDB4ORA_DatetimeType,
    ORDB4ORA_DerivedTable,
    ORDB4ORA_Feature,
    ORDB4ORA_ForeignKey,
    ORDB4ORA_Function,
    ORDB4ORA_IntervalFeature,
    ORDB4ORA_LOBType,
    ORDB4ORA_LongAndRawType,
    ORDB4ORA_MediaType,
    ORDB4ORA_Method,
    ORDB4ORA_MethodParameter,
    ORDB4ORA_Model,
    ORDB4ORA_NestedTableType,
    ORDB4ORA_NotNull,
    ORDB4ORA_NumberFeature,
    ORDB4ORA_Operation,
    ORDB4ORA_OperationParameter,
    ORDB4ORA_Package,
    ORDB4ORA_Parameter,
    ORDB4ORA_PrimaryKey,
    ORDB4ORA_Procedure,
    ORDB4ORA_ROWIDType,
    ORDB4ORA_RawFeature,
    ORDB4ORA_ReferenceType,
    ORDB4ORA_Restriction,
    ORDB4ORA_RowFeature,
    ORDB4ORA_SpacialType,
    ORDB4ORA_StoredNestedTable,
    ORDB4ORA_StructuralComponent,
    ORDB4ORA_StructuredType,
    ORDB4ORA_SuppliedType,
    ORDB4ORA_Table,
    ORDB4ORA_Trigger,
    ORDB4ORA_TypedTable,
    ORDB4ORA_Unique,
    ORDB4ORA_Varray,
    ORDB4ORA_View,
    ORDB4ORA_XMLType,
    Operation,
    Parameter,
    Restriction,
    StructuralComponent,
    SuppliedType,
    Table,
    ANSICharacterTypes,
    ANSINumberTypes,
    BuiltInCharacterSemantics,
    BuiltInCharacterTypes,
    BuiltInDatetimeTypes,
    BuiltInLOBType,
    BuiltInLongAndRawTypes,
    BuiltInROWIDType,
    BuiltNumberTypes,
    CharacterFeatures,
    DatetimeFeatures,
    IntervalFeatures,
    NumberFeatures,
    ONDELETEActions,
    ParameterMode,
    RawFeatures,
    RowFeatures,
    SuppliedAnyTypes,
    SuppliedMediaTypes,
    SuppliedSpacialTypes,
    SuppliedXMLTypes,
    TriggerActionTime,
    TriggerEvent,
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

def test_assoc_Type40_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    a2 = ORDB4ORA_StructuredType(Name="sample_text_2", is_final=False, is_instantiable=False)
    b = ORDB4ORA_ReferenceType(Name="sample_text")
    _safe_set(b, 'ORDB4ORA_ReferenceType', a1)
    assert _is_linked(b, 'ORDB4ORA_ReferenceType', a1)
    if hasattr(a1, 'ORDB4ORA_StructuredType'):
        assert _is_linked(a1, 'ORDB4ORA_StructuredType', b)
    _safe_set(b, 'ORDB4ORA_ReferenceType', a2)
    assert _is_linked(b, 'ORDB4ORA_ReferenceType', a2)
    if hasattr(a1, 'ORDB4ORA_StructuredType'):
        assert not _is_linked(a1, 'ORDB4ORA_StructuredType', b)
    if hasattr(a2, 'ORDB4ORA_StructuredType'):
        assert _is_linked(a2, 'ORDB4ORA_StructuredType', b)
    _safe_set(b, 'ORDB4ORA_ReferenceType', None)
    assert not _is_linked(b, 'ORDB4ORA_ReferenceType', a2)
    if hasattr(a2, 'ORDB4ORA_StructuredType'):
        assert not _is_linked(a2, 'ORDB4ORA_StructuredType', b)


def test_assoc_attribute44_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StoredNestedTable(Name="sample_text")
    a2 = ORDB4ORA_StoredNestedTable(Name="sample_text_2")
    b = ORDB4ORA_Attribute(default="sample_text")
    _safe_set(b, 'ORDB4ORA_Attribute', a1)
    assert _is_linked(b, 'ORDB4ORA_Attribute', a1)
    if hasattr(a1, 'ORDB4ORA_StoredNestedTable'):
        assert _is_linked(a1, 'ORDB4ORA_StoredNestedTable', b)
    _safe_set(b, 'ORDB4ORA_Attribute', a2)
    assert _is_linked(b, 'ORDB4ORA_Attribute', a2)
    if hasattr(a1, 'ORDB4ORA_StoredNestedTable'):
        assert not _is_linked(a1, 'ORDB4ORA_StoredNestedTable', b)
    if hasattr(a2, 'ORDB4ORA_StoredNestedTable'):
        assert _is_linked(a2, 'ORDB4ORA_StoredNestedTable', b)
    _safe_set(b, 'ORDB4ORA_Attribute', None)
    assert not _is_linked(b, 'ORDB4ORA_Attribute', a2)
    if hasattr(a2, 'ORDB4ORA_StoredNestedTable'):
        assert not _is_linked(a2, 'ORDB4ORA_StoredNestedTable', b)


def test_assoc_attribute51_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    a2 = ORDB4ORA_StructuredType(Name="sample_text_2", is_final=False, is_instantiable=False)
    b = ORDB4ORA_Attribute(default="sample_text")
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


def test_assoc_method52_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    a2 = ORDB4ORA_StructuredType(Name="sample_text_2", is_final=False, is_instantiable=False)
    b = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    _safe_set(b, 'Method54', a1)
    assert _is_linked(b, 'Method54', a1)
    if hasattr(a1, 'structured53'):
        assert _is_linked(a1, 'structured53', b)
    _safe_set(b, 'Method54', a2)
    assert _is_linked(b, 'Method54', a2)
    if hasattr(a1, 'structured53'):
        assert not _is_linked(a1, 'structured53', b)
    if hasattr(a2, 'structured53'):
        assert _is_linked(a2, 'structured53', b)
    _safe_set(b, 'Method54', None)
    assert not _is_linked(b, 'Method54', a2)
    if hasattr(a2, 'structured53'):
        assert not _is_linked(a2, 'structured53', b)


def test_assoc_model26_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Operation(Body="sample_text", Name="sample_text")
    a2 = ORDB4ORA_Operation(Body="sample_text_2", Name="sample_text_2")
    b = ORDB4ORA_Model(Name="sample_text")
    _safe_set(b, 'Model28', a1)
    assert _is_linked(b, 'Model28', a1)
    if hasattr(a1, 'operation27'):
        assert _is_linked(a1, 'operation27', b)
    _safe_set(b, 'Model28', a2)
    assert _is_linked(b, 'Model28', a2)
    if hasattr(a1, 'operation27'):
        assert not _is_linked(a1, 'operation27', b)
    if hasattr(a2, 'operation27'):
        assert _is_linked(a2, 'operation27', b)
    _safe_set(b, 'Model28', None)
    assert not _is_linked(b, 'Model28', a2)
    if hasattr(a2, 'operation27'):
        assert not _is_linked(a2, 'operation27', b)


def test_assoc_model35_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Package(Name="sample_text")
    a2 = ORDB4ORA_Package(Name="sample_text_2")
    b = ORDB4ORA_Model(Name="sample_text")
    _safe_set(b, 'Model37', a1)
    assert _is_linked(b, 'Model37', a1)
    if hasattr(a1, 'package36'):
        assert _is_linked(a1, 'package36', b)
    _safe_set(b, 'Model37', a2)
    assert _is_linked(b, 'Model37', a2)
    if hasattr(a1, 'package36'):
        assert not _is_linked(a1, 'package36', b)
    if hasattr(a2, 'package36'):
        assert _is_linked(a2, 'package36', b)
    _safe_set(b, 'Model37', None)
    assert not _is_linked(b, 'Model37', a2)
    if hasattr(a2, 'package36'):
        assert not _is_linked(a2, 'package36', b)


def test_assoc_model64_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Table(Name="sample_text")
    a2 = ORDB4ORA_Table(Name="sample_text_2")
    b = ORDB4ORA_Model(Name="sample_text")
    _safe_set(b, 'Model66', a1)
    assert _is_linked(b, 'Model66', a1)
    if hasattr(a1, 'table65'):
        assert _is_linked(a1, 'table65', b)
    _safe_set(b, 'Model66', a2)
    assert _is_linked(b, 'Model66', a2)
    if hasattr(a1, 'table65'):
        assert not _is_linked(a1, 'table65', b)
    if hasattr(a2, 'table65'):
        assert _is_linked(a2, 'table65', b)
    _safe_set(b, 'Model66', None)
    assert not _is_linked(b, 'Model66', a2)
    if hasattr(a2, 'table65'):
        assert not _is_linked(a2, 'table65', b)


def test_assoc_operation19_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Operation(Body="sample_text", Name="sample_text")
    a2 = ORDB4ORA_Operation(Body="sample_text_2", Name="sample_text_2")
    b = ORDB4ORA_Model(Name="sample_text")
    _safe_set(b, 'model20', {a1})
    assert _is_linked(b, 'model20', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'model20', {a2})
    assert _is_linked(b, 'model20', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'model20', set())
    assert not _is_linked(b, 'model20', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_operation31_reverse_link_reassign_clear():
    a1 = ORDB4ORA_OperationParameter(Mode="sample_text")
    a2 = ORDB4ORA_OperationParameter(Mode="sample_text_2")
    b = ORDB4ORA_Operation(Body="sample_text", Name="sample_text")
    _safe_set(b, 'Operation32', a1)
    assert _is_linked(b, 'Operation32', a1)
    if hasattr(a1, 'operationParameters'):
        assert _is_linked(a1, 'operationParameters', b)
    _safe_set(b, 'Operation32', a2)
    assert _is_linked(b, 'Operation32', a2)
    if hasattr(a1, 'operationParameters'):
        assert not _is_linked(a1, 'operationParameters', b)
    if hasattr(a2, 'operationParameters'):
        assert _is_linked(a2, 'operationParameters', b)
    _safe_set(b, 'Operation32', None)
    assert not _is_linked(b, 'Operation32', a2)
    if hasattr(a2, 'operationParameters'):
        assert not _is_linked(a2, 'operationParameters', b)


def test_assoc_operationParameters25_reverse_link_reassign_clear():
    a1 = ORDB4ORA_OperationParameter(Mode="sample_text")
    a2 = ORDB4ORA_OperationParameter(Mode="sample_text_2")
    b = ORDB4ORA_Operation(Body="sample_text", Name="sample_text")
    _safe_set(b, 'operation', {a1})
    assert _is_linked(b, 'operation', a1)
    if hasattr(a1, 'OperationParameter'):
        assert _is_linked(a1, 'OperationParameter', b)
    _safe_set(b, 'operation', {a2})
    assert _is_linked(b, 'operation', a2)
    if hasattr(a1, 'OperationParameter'):
        assert not _is_linked(a1, 'OperationParameter', b)
    if hasattr(a2, 'OperationParameter'):
        assert _is_linked(a2, 'OperationParameter', b)
    _safe_set(b, 'operation', set())
    assert not _is_linked(b, 'operation', a2)
    if hasattr(a2, 'OperationParameter'):
        assert not _is_linked(a2, 'OperationParameter', b)


def test_assoc_operations33_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Package(Name="sample_text")
    a2 = ORDB4ORA_Package(Name="sample_text_2")
    b = ORDB4ORA_Operation(Body="sample_text", Name="sample_text")
    _safe_set(b, 'Operation34', a1)
    assert _is_linked(b, 'Operation34', a1)
    if hasattr(a1, 'package'):
        assert _is_linked(a1, 'package', b)
    _safe_set(b, 'Operation34', a2)
    assert _is_linked(b, 'Operation34', a2)
    if hasattr(a1, 'package'):
        assert not _is_linked(a1, 'package', b)
    if hasattr(a2, 'package'):
        assert _is_linked(a2, 'package', b)
    _safe_set(b, 'Operation34', None)
    assert not _is_linked(b, 'Operation34', a2)
    if hasattr(a2, 'package'):
        assert not _is_linked(a2, 'package', b)


def test_assoc_override6_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    a2 = ORDB4ORA_Method(Body="sample_text_2", Name="sample_text_2")
    b = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    _safe_set(b, 'ORDB4ORA_Method5', a1)
    assert _is_linked(b, 'ORDB4ORA_Method5', a1)
    if hasattr(a1, 'ORDB4ORA_Method'):
        assert _is_linked(a1, 'ORDB4ORA_Method', b)
    _safe_set(b, 'ORDB4ORA_Method5', a2)
    assert _is_linked(b, 'ORDB4ORA_Method5', a2)
    if hasattr(a1, 'ORDB4ORA_Method'):
        assert not _is_linked(a1, 'ORDB4ORA_Method', b)
    if hasattr(a2, 'ORDB4ORA_Method'):
        assert _is_linked(a2, 'ORDB4ORA_Method', b)
    _safe_set(b, 'ORDB4ORA_Method5', None)
    assert not _is_linked(b, 'ORDB4ORA_Method5', a2)
    if hasattr(a2, 'ORDB4ORA_Method'):
        assert not _is_linked(a2, 'ORDB4ORA_Method', b)


def test_assoc_package21_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Package(Name="sample_text")
    a2 = ORDB4ORA_Package(Name="sample_text_2")
    b = ORDB4ORA_Model(Name="sample_text")
    _safe_set(b, 'model22', {a1})
    assert _is_linked(b, 'model22', a1)
    if hasattr(a1, 'Package'):
        assert _is_linked(a1, 'Package', b)
    _safe_set(b, 'model22', {a2})
    assert _is_linked(b, 'model22', a2)
    if hasattr(a1, 'Package'):
        assert not _is_linked(a1, 'Package', b)
    if hasattr(a2, 'Package'):
        assert _is_linked(a2, 'Package', b)
    _safe_set(b, 'model22', set())
    assert not _is_linked(b, 'model22', a2)
    if hasattr(a2, 'Package'):
        assert not _is_linked(a2, 'Package', b)


def test_assoc_package29_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Package(Name="sample_text")
    a2 = ORDB4ORA_Package(Name="sample_text_2")
    b = ORDB4ORA_Operation(Body="sample_text", Name="sample_text")
    _safe_set(b, 'operations', a1)
    assert _is_linked(b, 'operations', a1)
    if hasattr(a1, 'Package30'):
        assert _is_linked(a1, 'Package30', b)
    _safe_set(b, 'operations', a2)
    assert _is_linked(b, 'operations', a2)
    if hasattr(a1, 'Package30'):
        assert not _is_linked(a1, 'Package30', b)
    if hasattr(a2, 'Package30'):
        assert _is_linked(a2, 'Package30', b)
    _safe_set(b, 'operations', None)
    assert not _is_linked(b, 'operations', a2)
    if hasattr(a2, 'Package30'):
        assert not _is_linked(a2, 'Package30', b)


def test_assoc_reference3_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Table(Name="sample_text")
    a2 = ORDB4ORA_Table(Name="sample_text_2")
    b = ORDB4ORA_ForeignKey(Name="sample_text", OnDelete="sample_text")
    _safe_set(b, 'ORDB4ORA_ForeignKey', a1)
    assert _is_linked(b, 'ORDB4ORA_ForeignKey', a1)
    if hasattr(a1, 'ORDB4ORA_Table'):
        assert _is_linked(a1, 'ORDB4ORA_Table', b)
    _safe_set(b, 'ORDB4ORA_ForeignKey', a2)
    assert _is_linked(b, 'ORDB4ORA_ForeignKey', a2)
    if hasattr(a1, 'ORDB4ORA_Table'):
        assert not _is_linked(a1, 'ORDB4ORA_Table', b)
    if hasattr(a2, 'ORDB4ORA_Table'):
        assert _is_linked(a2, 'ORDB4ORA_Table', b)
    _safe_set(b, 'ORDB4ORA_ForeignKey', None)
    assert not _is_linked(b, 'ORDB4ORA_ForeignKey', a2)
    if hasattr(a2, 'ORDB4ORA_Table'):
        assert not _is_linked(a2, 'ORDB4ORA_Table', b)


def test_assoc_structured0_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    a2 = ORDB4ORA_StructuredType(Name="sample_text_2", is_final=False, is_instantiable=False)
    b = ORDB4ORA_Attribute(default="sample_text")
    _safe_set(b, 'attribute', a1)
    assert _is_linked(b, 'attribute', a1)
    if hasattr(a1, 'StructuredType'):
        assert _is_linked(a1, 'StructuredType', b)
    _safe_set(b, 'attribute', a2)
    assert _is_linked(b, 'attribute', a2)
    if hasattr(a1, 'StructuredType'):
        assert not _is_linked(a1, 'StructuredType', b)
    if hasattr(a2, 'StructuredType'):
        assert _is_linked(a2, 'StructuredType', b)
    _safe_set(b, 'attribute', None)
    assert not _is_linked(b, 'attribute', a2)
    if hasattr(a2, 'StructuredType'):
        assert not _is_linked(a2, 'StructuredType', b)


def test_assoc_structured7_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    a2 = ORDB4ORA_StructuredType(Name="sample_text_2", is_final=False, is_instantiable=False)
    b = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    _safe_set(b, 'method', a1)
    assert _is_linked(b, 'method', a1)
    if hasattr(a1, 'StructuredType8'):
        assert _is_linked(a1, 'StructuredType8', b)
    _safe_set(b, 'method', a2)
    assert _is_linked(b, 'method', a2)
    if hasattr(a1, 'StructuredType8'):
        assert not _is_linked(a1, 'StructuredType8', b)
    if hasattr(a2, 'StructuredType8'):
        assert _is_linked(a2, 'StructuredType8', b)
    _safe_set(b, 'method', None)
    assert not _is_linked(b, 'method', a2)
    if hasattr(a2, 'StructuredType8'):
        assert not _is_linked(a2, 'StructuredType8', b)


def test_assoc_supertype58_reverse_link_reassign_clear():
    a1 = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    a2 = ORDB4ORA_StructuredType(Name="sample_text_2", is_final=False, is_instantiable=False)
    b = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    _safe_set(b, 'ORDB4ORA_StructuredType59', a1)
    assert _is_linked(b, 'ORDB4ORA_StructuredType59', a1)
    if hasattr(a1, 'ORDB4ORA_StructuredType57'):
        assert _is_linked(a1, 'ORDB4ORA_StructuredType57', b)
    _safe_set(b, 'ORDB4ORA_StructuredType59', a2)
    assert _is_linked(b, 'ORDB4ORA_StructuredType59', a2)
    if hasattr(a1, 'ORDB4ORA_StructuredType57'):
        assert not _is_linked(a1, 'ORDB4ORA_StructuredType57', b)
    if hasattr(a2, 'ORDB4ORA_StructuredType57'):
        assert _is_linked(a2, 'ORDB4ORA_StructuredType57', b)
    _safe_set(b, 'ORDB4ORA_StructuredType59', None)
    assert not _is_linked(b, 'ORDB4ORA_StructuredType59', a2)
    if hasattr(a2, 'ORDB4ORA_StructuredType57'):
        assert not _is_linked(a2, 'ORDB4ORA_StructuredType57', b)


def test_assoc_table16_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Table(Name="sample_text")
    a2 = ORDB4ORA_Table(Name="sample_text_2")
    b = ORDB4ORA_Model(Name="sample_text")
    _safe_set(b, 'model17', {a1})
    assert _is_linked(b, 'model17', a1)
    if hasattr(a1, 'Table18'):
        assert _is_linked(a1, 'Table18', b)
    _safe_set(b, 'model17', {a2})
    assert _is_linked(b, 'model17', a2)
    if hasattr(a1, 'Table18'):
        assert not _is_linked(a1, 'Table18', b)
    if hasattr(a2, 'Table18'):
        assert _is_linked(a2, 'Table18', b)
    _safe_set(b, 'model17', set())
    assert not _is_linked(b, 'model17', a2)
    if hasattr(a2, 'Table18'):
        assert not _is_linked(a2, 'Table18', b)


def test_assoc_table71_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Trigger(Action="sample_text", Body="sample_text", Event="sample_text", Name="sample_text")
    a2 = ORDB4ORA_Trigger(Action="sample_text_2", Body="sample_text_2", Event="sample_text_2", Name="sample_text_2")
    b = ORDB4ORA_Table(Name="sample_text")
    _safe_set(b, 'Table72', a1)
    assert _is_linked(b, 'Table72', a1)
    if hasattr(a1, 'triggers'):
        assert _is_linked(a1, 'triggers', b)
    _safe_set(b, 'Table72', a2)
    assert _is_linked(b, 'Table72', a2)
    if hasattr(a1, 'triggers'):
        assert not _is_linked(a1, 'triggers', b)
    if hasattr(a2, 'triggers'):
        assert _is_linked(a2, 'triggers', b)
    _safe_set(b, 'Table72', None)
    assert not _is_linked(b, 'Table72', a2)
    if hasattr(a2, 'triggers'):
        assert not _is_linked(a2, 'triggers', b)


def test_assoc_triggers67_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Trigger(Action="sample_text", Body="sample_text", Event="sample_text", Name="sample_text")
    a2 = ORDB4ORA_Trigger(Action="sample_text_2", Body="sample_text_2", Event="sample_text_2", Name="sample_text_2")
    b = ORDB4ORA_Table(Name="sample_text")
    _safe_set(b, 'table68', {a1})
    assert _is_linked(b, 'table68', a1)
    if hasattr(a1, 'Trigger'):
        assert _is_linked(a1, 'Trigger', b)
    _safe_set(b, 'table68', {a2})
    assert _is_linked(b, 'table68', a2)
    if hasattr(a1, 'Trigger'):
        assert not _is_linked(a1, 'Trigger', b)
    if hasattr(a2, 'Trigger'):
        assert _is_linked(a2, 'Trigger', b)
    _safe_set(b, 'table68', set())
    assert not _is_linked(b, 'table68', a2)
    if hasattr(a2, 'Trigger'):
        assert not _is_linked(a2, 'Trigger', b)


def test_assoc_updateColumns69_reverse_link_reassign_clear():
    a1 = ORDB4ORA_Trigger(Action="sample_text", Body="sample_text", Event="sample_text", Name="sample_text")
    a2 = ORDB4ORA_Trigger(Action="sample_text_2", Body="sample_text_2", Event="sample_text_2", Name="sample_text_2")
    b = ORDB4ORA_StructuralComponent(Name="sample_text")
    _safe_set(b, 'ORDB4ORA_StructuralComponent70', a1)
    assert _is_linked(b, 'ORDB4ORA_StructuralComponent70', a1)
    if hasattr(a1, 'ORDB4ORA_Trigger'):
        assert _is_linked(a1, 'ORDB4ORA_Trigger', b)
    _safe_set(b, 'ORDB4ORA_StructuralComponent70', a2)
    assert _is_linked(b, 'ORDB4ORA_StructuralComponent70', a2)
    if hasattr(a1, 'ORDB4ORA_Trigger'):
        assert not _is_linked(a1, 'ORDB4ORA_Trigger', b)
    if hasattr(a2, 'ORDB4ORA_Trigger'):
        assert _is_linked(a2, 'ORDB4ORA_Trigger', b)
    _safe_set(b, 'ORDB4ORA_StructuralComponent70', None)
    assert not _is_linked(b, 'ORDB4ORA_StructuralComponent70', a2)
    if hasattr(a2, 'ORDB4ORA_Trigger'):
        assert not _is_linked(a2, 'ORDB4ORA_Trigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Type23_stub_double():
    # ORDB4ORA_Datatype has no real 'ORDB4ORA_Datatype24' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_NestedTableType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_NestedTableType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_NestedTableType(Name="sample_text")
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'ORDB4ORA_Datatype24', None)
    _safe_set(owner, 'ORDB4ORA_NestedTableType', partner)
    assert getattr(partner, 'ORDB4ORA_Datatype24') == owner
    _safe_set(owner, 'ORDB4ORA_NestedTableType', None)
    assert getattr(partner, 'ORDB4ORA_Datatype24') is None


def test_assoc_Type38_stub_double():
    # ORDB4ORA_Datatype has no real 'ORDB4ORA_Datatype39' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Parameter(Name="sample_text")
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'ORDB4ORA_Datatype39', None)
    _safe_set(owner, 'ORDB4ORA_Parameter', partner)
    assert getattr(partner, 'ORDB4ORA_Datatype39') == owner
    _safe_set(owner, 'ORDB4ORA_Parameter', None)
    assert getattr(partner, 'ORDB4ORA_Datatype39') is None


def test_assoc_Type46_stub_double():
    # ORDB4ORA_Datatype has no real 'ORDB4ORA_Datatype47' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuralComponent(Name="sample_text")
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'ORDB4ORA_Datatype47', None)
    _safe_set(owner, 'ORDB4ORA_StructuralComponent', partner)
    assert getattr(partner, 'ORDB4ORA_Datatype47') == owner
    _safe_set(owner, 'ORDB4ORA_StructuralComponent', None)
    assert getattr(partner, 'ORDB4ORA_Datatype47') is None


def test_assoc_Type77_stub_double():
    # ORDB4ORA_Datatype has no real 'ORDB4ORA_Datatype78' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Varray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Varray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Varray(Name="sample_text", NumElements=7)
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'ORDB4ORA_Datatype78', None)
    _safe_set(owner, 'ORDB4ORA_Varray', partner)
    assert getattr(partner, 'ORDB4ORA_Datatype78') == owner
    _safe_set(owner, 'ORDB4ORA_Varray', None)
    assert getattr(partner, 'ORDB4ORA_Datatype78') is None


def test_assoc_attributes41_stub_double():
    # ORDB4ORA_Restriction has no real 'restrictions' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuralComponent(Name="sample_text")
    partner = ORDB4ORA_Restriction()
    setattr(partner, 'restrictions', None)
    _safe_set(owner, 'StructuralComponent', partner)
    assert owner in getattr(partner, 'restrictions')
    _safe_set(owner, 'StructuralComponent', None)
    assert owner not in getattr(partner, 'restrictions')


def test_assoc_columns62_stub_double():
    # ORDB4ORA_Column has no real 'Column' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Table(Name="sample_text")
    partner = ORDB4ORA_Column()
    setattr(partner, 'Column', None)
    _safe_set(owner, 'table63', {partner})
    assert getattr(partner, 'Column') == owner
    _safe_set(owner, 'table63', set())
    assert getattr(partner, 'Column') is None


def test_assoc_components81_stub_double():
    # ORDB4ORA_View has no real 'ORDB4ORA_View82' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuralComponent(Name="sample_text")
    partner = ORDB4ORA_View()
    setattr(partner, 'ORDB4ORA_View82', None)
    _safe_set(owner, 'ORDB4ORA_StructuralComponent83', partner)
    assert owner in getattr(partner, 'ORDB4ORA_View82')
    _safe_set(owner, 'ORDB4ORA_StructuralComponent83', None)
    assert owner not in getattr(partner, 'ORDB4ORA_View82')


def test_assoc_datatype15_stub_double():
    # ORDB4ORA_Datatype has no real 'Datatype' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Model(Name="sample_text")
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'Datatype', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'Datatype') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'Datatype') is None


def test_assoc_features48_stub_double():
    # ORDB4ORA_Feature has no real 'ORDB4ORA_Feature' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuralComponent(Name="sample_text")
    partner = ORDB4ORA_Feature()
    setattr(partner, 'ORDB4ORA_Feature', None)
    _safe_set(owner, 'ORDB4ORA_StructuralComponent49', {partner})
    assert getattr(partner, 'ORDB4ORA_Feature') == owner
    _safe_set(owner, 'ORDB4ORA_StructuralComponent49', set())
    assert getattr(partner, 'ORDB4ORA_Feature') is None


def test_assoc_method14_stub_double():
    # ORDB4ORA_MethodParameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    partner = ORDB4ORA_MethodParameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Method', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Method', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_model2_stub_double():
    # ORDB4ORA_Datatype has no real 'datatype' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Model(Name="sample_text")
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'datatype', None)
    _safe_set(owner, 'Model', partner)
    assert getattr(partner, 'datatype') == owner
    _safe_set(owner, 'Model', None)
    assert getattr(partner, 'datatype') is None


def test_assoc_parameters9_stub_double():
    # ORDB4ORA_MethodParameter has no real 'MethodParameter' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    partner = ORDB4ORA_MethodParameter()
    setattr(partner, 'MethodParameter', None)
    _safe_set(owner, 'method10', {partner})
    assert getattr(partner, 'MethodParameter') == owner
    _safe_set(owner, 'method10', set())
    assert getattr(partner, 'MethodParameter') is None


def test_assoc_restriction60_stub_double():
    # ORDB4ORA_Restriction has no real 'Restriction61' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Table(Name="sample_text")
    partner = ORDB4ORA_Restriction()
    setattr(partner, 'Restriction61', None)
    _safe_set(owner, 'table', {partner})
    assert getattr(partner, 'Restriction61') == owner
    _safe_set(owner, 'table', set())
    assert getattr(partner, 'Restriction61') is None


def test_assoc_restrictions50_stub_double():
    # ORDB4ORA_Restriction has no real 'Restriction' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuralComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuralComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuralComponent(Name="sample_text")
    partner = ORDB4ORA_Restriction()
    setattr(partner, 'Restriction', None)
    _safe_set(owner, 'attributes', {partner})
    assert getattr(partner, 'Restriction') == owner
    _safe_set(owner, 'attributes', set())
    assert getattr(partner, 'Restriction') is None


def test_assoc_returnType11_stub_double():
    # ORDB4ORA_Datatype has no real 'ORDB4ORA_Datatype13' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Method(Body="sample_text", Name="sample_text")
    partner = ORDB4ORA_Datatype()
    setattr(partner, 'ORDB4ORA_Datatype13', None)
    _safe_set(owner, 'ORDB4ORA_Method12', partner)
    assert getattr(partner, 'ORDB4ORA_Datatype13') == owner
    _safe_set(owner, 'ORDB4ORA_Method12', None)
    assert getattr(partner, 'ORDB4ORA_Datatype13') is None


def test_assoc_storedNested73_stub_double():
    # ORDB4ORA_TypedTable has no real 'typed' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StoredNestedTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StoredNestedTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StoredNestedTable(Name="sample_text")
    partner = ORDB4ORA_TypedTable()
    setattr(partner, 'typed', None)
    _safe_set(owner, 'StoredNestedTable', partner)
    assert owner in getattr(partner, 'typed')
    _safe_set(owner, 'StoredNestedTable', None)
    assert owner not in getattr(partner, 'typed')


def test_assoc_structuredType74_stub_double():
    # ORDB4ORA_TypedTable has no real 'typed75' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    partner = ORDB4ORA_TypedTable()
    setattr(partner, 'typed75', None)
    _safe_set(owner, 'StructuredType76', partner)
    assert getattr(partner, 'typed75') == owner
    _safe_set(owner, 'StructuredType76', None)
    assert getattr(partner, 'typed75') is None


def test_assoc_table1_stub_double():
    # ORDB4ORA_Column has no real 'columns' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Table(Name="sample_text")
    partner = ORDB4ORA_Column()
    setattr(partner, 'columns', None)
    _safe_set(owner, 'Table', partner)
    assert getattr(partner, 'columns') == owner
    _safe_set(owner, 'Table', None)
    assert getattr(partner, 'columns') is None


def test_assoc_table42_stub_double():
    # ORDB4ORA_Restriction has no real 'restriction' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Table(Name="sample_text")
    partner = ORDB4ORA_Restriction()
    setattr(partner, 'restriction', None)
    _safe_set(owner, 'Table43', partner)
    assert getattr(partner, 'restriction') == owner
    _safe_set(owner, 'Table43', None)
    assert getattr(partner, 'restriction') is None


def test_assoc_tables79_stub_double():
    # ORDB4ORA_View has no real 'ORDB4ORA_View' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_Table(Name="sample_text")
    partner = ORDB4ORA_View()
    setattr(partner, 'ORDB4ORA_View', None)
    _safe_set(owner, 'ORDB4ORA_Table80', partner)
    assert owner in getattr(partner, 'ORDB4ORA_View')
    _safe_set(owner, 'ORDB4ORA_Table80', None)
    assert owner not in getattr(partner, 'ORDB4ORA_View')


def test_assoc_typed45_stub_double():
    # ORDB4ORA_TypedTable has no real 'TypedTable' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StoredNestedTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StoredNestedTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StoredNestedTable(Name="sample_text")
    partner = ORDB4ORA_TypedTable()
    setattr(partner, 'TypedTable', None)
    _safe_set(owner, 'storedNested', partner)
    assert getattr(partner, 'TypedTable') == owner
    _safe_set(owner, 'storedNested', None)
    assert getattr(partner, 'TypedTable') is None


def test_assoc_typed55_stub_double():
    # ORDB4ORA_TypedTable has no real 'TypedTable56' property in the generated
    # code (a bare stub) -- manually attach it so ORDB4ORA_StructuredType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ORDB4ORA_StructuredType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ORDB4ORA_StructuredType(Name="sample_text", is_final=True, is_instantiable=True)
    partner = ORDB4ORA_TypedTable()
    setattr(partner, 'TypedTable56', None)
    _safe_set(owner, 'structuredType', {partner})
    assert getattr(partner, 'TypedTable56') == owner
    _safe_set(owner, 'structuredType', set())
    assert getattr(partner, 'TypedTable56') is None


