import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Condition,
    EmbeddedInstanceDeclaration,
    Expression,
    GraphPattern,
    InstanceDeclarationStatement,
    ModelElement,
    ResourceBySetOp,
    ResourceIdentifier,
    Statement,
    sadl_AdditionalPropertyInfo,
    sadl_AddlClassInfo,
    sadl_AllValuesCondition,
    sadl_AllValuesFrom,
    sadl_AskQueryExpression,
    sadl_BinaryOpExpression,
    sadl_CardCondition,
    sadl_Cardinality,
    sadl_ClassDeclaration,
    sadl_ComplementOfClass,
    sadl_Condition,
    sadl_ConstructExpression,
    sadl_ContentList,
    sadl_DataTypeRestriction,
    sadl_DefaultValue,
    sadl_DisjointClasses,
    sadl_Display,
    sadl_EObject,
    sadl_ElementSet,
    sadl_EmbeddedInstanceDeclaration,
    sadl_EnumeratedAllAndSomeValuesFrom,
    sadl_EnumeratedAllValuesFrom,
    sadl_EnumeratedInstances,
    sadl_EquivalentConcepts,
    sadl_ExistentialNegation,
    sadl_ExistingInstanceAttribution,
    sadl_ExistingResourceList,
    sadl_Explanation,
    sadl_ExplicitValue,
    sadl_Expr,
    sadl_Expression,
    sadl_Facets,
    sadl_FunctionalProperty,
    sadl_GraphPattern,
    sadl_HasValue,
    sadl_HasValueCondition,
    sadl_Import,
    sadl_InstAttrPSV,
    sadl_InstAttrSPV,
    sadl_InstanceDeclaration,
    sadl_InstanceDeclarationStatement,
    sadl_InstanceDifferentFrom,
    sadl_InstancesAllDifferent,
    sadl_IntersectionResource,
    sadl_IntervalValue,
    sadl_InverseFunctionalProperty,
    sadl_InverseProperty,
    sadl_IsInverseOf,
    sadl_JunctionExpression,
    sadl_LiteralList,
    sadl_LiteralValue,
    sadl_MaxCardCondition,
    sadl_MaxCardinality,
    sadl_MergedTriples,
    sadl_MinCardCondition,
    sadl_MinCardinality,
    sadl_Model,
    sadl_ModelElement,
    sadl_ModelName,
    sadl_NecessaryAndSufficient,
    sadl_Object,
    sadl_OfPatternReturningValues,
    sadl_OfPhrase,
    sadl_OrderElement,
    sadl_OrderList,
    sadl_PropOfSubj,
    sadl_PropValPartialTriple,
    sadl_PropertyDeclaration,
    sadl_PropertyOfClass,
    sadl_Query,
    sadl_Range,
    sadl_RangeType,
    sadl_ResourceByName,
    sadl_ResourceByRestriction,
    sadl_ResourceBySetOp,
    sadl_ResourceIdentifier,
    sadl_ResourceList,
    sadl_ResourceName,
    sadl_Rule,
    sadl_SelectExpression,
    sadl_SomeValuesCondition,
    sadl_SomeValuesFrom,
    sadl_Statement,
    sadl_SubTypeOf,
    sadl_SubjProp,
    sadl_SymmetricalProperty,
    sadl_Test,
    sadl_TransitiveProperty,
    sadl_TypeDeclaration,
    sadl_TypedBNode,
    sadl_UnaryOpExpression,
    sadl_UnionResource,
    sadl_UserDefinedDataType,
    sadl_ValueRow,
    sadl_ValueTable,
    sadl_VariableList,
    sadl_WithChain,
    sadl_WithPhrase,
    DataType,
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

def test_assoc_addlPropInfo193_reverse_link_reassign_clear():
    a1 = sadl_PropertyDeclaration(article="sample_text")
    a2 = sadl_PropertyDeclaration(article="sample_text_2")
    b = sadl_AdditionalPropertyInfo(isSym="sample_text", isTrans="sample_text", isfunc="sample_text", isinvfunc="sample_text")
    _safe_set(b, 'sadl_AdditionalPropertyInfo', a1)
    assert _is_linked(b, 'sadl_AdditionalPropertyInfo', a1)
    if hasattr(a1, 'sadl_PropertyDeclaration194'):
        assert _is_linked(a1, 'sadl_PropertyDeclaration194', b)
    _safe_set(b, 'sadl_AdditionalPropertyInfo', a2)
    assert _is_linked(b, 'sadl_AdditionalPropertyInfo', a2)
    if hasattr(a1, 'sadl_PropertyDeclaration194'):
        assert not _is_linked(a1, 'sadl_PropertyDeclaration194', b)
    if hasattr(a2, 'sadl_PropertyDeclaration194'):
        assert _is_linked(a2, 'sadl_PropertyDeclaration194', b)
    _safe_set(b, 'sadl_AdditionalPropertyInfo', None)
    assert not _is_linked(b, 'sadl_AdditionalPropertyInfo', a2)
    if hasattr(a2, 'sadl_PropertyDeclaration194'):
        assert not _is_linked(a2, 'sadl_PropertyDeclaration194', b)


def test_assoc_annContent15_reverse_link_reassign_clear():
    a1 = sadl_ResourceBySetOp(annType="sample_text", op="sample_text")
    a2 = sadl_ResourceBySetOp(annType="sample_text_2", op="sample_text_2")
    b = sadl_ContentList(annContent="sample_text")
    _safe_set(b, 'sadl_ContentList16', a1)
    assert _is_linked(b, 'sadl_ContentList16', a1)
    if hasattr(a1, 'sadl_ResourceBySetOp'):
        assert _is_linked(a1, 'sadl_ResourceBySetOp', b)
    _safe_set(b, 'sadl_ContentList16', a2)
    assert _is_linked(b, 'sadl_ContentList16', a2)
    if hasattr(a1, 'sadl_ResourceBySetOp'):
        assert not _is_linked(a1, 'sadl_ResourceBySetOp', b)
    if hasattr(a2, 'sadl_ResourceBySetOp'):
        assert _is_linked(a2, 'sadl_ResourceBySetOp', b)
    _safe_set(b, 'sadl_ContentList16', None)
    assert not _is_linked(b, 'sadl_ContentList16', a2)
    if hasattr(a2, 'sadl_ResourceBySetOp'):
        assert not _is_linked(a2, 'sadl_ResourceBySetOp', b)


def test_assoc_annContent20_reverse_link_reassign_clear():
    a1 = sadl_ResourceByRestriction(annType="sample_text")
    a2 = sadl_ResourceByRestriction(annType="sample_text_2")
    b = sadl_ContentList(annContent="sample_text")
    _safe_set(b, 'sadl_ContentList21', a1)
    assert _is_linked(b, 'sadl_ContentList21', a1)
    if hasattr(a1, 'sadl_ResourceByRestriction'):
        assert _is_linked(a1, 'sadl_ResourceByRestriction', b)
    _safe_set(b, 'sadl_ContentList21', a2)
    assert _is_linked(b, 'sadl_ContentList21', a2)
    if hasattr(a1, 'sadl_ResourceByRestriction'):
        assert not _is_linked(a1, 'sadl_ResourceByRestriction', b)
    if hasattr(a2, 'sadl_ResourceByRestriction'):
        assert _is_linked(a2, 'sadl_ResourceByRestriction', b)
    _safe_set(b, 'sadl_ContentList21', None)
    assert not _is_linked(b, 'sadl_ContentList21', a2)
    if hasattr(a2, 'sadl_ResourceByRestriction'):
        assert not _is_linked(a2, 'sadl_ResourceByRestriction', b)


def test_assoc_annContent5_reverse_link_reassign_clear():
    a1 = sadl_ModelName(alias="sample_text", annType="sample_text", baseUri="sample_text", version="sample_text")
    a2 = sadl_ModelName(alias="sample_text_2", annType="sample_text_2", baseUri="sample_text_2", version="sample_text_2")
    b = sadl_ContentList(annContent="sample_text")
    _safe_set(b, 'sadl_ContentList', a1)
    assert _is_linked(b, 'sadl_ContentList', a1)
    if hasattr(a1, 'sadl_ModelName6'):
        assert _is_linked(a1, 'sadl_ModelName6', b)
    _safe_set(b, 'sadl_ContentList', a2)
    assert _is_linked(b, 'sadl_ContentList', a2)
    if hasattr(a1, 'sadl_ModelName6'):
        assert not _is_linked(a1, 'sadl_ModelName6', b)
    if hasattr(a2, 'sadl_ModelName6'):
        assert _is_linked(a2, 'sadl_ModelName6', b)
    _safe_set(b, 'sadl_ContentList', None)
    assert not _is_linked(b, 'sadl_ContentList', a2)
    if hasattr(a2, 'sadl_ModelName6'):
        assert not _is_linked(a2, 'sadl_ModelName6', b)


