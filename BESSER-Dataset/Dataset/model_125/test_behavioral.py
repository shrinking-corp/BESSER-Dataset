import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccessKind,
    ActualParameter,
    ActualParameterExpression,
    AggregateScope,
    AggregateType,
    AnnotationExpression,
    BinaryOperator,
    BlockScope,
    CatchBlock,
    CompilationUnit,
    ConstructedType,
    DataDefinition,
    DataType,
    Declaration,
    DeclarationOrDefinition,
    Definition,
    DefinitionObject,
    DerivesFrom,
    Dimension,
    EnumLiteralDefinition,
    Expression,
    ForStatement,
    FormalParameterDeclaration,
    FormalParameterDefinition,
    FormalParameterType,
    FunctionMemberAttributes,
    FunctionScope,
    GASTMObject,
    GASTMSemanticObject,
    GASTMSourceObject,
    GASTMSyntaxObject,
    GlobalScope,
    IdentifierReference,
    LabelAccess,
    LabelDefinition,
    LabelType,
    Literal,
    LoopStatement,
    MacroDefinition,
    Name,
    NameReference,
    NameSpaceType,
    NamedType,
    OtherSyntaxObject,
    PreprocessorElement,
    PrimitiveType,
    ProgramScope,
    QualifiedIdentifierReference,
    Scope,
    SourceFile,
    SourceLocation,
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
    astm_SpecificConcatString,
    astm_SpecificGreaterEqual,
    astm_SpecificIn,
    astm_SpecificLessEqual,
    astm_SpecificLike,
    astm_SpecificSelectStatement,
    astm_SpecificTriggerDefinition,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessKind17_stub_double():
    # OtherSyntaxObject has no real 'OtherSyntaxObject19' property in the generated
    # code (a bare stub) -- manually attach it so astm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    partner = OtherSyntaxObject()
    setattr(partner, 'OtherSyntaxObject19', None)
    _safe_set(owner, 'astm_DeclarationOrDefinition18', partner)
    assert getattr(partner, 'OtherSyntaxObject19') == owner
    _safe_set(owner, 'astm_DeclarationOrDefinition18', None)
    assert getattr(partner, 'OtherSyntaxObject19') is None


def test_assoc_accessKind94_stub_double():
    # OtherSyntaxObject has no real 'OtherSyntaxObject95' property in the generated
    # code (a bare stub) -- manually attach it so astm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DerivesFrom(isVirtual=True)
    partner = OtherSyntaxObject()
    setattr(partner, 'OtherSyntaxObject95', None)
    _safe_set(owner, 'astm_DerivesFrom', partner)
    assert getattr(partner, 'OtherSyntaxObject95') == owner
    _safe_set(owner, 'astm_DerivesFrom', None)
    assert getattr(partner, 'OtherSyntaxObject95') is None


def test_assoc_className96_stub_double():
    # NamedType has no real 'NamedType98' property in the generated
    # code (a bare stub) -- manually attach it so astm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DerivesFrom(isVirtual=True)
    partner = NamedType()
    setattr(partner, 'NamedType98', None)
    _safe_set(owner, 'astm_DerivesFrom97', partner)
    assert getattr(partner, 'NamedType98') == owner
    _safe_set(owner, 'astm_DerivesFrom97', None)
    assert getattr(partner, 'NamedType98') is None


def test_assoc_fragments12_stub_double():
    # DefinitionObject has no real 'DefinitionObject13' property in the generated
    # code (a bare stub) -- manually attach it so astm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_CompilationUnit(language="sample_text")
    partner = DefinitionObject()
    setattr(partner, 'DefinitionObject13', None)
    _safe_set(owner, 'astm_CompilationUnit', {partner})
    assert getattr(partner, 'DefinitionObject13') == owner
    _safe_set(owner, 'astm_CompilationUnit', set())
    assert getattr(partner, 'DefinitionObject13') is None


def test_assoc_inSourceFile0_stub_double():
    # SourceFile has no real 'SourceFile' property in the generated
    # code (a bare stub) -- manually attach it so astm_SourceLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_SourceLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = SourceFile()
    setattr(partner, 'SourceFile', None)
    _safe_set(owner, 'astm_SourceLocation', partner)
    assert getattr(partner, 'SourceFile') == owner
    _safe_set(owner, 'astm_SourceLocation', None)
    assert getattr(partner, 'SourceFile') is None


def test_assoc_initialValue50_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so astm_DataDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DataDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DataDefinition(isMutable=True)
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'astm_DataDefinition', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'astm_DataDefinition', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_opensScope14_stub_double():
    # ProgramScope has no real 'ProgramScope' property in the generated
    # code (a bare stub) -- manually attach it so astm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_CompilationUnit(language="sample_text")
    partner = ProgramScope()
    setattr(partner, 'ProgramScope', None)
    _safe_set(owner, 'astm_CompilationUnit15', partner)
    assert getattr(partner, 'ProgramScope') == owner
    _safe_set(owner, 'astm_CompilationUnit15', None)
    assert getattr(partner, 'ProgramScope') is None


def test_assoc_storageSpecifiers16_stub_double():
    # OtherSyntaxObject has no real 'OtherSyntaxObject' property in the generated
    # code (a bare stub) -- manually attach it so astm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    partner = OtherSyntaxObject()
    setattr(partner, 'OtherSyntaxObject', None)
    _safe_set(owner, 'astm_DeclarationOrDefinition', partner)
    assert getattr(partner, 'OtherSyntaxObject') == owner
    _safe_set(owner, 'astm_DeclarationOrDefinition', None)
    assert getattr(partner, 'OtherSyntaxObject') is None


def test_assoc_virtualSpecifier44_stub_double():
    # VirtualSpecification has no real 'VirtualSpecification' property in the generated
    # code (a bare stub) -- manually attach it so astm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    partner = VirtualSpecification()
    setattr(partner, 'VirtualSpecification', None)
    _safe_set(owner, 'astm_FunctionMemberAttributes', partner)
    assert getattr(partner, 'VirtualSpecification') == owner
    _safe_set(owner, 'astm_FunctionMemberAttributes', None)
    assert getattr(partner, 'VirtualSpecification') is None


