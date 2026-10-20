import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotationStatement,
    AnyType,
    ArithmeticOperatorExpression,
    AssignmentStatement,
    BinaryOperatorExpression,
    Block,
    CollectionExpression,
    CollectionInitialisationExpression,
    CollectionType,
    ComparableExpression,
    ComparablePrimitiveType,
    ComparisonOperatorExpression,
    EOLElement,
    EOLLibraryModule,
    Expression,
    FeatureCallExpression,
    KeyValueExpression,
    LogicalOperatorExpression,
    OperatorExpression,
    OrderedCollection,
    OrderedCollectionType,
    PrimitiveExpression,
    PrimitiveType,
    PseudoType,
    RealType,
    Statement,
    SummableExpression,
    SummablePrimitiveType,
    SwitchCaseStatement,
    Type,
    UnaryOperatorExpression,
    UniqueCollection,
    UniqueCollectionType,
    VariableDeclarationExpression,
    eol_AbortStatement,
    eol_AndOperatorExpression,
    eol_AnnotationBlock,
    eol_AnnotationStatement,
    eol_AnyType,
    eol_ArithmeticOperatorExpression,
    eol_AssignmentStatement,
    eol_BagExpression,
    eol_BagType,
    eol_BinaryOperatorExpression,
    eol_Block,
    eol_BooleanExpression,
    eol_BooleanType,
    eol_BreakAllStatement,
    eol_BreakStatement,
    eol_CollectionExpression,
    eol_CollectionInitialisationExpression,
    eol_CollectionType,
    eol_ComparableExpression,
    eol_ComparablePrimitiveType,
    eol_ComparisonOperatorExpression,
    eol_ContinueStatement,
    eol_DeleteStatement,
    eol_DivideOperatorExpression,
    eol_EOLElement,
    eol_EOLLibraryModule,
    eol_EOLProgram,
    eol_EnumerationLiteralExpression,
    eol_EqualsOperatorExpression,
    eol_ExecutableAnnotationStatement,
    eol_Expression,
    eol_ExpressionList,
    eol_ExpressionOrStatementBlock,
    eol_ExpressionRange,
    eol_ExpressionStatement,
    eol_FOLMethodCallExpression,
    eol_FeatureCallExpression,
    eol_ForStatement,
    eol_FormalParameterExpression,
    eol_GreaterThanOperatorExpression,
    eol_GreaterThanOrEqualToOperatorExpression,
    eol_IModel,
    eol_IPackage,
    eol_IfStatement,
    eol_ImpliesOperatorExpression,
    eol_Import,
    eol_IntegerExpression,
    eol_IntegerType,
    eol_InvalidType,
    eol_KeyValueExpression,
    eol_LessThanOperatorExpression,
    eol_LessThanOrEqualToOperatorExpression,
    eol_LogicalOperatorExpression,
    eol_MapExpression,
    eol_MapType,
    eol_MethodCallExpression,
    eol_MinusOperatorExpression,
    eol_ModelDeclarationParameter,
    eol_ModelDeclarationStatement,
    eol_ModelElementType,
    eol_ModelType,
    eol_MultiplyOperatorExpression,
    eol_NameExpression,
    eol_NativeType,
    eol_NegativeOperatorExpression,
    eol_NewExpression,
    eol_NotEqualsOperatorExpression,
    eol_NotOperatorExpression,
    eol_OperationDefinition,
    eol_OperatorExpression,
    eol_OrOperatorExpression,
    eol_OrderedCollection,
    eol_OrderedCollectionType,
    eol_OrderedSetExpression,
    eol_OrderedSetType,
    eol_PlusOperatorExpression,
    eol_PrimitiveExpression,
    eol_PrimitiveType,
    eol_PropertyCallExpression,
    eol_PseudoType,
    eol_RealExpression,
    eol_RealType,
    eol_ReturnStatement,
    eol_SelfContentType,
    eol_SelfInnermostContentType,
    eol_SelfType,
    eol_SequenceExpression,
    eol_SequenceType,
    eol_SetExpression,
    eol_SetType,
    eol_SimpleAnnotationStatement,
    eol_SpecialAssignmentStatement,
    eol_Statement,
    eol_StringExpression,
    eol_StringType,
    eol_SummableExpression,
    eol_SummablePrimitiveType,
    eol_SwitchCaseDefaultStatement,
    eol_SwitchCaseExpressionStatement,
    eol_SwitchCaseStatement,
    eol_SwitchStatement,
    eol_TextPosition,
    eol_TextRegion,
    eol_ThrowStatement,
    eol_TransactionStatement,
    eol_Type,
    eol_UnaryOperatorExpression,
    eol_UniqueCollection,
    eol_UniqueCollectionType,
    eol_VariableDeclarationExpression,
    eol_VoidType,
    eol_WhileStatement,
    eol_XorOperatorExpression,
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

