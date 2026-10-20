from python_code import query_XMLAggregateFunction
from python_code import query_XMLAggregateSortSpecification

def test_query_XMLAggregateFunction___init__():
    assert query_XMLAggregateFunction.__init__(query_XMLAggregateFunction('', aggregateFunction=set(), XMLAggregateFunction=query_XMLAggregateSortSpecification()), '', aggregateFunction=set(), XMLAggregateFunction=query_XMLAggregateSortSpecification()) == None


from python_code import query_XMLNamespaceDeclarationDefault

def test_query_XMLNamespaceDeclarationDefault___init__():
    assert query_XMLNamespaceDeclarationDefault.__init__(query_XMLNamespaceDeclarationDefault(True), False) == None


from python_code import query_XMLNamespaceDeclarationItem
from python_code import query_XMLNamespacesDeclaration

def test_query_XMLNamespaceDeclarationItem___init__():
    assert query_XMLNamespaceDeclarationItem.__init__(query_XMLNamespaceDeclarationItem('', namespaceDecltemList=query_XMLNamespacesDeclaration(), XMLNamespaceDeclarationItem=query_XMLNamespacesDeclaration()), '', namespaceDecltemList=query_XMLNamespacesDeclaration(), XMLNamespaceDeclarationItem=query_XMLNamespacesDeclaration()) == None


from python_code import query_XMLNamespaceDeclarationPrefix

def test_query_XMLNamespaceDeclarationPrefix___init__():
    assert query_XMLNamespaceDeclarationPrefix.__init__(query_XMLNamespaceDeclarationPrefix(''), '') == None


from python_code import DataType
from python_code import query_XMLTableColumnDefinitionDefault
from python_code import query_XMLTableColumnDefinitionRegular

def test_query_XMLTableColumnDefinitionRegular___init__():
    assert query_XMLTableColumnDefinitionRegular.__init__(query_XMLTableColumnDefinitionRegular('', '\x00', query_XMLTableColumnDefinitionRegular=DataType(), columnDefinitionRegular=query_XMLTableColumnDefinitionDefault(), XMLTableColumnDefinitionRegular=query_XMLTableColumnDefinitionDefault()), '\x00\x00', '', query_XMLTableColumnDefinitionRegular=DataType(), columnDefinitionRegular=query_XMLTableColumnDefinitionDefault(), XMLTableColumnDefinitionRegular=query_XMLTableColumnDefinitionDefault()) == None


from python_code import query_XMLValueExpressionCast

def test_query_XMLValueExpressionCast___init__():
    assert query_XMLValueExpressionCast.__init__(query_XMLValueExpressionCast(''), '') == None


from python_code import query_XMLValueFunctionComment
from python_code import query_XMLValueFunctionCommentContent

def test_query_XMLValueFunctionComment___init__():
    assert query_XMLValueFunctionComment.__init__(query_XMLValueFunctionComment('', valueFunctionComment=query_XMLValueFunctionCommentContent(), XMLValueFunctionComment=query_XMLValueFunctionCommentContent()), '', valueFunctionComment=query_XMLValueFunctionCommentContent(), XMLValueFunctionComment=query_XMLValueFunctionCommentContent()) == None


from python_code import query_XMLValueFunctionConcat
from python_code import query_XMLValueFunctionConcatContentItem

def test_query_XMLValueFunctionConcat___init__():
    assert query_XMLValueFunctionConcat.__init__(query_XMLValueFunctionConcat('', valueFunctionConcat=set(), XMLValueFunctionConcat=query_XMLValueFunctionConcatContentItem()), '', valueFunctionConcat=set(), XMLValueFunctionConcat=query_XMLValueFunctionConcatContentItem()) == None


from python_code import query_XMLValueFunctionDocument
from python_code import query_XMLValueFunctionDocumentContent

def test_query_XMLValueFunctionDocument___init__():
    assert query_XMLValueFunctionDocument.__init__(query_XMLValueFunctionDocument('', valueFunctionDocument=query_XMLValueFunctionDocumentContent(), XMLValueFunctionDocument=query_XMLValueFunctionDocumentContent()), '', valueFunctionDocument=query_XMLValueFunctionDocumentContent(), XMLValueFunctionDocument=query_XMLValueFunctionDocumentContent()) == None


from python_code import query_XMLNamespacesDeclaration
from python_code import query_XMLValueFunctionForest
from python_code import query_XMLValueFunctionForestContentItem

