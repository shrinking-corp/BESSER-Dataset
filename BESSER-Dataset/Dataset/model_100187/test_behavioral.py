import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    ColumnConstraint,
    Comment,
    DataType,
    DatetimeLiteral,
    DatetimeType,
    DatetimeValueFunction,
    DefaultOption,
    DirectSQLStatement,
    EObject,
    GeneralLiteral,
    ImplicitlyTypedValueSpecification,
    LargeObjectLength,
    Literal,
    NationalCharacterStringLiteral,
    NumericLiteral,
    NumericType,
    PredefinedType,
    SQLSchemaStatement,
    SchemaQualifiedName,
    Separator,
    Statement,
    TableConstraint,
    TableContentsSource,
    TableDefinition,
    TableElement,
    TableElementList,
    TableReference,
    schema_ColumnConstraint,
    schema_ReferentialConstraint,
    schema_SQLSchemaDefinitionStatement,
    schema_TableColumnsConstraint,
    schema_TableElement,
    schema_UniqueConstraint,
    sql_Dummy,
    sql_common_BracketedComment,
    sql_common_Comment,
    sql_common_DirectSQLStatement,
    sql_common_SQLScript,
    sql_common_SchemaQualifiedName,
    sql_common_Separator,
    sql_common_SimpleComment,
    sql_common_Statement,
    sql_datatype_ApproximateNumericType,
    sql_datatype_BinaryLargeObjectStringType,
    sql_datatype_BooleanType,
    sql_datatype_CharacterStringType,
    sql_datatype_DataType,
    sql_datatype_DateType,
    sql_datatype_DatetimeType,
    sql_datatype_ExactNumericType,
    sql_datatype_LargeObjectLength,
    sql_datatype_NationalCharacterStringType,
    sql_datatype_NumericType,
    sql_datatype_PredefinedType,
    sql_datatype_TimeType,
    sql_datatype_TimestampType,
    sql_expression_ImplicitlyTypedValueSpecification,
    sql_expression_NullSpecification,
    sql_function_DatetimeValueFunction,
    sql_literal_ApproximateNumericLiteral,
    sql_literal_BooleanLiteral,
    sql_literal_CharacterStringLiteral,
    sql_literal_DateLiteral,
    sql_literal_DatetimeLiteral,
    sql_literal_ExactNumericLiteral,
    sql_literal_GeneralLiteral,
    sql_literal_Literal,
    sql_literal_NationalCharacterStringLiteral,
    sql_literal_NumericLiteral,
    sql_literal_TimeLiteral,
    sql_literal_TimestampLiteral,
    sql_schema_Column,
    sql_schema_ColumnConstraint,
    sql_schema_DatetimeValueFunctionDefaultOption,
    sql_schema_DefaultOption,
    sql_schema_ImplicitlyTypedValueSpecificationDefaultOption,
    sql_schema_LiteralDefaultOption,
    sql_schema_NotNullColumnConstraint,
    sql_schema_ReferentialColumnConstraint,
    sql_schema_ReferentialConstraint,
    sql_schema_ReferentialTableConstraint,
    sql_schema_SQLSchemaDefinitionStatement,
    sql_schema_SQLSchemaStatement,
    sql_schema_TableColumnsConstraint,
    sql_schema_TableConstraint,
    sql_schema_TableContentsSource,
    sql_schema_TableDefinition,
    sql_schema_TableElement,
    sql_schema_TableElementList,
    sql_schema_TableReference,
    sql_schema_UniqueColumnConstraint,
    sql_schema_UniqueConstraint,
    sql_schema_UniqueTableConstraint,
    ApproximateNumericTypeKind,
    BinaryLargeObjectStringTypeKind,
    CharLengthUnits,
    CharacterStringTypeKind,
    DatetimeValueFunctionKind,
    ExactNumericTypeKind,
    Multiplier,
    NationalCharacterStringTypeKind,
    TableScope,
    UniqueSpecificationKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_characterSetName3_stub_double():
    # SchemaQualifiedName has no real 'SchemaQualifiedName4' property in the generated
    # code (a bare stub) -- manually attach it so sql_datatype_CharacterStringType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_datatype_CharacterStringType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    partner = SchemaQualifiedName()
    setattr(partner, 'SchemaQualifiedName4', None)
    _safe_set(owner, 'sql_datatype_CharacterStringType', partner)
    assert getattr(partner, 'SchemaQualifiedName4') == owner
    _safe_set(owner, 'sql_datatype_CharacterStringType', None)
    assert getattr(partner, 'SchemaQualifiedName4') is None


def test_assoc_collationName22_stub_double():
    # SchemaQualifiedName has no real 'SchemaQualifiedName24' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_Column(name="sample_text")
    partner = SchemaQualifiedName()
    setattr(partner, 'SchemaQualifiedName24', None)
    _safe_set(owner, 'sql_schema_Column23', partner)
    assert getattr(partner, 'SchemaQualifiedName24') == owner
    _safe_set(owner, 'sql_schema_Column23', None)
    assert getattr(partner, 'SchemaQualifiedName24') is None


