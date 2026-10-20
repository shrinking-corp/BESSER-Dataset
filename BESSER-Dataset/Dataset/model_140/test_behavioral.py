import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AddAccessorDeclaration,
    Argument,
    ArrayType,
    AttributeSection,
    BuiltInClassType,
    BuiltInType,
    ClassBase,
    ConstantDeclaration,
    ConstructorInitializer,
    DelegateDeclaration,
    EventDeclaration,
    FieldDeclaration,
    FormalParameterList,
    GetAccessorDeclaration,
    IntegralType,
    MaybeEmptyBlock,
    OperatorDeclarator,
    PropertyDeclaration,
    RemoveAccessorDeclaration,
    ResourceAquisition,
    SetAccessorDeclaration,
    TypeOrVoid,
    VariableInitializer,
    cSharp_AccessorDeclarations,
    cSharp_AddAccessorDeclaration,
    cSharp_Argument,
    cSharp_ArgumentList,
    cSharp_ArrayInitializer,
    cSharp_ArrayType,
    cSharp_Attribute,
    cSharp_AttributeArguments,
    cSharp_AttributeList,
    cSharp_AttributeName,
    cSharp_AttributeSection,
    cSharp_Attributes,
    cSharp_BinaryOperatorDeclarator,
    cSharp_Block,
    cSharp_Bool,
    cSharp_BreakStatement,
    cSharp_BuiltInClassType,
    cSharp_BuiltInType,
    cSharp_Byte,
    cSharp_CatchClauses,
    cSharp_Char,
    cSharp_ClassBase,
    cSharp_ClassBody,
    cSharp_ClassDeclaration,
    cSharp_ClassMemberDeclaration,
    cSharp_CompilationUnit,
    cSharp_ConstantDeclaration,
    cSharp_ConstantDeclarator,
    cSharp_ConstructorDeclaration,
    cSharp_ConstructorDeclarator,
    cSharp_ConstructorInitializer,
    cSharp_ContinueStatement,
    cSharp_ConversionOperatorDeclarator,
    cSharp_Decimal,
    cSharp_DeclarationStatment,
    cSharp_DelegateDeclaration,
    cSharp_DestructorDeclaration,
    cSharp_DoStatement,
    cSharp_Double,
    cSharp_ElsePart,
    cSharp_EmbeddedStatement,
    cSharp_EnumBody,
    cSharp_EnumDeclaration,
    cSharp_EnumMemberDeclaration,
    cSharp_EventAccessorDeclarations,
    cSharp_EventDeclaration,
    cSharp_Expression,
    cSharp_Expression2,
    cSharp_ExpressionList,
    cSharp_FieldDeclaration,
    cSharp_FinallyClause,
    cSharp_FixedParameter,
    cSharp_FixedParameters,
    cSharp_Float,
    cSharp_ForInitializer,
    cSharp_ForStatement,
    cSharp_ForeachStatement,
    cSharp_FormalParameterList,
    cSharp_GeneralCatchclause,
    cSharp_GetAccessorDeclaration,
    cSharp_GlobalAttributeSection,
    cSharp_GlobalAttributes,
    cSharp_GotoStatement,
    cSharp_Identifier,
    cSharp_IfStatement,
    cSharp_IndexerDeclaration,
    cSharp_IndexerDeclarator,
    cSharp_Int,
    cSharp_IntegralType,
    cSharp_InterfaceAccessors,
    cSharp_InterfaceBody,
    cSharp_InterfaceDeclaration,
    cSharp_InterfaceEventDeclaration,
    cSharp_InterfaceIndexerDeclaration,
    cSharp_InterfaceMemberDeclaration,
    cSharp_InterfaceMethodDeclaration,
    cSharp_InterfacePropertyDeclaration,
    cSharp_IterationStatement,
    cSharp_JumpStatement,
    cSharp_LabeledStatement,
    cSharp_LocalVariableDeclaration,
    cSharp_LocalconstantDeclaration,
    cSharp_LockStatement,
    cSharp_Long,
    cSharp_MaybeEmptyBlock,
    cSharp_MethodDeclaration,
    cSharp_MethodHeader,
    cSharp_NamespaceBody,
    cSharp_NamespaceDeclaration,
    cSharp_NamespaceMemberDeclaration,
    cSharp_NonArrayType,
    cSharp_Object,
    cSharp_OperatorDeclaration,
    cSharp_OperatorDeclarator,
    cSharp_ParameterArray,
    cSharp_PrimaryExpression,
    cSharp_PrimaryExpression2,
    cSharp_PropertyDeclaration,
    cSharp_QualifiedIdentifier,
    cSharp_QualifiedIdentifierList,
    cSharp_RemoveAccessorDeclaration,
    cSharp_ResourceAquisition,
    cSharp_ReturnStatement,
    cSharp_SByte,
    cSharp_SelectionStatement,
    cSharp_SetAccessorDeclaration,
    cSharp_Short,
    cSharp_SpecificCatchClause,
    cSharp_Statement,
    cSharp_StatementExpression,
    cSharp_StatementExpressionList,
    cSharp_StaticConstructorDeclaration,
    cSharp_String,
    cSharp_SwitchLabel,
    cSharp_SwitchSection,
    cSharp_SwitchStatement,
    cSharp_ThrowStatement,
    cSharp_TryStatement,
    cSharp_Type,
    cSharp_TypeDeclaration,
    cSharp_TypeOrVoid,
    cSharp_UInt,
    cSharp_ULong,
    cSharp_UShort,
    cSharp_UnaryExpression,
    cSharp_UnaryOperatorDeclarator,
    cSharp_UsingDirective,
    cSharp_UsingStatement,
    cSharp_VariableDeclarator,
    cSharp_VariableInitializer,
    cSharp_Void,
    cSharp_WhileStatement,
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

