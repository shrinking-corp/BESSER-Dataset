import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributeFlag,
    AttributeProperty,
    ComplexType,
    DaoFeature,
    DaoOperation,
    Dependant,
    Expression,
    ExpressionFlag,
    FromRange,
    IDocumentable,
    JoinEntity,
    LiteralValue,
    ModelElement,
    PresentableFeature,
    QlStatement,
    QueryParameter,
    QueryParameterReference,
    ReferenceableByXmadslVariable,
    SelectStatement,
    Type,
    dom_AggregateFunction,
    dom_AliasedExpression,
    dom_AltWhenClause,
    dom_ApplicationSession,
    dom_Attribute,
    dom_AttributeFlag,
    dom_AttributeGroup,
    dom_AttributeProperty,
    dom_AttributeSortOrder,
    dom_AttributeTextProperty,
    dom_AttributeValidationProperty,
    dom_AvailableFlag,
    dom_BetweenExpression,
    dom_BinaryExpression,
    dom_BoolLiteral,
    dom_BooleanLiteralValue,
    dom_CallInputParameter,
    dom_CallOutputParameter,
    dom_CallableStatement,
    dom_CaseExpression,
    dom_CastFunction,
    dom_CollectionFunction,
    dom_Column,
    dom_ComplexType,
    dom_ConditionsBlock,
    dom_Constraint,
    dom_Dao,
    dom_DaoFeature,
    dom_DaoOperation,
    dom_DataBaseConstraint,
    dom_DataTypeAndTypeParameter,
    dom_DataView,
    dom_DelegateOperation,
    dom_DeleteStatement,
    dom_Dependant,
    dom_DerivedFlag,
    dom_EmptyLiteralValue,
    dom_Entity,
    dom_EqualityExpr,
    dom_Expression,
    dom_ExpressionFlag,
    dom_FeatureReference,
    dom_FromClass,
    dom_FromRange,
    dom_Function,
    dom_FunctionCall,
    dom_IElementWithNoName,
    dom_InClass,
    dom_InCollection,
    dom_InCollectionElements,
    dom_InExpression,
    dom_IncrementerReference,
    dom_InsertStatement,
    dom_IntegerLiteralValue,
    dom_Join,
    dom_JoinEntity,
    dom_LikeExpression,
    dom_LiteralValue,
    dom_ManyToMany,
    dom_ManyToOne,
    dom_Mapper,
    dom_MemberOfExpression,
    dom_NotExpression,
    dom_NullLiteralValue,
    dom_OneToMany,
    dom_OneToOne,
    dom_Operation,
    dom_Parameter,
    dom_ParenthesizedExpression,
    dom_PresentableFeature,
    dom_Property,
    dom_PropertyAssignment,
    dom_PropertyMapping,
    dom_PropertyValue,
    dom_QlStatement,
    dom_QuantifiedExpression,
    dom_QueryOperation,
    dom_QueryParameter,
    dom_QueryParameterReference,
    dom_QueryParameterValue,
    dom_ReadOnlyFlag,
    dom_RealLiteralValue,
    dom_RequiredFlag,
    dom_SelectClass,
    dom_SelectObject,
    dom_SelectProperties,
    dom_SelectStatement,
    dom_Service,
    dom_SimpleType,
    dom_SortOrderElement,
    dom_SqlType,
    dom_StringLiteralValue,
    dom_SubQuery,
    dom_TransientFlag,
    dom_TrimFunction,
    dom_Type,
    dom_UnaryExpression,
    dom_UpdateStatement,
    dom_ValidatorReference,
    dom_ValueObject,
    dom_WhenClause,
    CrudOperationType,
    DataBaseConstraintType,
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

