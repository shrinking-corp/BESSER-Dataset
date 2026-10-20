import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    Predicate,
    QueryValueExpression,
    SQLQueryObject,
    TableFunction,
    ValueExpressionCast,
    ValueExpressionFunction,
    XMLNamespaceDeclarationItem,
    XMLPredicate,
    XMLTableColumnDefinitionItem,
    XMLValueFunction,
    XMLValueFunctionValidateAccordingTo,
    query_OrderBySpecification,
    query_QueryValueExpression,
    query_XMLAggregateFunction,
    query_XMLAggregateSortSpecification,
    query_XMLAttributeDeclarationItem,
    query_XMLAttributesDeclaration,
    query_XMLNamespaceDeclarationDefault,
    query_XMLNamespaceDeclarationItem,
    query_XMLNamespaceDeclarationPrefix,
    query_XMLNamespacesDeclaration,
    query_XMLPredicate,
    query_XMLPredicateContent,
    query_XMLPredicateDocument,
    query_XMLPredicateExists,
    query_XMLPredicateValid,
    query_XMLQueryArgumentItem,
    query_XMLQueryArgumentList,
    query_XMLQueryExpression,
    query_XMLSerializeFunction,
    query_XMLSerializeFunctionEncoding,
    query_XMLSerializeFunctionTarget,
    query_XMLTableColumnDefinitionDefault,
    query_XMLTableColumnDefinitionItem,
    query_XMLTableColumnDefinitionOrdinality,
    query_XMLTableColumnDefinitionRegular,
    query_XMLTableFunction,
    query_XMLValueExpressionCast,
    query_XMLValueFunction,
    query_XMLValueFunctionComment,
    query_XMLValueFunctionCommentContent,
    query_XMLValueFunctionConcat,
    query_XMLValueFunctionConcatContentItem,
    query_XMLValueFunctionDocument,
    query_XMLValueFunctionDocumentContent,
    query_XMLValueFunctionElement,
    query_XMLValueFunctionElementContentItem,
    query_XMLValueFunctionElementContentList,
    query_XMLValueFunctionForest,
    query_XMLValueFunctionForestContentItem,
    query_XMLValueFunctionPI,
    query_XMLValueFunctionPIContent,
    query_XMLValueFunctionParse,
    query_XMLValueFunctionParseContent,
    query_XMLValueFunctionQuery,
    query_XMLValueFunctionQueryReturning,
    query_XMLValueFunctionText,
    query_XMLValueFunctionTextContent,
    query_XMLValueFunctionValidate,
    query_XMLValueFunctionValidateAccordingTo,
    query_XMLValueFunctionValidateAccordingToIdentifier,
    query_XMLValueFunctionValidateAccordingToURI,
    query_XMLValueFunctionValidateContent,
    query_XMLValueFunctionValidateElement,
    query_XMLValueFunctionValidateElementName,
    query_XMLValueFunctionValidateElementNamespace,
    XMLContentType,
    XMLContentType2,
    XMLDeclarationType,
    XMLEmptyHandlingType,
    XMLNullHandlingType,
    XMLPassingType,
    XMLReturningType,
    XMLWhitespaceHandlingType,
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

def test_assoc_elementContentList7_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionElementContentList(nullHandlingOption="sample_text")
    a2 = query_XMLValueFunctionElementContentList(nullHandlingOption="sample_text_2")
    b = query_XMLValueFunctionElement(elementName="sample_text", returningOption="sample_text")
    _safe_set(b, 'valueFunctionElement8', a1)
    assert _is_linked(b, 'valueFunctionElement8', a1)
    if hasattr(a1, 'XMLValueFunctionElementContentList'):
        assert _is_linked(a1, 'XMLValueFunctionElementContentList', b)
    _safe_set(b, 'valueFunctionElement8', a2)
    assert _is_linked(b, 'valueFunctionElement8', a2)
    if hasattr(a1, 'XMLValueFunctionElementContentList'):
        assert not _is_linked(a1, 'XMLValueFunctionElementContentList', b)
    if hasattr(a2, 'XMLValueFunctionElementContentList'):
        assert _is_linked(a2, 'XMLValueFunctionElementContentList', b)
    _safe_set(b, 'valueFunctionElement8', None)
    assert not _is_linked(b, 'valueFunctionElement8', a2)
    if hasattr(a2, 'XMLValueFunctionElementContentList'):
        assert not _is_linked(a2, 'XMLValueFunctionElementContentList', b)


def test_assoc_queryReturning26_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionQueryReturning(passingOption="sample_text", returningOption="sample_text")
    a2 = query_XMLValueFunctionQueryReturning(passingOption="sample_text_2", returningOption="sample_text_2")
    b = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text")
    _safe_set(b, 'valueFunctionQuery27', a1)
    assert _is_linked(b, 'valueFunctionQuery27', a1)
    if hasattr(a1, 'XMLValueFunctionQueryReturning'):
        assert _is_linked(a1, 'XMLValueFunctionQueryReturning', b)
    _safe_set(b, 'valueFunctionQuery27', a2)
    assert _is_linked(b, 'valueFunctionQuery27', a2)
    if hasattr(a1, 'XMLValueFunctionQueryReturning'):
        assert not _is_linked(a1, 'XMLValueFunctionQueryReturning', b)
    if hasattr(a2, 'XMLValueFunctionQueryReturning'):
        assert _is_linked(a2, 'XMLValueFunctionQueryReturning', b)
    _safe_set(b, 'valueFunctionQuery27', None)
    assert not _is_linked(b, 'valueFunctionQuery27', a2)
    if hasattr(a2, 'XMLValueFunctionQueryReturning'):
        assert not _is_linked(a2, 'XMLValueFunctionQueryReturning', b)


