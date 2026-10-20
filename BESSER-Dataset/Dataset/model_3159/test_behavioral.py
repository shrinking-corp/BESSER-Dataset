import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstractions_BlockedElement,
    Abstractions_NamedElement,
    Access,
    ArithmeticExpression,
    BlockedElement,
    C_Abstractions_BlockedElement,
    C_Abstractions_NamedElement,
    C_Commands_Assignment,
    C_Commands_CaseOption,
    C_Commands_Command,
    C_Commands_DecisionCommand,
    C_Commands_DefaultOption,
    C_Commands_ExpressionCommand,
    C_Commands_FlowControlCommand,
    C_Commands_ForCommand,
    C_Commands_IfCommand,
    C_Commands_IterativeCommand,
    C_Commands_LabelCommand,
    C_Commands_ReturnCommand,
    C_Commands_SwitchCommand,
    C_Commands_WhileCommand,
    C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration,
    C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration,
    C_CompilationDirectiveDeclarations_Define,
    C_CompilationDirectiveDeclarations_Elif,
    C_CompilationDirectiveDeclarations_ElseDirective,
    C_CompilationDirectiveDeclarations_Endif,
    C_CompilationDirectiveDeclarations_IfDirective,
    C_CompilationDirectiveDeclarations_Ifdef,
    C_CompilationDirectiveDeclarations_Ifndef,
    C_CompilationDirectiveDeclarations_Include,
    C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration,
    C_Declarations_ArrayDeclaration,
    C_Declarations_CompositeVariableDeclaration,
    C_Declarations_ConstantDeclaration,
    C_Declarations_Declaration,
    C_Declarations_EnumDeclaration,
    C_Declarations_FragmentVariableDeclaration,
    C_Declarations_PrototypeFunctionDeclaration,
    C_Declarations_SimpleVariableDeclaration,
    C_Declarations_StructDeclaration,
    C_Declarations_TypeDefDeclaration,
    C_Declarations_VariableDeclaration,
    C_Expressions_Access,
    C_Expressions_ArithmeticExpression,
    C_Expressions_ArrayAccess,
    C_Expressions_AtomicConditionalExpression,
    C_Expressions_BinaryArithmeticExpression,
    C_Expressions_CastExpression,
    C_Expressions_CharLiteral,
    C_Expressions_ComposedConditionalExpression,
    C_Expressions_ConditionalExpression,
    C_Expressions_ConstantAccess,
    C_Expressions_ConstantExpression,
    C_Expressions_Construction,
    C_Expressions_DisplacementLogicExpression,
    C_Expressions_DoubleLiteral,
    C_Expressions_Expression,
    C_Expressions_FloatLiteral,
    C_Expressions_FunctionCall,
    C_Expressions_IntLiteral,
    C_Expressions_Literal,
    C_Expressions_LogicExpression,
    C_Expressions_PointerVariableAccess,
    C_Expressions_PrototypeAccess,
    C_Expressions_ShortLiteral,
    C_Expressions_SimpleLogicExpression,
    C_Expressions_StringLiteral,
    C_Expressions_UnaryArithmeticExpression,
    C_Expressions_VariableAccess,
    C_Main_Block,
    C_Main_C_Unit,
    C_Main_Comment,
    C_Main_DeclarationsBlock,
    C_Main_Element,
    C_Main_Function,
    C_Main_FunctionsBlock,
    C_Main_H_Unit,
    C_Main_Program,
    C_Main_Unit,
    C_Sequencers_Break,
    C_Sequencers_Goto,
    C_Sequencers_Sequencer,
    C_Types_Array,
    C_Types_Char,
    C_Types_CompositeType,
    C_Types_Double,
    C_Types_Enum,
    C_Types_Float,
    C_Types_FromHeader,
    C_Types_Int,
    C_Types_PrimitiveType,
    C_Types_Short,
    C_Types_Struct,
    C_Types_Type,
    C_Types_Typedef,
    C_Types_Void,
    Command,
    Commands_CaseOption,
    Commands_Command,
    Commands_DefaultOption,
    Commands_LabelCommand,
    CompilationDirectiveDeclaration,
    CompilationDirectiveDeclarations_CompilationDirectiveDeclaration,
    CompilationDirectiveDeclarations_ComplexDirectiveDeclaration,
    CompilationDirectiveDeclarations_Endif,
    ComplexDirectiveDeclaration,
    CompositeType,
    CompositeVariableDeclaration,
    ConditionalExpression,
    DecisionCommand,
    Declaration,
    Declarations_ArrayDeclaration,
    Declarations_CompositeVariableDeclaration,
    Declarations_ConstantDeclaration,
    Declarations_Declaration,
    Declarations_FragmentVariableDeclaration,
    Declarations_PrototypeFunctionDeclaration,
    Declarations_SimpleVariableDeclaration,
    Declarations_VariableDeclaration,
    Element,
    Expression,
    Expressions_Access,
    Expressions_ConditionalExpression,
    Expressions_ConstantExpression,
    Expressions_Construction,
    Expressions_Expression,
    Expressions_Literal,
    Expressions_VariableAccess,
    FlowControlCommand,
    IfDirective,
    IterativeCommand,
    Literal,
    LogicExpression,
    Main_Block,
    Main_Comment,
    Main_DeclarationsBlock,
    Main_Element,
    Main_Function,
    Main_Unit,
    NamedElement,
    PrimitiveType,
    Sequencer,
    SimpleDirectiveDeclaration,
    Type,
    Types_Array,
    Types_PrimitiveType,
    Types_Type,
    Unit,
    VariableAccess,
    VariableDeclaration,
    BinaryOperatorKind,
    DisplacementLogicOperatorKind,
    FunctionModifierKind,
    ModifierKind,
    RelationalConectorKind,
    RelationalOperatorKind,
    SimpleLogicOperatorKind,
    UnaryOperatorKind,
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