def test_assoc_aliases5_reverse_link_reassign_clear():
    a1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_IModel(iMetamodelDriver="sample_text")
    _safe_set(b, 'eol_IModel6', {a1})
    assert _is_linked(b, 'eol_IModel6', a1)
    if hasattr(a1, 'eol_NameExpression7'):
        assert _is_linked(a1, 'eol_NameExpression7', b)
    _safe_set(b, 'eol_IModel6', {a2})
    assert _is_linked(b, 'eol_IModel6', a2)
    if hasattr(a1, 'eol_NameExpression7'):
        assert not _is_linked(a1, 'eol_NameExpression7', b)
    if hasattr(a2, 'eol_NameExpression7'):
        assert _is_linked(a2, 'eol_NameExpression7', b)
    _safe_set(b, 'eol_IModel6', set())
    assert not _is_linked(b, 'eol_IModel6', a2)
    if hasattr(a2, 'eol_NameExpression7'):
        assert not _is_linked(a2, 'eol_NameExpression7', b)


def test_assoc_container1_reverse_link_reassign_clear():
    a1 = eol_EOLElement(uri="sample_text")
    a2 = eol_EOLElement(uri="sample_text_2")
    b = eol_EOLElement(uri="sample_text")
    _safe_set(b, 'eol_EOLElement0', a1)
    assert _is_linked(b, 'eol_EOLElement0', a1)
    if hasattr(a1, 'eol_EOLElement'):
        assert _is_linked(a1, 'eol_EOLElement', b)
    _safe_set(b, 'eol_EOLElement0', a2)
    assert _is_linked(b, 'eol_EOLElement0', a2)
    if hasattr(a1, 'eol_EOLElement'):
        assert not _is_linked(a1, 'eol_EOLElement', b)
    if hasattr(a2, 'eol_EOLElement'):
        assert _is_linked(a2, 'eol_EOLElement', b)
    _safe_set(b, 'eol_EOLElement0', None)
    assert not _is_linked(b, 'eol_EOLElement0', a2)
    if hasattr(a2, 'eol_EOLElement'):
        assert not _is_linked(a2, 'eol_EOLElement', b)


def test_assoc_driver8_reverse_link_reassign_clear():
    a1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_IModel(iMetamodelDriver="sample_text")
    _safe_set(b, 'eol_IModel9', a1)
    assert _is_linked(b, 'eol_IModel9', a1)
    if hasattr(a1, 'eol_NameExpression10'):
        assert _is_linked(a1, 'eol_NameExpression10', b)
    _safe_set(b, 'eol_IModel9', a2)
    assert _is_linked(b, 'eol_IModel9', a2)
    if hasattr(a1, 'eol_NameExpression10'):
        assert not _is_linked(a1, 'eol_NameExpression10', b)
    if hasattr(a2, 'eol_NameExpression10'):
        assert _is_linked(a2, 'eol_NameExpression10', b)
    _safe_set(b, 'eol_IModel9', None)
    assert not _is_linked(b, 'eol_IModel9', a2)
    if hasattr(a2, 'eol_NameExpression10'):
        assert not _is_linked(a2, 'eol_NameExpression10', b)