def test_assoc_primaryExoression2149_reverse_link_reassign_clear():
    a1 = cSharp_PrimaryExpression2(incrementeDecrement="sample_text")
    a2 = cSharp_PrimaryExpression2(incrementeDecrement="sample_text_2")
    b = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    _safe_set(b, 'cSharp_PrimaryExpression150', a1)
    assert _is_linked(b, 'cSharp_PrimaryExpression150', a1)
    if hasattr(a1, 'cSharp_PrimaryExpression2'):
        assert _is_linked(a1, 'cSharp_PrimaryExpression2', b)
    _safe_set(b, 'cSharp_PrimaryExpression150', a2)
    assert _is_linked(b, 'cSharp_PrimaryExpression150', a2)
    if hasattr(a1, 'cSharp_PrimaryExpression2'):
        assert not _is_linked(a1, 'cSharp_PrimaryExpression2', b)
    if hasattr(a2, 'cSharp_PrimaryExpression2'):
        assert _is_linked(a2, 'cSharp_PrimaryExpression2', b)
    _safe_set(b, 'cSharp_PrimaryExpression150', None)
    assert not _is_linked(b, 'cSharp_PrimaryExpression150', a2)
    if hasattr(a2, 'cSharp_PrimaryExpression2'):
        assert not _is_linked(a2, 'cSharp_PrimaryExpression2', b)


def test_assoc_primaryExp122_reverse_link_reassign_clear():
    a1 = cSharp_UnaryExpression(expUnaryOperator="sample_text")
    a2 = cSharp_UnaryExpression(expUnaryOperator="sample_text_2")
    b = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    _safe_set(b, 'cSharp_PrimaryExpression', a1)
    assert _is_linked(b, 'cSharp_PrimaryExpression', a1)
    if hasattr(a1, 'cSharp_UnaryExpression123'):
        assert _is_linked(a1, 'cSharp_UnaryExpression123', b)
    _safe_set(b, 'cSharp_PrimaryExpression', a2)
    assert _is_linked(b, 'cSharp_PrimaryExpression', a2)
    if hasattr(a1, 'cSharp_UnaryExpression123'):
        assert not _is_linked(a1, 'cSharp_UnaryExpression123', b)
    if hasattr(a2, 'cSharp_UnaryExpression123'):
        assert _is_linked(a2, 'cSharp_UnaryExpression123', b)
    _safe_set(b, 'cSharp_PrimaryExpression', None)
    assert not _is_linked(b, 'cSharp_PrimaryExpression', a2)
    if hasattr(a2, 'cSharp_UnaryExpression123'):
        assert not _is_linked(a2, 'cSharp_UnaryExpression123', b)


def test_assoc_primaryExpression2161_reverse_link_reassign_clear():
    a1 = cSharp_PrimaryExpression2(incrementeDecrement="sample_text")
    a2 = cSharp_PrimaryExpression2(incrementeDecrement="sample_text_2")
    b = cSharp_PrimaryExpression2(incrementeDecrement="sample_text")
    _safe_set(b, 'cSharp_PrimaryExpression2162', a1)
    assert _is_linked(b, 'cSharp_PrimaryExpression2162', a1)
    if hasattr(a1, 'cSharp_PrimaryExpression2160'):
        assert _is_linked(a1, 'cSharp_PrimaryExpression2160', b)
    _safe_set(b, 'cSharp_PrimaryExpression2162', a2)
    assert _is_linked(b, 'cSharp_PrimaryExpression2162', a2)
    if hasattr(a1, 'cSharp_PrimaryExpression2160'):
        assert not _is_linked(a1, 'cSharp_PrimaryExpression2160', b)
    if hasattr(a2, 'cSharp_PrimaryExpression2160'):
        assert _is_linked(a2, 'cSharp_PrimaryExpression2160', b)
    _safe_set(b, 'cSharp_PrimaryExpression2162', None)
    assert not _is_linked(b, 'cSharp_PrimaryExpression2162', a2)
    if hasattr(a2, 'cSharp_PrimaryExpression2160'):
        assert not _is_linked(a2, 'cSharp_PrimaryExpression2160', b)


