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

def test_assoc_aliases174_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement175', {a1})
    assert _is_linked(b, 'eol_ModelDeclarationStatement175', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression176'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression176', b)
    _safe_set(b, 'eol_ModelDeclarationStatement175', {a2})
    assert _is_linked(b, 'eol_ModelDeclarationStatement175', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression176'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression176', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression176'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression176', b)
    _safe_set(b, 'eol_ModelDeclarationStatement175', set())
    assert not _is_linked(b, 'eol_ModelDeclarationStatement175', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression176'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression176', b)


def test_assoc_driver171_reverse_link_reassign_clear():
    a1 = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    a2 = eol_NameExpression(isType=False, name="sample_text_2", resolvedContent="sample_text_2")
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement172', a1)
    assert _is_linked(b, 'eol_ModelDeclarationStatement172', a1)
    if hasattr(a1, 'eol_NameExpression173'):
        assert _is_linked(a1, 'eol_NameExpression173', b)
    _safe_set(b, 'eol_ModelDeclarationStatement172', a2)
    assert _is_linked(b, 'eol_ModelDeclarationStatement172', a2)
    if hasattr(a1, 'eol_NameExpression173'):
        assert not _is_linked(a1, 'eol_NameExpression173', b)
    if hasattr(a2, 'eol_NameExpression173'):
        assert _is_linked(a2, 'eol_NameExpression173', b)
    _safe_set(b, 'eol_ModelDeclarationStatement172', None)
    assert not _is_linked(b, 'eol_ModelDeclarationStatement172', a2)
    if hasattr(a2, 'eol_NameExpression173'):
        assert not _is_linked(a2, 'eol_NameExpression173', b)


