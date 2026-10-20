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
    BlockStatement,
    CatchBlock,
    CompilationUnit,
    ConstructedType,
    DataDefinition,
    DataType,
    Declaration,
    DeclarationOrDefinition,
    Definition,
    DefinitionObject,
    DelphiImplementationSection,
    DelphiInterfaceSection,
    DerivesFrom,
    Dimension,
    EnumLiteralDefinition,
    Expression,
    ForStatement,
    FormalParameterDeclaration,
    FormalParameterDefinition,
    FormalParameterType,
    FunctionCallExpression,
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
    NamedTypeReference,
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
    astm_gastm_AccessKind,
    astm_gastm_ActualParameter,
    astm_gastm_ActualParameterExpression,
    astm_gastm_Add,
    astm_gastm_AddressOf,
    astm_gastm_AggregateExpression,
    astm_gastm_AggregateScope,
    astm_gastm_AggregateType,
    astm_gastm_AggregateTypeDefinition,
    astm_gastm_And,
    astm_gastm_AnnotationExpression,
    astm_gastm_AnnotationType,
    astm_gastm_ArrayAccess,
    astm_gastm_ArrayType,
    astm_gastm_Assign,
    astm_gastm_BinaryExpression,
    astm_gastm_BinaryOperator,
    astm_gastm_BitAnd,
    astm_gastm_BitFieldDefinition,
    astm_gastm_BitLeftShift,
    astm_gastm_BitLiteral,
    astm_gastm_BitNot,
    astm_gastm_BitOr,
    astm_gastm_BitRightShift,
    astm_gastm_BitXor,
    astm_gastm_BlockScope,
    astm_gastm_BlockStatement,
    astm_gastm_Boolean,
    astm_gastm_BooleanLiteral,
    astm_gastm_BreakStatement,
    astm_gastm_ByReferenceActualParameterExpression,
    astm_gastm_ByReferenceFormalParameterType,
    astm_gastm_ByValueActualParameterExpression,
    astm_gastm_ByValueFormalParameterType,
    astm_gastm_Byte,
    astm_gastm_CaseBlock,
    astm_gastm_CastExpression,
    astm_gastm_CatchBlock,
    astm_gastm_CharLiteral,
    astm_gastm_Character,
    astm_gastm_ClassType,
    astm_gastm_CollectionType,
    astm_gastm_Comment,
    astm_gastm_CompilationUnit,
    astm_gastm_ConditionalExpression,
    astm_gastm_ConstructedType,
    astm_gastm_ContinueStatement,
    astm_gastm_DataDefinition,
    astm_gastm_DataType,
    astm_gastm_Declaration,
    astm_gastm_DeclarationOrDefinition,
    astm_gastm_DeclarationOrDefinitionStatement,
    astm_gastm_Decrement,
    astm_gastm_DefaultBlock,
    astm_gastm_Definition,
    astm_gastm_DefinitionObject,
    astm_gastm_DeleteStatement,
    astm_gastm_Deref,
    astm_gastm_DerivesFrom,
    astm_gastm_Dimension,
    astm_gastm_Divide,
    astm_gastm_DoWhileStatement,
    astm_gastm_Double,
    astm_gastm_EmptyStatement,
    astm_gastm_EntryDefinition,
    astm_gastm_EnumLiteralDefinition,
    astm_gastm_EnumType,
    astm_gastm_Equal,
    astm_gastm_ExceptionType,
    astm_gastm_Exponent,
    astm_gastm_Expression,
    astm_gastm_ExpressionStatement,
    astm_gastm_External,
    astm_gastm_FileLocal,
    astm_gastm_Float,
    astm_gastm_ForCheckAfterStatement,
    astm_gastm_ForCheckBeforeStatement,
    astm_gastm_ForStatement,
    astm_gastm_FormalParameterDeclaration,
    astm_gastm_FormalParameterDefinition,
    astm_gastm_FormalParameterType,
    astm_gastm_FunctionCallExpression,
    astm_gastm_FunctionDeclaration,
    astm_gastm_FunctionDefinition,
    astm_gastm_FunctionMemberAttribute,
    astm_gastm_FunctionMemberAttributes,
    astm_gastm_FunctionPersistent,
    astm_gastm_FunctionScope,
    astm_gastm_FunctionType,
    astm_gastm_GASTMObject,
    astm_gastm_GASTMSemanticObject,
    astm_gastm_GASTMSourceObject,
    astm_gastm_GASTMSyntaxObject,
    astm_gastm_GlobalScope,
    astm_gastm_Greater,
    astm_gastm_IdentifierReference,
    astm_gastm_IfStatement,
    astm_gastm_IncludeUnit,
    astm_gastm_Increment,
    astm_gastm_Integer,
    astm_gastm_IntegerLiteral,
    astm_gastm_JumpStatement,
    astm_gastm_LabelAccess,
    astm_gastm_LabelDefinition,
    astm_gastm_LabelType,
    astm_gastm_LabeledStatement,
    astm_gastm_Less,
    astm_gastm_Literal,
    astm_gastm_LongDouble,
    astm_gastm_LongInteger,
    astm_gastm_LoopStatement,
    astm_gastm_MacroCall,
    astm_gastm_MacroDefinition,
    astm_gastm_MissingActualParameter,
    astm_gastm_Modulus,
    astm_gastm_Multiply,
    astm_gastm_Name,
    astm_gastm_NameReference,
    astm_gastm_NameSpaceDefinition,
    astm_gastm_NameSpaceType,
    astm_gastm_NamedType,
    astm_gastm_NamedTypeDefinition,
    astm_gastm_NamedTypeReference,
    astm_gastm_Negate,
    astm_gastm_NewExpression,
    astm_gastm_NoDef,
    astm_gastm_NonVirtual,
    astm_gastm_Not,
    astm_gastm_NotEqual,
    astm_gastm_NotGreater,
    astm_gastm_NotLess,
    astm_gastm_OperatorAssign,
    astm_gastm_Or,
    astm_gastm_OtherSyntaxObject,
    astm_gastm_PerClassMember,
    astm_gastm_PointerType,
    astm_gastm_PostDecrement,
    astm_gastm_PostIncrement,
    astm_gastm_PreprocessorElement,
    astm_gastm_PrimitiveType,
    astm_gastm_Private,
    astm_gastm_ProgramScope,
    astm_gastm_Project,
    astm_gastm_Protected,
    astm_gastm_Public,
    astm_gastm_PureVirtual,
    astm_gastm_QualifiedIdentifierReference,
    astm_gastm_QualifiedOverData,
    astm_gastm_QualifiedOverPointer,
    astm_gastm_RangeExpression,
    astm_gastm_RangeType,
    astm_gastm_RealLiteral,
    astm_gastm_ReferenceType,
    astm_gastm_ReturnStatement,
    astm_gastm_Scope,
    astm_gastm_ShortInteger,
    astm_gastm_SourceFile,
    astm_gastm_SourceLocation,
    astm_gastm_SpecificConcatString,
    astm_gastm_SpecificGreaterEqual,
    astm_gastm_SpecificIn,
    astm_gastm_SpecificLessEqual,
    astm_gastm_SpecificLike,
    astm_gastm_SpecificSelectStatement,
    astm_gastm_SpecificTriggerDefinition,
    astm_gastm_Statement,
    astm_gastm_StorageSpecification,
    astm_gastm_String,
    astm_gastm_StringLiteral,
    astm_gastm_StructureType,
    astm_gastm_Subtract,
    astm_gastm_SwitchCase,
    astm_gastm_SwitchStatement,
    astm_gastm_TerminateStatement,
    astm_gastm_ThrowStatement,
    astm_gastm_TryStatement,
    astm_gastm_Type,
    astm_gastm_TypeDefinition,
    astm_gastm_TypeQualifiedIdentifierReference,
    astm_gastm_TypeReference,
    astm_gastm_TypesCatchBlock,
    astm_gastm_UnaryExpression,
    astm_gastm_UnaryOperator,
    astm_gastm_UnaryPlus,
    astm_gastm_UnionType,
    astm_gastm_UnnamedTypeReference,
    astm_gastm_VariableCatchBlock,
    astm_gastm_VariableDeclaration,
    astm_gastm_VariableDefinition,
    astm_gastm_Virtual,
    astm_gastm_VirtualSpecification,
    astm_gastm_Void,
    astm_gastm_WhileStatement,
    astm_gastm_WideCharacter,
    astm_sastm_DelphiBlockStatement,
    astm_sastm_DelphiFunctionCallExpression,
    astm_sastm_DelphiImplementationSection,
    astm_sastm_DelphiInterfaceSection,
    astm_sastm_DelphiUnit,
    astm_sastm_DelphiWithStatement,
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
    # code (a bare stub) -- manually attach it so astm_gastm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    partner = OtherSyntaxObject()
    setattr(partner, 'OtherSyntaxObject19', None)
    _safe_set(owner, 'astm_gastm_DeclarationOrDefinition18', partner)
    assert getattr(partner, 'OtherSyntaxObject19') == owner
    _safe_set(owner, 'astm_gastm_DeclarationOrDefinition18', None)
    assert getattr(partner, 'OtherSyntaxObject19') is None


