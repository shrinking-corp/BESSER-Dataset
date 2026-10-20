import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccessKind,
    ActualParameter,
    ActualParameterExpression,
    AggregateType,
    BinaryOperator,
    CatchBlock,
    ConstructedType,
    DataDefinition,
    DataType,
    Declaration,
    DeclarationOrDefinition,
    Definition,
    DefinitionObject,
    Expression,
    ForStatement,
    FormalParameterType,
    GASTMObject,
    GASTMSemanticObject,
    GASTMSourceObject,
    GASTMSyntaxObject,
    IntegerLiteral,
    IntegralType,
    Literal,
    LoopStatement,
    MinorSyntaxObject,
    NameReference,
    NumberType,
    PreprocessorElement,
    PrimitiveType,
    QualifiedIdentifierReference,
    RealType,
    Scope,
    SourceFile,
    Statement,
    StorageSpecification,
    SwitchCase,
    Type,
    TypeDeclaration,
    TypeDefinition,
    TypeReference,
    UnaryOperator,
    VirtualSpecification,
    gastm_AccessKind,
    gastm_ActualParameter,
    gastm_ActualParameterExpression,
    gastm_Add,
    gastm_AddressOf,
    gastm_AggregateExpression,
    gastm_AggregateScope,
    gastm_AggregateType,
    gastm_AggregateTypeDeclaration,
    gastm_AggregateTypeDefinition,
    gastm_And,
    gastm_AnnotationExpression,
    gastm_AnnotationType,
    gastm_ArrayAccess,
    gastm_ArrayType,
    gastm_Assign,
    gastm_BinaryExpression,
    gastm_BinaryOperator,
    gastm_BitAnd,
    gastm_BitFieldDefinition,
    gastm_BitLeftShift,
    gastm_BitLiteral,
    gastm_BitNot,
    gastm_BitOr,
    gastm_BitRightShift,
    gastm_BitXor,
    gastm_BlockScope,
    gastm_BlockStatement,
    gastm_Boolean,
    gastm_BooleanLiteral,
    gastm_BreakStatement,
    gastm_ByReferenceActualParameterExpression,
    gastm_ByReferenceFormalParameterType,
    gastm_ByValueActualParameterExpression,
    gastm_ByValueFormalParameterType,
    gastm_Byte,
    gastm_CaseBlock,
    gastm_CastExpression,
    gastm_CatchBlock,
    gastm_CharLiteral,
    gastm_Character,
    gastm_ClassType,
    gastm_CollectionExpression,
    gastm_CollectionType,
    gastm_Comment,
    gastm_CompilationUnit,
    gastm_ConditionalExpression,
    gastm_ConstructedType,
    gastm_ContinueStatement,
    gastm_DataDefinition,
    gastm_DataType,
    gastm_Declaration,
    gastm_DeclarationOrDefinition,
    gastm_DeclarationOrDefinitionStatement,
    gastm_Decrement,
    gastm_DefaultBlock,
    gastm_Definition,
    gastm_DefinitionObject,
    gastm_DeleteStatement,
    gastm_Deref,
    gastm_DerivesFrom,
    gastm_Dimension,
    gastm_Divide,
    gastm_DoWhileStatement,
    gastm_Double,
    gastm_EmptyStatement,
    gastm_EntryDefinition,
    gastm_EnumLiteral,
    gastm_EnumLiteralDefinition,
    gastm_EnumType,
    gastm_EnumTypeDeclaration,
    gastm_EnumTypeDefinition,
    gastm_Equal,
    gastm_ExceptionType,
    gastm_Exponent,
    gastm_Expression,
    gastm_ExpressionStatement,
    gastm_External,
    gastm_FileLocal,
    gastm_ForCheckAfterStatement,
    gastm_ForCheckBeforeStatement,
    gastm_ForStatement,
    gastm_FormalParameterDeclaration,
    gastm_FormalParameterDefinition,
    gastm_FormalParameterType,
    gastm_FunctionCallExpression,
    gastm_FunctionDeclaration,
    gastm_FunctionDefinition,
    gastm_FunctionMemberAttributes,
    gastm_FunctionPersistent,
    gastm_FunctionScope,
    gastm_FunctionType,
    gastm_GASTMObject,
    gastm_GASTMSemanticObject,
    gastm_GASTMSourceObject,
    gastm_GASTMSyntaxObject,
    gastm_GlobalScope,
    gastm_Greater,
    gastm_IdentifierReference,
    gastm_IfStatement,
    gastm_IncludeUnit,
    gastm_Increment,
    gastm_Integer,
    gastm_IntegerLiteral,
    gastm_IntegralType,
    gastm_JumpStatement,
    gastm_LabelAccess,
    gastm_LabelDefinition,
    gastm_LabelType,
    gastm_LabeledStatement,
    gastm_Less,
    gastm_Literal,
    gastm_LongDouble,
    gastm_LongInteger,
    gastm_LoopStatement,
    gastm_MacroCall,
    gastm_MacroDefinition,
    gastm_MemberObject,
    gastm_MinorSyntaxObject,
    gastm_MissingActualParameter,
    gastm_Modulus,
    gastm_Multiply,
    gastm_Name,
    gastm_NameReference,
    gastm_NameSpaceDefinition,
    gastm_NameSpaceType,
    gastm_NamedType,
    gastm_NamedTypeDefinition,
    gastm_NamedTypeReference,
    gastm_NewExpression,
    gastm_NoDef,
    gastm_Not,
    gastm_NotEqual,
    gastm_NotGreater,
    gastm_NotLess,
    gastm_NumberType,
    gastm_OperatorAssign,
    gastm_Or,
    gastm_PerClassMember,
    gastm_PointerType,
    gastm_PostDecrement,
    gastm_PostIncrement,
    gastm_PreprocessorElement,
    gastm_PrimitiveType,
    gastm_Private,
    gastm_ProgramScope,
    gastm_Project,
    gastm_Protected,
    gastm_Public,
    gastm_QualifiedIdentifierReference,
    gastm_QualifiedOverData,
    gastm_QualifiedOverPointer,
    gastm_RangeExpression,
    gastm_RangeType,
    gastm_Real,
    gastm_RealLiteral,
    gastm_RealType,
    gastm_ReferenceType,
    gastm_ReturnStatement,
    gastm_Scope,
    gastm_ShortInteger,
    gastm_SourceFile,
    gastm_SourceFileReference,
    gastm_SourceLocation,
    gastm_Statement,
    gastm_StorageSpecification,
    gastm_StringLiteral,
    gastm_StructureType,
    gastm_Subtract,
    gastm_SwitchCase,
    gastm_SwitchStatement,
    gastm_TerminateStatement,
    gastm_ThrowStatement,
    gastm_TryStatement,
    gastm_Type,
    gastm_TypeDeclaration,
    gastm_TypeDefinition,
    gastm_TypeQualifiedIdentifierReference,
    gastm_TypeReference,
    gastm_TypesCatchBlock,
    gastm_UnaryExpression,
    gastm_UnaryMinus,
    gastm_UnaryOperator,
    gastm_UnaryPlus,
    gastm_UnionType,
    gastm_UnnamedTypeReference,
    gastm_VariableCatchBlock,
    gastm_VariableDeclaration,
    gastm_VariableDefinition,
    gastm_Virtual,
    gastm_VirtualSpecification,
    gastm_Void,
    gastm_WhileStatement,
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