def test_query_XMLValueFunctionForest___init__():
    assert query_XMLValueFunctionForest.__init__(query_XMLValueFunctionForest('\x00\x00', '', valueFunctionForest=set(), valueFunctionForest17=query_XMLNamespacesDeclaration(), XMLValueFunctionForest=query_XMLValueFunctionForestContentItem(), XMLValueFunctionForest109=query_XMLNamespacesDeclaration()), '', '', valueFunctionForest=set(), valueFunctionForest17=query_XMLNamespacesDeclaration(), XMLValueFunctionForest=query_XMLValueFunctionForestContentItem(), XMLValueFunctionForest109=query_XMLNamespacesDeclaration()) == None


from python_code import query_XMLValueFunctionPI
from python_code import query_XMLValueFunctionPIContent

def test_query_XMLValueFunctionPI___init__():
    assert query_XMLValueFunctionPI.__init__(query_XMLValueFunctionPI('', '\x00', valueFunctionPI=query_XMLValueFunctionPIContent(), XMLValueFunctionPI=query_XMLValueFunctionPIContent()), '\x00\x00', '', valueFunctionPI=query_XMLValueFunctionPIContent(), XMLValueFunctionPI=query_XMLValueFunctionPIContent()) == None


from python_code import query_XMLValueFunctionParse
from python_code import query_XMLValueFunctionParseContent

def test_query_XMLValueFunctionParse___init__():
    assert query_XMLValueFunctionParse.__init__(query_XMLValueFunctionParse('', '\x00', valueFunctionParse=query_XMLValueFunctionParseContent(), XMLValueFunctionParse=query_XMLValueFunctionParseContent()), '\x00\x00', '', valueFunctionParse=query_XMLValueFunctionParseContent(), XMLValueFunctionParse=query_XMLValueFunctionParseContent()) == None


from python_code import query_XMLValueFunctionText
from python_code import query_XMLValueFunctionTextContent

def test_query_XMLValueFunctionText___init__():
    assert query_XMLValueFunctionText.__init__(query_XMLValueFunctionText('', valueFunctionText=query_XMLValueFunctionTextContent(), XMLValueFunctionText=query_XMLValueFunctionTextContent()), '', valueFunctionText=query_XMLValueFunctionTextContent(), XMLValueFunctionText=query_XMLValueFunctionTextContent()) == None


from python_code import query_XMLValueFunctionValidate
from python_code import query_XMLValueFunctionValidateAccordingTo
from python_code import query_XMLValueFunctionValidateContent

def test_query_XMLValueFunctionValidate___init__():
    assert query_XMLValueFunctionValidate.__init__(query_XMLValueFunctionValidate('', valueFunctionValidate=query_XMLValueFunctionValidateContent(), valueFunctionValidate31=query_XMLValueFunctionValidateAccordingTo(), XMLValueFunctionValidate=query_XMLValueFunctionValidateContent(), XMLValueFunctionValidate97=query_XMLValueFunctionValidateAccordingTo()), '', valueFunctionValidate=query_XMLValueFunctionValidateContent(), valueFunctionValidate31=query_XMLValueFunctionValidateAccordingTo(), XMLValueFunctionValidate=query_XMLValueFunctionValidateContent(), XMLValueFunctionValidate97=query_XMLValueFunctionValidateAccordingTo()) == None


from python_code import query_XMLValueFunctionValidateAccordingToIdentifier

def test_query_XMLValueFunctionValidateAccordingToIdentifier___init__():
    assert query_XMLValueFunctionValidateAccordingToIdentifier.__init__(query_XMLValueFunctionValidateAccordingToIdentifier('', '\x00'), '\x00\x00', '') == None


from python_code import query_XMLValueFunctionValidateAccordingToURI

def test_query_XMLValueFunctionValidateAccordingToURI___init__():
    assert query_XMLValueFunctionValidateAccordingToURI.__init__(query_XMLValueFunctionValidateAccordingToURI(False, '', '\x00\x00'), False, '', '') == None


from python_code import query_XMLValueFunctionValidateElement
from python_code import query_XMLValueFunctionValidateElementNamespace

def test_query_XMLValueFunctionValidateElementNamespace___init__():
    assert query_XMLValueFunctionValidateElementNamespace.__init__(query_XMLValueFunctionValidateElementNamespace(False, '\x00', XMLValueFunctionValidateElementNamespace=query_XMLValueFunctionValidateElement(), validateElementNamespace=query_XMLValueFunctionValidateElement()), False, '\x00', XMLValueFunctionValidateElementNamespace=query_XMLValueFunctionValidateElement(), validateElementNamespace=query_XMLValueFunctionValidateElement()) == None