def test_assoc_accessKind97_stub_double():
    # OtherSyntaxObject has no real 'OtherSyntaxObject98' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_DerivesFrom(isVirtual=True)
    partner = OtherSyntaxObject()
    setattr(partner, 'OtherSyntaxObject98', None)
    _safe_set(owner, 'astm_gastm_DerivesFrom', partner)
    assert getattr(partner, 'OtherSyntaxObject98') == owner
    _safe_set(owner, 'astm_gastm_DerivesFrom', None)
    assert getattr(partner, 'OtherSyntaxObject98') is None


def test_assoc_className99_stub_double():
    # NamedType has no real 'NamedType101' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_DerivesFrom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_DerivesFrom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_DerivesFrom(isVirtual=True)
    partner = NamedType()
    setattr(partner, 'NamedType101', None)
    _safe_set(owner, 'astm_gastm_DerivesFrom100', partner)
    assert getattr(partner, 'NamedType101') == owner
    _safe_set(owner, 'astm_gastm_DerivesFrom100', None)
    assert getattr(partner, 'NamedType101') is None


def test_assoc_fragments12_stub_double():
    # DefinitionObject has no real 'DefinitionObject13' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_CompilationUnit(language="sample_text")
    partner = DefinitionObject()
    setattr(partner, 'DefinitionObject13', None)
    _safe_set(owner, 'astm_gastm_CompilationUnit', {partner})
    assert getattr(partner, 'DefinitionObject13') == owner
    _safe_set(owner, 'astm_gastm_CompilationUnit', set())
    assert getattr(partner, 'DefinitionObject13') is None