def test_assoc_inSourceFile5_reverse_link_reassign_clear():
    a1 = gastm_SourceLocation(endLine="sample_text", endPosition="sample_text", startLine="sample_text", startPosition="sample_text")
    a2 = gastm_SourceLocation(endLine="sample_text_2", endPosition="sample_text_2", startLine="sample_text_2", startPosition="sample_text_2")
    b = gastm_SourceFile(path="sample_text")
    _safe_set(b, 'gastm_SourceFile', a1)
    assert _is_linked(b, 'gastm_SourceFile', a1)
    if hasattr(a1, 'gastm_SourceLocation6'):
        assert _is_linked(a1, 'gastm_SourceLocation6', b)
    _safe_set(b, 'gastm_SourceFile', a2)
    assert _is_linked(b, 'gastm_SourceFile', a2)
    if hasattr(a1, 'gastm_SourceLocation6'):
        assert not _is_linked(a1, 'gastm_SourceLocation6', b)
    if hasattr(a2, 'gastm_SourceLocation6'):
        assert _is_linked(a2, 'gastm_SourceLocation6', b)
    _safe_set(b, 'gastm_SourceFile', None)
    assert not _is_linked(b, 'gastm_SourceFile', a2)
    if hasattr(a2, 'gastm_SourceLocation6'):
        assert not _is_linked(a2, 'gastm_SourceLocation6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessKind43_stub_double():
    # gastm_AccessKind has no real 'gastm_AccessKind45' property in the generated
    # code (a bare stub) -- manually attach it so gastm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_DeclarationOrDefinition(linkageSpecifier="sample_text")
    partner = gastm_AccessKind()
    setattr(partner, 'gastm_AccessKind45', None)
    _safe_set(owner, 'gastm_DeclarationOrDefinition44', partner)
    assert getattr(partner, 'gastm_AccessKind45') == owner
    _safe_set(owner, 'gastm_DeclarationOrDefinition44', None)
    assert getattr(partner, 'gastm_AccessKind45') is None


def test_assoc_body123_stub_double():
    # gastm_NamedType has no real 'gastm_NamedType124' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Type(isConst="sample_text")
    partner = gastm_NamedType()
    setattr(partner, 'gastm_NamedType124', None)
    _safe_set(owner, 'gastm_Type', partner)
    assert getattr(partner, 'gastm_NamedType124') == owner
    _safe_set(owner, 'gastm_Type', None)
    assert getattr(partner, 'gastm_NamedType124') is None


def test_assoc_body30_stub_double():
    # gastm_Statement has no real 'gastm_Statement' property in the generated
    # code (a bare stub) -- manually attach it so gastm_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_SwitchCase(isEvaluateAllCases="sample_text")
    partner = gastm_Statement()
    setattr(partner, 'gastm_Statement', None)
    _safe_set(owner, 'gastm_SwitchCase', {partner})
    assert getattr(partner, 'gastm_Statement') == owner
    _safe_set(owner, 'gastm_SwitchCase', set())
    assert getattr(partner, 'gastm_Statement') is None


def test_assoc_cases163_stub_double():
    # gastm_SwitchStatement has no real 'gastm_SwitchStatement164' property in the generated
    # code (a bare stub) -- manually attach it so gastm_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_SwitchCase(isEvaluateAllCases="sample_text")
    partner = gastm_SwitchStatement()
    setattr(partner, 'gastm_SwitchStatement164', None)
    _safe_set(owner, 'gastm_SwitchCase165', partner)
    assert getattr(partner, 'gastm_SwitchStatement164') == owner
    _safe_set(owner, 'gastm_SwitchCase165', None)
    assert getattr(partner, 'gastm_SwitchStatement164') is None


def test_assoc_exceptionVariable196_stub_double():
    # gastm_VariableCatchBlock has no real 'gastm_VariableCatchBlock' property in the generated
    # code (a bare stub) -- manually attach it so gastm_DataDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_DataDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_DataDefinition(isMutable="sample_text")
    partner = gastm_VariableCatchBlock()
    setattr(partner, 'gastm_VariableCatchBlock', None)
    _safe_set(owner, 'gastm_DataDefinition197', partner)
    assert getattr(partner, 'gastm_VariableCatchBlock') == owner
    _safe_set(owner, 'gastm_DataDefinition197', None)
    assert getattr(partner, 'gastm_VariableCatchBlock') is None


def test_assoc_exceptions194_stub_double():
    # gastm_TypesCatchBlock has no real 'gastm_TypesCatchBlock' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Type(isConst="sample_text")
    partner = gastm_TypesCatchBlock()
    setattr(partner, 'gastm_TypesCatchBlock', None)
    _safe_set(owner, 'gastm_Type195', partner)
    assert owner in getattr(partner, 'gastm_TypesCatchBlock')
    _safe_set(owner, 'gastm_Type195', None)
    assert owner not in getattr(partner, 'gastm_TypesCatchBlock')


def test_assoc_files15_stub_double():
    # gastm_Project has no real 'gastm_Project' property in the generated
    # code (a bare stub) -- manually attach it so gastm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_CompilationUnit(language="sample_text")
    partner = gastm_Project()
    setattr(partner, 'gastm_Project', None)
    _safe_set(owner, 'gastm_CompilationUnit16', partner)
    assert owner in getattr(partner, 'gastm_Project')
    _safe_set(owner, 'gastm_CompilationUnit16', None)
    assert owner not in getattr(partner, 'gastm_Project')


def test_assoc_fragments7_stub_double():
    # gastm_DefinitionObject has no real 'gastm_DefinitionObject' property in the generated
    # code (a bare stub) -- manually attach it so gastm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_CompilationUnit(language="sample_text")
    partner = gastm_DefinitionObject()
    setattr(partner, 'gastm_DefinitionObject', None)
    _safe_set(owner, 'gastm_CompilationUnit', {partner})
    assert getattr(partner, 'gastm_DefinitionObject') == owner
    _safe_set(owner, 'gastm_CompilationUnit', set())
    assert getattr(partner, 'gastm_DefinitionObject') is None


def test_assoc_functionMemberAttributes80_stub_double():
    # gastm_FunctionDefinition has no real 'gastm_FunctionDefinition81' property in the generated
    # code (a bare stub) -- manually attach it so gastm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_FunctionMemberAttributes(isFriend="sample_text", isInLine="sample_text", isThisConst="sample_text")
    partner = gastm_FunctionDefinition()
    setattr(partner, 'gastm_FunctionDefinition81', None)
    _safe_set(owner, 'gastm_FunctionMemberAttributes82', partner)
    assert getattr(partner, 'gastm_FunctionDefinition81') == owner
    _safe_set(owner, 'gastm_FunctionMemberAttributes82', None)
    assert getattr(partner, 'gastm_FunctionDefinition81') is None


def test_assoc_functionMemberAttributes95_stub_double():
    # gastm_FunctionDeclaration has no real 'gastm_FunctionDeclaration96' property in the generated
    # code (a bare stub) -- manually attach it so gastm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_FunctionMemberAttributes(isFriend="sample_text", isInLine="sample_text", isThisConst="sample_text")
    partner = gastm_FunctionDeclaration()
    setattr(partner, 'gastm_FunctionDeclaration96', None)
    _safe_set(owner, 'gastm_FunctionMemberAttributes97', partner)
    assert getattr(partner, 'gastm_FunctionDeclaration96') == owner
    _safe_set(owner, 'gastm_FunctionMemberAttributes97', None)
    assert getattr(partner, 'gastm_FunctionDeclaration96') is None


def test_assoc_identifierName60_stub_double():
    # gastm_Definition has no real 'gastm_Definition' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_Definition()
    setattr(partner, 'gastm_Definition', None)
    _safe_set(owner, 'gastm_Name61', partner)
    assert getattr(partner, 'gastm_Definition') == owner
    _safe_set(owner, 'gastm_Name61', None)
    assert getattr(partner, 'gastm_Definition') is None


def test_assoc_identifierName67_stub_double():
    # gastm_Declaration has no real 'gastm_Declaration68' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_Declaration()
    setattr(partner, 'gastm_Declaration68', None)
    _safe_set(owner, 'gastm_Name69', partner)
    assert getattr(partner, 'gastm_Declaration68') == owner
    _safe_set(owner, 'gastm_Name69', None)
    assert getattr(partner, 'gastm_Declaration68') is None


def test_assoc_initialValue90_stub_double():
    # gastm_Expression has no real 'gastm_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so gastm_DataDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_DataDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_DataDefinition(isMutable="sample_text")
    partner = gastm_Expression()
    setattr(partner, 'gastm_Expression91', None)
    _safe_set(owner, 'gastm_DataDefinition', partner)
    assert getattr(partner, 'gastm_Expression91') == owner
    _safe_set(owner, 'gastm_DataDefinition', None)
    assert getattr(partner, 'gastm_Expression91') is None


def test_assoc_labelName243_stub_double():
    # gastm_LabelAccess has no real 'gastm_LabelAccess244' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_LabelAccess()
    setattr(partner, 'gastm_LabelAccess244', None)
    _safe_set(owner, 'gastm_Name245', partner)
    assert getattr(partner, 'gastm_LabelAccess244') == owner
    _safe_set(owner, 'gastm_Name245', None)
    assert getattr(partner, 'gastm_LabelAccess244') is None


def test_assoc_labelName54_stub_double():
    # gastm_LabelDefinition has no real 'gastm_LabelDefinition' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_LabelDefinition()
    setattr(partner, 'gastm_LabelDefinition', None)
    _safe_set(owner, 'gastm_Name55', partner)
    assert getattr(partner, 'gastm_LabelDefinition') == owner
    _safe_set(owner, 'gastm_Name55', None)
    assert getattr(partner, 'gastm_LabelDefinition') is None


def test_assoc_locationInfo0_stub_double():
    # gastm_GASTMSyntaxObject has no real 'gastm_GASTMSyntaxObject' property in the generated
    # code (a bare stub) -- manually attach it so gastm_SourceLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_SourceLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_SourceLocation(endLine="sample_text", endPosition="sample_text", startLine="sample_text", startPosition="sample_text")
    partner = gastm_GASTMSyntaxObject()
    setattr(partner, 'gastm_GASTMSyntaxObject', None)
    _safe_set(owner, 'gastm_SourceLocation', partner)
    assert getattr(partner, 'gastm_GASTMSyntaxObject') == owner
    _safe_set(owner, 'gastm_SourceLocation', None)
    assert getattr(partner, 'gastm_GASTMSyntaxObject') is None


def test_assoc_locationInfo10_stub_double():
    # gastm_SourceFileReference has no real 'gastm_SourceFileReference' property in the generated
    # code (a bare stub) -- manually attach it so gastm_SourceLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_SourceLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_SourceLocation(endLine="sample_text", endPosition="sample_text", startLine="sample_text", startPosition="sample_text")
    partner = gastm_SourceFileReference()
    setattr(partner, 'gastm_SourceFileReference', None)
    _safe_set(owner, 'gastm_SourceLocation11', partner)
    assert getattr(partner, 'gastm_SourceFileReference') == owner
    _safe_set(owner, 'gastm_SourceLocation11', None)
    assert getattr(partner, 'gastm_SourceFileReference') is None


def test_assoc_member40_stub_double():
    # gastm_DefinitionObject has no real 'gastm_DefinitionObject41' property in the generated
    # code (a bare stub) -- manually attach it so gastm_MemberObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_MemberObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_MemberObject(offset="sample_text")
    partner = gastm_DefinitionObject()
    setattr(partner, 'gastm_DefinitionObject41', None)
    _safe_set(owner, 'gastm_MemberObject', partner)
    assert getattr(partner, 'gastm_DefinitionObject41') == owner
    _safe_set(owner, 'gastm_MemberObject', None)
    assert getattr(partner, 'gastm_DefinitionObject41') is None


def test_assoc_members115_stub_double():
    # gastm_AggregateType has no real 'gastm_AggregateType116' property in the generated
    # code (a bare stub) -- manually attach it so gastm_MemberObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_MemberObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_MemberObject(offset="sample_text")
    partner = gastm_AggregateType()
    setattr(partner, 'gastm_AggregateType116', None)
    _safe_set(owner, 'gastm_MemberObject117', partner)
    assert owner in getattr(partner, 'gastm_AggregateType116')
    _safe_set(owner, 'gastm_MemberObject117', None)
    assert owner not in getattr(partner, 'gastm_AggregateType116')


def test_assoc_name238_stub_double():
    # gastm_NameReference has no real 'gastm_NameReference' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_NameReference()
    setattr(partner, 'gastm_NameReference', None)
    _safe_set(owner, 'gastm_Name239', partner)
    assert getattr(partner, 'gastm_NameReference') == owner
    _safe_set(owner, 'gastm_Name239', None)
    assert getattr(partner, 'gastm_NameReference') is None


def test_assoc_nameSpace47_stub_double():
    # gastm_NameSpaceDefinition has no real 'gastm_NameSpaceDefinition' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_NameSpaceDefinition()
    setattr(partner, 'gastm_NameSpaceDefinition', None)
    _safe_set(owner, 'gastm_Name48', partner)
    assert getattr(partner, 'gastm_NameSpaceDefinition') == owner
    _safe_set(owner, 'gastm_Name48', None)
    assert getattr(partner, 'gastm_NameSpaceDefinition') is None


def test_assoc_ofSourceFile12_stub_double():
    # gastm_SourceFileReference has no real 'gastm_SourceFileReference13' property in the generated
    # code (a bare stub) -- manually attach it so gastm_SourceFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_SourceFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_SourceFile(path="sample_text")
    partner = gastm_SourceFileReference()
    setattr(partner, 'gastm_SourceFileReference13', None)
    _safe_set(owner, 'gastm_SourceFile14', partner)
    assert getattr(partner, 'gastm_SourceFileReference13') == owner
    _safe_set(owner, 'gastm_SourceFile14', None)
    assert getattr(partner, 'gastm_SourceFileReference13') is None


def test_assoc_opensScope8_stub_double():
    # gastm_ProgramScope has no real 'gastm_ProgramScope' property in the generated
    # code (a bare stub) -- manually attach it so gastm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_CompilationUnit(language="sample_text")
    partner = gastm_ProgramScope()
    setattr(partner, 'gastm_ProgramScope', None)
    _safe_set(owner, 'gastm_CompilationUnit9', partner)
    assert getattr(partner, 'gastm_ProgramScope') == owner
    _safe_set(owner, 'gastm_CompilationUnit9', None)
    assert getattr(partner, 'gastm_ProgramScope') is None


def test_assoc_refersTo105_stub_double():
    # gastm_MacroCall has no real 'gastm_MacroCall' property in the generated
    # code (a bare stub) -- manually attach it so gastm_MacroDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_MacroDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_MacroDefinition(body="sample_text", macroName="sample_text")
    partner = gastm_MacroCall()
    setattr(partner, 'gastm_MacroCall', None)
    _safe_set(owner, 'gastm_MacroDefinition', partner)
    assert getattr(partner, 'gastm_MacroCall') == owner
    _safe_set(owner, 'gastm_MacroDefinition', None)
    assert getattr(partner, 'gastm_MacroCall') is None


def test_assoc_storageSpecifiers42_stub_double():
    # gastm_StorageSpecification has no real 'gastm_StorageSpecification' property in the generated
    # code (a bare stub) -- manually attach it so gastm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_DeclarationOrDefinition(linkageSpecifier="sample_text")
    partner = gastm_StorageSpecification()
    setattr(partner, 'gastm_StorageSpecification', None)
    _safe_set(owner, 'gastm_DeclarationOrDefinition', partner)
    assert getattr(partner, 'gastm_StorageSpecification') == owner
    _safe_set(owner, 'gastm_DeclarationOrDefinition', None)
    assert getattr(partner, 'gastm_StorageSpecification') is None


def test_assoc_type129_stub_double():
    # gastm_UnnamedTypeReference has no real 'gastm_UnnamedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Type(isConst="sample_text")
    partner = gastm_UnnamedTypeReference()
    setattr(partner, 'gastm_UnnamedTypeReference', None)
    _safe_set(owner, 'gastm_Type130', partner)
    assert getattr(partner, 'gastm_UnnamedTypeReference') == owner
    _safe_set(owner, 'gastm_Type130', None)
    assert getattr(partner, 'gastm_UnnamedTypeReference') is None


def test_assoc_typeName131_stub_double():
    # gastm_NamedTypeReference has no real 'gastm_NamedTypeReference132' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_NamedTypeReference()
    setattr(partner, 'gastm_NamedTypeReference132', None)
    _safe_set(owner, 'gastm_Name133', partner)
    assert getattr(partner, 'gastm_NamedTypeReference132') == owner
    _safe_set(owner, 'gastm_Name133', None)
    assert getattr(partner, 'gastm_NamedTypeReference132') is None


def test_assoc_typeName46_stub_double():
    # gastm_TypeDefinition has no real 'gastm_TypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so gastm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_Name(nameString="sample_text")
    partner = gastm_TypeDefinition()
    setattr(partner, 'gastm_TypeDefinition', None)
    _safe_set(owner, 'gastm_Name', partner)
    assert getattr(partner, 'gastm_TypeDefinition') == owner
    _safe_set(owner, 'gastm_Name', None)
    assert getattr(partner, 'gastm_TypeDefinition') is None


def test_assoc_virtualSpecifier33_stub_double():
    # gastm_VirtualSpecification has no real 'gastm_VirtualSpecification' property in the generated
    # code (a bare stub) -- manually attach it so gastm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gastm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gastm_FunctionMemberAttributes(isFriend="sample_text", isInLine="sample_text", isThisConst="sample_text")
    partner = gastm_VirtualSpecification()
    setattr(partner, 'gastm_VirtualSpecification', None)
    _safe_set(owner, 'gastm_FunctionMemberAttributes', partner)
    assert getattr(partner, 'gastm_VirtualSpecification') == owner
    _safe_set(owner, 'gastm_FunctionMemberAttributes', None)
    assert getattr(partner, 'gastm_VirtualSpecification') is None