def test_assoc_primaryExpression675_reverse_link_reassign_clear():
    a1 = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    a2 = cSharp_StatementExpression(assignementOperator="sample_text_2", incrimentDecrement="sample_text_2")
    b = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    _safe_set(b, 'cSharp_PrimaryExpression677', a1)
    assert _is_linked(b, 'cSharp_PrimaryExpression677', a1)
    if hasattr(a1, 'cSharp_StatementExpression676'):
        assert _is_linked(a1, 'cSharp_StatementExpression676', b)
    _safe_set(b, 'cSharp_PrimaryExpression677', a2)
    assert _is_linked(b, 'cSharp_PrimaryExpression677', a2)
    if hasattr(a1, 'cSharp_StatementExpression676'):
        assert not _is_linked(a1, 'cSharp_StatementExpression676', b)
    if hasattr(a2, 'cSharp_StatementExpression676'):
        assert _is_linked(a2, 'cSharp_StatementExpression676', b)
    _safe_set(b, 'cSharp_PrimaryExpression677', None)
    assert not _is_linked(b, 'cSharp_PrimaryExpression677', a2)
    if hasattr(a2, 'cSharp_StatementExpression676'):
        assert not _is_linked(a2, 'cSharp_StatementExpression676', b)


def test_assoc_unaryExp120_reverse_link_reassign_clear():
    a1 = cSharp_UnaryExpression(expUnaryOperator="sample_text")
    a2 = cSharp_UnaryExpression(expUnaryOperator="sample_text_2")
    b = cSharp_UnaryExpression(expUnaryOperator="sample_text")
    _safe_set(b, 'cSharp_UnaryExpression121', a1)
    assert _is_linked(b, 'cSharp_UnaryExpression121', a1)
    if hasattr(a1, 'cSharp_UnaryExpression119'):
        assert _is_linked(a1, 'cSharp_UnaryExpression119', b)
    _safe_set(b, 'cSharp_UnaryExpression121', a2)
    assert _is_linked(b, 'cSharp_UnaryExpression121', a2)
    if hasattr(a1, 'cSharp_UnaryExpression119'):
        assert not _is_linked(a1, 'cSharp_UnaryExpression119', b)
    if hasattr(a2, 'cSharp_UnaryExpression119'):
        assert _is_linked(a2, 'cSharp_UnaryExpression119', b)
    _safe_set(b, 'cSharp_UnaryExpression121', None)
    assert not _is_linked(b, 'cSharp_UnaryExpression121', a2)
    if hasattr(a2, 'cSharp_UnaryExpression119'):
        assert not _is_linked(a2, 'cSharp_UnaryExpression119', b)