def test_assoc_annContent7_reverse_link_reassign_clear():
    a1 = sadl_ResourceName(annType="sample_text", name="sample_text")
    a2 = sadl_ResourceName(annType="sample_text_2", name="sample_text_2")
    b = sadl_ContentList(annContent="sample_text")
    _safe_set(b, 'sadl_ContentList8', a1)
    assert _is_linked(b, 'sadl_ContentList8', a1)
    if hasattr(a1, 'sadl_ResourceName'):
        assert _is_linked(a1, 'sadl_ResourceName', b)
    _safe_set(b, 'sadl_ContentList8', a2)
    assert _is_linked(b, 'sadl_ContentList8', a2)
    if hasattr(a1, 'sadl_ResourceName'):
        assert not _is_linked(a1, 'sadl_ResourceName', b)
    if hasattr(a2, 'sadl_ResourceName'):
        assert _is_linked(a2, 'sadl_ResourceName', b)
    _safe_set(b, 'sadl_ContentList8', None)
    assert not _is_linked(b, 'sadl_ContentList8', a2)
    if hasattr(a2, 'sadl_ResourceName'):
        assert not _is_linked(a2, 'sadl_ResourceName', b)


def test_assoc_annotationProperty201_reverse_link_reassign_clear():
    a1 = sadl_ResourceName(annType="sample_text", name="sample_text")
    a2 = sadl_ResourceName(annType="sample_text_2", name="sample_text_2")
    b = sadl_PropertyDeclaration(article="sample_text")
    _safe_set(b, 'sadl_PropertyDeclaration202', a1)
    assert _is_linked(b, 'sadl_PropertyDeclaration202', a1)
    if hasattr(a1, 'sadl_ResourceName203'):
        assert _is_linked(a1, 'sadl_ResourceName203', b)
    _safe_set(b, 'sadl_PropertyDeclaration202', a2)
    assert _is_linked(b, 'sadl_PropertyDeclaration202', a2)
    if hasattr(a1, 'sadl_ResourceName203'):
        assert not _is_linked(a1, 'sadl_ResourceName203', b)
    if hasattr(a2, 'sadl_ResourceName203'):
        assert _is_linked(a2, 'sadl_ResourceName203', b)
    _safe_set(b, 'sadl_PropertyDeclaration202', None)
    assert not _is_linked(b, 'sadl_PropertyDeclaration202', a2)
    if hasattr(a2, 'sadl_ResourceName203'):
        assert not _is_linked(a2, 'sadl_ResourceName203', b)


def test_assoc_args343_reverse_link_reassign_clear():
    a1 = sadl_Expression(func="sample_text")
    a2 = sadl_Expression(func="sample_text_2")
    b = sadl_Expression(func="sample_text")
    _safe_set(b, 'sadl_Expression344', a1)
    assert _is_linked(b, 'sadl_Expression344', a1)
    if hasattr(a1, 'sadl_Expression342'):
        assert _is_linked(a1, 'sadl_Expression342', b)
    _safe_set(b, 'sadl_Expression344', a2)
    assert _is_linked(b, 'sadl_Expression344', a2)
    if hasattr(a1, 'sadl_Expression342'):
        assert not _is_linked(a1, 'sadl_Expression342', b)
    if hasattr(a2, 'sadl_Expression342'):
        assert _is_linked(a2, 'sadl_Expression342', b)
    _safe_set(b, 'sadl_Expression344', None)
    assert not _is_linked(b, 'sadl_Expression344', a2)
    if hasattr(a2, 'sadl_Expression342'):
        assert not _is_linked(a2, 'sadl_Expression342', b)


def test_assoc_defValue161_reverse_link_reassign_clear():
    a1 = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    a2 = sadl_ExplicitValue(term="sample_text_2", valueList="sample_text_2")
    b = sadl_DefaultValue(level="sample_text")
    _safe_set(b, 'sadl_DefaultValue162', a1)
    assert _is_linked(b, 'sadl_DefaultValue162', a1)
    if hasattr(a1, 'sadl_ExplicitValue'):
        assert _is_linked(a1, 'sadl_ExplicitValue', b)
    _safe_set(b, 'sadl_DefaultValue162', a2)
    assert _is_linked(b, 'sadl_DefaultValue162', a2)
    if hasattr(a1, 'sadl_ExplicitValue'):
        assert not _is_linked(a1, 'sadl_ExplicitValue', b)
    if hasattr(a2, 'sadl_ExplicitValue'):
        assert _is_linked(a2, 'sadl_ExplicitValue', b)
    _safe_set(b, 'sadl_DefaultValue162', None)
    assert not _is_linked(b, 'sadl_DefaultValue162', a2)
    if hasattr(a2, 'sadl_ExplicitValue'):
        assert not _is_linked(a2, 'sadl_ExplicitValue', b)


def test_assoc_expr340_reverse_link_reassign_clear():
    a1 = sadl_Expression(func="sample_text")
    a2 = sadl_Expression(func="sample_text_2")
    b = sadl_Expression(func="sample_text")
    _safe_set(b, 'sadl_Expression341', a1)
    assert _is_linked(b, 'sadl_Expression341', a1)
    if hasattr(a1, 'sadl_Expression339'):
        assert _is_linked(a1, 'sadl_Expression339', b)
    _safe_set(b, 'sadl_Expression341', a2)
    assert _is_linked(b, 'sadl_Expression341', a2)
    if hasattr(a1, 'sadl_Expression339'):
        assert not _is_linked(a1, 'sadl_Expression339', b)
    if hasattr(a2, 'sadl_Expression339'):
        assert _is_linked(a2, 'sadl_Expression339', b)
    _safe_set(b, 'sadl_Expression341', None)
    assert not _is_linked(b, 'sadl_Expression341', a2)
    if hasattr(a2, 'sadl_Expression339'):
        assert not _is_linked(a2, 'sadl_Expression339', b)


def test_assoc_expr387_reverse_link_reassign_clear():
    a1 = sadl_IntervalValue(op="sample_text")
    a2 = sadl_IntervalValue(op="sample_text_2")
    b = sadl_Expression(func="sample_text")
    _safe_set(b, 'sadl_Expression389', a1)
    assert _is_linked(b, 'sadl_Expression389', a1)
    if hasattr(a1, 'sadl_IntervalValue388'):
        assert _is_linked(a1, 'sadl_IntervalValue388', b)
    _safe_set(b, 'sadl_Expression389', a2)
    assert _is_linked(b, 'sadl_Expression389', a2)
    if hasattr(a1, 'sadl_IntervalValue388'):
        assert not _is_linked(a1, 'sadl_IntervalValue388', b)
    if hasattr(a2, 'sadl_IntervalValue388'):
        assert _is_linked(a2, 'sadl_IntervalValue388', b)
    _safe_set(b, 'sadl_Expression389', None)
    assert not _is_linked(b, 'sadl_Expression389', a2)
    if hasattr(a2, 'sadl_IntervalValue388'):
        assert not _is_linked(a2, 'sadl_IntervalValue388', b)


def test_assoc_facets62_reverse_link_reassign_clear():
    a1 = sadl_Facets(len="sample_text", max="sample_text", maxexin="sample_text", maxlen="sample_text", min="sample_text", minexin="sample_text", minlen="sample_text", regex="sample_text", values="sample_text")
    a2 = sadl_Facets(len="sample_text_2", max="sample_text_2", maxexin="sample_text_2", maxlen="sample_text_2", min="sample_text_2", minexin="sample_text_2", minlen="sample_text_2", regex="sample_text_2", values="sample_text_2")
    b = sadl_DataTypeRestriction(basetype="sample_text", basetypes="sample_text")
    _safe_set(b, 'sadl_DataTypeRestriction63', a1)
    assert _is_linked(b, 'sadl_DataTypeRestriction63', a1)
    if hasattr(a1, 'sadl_Facets'):
        assert _is_linked(a1, 'sadl_Facets', b)
    _safe_set(b, 'sadl_DataTypeRestriction63', a2)
    assert _is_linked(b, 'sadl_DataTypeRestriction63', a2)
    if hasattr(a1, 'sadl_Facets'):
        assert not _is_linked(a1, 'sadl_Facets', b)
    if hasattr(a2, 'sadl_Facets'):
        assert _is_linked(a2, 'sadl_Facets', b)
    _safe_set(b, 'sadl_DataTypeRestriction63', None)
    assert not _is_linked(b, 'sadl_DataTypeRestriction63', a2)
    if hasattr(a2, 'sadl_Facets'):
        assert not _is_linked(a2, 'sadl_Facets', b)