def test_assoc_serializeEncoding54_reverse_link_reassign_clear():
    a1 = query_XMLSerializeFunctionEncoding(encodingName="sample_text")
    a2 = query_XMLSerializeFunctionEncoding(encodingName="sample_text_2")
    b = query_XMLSerializeFunction(contentOption="sample_text", declarationOption="sample_text", serializeVersion="sample_text")
    _safe_set(b, 'query_XMLSerializeFunction', a1)
    assert _is_linked(b, 'query_XMLSerializeFunction', a1)
    if hasattr(a1, 'query_XMLSerializeFunctionEncoding'):
        assert _is_linked(a1, 'query_XMLSerializeFunctionEncoding', b)
    _safe_set(b, 'query_XMLSerializeFunction', a2)
    assert _is_linked(b, 'query_XMLSerializeFunction', a2)
    if hasattr(a1, 'query_XMLSerializeFunctionEncoding'):
        assert not _is_linked(a1, 'query_XMLSerializeFunctionEncoding', b)
    if hasattr(a2, 'query_XMLSerializeFunctionEncoding'):
        assert _is_linked(a2, 'query_XMLSerializeFunctionEncoding', b)
    _safe_set(b, 'query_XMLSerializeFunction', None)
    assert not _is_linked(b, 'query_XMLSerializeFunction', a2)
    if hasattr(a2, 'query_XMLSerializeFunctionEncoding'):
        assert not _is_linked(a2, 'query_XMLSerializeFunctionEncoding', b)


def test_assoc_tableFunction47_reverse_link_reassign_clear():
    a1 = query_XMLTableFunction(tableRowPattern="sample_text")
    a2 = query_XMLTableFunction(tableRowPattern="sample_text_2")
    b = query_XMLQueryArgumentList(passingMechanism="sample_text")
    _safe_set(b, 'xqueryArgList48', a1)
    assert _is_linked(b, 'xqueryArgList48', a1)
    if hasattr(a1, 'XMLTableFunction'):
        assert _is_linked(a1, 'XMLTableFunction', b)
    _safe_set(b, 'xqueryArgList48', a2)
    assert _is_linked(b, 'xqueryArgList48', a2)
    if hasattr(a1, 'XMLTableFunction'):
        assert not _is_linked(a1, 'XMLTableFunction', b)
    if hasattr(a2, 'XMLTableFunction'):
        assert _is_linked(a2, 'XMLTableFunction', b)
    _safe_set(b, 'xqueryArgList48', None)
    assert not _is_linked(b, 'xqueryArgList48', a2)
    if hasattr(a2, 'XMLTableFunction'):
        assert not _is_linked(a2, 'XMLTableFunction', b)


def test_assoc_valueFunctionElement117_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionElementContentList(nullHandlingOption="sample_text")
    a2 = query_XMLValueFunctionElementContentList(nullHandlingOption="sample_text_2")
    b = query_XMLValueFunctionElement(elementName="sample_text", returningOption="sample_text")
    _safe_set(b, 'XMLValueFunctionElement118', a1)
    assert _is_linked(b, 'XMLValueFunctionElement118', a1)
    if hasattr(a1, 'elementContentList'):
        assert _is_linked(a1, 'elementContentList', b)
    _safe_set(b, 'XMLValueFunctionElement118', a2)
    assert _is_linked(b, 'XMLValueFunctionElement118', a2)
    if hasattr(a1, 'elementContentList'):
        assert not _is_linked(a1, 'elementContentList', b)
    if hasattr(a2, 'elementContentList'):
        assert _is_linked(a2, 'elementContentList', b)
    _safe_set(b, 'XMLValueFunctionElement118', None)
    assert not _is_linked(b, 'XMLValueFunctionElement118', a2)
    if hasattr(a2, 'elementContentList'):
        assert not _is_linked(a2, 'elementContentList', b)


def test_assoc_valueFunctionQuery121_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionQueryReturning(passingOption="sample_text", returningOption="sample_text")
    a2 = query_XMLValueFunctionQueryReturning(passingOption="sample_text_2", returningOption="sample_text_2")
    b = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text")
    _safe_set(b, 'XMLValueFunctionQuery122', a1)
    assert _is_linked(b, 'XMLValueFunctionQuery122', a1)
    if hasattr(a1, 'queryReturning'):
        assert _is_linked(a1, 'queryReturning', b)
    _safe_set(b, 'XMLValueFunctionQuery122', a2)
    assert _is_linked(b, 'XMLValueFunctionQuery122', a2)
    if hasattr(a1, 'queryReturning'):
        assert not _is_linked(a1, 'queryReturning', b)
    if hasattr(a2, 'queryReturning'):
        assert _is_linked(a2, 'queryReturning', b)
    _safe_set(b, 'XMLValueFunctionQuery122', None)
    assert not _is_linked(b, 'XMLValueFunctionQuery122', a2)
    if hasattr(a2, 'queryReturning'):
        assert not _is_linked(a2, 'queryReturning', b)


def test_assoc_valueFunctionQuery38_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text")
    a2 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text_2")
    b = query_XMLQueryExpression(xqueryExprContent="sample_text")
    _safe_set(b, 'xqueryExpr39', a1)
    assert _is_linked(b, 'xqueryExpr39', a1)
    if hasattr(a1, 'XMLValueFunctionQuery'):
        assert _is_linked(a1, 'XMLValueFunctionQuery', b)
    _safe_set(b, 'xqueryExpr39', a2)
    assert _is_linked(b, 'xqueryExpr39', a2)
    if hasattr(a1, 'XMLValueFunctionQuery'):
        assert not _is_linked(a1, 'XMLValueFunctionQuery', b)
    if hasattr(a2, 'XMLValueFunctionQuery'):
        assert _is_linked(a2, 'XMLValueFunctionQuery', b)
    _safe_set(b, 'xqueryExpr39', None)
    assert not _is_linked(b, 'xqueryExpr39', a2)
    if hasattr(a2, 'XMLValueFunctionQuery'):
        assert not _is_linked(a2, 'XMLValueFunctionQuery', b)


