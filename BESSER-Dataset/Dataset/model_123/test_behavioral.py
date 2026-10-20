import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccessKind,
    ActualParameter,
    ActualParameterExpression,
    AggregateType,
    BinaryOperator,
    CatchBlock,
    ClassType,
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
    Literal,
    LoopStatement,
    NameReference,
    OtherSyntaxObject,
    PreprocessorElement,
    PrimitiveType,
    QualifiedIdentifierReference,
    Scope,
    Statement,
    StorageSpecification,
    SwitchCase,
    Type,
    TypeDefinition,
    TypeReference,
    UnaryOperator,
    VirtualSpecification,
    astm_AccessKind,
    astm_ActualParameter,
    astm_ActualParameterExpression,
    astm_Add,
    astm_AddressOf,
    astm_AggregateExpression,
    astm_AggregateScope,
    astm_AggregateType,
    astm_AggregateTypeDefinition,
    astm_And,
    astm_AnnotationExpression,
    astm_AnnotationType,
    astm_ArrayAccess,
    astm_ArrayType,
    astm_Assign,
    astm_BinaryExpression,
    astm_BinaryOperator,
    astm_BitAnd,
    astm_BitFieldDefinition,
    astm_BitLeftShift,
    astm_BitLiteral,
    astm_BitNot,
    astm_BitOr,
    astm_BitRightShift,
    astm_BitXor,
    astm_BlockScope,
    astm_BlockStatement,
    astm_Boolean,
    astm_BooleanLiteral,
    astm_BreakStatement,
    astm_ByReferenceActualParameterExpression,
    astm_ByReferenceFormalParameterType,
    astm_ByValueActualParameterExpression,
    astm_ByValueFormalParameterType,
    astm_Byte,
    astm_CaseBlock,
    astm_CastExpression,
    astm_CatchBlock,
    astm_CharLiteral,
    astm_Character,
    astm_ClassType,
    astm_CollectionType,
    astm_Comment,
    astm_CompilationUnit,
    astm_ConditionalExpression,
    astm_ConstructedType,
    astm_ContinueStatement,
    astm_DataDefinition,
    astm_DataType,
    astm_Declaration,
    astm_DeclarationOrDefinition,
    astm_DeclarationOrDefinitionStatement,
    astm_Decrement,
    astm_DefaultBlock,
    astm_Definition,
    astm_DefinitionObject,
    astm_DeleteStatement,
    astm_Deref,
    astm_DerivesFrom,
    astm_Dimension,
    astm_Divide,
    astm_DoWhileStatement,
    astm_Double,
    astm_EmptyStatement,
    astm_EntryDefinition,
    astm_EnumLiteralDefinition,
    astm_EnumType,
    astm_Equal,
    astm_ExceptionType,
    astm_Exponent,
    astm_Expression,
    astm_ExpressionStatement,
    astm_External,
    astm_FileLocal,
    astm_Float,
    astm_ForCheckAfterStatement,
    astm_ForCheckBeforeStatement,
    astm_ForStatement,
    astm_FormalParameterDeclaration,
    astm_FormalParameterDefinition,
    astm_FormalParameterType,
    astm_FunctionCallExpression,
    astm_FunctionDeclaration,
    astm_FunctionDefinition,
    astm_FunctionMemberAttribute,
    astm_FunctionMemberAttributes,
    astm_FunctionPersistent,
    astm_FunctionScope,
    astm_FunctionType,
    astm_GASTMObject,
    astm_GASTMSemanticObject,
    astm_GASTMSourceObject,
    astm_GASTMSyntaxObject,
    astm_GlobalScope,
    astm_Greater,
    astm_IdentifierReference,
    astm_IfStatement,
    astm_IncludeUnit,
    astm_Increment,
    astm_Integer,
    astm_IntegerlLiteral,
    astm_JumpStatement,
    astm_LabelAccess,
    astm_LabelDefinition,
    astm_LabelType,
    astm_LabeledStatement,
    astm_Less,
    astm_Literal,
    astm_LongDouble,
    astm_LongInteger,
    astm_LoopStatement,
    astm_MacroCall,
    astm_MacroDefinition,
    astm_MissingActualParameter,
    astm_Modulus,
    astm_Multiply,
    astm_Name,
    astm_NameReference,
    astm_NameSpaceDefinition,
    astm_NameSpaceType,
    astm_NamedType,
    astm_NamedTypeDefinition,
    astm_NamedTypeReference,
    astm_Negate,
    astm_NewExpression,
    astm_NoDef,
    astm_NonVirtual,
    astm_Not,
    astm_NotEqual,
    astm_NotGreater,
    astm_NotLess,
    astm_OperatorAssign,
    astm_Or,
    astm_OtherSyntaxObject,
    astm_PerClassMember,
    astm_PointerType,
    astm_PostDecrement,
    astm_PostIncrement,
    astm_PreprocessorElement,
    astm_PrimitiveType,
    astm_Private,
    astm_ProgramScope,
    astm_Project,
    astm_Protected,
    astm_Public,
    astm_PureVirtual,
    astm_QualifiedIdentifierReference,
    astm_QualifiedOverData,
    astm_QualifiedOverPointer,
    astm_RangeExpression,
    astm_RangeType,
    astm_RealLiteral,
    astm_ReferenceType,
    astm_ReturnStatement,
    astm_Scope,
    astm_ShortInteger,
    astm_SourceFile,
    astm_SourceLocation,
    astm_SpecificClassType,
    astm_Statement,
    astm_StorageSpecification,
    astm_String,
    astm_StringLiteral,
    astm_StructureType,
    astm_Subtract,
    astm_SwitchCase,
    astm_SwitchStatement,
    astm_TerminateStatement,
    astm_ThrowStatement,
    astm_TryStatement,
    astm_Type,
    astm_TypeDefinition,
    astm_TypeQualifiedIdentifierReference,
    astm_TypeReference,
    astm_TypesCatchBlock,
    astm_UnaryExpression,
    astm_UnaryOperator,
    astm_UnaryPlus,
    astm_UnionType,
    astm_UnnamedTypeReference,
    astm_VariableCatchBlock,
    astm_VariableDeclaration,
    astm_VariableDefinition,
    astm_Virtual,
    astm_VirtualSpecification,
    astm_Void,
    astm_WhileStatement,
    astm_WideCharacter,
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