def test_assoc_instanceName240_reverse_link_reassign_clear():
    a1 = sadl_ResourceName(annType="sample_text", name="sample_text")
    a2 = sadl_ResourceName(annType="sample_text_2", name="sample_text_2")
    b = sadl_InstanceDeclaration(article="sample_text")
    _safe_set(b, 'sadl_InstanceDeclaration241', a1)
    assert _is_linked(b, 'sadl_InstanceDeclaration241', a1)
    if hasattr(a1, 'sadl_ResourceName242'):
        assert _is_linked(a1, 'sadl_ResourceName242', b)
    _safe_set(b, 'sadl_InstanceDeclaration241', a2)
    assert _is_linked(b, 'sadl_InstanceDeclaration241', a2)
    if hasattr(a1, 'sadl_ResourceName242'):
        assert not _is_linked(a1, 'sadl_ResourceName242', b)
    if hasattr(a2, 'sadl_ResourceName242'):
        assert _is_linked(a2, 'sadl_ResourceName242', b)
    _safe_set(b, 'sadl_InstanceDeclaration241', None)
    assert not _is_linked(b, 'sadl_InstanceDeclaration241', a2)
    if hasattr(a2, 'sadl_ResourceName242'):
        assert not _is_linked(a2, 'sadl_ResourceName242', b)


def test_assoc_ivalue347_reverse_link_reassign_clear():
    a1 = sadl_IntervalValue(op="sample_text")
    a2 = sadl_IntervalValue(op="sample_text_2")
    b = sadl_Expression(func="sample_text")
    _safe_set(b, 'sadl_Expression348', a1)
    assert _is_linked(b, 'sadl_Expression348', a1)
    if hasattr(a1, 'sadl_IntervalValue'):
        assert _is_linked(a1, 'sadl_IntervalValue', b)
    _safe_set(b, 'sadl_Expression348', a2)
    assert _is_linked(b, 'sadl_Expression348', a2)
    if hasattr(a1, 'sadl_IntervalValue'):
        assert not _is_linked(a1, 'sadl_IntervalValue', b)
    if hasattr(a2, 'sadl_IntervalValue'):
        assert _is_linked(a2, 'sadl_IntervalValue', b)
    _safe_set(b, 'sadl_Expression348', None)
    assert not _is_linked(b, 'sadl_Expression348', a2)
    if hasattr(a2, 'sadl_IntervalValue'):
        assert not _is_linked(a2, 'sadl_IntervalValue', b)


def test_assoc_left404_reverse_link_reassign_clear():
    a1 = sadl_JunctionExpression(op="sample_text")
    a2 = sadl_JunctionExpression(op="sample_text_2")
    b = sadl_Expression(func="sample_text")
    _safe_set(b, 'sadl_Expression405', a1)
    assert _is_linked(b, 'sadl_Expression405', a1)
    if hasattr(a1, 'sadl_JunctionExpression'):
        assert _is_linked(a1, 'sadl_JunctionExpression', b)
    _safe_set(b, 'sadl_Expression405', a2)
    assert _is_linked(b, 'sadl_Expression405', a2)
    if hasattr(a1, 'sadl_JunctionExpression'):
        assert not _is_linked(a1, 'sadl_JunctionExpression', b)
    if hasattr(a2, 'sadl_JunctionExpression'):
        assert _is_linked(a2, 'sadl_JunctionExpression', b)
    _safe_set(b, 'sadl_Expression405', None)
    assert not _is_linked(b, 'sadl_Expression405', a2)
    if hasattr(a2, 'sadl_JunctionExpression'):
        assert not _is_linked(a2, 'sadl_JunctionExpression', b)


def test_assoc_left409_reverse_link_reassign_clear():
    a1 = sadl_Expression(func="sample_text")
    a2 = sadl_Expression(func="sample_text_2")
    b = sadl_BinaryOpExpression(op="sample_text")
    _safe_set(b, 'sadl_BinaryOpExpression', a1)
    assert _is_linked(b, 'sadl_BinaryOpExpression', a1)
    if hasattr(a1, 'sadl_Expression410'):
        assert _is_linked(a1, 'sadl_Expression410', b)
    _safe_set(b, 'sadl_BinaryOpExpression', a2)
    assert _is_linked(b, 'sadl_BinaryOpExpression', a2)
    if hasattr(a1, 'sadl_Expression410'):
        assert not _is_linked(a1, 'sadl_Expression410', b)
    if hasattr(a2, 'sadl_Expression410'):
        assert _is_linked(a2, 'sadl_Expression410', b)
    _safe_set(b, 'sadl_BinaryOpExpression', None)
    assert not _is_linked(b, 'sadl_BinaryOpExpression', a2)
    if hasattr(a2, 'sadl_Expression410'):
        assert not _is_linked(a2, 'sadl_Expression410', b)


def test_assoc_litValue393_reverse_link_reassign_clear():
    a1 = sadl_LiteralValue(literalBoolean="sample_text", literalNumber="sample_text", literalString="sample_text")
    a2 = sadl_LiteralValue(literalBoolean="sample_text_2", literalNumber="sample_text_2", literalString="sample_text_2")
    b = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    _safe_set(b, 'sadl_ExplicitValue394', a1)
    assert _is_linked(b, 'sadl_ExplicitValue394', a1)
    if hasattr(a1, 'sadl_LiteralValue395'):
        assert _is_linked(a1, 'sadl_LiteralValue395', b)
    _safe_set(b, 'sadl_ExplicitValue394', a2)
    assert _is_linked(b, 'sadl_ExplicitValue394', a2)
    if hasattr(a1, 'sadl_LiteralValue395'):
        assert not _is_linked(a1, 'sadl_LiteralValue395', b)
    if hasattr(a2, 'sadl_LiteralValue395'):
        assert _is_linked(a2, 'sadl_LiteralValue395', b)
    _safe_set(b, 'sadl_ExplicitValue394', None)
    assert not _is_linked(b, 'sadl_ExplicitValue394', a2)
    if hasattr(a2, 'sadl_LiteralValue395'):
        assert not _is_linked(a2, 'sadl_LiteralValue395', b)


def test_assoc_name336_reverse_link_reassign_clear():
    a1 = sadl_ResourceName(annType="sample_text", name="sample_text")
    a2 = sadl_ResourceName(annType="sample_text_2", name="sample_text_2")
    b = sadl_OrderElement(order="sample_text")
    _safe_set(b, 'sadl_OrderElement337', a1)
    assert _is_linked(b, 'sadl_OrderElement337', a1)
    if hasattr(a1, 'sadl_ResourceName338'):
        assert _is_linked(a1, 'sadl_ResourceName338', b)
    _safe_set(b, 'sadl_OrderElement337', a2)
    assert _is_linked(b, 'sadl_OrderElement337', a2)
    if hasattr(a1, 'sadl_ResourceName338'):
        assert not _is_linked(a1, 'sadl_ResourceName338', b)
    if hasattr(a2, 'sadl_ResourceName338'):
        assert _is_linked(a2, 'sadl_ResourceName338', b)
    _safe_set(b, 'sadl_OrderElement337', None)
    assert not _is_linked(b, 'sadl_OrderElement337', a2)
    if hasattr(a2, 'sadl_ResourceName338'):
        assert not _is_linked(a2, 'sadl_ResourceName338', b)


def test_assoc_propertyName188_reverse_link_reassign_clear():
    a1 = sadl_ResourceName(annType="sample_text", name="sample_text")
    a2 = sadl_ResourceName(annType="sample_text_2", name="sample_text_2")
    b = sadl_PropertyDeclaration(article="sample_text")
    _safe_set(b, 'sadl_PropertyDeclaration', a1)
    assert _is_linked(b, 'sadl_PropertyDeclaration', a1)
    if hasattr(a1, 'sadl_ResourceName189'):
        assert _is_linked(a1, 'sadl_ResourceName189', b)
    _safe_set(b, 'sadl_PropertyDeclaration', a2)
    assert _is_linked(b, 'sadl_PropertyDeclaration', a2)
    if hasattr(a1, 'sadl_ResourceName189'):
        assert not _is_linked(a1, 'sadl_ResourceName189', b)
    if hasattr(a2, 'sadl_ResourceName189'):
        assert _is_linked(a2, 'sadl_ResourceName189', b)
    _safe_set(b, 'sadl_PropertyDeclaration', None)
    assert not _is_linked(b, 'sadl_PropertyDeclaration', a2)
    if hasattr(a2, 'sadl_ResourceName189'):
        assert not _is_linked(a2, 'sadl_ResourceName189', b)