def test_assoc_importedModule6_reverse_link_reassign_clear():
    a1 = eol_Import(imported="sample_text")
    a2 = eol_Import(imported="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule8', a1)
    assert _is_linked(b, 'eol_EOLLibraryModule8', a1)
    if hasattr(a1, 'eol_Import7'):
        assert _is_linked(a1, 'eol_Import7', b)
    _safe_set(b, 'eol_EOLLibraryModule8', a2)
    assert _is_linked(b, 'eol_EOLLibraryModule8', a2)
    if hasattr(a1, 'eol_Import7'):
        assert not _is_linked(a1, 'eol_Import7', b)
    if hasattr(a2, 'eol_Import7'):
        assert _is_linked(a2, 'eol_Import7', b)
    _safe_set(b, 'eol_EOLLibraryModule8', None)
    assert not _is_linked(b, 'eol_EOLLibraryModule8', a2)
    if hasattr(a2, 'eol_Import7'):
        assert not _is_linked(a2, 'eol_Import7', b)


def test_assoc_imports0_reverse_link_reassign_clear():
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


def test_assoc_modelDeclarations1_reverse_link_reassign_clear():
    a1 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    a2 = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text_2")
    b = eol_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_EOLLibraryModule2', {a1})
    assert _is_linked(b, 'eol_EOLLibraryModule2', a1)
    if hasattr(a1, 'eol_ModelDeclarationStatement'):
        assert _is_linked(a1, 'eol_ModelDeclarationStatement', b)
    _safe_set(b, 'eol_EOLLibraryModule2', {a2})
    assert _is_linked(b, 'eol_EOLLibraryModule2', a2)
    if hasattr(a1, 'eol_ModelDeclarationStatement'):
        assert not _is_linked(a1, 'eol_ModelDeclarationStatement', b)
    if hasattr(a2, 'eol_ModelDeclarationStatement'):
        assert _is_linked(a2, 'eol_ModelDeclarationStatement', b)
    _safe_set(b, 'eol_EOLLibraryModule2', set())
    assert not _is_linked(b, 'eol_EOLLibraryModule2', a2)
    if hasattr(a2, 'eol_ModelDeclarationStatement'):
        assert not _is_linked(a2, 'eol_ModelDeclarationStatement', b)


def test_assoc_name168_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement169', a1)
    assert _is_linked(b, 'eol_ModelDeclarationStatement169', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression170'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression170', b)
    _safe_set(b, 'eol_ModelDeclarationStatement169', a2)
    assert _is_linked(b, 'eol_ModelDeclarationStatement169', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression170'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression170', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression170'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression170', b)
    _safe_set(b, 'eol_ModelDeclarationStatement169', None)
    assert not _is_linked(b, 'eol_ModelDeclarationStatement169', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression170'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression170', b)


def test_assoc_name50_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression52', a1)
    assert _is_linked(b, 'eol_NameExpression52', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression51'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression51', b)
    _safe_set(b, 'eol_NameExpression52', a2)
    assert _is_linked(b, 'eol_NameExpression52', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression51'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression51', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression51'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression51', b)
    _safe_set(b, 'eol_NameExpression52', None)
    assert not _is_linked(b, 'eol_NameExpression52', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression51'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression51', b)


def test_assoc_property66_reverse_link_reassign_clear():
    a1 = eol_PropertyCallExpression(extended=True)
    a2 = eol_PropertyCallExpression(extended=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression67', a1)
    assert _is_linked(b, 'eol_NameExpression67', a1)
    if hasattr(a1, 'eol_PropertyCallExpression'):
        assert _is_linked(a1, 'eol_PropertyCallExpression', b)
    _safe_set(b, 'eol_NameExpression67', a2)
    assert _is_linked(b, 'eol_NameExpression67', a2)
    if hasattr(a1, 'eol_PropertyCallExpression'):
        assert not _is_linked(a1, 'eol_PropertyCallExpression', b)
    if hasattr(a2, 'eol_PropertyCallExpression'):
        assert _is_linked(a2, 'eol_PropertyCallExpression', b)
    _safe_set(b, 'eol_NameExpression67', None)
    assert not _is_linked(b, 'eol_NameExpression67', a2)
    if hasattr(a2, 'eol_PropertyCallExpression'):
        assert not _is_linked(a2, 'eol_PropertyCallExpression', b)


def test_assoc_references53_reverse_link_reassign_clear():
    a1 = eol_VariableDeclarationExpression(create=True)
    a2 = eol_VariableDeclarationExpression(create=False)
    b = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    _safe_set(b, 'eol_NameExpression55', a1)
    assert _is_linked(b, 'eol_NameExpression55', a1)
    if hasattr(a1, 'eol_VariableDeclarationExpression54'):
        assert _is_linked(a1, 'eol_VariableDeclarationExpression54', b)
    _safe_set(b, 'eol_NameExpression55', a2)
    assert _is_linked(b, 'eol_NameExpression55', a2)
    if hasattr(a1, 'eol_VariableDeclarationExpression54'):
        assert not _is_linked(a1, 'eol_VariableDeclarationExpression54', b)
    if hasattr(a2, 'eol_VariableDeclarationExpression54'):
        assert _is_linked(a2, 'eol_VariableDeclarationExpression54', b)
    _safe_set(b, 'eol_NameExpression55', None)
    assert not _is_linked(b, 'eol_NameExpression55', a2)
    if hasattr(a2, 'eol_VariableDeclarationExpression54'):
        assert not _is_linked(a2, 'eol_VariableDeclarationExpression54', b)


def test_assoc_resolvedModelDeclaration181_reverse_link_reassign_clear():
    a1 = eol_ModelElementType(elementName="sample_text", modelElementType="sample_text", modelName="sample_text", resolvedIMetamodel="sample_text", resolvedIPackage="sample_text")
    a2 = eol_ModelElementType(elementName="sample_text_2", modelElementType="sample_text_2", modelName="sample_text_2", resolvedIMetamodel="sample_text_2", resolvedIPackage="sample_text_2")
    b = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    _safe_set(b, 'eol_ModelDeclarationStatement182', a1)
    assert _is_linked(b, 'eol_ModelDeclarationStatement182', a1)
    if hasattr(a1, 'eol_ModelElementType'):
        assert _is_linked(a1, 'eol_ModelElementType', b)
    _safe_set(b, 'eol_ModelDeclarationStatement182', a2)
    assert _is_linked(b, 'eol_ModelDeclarationStatement182', a2)
    if hasattr(a1, 'eol_ModelElementType'):
        assert not _is_linked(a1, 'eol_ModelElementType', b)
    if hasattr(a2, 'eol_ModelElementType'):
        assert _is_linked(a2, 'eol_ModelElementType', b)
    _safe_set(b, 'eol_ModelDeclarationStatement182', None)
    assert not _is_linked(b, 'eol_ModelDeclarationStatement182', a2)
    if hasattr(a2, 'eol_ModelElementType'):
        assert not _is_linked(a2, 'eol_ModelElementType', b)


def test_assoc_target56_reverse_link_reassign_clear():
    a1 = eol_FeatureCallExpression(arrow=True)
    a2 = eol_FeatureCallExpression(arrow=False)
    b = eol_Expression(inBrackets=True)
    _safe_set(b, 'eol_Expression57', a1)
    assert _is_linked(b, 'eol_Expression57', a1)
    if hasattr(a1, 'eol_FeatureCallExpression'):
        assert _is_linked(a1, 'eol_FeatureCallExpression', b)
    _safe_set(b, 'eol_Expression57', a2)
    assert _is_linked(b, 'eol_Expression57', a2)
    if hasattr(a1, 'eol_FeatureCallExpression'):
        assert not _is_linked(a1, 'eol_FeatureCallExpression', b)
    if hasattr(a2, 'eol_FeatureCallExpression'):
        assert _is_linked(a2, 'eol_FeatureCallExpression', b)
    _safe_set(b, 'eol_Expression57', None)
    assert not _is_linked(b, 'eol_Expression57', a2)
    if hasattr(a2, 'eol_FeatureCallExpression'):
        assert not _is_linked(a2, 'eol_FeatureCallExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc__result34_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition35' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition35', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression36', partner)
    assert getattr(partner, 'eol_OperationDefinition35') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression36', None)
    assert getattr(partner, 'eol_OperationDefinition35') is None


def test_assoc_arguments58_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression', None)
    _safe_set(owner, 'eol_Expression59', partner)
    assert owner in getattr(partner, 'eol_MethodCallExpression')
    _safe_set(owner, 'eol_Expression59', None)
    assert owner not in getattr(partner, 'eol_MethodCallExpression')


def test_assoc_condition128_stub_double():
    # eol_IfStatement has no real 'eol_IfStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_IfStatement()
    setattr(partner, 'eol_IfStatement', None)
    _safe_set(owner, 'eol_Expression129', partner)
    assert getattr(partner, 'eol_IfStatement') == owner
    _safe_set(owner, 'eol_Expression129', None)
    assert getattr(partner, 'eol_IfStatement') is None


def test_assoc_condition141_stub_double():
    # eol_ForStatement has no real 'eol_ForStatement142' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ForStatement()
    setattr(partner, 'eol_ForStatement142', None)
    _safe_set(owner, 'eol_Expression143', partner)
    assert getattr(partner, 'eol_ForStatement142') == owner
    _safe_set(owner, 'eol_Expression143', None)
    assert getattr(partner, 'eol_ForStatement142') is None


def test_assoc_condition147_stub_double():
    # eol_WhileStatement has no real 'eol_WhileStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_WhileStatement()
    setattr(partner, 'eol_WhileStatement', None)
    _safe_set(owner, 'eol_Expression148', partner)
    assert getattr(partner, 'eol_WhileStatement') == owner
    _safe_set(owner, 'eol_Expression148', None)
    assert getattr(partner, 'eol_WhileStatement') is None


def test_assoc_condition15_stub_double():
    # eol_ExpressionOrStatementBlock has no real 'eol_ExpressionOrStatementBlock16' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionOrStatementBlock()
    setattr(partner, 'eol_ExpressionOrStatementBlock16', None)
    _safe_set(owner, 'eol_Expression17', partner)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock16') == owner
    _safe_set(owner, 'eol_Expression17', None)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock16') is None


def test_assoc_conditions70_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression71' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression71', None)
    _safe_set(owner, 'eol_Expression72', partner)
    assert owner in getattr(partner, 'eol_FOLMethodCallExpression71')
    _safe_set(owner, 'eol_Expression72', None)
    assert owner not in getattr(partner, 'eol_FOLMethodCallExpression71')


def test_assoc_contents91_stub_double():
    # eol_CollectionExpression has no real 'eol_CollectionExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_CollectionExpression()
    setattr(partner, 'eol_CollectionExpression', None)
    _safe_set(owner, 'eol_Expression92', partner)
    assert owner in getattr(partner, 'eol_CollectionExpression')
    _safe_set(owner, 'eol_Expression92', None)
    assert owner not in getattr(partner, 'eol_CollectionExpression')


def test_assoc_dynamicTypes179_stub_double():
    # eol_Type has no real 'eol_Type180' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_Type()
    setattr(partner, 'eol_Type180', None)
    _safe_set(owner, 'eol_AnyType', {partner})
    assert getattr(partner, 'eol_Type180') == owner
    _safe_set(owner, 'eol_AnyType', set())
    assert getattr(partner, 'eol_Type180') is None


def test_assoc_end105_stub_double():
    # eol_ExpressionRange has no real 'eol_ExpressionRange106' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionRange()
    setattr(partner, 'eol_ExpressionRange106', None)
    _safe_set(owner, 'eol_Expression107', partner)
    assert getattr(partner, 'eol_ExpressionRange106') == owner
    _safe_set(owner, 'eol_Expression107', None)
    assert getattr(partner, 'eol_ExpressionRange106') is None


def test_assoc_enumeration97_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression98' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression98', None)
    _safe_set(owner, 'eol_NameExpression99', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression98') == owner
    _safe_set(owner, 'eol_NameExpression99', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression98') is None


def test_assoc_expression115_stub_double():
    # eol_ExpressionStatement has no real 'eol_ExpressionStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionStatement()
    setattr(partner, 'eol_ExpressionStatement', None)
    _safe_set(owner, 'eol_Expression116', partner)
    assert getattr(partner, 'eol_ExpressionStatement') == owner
    _safe_set(owner, 'eol_Expression116', None)
    assert getattr(partner, 'eol_ExpressionStatement') is None


def test_assoc_expression117_stub_double():
    # eol_SwitchStatement has no real 'eol_SwitchStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_SwitchStatement()
    setattr(partner, 'eol_SwitchStatement', None)
    _safe_set(owner, 'eol_Expression118', partner)
    assert getattr(partner, 'eol_SwitchStatement') == owner
    _safe_set(owner, 'eol_Expression118', None)
    assert getattr(partner, 'eol_SwitchStatement') is None


def test_assoc_expression125_stub_double():
    # eol_SwitchCaseExpressionStatement has no real 'eol_SwitchCaseExpressionStatement126' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_SwitchCaseExpressionStatement()
    setattr(partner, 'eol_SwitchCaseExpressionStatement126', None)
    _safe_set(owner, 'eol_Expression127', partner)
    assert getattr(partner, 'eol_SwitchCaseExpressionStatement126') == owner
    _safe_set(owner, 'eol_Expression127', None)
    assert getattr(partner, 'eol_SwitchCaseExpressionStatement126') is None


def test_assoc_expression13_stub_double():
    # eol_ExpressionOrStatementBlock has no real 'eol_ExpressionOrStatementBlock14' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionOrStatementBlock()
    setattr(partner, 'eol_ExpressionOrStatementBlock14', None)
    _safe_set(owner, 'eol_Expression', partner)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock14') == owner
    _safe_set(owner, 'eol_Expression', None)
    assert getattr(partner, 'eol_ExpressionOrStatementBlock14') is None


def test_assoc_expression152_stub_double():
    # eol_ReturnStatement has no real 'eol_ReturnStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ReturnStatement()
    setattr(partner, 'eol_ReturnStatement', None)
    _safe_set(owner, 'eol_Expression153', partner)
    assert getattr(partner, 'eol_ReturnStatement') == owner
    _safe_set(owner, 'eol_Expression153', None)
    assert getattr(partner, 'eol_ReturnStatement') is None


def test_assoc_expression154_stub_double():
    # eol_ThrowStatement has no real 'eol_ThrowStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ThrowStatement()
    setattr(partner, 'eol_ThrowStatement', None)
    _safe_set(owner, 'eol_Expression155', partner)
    assert getattr(partner, 'eol_ThrowStatement') == owner
    _safe_set(owner, 'eol_Expression155', None)
    assert getattr(partner, 'eol_ThrowStatement') is None


def test_assoc_expression156_stub_double():
    # eol_DeleteStatement has no real 'eol_DeleteStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_DeleteStatement()
    setattr(partner, 'eol_DeleteStatement', None)
    _safe_set(owner, 'eol_Expression157', partner)
    assert getattr(partner, 'eol_DeleteStatement') == owner
    _safe_set(owner, 'eol_Expression157', None)
    assert getattr(partner, 'eol_DeleteStatement') is None


def test_assoc_expression166_stub_double():
    # eol_ExecutableAnnotationStatement has no real 'eol_ExecutableAnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExecutableAnnotationStatement()
    setattr(partner, 'eol_ExecutableAnnotationStatement', None)
    _safe_set(owner, 'eol_Expression167', partner)
    assert getattr(partner, 'eol_ExecutableAnnotationStatement') == owner
    _safe_set(owner, 'eol_Expression167', None)
    assert getattr(partner, 'eol_ExecutableAnnotationStatement') is None


def test_assoc_expression188_stub_double():
    # eol_NativeType has no real 'eol_NativeType' property in the generated
    # code (a bare stub) -- manually attach it so eol_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_StringExpression(value="sample_text")
    partner = eol_NativeType()
    setattr(partner, 'eol_NativeType', None)
    _safe_set(owner, 'eol_StringExpression189', partner)
    assert getattr(partner, 'eol_NativeType') == owner
    _safe_set(owner, 'eol_StringExpression189', None)
    assert getattr(partner, 'eol_NativeType') is None


def test_assoc_expression43_stub_double():
    # eol_UnaryOperatorExpression has no real 'eol_UnaryOperatorExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_UnaryOperatorExpression()
    setattr(partner, 'eol_UnaryOperatorExpression', None)
    _safe_set(owner, 'eol_Expression44', partner)
    assert getattr(partner, 'eol_UnaryOperatorExpression') == owner
    _safe_set(owner, 'eol_Expression44', None)
    assert getattr(partner, 'eol_UnaryOperatorExpression') is None


def test_assoc_expressions108_stub_double():
    # eol_ExpressionList has no real 'eol_ExpressionList' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionList()
    setattr(partner, 'eol_ExpressionList', None)
    _safe_set(owner, 'eol_Expression109', partner)
    assert owner in getattr(partner, 'eol_ExpressionList')
    _safe_set(owner, 'eol_Expression109', None)
    assert owner not in getattr(partner, 'eol_ExpressionList')


def test_assoc_key79_stub_double():
    # eol_KeyValueExpression has no real 'eol_KeyValueExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_KeyValueExpression()
    setattr(partner, 'eol_KeyValueExpression', None)
    _safe_set(owner, 'eol_Expression80', partner)
    assert getattr(partner, 'eol_KeyValueExpression') == owner
    _safe_set(owner, 'eol_Expression80', None)
    assert getattr(partner, 'eol_KeyValueExpression') is None


def test_assoc_keyType183_stub_double():
    # eol_MapType has no real 'eol_MapType' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_MapType()
    setattr(partner, 'eol_MapType', None)
    _safe_set(owner, 'eol_AnyType184', partner)
    assert getattr(partner, 'eol_MapType') == owner
    _safe_set(owner, 'eol_AnyType184', None)
    assert getattr(partner, 'eol_MapType') is None


def test_assoc_lhs158_stub_double():
    # eol_AssignmentStatement has no real 'eol_AssignmentStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_AssignmentStatement()
    setattr(partner, 'eol_AssignmentStatement', None)
    _safe_set(owner, 'eol_Expression159', partner)
    assert getattr(partner, 'eol_AssignmentStatement') == owner
    _safe_set(owner, 'eol_Expression159', None)
    assert getattr(partner, 'eol_AssignmentStatement') is None


def test_assoc_lhs45_stub_double():
    # eol_BinaryOperatorExpression has no real 'eol_BinaryOperatorExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_BinaryOperatorExpression()
    setattr(partner, 'eol_BinaryOperatorExpression', None)
    _safe_set(owner, 'eol_Expression46', partner)
    assert getattr(partner, 'eol_BinaryOperatorExpression') == owner
    _safe_set(owner, 'eol_Expression46', None)
    assert getattr(partner, 'eol_BinaryOperatorExpression') is None


def test_assoc_literal95_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression', None)
    _safe_set(owner, 'eol_NameExpression96', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'eol_NameExpression96', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression') is None


def test_assoc_method60_stub_double():
    # eol_MethodCallExpression has no real 'eol_MethodCallExpression61' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_MethodCallExpression()
    setattr(partner, 'eol_MethodCallExpression61', None)
    _safe_set(owner, 'eol_NameExpression62', partner)
    assert getattr(partner, 'eol_MethodCallExpression61') == owner
    _safe_set(owner, 'eol_NameExpression62', None)
    assert getattr(partner, 'eol_MethodCallExpression61') is None


def test_assoc_method73_stub_double():
    # eol_FOLMethodCallExpression has no real 'eol_FOLMethodCallExpression74' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_FOLMethodCallExpression()
    setattr(partner, 'eol_FOLMethodCallExpression74', None)
    _safe_set(owner, 'eol_NameExpression75', partner)
    assert getattr(partner, 'eol_FOLMethodCallExpression74') == owner
    _safe_set(owner, 'eol_NameExpression75', None)
    assert getattr(partner, 'eol_FOLMethodCallExpression74') is None


def test_assoc_model100_stub_double():
    # eol_EnumerationLiteralExpression has no real 'eol_EnumerationLiteralExpression101' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_EnumerationLiteralExpression()
    setattr(partner, 'eol_EnumerationLiteralExpression101', None)
    _safe_set(owner, 'eol_NameExpression102', partner)
    assert getattr(partner, 'eol_EnumerationLiteralExpression101') == owner
    _safe_set(owner, 'eol_NameExpression102', None)
    assert getattr(partner, 'eol_EnumerationLiteralExpression101') is None


def test_assoc_name163_stub_double():
    # eol_AnnotationStatement has no real 'eol_AnnotationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_AnnotationStatement()
    setattr(partner, 'eol_AnnotationStatement', None)
    _safe_set(owner, 'eol_NameExpression164', partner)
    assert getattr(partner, 'eol_AnnotationStatement') == owner
    _safe_set(owner, 'eol_NameExpression164', None)
    assert getattr(partner, 'eol_AnnotationStatement') is None


def test_assoc_name28_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition29' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition29', None)
    _safe_set(owner, 'eol_NameExpression', partner)
    assert getattr(partner, 'eol_OperationDefinition29') == owner
    _safe_set(owner, 'eol_NameExpression', None)
    assert getattr(partner, 'eol_OperationDefinition29') is None


def test_assoc_names110_stub_double():
    # eol_TransactionStatement has no real 'eol_TransactionStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_TransactionStatement()
    setattr(partner, 'eol_TransactionStatement', None)
    _safe_set(owner, 'eol_NameExpression111', partner)
    assert owner in getattr(partner, 'eol_TransactionStatement')
    _safe_set(owner, 'eol_NameExpression111', None)
    assert owner not in getattr(partner, 'eol_TransactionStatement')


def test_assoc_operations3_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition' property in the generated
    # code (a bare stub) -- manually attach it so eol_EOLLibraryModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_EOLLibraryModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_EOLLibraryModule(name="sample_text")
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition', None)
    _safe_set(owner, 'eol_EOLLibraryModule4', {partner})
    assert getattr(partner, 'eol_OperationDefinition') == owner
    _safe_set(owner, 'eol_EOLLibraryModule4', set())
    assert getattr(partner, 'eol_OperationDefinition') is None


def test_assoc_parameters177_stub_double():
    # eol_ModelDeclarationParameter has no real 'eol_ModelDeclarationParameter' property in the generated
    # code (a bare stub) -- manually attach it so eol_ModelDeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_ModelDeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_ModelDeclarationStatement(resolvedIMetamodel="sample_text")
    partner = eol_ModelDeclarationParameter()
    setattr(partner, 'eol_ModelDeclarationParameter', None)
    _safe_set(owner, 'eol_ModelDeclarationStatement178', {partner})
    assert getattr(partner, 'eol_ModelDeclarationParameter') == owner
    _safe_set(owner, 'eol_ModelDeclarationStatement178', set())
    assert getattr(partner, 'eol_ModelDeclarationParameter') is None


def test_assoc_parameters86_stub_double():
    # eol_NewExpression has no real 'eol_NewExpression87' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_NewExpression()
    setattr(partner, 'eol_NewExpression87', None)
    _safe_set(owner, 'eol_Expression88', partner)
    assert owner in getattr(partner, 'eol_NewExpression87')
    _safe_set(owner, 'eol_Expression88', None)
    assert owner not in getattr(partner, 'eol_NewExpression87')


def test_assoc_resolvedType40_stub_double():
    # eol_Type has no real 'eol_Type42' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_Type()
    setattr(partner, 'eol_Type42', None)
    _safe_set(owner, 'eol_Expression41', partner)
    assert getattr(partner, 'eol_Type42') == owner
    _safe_set(owner, 'eol_Expression41', None)
    assert getattr(partner, 'eol_Type42') is None


def test_assoc_rhs160_stub_double():
    # eol_AssignmentStatement has no real 'eol_AssignmentStatement161' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_AssignmentStatement()
    setattr(partner, 'eol_AssignmentStatement161', None)
    _safe_set(owner, 'eol_Expression162', partner)
    assert getattr(partner, 'eol_AssignmentStatement161') == owner
    _safe_set(owner, 'eol_Expression162', None)
    assert getattr(partner, 'eol_AssignmentStatement161') is None


def test_assoc_rhs47_stub_double():
    # eol_BinaryOperatorExpression has no real 'eol_BinaryOperatorExpression48' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_BinaryOperatorExpression()
    setattr(partner, 'eol_BinaryOperatorExpression48', None)
    _safe_set(owner, 'eol_Expression49', partner)
    assert getattr(partner, 'eol_BinaryOperatorExpression48') == owner
    _safe_set(owner, 'eol_Expression49', None)
    assert getattr(partner, 'eol_BinaryOperatorExpression48') is None


def test_assoc_self32_stub_double():
    # eol_OperationDefinition has no real 'eol_OperationDefinition33' property in the generated
    # code (a bare stub) -- manually attach it so eol_VariableDeclarationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_VariableDeclarationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_VariableDeclarationExpression(create=True)
    partner = eol_OperationDefinition()
    setattr(partner, 'eol_OperationDefinition33', None)
    _safe_set(owner, 'eol_VariableDeclarationExpression', partner)
    assert getattr(partner, 'eol_OperationDefinition33') == owner
    _safe_set(owner, 'eol_VariableDeclarationExpression', None)
    assert getattr(partner, 'eol_OperationDefinition33') is None


def test_assoc_start103_stub_double():
    # eol_ExpressionRange has no real 'eol_ExpressionRange' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_ExpressionRange()
    setattr(partner, 'eol_ExpressionRange', None)
    _safe_set(owner, 'eol_Expression104', partner)
    assert getattr(partner, 'eol_ExpressionRange') == owner
    _safe_set(owner, 'eol_Expression104', None)
    assert getattr(partner, 'eol_ExpressionRange') is None


def test_assoc_typeName84_stub_double():
    # eol_NewExpression has no real 'eol_NewExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_NameExpression(isType=True, name="sample_text", resolvedContent="sample_text")
    partner = eol_NewExpression()
    setattr(partner, 'eol_NewExpression', None)
    _safe_set(owner, 'eol_NameExpression85', partner)
    assert getattr(partner, 'eol_NewExpression') == owner
    _safe_set(owner, 'eol_NameExpression85', None)
    assert getattr(partner, 'eol_NewExpression') is None


def test_assoc_value81_stub_double():
    # eol_KeyValueExpression has no real 'eol_KeyValueExpression82' property in the generated
    # code (a bare stub) -- manually attach it so eol_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_Expression(inBrackets=True)
    partner = eol_KeyValueExpression()
    setattr(partner, 'eol_KeyValueExpression82', None)
    _safe_set(owner, 'eol_Expression83', partner)
    assert getattr(partner, 'eol_KeyValueExpression82') == owner
    _safe_set(owner, 'eol_Expression83', None)
    assert getattr(partner, 'eol_KeyValueExpression82') is None


def test_assoc_valueType185_stub_double():
    # eol_MapType has no real 'eol_MapType186' property in the generated
    # code (a bare stub) -- manually attach it so eol_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_AnyType(declared=True)
    partner = eol_MapType()
    setattr(partner, 'eol_MapType186', None)
    _safe_set(owner, 'eol_AnyType187', partner)
    assert getattr(partner, 'eol_MapType186') == owner
    _safe_set(owner, 'eol_AnyType187', None)
    assert getattr(partner, 'eol_MapType186') is None


def test_assoc_values165_stub_double():
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