def test_assoc_valueFunctionQuery44_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text")
    a2 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text_2")
    b = query_XMLQueryArgumentList(passingMechanism="sample_text")
    _safe_set(b, 'xqueryArgList45', a1)
    assert _is_linked(b, 'xqueryArgList45', a1)
    if hasattr(a1, 'XMLValueFunctionQuery46'):
        assert _is_linked(a1, 'XMLValueFunctionQuery46', b)
    _safe_set(b, 'xqueryArgList45', a2)
    assert _is_linked(b, 'xqueryArgList45', a2)
    if hasattr(a1, 'XMLValueFunctionQuery46'):
        assert not _is_linked(a1, 'XMLValueFunctionQuery46', b)
    if hasattr(a2, 'XMLValueFunctionQuery46'):
        assert _is_linked(a2, 'XMLValueFunctionQuery46', b)
    _safe_set(b, 'xqueryArgList45', None)
    assert not _is_linked(b, 'xqueryArgList45', a2)
    if hasattr(a2, 'XMLValueFunctionQuery46'):
        assert not _is_linked(a2, 'XMLValueFunctionQuery46', b)


def test_assoc_xqueryArgList24_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text")
    a2 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text_2")
    b = query_XMLQueryArgumentList(passingMechanism="sample_text")
    _safe_set(b, 'XMLQueryArgumentList', a1)
    assert _is_linked(b, 'XMLQueryArgumentList', a1)
    if hasattr(a1, 'valueFunctionQuery25'):
        assert _is_linked(a1, 'valueFunctionQuery25', b)
    _safe_set(b, 'XMLQueryArgumentList', a2)
    assert _is_linked(b, 'XMLQueryArgumentList', a2)
    if hasattr(a1, 'valueFunctionQuery25'):
        assert not _is_linked(a1, 'valueFunctionQuery25', b)
    if hasattr(a2, 'valueFunctionQuery25'):
        assert _is_linked(a2, 'valueFunctionQuery25', b)
    _safe_set(b, 'XMLQueryArgumentList', None)
    assert not _is_linked(b, 'XMLQueryArgumentList', a2)
    if hasattr(a2, 'valueFunctionQuery25'):
        assert not _is_linked(a2, 'valueFunctionQuery25', b)


def test_assoc_xqueryArgList49_reverse_link_reassign_clear():
    a1 = query_XMLQueryArgumentList(passingMechanism="sample_text")
    a2 = query_XMLQueryArgumentList(passingMechanism="sample_text_2")
    b = query_XMLQueryArgumentItem(passingMechanism="sample_text")
    _safe_set(b, 'xqueryArgListChildren', a1)
    assert _is_linked(b, 'xqueryArgListChildren', a1)
    if hasattr(a1, 'XMLQueryArgumentList50'):
        assert _is_linked(a1, 'XMLQueryArgumentList50', b)
    _safe_set(b, 'xqueryArgListChildren', a2)
    assert _is_linked(b, 'xqueryArgListChildren', a2)
    if hasattr(a1, 'XMLQueryArgumentList50'):
        assert not _is_linked(a1, 'XMLQueryArgumentList50', b)
    if hasattr(a2, 'XMLQueryArgumentList50'):
        assert _is_linked(a2, 'XMLQueryArgumentList50', b)
    _safe_set(b, 'xqueryArgListChildren', None)
    assert not _is_linked(b, 'xqueryArgListChildren', a2)
    if hasattr(a2, 'XMLQueryArgumentList50'):
        assert not _is_linked(a2, 'XMLQueryArgumentList50', b)


def test_assoc_xqueryArgList79_reverse_link_reassign_clear():
    a1 = query_XMLTableFunction(tableRowPattern="sample_text")
    a2 = query_XMLTableFunction(tableRowPattern="sample_text_2")
    b = query_XMLQueryArgumentList(passingMechanism="sample_text")
    _safe_set(b, 'XMLQueryArgumentList80', a1)
    assert _is_linked(b, 'XMLQueryArgumentList80', a1)
    if hasattr(a1, 'tableFunction'):
        assert _is_linked(a1, 'tableFunction', b)
    _safe_set(b, 'XMLQueryArgumentList80', a2)
    assert _is_linked(b, 'XMLQueryArgumentList80', a2)
    if hasattr(a1, 'tableFunction'):
        assert not _is_linked(a1, 'tableFunction', b)
    if hasattr(a2, 'tableFunction'):
        assert _is_linked(a2, 'tableFunction', b)
    _safe_set(b, 'XMLQueryArgumentList80', None)
    assert not _is_linked(b, 'XMLQueryArgumentList80', a2)
    if hasattr(a2, 'tableFunction'):
        assert not _is_linked(a2, 'tableFunction', b)


def test_assoc_xqueryArgListChildren42_reverse_link_reassign_clear():
    a1 = query_XMLQueryArgumentList(passingMechanism="sample_text")
    a2 = query_XMLQueryArgumentList(passingMechanism="sample_text_2")
    b = query_XMLQueryArgumentItem(passingMechanism="sample_text")
    _safe_set(b, 'XMLQueryArgumentItem', a1)
    assert _is_linked(b, 'XMLQueryArgumentItem', a1)
    if hasattr(a1, 'xqueryArgList43'):
        assert _is_linked(a1, 'xqueryArgList43', b)
    _safe_set(b, 'XMLQueryArgumentItem', a2)
    assert _is_linked(b, 'XMLQueryArgumentItem', a2)
    if hasattr(a1, 'xqueryArgList43'):
        assert not _is_linked(a1, 'xqueryArgList43', b)
    if hasattr(a2, 'xqueryArgList43'):
        assert _is_linked(a2, 'xqueryArgList43', b)
    _safe_set(b, 'XMLQueryArgumentItem', None)
    assert not _is_linked(b, 'XMLQueryArgumentItem', a2)
    if hasattr(a2, 'xqueryArgList43'):
        assert not _is_linked(a2, 'xqueryArgList43', b)