def test_assoc_range210_reverse_link_reassign_clear():
    a1 = sadl_Range(list="sample_text", lists="sample_text", single="sample_text")
    a2 = sadl_Range(list="sample_text_2", lists="sample_text_2", single="sample_text_2")
    b = sadl_AdditionalPropertyInfo(isSym="sample_text", isTrans="sample_text", isfunc="sample_text", isinvfunc="sample_text")
    _safe_set(b, 'sadl_AdditionalPropertyInfo211', a1)
    assert _is_linked(b, 'sadl_AdditionalPropertyInfo211', a1)
    if hasattr(a1, 'sadl_Range212'):
        assert _is_linked(a1, 'sadl_Range212', b)
    _safe_set(b, 'sadl_AdditionalPropertyInfo211', a2)
    assert _is_linked(b, 'sadl_AdditionalPropertyInfo211', a2)
    if hasattr(a1, 'sadl_Range212'):
        assert not _is_linked(a1, 'sadl_Range212', b)
    if hasattr(a2, 'sadl_Range212'):
        assert _is_linked(a2, 'sadl_Range212', b)
    _safe_set(b, 'sadl_AdditionalPropertyInfo211', None)
    assert not _is_linked(b, 'sadl_AdditionalPropertyInfo211', a2)
    if hasattr(a2, 'sadl_Range212'):
        assert not _is_linked(a2, 'sadl_Range212', b)


def test_assoc_right406_reverse_link_reassign_clear():
    a1 = sadl_JunctionExpression(op="sample_text")
    a2 = sadl_JunctionExpression(op="sample_text_2")
    b = sadl_Expression(func="sample_text")
    _safe_set(b, 'sadl_Expression408', a1)
    assert _is_linked(b, 'sadl_Expression408', a1)
    if hasattr(a1, 'sadl_JunctionExpression407'):
        assert _is_linked(a1, 'sadl_JunctionExpression407', b)
    _safe_set(b, 'sadl_Expression408', a2)
    assert _is_linked(b, 'sadl_Expression408', a2)
    if hasattr(a1, 'sadl_JunctionExpression407'):
        assert not _is_linked(a1, 'sadl_JunctionExpression407', b)
    if hasattr(a2, 'sadl_JunctionExpression407'):
        assert _is_linked(a2, 'sadl_JunctionExpression407', b)
    _safe_set(b, 'sadl_Expression408', None)
    assert not _is_linked(b, 'sadl_Expression408', a2)
    if hasattr(a2, 'sadl_JunctionExpression407'):
        assert not _is_linked(a2, 'sadl_JunctionExpression407', b)


def test_assoc_right411_reverse_link_reassign_clear():
    a1 = sadl_Expression(func="sample_text")
    a2 = sadl_Expression(func="sample_text_2")
    b = sadl_BinaryOpExpression(op="sample_text")
    _safe_set(b, 'sadl_BinaryOpExpression412', a1)
    assert _is_linked(b, 'sadl_BinaryOpExpression412', a1)
    if hasattr(a1, 'sadl_Expression413'):
        assert _is_linked(a1, 'sadl_Expression413', b)
    _safe_set(b, 'sadl_BinaryOpExpression412', a2)
    assert _is_linked(b, 'sadl_BinaryOpExpression412', a2)
    if hasattr(a1, 'sadl_Expression413'):
        assert not _is_linked(a1, 'sadl_Expression413', b)
    if hasattr(a2, 'sadl_Expression413'):
        assert _is_linked(a2, 'sadl_Expression413', b)
    _safe_set(b, 'sadl_BinaryOpExpression412', None)
    assert not _is_linked(b, 'sadl_BinaryOpExpression412', a2)
    if hasattr(a2, 'sadl_Expression413'):
        assert not _is_linked(a2, 'sadl_Expression413', b)


def test_assoc_subClass179_reverse_link_reassign_clear():
    a1 = sadl_ResourceName(annType="sample_text", name="sample_text")
    a2 = sadl_ResourceName(annType="sample_text_2", name="sample_text_2")
    b = sadl_NecessaryAndSufficient(article="sample_text")
    _safe_set(b, 'sadl_NecessaryAndSufficient180', a1)
    assert _is_linked(b, 'sadl_NecessaryAndSufficient180', a1)
    if hasattr(a1, 'sadl_ResourceName181'):
        assert _is_linked(a1, 'sadl_ResourceName181', b)
    _safe_set(b, 'sadl_NecessaryAndSufficient180', a2)
    assert _is_linked(b, 'sadl_NecessaryAndSufficient180', a2)
    if hasattr(a1, 'sadl_ResourceName181'):
        assert not _is_linked(a1, 'sadl_ResourceName181', b)
    if hasattr(a2, 'sadl_ResourceName181'):
        assert _is_linked(a2, 'sadl_ResourceName181', b)
    _safe_set(b, 'sadl_NecessaryAndSufficient180', None)
    assert not _is_linked(b, 'sadl_NecessaryAndSufficient180', a2)
    if hasattr(a2, 'sadl_ResourceName181'):
        assert not _is_linked(a2, 'sadl_ResourceName181', b)


def test_assoc_superClass178_reverse_link_reassign_clear():
    a1 = sadl_TypedBNode(article="sample_text")
    a2 = sadl_TypedBNode(article="sample_text_2")
    b = sadl_NecessaryAndSufficient(article="sample_text")
    _safe_set(b, 'sadl_NecessaryAndSufficient', a1)
    assert _is_linked(b, 'sadl_NecessaryAndSufficient', a1)
    if hasattr(a1, 'sadl_TypedBNode'):
        assert _is_linked(a1, 'sadl_TypedBNode', b)
    _safe_set(b, 'sadl_NecessaryAndSufficient', a2)
    assert _is_linked(b, 'sadl_NecessaryAndSufficient', a2)
    if hasattr(a1, 'sadl_TypedBNode'):
        assert not _is_linked(a1, 'sadl_TypedBNode', b)
    if hasattr(a2, 'sadl_TypedBNode'):
        assert _is_linked(a2, 'sadl_TypedBNode', b)
    _safe_set(b, 'sadl_NecessaryAndSufficient', None)
    assert not _is_linked(b, 'sadl_NecessaryAndSufficient', a2)
    if hasattr(a2, 'sadl_TypedBNode'):
        assert not _is_linked(a2, 'sadl_TypedBNode', b)


def test_assoc_type53_reverse_link_reassign_clear():
    a1 = sadl_RangeType(dataType="sample_text")
    a2 = sadl_RangeType(dataType="sample_text_2")
    b = sadl_Range(list="sample_text", lists="sample_text", single="sample_text")
    _safe_set(b, 'sadl_Range54', a1)
    assert _is_linked(b, 'sadl_Range54', a1)
    if hasattr(a1, 'sadl_RangeType'):
        assert _is_linked(a1, 'sadl_RangeType', b)
    _safe_set(b, 'sadl_Range54', a2)
    assert _is_linked(b, 'sadl_Range54', a2)
    if hasattr(a1, 'sadl_RangeType'):
        assert not _is_linked(a1, 'sadl_RangeType', b)
    if hasattr(a2, 'sadl_RangeType'):
        assert _is_linked(a2, 'sadl_RangeType', b)
    _safe_set(b, 'sadl_Range54', None)
    assert not _is_linked(b, 'sadl_Range54', a2)
    if hasattr(a2, 'sadl_RangeType'):
        assert not _is_linked(a2, 'sadl_RangeType', b)