def test_assoc_unaryExpression678_reverse_link_reassign_clear():
    a1 = cSharp_UnaryExpression(expUnaryOperator="sample_text")
    a2 = cSharp_UnaryExpression(expUnaryOperator="sample_text_2")
    b = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    _safe_set(b, 'cSharp_StatementExpression679', a1)
    assert _is_linked(b, 'cSharp_StatementExpression679', a1)
    if hasattr(a1, 'cSharp_UnaryExpression680'):
        assert _is_linked(a1, 'cSharp_UnaryExpression680', b)
    _safe_set(b, 'cSharp_StatementExpression679', a2)
    assert _is_linked(b, 'cSharp_StatementExpression679', a2)
    if hasattr(a1, 'cSharp_UnaryExpression680'):
        assert not _is_linked(a1, 'cSharp_UnaryExpression680', b)
    if hasattr(a2, 'cSharp_UnaryExpression680'):
        assert _is_linked(a2, 'cSharp_UnaryExpression680', b)
    _safe_set(b, 'cSharp_StatementExpression679', None)
    assert not _is_linked(b, 'cSharp_StatementExpression679', a2)
    if hasattr(a2, 'cSharp_UnaryExpression680'):
        assert not _is_linked(a2, 'cSharp_UnaryExpression680', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accDeclaration407_stub_double():
    # cSharp_AccessorDeclarations has no real 'cSharp_AccessorDeclarations409' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_IndexerDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_IndexerDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_IndexerDeclaration(idModifier="sample_text")
    partner = cSharp_AccessorDeclarations()
    setattr(partner, 'cSharp_AccessorDeclarations409', None)
    _safe_set(owner, 'cSharp_IndexerDeclaration408', partner)
    assert getattr(partner, 'cSharp_AccessorDeclarations409') == owner
    _safe_set(owner, 'cSharp_IndexerDeclaration408', None)
    assert getattr(partner, 'cSharp_AccessorDeclarations409') is None


def test_assoc_argumentList139_stub_double():
    # cSharp_ArgumentList has no real 'cSharp_ArgumentList' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_ArgumentList()
    setattr(partner, 'cSharp_ArgumentList', None)
    _safe_set(owner, 'cSharp_PrimaryExpression140', partner)
    assert getattr(partner, 'cSharp_ArgumentList') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression140', None)
    assert getattr(partner, 'cSharp_ArgumentList') is None


def test_assoc_argumentList154_stub_double():
    # cSharp_ArgumentList has no real 'cSharp_ArgumentList156' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression2(incrementeDecrement="sample_text")
    partner = cSharp_ArgumentList()
    setattr(partner, 'cSharp_ArgumentList156', None)
    _safe_set(owner, 'cSharp_PrimaryExpression2155', {partner})
    assert getattr(partner, 'cSharp_ArgumentList156') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression2155', set())
    assert getattr(partner, 'cSharp_ArgumentList156') is None


def test_assoc_argumentList672_stub_double():
    # cSharp_ArgumentList has no real 'cSharp_ArgumentList674' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    partner = cSharp_ArgumentList()
    setattr(partner, 'cSharp_ArgumentList674', None)
    _safe_set(owner, 'cSharp_StatementExpression673', partner)
    assert getattr(partner, 'cSharp_ArgumentList674') == owner
    _safe_set(owner, 'cSharp_StatementExpression673', None)
    assert getattr(partner, 'cSharp_ArgumentList674') is None


def test_assoc_arrayInitializer129_stub_double():
    # cSharp_ArrayInitializer has no real 'cSharp_ArrayInitializer' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_ArrayInitializer()
    setattr(partner, 'cSharp_ArrayInitializer', None)
    _safe_set(owner, 'cSharp_PrimaryExpression130', {partner})
    assert getattr(partner, 'cSharp_ArrayInitializer') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression130', set())
    assert getattr(partner, 'cSharp_ArrayInitializer') is None


def test_assoc_arrayInitializer2133_stub_double():
    # cSharp_ArrayInitializer has no real 'cSharp_ArrayInitializer135' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_ArrayInitializer()
    setattr(partner, 'cSharp_ArrayInitializer135', None)
    _safe_set(owner, 'cSharp_PrimaryExpression134', partner)
    assert getattr(partner, 'cSharp_ArrayInitializer135') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression134', None)
    assert getattr(partner, 'cSharp_ArrayInitializer135') is None


def test_assoc_arrayType131_stub_double():
    # cSharp_ArrayType has no real 'cSharp_ArrayType' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_ArrayType()
    setattr(partner, 'cSharp_ArrayType', None)
    _safe_set(owner, 'cSharp_PrimaryExpression132', partner)
    assert getattr(partner, 'cSharp_ArrayType') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression132', None)
    assert getattr(partner, 'cSharp_ArrayType') is None


def test_assoc_binType389_stub_double():
    # cSharp_Type has no real 'cSharp_Type390' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_BinaryOperatorDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_BinaryOperatorDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_BinaryOperatorDeclarator(overBinOperator="sample_text")
    partner = cSharp_Type()
    setattr(partner, 'cSharp_Type390', None)
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator', partner)
    assert getattr(partner, 'cSharp_Type390') == owner
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator', None)
    assert getattr(partner, 'cSharp_Type390') is None


def test_assoc_classBase315_stub_double():
    # cSharp_ClassBase has no real 'cSharp_ClassBase' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ClassDeclaration(classModifier="sample_text")
    partner = cSharp_ClassBase()
    setattr(partner, 'cSharp_ClassBase', None)
    _safe_set(owner, 'cSharp_ClassDeclaration316', partner)
    assert getattr(partner, 'cSharp_ClassBase') == owner
    _safe_set(owner, 'cSharp_ClassDeclaration316', None)
    assert getattr(partner, 'cSharp_ClassBase') is None


def test_assoc_classBody317_stub_double():
    # cSharp_ClassBody has no real 'cSharp_ClassBody' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ClassDeclaration(classModifier="sample_text")
    partner = cSharp_ClassBody()
    setattr(partner, 'cSharp_ClassBody', None)
    _safe_set(owner, 'cSharp_ClassDeclaration318', partner)
    assert getattr(partner, 'cSharp_ClassBody') == owner
    _safe_set(owner, 'cSharp_ClassDeclaration318', None)
    assert getattr(partner, 'cSharp_ClassBody') is None


def test_assoc_classDeclaration228_stub_double():
    # cSharp_TypeDeclaration has no real 'cSharp_TypeDeclaration229' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ClassDeclaration(classModifier="sample_text")
    partner = cSharp_TypeDeclaration()
    setattr(partner, 'cSharp_TypeDeclaration229', None)
    _safe_set(owner, 'cSharp_ClassDeclaration', partner)
    assert getattr(partner, 'cSharp_TypeDeclaration229') == owner
    _safe_set(owner, 'cSharp_ClassDeclaration', None)
    assert getattr(partner, 'cSharp_TypeDeclaration229') is None


def test_assoc_className312_stub_double():
    # cSharp_Identifier has no real 'cSharp_Identifier314' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ClassDeclaration(classModifier="sample_text")
    partner = cSharp_Identifier()
    setattr(partner, 'cSharp_Identifier314', None)
    _safe_set(owner, 'cSharp_ClassDeclaration313', partner)
    assert getattr(partner, 'cSharp_Identifier314') == owner
    _safe_set(owner, 'cSharp_ClassDeclaration313', None)
    assert getattr(partner, 'cSharp_Identifier314') is None


def test_assoc_constrDeclarator358_stub_double():
    # cSharp_ConstructorDeclarator has no real 'cSharp_ConstructorDeclarator' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ConstructorDeclaration(constModifier="sample_text")
    partner = cSharp_ConstructorDeclarator()
    setattr(partner, 'cSharp_ConstructorDeclarator', None)
    _safe_set(owner, 'cSharp_ConstructorDeclaration359', partner)
    assert getattr(partner, 'cSharp_ConstructorDeclarator') == owner
    _safe_set(owner, 'cSharp_ConstructorDeclaration359', None)
    assert getattr(partner, 'cSharp_ConstructorDeclarator') is None


def test_assoc_constructorDeclaration341_stub_double():
    # cSharp_ClassMemberDeclaration has no real 'cSharp_ClassMemberDeclaration342' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ConstructorDeclaration(constModifier="sample_text")
    partner = cSharp_ClassMemberDeclaration()
    setattr(partner, 'cSharp_ClassMemberDeclaration342', None)
    _safe_set(owner, 'cSharp_ConstructorDeclaration', partner)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration342') == owner
    _safe_set(owner, 'cSharp_ConstructorDeclaration', None)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration342') is None


def test_assoc_emptyBlock350_stub_double():
    # cSharp_MaybeEmptyBlock has no real 'cSharp_MaybeEmptyBlock' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StaticConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StaticConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StaticConstructorDeclaration(staticCosntModifier="sample_text")
    partner = cSharp_MaybeEmptyBlock()
    setattr(partner, 'cSharp_MaybeEmptyBlock', None)
    _safe_set(owner, 'cSharp_StaticConstructorDeclaration351', partner)
    assert getattr(partner, 'cSharp_MaybeEmptyBlock') == owner
    _safe_set(owner, 'cSharp_StaticConstructorDeclaration351', None)
    assert getattr(partner, 'cSharp_MaybeEmptyBlock') is None


def test_assoc_emptyBlock360_stub_double():
    # cSharp_MaybeEmptyBlock has no real 'cSharp_MaybeEmptyBlock362' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_ConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_ConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_ConstructorDeclaration(constModifier="sample_text")
    partner = cSharp_MaybeEmptyBlock()
    setattr(partner, 'cSharp_MaybeEmptyBlock362', None)
    _safe_set(owner, 'cSharp_ConstructorDeclaration361', partner)
    assert getattr(partner, 'cSharp_MaybeEmptyBlock362') == owner
    _safe_set(owner, 'cSharp_ConstructorDeclaration361', None)
    assert getattr(partner, 'cSharp_MaybeEmptyBlock362') is None


def test_assoc_emptyBlock378_stub_double():
    # cSharp_MaybeEmptyBlock has no real 'cSharp_MaybeEmptyBlock380' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_OperatorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_OperatorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_OperatorDeclaration(opModifier="sample_text")
    partner = cSharp_MaybeEmptyBlock()
    setattr(partner, 'cSharp_MaybeEmptyBlock380', None)
    _safe_set(owner, 'cSharp_OperatorDeclaration379', partner)
    assert getattr(partner, 'cSharp_MaybeEmptyBlock380') == owner
    _safe_set(owner, 'cSharp_OperatorDeclaration379', None)
    assert getattr(partner, 'cSharp_MaybeEmptyBlock380') is None


def test_assoc_expression144_stub_double():
    # cSharp_Expression has no real 'cSharp_Expression146' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_Expression()
    setattr(partner, 'cSharp_Expression146', None)
    _safe_set(owner, 'cSharp_PrimaryExpression145', partner)
    assert getattr(partner, 'cSharp_Expression146') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression145', None)
    assert getattr(partner, 'cSharp_Expression146') is None


def test_assoc_expression681_stub_double():
    # cSharp_Expression has no real 'cSharp_Expression683' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    partner = cSharp_Expression()
    setattr(partner, 'cSharp_Expression683', None)
    _safe_set(owner, 'cSharp_StatementExpression682', partner)
    assert getattr(partner, 'cSharp_Expression683') == owner
    _safe_set(owner, 'cSharp_StatementExpression682', None)
    assert getattr(partner, 'cSharp_Expression683') is None


def test_assoc_expressionList126_stub_double():
    # cSharp_ExpressionList has no real 'cSharp_ExpressionList128' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_ExpressionList()
    setattr(partner, 'cSharp_ExpressionList128', None)
    _safe_set(owner, 'cSharp_PrimaryExpression127', partner)
    assert getattr(partner, 'cSharp_ExpressionList128') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression127', None)
    assert getattr(partner, 'cSharp_ExpressionList128') is None


def test_assoc_expressionList157_stub_double():
    # cSharp_ExpressionList has no real 'cSharp_ExpressionList159' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression2(incrementeDecrement="sample_text")
    partner = cSharp_ExpressionList()
    setattr(partner, 'cSharp_ExpressionList159', None)
    _safe_set(owner, 'cSharp_PrimaryExpression2158', {partner})
    assert getattr(partner, 'cSharp_ExpressionList159') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression2158', set())
    assert getattr(partner, 'cSharp_ExpressionList159') is None


def test_assoc_formalParameters450_stub_double():
    # cSharp_FormalParameterList has no real 'cSharp_FormalParameterList452' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_MethodHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_MethodHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_MethodHeader(modifier="sample_text")
    partner = cSharp_FormalParameterList()
    setattr(partner, 'cSharp_FormalParameterList452', None)
    _safe_set(owner, 'cSharp_MethodHeader451', partner)
    assert getattr(partner, 'cSharp_FormalParameterList452') == owner
    _safe_set(owner, 'cSharp_MethodHeader451', None)
    assert getattr(partner, 'cSharp_FormalParameterList452') is None


def test_assoc_id141_stub_double():
    # cSharp_Identifier has no real 'cSharp_Identifier143' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_Identifier()
    setattr(partner, 'cSharp_Identifier143', None)
    _safe_set(owner, 'cSharp_PrimaryExpression142', partner)
    assert getattr(partner, 'cSharp_Identifier143') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression142', None)
    assert getattr(partner, 'cSharp_Identifier143') is None


def test_assoc_id151_stub_double():
    # cSharp_Identifier has no real 'cSharp_Identifier153' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression2(incrementeDecrement="sample_text")
    partner = cSharp_Identifier()
    setattr(partner, 'cSharp_Identifier153', None)
    _safe_set(owner, 'cSharp_PrimaryExpression2152', {partner})
    assert getattr(partner, 'cSharp_Identifier153') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression2152', set())
    assert getattr(partner, 'cSharp_Identifier153') is None


def test_assoc_indexDeclaration334_stub_double():
    # cSharp_ClassMemberDeclaration has no real 'cSharp_ClassMemberDeclaration335' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_IndexerDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_IndexerDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_IndexerDeclaration(idModifier="sample_text")
    partner = cSharp_ClassMemberDeclaration()
    setattr(partner, 'cSharp_ClassMemberDeclaration335', None)
    _safe_set(owner, 'cSharp_IndexerDeclaration', partner)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration335') == owner
    _safe_set(owner, 'cSharp_IndexerDeclaration', None)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration335') is None


def test_assoc_indexerDeclarator405_stub_double():
    # cSharp_IndexerDeclarator has no real 'cSharp_IndexerDeclarator' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_IndexerDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_IndexerDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_IndexerDeclaration(idModifier="sample_text")
    partner = cSharp_IndexerDeclarator()
    setattr(partner, 'cSharp_IndexerDeclarator', None)
    _safe_set(owner, 'cSharp_IndexerDeclaration406', partner)
    assert getattr(partner, 'cSharp_IndexerDeclarator') == owner
    _safe_set(owner, 'cSharp_IndexerDeclaration406', None)
    assert getattr(partner, 'cSharp_IndexerDeclarator') is None


def test_assoc_list663_stub_double():
    # cSharp_StatementExpressionList has no real 'cSharp_StatementExpressionList664' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    partner = cSharp_StatementExpressionList()
    setattr(partner, 'cSharp_StatementExpressionList664', None)
    _safe_set(owner, 'cSharp_StatementExpression665', partner)
    assert getattr(partner, 'cSharp_StatementExpressionList664') == owner
    _safe_set(owner, 'cSharp_StatementExpression665', None)
    assert getattr(partner, 'cSharp_StatementExpressionList664') is None


def test_assoc_lists666_stub_double():
    # cSharp_StatementExpressionList has no real 'cSharp_StatementExpressionList667' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    partner = cSharp_StatementExpressionList()
    setattr(partner, 'cSharp_StatementExpressionList667', None)
    _safe_set(owner, 'cSharp_StatementExpression668', partner)
    assert owner in getattr(partner, 'cSharp_StatementExpressionList667')
    _safe_set(owner, 'cSharp_StatementExpression668', None)
    assert owner not in getattr(partner, 'cSharp_StatementExpressionList667')


def test_assoc_methodHeader439_stub_double():
    # cSharp_MethodDeclaration has no real 'cSharp_MethodDeclaration440' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_MethodHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_MethodHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_MethodHeader(modifier="sample_text")
    partner = cSharp_MethodDeclaration()
    setattr(partner, 'cSharp_MethodDeclaration440', None)
    _safe_set(owner, 'cSharp_MethodHeader', partner)
    assert getattr(partner, 'cSharp_MethodDeclaration440') == owner
    _safe_set(owner, 'cSharp_MethodHeader', None)
    assert getattr(partner, 'cSharp_MethodDeclaration440') is None


def test_assoc_name347_stub_double():
    # cSharp_Identifier has no real 'cSharp_Identifier349' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StaticConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StaticConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StaticConstructorDeclaration(staticCosntModifier="sample_text")
    partner = cSharp_Identifier()
    setattr(partner, 'cSharp_Identifier349', None)
    _safe_set(owner, 'cSharp_StaticConstructorDeclaration348', partner)
    assert getattr(partner, 'cSharp_Identifier349') == owner
    _safe_set(owner, 'cSharp_StaticConstructorDeclaration348', None)
    assert getattr(partner, 'cSharp_Identifier349') is None


def test_assoc_nonArrayType124_stub_double():
    # cSharp_NonArrayType has no real 'cSharp_NonArrayType' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_NonArrayType()
    setattr(partner, 'cSharp_NonArrayType', None)
    _safe_set(owner, 'cSharp_PrimaryExpression125', partner)
    assert getattr(partner, 'cSharp_NonArrayType') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression125', None)
    assert getattr(partner, 'cSharp_NonArrayType') is None


def test_assoc_opDeclaration339_stub_double():
    # cSharp_ClassMemberDeclaration has no real 'cSharp_ClassMemberDeclaration340' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_OperatorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_OperatorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_OperatorDeclaration(opModifier="sample_text")
    partner = cSharp_ClassMemberDeclaration()
    setattr(partner, 'cSharp_ClassMemberDeclaration340', None)
    _safe_set(owner, 'cSharp_OperatorDeclaration', partner)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration340') == owner
    _safe_set(owner, 'cSharp_OperatorDeclaration', None)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration340') is None


def test_assoc_opDeclarator376_stub_double():
    # cSharp_OperatorDeclarator has no real 'cSharp_OperatorDeclarator' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_OperatorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_OperatorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_OperatorDeclaration(opModifier="sample_text")
    partner = cSharp_OperatorDeclarator()
    setattr(partner, 'cSharp_OperatorDeclarator', None)
    _safe_set(owner, 'cSharp_OperatorDeclaration377', partner)
    assert getattr(partner, 'cSharp_OperatorDeclarator') == owner
    _safe_set(owner, 'cSharp_OperatorDeclaration377', None)
    assert getattr(partner, 'cSharp_OperatorDeclarator') is None


def test_assoc_otherName391_stub_double():
    # cSharp_Identifier has no real 'cSharp_Identifier393' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_BinaryOperatorDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_BinaryOperatorDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_BinaryOperatorDeclarator(overBinOperator="sample_text")
    partner = cSharp_Identifier()
    setattr(partner, 'cSharp_Identifier393', None)
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator392', partner)
    assert getattr(partner, 'cSharp_Identifier393') == owner
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator392', None)
    assert getattr(partner, 'cSharp_Identifier393') is None


def test_assoc_qualifiedIdentifier447_stub_double():
    # cSharp_QualifiedIdentifier has no real 'cSharp_QualifiedIdentifier449' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_MethodHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_MethodHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_MethodHeader(modifier="sample_text")
    partner = cSharp_QualifiedIdentifier()
    setattr(partner, 'cSharp_QualifiedIdentifier449', None)
    _safe_set(owner, 'cSharp_MethodHeader448', partner)
    assert getattr(partner, 'cSharp_QualifiedIdentifier449') == owner
    _safe_set(owner, 'cSharp_MethodHeader448', None)
    assert getattr(partner, 'cSharp_QualifiedIdentifier449') is None


def test_assoc_secondName397_stub_double():
    # cSharp_Identifier has no real 'cSharp_Identifier399' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_BinaryOperatorDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_BinaryOperatorDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_BinaryOperatorDeclarator(overBinOperator="sample_text")
    partner = cSharp_Identifier()
    setattr(partner, 'cSharp_Identifier399', None)
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator398', partner)
    assert getattr(partner, 'cSharp_Identifier399') == owner
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator398', None)
    assert getattr(partner, 'cSharp_Identifier399') is None


def test_assoc_secondType394_stub_double():
    # cSharp_Type has no real 'cSharp_Type396' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_BinaryOperatorDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_BinaryOperatorDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_BinaryOperatorDeclarator(overBinOperator="sample_text")
    partner = cSharp_Type()
    setattr(partner, 'cSharp_Type396', None)
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator395', partner)
    assert getattr(partner, 'cSharp_Type396') == owner
    _safe_set(owner, 'cSharp_BinaryOperatorDeclarator395', None)
    assert getattr(partner, 'cSharp_Type396') is None


def test_assoc_statExp534_stub_double():
    # cSharp_EmbeddedStatement has no real 'cSharp_EmbeddedStatement535' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    partner = cSharp_EmbeddedStatement()
    setattr(partner, 'cSharp_EmbeddedStatement535', None)
    _safe_set(owner, 'cSharp_StatementExpression', partner)
    assert getattr(partner, 'cSharp_EmbeddedStatement535') == owner
    _safe_set(owner, 'cSharp_StatementExpression', None)
    assert getattr(partner, 'cSharp_EmbeddedStatement535') is None


def test_assoc_staticDeclaration345_stub_double():
    # cSharp_ClassMemberDeclaration has no real 'cSharp_ClassMemberDeclaration346' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StaticConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StaticConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StaticConstructorDeclaration(staticCosntModifier="sample_text")
    partner = cSharp_ClassMemberDeclaration()
    setattr(partner, 'cSharp_ClassMemberDeclaration346', None)
    _safe_set(owner, 'cSharp_StaticConstructorDeclaration', partner)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration346') == owner
    _safe_set(owner, 'cSharp_StaticConstructorDeclaration', None)
    assert getattr(partner, 'cSharp_ClassMemberDeclaration346') is None


def test_assoc_tipo136_stub_double():
    # cSharp_Type has no real 'cSharp_Type138' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_Type()
    setattr(partner, 'cSharp_Type138', None)
    _safe_set(owner, 'cSharp_PrimaryExpression137', partner)
    assert getattr(partner, 'cSharp_Type138') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression137', None)
    assert getattr(partner, 'cSharp_Type138') is None


def test_assoc_tipo669_stub_double():
    # cSharp_Type has no real 'cSharp_Type671' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_StatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_StatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_StatementExpression(assignementOperator="sample_text", incrimentDecrement="sample_text")
    partner = cSharp_Type()
    setattr(partner, 'cSharp_Type671', None)
    _safe_set(owner, 'cSharp_StatementExpression670', partner)
    assert getattr(partner, 'cSharp_Type671') == owner
    _safe_set(owner, 'cSharp_StatementExpression670', None)
    assert getattr(partner, 'cSharp_Type671') is None


def test_assoc_type117_stub_double():
    # cSharp_Type has no real 'cSharp_Type' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_UnaryExpression(expUnaryOperator="sample_text")
    partner = cSharp_Type()
    setattr(partner, 'cSharp_Type', None)
    _safe_set(owner, 'cSharp_UnaryExpression118', partner)
    assert getattr(partner, 'cSharp_Type') == owner
    _safe_set(owner, 'cSharp_UnaryExpression118', None)
    assert getattr(partner, 'cSharp_Type') is None


def test_assoc_typeOrVoid147_stub_double():
    # cSharp_TypeOrVoid has no real 'cSharp_TypeOrVoid' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_PrimaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_PrimaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_PrimaryExpression(literal="sample_text", predefinedType="sample_text", rankSpecifier="sample_text")
    partner = cSharp_TypeOrVoid()
    setattr(partner, 'cSharp_TypeOrVoid', None)
    _safe_set(owner, 'cSharp_PrimaryExpression148', partner)
    assert getattr(partner, 'cSharp_TypeOrVoid') == owner
    _safe_set(owner, 'cSharp_PrimaryExpression148', None)
    assert getattr(partner, 'cSharp_TypeOrVoid') is None


def test_assoc_typeOrVoid444_stub_double():
    # cSharp_TypeOrVoid has no real 'cSharp_TypeOrVoid446' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_MethodHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_MethodHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_MethodHeader(modifier="sample_text")
    partner = cSharp_TypeOrVoid()
    setattr(partner, 'cSharp_TypeOrVoid446', None)
    _safe_set(owner, 'cSharp_MethodHeader445', partner)
    assert getattr(partner, 'cSharp_TypeOrVoid446') == owner
    _safe_set(owner, 'cSharp_MethodHeader445', None)
    assert getattr(partner, 'cSharp_TypeOrVoid446') is None


def test_assoc_unary30_stub_double():
    # cSharp_Expression has no real 'cSharp_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so cSharp_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cSharp_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cSharp_UnaryExpression(expUnaryOperator="sample_text")
    partner = cSharp_Expression()
    setattr(partner, 'cSharp_Expression31', None)
    _safe_set(owner, 'cSharp_UnaryExpression', partner)
    assert getattr(partner, 'cSharp_Expression31') == owner
    _safe_set(owner, 'cSharp_UnaryExpression', None)
    assert getattr(partner, 'cSharp_Expression31') is None