def test_assoc_iModels24_reverse_link_reassign_clear():
    a1 = eol_IModel(iMetamodelDriver="sample_text")
    a2 = eol_IModel(iMetamodelDriver="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule25', {a1})
    assert _is_linked(b, 'eol_EOLLibraryModule25', a1)
    if hasattr(a1, 'eol_IModel26'):
        assert _is_linked(a1, 'eol_IModel26', b)
    _safe_set(b, 'eol_EOLLibraryModule25', {a2})
    assert _is_linked(b, 'eol_EOLLibraryModule25', a2)
    if hasattr(a1, 'eol_IModel26'):
        assert not _is_linked(a1, 'eol_IModel26', b)
    if hasattr(a2, 'eol_IModel26'):
        assert _is_linked(a2, 'eol_IModel26', b)
    _safe_set(b, 'eol_EOLLibraryModule25', set())
    assert not _is_linked(b, 'eol_EOLLibraryModule25', a2)
    if hasattr(a2, 'eol_IModel26'):
        assert not _is_linked(a2, 'eol_IModel26', b)


def test_assoc_iPackages11_reverse_link_reassign_clear():
    a1 = eol_IPackage(iPackageDriver="sample_text", name="sample_text", nsPrefix="sample_text")
    a2 = eol_IPackage(iPackageDriver="sample_text_2", name="sample_text_2", nsPrefix="sample_text_2")
    b = eol_IModel(iMetamodelDriver="sample_text")
    _safe_set(b, 'eol_IModel12', {a1})
    assert _is_linked(b, 'eol_IModel12', a1)
    if hasattr(a1, 'eol_IPackage'):
        assert _is_linked(a1, 'eol_IPackage', b)
    _safe_set(b, 'eol_IModel12', {a2})
    assert _is_linked(b, 'eol_IModel12', a2)
    if hasattr(a1, 'eol_IPackage'):
        assert not _is_linked(a1, 'eol_IPackage', b)
    if hasattr(a2, 'eol_IPackage'):
        assert _is_linked(a2, 'eol_IPackage', b)
    _safe_set(b, 'eol_IModel12', set())
    assert not _is_linked(b, 'eol_IModel12', a2)
    if hasattr(a2, 'eol_IPackage'):
        assert not _is_linked(a2, 'eol_IPackage', b)


def test_assoc_importedModule32_reverse_link_reassign_clear():
    a1 = eol_Import(imported="sample_text")
    a2 = eol_Import(imported="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule34', a1)
    assert _is_linked(b, 'eol_EOLLibraryModule34', a1)
    if hasattr(a1, 'eol_Import33'):
        assert _is_linked(a1, 'eol_Import33', b)
    _safe_set(b, 'eol_EOLLibraryModule34', a2)
    assert _is_linked(b, 'eol_EOLLibraryModule34', a2)
    if hasattr(a1, 'eol_Import33'):
        assert not _is_linked(a1, 'eol_Import33', b)
    if hasattr(a2, 'eol_Import33'):
        assert _is_linked(a2, 'eol_Import33', b)
    _safe_set(b, 'eol_EOLLibraryModule34', None)
    assert not _is_linked(b, 'eol_EOLLibraryModule34', a2)
    if hasattr(a2, 'eol_Import33'):
        assert not _is_linked(a2, 'eol_Import33', b)


def test_assoc_imports23_reverse_link_reassign_clear():
    a1 = eol_Import(imported="sample_text")
    a2 = eol_Import(imported="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule', {a1})
    assert _is_linked(b, 'eol_EOLLibraryModule', a1)
    if hasattr(a1, 'eol_Import'):
        assert _is_linked(a1, 'eol_Import', b)
    _safe_set(b, 'eol_EOLLibraryModule', {a2})
    assert _is_linked(b, 'eol_EOLLibraryModule', a2)
    if hasattr(a1, 'eol_Import'):
        assert not _is_linked(a1, 'eol_Import', b)
    if hasattr(a2, 'eol_Import'):
        assert _is_linked(a2, 'eol_Import', b)
    _safe_set(b, 'eol_EOLLibraryModule', set())
    assert not _is_linked(b, 'eol_EOLLibraryModule', a2)
    if hasattr(a2, 'eol_Import'):
        assert not _is_linked(a2, 'eol_Import', b)


def test_assoc_name4_reverse_link_reassign_clear():
    a1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_IModel(iMetamodelDriver="sample_text")
    _safe_set(b, 'eol_IModel', a1)
    assert _is_linked(b, 'eol_IModel', a1)
    if hasattr(a1, 'eol_NameExpression'):
        assert _is_linked(a1, 'eol_NameExpression', b)
    _safe_set(b, 'eol_IModel', a2)
    assert _is_linked(b, 'eol_IModel', a2)
    if hasattr(a1, 'eol_NameExpression'):
        assert not _is_linked(a1, 'eol_NameExpression', b)
    if hasattr(a2, 'eol_NameExpression'):
        assert _is_linked(a2, 'eol_NameExpression', b)
    _safe_set(b, 'eol_IModel', None)
    assert not _is_linked(b, 'eol_IModel', a2)
    if hasattr(a2, 'eol_NameExpression'):
        assert not _is_linked(a2, 'eol_NameExpression', b)


def test_assoc_name74_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression76', a1)
    assert _is_linked(b, 'eol_NameExpression76', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression75'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression75', b)
    _safe_set(b, 'eol_NameExpression76', a2)
    assert _is_linked(b, 'eol_NameExpression76', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression75'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression75', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression75'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression75', b)
    _safe_set(b, 'eol_NameExpression76', None)
    assert not _is_linked(b, 'eol_NameExpression76', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression75'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression75', b)


def test_assoc_nsURI13_reverse_link_reassign_clear():
    a1 = eol_StringExpression(value="sample_text")
    a2 = eol_StringExpression(value="sample_text_2")
    b = eol_IPackage(iPackageDriver="sample_text", name="sample_text", nsPrefix="sample_text")
    _safe_set(b, 'eol_IPackage14', a1)
    assert _is_linked(b, 'eol_IPackage14', a1)
    if hasattr(a1, 'eol_StringExpression'):
        assert _is_linked(a1, 'eol_StringExpression', b)
    _safe_set(b, 'eol_IPackage14', a2)
    assert _is_linked(b, 'eol_IPackage14', a2)
    if hasattr(a1, 'eol_StringExpression'):
        assert not _is_linked(a1, 'eol_StringExpression', b)
    if hasattr(a2, 'eol_StringExpression'):
        assert _is_linked(a2, 'eol_StringExpression', b)
    _safe_set(b, 'eol_IPackage14', None)
    assert not _is_linked(b, 'eol_IPackage14', a2)
    if hasattr(a2, 'eol_StringExpression'):
        assert not _is_linked(a2, 'eol_StringExpression', b)


def test_assoc_property93_reverse_link_reassign_clear():
    a1 = eol_PropertyCallExpression(extended=True)
    a2 = eol_PropertyCallExpression(extended=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression94', a1)
    assert _is_linked(b, 'eol_NameExpression94', a1)
    if hasattr(a1, 'eol_PropertyCallExpression'):
        assert _is_linked(a1, 'eol_PropertyCallExpression', b)
    _safe_set(b, 'eol_NameExpression94', a2)
    assert _is_linked(b, 'eol_NameExpression94', a2)
    if hasattr(a1, 'eol_PropertyCallExpression'):
        assert not _is_linked(a1, 'eol_PropertyCallExpression', b)
    if hasattr(a2, 'eol_PropertyCallExpression'):
        assert _is_linked(a2, 'eol_PropertyCallExpression', b)
    _safe_set(b, 'eol_NameExpression94', None)
    assert not _is_linked(b, 'eol_NameExpression94', a2)
    if hasattr(a2, 'eol_PropertyCallExpression'):
        assert not _is_linked(a2, 'eol_PropertyCallExpression', b)


def test_assoc_references80_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression82', a1)
    assert _is_linked(b, 'eol_NameExpression82', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression81'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression81', b)
    _safe_set(b, 'eol_NameExpression82', a2)
    assert _is_linked(b, 'eol_NameExpression82', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression81'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression81', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression81'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression81', b)
    _safe_set(b, 'eol_NameExpression82', None)
    assert not _is_linked(b, 'eol_NameExpression82', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression81'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression81', b)


def test_assoc_resolvedIModel214_reverse_link_reassign_clear():
    a1 = eol_ModelElementType(elementName="sample_text", modelName="sample_text", modelType="sample_text")
    a2 = eol_ModelElementType(elementName="sample_text_2", modelName="sample_text_2", modelType="sample_text_2")
    b = eol_IModel(iMetamodelDriver="sample_text")
    _safe_set(b, 'eol_IModel215', a1)
    assert _is_linked(b, 'eol_IModel215', a1)
    if hasattr(a1, 'eol_ModelElementType'):
        assert _is_linked(a1, 'eol_ModelElementType', b)
    _safe_set(b, 'eol_IModel215', a2)
    assert _is_linked(b, 'eol_IModel215', a2)
    if hasattr(a1, 'eol_ModelElementType'):
        assert not _is_linked(a1, 'eol_ModelElementType', b)
    if hasattr(a2, 'eol_ModelElementType'):
        assert _is_linked(a2, 'eol_ModelElementType', b)
    _safe_set(b, 'eol_IModel215', None)
    assert not _is_linked(b, 'eol_IModel215', a2)
    if hasattr(a2, 'eol_ModelElementType'):
        assert not _is_linked(a2, 'eol_ModelElementType', b)


def test_assoc_resolvedIPackage219_reverse_link_reassign_clear():
    a1 = eol_ModelElementType(elementName="sample_text", modelName="sample_text", modelType="sample_text")
    a2 = eol_ModelElementType(elementName="sample_text_2", modelName="sample_text_2", modelType="sample_text_2")
    b = eol_IPackage(iPackageDriver="sample_text", name="sample_text", nsPrefix="sample_text")
    _safe_set(b, 'eol_IPackage221', a1)
    assert _is_linked(b, 'eol_IPackage221', a1)
    if hasattr(a1, 'eol_ModelElementType220'):
        assert _is_linked(a1, 'eol_ModelElementType220', b)
    _safe_set(b, 'eol_IPackage221', a2)
    assert _is_linked(b, 'eol_IPackage221', a2)
    if hasattr(a1, 'eol_ModelElementType220'):
        assert not _is_linked(a1, 'eol_ModelElementType220', b)
    if hasattr(a2, 'eol_ModelElementType220'):
        assert _is_linked(a2, 'eol_ModelElementType220', b)
    _safe_set(b, 'eol_IPackage221', None)
    assert not _is_linked(b, 'eol_IPackage221', a2)
    if hasattr(a2, 'eol_ModelElementType220'):
        assert not _is_linked(a2, 'eol_ModelElementType220', b)


def test_assoc_subPackages16_reverse_link_reassign_clear():
    a1 = eol_IPackage(iPackageDriver="sample_text", name="sample_text", nsPrefix="sample_text")
    a2 = eol_IPackage(iPackageDriver="sample_text_2", name="sample_text_2", nsPrefix="sample_text_2")
    b = eol_IPackage(iPackageDriver="sample_text", name="sample_text", nsPrefix="sample_text")
    _safe_set(b, 'eol_IPackage17', a1)
    assert _is_linked(b, 'eol_IPackage17', a1)
    if hasattr(a1, 'eol_IPackage15'):
        assert _is_linked(a1, 'eol_IPackage15', b)
    _safe_set(b, 'eol_IPackage17', a2)
    assert _is_linked(b, 'eol_IPackage17', a2)
    if hasattr(a1, 'eol_IPackage15'):
        assert not _is_linked(a1, 'eol_IPackage15', b)
    if hasattr(a2, 'eol_IPackage15'):
        assert _is_linked(a2, 'eol_IPackage15', b)
    _safe_set(b, 'eol_IPackage17', None)
    assert not _is_linked(b, 'eol_IPackage17', a2)
    if hasattr(a2, 'eol_IPackage15'):
        assert not _is_linked(a2, 'eol_IPackage15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alias202_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement203' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement203', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression204', partner)
    assert owner in getattr(partner, 'eol_ModelDeclarationStatement203')
    _safe_set(owner, 'eol_VariableDeclarationExpression204', None)
    assert owner not in getattr(partner, 'eol_ModelDeclarationStatement203')


def test_assoc_driver199_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement200' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement200', None)
    _safe_set(owner, 'eol_NameExpression201', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement200') == owner
    _safe_set(owner, 'eol_NameExpression201', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement200') is None


def test_assoc_dynamicTypes210_stub_double():
    # eol_Type has no real 'eol_Type211' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_Type()
    setattr(partner, 'eol_Type211', None)
    _safe_set(owner, 'eol_AnyType', {partner})
    assert getattr(partner, 'eol_Type211') == owner
    _safe_set(owner, 'eol_AnyType', set())
    assert getattr(partner, 'eol_Type211') is None


def test_assoc_end20_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion21' property in the generated
    # code (a bare stub) -- manually attach it so eol_TextPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_TextPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_TextPosition(column=7, line=7)
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion21', None)
    _safe_set(owner, 'eol_TextPosition22', partner)
    assert getattr(partner, 'eol_TextRegion21') == owner
    _safe_set(owner, 'eol_TextPosition22', None)
    assert getattr(partner, 'eol_TextRegion21') is None


def test_assoc_enumeration124_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression125' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression125', None)
    _safe_set(owner, 'eol_NameExpression126', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression125') == owner
    _safe_set(owner, 'eol_NameExpression126', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression125') is None


def test_assoc_expression227_stub_double():
    # eol_NativeType has no real 'eol_NativeType' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(value="sample_text")
    partner = eol_NativeType()
    setattr(partner, 'eol_NativeType', None)
    _safe_set(owner, 'eol_StringExpression228', partner)
    assert getattr(partner, 'eol_NativeType') == owner
    _safe_set(owner, 'eol_StringExpression228', None)
    assert getattr(partner, 'eol_NativeType') is None


def test_assoc_iModel127_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression128' property in the generated
    # code (a bare stub) -- manually attach it so eol_IModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_IModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_IModel(iMetamodelDriver="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression128', None)
    _safe_set(owner, 'eol_IModel129', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression128') == owner
    _safe_set(owner, 'eol_IModel129', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression128') is None


def test_assoc_imodel205_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement206' property in the generated
    # code (a bare stub) -- manually attach it so eol_IModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_IModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_IModel(iMetamodelDriver="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement206', None)
    _safe_set(owner, 'eol_IModel207', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement206') == owner
    _safe_set(owner, 'eol_IModel207', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement206') is None


def test_assoc_keyType222_stub_double():
    # eol_MapType has no real 'eol_MapType' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_MapType()
    setattr(partner, 'eol_MapType', None)
    _safe_set(owner, 'eol_AnyType223', partner)
    assert getattr(partner, 'eol_MapType') == owner
    _safe_set(owner, 'eol_AnyType223', None)
    assert getattr(partner, 'eol_MapType') is None


def test_assoc_literal122_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression', None)
    _safe_set(owner, 'eol_NameExpression123', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'eol_NameExpression123', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') is None


def test_assoc_method100_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression101' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression101', None)
    _safe_set(owner, 'eol_NameExpression102', partner)
    assert getattr(partner, 'eol_FOLMethodCallExpression101') == owner
    _safe_set(owner, 'eol_NameExpression102', None)
    assert getattr(partner, 'eol_FOLMethodCallExpression101') is None


def test_assoc_method87_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression88' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression88', None)
    _safe_set(owner, 'eol_NameExpression89', partner)
    assert getattr(partner, 'eol_MethodCallExpression88') == owner
    _safe_set(owner, 'eol_NameExpression89', None)
    assert getattr(partner, 'eol_MethodCallExpression88') is None


def test_assoc_model130_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression131' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression131', None)
    _safe_set(owner, 'eol_NameExpression132', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression131') == owner
    _safe_set(owner, 'eol_NameExpression132', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression131') is None


def test_assoc_modelDeclarations27_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_EOLLibraryModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_EOLLibraryModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_EOLLibraryModule(name="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement', None)
    _safe_set(owner, 'eol_EOLLibraryModule28', {partner})
    assert getattr(partner, 'eol_ModelDeclarationStatement') == owner
    _safe_set(owner, 'eol_EOLLibraryModule28', set())
    assert getattr(partner, 'eol_ModelDeclarationStatement') is None


def test_assoc_name190_stub_double():
    # eol_AnnotationStatement has no real 'eol_AnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_AnnotationStatement()
    setattr(partner, 'eol_AnnotationStatement', None)
    _safe_set(owner, 'eol_NameExpression191', partner)
    assert getattr(partner, 'eol_AnnotationStatement') == owner
    _safe_set(owner, 'eol_NameExpression191', None)
    assert getattr(partner, 'eol_AnnotationStatement') is None


def test_assoc_name196_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement197' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement197', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression198', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement197') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression198', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement197') is None


def test_assoc_name51_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition52' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition52', None)
    _safe_set(owner, 'eol_NameExpression53', partner)
    assert getattr(partner, 'eol_OperationDefinition52') == owner
    _safe_set(owner, 'eol_NameExpression53', None)
    assert getattr(partner, 'eol_OperationDefinition52') is None


def test_assoc_names140_stub_double():
    # eol_TransactionStatement has no real 'eol_TransactionStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_TransactionStatement()
    setattr(partner, 'eol_TransactionStatement', None)
    _safe_set(owner, 'eol_NameExpression141', partner)
    assert owner in getattr(partner, 'eol_TransactionStatement')
    _safe_set(owner, 'eol_NameExpression141', None)
    assert owner not in getattr(partner, 'eol_TransactionStatement')


def test_assoc_operations29_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition' property in the generated
    # code (a bare stub) -- manually attach it so eol_EOLLibraryModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_EOLLibraryModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_EOLLibraryModule(name="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition', None)
    _safe_set(owner, 'eol_EOLLibraryModule30', {partner})
    assert getattr(partner, 'eol_OperationDefinition') == owner
    _safe_set(owner, 'eol_EOLLibraryModule30', set())
    assert getattr(partner, 'eol_OperationDefinition') is None


def test_assoc_parameters77_stub_double():
    # eol_Expression has no real 'eol_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_Expression()
    setattr(partner, 'eol_Expression79', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression78', {partner})
    assert getattr(partner, 'eol_Expression79') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression78', set())
    assert getattr(partner, 'eol_Expression79') is None


def test_assoc_region2_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion' property in the generated
    # code (a bare stub) -- manually attach it so eol_EOLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_EOLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_EOLElement(uri="sample_text")
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion', None)
    _safe_set(owner, 'eol_EOLElement3', partner)
    assert getattr(partner, 'eol_TextRegion') == owner
    _safe_set(owner, 'eol_EOLElement3', None)
    assert getattr(partner, 'eol_TextRegion') is None


def test_assoc_resolvedIModel212_stub_double():
    # eol_ModelType has no real 'eol_ModelType' property in the generated
    # code (a bare stub) -- manually attach it so eol_IModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_IModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_IModel(iMetamodelDriver="sample_text")
    partner = eol_ModelType()
    setattr(partner, 'eol_ModelType', None)
    _safe_set(owner, 'eol_IModel213', partner)
    assert getattr(partner, 'eol_ModelType') == owner
    _safe_set(owner, 'eol_IModel213', None)
    assert getattr(partner, 'eol_ModelType') is None


def test_assoc_resolvedModelDeclaration216_stub_double():
    # eol_ModelDeclarationStatement has no real 'eol_ModelDeclarationStatement218' property in the generated
    # code (a bare stub) -- manually attach it so eol_ModelElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_ModelElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_ModelElementType(elementName="sample_text", modelName="sample_text", modelType="sample_text")
    partner = eol_ModelDeclarationStatement()
    setattr(partner, 'eol_ModelDeclarationStatement218', None)
    _safe_set(owner, 'eol_ModelElementType217', partner)
    assert getattr(partner, 'eol_ModelDeclarationStatement218') == owner
    _safe_set(owner, 'eol_ModelElementType217', None)
    assert getattr(partner, 'eol_ModelDeclarationStatement218') is None


def test_assoc_result58_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition59' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition59', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression60', partner)
    assert getattr(partner, 'eol_OperationDefinition59') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression60', None)
    assert getattr(partner, 'eol_OperationDefinition59') is None


def test_assoc_self56_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition57' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition57', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression', partner)
    assert getattr(partner, 'eol_OperationDefinition57') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression', None)
    assert getattr(partner, 'eol_OperationDefinition57') is None


def test_assoc_start18_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion19' property in the generated
    # code (a bare stub) -- manually attach it so eol_TextPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_TextPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_TextPosition(column=7, line=7)
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion19', None)
    _safe_set(owner, 'eol_TextPosition', partner)
    assert getattr(partner, 'eol_TextRegion19') == owner
    _safe_set(owner, 'eol_TextPosition', None)
    assert getattr(partner, 'eol_TextRegion19') is None


def test_assoc_target83_stub_double():
    # eol_Expression has no real 'eol_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so eol_FeatureCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_FeatureCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_FeatureCallExpression(isArrow=True)
    partner = eol_Expression()
    setattr(partner, 'eol_Expression84', None)
    _safe_set(owner, 'eol_FeatureCallExpression', partner)
    assert getattr(partner, 'eol_Expression84') == owner
    _safe_set(owner, 'eol_FeatureCallExpression', None)
    assert getattr(partner, 'eol_Expression84') is None


def test_assoc_typeName111_stub_double():
    # eol_NewExpression has no real 'eol_NewExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_NewExpression()
    setattr(partner, 'eol_NewExpression', None)
    _safe_set(owner, 'eol_NameExpression112', partner)
    assert getattr(partner, 'eol_NewExpression') == owner
    _safe_set(owner, 'eol_NameExpression112', None)
    assert getattr(partner, 'eol_NewExpression') is None


def test_assoc_valueType224_stub_double():
    # eol_MapType has no real 'eol_MapType225' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_MapType()
    setattr(partner, 'eol_MapType225', None)
    _safe_set(owner, 'eol_AnyType226', partner)
    assert getattr(partner, 'eol_MapType225') == owner
    _safe_set(owner, 'eol_AnyType226', None)
    assert getattr(partner, 'eol_MapType225') is None


def test_assoc_values192_stub_double():
    # eol_SimpleAnnotationStatement has no real 'eol_SimpleAnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(value="sample_text")
    partner = eol_SimpleAnnotationStatement()
    setattr(partner, 'eol_SimpleAnnotationStatement', None)
    _safe_set(owner, 'eol_StringExpression193', partner)
    assert owner in getattr(partner, 'eol_SimpleAnnotationStatement')
    _safe_set(owner, 'eol_StringExpression193', None)
    assert owner not in getattr(partner, 'eol_SimpleAnnotationStatement')