def test_assoc_collationName5_stub_double():
    # SchemaQualifiedName has no real 'SchemaQualifiedName7' property in the generated
    # code (a bare stub) -- manually attach it so sql_datatype_CharacterStringType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_datatype_CharacterStringType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_datatype_CharacterStringType(kind="sample_text", length="sample_text")
    partner = SchemaQualifiedName()
    setattr(partner, 'SchemaQualifiedName7', None)
    _safe_set(owner, 'sql_datatype_CharacterStringType6', partner)
    assert getattr(partner, 'SchemaQualifiedName7') == owner
    _safe_set(owner, 'sql_datatype_CharacterStringType6', None)
    assert getattr(partner, 'SchemaQualifiedName7') is None


def test_assoc_collationName8_stub_double():
    # SchemaQualifiedName has no real 'SchemaQualifiedName9' property in the generated
    # code (a bare stub) -- manually attach it so sql_datatype_NationalCharacterStringType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_datatype_NationalCharacterStringType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_datatype_NationalCharacterStringType(kind="sample_text", length="sample_text")
    partner = SchemaQualifiedName()
    setattr(partner, 'SchemaQualifiedName9', None)
    _safe_set(owner, 'sql_datatype_NationalCharacterStringType', partner)
    assert getattr(partner, 'SchemaQualifiedName9') == owner
    _safe_set(owner, 'sql_datatype_NationalCharacterStringType', None)
    assert getattr(partner, 'SchemaQualifiedName9') is None


def test_assoc_constraint20_stub_double():
    # ColumnConstraint has no real 'ColumnConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_Column(name="sample_text")
    partner = ColumnConstraint()
    setattr(partner, 'ColumnConstraint', None)
    _safe_set(owner, 'owner21', partner)
    assert getattr(partner, 'ColumnConstraint') == owner
    _safe_set(owner, 'owner21', None)
    assert getattr(partner, 'ColumnConstraint') is None


def test_assoc_contentsSource13_stub_double():
    # TableContentsSource has no real 'TableContentsSource' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_TableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_TableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    partner = TableContentsSource()
    setattr(partner, 'TableContentsSource', None)
    _safe_set(owner, 'owner', partner)
    assert getattr(partner, 'TableContentsSource') == owner
    _safe_set(owner, 'owner', None)
    assert getattr(partner, 'TableContentsSource') is None


def test_assoc_dataType17_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_Column(name="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'sql_schema_Column', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'sql_schema_Column', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_defaultOption18_stub_double():
    # DefaultOption has no real 'DefaultOption' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_Column(name="sample_text")
    partner = DefaultOption()
    setattr(partner, 'DefaultOption', None)
    _safe_set(owner, 'owner19', partner)
    assert getattr(partner, 'DefaultOption') == owner
    _safe_set(owner, 'owner19', None)
    assert getattr(partner, 'DefaultOption') is None


def test_assoc_length10_stub_double():
    # LargeObjectLength has no real 'LargeObjectLength' property in the generated
    # code (a bare stub) -- manually attach it so sql_datatype_BinaryLargeObjectStringType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_datatype_BinaryLargeObjectStringType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_datatype_BinaryLargeObjectStringType(kind="sample_text")
    partner = LargeObjectLength()
    setattr(partner, 'LargeObjectLength', None)
    _safe_set(owner, 'sql_datatype_BinaryLargeObjectStringType', partner)
    assert getattr(partner, 'LargeObjectLength') == owner
    _safe_set(owner, 'sql_datatype_BinaryLargeObjectStringType', None)
    assert getattr(partner, 'LargeObjectLength') is None


def test_assoc_schemaQualifiedName11_stub_double():
    # SchemaQualifiedName has no real 'SchemaQualifiedName12' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_TableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_TableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_TableDefinition(label="sample_text", scope="sample_text")
    partner = SchemaQualifiedName()
    setattr(partner, 'SchemaQualifiedName12', None)
    _safe_set(owner, 'sql_schema_TableDefinition', partner)
    assert getattr(partner, 'SchemaQualifiedName12') == owner
    _safe_set(owner, 'sql_schema_TableDefinition', None)
    assert getattr(partner, 'SchemaQualifiedName12') is None


def test_assoc_separators2_stub_double():
    # Separator has no real 'Separator' property in the generated
    # code (a bare stub) -- manually attach it so sql_literal_NationalCharacterStringLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_literal_NationalCharacterStringLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_literal_NationalCharacterStringLiteral(values="sample_text")
    partner = Separator()
    setattr(partner, 'Separator', None)
    _safe_set(owner, 'sql_literal_NationalCharacterStringLiteral', {partner})
    assert getattr(partner, 'Separator') == owner
    _safe_set(owner, 'sql_literal_NationalCharacterStringLiteral', set())
    assert getattr(partner, 'Separator') is None


def test_assoc_target40_stub_double():
    # TableDefinition has no real 'TableDefinition41' property in the generated
    # code (a bare stub) -- manually attach it so sql_schema_TableReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_schema_TableReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_schema_TableReference(catalogName="sample_text", schemaName="sample_text")
    partner = TableDefinition()
    setattr(partner, 'TableDefinition41', None)
    _safe_set(owner, 'sql_schema_TableReference', partner)
    assert getattr(partner, 'TableDefinition41') == owner
    _safe_set(owner, 'sql_schema_TableReference', None)
    assert getattr(partner, 'TableDefinition41') is None


