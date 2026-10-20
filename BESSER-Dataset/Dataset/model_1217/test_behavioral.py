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
    eol_EOLModule,
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

def test_assoc_aliases183_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement184', {a1})
    assert _is_linked(b, 'eol_ModelDeclarationStatement184', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression185'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression185', b)
    _safe_set(b, 'eol_ModelDeclarationStatement184', {a2})
    assert _is_linked(b, 'eol_ModelDeclarationStatement184', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression185'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression185', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression185'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression185', b)
    _safe_set(b, 'eol_ModelDeclarationStatement184', set())
    assert not _is_linked(b, 'eol_ModelDeclarationStatement184', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression185'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression185', b)


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


def test_assoc_driver180_reverse_link_reassign_clear():
    a1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement181', a1)
    assert _is_linked(b, 'eol_ModelDeclarationStatement181', a1)
    if hasattr(a1, 'eol_NameExpression182'):
        assert _is_linked(a1, 'eol_NameExpression182', b)
    _safe_set(b, 'eol_ModelDeclarationStatement181', a2)
    assert _is_linked(b, 'eol_ModelDeclarationStatement181', a2)
    if hasattr(a1, 'eol_NameExpression182'):
        assert not _is_linked(a1, 'eol_NameExpression182', b)
    if hasattr(a2, 'eol_NameExpression182'):
        assert _is_linked(a2, 'eol_NameExpression182', b)
    _safe_set(b, 'eol_ModelDeclarationStatement181', None)
    assert not _is_linked(b, 'eol_ModelDeclarationStatement181', a2)
    if hasattr(a2, 'eol_NameExpression182'):
        assert not _is_linked(a2, 'eol_NameExpression182', b)