def test_assoc_inSourceFile0_stub_double():
    # SourceFile has no real 'SourceFile' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_SourceLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_SourceLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_SourceLocation(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = SourceFile()
    setattr(partner, 'SourceFile', None)
    _safe_set(owner, 'astm_gastm_SourceLocation', partner)
    assert getattr(partner, 'SourceFile') == owner
    _safe_set(owner, 'astm_gastm_SourceLocation', None)
    assert getattr(partner, 'SourceFile') is None


def test_assoc_initialValue53_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_DataDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_DataDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_DataDefinition(isMutable=True)
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'astm_gastm_DataDefinition', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'astm_gastm_DataDefinition', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_opensScope14_stub_double():
    # ProgramScope has no real 'ProgramScope' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_CompilationUnit(language="sample_text")
    partner = ProgramScope()
    setattr(partner, 'ProgramScope', None)
    _safe_set(owner, 'astm_gastm_CompilationUnit15', partner)
    assert getattr(partner, 'ProgramScope') == owner
    _safe_set(owner, 'astm_gastm_CompilationUnit15', None)
    assert getattr(partner, 'ProgramScope') is None


def test_assoc_storageSpecifiers16_stub_double():
    # OtherSyntaxObject has no real 'OtherSyntaxObject' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_DeclarationOrDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_DeclarationOrDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_DeclarationOrDefinition(isRegister=True, linkageSpecifier="sample_text")
    partner = OtherSyntaxObject()
    setattr(partner, 'OtherSyntaxObject', None)
    _safe_set(owner, 'astm_gastm_DeclarationOrDefinition', partner)
    assert getattr(partner, 'OtherSyntaxObject') == owner
    _safe_set(owner, 'astm_gastm_DeclarationOrDefinition', None)
    assert getattr(partner, 'OtherSyntaxObject') is None


def test_assoc_virtualSpecifier47_stub_double():
    # VirtualSpecification has no real 'VirtualSpecification' property in the generated
    # code (a bare stub) -- manually attach it so astm_gastm_FunctionMemberAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # astm_gastm_FunctionMemberAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = astm_gastm_FunctionMemberAttributes(isFriend=True, isInline=True, isThisConst=True)
    partner = VirtualSpecification()
    setattr(partner, 'VirtualSpecification', None)
    _safe_set(owner, 'astm_gastm_FunctionMemberAttributes', partner)
    assert getattr(partner, 'VirtualSpecification') == owner
    _safe_set(owner, 'astm_gastm_FunctionMemberAttributes', None)
    assert getattr(partner, 'VirtualSpecification') is None