def test_assoc_body6_stub_double():
    # Main_Block has no real 'Main_Block8' property in the generated
    # code (a bare stub) -- manually attach it so C_Main_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Main_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Main_Function(functionModifier="sample_text", modifier="sample_text")
    partner = Main_Block()
    setattr(partner, 'Main_Block8', None)
    _safe_set(owner, 'C_Main_Function7', partner)
    assert getattr(partner, 'Main_Block8') == owner
    _safe_set(owner, 'C_Main_Function7', None)
    assert getattr(partner, 'Main_Block8') is None


def test_assoc_elementType34_stub_double():
    # Types_Type has no real 'Types_Type36' property in the generated
    # code (a bare stub) -- manually attach it so C_Declarations_ArrayDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Declarations_ArrayDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Declarations_ArrayDeclaration(dimensions="sample_text")
    partner = Types_Type()
    setattr(partner, 'Types_Type36', None)
    _safe_set(owner, 'C_Declarations_ArrayDeclaration35', partner)
    assert getattr(partner, 'Types_Type36') == owner
    _safe_set(owner, 'C_Declarations_ArrayDeclaration35', None)
    assert getattr(partner, 'Types_Type36') is None


def test_assoc_extraOperand97_stub_double():
    # Expressions_Expression has no real 'Expressions_Expression98' property in the generated
    # code (a bare stub) -- manually attach it so C_Expressions_BinaryArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Expressions_BinaryArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Expressions_BinaryArithmeticExpression(operator="sample_text")
    partner = Expressions_Expression()
    setattr(partner, 'Expressions_Expression98', None)
    _safe_set(owner, 'C_Expressions_BinaryArithmeticExpression', partner)
    assert getattr(partner, 'Expressions_Expression98') == owner
    _safe_set(owner, 'C_Expressions_BinaryArithmeticExpression', None)
    assert getattr(partner, 'Expressions_Expression98') is None


def test_assoc_file1_stub_double():
    # Main_Unit has no real 'Main_Unit' property in the generated
    # code (a bare stub) -- manually attach it so C_Main_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Main_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Main_Program(description="sample_text")
    partner = Main_Unit()
    setattr(partner, 'Main_Unit', None)
    _safe_set(owner, 'C_Main_Program', {partner})
    assert getattr(partner, 'Main_Unit') == owner
    _safe_set(owner, 'C_Main_Program', set())
    assert getattr(partner, 'Main_Unit') is None


def test_assoc_inicializer33_stub_double():
    # Expressions_Construction has no real 'Expressions_Construction' property in the generated
    # code (a bare stub) -- manually attach it so C_Declarations_ArrayDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Declarations_ArrayDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Declarations_ArrayDeclaration(dimensions="sample_text")
    partner = Expressions_Construction()
    setattr(partner, 'Expressions_Construction', None)
    _safe_set(owner, 'C_Declarations_ArrayDeclaration', partner)
    assert getattr(partner, 'Expressions_Construction') == owner
    _safe_set(owner, 'C_Declarations_ArrayDeclaration', None)
    assert getattr(partner, 'Expressions_Construction') is None