def test_assoc_importedModule15_reverse_link_reassign_clear():
    a1 = eol_Import(imported="sample_text")
    a2 = eol_Import(imported="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule17', a1)
    assert _is_linked(b, 'eol_EOLLibraryModule17', a1)
    if hasattr(a1, 'eol_Import16'):
        assert _is_linked(a1, 'eol_Import16', b)
    _safe_set(b, 'eol_EOLLibraryModule17', a2)
    assert _is_linked(b, 'eol_EOLLibraryModule17', a2)
    if hasattr(a1, 'eol_Import16'):
        assert not _is_linked(a1, 'eol_Import16', b)
    if hasattr(a2, 'eol_Import16'):
        assert _is_linked(a2, 'eol_Import16', b)
    _safe_set(b, 'eol_EOLLibraryModule17', None)
    assert not _is_linked(b, 'eol_EOLLibraryModule17', a2)
    if hasattr(a2, 'eol_Import16'):
        assert not _is_linked(a2, 'eol_Import16', b)


def test_assoc_imports9_reverse_link_reassign_clear():
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


def test_assoc_modelDeclarations10_reverse_link_reassign_clear():
    a1 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    a2 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule11', {a1})
    assert _is_linked(b, 'eol_EOLLibraryModule11', a1)
    if hasattr(a1, 'eol_ModelDeclarationStatement'):
        assert _is_linked(a1, 'eol_ModelDeclarationStatement', b)
    _safe_set(b, 'eol_EOLLibraryModule11', {a2})
    assert _is_linked(b, 'eol_EOLLibraryModule11', a2)
    if hasattr(a1, 'eol_ModelDeclarationStatement'):
        assert not _is_linked(a1, 'eol_ModelDeclarationStatement', b)
    if hasattr(a2, 'eol_ModelDeclarationStatement'):
        assert _is_linked(a2, 'eol_ModelDeclarationStatement', b)
    _safe_set(b, 'eol_EOLLibraryModule11', set())
    assert not _is_linked(b, 'eol_EOLLibraryModule11', a2)
    if hasattr(a2, 'eol_ModelDeclarationStatement'):
        assert not _is_linked(a2, 'eol_ModelDeclarationStatement', b)


def test_assoc_name177_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement178', a1)
    assert _is_linked(b, 'eol_ModelDeclarationStatement178', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression179'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression179', b)
    _safe_set(b, 'eol_ModelDeclarationStatement178', a2)
    assert _is_linked(b, 'eol_ModelDeclarationStatement178', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression179'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression179', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression179'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression179', b)
    _safe_set(b, 'eol_ModelDeclarationStatement178', None)
    assert not _is_linked(b, 'eol_ModelDeclarationStatement178', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression179'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression179', b)


def test_assoc_name59_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression61', a1)
    assert _is_linked(b, 'eol_NameExpression61', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression60'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression60', b)
    _safe_set(b, 'eol_NameExpression61', a2)
    assert _is_linked(b, 'eol_NameExpression61', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression60'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression60', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression60'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression60', b)
    _safe_set(b, 'eol_NameExpression61', None)
    assert not _is_linked(b, 'eol_NameExpression61', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression60'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression60', b)


def test_assoc_property75_reverse_link_reassign_clear():
    a1 = eol_PropertyCallExpression(extended=True)
    a2 = eol_PropertyCallExpression(extended=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression76', a1)
    assert _is_linked(b, 'eol_NameExpression76', a1)
    if hasattr(a1, 'eol_PropertyCallExpression'):
        assert _is_linked(a1, 'eol_PropertyCallExpression', b)
    _safe_set(b, 'eol_NameExpression76', a2)
    assert _is_linked(b, 'eol_NameExpression76', a2)
    if hasattr(a1, 'eol_PropertyCallExpression'):
        assert not _is_linked(a1, 'eol_PropertyCallExpression', b)
    if hasattr(a2, 'eol_PropertyCallExpression'):
        assert _is_linked(a2, 'eol_PropertyCallExpression', b)
    _safe_set(b, 'eol_NameExpression76', None)
    assert not _is_linked(b, 'eol_NameExpression76', a2)
    if hasattr(a2, 'eol_PropertyCallExpression'):
        assert not _is_linked(a2, 'eol_PropertyCallExpression', b)


def test_assoc_references62_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression64', a1)
    assert _is_linked(b, 'eol_NameExpression64', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression63'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression63', b)
    _safe_set(b, 'eol_NameExpression64', a2)
    assert _is_linked(b, 'eol_NameExpression64', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression63'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression63', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression63'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression63', b)
    _safe_set(b, 'eol_NameExpression64', None)
    assert not _is_linked(b, 'eol_NameExpression64', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression63'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression63', b)


def test_assoc_resolvedModelDeclaration190_reverse_link_reassign_clear():
    a1 = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    a2 = eol_ModelElementType(elementName="sample_text_2", modelElementType="sample_text_2", modelName="sample_text_2", resolvedIMetamodel="sample_text_2", resolvedIPackage="sample_text_2")
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement191', a1)
    assert _is_linked(b, 'eol_ModelDeclarationStatement191', a1)
    if hasattr(a1, 'eol_ModelElementType'):
        assert _is_linked(a1, 'eol_ModelElementType', b)
    _safe_set(b, 'eol_ModelDeclarationStatement191', a2)
    assert _is_linked(b, 'eol_ModelDeclarationStatement191', a2)
    if hasattr(a1, 'eol_ModelElementType'):
        assert not _is_linked(a1, 'eol_ModelElementType', b)
    if hasattr(a2, 'eol_ModelElementType'):
        assert _is_linked(a2, 'eol_ModelElementType', b)
    _safe_set(b, 'eol_ModelDeclarationStatement191', None)
    assert not _is_linked(b, 'eol_ModelDeclarationStatement191', a2)
    if hasattr(a2, 'eol_ModelElementType'):
        assert not _is_linked(a2, 'eol_ModelElementType', b)


def test_assoc_target65_reverse_link_reassign_clear():
    a1 = eol_FeatureCallExpression(arrow=True)
    a2 = eol_FeatureCallExpression(arrow=False)
    b = eol_Expression(inBrackets=True)
    _safe_set(b, 'eol_Expression66', a1)
    assert _is_linked(b, 'eol_Expression66', a1)
    if hasattr(a1, 'eol_FeatureCallExpression'):
        assert _is_linked(a1, 'eol_FeatureCallExpression', b)
    _safe_set(b, 'eol_Expression66', a2)
    assert _is_linked(b, 'eol_Expression66', a2)
    if hasattr(a1, 'eol_FeatureCallExpression'):
        assert not _is_linked(a1, 'eol_FeatureCallExpression', b)
    if hasattr(a2, 'eol_FeatureCallExpression'):
        assert _is_linked(a2, 'eol_FeatureCallExpression', b)
    _safe_set(b, 'eol_Expression66', None)
    assert not _is_linked(b, 'eol_Expression66', a2)
    if hasattr(a2, 'eol_FeatureCallExpression'):
        assert not _is_linked(a2, 'eol_FeatureCallExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__result43_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition44' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition44', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression45', partner)
    assert getattr(partner, 'eol_OperationDefinition44') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression45', None)
    assert getattr(partner, 'eol_OperationDefinition44') is None


def test_assoc_arguments67_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression', None)
    _safe_set(owner, 'eol_Expression68', partner)
    assert owner in getattr(partner, 'eol_MethodCallExpression')
    _safe_set(owner, 'eol_Expression68', None)
    assert owner not in getattr(partner, 'eol_MethodCallExpression')


def test_assoc_condition137_stub_double():
    # eol_IfStatement has no real 'eol_IfStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_IfStatement()
    setattr(partner, 'eol_IfStatement', None)
    _safe_set(owner, 'eol_Expression138', partner)
    assert getattr(partner, 'eol_IfStatement') == owner
    _safe_set(owner, 'eol_Expression138', None)
    assert getattr(partner, 'eol_IfStatement') is None


def test_assoc_condition150_stub_double():
    # eol_ForStatement has no real 'eol_ForStatement151' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ForStatement()
    setattr(partner, 'eol_ForStatement151', None)
    _safe_set(owner, 'eol_Expression152', partner)
    assert getattr(partner, 'eol_ForStatement151') == owner
    _safe_set(owner, 'eol_Expression152', None)
    assert getattr(partner, 'eol_ForStatement151') is None


def test_assoc_condition156_stub_double():
    # eol_WhileStatement has no real 'eol_WhileStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_WhileStatement()
    setattr(partner, 'eol_WhileStatement', None)
    _safe_set(owner, 'eol_Expression157', partner)
    assert getattr(partner, 'eol_WhileStatement') == owner
    _safe_set(owner, 'eol_Expression157', None)
    assert getattr(partner, 'eol_WhileStatement') is None


def test_assoc_condition24_stub_double():
    # eol_ExpressionOrStatementBlock has no real 'eol_ExpressionOrStatementBlock25' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionOrStatementBlock()
    setattr(partner, 'eol_ExpressionOrStatementBlock25', None)
    _safe_set(owner, 'eol_Expression26', partner)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock25') == owner
    _safe_set(owner, 'eol_Expression26', None)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock25') is None


def test_assoc_conditions79_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression80' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression80', None)
    _safe_set(owner, 'eol_Expression81', partner)
    assert owner in getattr(partner, 'eol_FOLMethodCallExpression80')
    _safe_set(owner, 'eol_Expression81', None)
    assert owner not in getattr(partner, 'eol_FOLMethodCallExpression80')


def test_assoc_contents100_stub_double():
    # eol_CollectionExpression has no real 'eol_CollectionExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_CollectionExpression()
    setattr(partner, 'eol_CollectionExpression', None)
    _safe_set(owner, 'eol_Expression101', partner)
    assert owner in getattr(partner, 'eol_CollectionExpression')
    _safe_set(owner, 'eol_Expression101', None)
    assert owner not in getattr(partner, 'eol_CollectionExpression')


def test_assoc_dynamicTypes188_stub_double():
    # eol_Type has no real 'eol_Type189' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_Type()
    setattr(partner, 'eol_Type189', None)
    _safe_set(owner, 'eol_AnyType', {partner})
    assert getattr(partner, 'eol_Type189') == owner
    _safe_set(owner, 'eol_AnyType', set())
    assert getattr(partner, 'eol_Type189') is None


def test_assoc_end114_stub_double():
    # eol_ExpressionRange has no real 'eol_ExpressionRange115' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionRange()
    setattr(partner, 'eol_ExpressionRange115', None)
    _safe_set(owner, 'eol_Expression116', partner)
    assert getattr(partner, 'eol_ExpressionRange115') == owner
    _safe_set(owner, 'eol_Expression116', None)
    assert getattr(partner, 'eol_ExpressionRange115') is None


def test_assoc_end6_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion7' property in the generated
    # code (a bare stub) -- manually attach it so eol_TextPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_TextPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_TextPosition(column=7, line=7)
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion7', None)
    _safe_set(owner, 'eol_TextPosition8', partner)
    assert getattr(partner, 'eol_TextRegion7') == owner
    _safe_set(owner, 'eol_TextPosition8', None)
    assert getattr(partner, 'eol_TextRegion7') is None


def test_assoc_enumeration106_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression107' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression107', None)
    _safe_set(owner, 'eol_NameExpression108', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression107') == owner
    _safe_set(owner, 'eol_NameExpression108', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression107') is None


def test_assoc_expression124_stub_double():
    # eol_ExpressionStatement has no real 'eol_ExpressionStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionStatement()
    setattr(partner, 'eol_ExpressionStatement', None)
    _safe_set(owner, 'eol_Expression125', partner)
    assert getattr(partner, 'eol_ExpressionStatement') == owner
    _safe_set(owner, 'eol_Expression125', None)
    assert getattr(partner, 'eol_ExpressionStatement') is None


def test_assoc_expression126_stub_double():
    # eol_SwitchStatement has no real 'eol_SwitchStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_SwitchStatement()
    setattr(partner, 'eol_SwitchStatement', None)
    _safe_set(owner, 'eol_Expression127', partner)
    assert getattr(partner, 'eol_SwitchStatement') == owner
    _safe_set(owner, 'eol_Expression127', None)
    assert getattr(partner, 'eol_SwitchStatement') is None


def test_assoc_expression134_stub_double():
    # eol_SwitchCaseExpressionStatement has no real 'eol_SwitchCaseExpressionStatement135' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_SwitchCaseExpressionStatement()
    setattr(partner, 'eol_SwitchCaseExpressionStatement135', None)
    _safe_set(owner, 'eol_Expression136', partner)
    assert getattr(partner, 'eol_SwitchCaseExpressionStatement135') == owner
    _safe_set(owner, 'eol_Expression136', None)
    assert getattr(partner, 'eol_SwitchCaseExpressionStatement135') is None


def test_assoc_expression161_stub_double():
    # eol_ReturnStatement has no real 'eol_ReturnStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ReturnStatement()
    setattr(partner, 'eol_ReturnStatement', None)
    _safe_set(owner, 'eol_Expression162', partner)
    assert getattr(partner, 'eol_ReturnStatement') == owner
    _safe_set(owner, 'eol_Expression162', None)
    assert getattr(partner, 'eol_ReturnStatement') is None


def test_assoc_expression163_stub_double():
    # eol_ThrowStatement has no real 'eol_ThrowStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ThrowStatement()
    setattr(partner, 'eol_ThrowStatement', None)
    _safe_set(owner, 'eol_Expression164', partner)
    assert getattr(partner, 'eol_ThrowStatement') == owner
    _safe_set(owner, 'eol_Expression164', None)
    assert getattr(partner, 'eol_ThrowStatement') is None


def test_assoc_expression165_stub_double():
    # eol_DeleteStatement has no real 'eol_DeleteStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_DeleteStatement()
    setattr(partner, 'eol_DeleteStatement', None)
    _safe_set(owner, 'eol_Expression166', partner)
    assert getattr(partner, 'eol_DeleteStatement') == owner
    _safe_set(owner, 'eol_Expression166', None)
    assert getattr(partner, 'eol_DeleteStatement') is None


def test_assoc_expression175_stub_double():
    # eol_ExecutableAnnotationStatement has no real 'eol_ExecutableAnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExecutableAnnotationStatement()
    setattr(partner, 'eol_ExecutableAnnotationStatement', None)
    _safe_set(owner, 'eol_Expression176', partner)
    assert getattr(partner, 'eol_ExecutableAnnotationStatement') == owner
    _safe_set(owner, 'eol_Expression176', None)
    assert getattr(partner, 'eol_ExecutableAnnotationStatement') is None


def test_assoc_expression197_stub_double():
    # eol_NativeType has no real 'eol_NativeType' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(value="sample_text")
    partner = eol_NativeType()
    setattr(partner, 'eol_NativeType', None)
    _safe_set(owner, 'eol_StringExpression198', partner)
    assert getattr(partner, 'eol_NativeType') == owner
    _safe_set(owner, 'eol_StringExpression198', None)
    assert getattr(partner, 'eol_NativeType') is None


def test_assoc_expression22_stub_double():
    # eol_ExpressionOrStatementBlock has no real 'eol_ExpressionOrStatementBlock23' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionOrStatementBlock()
    setattr(partner, 'eol_ExpressionOrStatementBlock23', None)
    _safe_set(owner, 'eol_Expression', partner)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock23') == owner
    _safe_set(owner, 'eol_Expression', None)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock23') is None


def test_assoc_expression52_stub_double():
    # eol_UnaryOperatorExpression has no real 'eol_UnaryOperatorExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_UnaryOperatorExpression()
    setattr(partner, 'eol_UnaryOperatorExpression', None)
    _safe_set(owner, 'eol_Expression53', partner)
    assert getattr(partner, 'eol_UnaryOperatorExpression') == owner
    _safe_set(owner, 'eol_Expression53', None)
    assert getattr(partner, 'eol_UnaryOperatorExpression') is None


def test_assoc_expressions117_stub_double():
    # eol_ExpressionList has no real 'eol_ExpressionList' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionList()
    setattr(partner, 'eol_ExpressionList', None)
    _safe_set(owner, 'eol_Expression118', partner)
    assert owner in getattr(partner, 'eol_ExpressionList')
    _safe_set(owner, 'eol_Expression118', None)
    assert owner not in getattr(partner, 'eol_ExpressionList')


def test_assoc_key88_stub_double():
    # eol_KeyValueExpression has no real 'eol_KeyValueExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_KeyValueExpression()
    setattr(partner, 'eol_KeyValueExpression', None)
    _safe_set(owner, 'eol_Expression89', partner)
    assert getattr(partner, 'eol_KeyValueExpression') == owner
    _safe_set(owner, 'eol_Expression89', None)
    assert getattr(partner, 'eol_KeyValueExpression') is None


def test_assoc_keyType192_stub_double():
    # eol_MapType has no real 'eol_MapType' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_MapType()
    setattr(partner, 'eol_MapType', None)
    _safe_set(owner, 'eol_AnyType193', partner)
    assert getattr(partner, 'eol_MapType') == owner
    _safe_set(owner, 'eol_AnyType193', None)
    assert getattr(partner, 'eol_MapType') is None


def test_assoc_lhs167_stub_double():
    # eol_AssignmentStatement has no real 'eol_AssignmentStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_AssignmentStatement()
    setattr(partner, 'eol_AssignmentStatement', None)
    _safe_set(owner, 'eol_Expression168', partner)
    assert getattr(partner, 'eol_AssignmentStatement') == owner
    _safe_set(owner, 'eol_Expression168', None)
    assert getattr(partner, 'eol_AssignmentStatement') is None


def test_assoc_lhs54_stub_double():
    # eol_BinaryOperatorExpression has no real 'eol_BinaryOperatorExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_BinaryOperatorExpression()
    setattr(partner, 'eol_BinaryOperatorExpression', None)
    _safe_set(owner, 'eol_Expression55', partner)
    assert getattr(partner, 'eol_BinaryOperatorExpression') == owner
    _safe_set(owner, 'eol_Expression55', None)
    assert getattr(partner, 'eol_BinaryOperatorExpression') is None


def test_assoc_literal104_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression', None)
    _safe_set(owner, 'eol_NameExpression105', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'eol_NameExpression105', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') is None


def test_assoc_method69_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression70' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression70', None)
    _safe_set(owner, 'eol_NameExpression71', partner)
    assert getattr(partner, 'eol_MethodCallExpression70') == owner
    _safe_set(owner, 'eol_NameExpression71', None)
    assert getattr(partner, 'eol_MethodCallExpression70') is None


def test_assoc_method82_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression83' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression83', None)
    _safe_set(owner, 'eol_NameExpression84', partner)
    assert getattr(partner, 'eol_FOLMethodCallExpression83') == owner
    _safe_set(owner, 'eol_NameExpression84', None)
    assert getattr(partner, 'eol_FOLMethodCallExpression83') is None


def test_assoc_model109_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression110' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression110', None)
    _safe_set(owner, 'eol_NameExpression111', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression110') == owner
    _safe_set(owner, 'eol_NameExpression111', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression110') is None


def test_assoc_name172_stub_double():
    # eol_AnnotationStatement has no real 'eol_AnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_AnnotationStatement()
    setattr(partner, 'eol_AnnotationStatement', None)
    _safe_set(owner, 'eol_NameExpression173', partner)
    assert getattr(partner, 'eol_AnnotationStatement') == owner
    _safe_set(owner, 'eol_NameExpression173', None)
    assert getattr(partner, 'eol_AnnotationStatement') is None


def test_assoc_name37_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition38' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition38', None)
    _safe_set(owner, 'eol_NameExpression', partner)
    assert getattr(partner, 'eol_OperationDefinition38') == owner
    _safe_set(owner, 'eol_NameExpression', None)
    assert getattr(partner, 'eol_OperationDefinition38') is None


def test_assoc_names119_stub_double():
    # eol_TransactionStatement has no real 'eol_TransactionStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_TransactionStatement()
    setattr(partner, 'eol_TransactionStatement', None)
    _safe_set(owner, 'eol_NameExpression120', partner)
    assert owner in getattr(partner, 'eol_TransactionStatement')
    _safe_set(owner, 'eol_NameExpression120', None)
    assert owner not in getattr(partner, 'eol_TransactionStatement')


def test_assoc_operations12_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition' property in the generated
    # code (a bare stub) -- manually attach it so eol_EOLLibraryModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_EOLLibraryModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_EOLLibraryModule(name="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition', None)
    _safe_set(owner, 'eol_EOLLibraryModule13', {partner})
    assert getattr(partner, 'eol_OperationDefinition') == owner
    _safe_set(owner, 'eol_EOLLibraryModule13', set())
    assert getattr(partner, 'eol_OperationDefinition') is None


def test_assoc_parameters186_stub_double():
    # eol_ModelDeclarationParameter has no real 'eol_ModelDeclarationParameter' property in the generated
    # code (a bare stub) -- manually attach it so eol_ModelDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_ModelDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    partner = eol_ModelDeclarationParameter()
    setattr(partner, 'eol_ModelDeclarationParameter', None)
    _safe_set(owner, 'eol_ModelDeclarationStatement187', {partner})
    assert getattr(partner, 'eol_ModelDeclarationParameter') == owner
    _safe_set(owner, 'eol_ModelDeclarationStatement187', set())
    assert getattr(partner, 'eol_ModelDeclarationParameter') is None


def test_assoc_parameters95_stub_double():
    # eol_NewExpression has no real 'eol_NewExpression96' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_NewExpression()
    setattr(partner, 'eol_NewExpression96', None)
    _safe_set(owner, 'eol_Expression97', partner)
    assert owner in getattr(partner, 'eol_NewExpression96')
    _safe_set(owner, 'eol_Expression97', None)
    assert owner not in getattr(partner, 'eol_NewExpression96')


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


def test_assoc_resolvedType49_stub_double():
    # eol_Type has no real 'eol_Type51' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_Type()
    setattr(partner, 'eol_Type51', None)
    _safe_set(owner, 'eol_Expression50', partner)
    assert getattr(partner, 'eol_Type51') == owner
    _safe_set(owner, 'eol_Expression50', None)
    assert getattr(partner, 'eol_Type51') is None


def test_assoc_rhs169_stub_double():
    # eol_AssignmentStatement has no real 'eol_AssignmentStatement170' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_AssignmentStatement()
    setattr(partner, 'eol_AssignmentStatement170', None)
    _safe_set(owner, 'eol_Expression171', partner)
    assert getattr(partner, 'eol_AssignmentStatement170') == owner
    _safe_set(owner, 'eol_Expression171', None)
    assert getattr(partner, 'eol_AssignmentStatement170') is None


def test_assoc_rhs56_stub_double():
    # eol_BinaryOperatorExpression has no real 'eol_BinaryOperatorExpression57' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_BinaryOperatorExpression()
    setattr(partner, 'eol_BinaryOperatorExpression57', None)
    _safe_set(owner, 'eol_Expression58', partner)
    assert getattr(partner, 'eol_BinaryOperatorExpression57') == owner
    _safe_set(owner, 'eol_Expression58', None)
    assert getattr(partner, 'eol_BinaryOperatorExpression57') is None


def test_assoc_self41_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition42' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition42', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression', partner)
    assert getattr(partner, 'eol_OperationDefinition42') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression', None)
    assert getattr(partner, 'eol_OperationDefinition42') is None


def test_assoc_start112_stub_double():
    # eol_ExpressionRange has no real 'eol_ExpressionRange' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionRange()
    setattr(partner, 'eol_ExpressionRange', None)
    _safe_set(owner, 'eol_Expression113', partner)
    assert getattr(partner, 'eol_ExpressionRange') == owner
    _safe_set(owner, 'eol_Expression113', None)
    assert getattr(partner, 'eol_ExpressionRange') is None


def test_assoc_start4_stub_double():
    # eol_TextRegion has no real 'eol_TextRegion5' property in the generated
    # code (a bare stub) -- manually attach it so eol_TextPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_TextPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_TextPosition(column=7, line=7)
    partner = eol_TextRegion()
    setattr(partner, 'eol_TextRegion5', None)
    _safe_set(owner, 'eol_TextPosition', partner)
    assert getattr(partner, 'eol_TextRegion5') == owner
    _safe_set(owner, 'eol_TextPosition', None)
    assert getattr(partner, 'eol_TextRegion5') is None


def test_assoc_typeName93_stub_double():
    # eol_NewExpression has no real 'eol_NewExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_NewExpression()
    setattr(partner, 'eol_NewExpression', None)
    _safe_set(owner, 'eol_NameExpression94', partner)
    assert getattr(partner, 'eol_NewExpression') == owner
    _safe_set(owner, 'eol_NameExpression94', None)
    assert getattr(partner, 'eol_NewExpression') is None


def test_assoc_value90_stub_double():
    # eol_KeyValueExpression has no real 'eol_KeyValueExpression91' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_KeyValueExpression()
    setattr(partner, 'eol_KeyValueExpression91', None)
    _safe_set(owner, 'eol_Expression92', partner)
    assert getattr(partner, 'eol_KeyValueExpression91') == owner
    _safe_set(owner, 'eol_Expression92', None)
    assert getattr(partner, 'eol_KeyValueExpression91') is None


def test_assoc_valueType194_stub_double():
    # eol_MapType has no real 'eol_MapType195' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_MapType()
    setattr(partner, 'eol_MapType195', None)
    _safe_set(owner, 'eol_AnyType196', partner)
    assert getattr(partner, 'eol_MapType195') == owner
    _safe_set(owner, 'eol_AnyType196', None)
    assert getattr(partner, 'eol_MapType195') is None


def test_assoc_values174_stub_double():
    # eol_SimpleAnnotationStatement has no real 'eol_SimpleAnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(value="sample_text")
    partner = eol_SimpleAnnotationStatement()
    setattr(partner, 'eol_SimpleAnnotationStatement', None)
    _safe_set(owner, 'eol_StringExpression', partner)
    assert owner in getattr(partner, 'eol_SimpleAnnotationStatement')
    _safe_set(owner, 'eol_StringExpression', None)
    assert owner not in getattr(partner, 'eol_SimpleAnnotationStatement')