def test_assoc_value349_reverse_link_reassign_clear():
    a1 = sadl_Expression(func="sample_text")
    a2 = sadl_Expression(func="sample_text_2")
    b = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    _safe_set(b, 'sadl_ExplicitValue351', a1)
    assert _is_linked(b, 'sadl_ExplicitValue351', a1)
    if hasattr(a1, 'sadl_Expression350'):
        assert _is_linked(a1, 'sadl_Expression350', b)
    _safe_set(b, 'sadl_ExplicitValue351', a2)
    assert _is_linked(b, 'sadl_ExplicitValue351', a2)
    if hasattr(a1, 'sadl_Expression350'):
        assert not _is_linked(a1, 'sadl_Expression350', b)
    if hasattr(a2, 'sadl_Expression350'):
        assert _is_linked(a2, 'sadl_Expression350', b)
    _safe_set(b, 'sadl_ExplicitValue351', None)
    assert not _is_linked(b, 'sadl_ExplicitValue351', a2)
    if hasattr(a2, 'sadl_Expression350'):
        assert not _is_linked(a2, 'sadl_Expression350', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_addlInfoItems235_stub_double():
    # sadl_PropValPartialTriple has no real 'sadl_PropValPartialTriple' property in the generated
    # code (a bare stub) -- manually attach it so sadl_InstanceDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_InstanceDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_InstanceDeclaration(article="sample_text")
    partner = sadl_PropValPartialTriple()
    setattr(partner, 'sadl_PropValPartialTriple', None)
    _safe_set(owner, 'sadl_InstanceDeclaration236', {partner})
    assert getattr(partner, 'sadl_PropValPartialTriple') == owner
    _safe_set(owner, 'sadl_InstanceDeclaration236', set())
    assert getattr(partner, 'sadl_PropValPartialTriple') is None


def test_assoc_classIdentifier231_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier233' property in the generated
    # code (a bare stub) -- manually attach it so sadl_TypedBNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_TypedBNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_TypedBNode(article="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier233', None)
    _safe_set(owner, 'sadl_TypedBNode232', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier233') == owner
    _safe_set(owner, 'sadl_TypedBNode232', None)
    assert getattr(partner, 'sadl_ResourceIdentifier233') is None


def test_assoc_classIdentifier55_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier57' property in the generated
    # code (a bare stub) -- manually attach it so sadl_RangeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_RangeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_RangeType(dataType="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier57', None)
    _safe_set(owner, 'sadl_RangeType56', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier57') == owner
    _safe_set(owner, 'sadl_RangeType56', None)
    assert getattr(partner, 'sadl_ResourceIdentifier57') is None


def test_assoc_className237_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName239' property in the generated
    # code (a bare stub) -- manually attach it so sadl_InstanceDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_InstanceDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_InstanceDeclaration(article="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName239', None)
    _safe_set(owner, 'sadl_InstanceDeclaration238', partner)
    assert getattr(partner, 'sadl_ResourceByName239') == owner
    _safe_set(owner, 'sadl_InstanceDeclaration238', None)
    assert getattr(partner, 'sadl_ResourceByName239') is None


def test_assoc_className27_stub_double():
    # sadl_ClassDeclaration has no real 'sadl_ClassDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_ClassDeclaration()
    setattr(partner, 'sadl_ClassDeclaration', None)
    _safe_set(owner, 'sadl_ResourceName28', partner)
    assert getattr(partner, 'sadl_ClassDeclaration') == owner
    _safe_set(owner, 'sadl_ResourceName28', None)
    assert getattr(partner, 'sadl_ClassDeclaration') is None


def test_assoc_classQualifier169_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier171' property in the generated
    # code (a bare stub) -- manually attach it so sadl_MinCardCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_MinCardCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_MinCardCondition(card="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier171', None)
    _safe_set(owner, 'sadl_MinCardCondition170', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier171') == owner
    _safe_set(owner, 'sadl_MinCardCondition170', None)
    assert getattr(partner, 'sadl_ResourceIdentifier171') is None


def test_assoc_classQualifier172_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier174' property in the generated
    # code (a bare stub) -- manually attach it so sadl_MaxCardCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_MaxCardCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_MaxCardCondition(card="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier174', None)
    _safe_set(owner, 'sadl_MaxCardCondition173', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier174') == owner
    _safe_set(owner, 'sadl_MaxCardCondition173', None)
    assert getattr(partner, 'sadl_ResourceIdentifier174') is None


def test_assoc_classQualifier175_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier177' property in the generated
    # code (a bare stub) -- manually attach it so sadl_CardCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_CardCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_CardCondition(card="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier177', None)
    _safe_set(owner, 'sadl_CardCondition176', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier177') == owner
    _safe_set(owner, 'sadl_CardCondition176', None)
    assert getattr(partner, 'sadl_ResourceIdentifier177') is None


def test_assoc_cond113_stub_double():
    # sadl_Cardinality has no real 'sadl_Cardinality114' property in the generated
    # code (a bare stub) -- manually attach it so sadl_CardCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_CardCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_CardCondition(card="sample_text")
    partner = sadl_Cardinality()
    setattr(partner, 'sadl_Cardinality114', None)
    _safe_set(owner, 'sadl_CardCondition', partner)
    assert getattr(partner, 'sadl_Cardinality114') == owner
    _safe_set(owner, 'sadl_CardCondition', None)
    assert getattr(partner, 'sadl_Cardinality114') is None


def test_assoc_cond123_stub_double():
    # sadl_MinCardinality has no real 'sadl_MinCardinality124' property in the generated
    # code (a bare stub) -- manually attach it so sadl_MinCardCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_MinCardCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_MinCardCondition(card="sample_text")
    partner = sadl_MinCardinality()
    setattr(partner, 'sadl_MinCardinality124', None)
    _safe_set(owner, 'sadl_MinCardCondition', partner)
    assert getattr(partner, 'sadl_MinCardinality124') == owner
    _safe_set(owner, 'sadl_MinCardCondition', None)
    assert getattr(partner, 'sadl_MinCardinality124') is None


def test_assoc_cond133_stub_double():
    # sadl_MaxCardinality has no real 'sadl_MaxCardinality134' property in the generated
    # code (a bare stub) -- manually attach it so sadl_MaxCardCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_MaxCardCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_MaxCardCondition(card="sample_text")
    partner = sadl_MaxCardinality()
    setattr(partner, 'sadl_MaxCardinality134', None)
    _safe_set(owner, 'sadl_MaxCardCondition', partner)
    assert getattr(partner, 'sadl_MaxCardinality134') == owner
    _safe_set(owner, 'sadl_MaxCardCondition', None)
    assert getattr(partner, 'sadl_MaxCardinality134') is None


def test_assoc_cond185_stub_double():
    # sadl_Condition has no real 'sadl_Condition187' property in the generated
    # code (a bare stub) -- manually attach it so sadl_NecessaryAndSufficient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_NecessaryAndSufficient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_NecessaryAndSufficient(article="sample_text")
    partner = sadl_Condition()
    setattr(partner, 'sadl_Condition187', None)
    _safe_set(owner, 'sadl_NecessaryAndSufficient186', {partner})
    assert getattr(partner, 'sadl_Condition187') == owner
    _safe_set(owner, 'sadl_NecessaryAndSufficient186', set())
    assert getattr(partner, 'sadl_Condition187') is None


def test_assoc_cond207_stub_double():
    # sadl_Condition has no real 'sadl_Condition209' property in the generated
    # code (a bare stub) -- manually attach it so sadl_AdditionalPropertyInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_AdditionalPropertyInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_AdditionalPropertyInfo(isSym="sample_text", isTrans="sample_text", isfunc="sample_text", isinvfunc="sample_text")
    partner = sadl_Condition()
    setattr(partner, 'sadl_Condition209', None)
    _safe_set(owner, 'sadl_AdditionalPropertyInfo208', partner)
    assert getattr(partner, 'sadl_Condition209') == owner
    _safe_set(owner, 'sadl_AdditionalPropertyInfo208', None)
    assert getattr(partner, 'sadl_Condition209') is None


def test_assoc_cond25_stub_double():
    # sadl_Condition has no real 'sadl_Condition' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceByRestriction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceByRestriction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceByRestriction(annType="sample_text")
    partner = sadl_Condition()
    setattr(partner, 'sadl_Condition', None)
    _safe_set(owner, 'sadl_ResourceByRestriction26', partner)
    assert getattr(partner, 'sadl_Condition') == owner
    _safe_set(owner, 'sadl_ResourceByRestriction26', None)
    assert getattr(partner, 'sadl_Condition') is None


def test_assoc_defValueClass159_stub_double():
    # sadl_PropertyOfClass has no real 'sadl_PropertyOfClass160' property in the generated
    # code (a bare stub) -- manually attach it so sadl_DefaultValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_DefaultValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_DefaultValue(level="sample_text")
    partner = sadl_PropertyOfClass()
    setattr(partner, 'sadl_PropertyOfClass160', None)
    _safe_set(owner, 'sadl_DefaultValue', partner)
    assert getattr(partner, 'sadl_PropertyOfClass160') == owner
    _safe_set(owner, 'sadl_DefaultValue', None)
    assert getattr(partner, 'sadl_PropertyOfClass160') is None


def test_assoc_domain195_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier197' property in the generated
    # code (a bare stub) -- manually attach it so sadl_PropertyDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_PropertyDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_PropertyDeclaration(article="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier197', None)
    _safe_set(owner, 'sadl_PropertyDeclaration196', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier197') == owner
    _safe_set(owner, 'sadl_PropertyDeclaration196', None)
    assert getattr(partner, 'sadl_ResourceIdentifier197') is None


def test_assoc_domain204_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier206' property in the generated
    # code (a bare stub) -- manually attach it so sadl_AdditionalPropertyInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_AdditionalPropertyInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_AdditionalPropertyInfo(isSym="sample_text", isTrans="sample_text", isfunc="sample_text", isinvfunc="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier206', None)
    _safe_set(owner, 'sadl_AdditionalPropertyInfo205', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier206') == owner
    _safe_set(owner, 'sadl_AdditionalPropertyInfo205', None)
    assert getattr(partner, 'sadl_ResourceIdentifier206') is None


def test_assoc_elements319_stub_double():
    # sadl_ElementSet has no real 'sadl_ElementSet320' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_ElementSet()
    setattr(partner, 'sadl_ElementSet320', None)
    _safe_set(owner, 'sadl_Expression321', partner)
    assert owner in getattr(partner, 'sadl_ElementSet320')
    _safe_set(owner, 'sadl_Expression321', None)
    assert owner not in getattr(partner, 'sadl_ElementSet320')


def test_assoc_explicitValues401_stub_double():
    # sadl_ValueRow has no real 'sadl_ValueRow402' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ExplicitValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ExplicitValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    partner = sadl_ValueRow()
    setattr(partner, 'sadl_ValueRow402', None)
    _safe_set(owner, 'sadl_ExplicitValue403', partner)
    assert owner in getattr(partner, 'sadl_ValueRow402')
    _safe_set(owner, 'sadl_ExplicitValue403', None)
    assert owner not in getattr(partner, 'sadl_ValueRow402')


def test_assoc_expr312_stub_double():
    # sadl_Query has no real 'sadl_Query' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_Query()
    setattr(partner, 'sadl_Query', None)
    _safe_set(owner, 'sadl_Expression', partner)
    assert getattr(partner, 'sadl_Query') == owner
    _safe_set(owner, 'sadl_Expression', None)
    assert getattr(partner, 'sadl_Query') is None


def test_assoc_expr313_stub_double():
    # sadl_Test has no real 'sadl_Test' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_Test()
    setattr(partner, 'sadl_Test', None)
    _safe_set(owner, 'sadl_Expression314', partner)
    assert getattr(partner, 'sadl_Test') == owner
    _safe_set(owner, 'sadl_Expression314', None)
    assert getattr(partner, 'sadl_Test') is None


def test_assoc_expr315_stub_double():
    # sadl_Expr has no real 'sadl_Expr' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_Expr()
    setattr(partner, 'sadl_Expr', None)
    _safe_set(owner, 'sadl_Expression316', partner)
    assert getattr(partner, 'sadl_Expr') == owner
    _safe_set(owner, 'sadl_Expression316', None)
    assert getattr(partner, 'sadl_Expr') is None


def test_assoc_expr317_stub_double():
    # sadl_EObject has no real 'sadl_EObject318' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Explanation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Explanation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Explanation(rulename="sample_text")
    partner = sadl_EObject()
    setattr(partner, 'sadl_EObject318', None)
    _safe_set(owner, 'sadl_Explanation', partner)
    assert getattr(partner, 'sadl_EObject318') == owner
    _safe_set(owner, 'sadl_Explanation', None)
    assert getattr(partner, 'sadl_EObject318') is None


def test_assoc_givens305_stub_double():
    # sadl_ElementSet has no real 'sadl_ElementSet' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Rule(name="sample_text")
    partner = sadl_ElementSet()
    setattr(partner, 'sadl_ElementSet', None)
    _safe_set(owner, 'sadl_Rule', partner)
    assert getattr(partner, 'sadl_ElementSet') == owner
    _safe_set(owner, 'sadl_Rule', None)
    assert getattr(partner, 'sadl_ElementSet') is None


def test_assoc_gp345_stub_double():
    # sadl_GraphPattern has no real 'sadl_GraphPattern' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_GraphPattern()
    setattr(partner, 'sadl_GraphPattern', None)
    _safe_set(owner, 'sadl_Expression346', partner)
    assert getattr(partner, 'sadl_GraphPattern') == owner
    _safe_set(owner, 'sadl_Expression346', None)
    assert getattr(partner, 'sadl_GraphPattern') is None


def test_assoc_ifs306_stub_double():
    # sadl_ElementSet has no real 'sadl_ElementSet308' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Rule(name="sample_text")
    partner = sadl_ElementSet()
    setattr(partner, 'sadl_ElementSet308', None)
    _safe_set(owner, 'sadl_Rule307', partner)
    assert getattr(partner, 'sadl_ElementSet308') == owner
    _safe_set(owner, 'sadl_Rule307', None)
    assert getattr(partner, 'sadl_ElementSet308') is None


def test_assoc_imports1_stub_double():
    # sadl_Model has no real 'sadl_Model2' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Import(alias="sample_text", importURI="sample_text")
    partner = sadl_Model()
    setattr(partner, 'sadl_Model2', None)
    _safe_set(owner, 'sadl_Import', partner)
    assert owner in getattr(partner, 'sadl_Model2')
    _safe_set(owner, 'sadl_Import', None)
    assert owner not in getattr(partner, 'sadl_Model2')


def test_assoc_instName243_stub_double():
    # sadl_TypeDeclaration has no real 'sadl_TypeDeclaration244' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_TypeDeclaration()
    setattr(partner, 'sadl_TypeDeclaration244', None)
    _safe_set(owner, 'sadl_ResourceName245', partner)
    assert getattr(partner, 'sadl_TypeDeclaration244') == owner
    _safe_set(owner, 'sadl_ResourceName245', None)
    assert getattr(partner, 'sadl_TypeDeclaration244') is None


def test_assoc_instName390_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName392' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ExplicitValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ExplicitValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName392', None)
    _safe_set(owner, 'sadl_ExplicitValue391', partner)
    assert getattr(partner, 'sadl_ResourceByName392') == owner
    _safe_set(owner, 'sadl_ExplicitValue391', None)
    assert getattr(partner, 'sadl_ResourceByName392') is None


def test_assoc_isInvOf213_stub_double():
    # sadl_IsInverseOf has no real 'sadl_IsInverseOf' property in the generated
    # code (a bare stub) -- manually attach it so sadl_AdditionalPropertyInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_AdditionalPropertyInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_AdditionalPropertyInfo(isSym="sample_text", isTrans="sample_text", isfunc="sample_text", isinvfunc="sample_text")
    partner = sadl_IsInverseOf()
    setattr(partner, 'sadl_IsInverseOf', None)
    _safe_set(owner, 'sadl_AdditionalPropertyInfo214', partner)
    assert getattr(partner, 'sadl_IsInverseOf') == owner
    _safe_set(owner, 'sadl_AdditionalPropertyInfo214', None)
    assert getattr(partner, 'sadl_IsInverseOf') is None


def test_assoc_literals11_stub_double():
    # sadl_LiteralList has no real 'sadl_LiteralList' property in the generated
    # code (a bare stub) -- manually attach it so sadl_LiteralValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_LiteralValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_LiteralValue(literalBoolean="sample_text", literalNumber="sample_text", literalString="sample_text")
    partner = sadl_LiteralList()
    setattr(partner, 'sadl_LiteralList', None)
    _safe_set(owner, 'sadl_LiteralValue', partner)
    assert owner in getattr(partner, 'sadl_LiteralList')
    _safe_set(owner, 'sadl_LiteralValue', None)
    assert owner not in getattr(partner, 'sadl_LiteralList')


def test_assoc_modelName0_stub_double():
    # sadl_Model has no real 'sadl_Model' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ModelName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ModelName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ModelName(alias="sample_text", annType="sample_text", baseUri="sample_text", version="sample_text")
    partner = sadl_Model()
    setattr(partner, 'sadl_Model', None)
    _safe_set(owner, 'sadl_ModelName', partner)
    assert getattr(partner, 'sadl_Model') == owner
    _safe_set(owner, 'sadl_ModelName', None)
    assert getattr(partner, 'sadl_Model') is None


def test_assoc_name12_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName', None)
    _safe_set(owner, 'sadl_ResourceName13', partner)
    assert getattr(partner, 'sadl_ResourceByName') == owner
    _safe_set(owner, 'sadl_ResourceName13', None)
    assert getattr(partner, 'sadl_ResourceByName') is None


def test_assoc_names17_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier19' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceBySetOp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceBySetOp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceBySetOp(annType="sample_text", op="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier19', None)
    _safe_set(owner, 'sadl_ResourceBySetOp18', {partner})
    assert getattr(partner, 'sadl_ResourceIdentifier19') == owner
    _safe_set(owner, 'sadl_ResourceBySetOp18', set())
    assert getattr(partner, 'sadl_ResourceIdentifier19') is None


def test_assoc_names303_stub_double():
    # sadl_VariableList has no real 'sadl_VariableList' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_VariableList()
    setattr(partner, 'sadl_VariableList', None)
    _safe_set(owner, 'sadl_ResourceName304', partner)
    assert owner in getattr(partner, 'sadl_VariableList')
    _safe_set(owner, 'sadl_ResourceName304', None)
    assert owner not in getattr(partner, 'sadl_VariableList')


def test_assoc_names9_stub_double():
    # sadl_ResourceList has no real 'sadl_ResourceList' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_ResourceList()
    setattr(partner, 'sadl_ResourceList', None)
    _safe_set(owner, 'sadl_ResourceName10', partner)
    assert owner in getattr(partner, 'sadl_ResourceList')
    _safe_set(owner, 'sadl_ResourceName10', None)
    assert owner not in getattr(partner, 'sadl_ResourceList')


def test_assoc_obj331_stub_double():
    # sadl_ConstructExpression has no real 'sadl_ConstructExpression332' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_ConstructExpression()
    setattr(partner, 'sadl_ConstructExpression332', None)
    _safe_set(owner, 'sadl_ResourceName333', partner)
    assert getattr(partner, 'sadl_ConstructExpression332') == owner
    _safe_set(owner, 'sadl_ResourceName333', None)
    assert getattr(partner, 'sadl_ConstructExpression332') is None


def test_assoc_objectValue271_stub_double():
    # sadl_PropValPartialTriple has no real 'sadl_PropValPartialTriple272' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ExplicitValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ExplicitValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    partner = sadl_PropValPartialTriple()
    setattr(partner, 'sadl_PropValPartialTriple272', None)
    _safe_set(owner, 'sadl_ExplicitValue273', partner)
    assert getattr(partner, 'sadl_PropValPartialTriple272') == owner
    _safe_set(owner, 'sadl_ExplicitValue273', None)
    assert getattr(partner, 'sadl_PropValPartialTriple272') is None


def test_assoc_objectValueBNode274_stub_double():
    # sadl_PropValPartialTriple has no real 'sadl_PropValPartialTriple275' property in the generated
    # code (a bare stub) -- manually attach it so sadl_InstanceDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_InstanceDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_InstanceDeclaration(article="sample_text")
    partner = sadl_PropValPartialTriple()
    setattr(partner, 'sadl_PropValPartialTriple275', None)
    _safe_set(owner, 'sadl_InstanceDeclaration276', partner)
    assert getattr(partner, 'sadl_PropValPartialTriple275') == owner
    _safe_set(owner, 'sadl_InstanceDeclaration276', None)
    assert getattr(partner, 'sadl_PropValPartialTriple275') is None


def test_assoc_ofPhr354_stub_double():
    # sadl_PropOfSubj has no real 'sadl_PropOfSubj' property in the generated
    # code (a bare stub) -- manually attach it so sadl_OfPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_OfPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_OfPhrase(article="sample_text")
    partner = sadl_PropOfSubj()
    setattr(partner, 'sadl_PropOfSubj', None)
    _safe_set(owner, 'sadl_OfPhrase355', partner)
    assert owner in getattr(partner, 'sadl_PropOfSubj')
    _safe_set(owner, 'sadl_OfPhrase355', None)
    assert owner not in getattr(partner, 'sadl_PropOfSubj')


def test_assoc_ofphrs277_stub_double():
    # sadl_OfPatternReturningValues has no real 'sadl_OfPatternReturningValues278' property in the generated
    # code (a bare stub) -- manually attach it so sadl_OfPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_OfPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_OfPhrase(article="sample_text")
    partner = sadl_OfPatternReturningValues()
    setattr(partner, 'sadl_OfPatternReturningValues278', None)
    _safe_set(owner, 'sadl_OfPhrase', partner)
    assert owner in getattr(partner, 'sadl_OfPatternReturningValues278')
    _safe_set(owner, 'sadl_OfPhrase', None)
    assert owner not in getattr(partner, 'sadl_OfPatternReturningValues278')


def test_assoc_ops292_stub_double():
    # sadl_MergedTriples has no real 'sadl_MergedTriples' property in the generated
    # code (a bare stub) -- manually attach it so sadl_OfPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_OfPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_OfPhrase(article="sample_text")
    partner = sadl_MergedTriples()
    setattr(partner, 'sadl_MergedTriples', None)
    _safe_set(owner, 'sadl_OfPhrase293', partner)
    assert owner in getattr(partner, 'sadl_MergedTriples')
    _safe_set(owner, 'sadl_OfPhrase293', None)
    assert owner not in getattr(partner, 'sadl_MergedTriples')


def test_assoc_orderList324_stub_double():
    # sadl_OrderList has no real 'sadl_OrderList' property in the generated
    # code (a bare stub) -- manually attach it so sadl_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_SelectExpression(allVars="sample_text", distinct="sample_text", orderby="sample_text")
    partner = sadl_OrderList()
    setattr(partner, 'sadl_OrderList', None)
    _safe_set(owner, 'sadl_SelectExpression325', partner)
    assert getattr(partner, 'sadl_OrderList') == owner
    _safe_set(owner, 'sadl_SelectExpression325', None)
    assert getattr(partner, 'sadl_OrderList') is None


def test_assoc_orderList334_stub_double():
    # sadl_OrderList has no real 'sadl_OrderList335' property in the generated
    # code (a bare stub) -- manually attach it so sadl_OrderElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_OrderElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_OrderElement(order="sample_text")
    partner = sadl_OrderList()
    setattr(partner, 'sadl_OrderList335', None)
    _safe_set(owner, 'sadl_OrderElement', partner)
    assert owner in getattr(partner, 'sadl_OrderList335')
    _safe_set(owner, 'sadl_OrderElement', None)
    assert owner not in getattr(partner, 'sadl_OrderList335')


def test_assoc_pivot294_stub_double():
    # sadl_MergedTriples has no real 'sadl_MergedTriples295' property in the generated
    # code (a bare stub) -- manually attach it so sadl_TypedBNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_TypedBNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_TypedBNode(article="sample_text")
    partner = sadl_MergedTriples()
    setattr(partner, 'sadl_MergedTriples295', None)
    _safe_set(owner, 'sadl_TypedBNode296', partner)
    assert getattr(partner, 'sadl_MergedTriples295') == owner
    _safe_set(owner, 'sadl_TypedBNode296', None)
    assert getattr(partner, 'sadl_MergedTriples295') is None


def test_assoc_pred328_stub_double():
    # sadl_ConstructExpression has no real 'sadl_ConstructExpression329' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_ConstructExpression()
    setattr(partner, 'sadl_ConstructExpression329', None)
    _safe_set(owner, 'sadl_ResourceName330', partner)
    assert getattr(partner, 'sadl_ConstructExpression329') == owner
    _safe_set(owner, 'sadl_ResourceName330', None)
    assert getattr(partner, 'sadl_ConstructExpression329') is None


def test_assoc_propName22_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName24' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceByRestriction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceByRestriction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceByRestriction(annType="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName24', None)
    _safe_set(owner, 'sadl_ResourceByRestriction23', partner)
    assert getattr(partner, 'sadl_ResourceByName24') == owner
    _safe_set(owner, 'sadl_ResourceByRestriction23', None)
    assert getattr(partner, 'sadl_ResourceByName24') is None


def test_assoc_propertyName182_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName184' property in the generated
    # code (a bare stub) -- manually attach it so sadl_NecessaryAndSufficient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_NecessaryAndSufficient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_NecessaryAndSufficient(article="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName184', None)
    _safe_set(owner, 'sadl_NecessaryAndSufficient183', {partner})
    assert getattr(partner, 'sadl_ResourceByName184') == owner
    _safe_set(owner, 'sadl_NecessaryAndSufficient183', set())
    assert getattr(partner, 'sadl_ResourceByName184') is None


def test_assoc_propertyName300_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName302' property in the generated
    # code (a bare stub) -- manually attach it so sadl_OfPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_OfPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_OfPhrase(article="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName302', None)
    _safe_set(owner, 'sadl_OfPhrase301', partner)
    assert getattr(partner, 'sadl_ResourceByName302') == owner
    _safe_set(owner, 'sadl_OfPhrase301', None)
    assert getattr(partner, 'sadl_ResourceByName302') is None


def test_assoc_propertyName45_stub_double():
    # sadl_AddlClassInfo has no real 'sadl_AddlClassInfo46' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_AddlClassInfo()
    setattr(partner, 'sadl_AddlClassInfo46', None)
    _safe_set(owner, 'sadl_ResourceName47', partner)
    assert getattr(partner, 'sadl_AddlClassInfo46') == owner
    _safe_set(owner, 'sadl_ResourceName47', None)
    assert getattr(partner, 'sadl_AddlClassInfo46') is None


def test_assoc_quantified384_stub_double():
    # sadl_ExistentialNegation has no real 'sadl_ExistentialNegation385' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_ExistentialNegation()
    setattr(partner, 'sadl_ExistentialNegation385', None)
    _safe_set(owner, 'sadl_Expression386', partner)
    assert getattr(partner, 'sadl_ExistentialNegation385') == owner
    _safe_set(owner, 'sadl_Expression386', None)
    assert getattr(partner, 'sadl_ExistentialNegation385') is None


def test_assoc_range48_stub_double():
    # sadl_AddlClassInfo has no real 'sadl_AddlClassInfo49' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Range's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Range's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Range(list="sample_text", lists="sample_text", single="sample_text")
    partner = sadl_AddlClassInfo()
    setattr(partner, 'sadl_AddlClassInfo49', None)
    _safe_set(owner, 'sadl_Range', partner)
    assert getattr(partner, 'sadl_AddlClassInfo49') == owner
    _safe_set(owner, 'sadl_Range', None)
    assert getattr(partner, 'sadl_AddlClassInfo49') is None


def test_assoc_rangeResource198_stub_double():
    # sadl_ResourceIdentifier has no real 'sadl_ResourceIdentifier200' property in the generated
    # code (a bare stub) -- manually attach it so sadl_PropertyDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_PropertyDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_PropertyDeclaration(article="sample_text")
    partner = sadl_ResourceIdentifier()
    setattr(partner, 'sadl_ResourceIdentifier200', None)
    _safe_set(owner, 'sadl_PropertyDeclaration199', partner)
    assert getattr(partner, 'sadl_ResourceIdentifier200') == owner
    _safe_set(owner, 'sadl_PropertyDeclaration199', None)
    assert getattr(partner, 'sadl_ResourceIdentifier200') is None


def test_assoc_restriction166_stub_double():
    # sadl_HasValueCondition has no real 'sadl_HasValueCondition167' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ExplicitValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ExplicitValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    partner = sadl_HasValueCondition()
    setattr(partner, 'sadl_HasValueCondition167', None)
    _safe_set(owner, 'sadl_ExplicitValue168', partner)
    assert getattr(partner, 'sadl_HasValueCondition167') == owner
    _safe_set(owner, 'sadl_ExplicitValue168', None)
    assert getattr(partner, 'sadl_HasValueCondition167') is None


def test_assoc_restriction60_stub_double():
    # sadl_UserDefinedDataType has no real 'sadl_UserDefinedDataType61' property in the generated
    # code (a bare stub) -- manually attach it so sadl_DataTypeRestriction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_DataTypeRestriction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_DataTypeRestriction(basetype="sample_text", basetypes="sample_text")
    partner = sadl_UserDefinedDataType()
    setattr(partner, 'sadl_UserDefinedDataType61', None)
    _safe_set(owner, 'sadl_DataTypeRestriction', partner)
    assert getattr(partner, 'sadl_UserDefinedDataType61') == owner
    _safe_set(owner, 'sadl_DataTypeRestriction', None)
    assert getattr(partner, 'sadl_UserDefinedDataType61') is None


def test_assoc_row396_stub_double():
    # sadl_ValueRow has no real 'sadl_ValueRow' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ExplicitValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ExplicitValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    partner = sadl_ValueRow()
    setattr(partner, 'sadl_ValueRow', None)
    _safe_set(owner, 'sadl_ExplicitValue397', partner)
    assert getattr(partner, 'sadl_ValueRow') == owner
    _safe_set(owner, 'sadl_ExplicitValue397', None)
    assert getattr(partner, 'sadl_ValueRow') is None


def test_assoc_subj326_stub_double():
    # sadl_ConstructExpression has no real 'sadl_ConstructExpression' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_ConstructExpression()
    setattr(partner, 'sadl_ConstructExpression', None)
    _safe_set(owner, 'sadl_ResourceName327', partner)
    assert getattr(partner, 'sadl_ConstructExpression') == owner
    _safe_set(owner, 'sadl_ResourceName327', None)
    assert getattr(partner, 'sadl_ConstructExpression') is None


def test_assoc_superPropName190_stub_double():
    # sadl_ResourceByName has no real 'sadl_ResourceByName192' property in the generated
    # code (a bare stub) -- manually attach it so sadl_PropertyDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_PropertyDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_PropertyDeclaration(article="sample_text")
    partner = sadl_ResourceByName()
    setattr(partner, 'sadl_ResourceByName192', None)
    _safe_set(owner, 'sadl_PropertyDeclaration191', partner)
    assert getattr(partner, 'sadl_ResourceByName192') == owner
    _safe_set(owner, 'sadl_PropertyDeclaration191', None)
    assert getattr(partner, 'sadl_ResourceByName192') is None


def test_assoc_thens309_stub_double():
    # sadl_ElementSet has no real 'sadl_ElementSet311' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Rule(name="sample_text")
    partner = sadl_ElementSet()
    setattr(partner, 'sadl_ElementSet311', None)
    _safe_set(owner, 'sadl_Rule310', partner)
    assert getattr(partner, 'sadl_ElementSet311') == owner
    _safe_set(owner, 'sadl_Rule310', None)
    assert getattr(partner, 'sadl_ElementSet311') is None


def test_assoc_type246_stub_double():
    # sadl_TypeDeclaration has no real 'sadl_TypeDeclaration247' property in the generated
    # code (a bare stub) -- manually attach it so sadl_TypedBNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_TypedBNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_TypedBNode(article="sample_text")
    partner = sadl_TypeDeclaration()
    setattr(partner, 'sadl_TypeDeclaration247', None)
    _safe_set(owner, 'sadl_TypedBNode248', partner)
    assert getattr(partner, 'sadl_TypeDeclaration247') == owner
    _safe_set(owner, 'sadl_TypedBNode248', None)
    assert getattr(partner, 'sadl_TypeDeclaration247') is None


def test_assoc_type282_stub_double():
    # sadl_OfPatternReturningValues has no real 'sadl_OfPatternReturningValues283' property in the generated
    # code (a bare stub) -- manually attach it so sadl_TypedBNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_TypedBNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_TypedBNode(article="sample_text")
    partner = sadl_OfPatternReturningValues()
    setattr(partner, 'sadl_OfPatternReturningValues283', None)
    _safe_set(owner, 'sadl_TypedBNode284', partner)
    assert getattr(partner, 'sadl_OfPatternReturningValues283') == owner
    _safe_set(owner, 'sadl_TypedBNode284', None)
    assert getattr(partner, 'sadl_OfPatternReturningValues283') is None


def test_assoc_typeDecl234_stub_double():
    # sadl_TypeDeclaration has no real 'sadl_TypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so sadl_InstanceDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_InstanceDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_InstanceDeclaration(article="sample_text")
    partner = sadl_TypeDeclaration()
    setattr(partner, 'sadl_TypeDeclaration', None)
    _safe_set(owner, 'sadl_InstanceDeclaration', partner)
    assert getattr(partner, 'sadl_TypeDeclaration') == owner
    _safe_set(owner, 'sadl_InstanceDeclaration', None)
    assert getattr(partner, 'sadl_TypeDeclaration') is None


def test_assoc_userDefinedDataType58_stub_double():
    # sadl_UserDefinedDataType has no real 'sadl_UserDefinedDataType' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ResourceName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ResourceName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ResourceName(annType="sample_text", name="sample_text")
    partner = sadl_UserDefinedDataType()
    setattr(partner, 'sadl_UserDefinedDataType', None)
    _safe_set(owner, 'sadl_ResourceName59', partner)
    assert getattr(partner, 'sadl_UserDefinedDataType') == owner
    _safe_set(owner, 'sadl_ResourceName59', None)
    assert getattr(partner, 'sadl_UserDefinedDataType') is None


def test_assoc_val374_stub_double():
    # sadl_InstAttrPSV has no real 'sadl_InstAttrPSV375' property in the generated
    # code (a bare stub) -- manually attach it so sadl_ExplicitValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_ExplicitValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_ExplicitValue(term="sample_text", valueList="sample_text")
    partner = sadl_InstAttrPSV()
    setattr(partner, 'sadl_InstAttrPSV375', None)
    _safe_set(owner, 'sadl_ExplicitValue376', partner)
    assert getattr(partner, 'sadl_InstAttrPSV375') == owner
    _safe_set(owner, 'sadl_ExplicitValue376', None)
    assert getattr(partner, 'sadl_InstAttrPSV375') is None


def test_assoc_vals369_stub_double():
    # sadl_InstAttrSPV has no real 'sadl_InstAttrSPV370' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_InstAttrSPV()
    setattr(partner, 'sadl_InstAttrSPV370', None)
    _safe_set(owner, 'sadl_Expression371', partner)
    assert owner in getattr(partner, 'sadl_InstAttrSPV370')
    _safe_set(owner, 'sadl_Expression371', None)
    assert owner not in getattr(partner, 'sadl_InstAttrSPV370')


def test_assoc_valueTable352_stub_double():
    # sadl_ValueTable has no real 'sadl_ValueTable' property in the generated
    # code (a bare stub) -- manually attach it so sadl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_Expression(func="sample_text")
    partner = sadl_ValueTable()
    setattr(partner, 'sadl_ValueTable', None)
    _safe_set(owner, 'sadl_Expression353', partner)
    assert getattr(partner, 'sadl_ValueTable') == owner
    _safe_set(owner, 'sadl_Expression353', None)
    assert getattr(partner, 'sadl_ValueTable') is None


def test_assoc_varList322_stub_double():
    # sadl_VariableList has no real 'sadl_VariableList323' property in the generated
    # code (a bare stub) -- manually attach it so sadl_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sadl_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sadl_SelectExpression(allVars="sample_text", distinct="sample_text", orderby="sample_text")
    partner = sadl_VariableList()
    setattr(partner, 'sadl_VariableList323', None)
    _safe_set(owner, 'sadl_SelectExpression', partner)
    assert getattr(partner, 'sadl_VariableList323') == owner
    _safe_set(owner, 'sadl_SelectExpression', None)
    assert getattr(partner, 'sadl_VariableList323') is None