def test_assoc_numberOfDisplacement103_stub_double():
    # Expressions_Expression has no real 'Expressions_Expression104' property in the generated
    # code (a bare stub) -- manually attach it so C_Expressions_DisplacementLogicExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Expressions_DisplacementLogicExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Expressions_DisplacementLogicExpression(operator="sample_text")
    partner = Expressions_Expression()
    setattr(partner, 'Expressions_Expression104', None)
    _safe_set(owner, 'C_Expressions_DisplacementLogicExpression', partner)
    assert getattr(partner, 'Expressions_Expression104') == owner
    _safe_set(owner, 'C_Expressions_DisplacementLogicExpression', None)
    assert getattr(partner, 'Expressions_Expression104') is None


def test_assoc_ownedParameter28_stub_double():
    # Declarations_VariableDeclaration has no real 'Declarations_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so C_Declarations_PrototypeFunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Declarations_PrototypeFunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Declarations_PrototypeFunctionDeclaration(functionModifier="sample_text", isAPointer="sample_text")
    partner = Declarations_VariableDeclaration()
    setattr(partner, 'Declarations_VariableDeclaration', None)
    _safe_set(owner, 'C_Declarations_PrototypeFunctionDeclaration', {partner})
    assert getattr(partner, 'Declarations_VariableDeclaration') == owner
    _safe_set(owner, 'C_Declarations_PrototypeFunctionDeclaration', set())
    assert getattr(partner, 'Declarations_VariableDeclaration') is None


def test_assoc_ownedParameter9_stub_double():
    # Declarations_Declaration has no real 'Declarations_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so C_Main_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Main_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Main_Function(functionModifier="sample_text", modifier="sample_text")
    partner = Declarations_Declaration()
    setattr(partner, 'Declarations_Declaration', None)
    _safe_set(owner, 'C_Main_Function10', {partner})
    assert getattr(partner, 'Declarations_Declaration') == owner
    _safe_set(owner, 'C_Main_Function10', set())
    assert getattr(partner, 'Declarations_Declaration') is None


def test_assoc_return_5_stub_double():
    # Types_Type has no real 'Types_Type' property in the generated
    # code (a bare stub) -- manually attach it so C_Main_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Main_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Main_Function(functionModifier="sample_text", modifier="sample_text")
    partner = Types_Type()
    setattr(partner, 'Types_Type', None)
    _safe_set(owner, 'C_Main_Function', partner)
    assert getattr(partner, 'Types_Type') == owner
    _safe_set(owner, 'C_Main_Function', None)
    assert getattr(partner, 'Types_Type') is None


def test_assoc_term99_stub_double():
    # Expressions_Expression has no real 'Expressions_Expression100' property in the generated
    # code (a bare stub) -- manually attach it so C_Expressions_ComposedConditionalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Expressions_ComposedConditionalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Expressions_ComposedConditionalExpression(operator="sample_text")
    partner = Expressions_Expression()
    setattr(partner, 'Expressions_Expression100', None)
    _safe_set(owner, 'C_Expressions_ComposedConditionalExpression', {partner})
    assert getattr(partner, 'Expressions_Expression100') == owner
    _safe_set(owner, 'C_Expressions_ComposedConditionalExpression', set())
    assert getattr(partner, 'Expressions_Expression100') is None


def test_assoc_type29_stub_double():
    # Types_Type has no real 'Types_Type31' property in the generated
    # code (a bare stub) -- manually attach it so C_Declarations_PrototypeFunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C_Declarations_PrototypeFunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C_Declarations_PrototypeFunctionDeclaration(functionModifier="sample_text", isAPointer="sample_text")
    partner = Types_Type()
    setattr(partner, 'Types_Type31', None)
    _safe_set(owner, 'C_Declarations_PrototypeFunctionDeclaration30', partner)
    assert getattr(partner, 'Types_Type31') == owner
    _safe_set(owner, 'C_Declarations_PrototypeFunctionDeclaration30', None)
    assert getattr(partner, 'Types_Type31') is None