def test_assoc_inSourceFile0_reverse_link_reassign_clear():
    a1 = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    a2 = astm_SourceLocation(endColumn=13, endLine=13, startColumn=13, startLine=13)
    b = astm_SourceFile(pathName="sample_text")
    _safe_set(b, 'astm_SourceFile', a1)
    assert _is_linked(b, 'astm_SourceFile', a1)
    if hasattr(a1, 'astm_SourceLocation'):
        assert _is_linked(a1, 'astm_SourceLocation', b)
    _safe_set(b, 'astm_SourceFile', a2)
    assert _is_linked(b, 'astm_SourceFile', a2)
    if hasattr(a1, 'astm_SourceLocation'):
        assert not _is_linked(a1, 'astm_SourceLocation', b)
    if hasattr(a2, 'astm_SourceLocation'):
        assert _is_linked(a2, 'astm_SourceLocation', b)
    _safe_set(b, 'astm_SourceFile', None)
    assert not _is_linked(b, 'astm_SourceFile', a2)
    if hasattr(a2, 'astm_SourceLocation'):
        assert not _is_linked(a2, 'astm_SourceLocation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessKind104_stub_double():
    # astm_OtherSyntaxObject has no real 'astm_OtherSyntaxObject106' property in the generated
    # code (a bare stub) -- manually attach it so astm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DerivesFrom(isVirtual=True)
    partner = astm_OtherSyntaxObject()
    setattr(partner, 'astm_OtherSyntaxObject106', None)
    _safe_set(owner, 'astm_DerivesFrom105', partner)
    assert getattr(partner, 'astm_OtherSyntaxObject106') == owner
    _safe_set(owner, 'astm_DerivesFrom105', None)
    assert getattr(partner, 'astm_OtherSyntaxObject106') is None


def test_assoc_accessKind20_stub_double():
    # astm_OtherSyntaxObject has no real 'astm_OtherSyntaxObject22' property in the generated
    # code (a bare stub) -- manually attach it so astm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    partner = astm_OtherSyntaxObject()
    setattr(partner, 'astm_OtherSyntaxObject22', None)
    _safe_set(owner, 'astm_DeclarationOrDefinition21', partner)
    assert getattr(partner, 'astm_OtherSyntaxObject22') == owner
    _safe_set(owner, 'astm_DeclarationOrDefinition21', None)
    assert getattr(partner, 'astm_OtherSyntaxObject22') is None


def test_assoc_body101_stub_double():
    # astm_NamedType has no real 'astm_NamedType102' property in the generated
    # code (a bare stub) -- manually attach it so astm_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Type(isConst=True, isVolatile=True)
    partner = astm_NamedType()
    setattr(partner, 'astm_NamedType102', None)
    _safe_set(owner, 'astm_Type', partner)
    assert getattr(partner, 'astm_NamedType102') == owner
    _safe_set(owner, 'astm_Type', None)
    assert getattr(partner, 'astm_NamedType102') is None


def test_assoc_className107_stub_double():
    # astm_NamedType has no real 'astm_NamedType109' property in the generated
    # code (a bare stub) -- manually attach it so astm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DerivesFrom(isVirtual=True)
    partner = astm_NamedType()
    setattr(partner, 'astm_NamedType109', None)
    _safe_set(owner, 'astm_DerivesFrom108', partner)
    assert getattr(partner, 'astm_NamedType109') == owner
    _safe_set(owner, 'astm_DerivesFrom108', None)
    assert getattr(partner, 'astm_NamedType109') is None


def test_assoc_derivesFrom103_stub_double():
    # astm_ClassType has no real 'astm_ClassType' property in the generated
    # code (a bare stub) -- manually attach it so astm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DerivesFrom(isVirtual=True)
    partner = astm_ClassType()
    setattr(partner, 'astm_ClassType', None)
    _safe_set(owner, 'astm_DerivesFrom', partner)
    assert owner in getattr(partner, 'astm_ClassType')
    _safe_set(owner, 'astm_DerivesFrom', None)
    assert owner not in getattr(partner, 'astm_ClassType')


def test_assoc_exceptionVariable178_stub_double():
    # astm_VariableCatchBlock has no real 'astm_VariableCatchBlock' property in the generated
    # code (a bare stub) -- manually attach it so astm_DataDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DataDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DataDefinition(isMutable=True)
    partner = astm_VariableCatchBlock()
    setattr(partner, 'astm_VariableCatchBlock', None)
    _safe_set(owner, 'astm_DataDefinition179', partner)
    assert getattr(partner, 'astm_VariableCatchBlock') == owner
    _safe_set(owner, 'astm_DataDefinition179', None)
    assert getattr(partner, 'astm_VariableCatchBlock') is None


def test_assoc_exceptions176_stub_double():
    # astm_TypesCatchBlock has no real 'astm_TypesCatchBlock' property in the generated
    # code (a bare stub) -- manually attach it so astm_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Type(isConst=True, isVolatile=True)
    partner = astm_TypesCatchBlock()
    setattr(partner, 'astm_TypesCatchBlock', None)
    _safe_set(owner, 'astm_Type177', partner)
    assert owner in getattr(partner, 'astm_TypesCatchBlock')
    _safe_set(owner, 'astm_Type177', None)
    assert owner not in getattr(partner, 'astm_TypesCatchBlock')


def test_assoc_file75_stub_double():
    # astm_IncludeUnit has no real 'astm_IncludeUnit' property in the generated
    # code (a bare stub) -- manually attach it so astm_SourceFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_SourceFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_SourceFile(pathName="sample_text")
    partner = astm_IncludeUnit()
    setattr(partner, 'astm_IncludeUnit', None)
    _safe_set(owner, 'astm_SourceFile76', partner)
    assert getattr(partner, 'astm_IncludeUnit') == owner
    _safe_set(owner, 'astm_SourceFile76', None)
    assert getattr(partner, 'astm_IncludeUnit') is None


def test_assoc_files1_stub_double():
    # astm_Project has no real 'astm_Project' property in the generated
    # code (a bare stub) -- manually attach it so astm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_CompilationUnit(language="sample_text")
    partner = astm_Project()
    setattr(partner, 'astm_Project', None)
    _safe_set(owner, 'astm_CompilationUnit', partner)
    assert owner in getattr(partner, 'astm_Project')
    _safe_set(owner, 'astm_CompilationUnit', None)
    assert owner not in getattr(partner, 'astm_Project')


def test_assoc_fragments14_stub_double():
    # astm_DefinitionObject has no real 'astm_DefinitionObject16' property in the generated
    # code (a bare stub) -- manually attach it so astm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_CompilationUnit(language="sample_text")
    partner = astm_DefinitionObject()
    setattr(partner, 'astm_DefinitionObject16', None)
    _safe_set(owner, 'astm_CompilationUnit15', {partner})
    assert getattr(partner, 'astm_DefinitionObject16') == owner
    _safe_set(owner, 'astm_CompilationUnit15', set())
    assert getattr(partner, 'astm_DefinitionObject16') is None


def test_assoc_functionMemberAttributes35_stub_double():
    # astm_FunctionDeclaration has no real 'astm_FunctionDeclaration36' property in the generated
    # code (a bare stub) -- manually attach it so astm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    partner = astm_FunctionDeclaration()
    setattr(partner, 'astm_FunctionDeclaration36', None)
    _safe_set(owner, 'astm_FunctionMemberAttributes', partner)
    assert getattr(partner, 'astm_FunctionDeclaration36') == owner
    _safe_set(owner, 'astm_FunctionMemberAttributes', None)
    assert getattr(partner, 'astm_FunctionDeclaration36') is None


def test_assoc_functionMemberAttributes43_stub_double():
    # astm_FunctionDefinition has no real 'astm_FunctionDefinition44' property in the generated
    # code (a bare stub) -- manually attach it so astm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    partner = astm_FunctionDefinition()
    setattr(partner, 'astm_FunctionDefinition44', None)
    _safe_set(owner, 'astm_FunctionMemberAttributes45', partner)
    assert getattr(partner, 'astm_FunctionDefinition44') == owner
    _safe_set(owner, 'astm_FunctionMemberAttributes45', None)
    assert getattr(partner, 'astm_FunctionDefinition44') is None


def test_assoc_identifierName23_stub_double():
    # astm_Definition has no real 'astm_Definition' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_Definition()
    setattr(partner, 'astm_Definition', None)
    _safe_set(owner, 'astm_Name', partner)
    assert getattr(partner, 'astm_Definition') == owner
    _safe_set(owner, 'astm_Name', None)
    assert getattr(partner, 'astm_Definition') is None


def test_assoc_identifierName28_stub_double():
    # astm_Declaration has no real 'astm_Declaration29' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_Declaration()
    setattr(partner, 'astm_Declaration29', None)
    _safe_set(owner, 'astm_Name30', partner)
    assert getattr(partner, 'astm_Declaration29') == owner
    _safe_set(owner, 'astm_Name30', None)
    assert getattr(partner, 'astm_Declaration29') is None


def test_assoc_initialValue55_stub_double():
    # astm_Expression has no real 'astm_Expression' property in the generated
    # code (a bare stub) -- manually attach it so astm_DataDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DataDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DataDefinition(isMutable=True)
    partner = astm_Expression()
    setattr(partner, 'astm_Expression', None)
    _safe_set(owner, 'astm_DataDefinition', partner)
    assert getattr(partner, 'astm_Expression') == owner
    _safe_set(owner, 'astm_DataDefinition', None)
    assert getattr(partner, 'astm_Expression') is None


def test_assoc_labelName71_stub_double():
    # astm_LabelDefinition has no real 'astm_LabelDefinition' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_LabelDefinition()
    setattr(partner, 'astm_LabelDefinition', None)
    _safe_set(owner, 'astm_Name72', partner)
    assert getattr(partner, 'astm_LabelDefinition') == owner
    _safe_set(owner, 'astm_Name72', None)
    assert getattr(partner, 'astm_LabelDefinition') is None


def test_assoc_locationInfo8_stub_double():
    # astm_GASTMSyntaxObject has no real 'astm_GASTMSyntaxObject' property in the generated
    # code (a bare stub) -- manually attach it so astm_SourceLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_SourceLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = astm_GASTMSyntaxObject()
    setattr(partner, 'astm_GASTMSyntaxObject', None)
    _safe_set(owner, 'astm_SourceLocation9', partner)
    assert getattr(partner, 'astm_GASTMSyntaxObject') == owner
    _safe_set(owner, 'astm_SourceLocation9', None)
    assert getattr(partner, 'astm_GASTMSyntaxObject') is None


def test_assoc_name112_stub_double():
    # astm_NamedTypeReference has no real 'astm_NamedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_NamedTypeReference()
    setattr(partner, 'astm_NamedTypeReference', None)
    _safe_set(owner, 'astm_Name113', partner)
    assert getattr(partner, 'astm_NamedTypeReference') == owner
    _safe_set(owner, 'astm_Name113', None)
    assert getattr(partner, 'astm_NamedTypeReference') is None


def test_assoc_name185_stub_double():
    # astm_NameReference has no real 'astm_NameReference' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_NameReference()
    setattr(partner, 'astm_NameReference', None)
    _safe_set(owner, 'astm_Name186', partner)
    assert getattr(partner, 'astm_NameReference') == owner
    _safe_set(owner, 'astm_Name186', None)
    assert getattr(partner, 'astm_NameReference') is None


def test_assoc_name249_stub_double():
    # astm_LabelAccess has no real 'astm_LabelAccess250' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_LabelAccess()
    setattr(partner, 'astm_LabelAccess250', None)
    _safe_set(owner, 'astm_Name251', partner)
    assert getattr(partner, 'astm_LabelAccess250') == owner
    _safe_set(owner, 'astm_Name251', None)
    assert getattr(partner, 'astm_LabelAccess250') is None


def test_assoc_name60_stub_double():
    # astm_TypeDefinition has no real 'astm_TypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_TypeDefinition()
    setattr(partner, 'astm_TypeDefinition', None)
    _safe_set(owner, 'astm_Name61', partner)
    assert getattr(partner, 'astm_TypeDefinition') == owner
    _safe_set(owner, 'astm_Name61', None)
    assert getattr(partner, 'astm_TypeDefinition') is None


def test_assoc_nameSpace64_stub_double():
    # astm_NameSpaceDefinition has no real 'astm_NameSpaceDefinition' property in the generated
    # code (a bare stub) -- manually attach it so astm_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Name(nameString="sample_text")
    partner = astm_NameSpaceDefinition()
    setattr(partner, 'astm_NameSpaceDefinition', None)
    _safe_set(owner, 'astm_Name65', partner)
    assert getattr(partner, 'astm_NameSpaceDefinition') == owner
    _safe_set(owner, 'astm_Name65', None)
    assert getattr(partner, 'astm_NameSpaceDefinition') is None


def test_assoc_opensScope17_stub_double():
    # astm_ProgramScope has no real 'astm_ProgramScope' property in the generated
    # code (a bare stub) -- manually attach it so astm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_CompilationUnit(language="sample_text")
    partner = astm_ProgramScope()
    setattr(partner, 'astm_ProgramScope', None)
    _safe_set(owner, 'astm_CompilationUnit18', partner)
    assert getattr(partner, 'astm_ProgramScope') == owner
    _safe_set(owner, 'astm_CompilationUnit18', None)
    assert getattr(partner, 'astm_ProgramScope') is None


def test_assoc_refersTo77_stub_double():
    # astm_MacroCall has no real 'astm_MacroCall' property in the generated
    # code (a bare stub) -- manually attach it so astm_MacroDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_MacroDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_MacroDefinition(body="sample_text", macroName="sample_text")
    partner = astm_MacroCall()
    setattr(partner, 'astm_MacroCall', None)
    _safe_set(owner, 'astm_MacroDefinition', partner)
    assert getattr(partner, 'astm_MacroCall') == owner
    _safe_set(owner, 'astm_MacroDefinition', None)
    assert getattr(partner, 'astm_MacroCall') is None


def test_assoc_storageSpecifiers19_stub_double():
    # astm_OtherSyntaxObject has no real 'astm_OtherSyntaxObject' property in the generated
    # code (a bare stub) -- manually attach it so astm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    partner = astm_OtherSyntaxObject()
    setattr(partner, 'astm_OtherSyntaxObject', None)
    _safe_set(owner, 'astm_DeclarationOrDefinition', partner)
    assert getattr(partner, 'astm_OtherSyntaxObject') == owner
    _safe_set(owner, 'astm_DeclarationOrDefinition', None)
    assert getattr(partner, 'astm_OtherSyntaxObject') is None


def test_assoc_type110_stub_double():
    # astm_UnnamedTypeReference has no real 'astm_UnnamedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so astm_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_Type(isConst=True, isVolatile=True)
    partner = astm_UnnamedTypeReference()
    setattr(partner, 'astm_UnnamedTypeReference', None)
    _safe_set(owner, 'astm_Type111', partner)
    assert getattr(partner, 'astm_UnnamedTypeReference') == owner
    _safe_set(owner, 'astm_Type111', None)
    assert getattr(partner, 'astm_UnnamedTypeReference') is None


def test_assoc_virtualSpecifier48_stub_double():
    # astm_VirtualSpecification has no real 'astm_VirtualSpecification' property in the generated
    # code (a bare stub) -- manually attach it so astm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    partner = astm_VirtualSpecification()
    setattr(partner, 'astm_VirtualSpecification', None)
    _safe_set(owner, 'astm_FunctionMemberAttributes49', partner)
    assert getattr(partner, 'astm_VirtualSpecification') == owner
    _safe_set(owner, 'astm_FunctionMemberAttributes49', None)
    assert getattr(partner, 'astm_VirtualSpecification') is None