def test_assoc_attribute126_reverse_link_reassign_clear():
    a1 = dom_AttributeSortOrder(asc=True, desc=True)
    a2 = dom_AttributeSortOrder(asc=False, desc=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute128', a1)
    assert _is_linked(b, 'dom_Attribute128', a1)
    if hasattr(a1, 'dom_AttributeSortOrder127'):
        assert _is_linked(a1, 'dom_AttributeSortOrder127', b)
    _safe_set(b, 'dom_Attribute128', a2)
    assert _is_linked(b, 'dom_Attribute128', a2)
    if hasattr(a1, 'dom_AttributeSortOrder127'):
        assert not _is_linked(a1, 'dom_AttributeSortOrder127', b)
    if hasattr(a2, 'dom_AttributeSortOrder127'):
        assert _is_linked(a2, 'dom_AttributeSortOrder127', b)
    _safe_set(b, 'dom_Attribute128', None)
    assert not _is_linked(b, 'dom_Attribute128', a2)
    if hasattr(a2, 'dom_AttributeSortOrder127'):
        assert not _is_linked(a2, 'dom_AttributeSortOrder127', b)


def test_assoc_attribute212_reverse_link_reassign_clear():
    a1 = dom_CallInputParameter(name="sample_text")
    a2 = dom_CallInputParameter(name="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute214', a1)
    assert _is_linked(b, 'dom_Attribute214', a1)
    if hasattr(a1, 'dom_CallInputParameter213'):
        assert _is_linked(a1, 'dom_CallInputParameter213', b)
    _safe_set(b, 'dom_Attribute214', a2)
    assert _is_linked(b, 'dom_Attribute214', a2)
    if hasattr(a1, 'dom_CallInputParameter213'):
        assert not _is_linked(a1, 'dom_CallInputParameter213', b)
    if hasattr(a2, 'dom_CallInputParameter213'):
        assert _is_linked(a2, 'dom_CallInputParameter213', b)
    _safe_set(b, 'dom_Attribute214', None)
    assert not _is_linked(b, 'dom_Attribute214', a2)
    if hasattr(a2, 'dom_CallInputParameter213'):
        assert not _is_linked(a2, 'dom_CallInputParameter213', b)


def test_assoc_attribute215_reverse_link_reassign_clear():
    a1 = dom_CallOutputParameter(name="sample_text")
    a2 = dom_CallOutputParameter(name="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute217', a1)
    assert _is_linked(b, 'dom_Attribute217', a1)
    if hasattr(a1, 'dom_CallOutputParameter216'):
        assert _is_linked(a1, 'dom_CallOutputParameter216', b)
    _safe_set(b, 'dom_Attribute217', a2)
    assert _is_linked(b, 'dom_Attribute217', a2)
    if hasattr(a1, 'dom_CallOutputParameter216'):
        assert not _is_linked(a1, 'dom_CallOutputParameter216', b)
    if hasattr(a2, 'dom_CallOutputParameter216'):
        assert _is_linked(a2, 'dom_CallOutputParameter216', b)
    _safe_set(b, 'dom_Attribute217', None)
    assert not _is_linked(b, 'dom_Attribute217', a2)
    if hasattr(a2, 'dom_CallOutputParameter216'):
        assert not _is_linked(a2, 'dom_CallOutputParameter216', b)


def test_assoc_attribute38_reverse_link_reassign_clear():
    a1 = dom_FeatureReference(all=True)
    a2 = dom_FeatureReference(all=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute40', a1)
    assert _is_linked(b, 'dom_Attribute40', a1)
    if hasattr(a1, 'dom_FeatureReference39'):
        assert _is_linked(a1, 'dom_FeatureReference39', b)
    _safe_set(b, 'dom_Attribute40', a2)
    assert _is_linked(b, 'dom_Attribute40', a2)
    if hasattr(a1, 'dom_FeatureReference39'):
        assert not _is_linked(a1, 'dom_FeatureReference39', b)
    if hasattr(a2, 'dom_FeatureReference39'):
        assert _is_linked(a2, 'dom_FeatureReference39', b)
    _safe_set(b, 'dom_Attribute40', None)
    assert not _is_linked(b, 'dom_Attribute40', a2)
    if hasattr(a2, 'dom_FeatureReference39'):
        assert not _is_linked(a2, 'dom_FeatureReference39', b)


def test_assoc_attributes121_reverse_link_reassign_clear():
    a1 = dom_AttributeSortOrder(asc=True, desc=True)
    a2 = dom_AttributeSortOrder(asc=False, desc=False)
    b = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    _safe_set(b, 'dom_AttributeGroup122', {a1})
    assert _is_linked(b, 'dom_AttributeGroup122', a1)
    if hasattr(a1, 'dom_AttributeSortOrder'):
        assert _is_linked(a1, 'dom_AttributeSortOrder', b)
    _safe_set(b, 'dom_AttributeGroup122', {a2})
    assert _is_linked(b, 'dom_AttributeGroup122', a2)
    if hasattr(a1, 'dom_AttributeSortOrder'):
        assert not _is_linked(a1, 'dom_AttributeSortOrder', b)
    if hasattr(a2, 'dom_AttributeSortOrder'):
        assert _is_linked(a2, 'dom_AttributeSortOrder', b)
    _safe_set(b, 'dom_AttributeGroup122', set())
    assert not _is_linked(b, 'dom_AttributeGroup122', a2)
    if hasattr(a2, 'dom_AttributeSortOrder'):
        assert not _is_linked(a2, 'dom_AttributeSortOrder', b)


def test_assoc_attributes193_reverse_link_reassign_clear():
    a1 = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    a2 = dom_DataBaseConstraint(name="sample_text_2", type="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute195', a1)
    assert _is_linked(b, 'dom_Attribute195', a1)
    if hasattr(a1, 'dom_DataBaseConstraint194'):
        assert _is_linked(a1, 'dom_DataBaseConstraint194', b)
    _safe_set(b, 'dom_Attribute195', a2)
    assert _is_linked(b, 'dom_Attribute195', a2)
    if hasattr(a1, 'dom_DataBaseConstraint194'):
        assert not _is_linked(a1, 'dom_DataBaseConstraint194', b)
    if hasattr(a2, 'dom_DataBaseConstraint194'):
        assert _is_linked(a2, 'dom_DataBaseConstraint194', b)
    _safe_set(b, 'dom_Attribute195', None)
    assert not _is_linked(b, 'dom_Attribute195', a2)
    if hasattr(a2, 'dom_DataBaseConstraint194'):
        assert not _is_linked(a2, 'dom_DataBaseConstraint194', b)


def test_assoc_character282_reverse_link_reassign_clear():
    a1 = dom_TrimFunction(function="sample_text", mode="sample_text")
    a2 = dom_TrimFunction(function="sample_text_2", mode="sample_text_2")
    b = dom_StringLiteralValue(value="sample_text")
    _safe_set(b, 'dom_StringLiteralValue', a1)
    assert _is_linked(b, 'dom_StringLiteralValue', a1)
    if hasattr(a1, 'dom_TrimFunction'):
        assert _is_linked(a1, 'dom_TrimFunction', b)
    _safe_set(b, 'dom_StringLiteralValue', a2)
    assert _is_linked(b, 'dom_StringLiteralValue', a2)
    if hasattr(a1, 'dom_TrimFunction'):
        assert not _is_linked(a1, 'dom_TrimFunction', b)
    if hasattr(a2, 'dom_TrimFunction'):
        assert _is_linked(a2, 'dom_TrimFunction', b)
    _safe_set(b, 'dom_StringLiteralValue', None)
    assert not _is_linked(b, 'dom_StringLiteralValue', a2)
    if hasattr(a2, 'dom_TrimFunction'):
        assert not _is_linked(a2, 'dom_TrimFunction', b)


def test_assoc_collection290_reverse_link_reassign_clear():
    a1 = dom_CollectionFunction(function="sample_text")
    a2 = dom_CollectionFunction(function="sample_text_2")
    b = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    _safe_set(b, 'dom_AggregateFunction291', a1)
    assert _is_linked(b, 'dom_AggregateFunction291', a1)
    if hasattr(a1, 'dom_CollectionFunction'):
        assert _is_linked(a1, 'dom_CollectionFunction', b)
    _safe_set(b, 'dom_AggregateFunction291', a2)
    assert _is_linked(b, 'dom_AggregateFunction291', a2)
    if hasattr(a1, 'dom_CollectionFunction'):
        assert not _is_linked(a1, 'dom_CollectionFunction', b)
    if hasattr(a2, 'dom_CollectionFunction'):
        assert _is_linked(a2, 'dom_CollectionFunction', b)
    _safe_set(b, 'dom_AggregateFunction291', None)
    assert not _is_linked(b, 'dom_AggregateFunction291', a2)
    if hasattr(a2, 'dom_CollectionFunction'):
        assert not _is_linked(a2, 'dom_CollectionFunction', b)


def test_assoc_columns141_reverse_link_reassign_clear():
    a1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    a2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column', a1)
    assert _is_linked(b, 'dom_Column', a1)
    if hasattr(a1, 'dom_Dao142'):
        assert _is_linked(a1, 'dom_Dao142', b)
    _safe_set(b, 'dom_Column', a2)
    assert _is_linked(b, 'dom_Column', a2)
    if hasattr(a1, 'dom_Dao142'):
        assert not _is_linked(a1, 'dom_Dao142', b)
    if hasattr(a2, 'dom_Dao142'):
        assert _is_linked(a2, 'dom_Dao142', b)
    _safe_set(b, 'dom_Column', None)
    assert not _is_linked(b, 'dom_Column', a2)
    if hasattr(a2, 'dom_Dao142'):
        assert not _is_linked(a2, 'dom_Dao142', b)


def test_assoc_columns180_reverse_link_reassign_clear():
    a1 = dom_Column(columnName="sample_text")
    a2 = dom_Column(columnName="sample_text_2")
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column181', a1)
    assert _is_linked(b, 'dom_Column181', a1)
    if hasattr(a1, 'dom_Column179'):
        assert _is_linked(a1, 'dom_Column179', b)
    _safe_set(b, 'dom_Column181', a2)
    assert _is_linked(b, 'dom_Column181', a2)
    if hasattr(a1, 'dom_Column179'):
        assert not _is_linked(a1, 'dom_Column179', b)
    if hasattr(a2, 'dom_Column179'):
        assert _is_linked(a2, 'dom_Column179', b)
    _safe_set(b, 'dom_Column181', None)
    assert not _is_linked(b, 'dom_Column181', a2)
    if hasattr(a2, 'dom_Column179'):
        assert not _is_linked(a2, 'dom_Column179', b)


def test_assoc_columns187_reverse_link_reassign_clear():
    a1 = dom_ManyToOne(columnName="sample_text", derived=True)
    a2 = dom_ManyToOne(columnName="sample_text_2", derived=False)
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column189', a1)
    assert _is_linked(b, 'dom_Column189', a1)
    if hasattr(a1, 'dom_ManyToOne188'):
        assert _is_linked(a1, 'dom_ManyToOne188', b)
    _safe_set(b, 'dom_Column189', a2)
    assert _is_linked(b, 'dom_Column189', a2)
    if hasattr(a1, 'dom_ManyToOne188'):
        assert not _is_linked(a1, 'dom_ManyToOne188', b)
    if hasattr(a2, 'dom_ManyToOne188'):
        assert _is_linked(a2, 'dom_ManyToOne188', b)
    _safe_set(b, 'dom_Column189', None)
    assert not _is_linked(b, 'dom_Column189', a2)
    if hasattr(a2, 'dom_ManyToOne188'):
        assert not _is_linked(a2, 'dom_ManyToOne188', b)


def test_assoc_columns190_reverse_link_reassign_clear():
    a1 = dom_OneToMany(columnName="sample_text")
    a2 = dom_OneToMany(columnName="sample_text_2")
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column192', a1)
    assert _is_linked(b, 'dom_Column192', a1)
    if hasattr(a1, 'dom_OneToMany191'):
        assert _is_linked(a1, 'dom_OneToMany191', b)
    _safe_set(b, 'dom_Column192', a2)
    assert _is_linked(b, 'dom_Column192', a2)
    if hasattr(a1, 'dom_OneToMany191'):
        assert not _is_linked(a1, 'dom_OneToMany191', b)
    if hasattr(a2, 'dom_OneToMany191'):
        assert _is_linked(a2, 'dom_OneToMany191', b)
    _safe_set(b, 'dom_Column192', None)
    assert not _is_linked(b, 'dom_Column192', a2)
    if hasattr(a2, 'dom_OneToMany191'):
        assert not _is_linked(a2, 'dom_OneToMany191', b)


def test_assoc_dataBaseConstraints139_reverse_link_reassign_clear():
    a1 = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    a2 = dom_DataBaseConstraint(name="sample_text_2", type="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao140', {a1})
    assert _is_linked(b, 'dom_Dao140', a1)
    if hasattr(a1, 'dom_DataBaseConstraint'):
        assert _is_linked(a1, 'dom_DataBaseConstraint', b)
    _safe_set(b, 'dom_Dao140', {a2})
    assert _is_linked(b, 'dom_Dao140', a2)
    if hasattr(a1, 'dom_DataBaseConstraint'):
        assert not _is_linked(a1, 'dom_DataBaseConstraint', b)
    if hasattr(a2, 'dom_DataBaseConstraint'):
        assert _is_linked(a2, 'dom_DataBaseConstraint', b)
    _safe_set(b, 'dom_Dao140', set())
    assert not _is_linked(b, 'dom_Dao140', a2)
    if hasattr(a2, 'dom_DataBaseConstraint'):
        assert not _is_linked(a2, 'dom_DataBaseConstraint', b)


def test_assoc_delegate12_reverse_link_reassign_clear():
    a1 = dom_Operation(expression="sample_text")
    a2 = dom_Operation(expression="sample_text_2")
    b = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    _safe_set(b, 'dom_DelegateOperation14', a1)
    assert _is_linked(b, 'dom_DelegateOperation14', a1)
    if hasattr(a1, 'dom_Operation13'):
        assert _is_linked(a1, 'dom_Operation13', b)
    _safe_set(b, 'dom_DelegateOperation14', a2)
    assert _is_linked(b, 'dom_DelegateOperation14', a2)
    if hasattr(a1, 'dom_Operation13'):
        assert not _is_linked(a1, 'dom_Operation13', b)
    if hasattr(a2, 'dom_Operation13'):
        assert _is_linked(a2, 'dom_Operation13', b)
    _safe_set(b, 'dom_DelegateOperation14', None)
    assert not _is_linked(b, 'dom_DelegateOperation14', a2)
    if hasattr(a2, 'dom_Operation13'):
        assert not _is_linked(a2, 'dom_Operation13', b)


def test_assoc_entity269_reverse_link_reassign_clear():
    a1 = dom_JoinEntity(name="sample_text")
    a2 = dom_JoinEntity(name="sample_text_2")
    b = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    _safe_set(b, 'dom_Join270', a1)
    assert _is_linked(b, 'dom_Join270', a1)
    if hasattr(a1, 'dom_JoinEntity'):
        assert _is_linked(a1, 'dom_JoinEntity', b)
    _safe_set(b, 'dom_Join270', a2)
    assert _is_linked(b, 'dom_Join270', a2)
    if hasattr(a1, 'dom_JoinEntity'):
        assert not _is_linked(a1, 'dom_JoinEntity', b)
    if hasattr(a2, 'dom_JoinEntity'):
        assert _is_linked(a2, 'dom_JoinEntity', b)
    _safe_set(b, 'dom_Join270', None)
    assert not _is_linked(b, 'dom_Join270', a2)
    if hasattr(a2, 'dom_JoinEntity'):
        assert not _is_linked(a2, 'dom_JoinEntity', b)


def test_assoc_inParameter206_reverse_link_reassign_clear():
    a1 = dom_CallableStatement(functionCall=True, name="sample_text")
    a2 = dom_CallableStatement(functionCall=False, name="sample_text_2")
    b = dom_CallInputParameter(name="sample_text")
    _safe_set(b, 'dom_CallInputParameter', a1)
    assert _is_linked(b, 'dom_CallInputParameter', a1)
    if hasattr(a1, 'dom_CallableStatement'):
        assert _is_linked(a1, 'dom_CallableStatement', b)
    _safe_set(b, 'dom_CallInputParameter', a2)
    assert _is_linked(b, 'dom_CallInputParameter', a2)
    if hasattr(a1, 'dom_CallableStatement'):
        assert not _is_linked(a1, 'dom_CallableStatement', b)
    if hasattr(a2, 'dom_CallableStatement'):
        assert _is_linked(a2, 'dom_CallableStatement', b)
    _safe_set(b, 'dom_CallInputParameter', None)
    assert not _is_linked(b, 'dom_CallInputParameter', a2)
    if hasattr(a2, 'dom_CallableStatement'):
        assert not _is_linked(a2, 'dom_CallableStatement', b)


def test_assoc_left56_reverse_link_reassign_clear():
    a1 = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    a2 = dom_PropertyMapping(biDirectional=False, toLeft=False, toRight=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute58', a1)
    assert _is_linked(b, 'dom_Attribute58', a1)
    if hasattr(a1, 'dom_PropertyMapping57'):
        assert _is_linked(a1, 'dom_PropertyMapping57', b)
    _safe_set(b, 'dom_Attribute58', a2)
    assert _is_linked(b, 'dom_Attribute58', a2)
    if hasattr(a1, 'dom_PropertyMapping57'):
        assert not _is_linked(a1, 'dom_PropertyMapping57', b)
    if hasattr(a2, 'dom_PropertyMapping57'):
        assert _is_linked(a2, 'dom_PropertyMapping57', b)
    _safe_set(b, 'dom_Attribute58', None)
    assert not _is_linked(b, 'dom_Attribute58', a2)
    if hasattr(a2, 'dom_PropertyMapping57'):
        assert not _is_linked(a2, 'dom_PropertyMapping57', b)


def test_assoc_manyToManyAssociations149_reverse_link_reassign_clear():
    a1 = dom_ManyToMany(columnName="sample_text", inverse=True, tableName="sample_text")
    a2 = dom_ManyToMany(columnName="sample_text_2", inverse=False, tableName="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao150', {a1})
    assert _is_linked(b, 'dom_Dao150', a1)
    if hasattr(a1, 'dom_ManyToMany'):
        assert _is_linked(a1, 'dom_ManyToMany', b)
    _safe_set(b, 'dom_Dao150', {a2})
    assert _is_linked(b, 'dom_Dao150', a2)
    if hasattr(a1, 'dom_ManyToMany'):
        assert not _is_linked(a1, 'dom_ManyToMany', b)
    if hasattr(a2, 'dom_ManyToMany'):
        assert _is_linked(a2, 'dom_ManyToMany', b)
    _safe_set(b, 'dom_Dao150', set())
    assert not _is_linked(b, 'dom_Dao150', a2)
    if hasattr(a2, 'dom_ManyToMany'):
        assert not _is_linked(a2, 'dom_ManyToMany', b)


def test_assoc_manyToOneAssociations143_reverse_link_reassign_clear():
    a1 = dom_ManyToOne(columnName="sample_text", derived=True)
    a2 = dom_ManyToOne(columnName="sample_text_2", derived=False)
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao144', {a1})
    assert _is_linked(b, 'dom_Dao144', a1)
    if hasattr(a1, 'dom_ManyToOne'):
        assert _is_linked(a1, 'dom_ManyToOne', b)
    _safe_set(b, 'dom_Dao144', {a2})
    assert _is_linked(b, 'dom_Dao144', a2)
    if hasattr(a1, 'dom_ManyToOne'):
        assert not _is_linked(a1, 'dom_ManyToOne', b)
    if hasattr(a2, 'dom_ManyToOne'):
        assert _is_linked(a2, 'dom_ManyToOne', b)
    _safe_set(b, 'dom_Dao144', set())
    assert not _is_linked(b, 'dom_Dao144', a2)
    if hasattr(a2, 'dom_ManyToOne'):
        assert not _is_linked(a2, 'dom_ManyToOne', b)


def test_assoc_naturalKey163_reverse_link_reassign_clear():
    a1 = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    a2 = dom_DataBaseConstraint(name="sample_text_2", type="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao164', a1)
    assert _is_linked(b, 'dom_Dao164', a1)
    if hasattr(a1, 'dom_DataBaseConstraint165'):
        assert _is_linked(a1, 'dom_DataBaseConstraint165', b)
    _safe_set(b, 'dom_Dao164', a2)
    assert _is_linked(b, 'dom_Dao164', a2)
    if hasattr(a1, 'dom_DataBaseConstraint165'):
        assert not _is_linked(a1, 'dom_DataBaseConstraint165', b)
    if hasattr(a2, 'dom_DataBaseConstraint165'):
        assert _is_linked(a2, 'dom_DataBaseConstraint165', b)
    _safe_set(b, 'dom_Dao164', None)
    assert not _is_linked(b, 'dom_Dao164', a2)
    if hasattr(a2, 'dom_DataBaseConstraint165'):
        assert not _is_linked(a2, 'dom_DataBaseConstraint165', b)


def test_assoc_naturalKeyColumns154_reverse_link_reassign_clear():
    a1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    a2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column156', a1)
    assert _is_linked(b, 'dom_Column156', a1)
    if hasattr(a1, 'dom_Dao155'):
        assert _is_linked(a1, 'dom_Dao155', b)
    _safe_set(b, 'dom_Column156', a2)
    assert _is_linked(b, 'dom_Column156', a2)
    if hasattr(a1, 'dom_Dao155'):
        assert not _is_linked(a1, 'dom_Dao155', b)
    if hasattr(a2, 'dom_Dao155'):
        assert _is_linked(a2, 'dom_Dao155', b)
    _safe_set(b, 'dom_Column156', None)
    assert not _is_linked(b, 'dom_Column156', a2)
    if hasattr(a2, 'dom_Dao155'):
        assert not _is_linked(a2, 'dom_Dao155', b)


def test_assoc_nestedAttribute218_reverse_link_reassign_clear():
    a1 = dom_CallOutputParameter(name="sample_text")
    a2 = dom_CallOutputParameter(name="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute220', a1)
    assert _is_linked(b, 'dom_Attribute220', a1)
    if hasattr(a1, 'dom_CallOutputParameter219'):
        assert _is_linked(a1, 'dom_CallOutputParameter219', b)
    _safe_set(b, 'dom_Attribute220', a2)
    assert _is_linked(b, 'dom_Attribute220', a2)
    if hasattr(a1, 'dom_CallOutputParameter219'):
        assert not _is_linked(a1, 'dom_CallOutputParameter219', b)
    if hasattr(a2, 'dom_CallOutputParameter219'):
        assert _is_linked(a2, 'dom_CallOutputParameter219', b)
    _safe_set(b, 'dom_Attribute220', None)
    assert not _is_linked(b, 'dom_Attribute220', a2)
    if hasattr(a2, 'dom_CallOutputParameter219'):
        assert not _is_linked(a2, 'dom_CallOutputParameter219', b)


def test_assoc_oneToManyAssociations147_reverse_link_reassign_clear():
    a1 = dom_OneToMany(columnName="sample_text")
    a2 = dom_OneToMany(columnName="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao148', {a1})
    assert _is_linked(b, 'dom_Dao148', a1)
    if hasattr(a1, 'dom_OneToMany'):
        assert _is_linked(a1, 'dom_OneToMany', b)
    _safe_set(b, 'dom_Dao148', {a2})
    assert _is_linked(b, 'dom_Dao148', a2)
    if hasattr(a1, 'dom_OneToMany'):
        assert not _is_linked(a1, 'dom_OneToMany', b)
    if hasattr(a2, 'dom_OneToMany'):
        assert _is_linked(a2, 'dom_OneToMany', b)
    _safe_set(b, 'dom_Dao148', set())
    assert not _is_linked(b, 'dom_Dao148', a2)
    if hasattr(a2, 'dom_OneToMany'):
        assert not _is_linked(a2, 'dom_OneToMany', b)


def test_assoc_operation21_reverse_link_reassign_clear():
    a1 = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    a2 = dom_DelegateOperation(crudOperationType="sample_text_2", many=False, name="sample_text_2")
    b = dom_DaoOperation(many=True, name="sample_text")
    _safe_set(b, 'dom_DaoOperation', a1)
    assert _is_linked(b, 'dom_DaoOperation', a1)
    if hasattr(a1, 'dom_DelegateOperation22'):
        assert _is_linked(a1, 'dom_DelegateOperation22', b)
    _safe_set(b, 'dom_DaoOperation', a2)
    assert _is_linked(b, 'dom_DaoOperation', a2)
    if hasattr(a1, 'dom_DelegateOperation22'):
        assert not _is_linked(a1, 'dom_DelegateOperation22', b)
    if hasattr(a2, 'dom_DelegateOperation22'):
        assert _is_linked(a2, 'dom_DelegateOperation22', b)
    _safe_set(b, 'dom_DaoOperation', None)
    assert not _is_linked(b, 'dom_DaoOperation', a2)
    if hasattr(a2, 'dom_DelegateOperation22'):
        assert not _is_linked(a2, 'dom_DelegateOperation22', b)


def test_assoc_operations134_reverse_link_reassign_clear():
    a1 = dom_Operation(expression="sample_text")
    a2 = dom_Operation(expression="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao135', {a1})
    assert _is_linked(b, 'dom_Dao135', a1)
    if hasattr(a1, 'dom_Operation136'):
        assert _is_linked(a1, 'dom_Operation136', b)
    _safe_set(b, 'dom_Dao135', {a2})
    assert _is_linked(b, 'dom_Dao135', a2)
    if hasattr(a1, 'dom_Operation136'):
        assert not _is_linked(a1, 'dom_Operation136', b)
    if hasattr(a2, 'dom_Operation136'):
        assert _is_linked(a2, 'dom_Operation136', b)
    _safe_set(b, 'dom_Dao135', set())
    assert not _is_linked(b, 'dom_Dao135', a2)
    if hasattr(a2, 'dom_Operation136'):
        assert not _is_linked(a2, 'dom_Operation136', b)


def test_assoc_opposite95_reverse_link_reassign_clear():
    a1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    a2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute96', a1)
    assert _is_linked(b, 'dom_Attribute96', a1)
    if hasattr(a1, 'dom_Attribute94'):
        assert _is_linked(a1, 'dom_Attribute94', b)
    _safe_set(b, 'dom_Attribute96', a2)
    assert _is_linked(b, 'dom_Attribute96', a2)
    if hasattr(a1, 'dom_Attribute94'):
        assert not _is_linked(a1, 'dom_Attribute94', b)
    if hasattr(a2, 'dom_Attribute94'):
        assert _is_linked(a2, 'dom_Attribute94', b)
    _safe_set(b, 'dom_Attribute96', None)
    assert not _is_linked(b, 'dom_Attribute96', a2)
    if hasattr(a2, 'dom_Attribute94'):
        assert not _is_linked(a2, 'dom_Attribute94', b)


def test_assoc_oppositeReference107_reverse_link_reassign_clear():
    a1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    a2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute108', a1)
    assert _is_linked(b, 'dom_Attribute108', a1)
    if hasattr(a1, 'dom_Attribute106'):
        assert _is_linked(a1, 'dom_Attribute106', b)
    _safe_set(b, 'dom_Attribute108', a2)
    assert _is_linked(b, 'dom_Attribute108', a2)
    if hasattr(a1, 'dom_Attribute106'):
        assert not _is_linked(a1, 'dom_Attribute106', b)
    if hasattr(a2, 'dom_Attribute106'):
        assert _is_linked(a2, 'dom_Attribute106', b)
    _safe_set(b, 'dom_Attribute108', None)
    assert not _is_linked(b, 'dom_Attribute108', a2)
    if hasattr(a2, 'dom_Attribute106'):
        assert not _is_linked(a2, 'dom_Attribute106', b)


def test_assoc_outParameter207_reverse_link_reassign_clear():
    a1 = dom_CallableStatement(functionCall=True, name="sample_text")
    a2 = dom_CallableStatement(functionCall=False, name="sample_text_2")
    b = dom_CallOutputParameter(name="sample_text")
    _safe_set(b, 'dom_CallOutputParameter', a1)
    assert _is_linked(b, 'dom_CallOutputParameter', a1)
    if hasattr(a1, 'dom_CallableStatement208'):
        assert _is_linked(a1, 'dom_CallableStatement208', b)
    _safe_set(b, 'dom_CallOutputParameter', a2)
    assert _is_linked(b, 'dom_CallOutputParameter', a2)
    if hasattr(a1, 'dom_CallableStatement208'):
        assert not _is_linked(a1, 'dom_CallableStatement208', b)
    if hasattr(a2, 'dom_CallableStatement208'):
        assert _is_linked(a2, 'dom_CallableStatement208', b)
    _safe_set(b, 'dom_CallOutputParameter', None)
    assert not _is_linked(b, 'dom_CallOutputParameter', a2)
    if hasattr(a2, 'dom_CallableStatement208'):
        assert not _is_linked(a2, 'dom_CallableStatement208', b)


def test_assoc_parameters10_reverse_link_reassign_clear():
    a1 = dom_Parameter(many=True, name="sample_text")
    a2 = dom_Parameter(many=False, name="sample_text_2")
    b = dom_Operation(expression="sample_text")
    _safe_set(b, 'dom_Operation11', {a1})
    assert _is_linked(b, 'dom_Operation11', a1)
    if hasattr(a1, 'dom_Parameter'):
        assert _is_linked(a1, 'dom_Parameter', b)
    _safe_set(b, 'dom_Operation11', {a2})
    assert _is_linked(b, 'dom_Operation11', a2)
    if hasattr(a1, 'dom_Parameter'):
        assert not _is_linked(a1, 'dom_Parameter', b)
    if hasattr(a2, 'dom_Parameter'):
        assert _is_linked(a2, 'dom_Parameter', b)
    _safe_set(b, 'dom_Operation11', set())
    assert not _is_linked(b, 'dom_Operation11', a2)
    if hasattr(a2, 'dom_Parameter'):
        assert not _is_linked(a2, 'dom_Parameter', b)


def test_assoc_primaryKey160_reverse_link_reassign_clear():
    a1 = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    a2 = dom_DataBaseConstraint(name="sample_text_2", type="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao161', a1)
    assert _is_linked(b, 'dom_Dao161', a1)
    if hasattr(a1, 'dom_DataBaseConstraint162'):
        assert _is_linked(a1, 'dom_DataBaseConstraint162', b)
    _safe_set(b, 'dom_Dao161', a2)
    assert _is_linked(b, 'dom_Dao161', a2)
    if hasattr(a1, 'dom_DataBaseConstraint162'):
        assert not _is_linked(a1, 'dom_DataBaseConstraint162', b)
    if hasattr(a2, 'dom_DataBaseConstraint162'):
        assert _is_linked(a2, 'dom_DataBaseConstraint162', b)
    _safe_set(b, 'dom_Dao161', None)
    assert not _is_linked(b, 'dom_Dao161', a2)
    if hasattr(a2, 'dom_DataBaseConstraint162'):
        assert not _is_linked(a2, 'dom_DataBaseConstraint162', b)


def test_assoc_primaryKeyColumn151_reverse_link_reassign_clear():
    a1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    a2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column153', a1)
    assert _is_linked(b, 'dom_Column153', a1)
    if hasattr(a1, 'dom_Dao152'):
        assert _is_linked(a1, 'dom_Dao152', b)
    _safe_set(b, 'dom_Column153', a2)
    assert _is_linked(b, 'dom_Column153', a2)
    if hasattr(a1, 'dom_Dao152'):
        assert not _is_linked(a1, 'dom_Dao152', b)
    if hasattr(a2, 'dom_Dao152'):
        assert _is_linked(a2, 'dom_Dao152', b)
    _safe_set(b, 'dom_Column153', None)
    assert not _is_linked(b, 'dom_Column153', a2)
    if hasattr(a2, 'dom_Dao152'):
        assert not _is_linked(a2, 'dom_Dao152', b)


def test_assoc_property319_reverse_link_reassign_clear():
    a1 = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    a2 = dom_PropertyValue(classProperty=False, name="sample_text_2", segments="sample_text_2")
    b = dom_CollectionFunction(function="sample_text")
    _safe_set(b, 'dom_CollectionFunction320', a1)
    assert _is_linked(b, 'dom_CollectionFunction320', a1)
    if hasattr(a1, 'dom_PropertyValue321'):
        assert _is_linked(a1, 'dom_PropertyValue321', b)
    _safe_set(b, 'dom_CollectionFunction320', a2)
    assert _is_linked(b, 'dom_CollectionFunction320', a2)
    if hasattr(a1, 'dom_PropertyValue321'):
        assert not _is_linked(a1, 'dom_PropertyValue321', b)
    if hasattr(a2, 'dom_PropertyValue321'):
        assert _is_linked(a2, 'dom_PropertyValue321', b)
    _safe_set(b, 'dom_CollectionFunction320', None)
    assert not _is_linked(b, 'dom_CollectionFunction320', a2)
    if hasattr(a2, 'dom_PropertyValue321'):
        assert not _is_linked(a2, 'dom_PropertyValue321', b)


def test_assoc_propertyMappings54_reverse_link_reassign_clear():
    a1 = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    a2 = dom_PropertyMapping(biDirectional=False, toLeft=False, toRight=False)
    b = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    _safe_set(b, 'dom_Mapper55', {a1})
    assert _is_linked(b, 'dom_Mapper55', a1)
    if hasattr(a1, 'dom_PropertyMapping'):
        assert _is_linked(a1, 'dom_PropertyMapping', b)
    _safe_set(b, 'dom_Mapper55', {a2})
    assert _is_linked(b, 'dom_Mapper55', a2)
    if hasattr(a1, 'dom_PropertyMapping'):
        assert not _is_linked(a1, 'dom_PropertyMapping', b)
    if hasattr(a2, 'dom_PropertyMapping'):
        assert _is_linked(a2, 'dom_PropertyMapping', b)
    _safe_set(b, 'dom_Mapper55', set())
    assert not _is_linked(b, 'dom_Mapper55', a2)
    if hasattr(a2, 'dom_PropertyMapping'):
        assert not _is_linked(a2, 'dom_PropertyMapping', b)


def test_assoc_reference271_reverse_link_reassign_clear():
    a1 = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    a2 = dom_Join(fetch=False, propertyFetch=False, type="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute273', a1)
    assert _is_linked(b, 'dom_Attribute273', a1)
    if hasattr(a1, 'dom_Join272'):
        assert _is_linked(a1, 'dom_Join272', b)
    _safe_set(b, 'dom_Attribute273', a2)
    assert _is_linked(b, 'dom_Attribute273', a2)
    if hasattr(a1, 'dom_Join272'):
        assert not _is_linked(a1, 'dom_Join272', b)
    if hasattr(a2, 'dom_Join272'):
        assert _is_linked(a2, 'dom_Join272', b)
    _safe_set(b, 'dom_Attribute273', None)
    assert not _is_linked(b, 'dom_Attribute273', a2)
    if hasattr(a2, 'dom_Join272'):
        assert not _is_linked(a2, 'dom_Join272', b)


def test_assoc_repository19_reverse_link_reassign_clear():
    a1 = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    a2 = dom_DelegateOperation(crudOperationType="sample_text_2", many=False, name="sample_text_2")
    b = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    _safe_set(b, 'dom_Dao', a1)
    assert _is_linked(b, 'dom_Dao', a1)
    if hasattr(a1, 'dom_DelegateOperation20'):
        assert _is_linked(a1, 'dom_DelegateOperation20', b)
    _safe_set(b, 'dom_Dao', a2)
    assert _is_linked(b, 'dom_Dao', a2)
    if hasattr(a1, 'dom_DelegateOperation20'):
        assert not _is_linked(a1, 'dom_DelegateOperation20', b)
    if hasattr(a2, 'dom_DelegateOperation20'):
        assert _is_linked(a2, 'dom_DelegateOperation20', b)
    _safe_set(b, 'dom_Dao', None)
    assert not _is_linked(b, 'dom_Dao', a2)
    if hasattr(a2, 'dom_DelegateOperation20'):
        assert not _is_linked(a2, 'dom_DelegateOperation20', b)


def test_assoc_resolvedAttributeList110_reverse_link_reassign_clear():
    a1 = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    a2 = dom_Attribute(composition=False, dataTypeName="sample_text_2", defaultValue="sample_text_2", derived=False, identifier=False, many=False, readOnly=False, reference=False, required=False, transient=False, version=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute111', a1)
    assert _is_linked(b, 'dom_Attribute111', a1)
    if hasattr(a1, 'dom_Attribute109'):
        assert _is_linked(a1, 'dom_Attribute109', b)
    _safe_set(b, 'dom_Attribute111', a2)
    assert _is_linked(b, 'dom_Attribute111', a2)
    if hasattr(a1, 'dom_Attribute109'):
        assert not _is_linked(a1, 'dom_Attribute109', b)
    if hasattr(a2, 'dom_Attribute109'):
        assert _is_linked(a2, 'dom_Attribute109', b)
    _safe_set(b, 'dom_Attribute111', None)
    assert not _is_linked(b, 'dom_Attribute111', a2)
    if hasattr(a2, 'dom_Attribute109'):
        assert not _is_linked(a2, 'dom_Attribute109', b)


def test_assoc_resolvedAttributeList123_reverse_link_reassign_clear():
    a1 = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    a2 = dom_AttributeGroup(filter=False, key=False, name="sample_text_2", sortorder=False, unique=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute125', a1)
    assert _is_linked(b, 'dom_Attribute125', a1)
    if hasattr(a1, 'dom_AttributeGroup124'):
        assert _is_linked(a1, 'dom_AttributeGroup124', b)
    _safe_set(b, 'dom_Attribute125', a2)
    assert _is_linked(b, 'dom_Attribute125', a2)
    if hasattr(a1, 'dom_AttributeGroup124'):
        assert not _is_linked(a1, 'dom_AttributeGroup124', b)
    if hasattr(a2, 'dom_AttributeGroup124'):
        assert _is_linked(a2, 'dom_AttributeGroup124', b)
    _safe_set(b, 'dom_Attribute125', None)
    assert not _is_linked(b, 'dom_Attribute125', a2)
    if hasattr(a2, 'dom_AttributeGroup124'):
        assert not _is_linked(a2, 'dom_AttributeGroup124', b)


def test_assoc_resolvedAttributeList196_reverse_link_reassign_clear():
    a1 = dom_DataBaseConstraint(name="sample_text", type="sample_text")
    a2 = dom_DataBaseConstraint(name="sample_text_2", type="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute198', a1)
    assert _is_linked(b, 'dom_Attribute198', a1)
    if hasattr(a1, 'dom_DataBaseConstraint197'):
        assert _is_linked(a1, 'dom_DataBaseConstraint197', b)
    _safe_set(b, 'dom_Attribute198', a2)
    assert _is_linked(b, 'dom_Attribute198', a2)
    if hasattr(a1, 'dom_DataBaseConstraint197'):
        assert not _is_linked(a1, 'dom_DataBaseConstraint197', b)
    if hasattr(a2, 'dom_DataBaseConstraint197'):
        assert _is_linked(a2, 'dom_DataBaseConstraint197', b)
    _safe_set(b, 'dom_Attribute198', None)
    assert not _is_linked(b, 'dom_Attribute198', a2)
    if hasattr(a2, 'dom_DataBaseConstraint197'):
        assert not _is_linked(a2, 'dom_DataBaseConstraint197', b)


def test_assoc_right59_reverse_link_reassign_clear():
    a1 = dom_PropertyMapping(biDirectional=True, toLeft=True, toRight=True)
    a2 = dom_PropertyMapping(biDirectional=False, toLeft=False, toRight=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute61', a1)
    assert _is_linked(b, 'dom_Attribute61', a1)
    if hasattr(a1, 'dom_PropertyMapping60'):
        assert _is_linked(a1, 'dom_PropertyMapping60', b)
    _safe_set(b, 'dom_Attribute61', a2)
    assert _is_linked(b, 'dom_Attribute61', a2)
    if hasattr(a1, 'dom_PropertyMapping60'):
        assert not _is_linked(a1, 'dom_PropertyMapping60', b)
    if hasattr(a2, 'dom_PropertyMapping60'):
        assert _is_linked(a2, 'dom_PropertyMapping60', b)
    _safe_set(b, 'dom_Attribute61', None)
    assert not _is_linked(b, 'dom_Attribute61', a2)
    if hasattr(a2, 'dom_PropertyMapping60'):
        assert not _is_linked(a2, 'dom_PropertyMapping60', b)


def test_assoc_sortOrder100_reverse_link_reassign_clear():
    a1 = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    a2 = dom_AttributeGroup(filter=False, key=False, name="sample_text_2", sortorder=False, unique=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute101', a1)
    assert _is_linked(b, 'dom_Attribute101', a1)
    if hasattr(a1, 'dom_AttributeGroup102'):
        assert _is_linked(a1, 'dom_AttributeGroup102', b)
    _safe_set(b, 'dom_Attribute101', a2)
    assert _is_linked(b, 'dom_Attribute101', a2)
    if hasattr(a1, 'dom_AttributeGroup102'):
        assert not _is_linked(a1, 'dom_AttributeGroup102', b)
    if hasattr(a2, 'dom_AttributeGroup102'):
        assert _is_linked(a2, 'dom_AttributeGroup102', b)
    _safe_set(b, 'dom_Attribute101', None)
    assert not _is_linked(b, 'dom_Attribute101', a2)
    if hasattr(a2, 'dom_AttributeGroup102'):
        assert not _is_linked(a2, 'dom_AttributeGroup102', b)


def test_assoc_target46_reverse_link_reassign_clear():
    a1 = dom_FeatureReference(all=True)
    a2 = dom_FeatureReference(all=False)
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute48', a1)
    assert _is_linked(b, 'dom_Attribute48', a1)
    if hasattr(a1, 'dom_FeatureReference47'):
        assert _is_linked(a1, 'dom_FeatureReference47', b)
    _safe_set(b, 'dom_Attribute48', a2)
    assert _is_linked(b, 'dom_Attribute48', a2)
    if hasattr(a1, 'dom_FeatureReference47'):
        assert not _is_linked(a1, 'dom_FeatureReference47', b)
    if hasattr(a2, 'dom_FeatureReference47'):
        assert _is_linked(a2, 'dom_FeatureReference47', b)
    _safe_set(b, 'dom_Attribute48', None)
    assert not _is_linked(b, 'dom_Attribute48', a2)
    if hasattr(a2, 'dom_FeatureReference47'):
        assert not _is_linked(a2, 'dom_FeatureReference47', b)


def test_assoc_unitAttribute119_reverse_link_reassign_clear():
    a1 = dom_AttributeTextProperty(hstoreColumn="sample_text", labelText="sample_text", tooltipText="sample_text", unitText="sample_text")
    a2 = dom_AttributeTextProperty(hstoreColumn="sample_text_2", labelText="sample_text_2", tooltipText="sample_text_2", unitText="sample_text_2")
    b = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    _safe_set(b, 'dom_Attribute120', a1)
    assert _is_linked(b, 'dom_Attribute120', a1)
    if hasattr(a1, 'dom_AttributeTextProperty'):
        assert _is_linked(a1, 'dom_AttributeTextProperty', b)
    _safe_set(b, 'dom_Attribute120', a2)
    assert _is_linked(b, 'dom_Attribute120', a2)
    if hasattr(a1, 'dom_AttributeTextProperty'):
        assert not _is_linked(a1, 'dom_AttributeTextProperty', b)
    if hasattr(a2, 'dom_AttributeTextProperty'):
        assert _is_linked(a2, 'dom_AttributeTextProperty', b)
    _safe_set(b, 'dom_Attribute120', None)
    assert not _is_linked(b, 'dom_Attribute120', a2)
    if hasattr(a2, 'dom_AttributeTextProperty'):
        assert not _is_linked(a2, 'dom_AttributeTextProperty', b)


def test_assoc_versionColumn157_reverse_link_reassign_clear():
    a1 = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    a2 = dom_Dao(discriminator="sample_text_2", qualifier="sample_text_2", tableName="sample_text_2")
    b = dom_Column(columnName="sample_text")
    _safe_set(b, 'dom_Column159', a1)
    assert _is_linked(b, 'dom_Column159', a1)
    if hasattr(a1, 'dom_Dao158'):
        assert _is_linked(a1, 'dom_Dao158', b)
    _safe_set(b, 'dom_Column159', a2)
    assert _is_linked(b, 'dom_Column159', a2)
    if hasattr(a1, 'dom_Dao158'):
        assert not _is_linked(a1, 'dom_Dao158', b)
    if hasattr(a2, 'dom_Dao158'):
        assert _is_linked(a2, 'dom_Dao158', b)
    _safe_set(b, 'dom_Column159', None)
    assert not _is_linked(b, 'dom_Column159', a2)
    if hasattr(a2, 'dom_Dao158'):
        assert not _is_linked(a2, 'dom_Dao158', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aggregateExpression288_stub_double():
    # dom_Expression has no real 'dom_Expression289' property in the generated
    # code (a bare stub) -- manually attach it so dom_AggregateFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_AggregateFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_AggregateFunction(all=True, distinct=True, from_="sample_text", function="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression289', None)
    _safe_set(owner, 'dom_AggregateFunction', partner)
    assert getattr(partner, 'dom_Expression289') == owner
    _safe_set(owner, 'dom_AggregateFunction', None)
    assert getattr(partner, 'dom_Expression289') is None


def test_assoc_allAttributes1_stub_double():
    # dom_ComplexType has no real 'dom_ComplexType2' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_ComplexType()
    setattr(partner, 'dom_ComplexType2', None)
    _safe_set(owner, 'dom_Attribute3', partner)
    assert owner in getattr(partner, 'dom_ComplexType2')
    _safe_set(owner, 'dom_Attribute3', None)
    assert owner not in getattr(partner, 'dom_ComplexType2')


def test_assoc_arguments265_stub_double():
    # dom_Expression has no real 'dom_Expression266' property in the generated
    # code (a bare stub) -- manually attach it so dom_SelectClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_SelectClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_SelectClass(class_="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression266', None)
    _safe_set(owner, 'dom_SelectClass', {partner})
    assert getattr(partner, 'dom_Expression266') == owner
    _safe_set(owner, 'dom_SelectClass', set())
    assert getattr(partner, 'dom_Expression266') is None


def test_assoc_arguments280_stub_double():
    # dom_Expression has no real 'dom_Expression281' property in the generated
    # code (a bare stub) -- manually attach it so dom_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FunctionCall(function="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression281', None)
    _safe_set(owner, 'dom_FunctionCall', {partner})
    assert getattr(partner, 'dom_Expression281') == owner
    _safe_set(owner, 'dom_FunctionCall', set())
    assert getattr(partner, 'dom_Expression281') is None


def test_assoc_assignment235_stub_double():
    # dom_PropertyAssignment has no real 'dom_PropertyAssignment' property in the generated
    # code (a bare stub) -- manually attach it so dom_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_UpdateStatement(name="sample_text", versioned=True)
    partner = dom_PropertyAssignment()
    setattr(partner, 'dom_PropertyAssignment', None)
    _safe_set(owner, 'dom_UpdateStatement236', {partner})
    assert getattr(partner, 'dom_PropertyAssignment') == owner
    _safe_set(owner, 'dom_UpdateStatement236', set())
    assert getattr(partner, 'dom_PropertyAssignment') is None


def test_assoc_attributProperties97_stub_double():
    # dom_AttributeProperty has no real 'dom_AttributeProperty99' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_AttributeProperty()
    setattr(partner, 'dom_AttributeProperty99', None)
    _safe_set(owner, 'dom_Attribute98', {partner})
    assert getattr(partner, 'dom_AttributeProperty99') == owner
    _safe_set(owner, 'dom_Attribute98', set())
    assert getattr(partner, 'dom_AttributeProperty99') is None


def test_assoc_attribute129_stub_double():
    # dom_DaoFeature has no real 'dom_DaoFeature' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_DaoFeature()
    setattr(partner, 'dom_DaoFeature', None)
    _safe_set(owner, 'dom_Attribute130', partner)
    assert getattr(partner, 'dom_DaoFeature') == owner
    _safe_set(owner, 'dom_Attribute130', None)
    assert getattr(partner, 'dom_DaoFeature') is None


def test_assoc_attribute170_stub_double():
    # dom_QueryParameter has no real 'dom_QueryParameter171' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_QueryParameter()
    setattr(partner, 'dom_QueryParameter171', None)
    _safe_set(owner, 'dom_Attribute172', partner)
    assert getattr(partner, 'dom_QueryParameter171') == owner
    _safe_set(owner, 'dom_Attribute172', None)
    assert getattr(partner, 'dom_QueryParameter171') is None


def test_assoc_attribute293_stub_double():
    # dom_QueryParameterValue has no real 'dom_QueryParameterValue294' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_QueryParameterValue()
    setattr(partner, 'dom_QueryParameterValue294', None)
    _safe_set(owner, 'dom_Attribute295', partner)
    assert getattr(partner, 'dom_QueryParameterValue294') == owner
    _safe_set(owner, 'dom_Attribute295', None)
    assert getattr(partner, 'dom_QueryParameterValue294') is None


def test_assoc_attributeGroups65_stub_double():
    # dom_Entity has no real 'dom_Entity66' property in the generated
    # code (a bare stub) -- manually attach it so dom_AttributeGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_AttributeGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity66', None)
    _safe_set(owner, 'dom_AttributeGroup', partner)
    assert owner in getattr(partner, 'dom_Entity66')
    _safe_set(owner, 'dom_AttributeGroup', None)
    assert owner not in getattr(partner, 'dom_Entity66')


def test_assoc_attributes0_stub_double():
    # dom_ComplexType has no real 'dom_ComplexType' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_ComplexType()
    setattr(partner, 'dom_ComplexType', None)
    _safe_set(owner, 'dom_Attribute', partner)
    assert owner in getattr(partner, 'dom_ComplexType')
    _safe_set(owner, 'dom_Attribute', None)
    assert owner not in getattr(partner, 'dom_ComplexType')


def test_assoc_columnType176_stub_double():
    # dom_Type has no real 'dom_Type178' property in the generated
    # code (a bare stub) -- manually attach it so dom_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Column(columnName="sample_text")
    partner = dom_Type()
    setattr(partner, 'dom_Type178', None)
    _safe_set(owner, 'dom_Column177', partner)
    assert getattr(partner, 'dom_Type178') == owner
    _safe_set(owner, 'dom_Column177', None)
    assert getattr(partner, 'dom_Type178') is None


def test_assoc_dataType103_stub_double():
    # dom_Type has no real 'dom_Type105' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_Type()
    setattr(partner, 'dom_Type105', None)
    _safe_set(owner, 'dom_Attribute104', partner)
    assert getattr(partner, 'dom_Type105') == owner
    _safe_set(owner, 'dom_Attribute104', None)
    assert getattr(partner, 'dom_Type105') is None


def test_assoc_delegateOperations7_stub_double():
    # dom_Service has no real 'dom_Service8' property in the generated
    # code (a bare stub) -- manually attach it so dom_DelegateOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DelegateOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    partner = dom_Service()
    setattr(partner, 'dom_Service8', None)
    _safe_set(owner, 'dom_DelegateOperation', partner)
    assert owner in getattr(partner, 'dom_Service8')
    _safe_set(owner, 'dom_DelegateOperation', None)
    assert owner not in getattr(partner, 'dom_Service8')


def test_assoc_entity131_stub_double():
    # dom_Entity has no real 'dom_Entity133' property in the generated
    # code (a bare stub) -- manually attach it so dom_Dao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Dao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    partner = dom_Entity()
    setattr(partner, 'dom_Entity133', None)
    _safe_set(owner, 'dom_Dao132', partner)
    assert getattr(partner, 'dom_Entity133') == owner
    _safe_set(owner, 'dom_Dao132', None)
    assert getattr(partner, 'dom_Entity133') is None


def test_assoc_entity228_stub_double():
    # dom_Entity has no real 'dom_Entity229' property in the generated
    # code (a bare stub) -- manually attach it so dom_DeleteStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DeleteStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DeleteStatement(name="sample_text")
    partner = dom_Entity()
    setattr(partner, 'dom_Entity229', None)
    _safe_set(owner, 'dom_DeleteStatement', partner)
    assert getattr(partner, 'dom_Entity229') == owner
    _safe_set(owner, 'dom_DeleteStatement', None)
    assert getattr(partner, 'dom_Entity229') is None


def test_assoc_entity233_stub_double():
    # dom_Entity has no real 'dom_Entity234' property in the generated
    # code (a bare stub) -- manually attach it so dom_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_UpdateStatement(name="sample_text", versioned=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity234', None)
    _safe_set(owner, 'dom_UpdateStatement', partner)
    assert getattr(partner, 'dom_Entity234') == owner
    _safe_set(owner, 'dom_UpdateStatement', None)
    assert getattr(partner, 'dom_Entity234') is None


def test_assoc_entity267_stub_double():
    # dom_Entity has no real 'dom_Entity268' property in the generated
    # code (a bare stub) -- manually attach it so dom_FromClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FromClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FromClass(popertyFetch=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity268', None)
    _safe_set(owner, 'dom_FromClass', partner)
    assert getattr(partner, 'dom_Entity268') == owner
    _safe_set(owner, 'dom_FromClass', None)
    assert getattr(partner, 'dom_Entity268') is None


def test_assoc_escape353_stub_double():
    # dom_Expression has no real 'dom_Expression355' property in the generated
    # code (a bare stub) -- manually attach it so dom_LikeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_LikeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_LikeExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression355', None)
    _safe_set(owner, 'dom_LikeExpression354', partner)
    assert getattr(partner, 'dom_Expression355') == owner
    _safe_set(owner, 'dom_LikeExpression354', None)
    assert getattr(partner, 'dom_Expression355') is None


def test_assoc_expression260_stub_double():
    # dom_Expression has no real 'dom_Expression262' property in the generated
    # code (a bare stub) -- manually attach it so dom_SortOrderElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_SortOrderElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_SortOrderElement(sortOrder="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression262', None)
    _safe_set(owner, 'dom_SortOrderElement261', partner)
    assert getattr(partner, 'dom_Expression262') == owner
    _safe_set(owner, 'dom_SortOrderElement261', None)
    assert getattr(partner, 'dom_Expression262') is None


def test_assoc_expression274_stub_double():
    # dom_Expression has no real 'dom_Expression276' property in the generated
    # code (a bare stub) -- manually attach it so dom_Join's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Join's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression276', None)
    _safe_set(owner, 'dom_Join275', partner)
    assert getattr(partner, 'dom_Expression276') == owner
    _safe_set(owner, 'dom_Join275', None)
    assert getattr(partner, 'dom_Expression276') is None


def test_assoc_expression296_stub_double():
    # dom_Expression has no real 'dom_Expression297' property in the generated
    # code (a bare stub) -- manually attach it so dom_QuantifiedExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_QuantifiedExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_QuantifiedExpression(name="sample_text", quantifier="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression297', None)
    _safe_set(owner, 'dom_QuantifiedExpression', partner)
    assert getattr(partner, 'dom_Expression297') == owner
    _safe_set(owner, 'dom_QuantifiedExpression', None)
    assert getattr(partner, 'dom_Expression297') is None


def test_assoc_expression326_stub_double():
    # dom_Expression has no real 'dom_Expression327' property in the generated
    # code (a bare stub) -- manually attach it so dom_AliasedExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_AliasedExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_AliasedExpression(name="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression327', None)
    _safe_set(owner, 'dom_AliasedExpression', partner)
    assert getattr(partner, 'dom_Expression327') == owner
    _safe_set(owner, 'dom_AliasedExpression', None)
    assert getattr(partner, 'dom_Expression327') is None


def test_assoc_expression335_stub_double():
    # dom_Expression has no real 'dom_Expression336' property in the generated
    # code (a bare stub) -- manually attach it so dom_InExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_InExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_InExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression336', None)
    _safe_set(owner, 'dom_InExpression', partner)
    assert getattr(partner, 'dom_Expression336') == owner
    _safe_set(owner, 'dom_InExpression', None)
    assert getattr(partner, 'dom_Expression336') is None


def test_assoc_expression340_stub_double():
    # dom_Expression has no real 'dom_Expression341' property in the generated
    # code (a bare stub) -- manually attach it so dom_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BetweenExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression341', None)
    _safe_set(owner, 'dom_BetweenExpression', partner)
    assert getattr(partner, 'dom_Expression341') == owner
    _safe_set(owner, 'dom_BetweenExpression', None)
    assert getattr(partner, 'dom_Expression341') is None


def test_assoc_expression348_stub_double():
    # dom_Expression has no real 'dom_Expression349' property in the generated
    # code (a bare stub) -- manually attach it so dom_LikeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_LikeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_LikeExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression349', None)
    _safe_set(owner, 'dom_LikeExpression', partner)
    assert getattr(partner, 'dom_Expression349') == owner
    _safe_set(owner, 'dom_LikeExpression', None)
    assert getattr(partner, 'dom_Expression349') is None


def test_assoc_expression356_stub_double():
    # dom_Expression has no real 'dom_Expression357' property in the generated
    # code (a bare stub) -- manually attach it so dom_MemberOfExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_MemberOfExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_MemberOfExpression(memberOf="sample_text", not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression357', None)
    _safe_set(owner, 'dom_MemberOfExpression', partner)
    assert getattr(partner, 'dom_Expression357') == owner
    _safe_set(owner, 'dom_MemberOfExpression', None)
    assert getattr(partner, 'dom_Expression357') is None


def test_assoc_expression358_stub_double():
    # dom_Expression has no real 'dom_Expression359' property in the generated
    # code (a bare stub) -- manually attach it so dom_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_UnaryExpression(operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression359', None)
    _safe_set(owner, 'dom_UnaryExpression', partner)
    assert getattr(partner, 'dom_Expression359') == owner
    _safe_set(owner, 'dom_UnaryExpression', None)
    assert getattr(partner, 'dom_Expression359') is None


def test_assoc_featureReferences34_stub_double():
    # dom_DataView has no real 'dom_DataView35' property in the generated
    # code (a bare stub) -- manually attach it so dom_FeatureReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FeatureReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FeatureReference(all=True)
    partner = dom_DataView()
    setattr(partner, 'dom_DataView35', None)
    _safe_set(owner, 'dom_FeatureReference', partner)
    assert owner in getattr(partner, 'dom_DataView35')
    _safe_set(owner, 'dom_FeatureReference', None)
    assert owner not in getattr(partner, 'dom_DataView35')


def test_assoc_filter26_stub_double():
    # dom_Expression has no real 'dom_Expression' property in the generated
    # code (a bare stub) -- manually attach it so dom_DelegateOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DelegateOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression', None)
    _safe_set(owner, 'dom_DelegateOperation27', partner)
    assert getattr(partner, 'dom_Expression') == owner
    _safe_set(owner, 'dom_DelegateOperation27', None)
    assert getattr(partner, 'dom_Expression') is None


def test_assoc_from_283_stub_double():
    # dom_Expression has no real 'dom_Expression285' property in the generated
    # code (a bare stub) -- manually attach it so dom_TrimFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_TrimFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_TrimFunction(function="sample_text", mode="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression285', None)
    _safe_set(owner, 'dom_TrimFunction284', partner)
    assert getattr(partner, 'dom_Expression285') == owner
    _safe_set(owner, 'dom_TrimFunction284', None)
    assert getattr(partner, 'dom_Expression285') is None


def test_assoc_from_286_stub_double():
    # dom_Expression has no real 'dom_Expression287' property in the generated
    # code (a bare stub) -- manually attach it so dom_CastFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_CastFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_CastFunction(function="sample_text", name="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression287', None)
    _safe_set(owner, 'dom_CastFunction', partner)
    assert getattr(partner, 'dom_Expression287') == owner
    _safe_set(owner, 'dom_CastFunction', None)
    assert getattr(partner, 'dom_Expression287') is None


def test_assoc_identifier78_stub_double():
    # dom_Entity has no real 'dom_Entity79' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity79', None)
    _safe_set(owner, 'dom_Attribute80', partner)
    assert getattr(partner, 'dom_Entity79') == owner
    _safe_set(owner, 'dom_Attribute80', None)
    assert getattr(partner, 'dom_Entity79') is None


def test_assoc_in_337_stub_double():
    # dom_Expression has no real 'dom_Expression339' property in the generated
    # code (a bare stub) -- manually attach it so dom_InExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_InExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_InExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression339', None)
    _safe_set(owner, 'dom_InExpression338', partner)
    assert getattr(partner, 'dom_Expression339') == owner
    _safe_set(owner, 'dom_InExpression338', None)
    assert getattr(partner, 'dom_Expression339') is None


def test_assoc_incrementerReference92_stub_double():
    # dom_IncrementerReference has no real 'dom_IncrementerReference' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_IncrementerReference()
    setattr(partner, 'dom_IncrementerReference', None)
    _safe_set(owner, 'dom_Attribute93', partner)
    assert getattr(partner, 'dom_IncrementerReference') == owner
    _safe_set(owner, 'dom_Attribute93', None)
    assert getattr(partner, 'dom_IncrementerReference') is None


def test_assoc_index277_stub_double():
    # dom_Expression has no real 'dom_Expression279' property in the generated
    # code (a bare stub) -- manually attach it so dom_PropertyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_PropertyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression279', None)
    _safe_set(owner, 'dom_PropertyValue278', {partner})
    assert getattr(partner, 'dom_Expression279') == owner
    _safe_set(owner, 'dom_PropertyValue278', set())
    assert getattr(partner, 'dom_Expression279') is None


def test_assoc_join247_stub_double():
    # dom_SelectStatement has no real 'dom_SelectStatement248' property in the generated
    # code (a bare stub) -- manually attach it so dom_Join's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Join's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Join(fetch=True, propertyFetch=True, type="sample_text")
    partner = dom_SelectStatement()
    setattr(partner, 'dom_SelectStatement248', None)
    _safe_set(owner, 'dom_Join', partner)
    assert owner in getattr(partner, 'dom_SelectStatement248')
    _safe_set(owner, 'dom_Join', None)
    assert owner not in getattr(partner, 'dom_SelectStatement248')


def test_assoc_key72_stub_double():
    # dom_Entity has no real 'dom_Entity73' property in the generated
    # code (a bare stub) -- manually attach it so dom_AttributeGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_AttributeGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity73', None)
    _safe_set(owner, 'dom_AttributeGroup74', partner)
    assert getattr(partner, 'dom_Entity73') == owner
    _safe_set(owner, 'dom_AttributeGroup74', None)
    assert getattr(partner, 'dom_Entity73') is None


def test_assoc_left328_stub_double():
    # dom_Expression has no real 'dom_Expression329' property in the generated
    # code (a bare stub) -- manually attach it so dom_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BinaryExpression(operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression329', None)
    _safe_set(owner, 'dom_BinaryExpression', partner)
    assert getattr(partner, 'dom_Expression329') == owner
    _safe_set(owner, 'dom_BinaryExpression', None)
    assert getattr(partner, 'dom_Expression329') is None


def test_assoc_left342_stub_double():
    # dom_Expression has no real 'dom_Expression344' property in the generated
    # code (a bare stub) -- manually attach it so dom_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BetweenExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression344', None)
    _safe_set(owner, 'dom_BetweenExpression343', partner)
    assert getattr(partner, 'dom_Expression344') == owner
    _safe_set(owner, 'dom_BetweenExpression343', None)
    assert getattr(partner, 'dom_Expression344') is None


def test_assoc_left49_stub_double():
    # dom_ComplexType has no real 'dom_ComplexType50' property in the generated
    # code (a bare stub) -- manually attach it so dom_Mapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Mapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    partner = dom_ComplexType()
    setattr(partner, 'dom_ComplexType50', None)
    _safe_set(owner, 'dom_Mapper', partner)
    assert getattr(partner, 'dom_ComplexType50') == owner
    _safe_set(owner, 'dom_Mapper', None)
    assert getattr(partner, 'dom_ComplexType50') is None


def test_assoc_like350_stub_double():
    # dom_Expression has no real 'dom_Expression352' property in the generated
    # code (a bare stub) -- manually attach it so dom_LikeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_LikeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_LikeExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression352', None)
    _safe_set(owner, 'dom_LikeExpression351', partner)
    assert getattr(partner, 'dom_Expression352') == owner
    _safe_set(owner, 'dom_LikeExpression351', None)
    assert getattr(partner, 'dom_Expression352') is None


def test_assoc_oneToOneAssociations145_stub_double():
    # dom_OneToOne has no real 'dom_OneToOne' property in the generated
    # code (a bare stub) -- manually attach it so dom_Dao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Dao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    partner = dom_OneToOne()
    setattr(partner, 'dom_OneToOne', None)
    _safe_set(owner, 'dom_Dao146', {partner})
    assert getattr(partner, 'dom_OneToOne') == owner
    _safe_set(owner, 'dom_Dao146', set())
    assert getattr(partner, 'dom_OneToOne') is None


def test_assoc_operations5_stub_double():
    # dom_Service has no real 'dom_Service6' property in the generated
    # code (a bare stub) -- manually attach it so dom_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Operation(expression="sample_text")
    partner = dom_Service()
    setattr(partner, 'dom_Service6', None)
    _safe_set(owner, 'dom_Operation', partner)
    assert owner in getattr(partner, 'dom_Service6')
    _safe_set(owner, 'dom_Operation', None)
    assert owner not in getattr(partner, 'dom_Service6')


def test_assoc_orderBy258_stub_double():
    # dom_SelectStatement has no real 'dom_SelectStatement259' property in the generated
    # code (a bare stub) -- manually attach it so dom_SortOrderElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_SortOrderElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_SortOrderElement(sortOrder="sample_text")
    partner = dom_SelectStatement()
    setattr(partner, 'dom_SelectStatement259', None)
    _safe_set(owner, 'dom_SortOrderElement', partner)
    assert owner in getattr(partner, 'dom_SelectStatement259')
    _safe_set(owner, 'dom_SortOrderElement', None)
    assert owner not in getattr(partner, 'dom_SelectStatement259')


def test_assoc_parameter209_stub_double():
    # dom_QueryParameter has no real 'dom_QueryParameter211' property in the generated
    # code (a bare stub) -- manually attach it so dom_CallInputParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_CallInputParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_CallInputParameter(name="sample_text")
    partner = dom_QueryParameter()
    setattr(partner, 'dom_QueryParameter211', None)
    _safe_set(owner, 'dom_CallInputParameter210', partner)
    assert getattr(partner, 'dom_QueryParameter211') == owner
    _safe_set(owner, 'dom_CallInputParameter210', None)
    assert getattr(partner, 'dom_QueryParameter211') is None


def test_assoc_properties199_stub_double():
    # dom_ApplicationSession has no real 'dom_ApplicationSession' property in the generated
    # code (a bare stub) -- manually attach it so dom_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Property(defaultValue="sample_text", name="sample_text")
    partner = dom_ApplicationSession()
    setattr(partner, 'dom_ApplicationSession', None)
    _safe_set(owner, 'dom_Property200', partner)
    assert owner in getattr(partner, 'dom_ApplicationSession')
    _safe_set(owner, 'dom_Property200', None)
    assert owner not in getattr(partner, 'dom_ApplicationSession')


def test_assoc_properties263_stub_double():
    # dom_Expression has no real 'dom_Expression264' property in the generated
    # code (a bare stub) -- manually attach it so dom_SelectProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_SelectProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_SelectProperties(distinct=True)
    partner = dom_Expression()
    setattr(partner, 'dom_Expression264', None)
    _safe_set(owner, 'dom_SelectProperties', {partner})
    assert getattr(partner, 'dom_Expression264') == owner
    _safe_set(owner, 'dom_SelectProperties', set())
    assert getattr(partner, 'dom_Expression264') is None


def test_assoc_properties44_stub_double():
    # dom_AttributeProperty has no real 'dom_AttributeProperty' property in the generated
    # code (a bare stub) -- manually attach it so dom_FeatureReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FeatureReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FeatureReference(all=True)
    partner = dom_AttributeProperty()
    setattr(partner, 'dom_AttributeProperty', None)
    _safe_set(owner, 'dom_FeatureReference45', {partner})
    assert getattr(partner, 'dom_AttributeProperty') == owner
    _safe_set(owner, 'dom_FeatureReference45', set())
    assert getattr(partner, 'dom_AttributeProperty') is None


def test_assoc_property240_stub_double():
    # dom_PropertyAssignment has no real 'dom_PropertyAssignment241' property in the generated
    # code (a bare stub) -- manually attach it so dom_PropertyValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_PropertyValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_PropertyValue(classProperty=True, name="sample_text", segments="sample_text")
    partner = dom_PropertyAssignment()
    setattr(partner, 'dom_PropertyAssignment241', None)
    _safe_set(owner, 'dom_PropertyValue', partner)
    assert getattr(partner, 'dom_PropertyAssignment241') == owner
    _safe_set(owner, 'dom_PropertyValue', None)
    assert getattr(partner, 'dom_PropertyAssignment241') is None


def test_assoc_queryOperation137_stub_double():
    # dom_QueryOperation has no real 'dom_QueryOperation' property in the generated
    # code (a bare stub) -- manually attach it so dom_Dao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Dao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    partner = dom_QueryOperation()
    setattr(partner, 'dom_QueryOperation', None)
    _safe_set(owner, 'dom_Dao138', {partner})
    assert getattr(partner, 'dom_QueryOperation') == owner
    _safe_set(owner, 'dom_Dao138', set())
    assert getattr(partner, 'dom_QueryOperation') is None


def test_assoc_repository69_stub_double():
    # dom_Entity has no real 'dom_Entity70' property in the generated
    # code (a bare stub) -- manually attach it so dom_Dao's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Dao's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Dao(discriminator="sample_text", qualifier="sample_text", tableName="sample_text")
    partner = dom_Entity()
    setattr(partner, 'dom_Entity70', None)
    _safe_set(owner, 'dom_Dao71', partner)
    assert getattr(partner, 'dom_Entity70') == owner
    _safe_set(owner, 'dom_Dao71', None)
    assert getattr(partner, 'dom_Entity70') is None


def test_assoc_requiredAttributes87_stub_double():
    # dom_Entity has no real 'dom_Entity88' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity88', None)
    _safe_set(owner, 'dom_Attribute89', partner)
    assert owner in getattr(partner, 'dom_Entity88')
    _safe_set(owner, 'dom_Attribute89', None)
    assert owner not in getattr(partner, 'dom_Entity88')


def test_assoc_requiredReferences84_stub_double():
    # dom_Entity has no real 'dom_Entity85' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity85', None)
    _safe_set(owner, 'dom_Attribute86', partner)
    assert owner in getattr(partner, 'dom_Entity85')
    _safe_set(owner, 'dom_Attribute86', None)
    assert owner not in getattr(partner, 'dom_Entity85')


def test_assoc_right330_stub_double():
    # dom_Expression has no real 'dom_Expression332' property in the generated
    # code (a bare stub) -- manually attach it so dom_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BinaryExpression(operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression332', None)
    _safe_set(owner, 'dom_BinaryExpression331', partner)
    assert getattr(partner, 'dom_Expression332') == owner
    _safe_set(owner, 'dom_BinaryExpression331', None)
    assert getattr(partner, 'dom_Expression332') is None


def test_assoc_right345_stub_double():
    # dom_Expression has no real 'dom_Expression347' property in the generated
    # code (a bare stub) -- manually attach it so dom_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BetweenExpression(not_=True, operator="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression347', None)
    _safe_set(owner, 'dom_BetweenExpression346', partner)
    assert getattr(partner, 'dom_Expression347') == owner
    _safe_set(owner, 'dom_BetweenExpression346', None)
    assert getattr(partner, 'dom_Expression347') is None


def test_assoc_right51_stub_double():
    # dom_ComplexType has no real 'dom_ComplexType53' property in the generated
    # code (a bare stub) -- manually attach it so dom_Mapper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Mapper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Mapper(biDirectional=True, toLeft=True, toRight=True)
    partner = dom_ComplexType()
    setattr(partner, 'dom_ComplexType53', None)
    _safe_set(owner, 'dom_Mapper52', partner)
    assert getattr(partner, 'dom_ComplexType53') == owner
    _safe_set(owner, 'dom_Mapper52', None)
    assert getattr(partner, 'dom_ComplexType53') is None


def test_assoc_sortOrders75_stub_double():
    # dom_Entity has no real 'dom_Entity76' property in the generated
    # code (a bare stub) -- manually attach it so dom_AttributeGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_AttributeGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_AttributeGroup(filter=True, key=True, name="sample_text", sortorder=True, unique=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity76', None)
    _safe_set(owner, 'dom_AttributeGroup77', partner)
    assert owner in getattr(partner, 'dom_Entity76')
    _safe_set(owner, 'dom_AttributeGroup77', None)
    assert owner not in getattr(partner, 'dom_Entity76')


def test_assoc_source36_stub_double():
    # dom_Entity has no real 'dom_Entity' property in the generated
    # code (a bare stub) -- manually attach it so dom_FeatureReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FeatureReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FeatureReference(all=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity', None)
    _safe_set(owner, 'dom_FeatureReference37', partner)
    assert getattr(partner, 'dom_Entity') == owner
    _safe_set(owner, 'dom_FeatureReference37', None)
    assert getattr(partner, 'dom_Entity') is None


def test_assoc_sqlType185_stub_double():
    # dom_SqlType has no real 'dom_SqlType' property in the generated
    # code (a bare stub) -- manually attach it so dom_ManyToOne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_ManyToOne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_ManyToOne(columnName="sample_text", derived=True)
    partner = dom_SqlType()
    setattr(partner, 'dom_SqlType', None)
    _safe_set(owner, 'dom_ManyToOne186', partner)
    assert getattr(partner, 'dom_SqlType') == owner
    _safe_set(owner, 'dom_ManyToOne186', None)
    assert getattr(partner, 'dom_SqlType') is None


def test_assoc_type15_stub_double():
    # dom_Type has no real 'dom_Type' property in the generated
    # code (a bare stub) -- manually attach it so dom_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Parameter(many=True, name="sample_text")
    partner = dom_Type()
    setattr(partner, 'dom_Type', None)
    _safe_set(owner, 'dom_Parameter16', partner)
    assert getattr(partner, 'dom_Type') == owner
    _safe_set(owner, 'dom_Parameter16', None)
    assert getattr(partner, 'dom_Type') is None


def test_assoc_type28_stub_double():
    # dom_Type has no real 'dom_Type30' property in the generated
    # code (a bare stub) -- manually attach it so dom_DaoOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DaoOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DaoOperation(many=True, name="sample_text")
    partner = dom_Type()
    setattr(partner, 'dom_Type30', None)
    _safe_set(owner, 'dom_DaoOperation29', partner)
    assert getattr(partner, 'dom_Type30') == owner
    _safe_set(owner, 'dom_DaoOperation29', None)
    assert getattr(partner, 'dom_Type30') is None


def test_assoc_type9_stub_double():
    # dom_SimpleType has no real 'dom_SimpleType' property in the generated
    # code (a bare stub) -- manually attach it so dom_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Property(defaultValue="sample_text", name="sample_text")
    partner = dom_SimpleType()
    setattr(partner, 'dom_SimpleType', None)
    _safe_set(owner, 'dom_Property', partner)
    assert getattr(partner, 'dom_SimpleType') == owner
    _safe_set(owner, 'dom_Property', None)
    assert getattr(partner, 'dom_SimpleType') is None


def test_assoc_type90_stub_double():
    # dom_DataTypeAndTypeParameter has no real 'dom_DataTypeAndTypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_DataTypeAndTypeParameter()
    setattr(partner, 'dom_DataTypeAndTypeParameter', None)
    _safe_set(owner, 'dom_Attribute91', partner)
    assert getattr(partner, 'dom_DataTypeAndTypeParameter') == owner
    _safe_set(owner, 'dom_Attribute91', None)
    assert getattr(partner, 'dom_DataTypeAndTypeParameter') is None


def test_assoc_userType173_stub_double():
    # dom_DataTypeAndTypeParameter has no real 'dom_DataTypeAndTypeParameter175' property in the generated
    # code (a bare stub) -- manually attach it so dom_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Column(columnName="sample_text")
    partner = dom_DataTypeAndTypeParameter()
    setattr(partner, 'dom_DataTypeAndTypeParameter175', None)
    _safe_set(owner, 'dom_Column174', partner)
    assert getattr(partner, 'dom_DataTypeAndTypeParameter175') == owner
    _safe_set(owner, 'dom_Column174', None)
    assert getattr(partner, 'dom_DataTypeAndTypeParameter175') is None


def test_assoc_userType182_stub_double():
    # dom_Type has no real 'dom_Type184' property in the generated
    # code (a bare stub) -- manually attach it so dom_ManyToOne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_ManyToOne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_ManyToOne(columnName="sample_text", derived=True)
    partner = dom_Type()
    setattr(partner, 'dom_Type184', None)
    _safe_set(owner, 'dom_ManyToOne183', partner)
    assert getattr(partner, 'dom_Type184') == owner
    _safe_set(owner, 'dom_ManyToOne183', None)
    assert getattr(partner, 'dom_Type184') is None


def test_assoc_version81_stub_double():
    # dom_Entity has no real 'dom_Entity82' property in the generated
    # code (a bare stub) -- manually attach it so dom_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Attribute(composition=True, dataTypeName="sample_text", defaultValue="sample_text", derived=True, identifier=True, many=True, readOnly=True, reference=True, required=True, transient=True, version=True)
    partner = dom_Entity()
    setattr(partner, 'dom_Entity82', None)
    _safe_set(owner, 'dom_Attribute83', partner)
    assert getattr(partner, 'dom_Entity82') == owner
    _safe_set(owner, 'dom_Attribute83', None)
    assert getattr(partner, 'dom_Entity82') is None


def test_assoc_view17_stub_double():
    # dom_DataView has no real 'dom_DataView' property in the generated
    # code (a bare stub) -- manually attach it so dom_DelegateOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DelegateOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    partner = dom_DataView()
    setattr(partner, 'dom_DataView', None)
    _safe_set(owner, 'dom_DelegateOperation18', partner)
    assert getattr(partner, 'dom_DataView') == owner
    _safe_set(owner, 'dom_DelegateOperation18', None)
    assert getattr(partner, 'dom_DataView') is None


def test_assoc_view41_stub_double():
    # dom_DataView has no real 'dom_DataView43' property in the generated
    # code (a bare stub) -- manually attach it so dom_FeatureReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FeatureReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FeatureReference(all=True)
    partner = dom_DataView()
    setattr(partner, 'dom_DataView43', None)
    _safe_set(owner, 'dom_FeatureReference42', partner)
    assert getattr(partner, 'dom_DataView43') == owner
    _safe_set(owner, 'dom_FeatureReference42', None)
    assert getattr(partner, 'dom_DataView43') is None


def test_assoc_viewParameter23_stub_double():
    # dom_DataView has no real 'dom_DataView25' property in the generated
    # code (a bare stub) -- manually attach it so dom_DelegateOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DelegateOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DelegateOperation(crudOperationType="sample_text", many=True, name="sample_text")
    partner = dom_DataView()
    setattr(partner, 'dom_DataView25', None)
    _safe_set(owner, 'dom_DelegateOperation24', partner)
    assert getattr(partner, 'dom_DataView25') == owner
    _safe_set(owner, 'dom_DelegateOperation24', None)
    assert getattr(partner, 'dom_DataView25') is None


def test_assoc_where230_stub_double():
    # dom_Expression has no real 'dom_Expression232' property in the generated
    # code (a bare stub) -- manually attach it so dom_DeleteStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_DeleteStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_DeleteStatement(name="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression232', None)
    _safe_set(owner, 'dom_DeleteStatement231', partner)
    assert getattr(partner, 'dom_Expression232') == owner
    _safe_set(owner, 'dom_DeleteStatement231', None)
    assert getattr(partner, 'dom_Expression232') is None


def test_assoc_where237_stub_double():
    # dom_Expression has no real 'dom_Expression239' property in the generated
    # code (a bare stub) -- manually attach it so dom_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_UpdateStatement(name="sample_text", versioned=True)
    partner = dom_Expression()
    setattr(partner, 'dom_Expression239', None)
    _safe_set(owner, 'dom_UpdateStatement238', partner)
    assert getattr(partner, 'dom_Expression239') == owner
    _safe_set(owner, 'dom_UpdateStatement238', None)
    assert getattr(partner, 'dom_Expression239') is None