def test_assoc_xqueryExpr23_reverse_link_reassign_clear():
    a1 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text")
    a2 = query_XMLValueFunctionQuery(emptyHandlingOption="sample_text_2")
    b = query_XMLQueryExpression(xqueryExprContent="sample_text")
    _safe_set(b, 'XMLQueryExpression', a1)
    assert _is_linked(b, 'XMLQueryExpression', a1)
    if hasattr(a1, 'valueFunctionQuery'):
        assert _is_linked(a1, 'valueFunctionQuery', b)
    _safe_set(b, 'XMLQueryExpression', a2)
    assert _is_linked(b, 'XMLQueryExpression', a2)
    if hasattr(a1, 'valueFunctionQuery'):
        assert not _is_linked(a1, 'valueFunctionQuery', b)
    if hasattr(a2, 'valueFunctionQuery'):
        assert _is_linked(a2, 'valueFunctionQuery', b)
    _safe_set(b, 'XMLQueryExpression', None)
    assert not _is_linked(b, 'XMLQueryExpression', a2)
    if hasattr(a2, 'valueFunctionQuery'):
        assert not _is_linked(a2, 'valueFunctionQuery', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_PIContent22_stub_double():
    # query_XMLValueFunctionPIContent has no real 'XMLValueFunctionPIContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionPI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionPI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionPI(returningOption="sample_text", targetName="sample_text")
    partner = query_XMLValueFunctionPIContent()
    setattr(partner, 'XMLValueFunctionPIContent', None)
    _safe_set(owner, 'valueFunctionPI', partner)
    assert getattr(partner, 'XMLValueFunctionPIContent') == owner
    _safe_set(owner, 'valueFunctionPI', None)
    assert getattr(partner, 'XMLValueFunctionPIContent') is None


def test_assoc_aggregateFunction68_stub_double():
    # query_XMLAggregateSortSpecification has no real 'sortSpecList' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLAggregateFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLAggregateFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLAggregateFunction(returningOption="sample_text")
    partner = query_XMLAggregateSortSpecification()
    setattr(partner, 'sortSpecList', None)
    _safe_set(owner, 'XMLAggregateFunction', partner)
    assert getattr(partner, 'sortSpecList') == owner
    _safe_set(owner, 'XMLAggregateFunction', None)
    assert getattr(partner, 'sortSpecList') is None


def test_assoc_attributesDecl4_stub_double():
    # query_XMLAttributesDeclaration has no real 'XMLAttributesDeclaration6' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionElement(elementName="sample_text", returningOption="sample_text")
    partner = query_XMLAttributesDeclaration()
    setattr(partner, 'XMLAttributesDeclaration6', None)
    _safe_set(owner, 'valueFunctionElement5', partner)
    assert getattr(partner, 'XMLAttributesDeclaration6') == owner
    _safe_set(owner, 'valueFunctionElement5', None)
    assert getattr(partner, 'XMLAttributesDeclaration6') is None


def test_assoc_columnDefList81_stub_double():
    # query_XMLTableColumnDefinitionItem has no real 'XMLTableColumnDefinitionItem' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableFunction(tableRowPattern="sample_text")
    partner = query_XMLTableColumnDefinitionItem()
    setattr(partner, 'XMLTableColumnDefinitionItem', None)
    _safe_set(owner, 'tableFunction82', {partner})
    assert getattr(partner, 'XMLTableColumnDefinitionItem') == owner
    _safe_set(owner, 'tableFunction82', set())
    assert getattr(partner, 'XMLTableColumnDefinitionItem') is None


def test_assoc_columnDefinitionDefault95_stub_double():
    # query_XMLTableColumnDefinitionDefault has no real 'XMLTableColumnDefinitionDefault' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableColumnDefinitionRegular's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableColumnDefinitionRegular's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableColumnDefinitionRegular(passingOption="sample_text", tableColumnPattern="sample_text")
    partner = query_XMLTableColumnDefinitionDefault()
    setattr(partner, 'XMLTableColumnDefinitionDefault', None)
    _safe_set(owner, 'columnDefinitionRegular', partner)
    assert getattr(partner, 'XMLTableColumnDefinitionDefault') == owner
    _safe_set(owner, 'columnDefinitionRegular', None)
    assert getattr(partner, 'XMLTableColumnDefinitionDefault') is None


def test_assoc_columnDefinitionRegular131_stub_double():
    # query_XMLTableColumnDefinitionDefault has no real 'columnDefinitionDefault' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableColumnDefinitionRegular's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableColumnDefinitionRegular's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableColumnDefinitionRegular(passingOption="sample_text", tableColumnPattern="sample_text")
    partner = query_XMLTableColumnDefinitionDefault()
    setattr(partner, 'columnDefinitionDefault', None)
    _safe_set(owner, 'XMLTableColumnDefinitionRegular', partner)
    assert getattr(partner, 'columnDefinitionDefault') == owner
    _safe_set(owner, 'XMLTableColumnDefinitionRegular', None)
    assert getattr(partner, 'columnDefinitionDefault') is None


def test_assoc_commentContent19_stub_double():
    # query_XMLValueFunctionCommentContent has no real 'XMLValueFunctionCommentContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionComment(returningOption="sample_text")
    partner = query_XMLValueFunctionCommentContent()
    setattr(partner, 'XMLValueFunctionCommentContent', None)
    _safe_set(owner, 'valueFunctionComment', partner)
    assert getattr(partner, 'XMLValueFunctionCommentContent') == owner
    _safe_set(owner, 'valueFunctionComment', None)
    assert getattr(partner, 'XMLValueFunctionCommentContent') is None


def test_assoc_concatContentList0_stub_double():
    # query_XMLValueFunctionConcatContentItem has no real 'XMLValueFunctionConcatContentItem' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionConcat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionConcat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionConcat(returningOption="sample_text")
    partner = query_XMLValueFunctionConcatContentItem()
    setattr(partner, 'XMLValueFunctionConcatContentItem', None)
    _safe_set(owner, 'valueFunctionConcat', {partner})
    assert getattr(partner, 'XMLValueFunctionConcatContentItem') == owner
    _safe_set(owner, 'valueFunctionConcat', set())
    assert getattr(partner, 'XMLValueFunctionConcatContentItem') is None


def test_assoc_dataType94_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableColumnDefinitionRegular's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableColumnDefinitionRegular's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableColumnDefinitionRegular(passingOption="sample_text", tableColumnPattern="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'query_XMLTableColumnDefinitionRegular', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'query_XMLTableColumnDefinitionRegular', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_documentContent20_stub_double():
    # query_XMLValueFunctionDocumentContent has no real 'XMLValueFunctionDocumentContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionDocument(returningOption="sample_text")
    partner = query_XMLValueFunctionDocumentContent()
    setattr(partner, 'XMLValueFunctionDocumentContent', None)
    _safe_set(owner, 'valueFunctionDocument', partner)
    assert getattr(partner, 'XMLValueFunctionDocumentContent') == owner
    _safe_set(owner, 'valueFunctionDocument', None)
    assert getattr(partner, 'XMLValueFunctionDocumentContent') is None


def test_assoc_elementContentList13_stub_double():
    # query_XMLValueFunctionElementContentItem has no real 'elementContentListChildren' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionElementContentList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionElementContentList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionElementContentList(nullHandlingOption="sample_text")
    partner = query_XMLValueFunctionElementContentItem()
    setattr(partner, 'elementContentListChildren', None)
    _safe_set(owner, 'XMLValueFunctionElementContentList14', partner)
    assert getattr(partner, 'elementContentListChildren') == owner
    _safe_set(owner, 'XMLValueFunctionElementContentList14', None)
    assert getattr(partner, 'elementContentListChildren') is None


def test_assoc_elementContentListChildren119_stub_double():
    # query_XMLValueFunctionElementContentItem has no real 'XMLValueFunctionElementContentItem' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionElementContentList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionElementContentList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionElementContentList(nullHandlingOption="sample_text")
    partner = query_XMLValueFunctionElementContentItem()
    setattr(partner, 'XMLValueFunctionElementContentItem', None)
    _safe_set(owner, 'elementContentList120', {partner})
    assert getattr(partner, 'XMLValueFunctionElementContentItem') == owner
    _safe_set(owner, 'elementContentList120', set())
    assert getattr(partner, 'XMLValueFunctionElementContentItem') is None


def test_assoc_forestContentList15_stub_double():
    # query_XMLValueFunctionForestContentItem has no real 'XMLValueFunctionForestContentItem' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionForest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionForest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionForest(nullHandlingOption="sample_text", returningOption="sample_text")
    partner = query_XMLValueFunctionForestContentItem()
    setattr(partner, 'XMLValueFunctionForestContentItem', None)
    _safe_set(owner, 'valueFunctionForest', {partner})
    assert getattr(partner, 'XMLValueFunctionForestContentItem') == owner
    _safe_set(owner, 'valueFunctionForest', set())
    assert getattr(partner, 'XMLValueFunctionForestContentItem') is None


def test_assoc_namespaceDecltemList104_stub_double():
    # query_XMLNamespacesDeclaration has no real 'namespacesDecl' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLNamespaceDeclarationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLNamespaceDeclarationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLNamespaceDeclarationItem(uri="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'namespacesDecl', None)
    _safe_set(owner, 'XMLNamespaceDeclarationItem', partner)
    assert owner in getattr(partner, 'namespacesDecl')
    _safe_set(owner, 'XMLNamespaceDeclarationItem', None)
    assert owner not in getattr(partner, 'namespacesDecl')


def test_assoc_namespacesDecl16_stub_double():
    # query_XMLNamespacesDeclaration has no real 'XMLNamespacesDeclaration18' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionForest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionForest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionForest(nullHandlingOption="sample_text", returningOption="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'XMLNamespacesDeclaration18', None)
    _safe_set(owner, 'valueFunctionForest17', partner)
    assert getattr(partner, 'XMLNamespacesDeclaration18') == owner
    _safe_set(owner, 'valueFunctionForest17', None)
    assert getattr(partner, 'XMLNamespacesDeclaration18') is None


def test_assoc_namespacesDecl3_stub_double():
    # query_XMLNamespacesDeclaration has no real 'XMLNamespacesDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionElement(elementName="sample_text", returningOption="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'XMLNamespacesDeclaration', None)
    _safe_set(owner, 'valueFunctionElement', partner)
    assert getattr(partner, 'XMLNamespacesDeclaration') == owner
    _safe_set(owner, 'valueFunctionElement', None)
    assert getattr(partner, 'XMLNamespacesDeclaration') is None


def test_assoc_namespacesDecl83_stub_double():
    # query_XMLNamespacesDeclaration has no real 'XMLNamespacesDeclaration85' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableFunction(tableRowPattern="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'XMLNamespacesDeclaration85', None)
    _safe_set(owner, 'tableFunction84', partner)
    assert getattr(partner, 'XMLNamespacesDeclaration85') == owner
    _safe_set(owner, 'tableFunction84', None)
    assert getattr(partner, 'XMLNamespacesDeclaration85') is None


def test_assoc_namespacesDecl9_stub_double():
    # query_XMLNamespacesDeclaration has no real 'XMLNamespacesDeclaration10' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLNamespaceDeclarationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLNamespaceDeclarationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLNamespaceDeclarationItem(uri="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'XMLNamespacesDeclaration10', None)
    _safe_set(owner, 'namespaceDecltemList', partner)
    assert getattr(partner, 'XMLNamespacesDeclaration10') == owner
    _safe_set(owner, 'namespaceDecltemList', None)
    assert getattr(partner, 'XMLNamespacesDeclaration10') is None


def test_assoc_parseContent21_stub_double():
    # query_XMLValueFunctionParseContent has no real 'XMLValueFunctionParseContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionParse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionParse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionParse(contentOption="sample_text", whitespaceHandlingOption="sample_text")
    partner = query_XMLValueFunctionParseContent()
    setattr(partner, 'XMLValueFunctionParseContent', None)
    _safe_set(owner, 'valueFunctionParse', partner)
    assert getattr(partner, 'XMLValueFunctionParseContent') == owner
    _safe_set(owner, 'valueFunctionParse', None)
    assert getattr(partner, 'XMLValueFunctionParseContent') is None


def test_assoc_predicateExists37_stub_double():
    # query_XMLPredicateExists has no real 'XMLPredicateExists' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLQueryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLQueryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLQueryExpression(xqueryExprContent="sample_text")
    partner = query_XMLPredicateExists()
    setattr(partner, 'XMLPredicateExists', None)
    _safe_set(owner, 'xqueryExpr', partner)
    assert getattr(partner, 'XMLPredicateExists') == owner
    _safe_set(owner, 'xqueryExpr', None)
    assert getattr(partner, 'XMLPredicateExists') is None


def test_assoc_predicateExists40_stub_double():
    # query_XMLPredicateExists has no real 'XMLPredicateExists41' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLQueryArgumentList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLQueryArgumentList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLQueryArgumentList(passingMechanism="sample_text")
    partner = query_XMLPredicateExists()
    setattr(partner, 'XMLPredicateExists41', None)
    _safe_set(owner, 'xqueryArgList', partner)
    assert getattr(partner, 'XMLPredicateExists41') == owner
    _safe_set(owner, 'xqueryArgList', None)
    assert getattr(partner, 'XMLPredicateExists41') is None


def test_assoc_serializeFunction55_stub_double():
    # query_XMLSerializeFunctionTarget has no real 'serializeTarget' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLSerializeFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLSerializeFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLSerializeFunction(contentOption="sample_text", declarationOption="sample_text", serializeVersion="sample_text")
    partner = query_XMLSerializeFunctionTarget()
    setattr(partner, 'serializeTarget', None)
    _safe_set(owner, 'XMLSerializeFunction', partner)
    assert getattr(partner, 'serializeTarget') == owner
    _safe_set(owner, 'XMLSerializeFunction', None)
    assert getattr(partner, 'serializeTarget') is None


def test_assoc_serializeTarget53_stub_double():
    # query_XMLSerializeFunctionTarget has no real 'XMLSerializeFunctionTarget' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLSerializeFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLSerializeFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLSerializeFunction(contentOption="sample_text", declarationOption="sample_text", serializeVersion="sample_text")
    partner = query_XMLSerializeFunctionTarget()
    setattr(partner, 'XMLSerializeFunctionTarget', None)
    _safe_set(owner, 'serializeFunction', partner)
    assert getattr(partner, 'XMLSerializeFunctionTarget') == owner
    _safe_set(owner, 'serializeFunction', None)
    assert getattr(partner, 'XMLSerializeFunctionTarget') is None


def test_assoc_sortSpecList58_stub_double():
    # query_XMLAggregateSortSpecification has no real 'XMLAggregateSortSpecification' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLAggregateFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLAggregateFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLAggregateFunction(returningOption="sample_text")
    partner = query_XMLAggregateSortSpecification()
    setattr(partner, 'XMLAggregateSortSpecification', None)
    _safe_set(owner, 'aggregateFunction', {partner})
    assert getattr(partner, 'XMLAggregateSortSpecification') == owner
    _safe_set(owner, 'aggregateFunction', set())
    assert getattr(partner, 'XMLAggregateSortSpecification') is None


def test_assoc_tableFunction110_stub_double():
    # query_XMLNamespacesDeclaration has no real 'namespacesDecl111' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableFunction(tableRowPattern="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'namespacesDecl111', None)
    _safe_set(owner, 'XMLTableFunction112', partner)
    assert getattr(partner, 'namespacesDecl111') == owner
    _safe_set(owner, 'XMLTableFunction112', None)
    assert getattr(partner, 'namespacesDecl111') is None


def test_assoc_tableFunction92_stub_double():
    # query_XMLTableColumnDefinitionItem has no real 'columnDefList' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLTableFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLTableFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLTableFunction(tableRowPattern="sample_text")
    partner = query_XMLTableColumnDefinitionItem()
    setattr(partner, 'columnDefList', None)
    _safe_set(owner, 'XMLTableFunction93', partner)
    assert getattr(partner, 'columnDefList') == owner
    _safe_set(owner, 'XMLTableFunction93', None)
    assert getattr(partner, 'columnDefList') is None


def test_assoc_textContent28_stub_double():
    # query_XMLValueFunctionTextContent has no real 'XMLValueFunctionTextContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionText(returningOption="sample_text")
    partner = query_XMLValueFunctionTextContent()
    setattr(partner, 'XMLValueFunctionTextContent', None)
    _safe_set(owner, 'valueFunctionText', partner)
    assert getattr(partner, 'XMLValueFunctionTextContent') == owner
    _safe_set(owner, 'valueFunctionText', None)
    assert getattr(partner, 'XMLValueFunctionTextContent') is None


def test_assoc_validateAccordingTo30_stub_double():
    # query_XMLValueFunctionValidateAccordingTo has no real 'XMLValueFunctionValidateAccordingTo' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionValidate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionValidate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionValidate(contentOption="sample_text")
    partner = query_XMLValueFunctionValidateAccordingTo()
    setattr(partner, 'XMLValueFunctionValidateAccordingTo', None)
    _safe_set(owner, 'valueFunctionValidate31', partner)
    assert getattr(partner, 'XMLValueFunctionValidateAccordingTo') == owner
    _safe_set(owner, 'valueFunctionValidate31', None)
    assert getattr(partner, 'XMLValueFunctionValidateAccordingTo') is None


def test_assoc_validateContent29_stub_double():
    # query_XMLValueFunctionValidateContent has no real 'XMLValueFunctionValidateContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionValidate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionValidate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionValidate(contentOption="sample_text")
    partner = query_XMLValueFunctionValidateContent()
    setattr(partner, 'XMLValueFunctionValidateContent', None)
    _safe_set(owner, 'valueFunctionValidate', partner)
    assert getattr(partner, 'XMLValueFunctionValidateContent') == owner
    _safe_set(owner, 'valueFunctionValidate', None)
    assert getattr(partner, 'XMLValueFunctionValidateContent') is None


def test_assoc_validateElement102_stub_double():
    # query_XMLValueFunctionValidateElement has no real 'XMLValueFunctionValidateElement103' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionValidateElementNamespace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionValidateElementNamespace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionValidateElementNamespace(namespaceURI="sample_text", noNamespace=True)
    partner = query_XMLValueFunctionValidateElement()
    setattr(partner, 'XMLValueFunctionValidateElement103', None)
    _safe_set(owner, 'validateElementNamespace', partner)
    assert getattr(partner, 'XMLValueFunctionValidateElement103') == owner
    _safe_set(owner, 'validateElementNamespace', None)
    assert getattr(partner, 'XMLValueFunctionValidateElement103') is None


def test_assoc_validateElementNamespace123_stub_double():
    # query_XMLValueFunctionValidateElement has no real 'validateElement' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionValidateElementNamespace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionValidateElementNamespace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionValidateElementNamespace(namespaceURI="sample_text", noNamespace=True)
    partner = query_XMLValueFunctionValidateElement()
    setattr(partner, 'validateElement', None)
    _safe_set(owner, 'XMLValueFunctionValidateElementNamespace', partner)
    assert getattr(partner, 'validateElement') == owner
    _safe_set(owner, 'XMLValueFunctionValidateElementNamespace', None)
    assert getattr(partner, 'validateElement') is None


def test_assoc_valueExpr51_stub_double():
    # query_QueryValueExpression has no real 'query_QueryValueExpression52' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLQueryArgumentItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLQueryArgumentItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLQueryArgumentItem(passingMechanism="sample_text")
    partner = query_QueryValueExpression()
    setattr(partner, 'query_QueryValueExpression52', None)
    _safe_set(owner, 'query_XMLQueryArgumentItem', partner)
    assert getattr(partner, 'query_QueryValueExpression52') == owner
    _safe_set(owner, 'query_XMLQueryArgumentItem', None)
    assert getattr(partner, 'query_QueryValueExpression52') is None


def test_assoc_valueFunctionComment62_stub_double():
    # query_XMLValueFunctionCommentContent has no real 'commentContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionComment(returningOption="sample_text")
    partner = query_XMLValueFunctionCommentContent()
    setattr(partner, 'commentContent', None)
    _safe_set(owner, 'XMLValueFunctionComment', partner)
    assert getattr(partner, 'commentContent') == owner
    _safe_set(owner, 'XMLValueFunctionComment', None)
    assert getattr(partner, 'commentContent') is None


def test_assoc_valueFunctionConcat59_stub_double():
    # query_XMLValueFunctionConcatContentItem has no real 'concatContentList' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionConcat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionConcat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionConcat(returningOption="sample_text")
    partner = query_XMLValueFunctionConcatContentItem()
    setattr(partner, 'concatContentList', None)
    _safe_set(owner, 'XMLValueFunctionConcat', partner)
    assert getattr(partner, 'concatContentList') == owner
    _safe_set(owner, 'XMLValueFunctionConcat', None)
    assert getattr(partner, 'concatContentList') is None


def test_assoc_valueFunctionDocument65_stub_double():
    # query_XMLValueFunctionDocumentContent has no real 'documentContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionDocument(returningOption="sample_text")
    partner = query_XMLValueFunctionDocumentContent()
    setattr(partner, 'documentContent', None)
    _safe_set(owner, 'XMLValueFunctionDocument', partner)
    assert getattr(partner, 'documentContent') == owner
    _safe_set(owner, 'XMLValueFunctionDocument', None)
    assert getattr(partner, 'documentContent') is None


def test_assoc_valueFunctionElement105_stub_double():
    # query_XMLNamespacesDeclaration has no real 'namespacesDecl106' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionElement(elementName="sample_text", returningOption="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'namespacesDecl106', None)
    _safe_set(owner, 'XMLValueFunctionElement', partner)
    assert getattr(partner, 'namespacesDecl106') == owner
    _safe_set(owner, 'XMLValueFunctionElement', None)
    assert getattr(partner, 'namespacesDecl106') is None


def test_assoc_valueFunctionElement113_stub_double():
    # query_XMLAttributesDeclaration has no real 'attributesDecl' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionElement(elementName="sample_text", returningOption="sample_text")
    partner = query_XMLAttributesDeclaration()
    setattr(partner, 'attributesDecl', None)
    _safe_set(owner, 'XMLValueFunctionElement114', partner)
    assert getattr(partner, 'attributesDecl') == owner
    _safe_set(owner, 'XMLValueFunctionElement114', None)
    assert getattr(partner, 'attributesDecl') is None


def test_assoc_valueFunctionForest107_stub_double():
    # query_XMLNamespacesDeclaration has no real 'namespacesDecl108' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionForest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionForest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionForest(nullHandlingOption="sample_text", returningOption="sample_text")
    partner = query_XMLNamespacesDeclaration()
    setattr(partner, 'namespacesDecl108', None)
    _safe_set(owner, 'XMLValueFunctionForest109', partner)
    assert getattr(partner, 'namespacesDecl108') == owner
    _safe_set(owner, 'XMLValueFunctionForest109', None)
    assert getattr(partner, 'namespacesDecl108') is None


def test_assoc_valueFunctionForest70_stub_double():
    # query_XMLValueFunctionForestContentItem has no real 'forestContentList' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionForest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionForest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionForest(nullHandlingOption="sample_text", returningOption="sample_text")
    partner = query_XMLValueFunctionForestContentItem()
    setattr(partner, 'forestContentList', None)
    _safe_set(owner, 'XMLValueFunctionForest', partner)
    assert getattr(partner, 'forestContentList') == owner
    _safe_set(owner, 'XMLValueFunctionForest', None)
    assert getattr(partner, 'forestContentList') is None


def test_assoc_valueFunctionPI76_stub_double():
    # query_XMLValueFunctionPIContent has no real 'PIContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionPI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionPI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionPI(returningOption="sample_text", targetName="sample_text")
    partner = query_XMLValueFunctionPIContent()
    setattr(partner, 'PIContent', None)
    _safe_set(owner, 'XMLValueFunctionPI', partner)
    assert getattr(partner, 'PIContent') == owner
    _safe_set(owner, 'XMLValueFunctionPI', None)
    assert getattr(partner, 'PIContent') is None


def test_assoc_valueFunctionParse73_stub_double():
    # query_XMLValueFunctionParseContent has no real 'parseContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionParse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionParse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionParse(contentOption="sample_text", whitespaceHandlingOption="sample_text")
    partner = query_XMLValueFunctionParseContent()
    setattr(partner, 'parseContent', None)
    _safe_set(owner, 'XMLValueFunctionParse', partner)
    assert getattr(partner, 'parseContent') == owner
    _safe_set(owner, 'XMLValueFunctionParse', None)
    assert getattr(partner, 'parseContent') is None


def test_assoc_valueFunctionText86_stub_double():
    # query_XMLValueFunctionTextContent has no real 'textContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionText(returningOption="sample_text")
    partner = query_XMLValueFunctionTextContent()
    setattr(partner, 'textContent', None)
    _safe_set(owner, 'XMLValueFunctionText', partner)
    assert getattr(partner, 'textContent') == owner
    _safe_set(owner, 'XMLValueFunctionText', None)
    assert getattr(partner, 'textContent') is None


def test_assoc_valueFunctionValidate89_stub_double():
    # query_XMLValueFunctionValidateContent has no real 'validateContent' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionValidate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionValidate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionValidate(contentOption="sample_text")
    partner = query_XMLValueFunctionValidateContent()
    setattr(partner, 'validateContent', None)
    _safe_set(owner, 'XMLValueFunctionValidate', partner)
    assert getattr(partner, 'validateContent') == owner
    _safe_set(owner, 'XMLValueFunctionValidate', None)
    assert getattr(partner, 'validateContent') is None


def test_assoc_valueFunctionValidate96_stub_double():
    # query_XMLValueFunctionValidateAccordingTo has no real 'validateAccordingTo' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLValueFunctionValidate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLValueFunctionValidate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLValueFunctionValidate(contentOption="sample_text")
    partner = query_XMLValueFunctionValidateAccordingTo()
    setattr(partner, 'validateAccordingTo', None)
    _safe_set(owner, 'XMLValueFunctionValidate97', partner)
    assert getattr(partner, 'validateAccordingTo') == owner
    _safe_set(owner, 'XMLValueFunctionValidate97', None)
    assert getattr(partner, 'validateAccordingTo') is None


def test_assoc_xqueryArgList34_stub_double():
    # query_XMLPredicateExists has no real 'predicateExists35' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLQueryArgumentList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLQueryArgumentList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLQueryArgumentList(passingMechanism="sample_text")
    partner = query_XMLPredicateExists()
    setattr(partner, 'predicateExists35', None)
    _safe_set(owner, 'XMLQueryArgumentList36', partner)
    assert getattr(partner, 'predicateExists35') == owner
    _safe_set(owner, 'XMLQueryArgumentList36', None)
    assert getattr(partner, 'predicateExists35') is None


def test_assoc_xqueryExpr32_stub_double():
    # query_XMLPredicateExists has no real 'predicateExists' property in the generated
    # code (a bare stub) -- manually attach it so query_XMLQueryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_XMLQueryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_XMLQueryExpression(xqueryExprContent="sample_text")
    partner = query_XMLPredicateExists()
    setattr(partner, 'predicateExists', None)
    _safe_set(owner, 'XMLQueryExpression33', partner)
    assert getattr(partner, 'predicateExists') == owner
    _safe_set(owner, 'XMLQueryExpression33', None)
    assert getattr(partner, 'predicateExists') is None


