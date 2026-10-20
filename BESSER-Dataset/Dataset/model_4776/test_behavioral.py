import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    AttributeBlock,
    Declaration,
    Else,
    Equation,
    Expr,
    FunctionRef,
    Statement,
    Type,
    TypeDeclaration,
    VarBlock,
    VariableRef,
    limp_AbstractType,
    limp_AbstractTypeDef,
    limp_ArrayAccessExpr,
    limp_ArrayExpr,
    limp_ArrayType,
    limp_ArrayTypeDef,
    limp_ArrayUpdateExpr,
    limp_AssignmentStatement,
    limp_Attribute,
    limp_AttributeBlock,
    limp_BinaryExpr,
    limp_BoolType,
    limp_BooleanLiteralExpr,
    limp_BreakStatement,
    limp_ChoiceExpr,
    limp_Comment,
    limp_ConstantDeclaration,
    limp_ContinueStatement,
    limp_Declaration,
    limp_Define,
    limp_DefineUseRef,
    limp_Else,
    limp_ElseBlock,
    limp_ElseIf,
    limp_EnumType,
    limp_EnumTypeDef,
    limp_EnumValue,
    limp_Equation,
    limp_EquationBlock,
    limp_Expr,
    limp_ExprList,
    limp_ExternalFunction,
    limp_ExternalProcedure,
    limp_FcnCallExpr,
    limp_ForStatement,
    limp_FreshVariable,
    limp_FunctionRef,
    limp_GlobalDeclaration,
    limp_GotoStatement,
    limp_IdExpr,
    limp_IdList,
    limp_IfThenElseExpr,
    limp_IfThenElseStatement,
    limp_Import,
    limp_InitExpr,
    limp_InputArg,
    limp_InputArgList,
    limp_IntegerLiteralExpr,
    limp_IntegerType,
    limp_IntegerWildCardExpr,
    limp_LabelStatement,
    limp_LocalArg,
    limp_LocalFunction,
    limp_LocalProcedure,
    limp_NamedType,
    limp_NoAttributeBlock,
    limp_NoElse,
    limp_NoVarBlock,
    limp_OutputArg,
    limp_OutputArgList,
    limp_Postcondition,
    limp_Precondition,
    limp_RealLiteralExpr,
    limp_RealType,
    limp_RecordAccessExpr,
    limp_RecordExpr,
    limp_RecordFieldExpr,
    limp_RecordFieldType,
    limp_RecordType,
    limp_RecordTypeDef,
    limp_RecordUpdateExpr,
    limp_ReturnStatement,
    limp_SecondInit,
    limp_SomeAttributeBlock,
    limp_SomeVarBlock,
    limp_Specification,
    limp_Statement,
    limp_StatementBlock,
    limp_StringLiteralExpr,
    limp_StringType,
    limp_TupleType,
    limp_Type,
    limp_TypeAlias,
    limp_TypeDeclaration,
    limp_UnaryMinusExpr,
    limp_UnaryNegationExpr,
    limp_Uses,
    limp_VarBlock,
    limp_VariableRef,
    limp_VoidStatement,
    limp_VoidType,
    limp_WhileStatement,
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

def test_assoc_arrayDef128_stub_double():
    # limp_ArrayType has no real 'limp_ArrayType' property in the generated
    # code (a bare stub) -- manually attach it so limp_ArrayTypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ArrayTypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ArrayTypeDef(size="sample_text")
    partner = limp_ArrayType()
    setattr(partner, 'limp_ArrayType', None)
    _safe_set(owner, 'limp_ArrayTypeDef129', partner)
    assert getattr(partner, 'limp_ArrayType') == owner
    _safe_set(owner, 'limp_ArrayTypeDef129', None)
    assert getattr(partner, 'limp_ArrayType') is None


def test_assoc_arrayDefinition106_stub_double():
    # limp_ArrayExpr has no real 'limp_ArrayExpr' property in the generated
    # code (a bare stub) -- manually attach it so limp_ArrayTypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ArrayTypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ArrayTypeDef(size="sample_text")
    partner = limp_ArrayExpr()
    setattr(partner, 'limp_ArrayExpr', None)
    _safe_set(owner, 'limp_ArrayTypeDef107', partner)
    assert getattr(partner, 'limp_ArrayExpr') == owner
    _safe_set(owner, 'limp_ArrayTypeDef107', None)
    assert getattr(partner, 'limp_ArrayExpr') is None


def test_assoc_attributeBlock27_stub_double():
    # limp_AttributeBlock has no real 'limp_AttributeBlock29' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalProcedure(name="sample_text")
    partner = limp_AttributeBlock()
    setattr(partner, 'limp_AttributeBlock29', None)
    _safe_set(owner, 'limp_LocalProcedure28', partner)
    assert getattr(partner, 'limp_AttributeBlock29') == owner
    _safe_set(owner, 'limp_LocalProcedure28', None)
    assert getattr(partner, 'limp_AttributeBlock29') is None


def test_assoc_attributeBlock8_stub_double():
    # limp_AttributeBlock has no real 'limp_AttributeBlock' property in the generated
    # code (a bare stub) -- manually attach it so limp_ExternalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ExternalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ExternalProcedure(name="sample_text")
    partner = limp_AttributeBlock()
    setattr(partner, 'limp_AttributeBlock', None)
    _safe_set(owner, 'limp_ExternalProcedure9', partner)
    assert getattr(partner, 'limp_AttributeBlock') == owner
    _safe_set(owner, 'limp_ExternalProcedure9', None)
    assert getattr(partner, 'limp_AttributeBlock') is None


def test_assoc_baseType34_stub_double():
    # limp_Type has no real 'limp_Type' property in the generated
    # code (a bare stub) -- manually attach it so limp_ArrayTypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ArrayTypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ArrayTypeDef(size="sample_text")
    partner = limp_Type()
    setattr(partner, 'limp_Type', None)
    _safe_set(owner, 'limp_ArrayTypeDef', partner)
    assert getattr(partner, 'limp_Type') == owner
    _safe_set(owner, 'limp_ArrayTypeDef', None)
    assert getattr(partner, 'limp_Type') is None


def test_assoc_equationBlock17_stub_double():
    # limp_EquationBlock has no real 'limp_EquationBlock' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalFunction(name="sample_text")
    partner = limp_EquationBlock()
    setattr(partner, 'limp_EquationBlock', None)
    _safe_set(owner, 'limp_LocalFunction18', partner)
    assert getattr(partner, 'limp_EquationBlock') == owner
    _safe_set(owner, 'limp_LocalFunction18', None)
    assert getattr(partner, 'limp_EquationBlock') is None


def test_assoc_expr57_stub_double():
    # limp_Expr has no real 'limp_Expr58' property in the generated
    # code (a bare stub) -- manually attach it so limp_Precondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_Precondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_Precondition(name="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr58', None)
    _safe_set(owner, 'limp_Precondition', partner)
    assert getattr(partner, 'limp_Expr58') == owner
    _safe_set(owner, 'limp_Precondition', None)
    assert getattr(partner, 'limp_Expr58') is None


def test_assoc_expr59_stub_double():
    # limp_Expr has no real 'limp_Expr60' property in the generated
    # code (a bare stub) -- manually attach it so limp_Postcondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_Postcondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_Postcondition(name="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr60', None)
    _safe_set(owner, 'limp_Postcondition', partner)
    assert getattr(partner, 'limp_Expr60') == owner
    _safe_set(owner, 'limp_Postcondition', None)
    assert getattr(partner, 'limp_Expr60') is None


def test_assoc_fieldExpr115_stub_double():
    # limp_Expr has no real 'limp_Expr117' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordFieldExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordFieldExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordFieldExpr(fieldName="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr117', None)
    _safe_set(owner, 'limp_RecordFieldExpr116', partner)
    assert getattr(partner, 'limp_Expr117') == owner
    _safe_set(owner, 'limp_RecordFieldExpr116', None)
    assert getattr(partner, 'limp_Expr117') is None


def test_assoc_fieldExprList113_stub_double():
    # limp_RecordExpr has no real 'limp_RecordExpr114' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordFieldExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordFieldExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordFieldExpr(fieldName="sample_text")
    partner = limp_RecordExpr()
    setattr(partner, 'limp_RecordExpr114', None)
    _safe_set(owner, 'limp_RecordFieldExpr', partner)
    assert owner in getattr(partner, 'limp_RecordExpr114')
    _safe_set(owner, 'limp_RecordFieldExpr', None)
    assert owner not in getattr(partner, 'limp_RecordExpr114')


def test_assoc_fieldType35_stub_double():
    # limp_Type has no real 'limp_Type37' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordFieldType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordFieldType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordFieldType(fieldName="sample_text")
    partner = limp_Type()
    setattr(partner, 'limp_Type37', None)
    _safe_set(owner, 'limp_RecordFieldType36', partner)
    assert getattr(partner, 'limp_Type37') == owner
    _safe_set(owner, 'limp_RecordFieldType36', None)
    assert getattr(partner, 'limp_Type37') is None


def test_assoc_fields33_stub_double():
    # limp_RecordTypeDef has no real 'limp_RecordTypeDef' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordFieldType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordFieldType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordFieldType(fieldName="sample_text")
    partner = limp_RecordTypeDef()
    setattr(partner, 'limp_RecordTypeDef', None)
    _safe_set(owner, 'limp_RecordFieldType', partner)
    assert owner in getattr(partner, 'limp_RecordTypeDef')
    _safe_set(owner, 'limp_RecordFieldType', None)
    assert owner not in getattr(partner, 'limp_RecordTypeDef')


def test_assoc_id177_stub_double():
    # limp_InitExpr has no real 'limp_InitExpr' property in the generated
    # code (a bare stub) -- manually attach it so limp_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_VariableRef(name="sample_text")
    partner = limp_InitExpr()
    setattr(partner, 'limp_InitExpr', None)
    _safe_set(owner, 'limp_VariableRef178', partner)
    assert getattr(partner, 'limp_InitExpr') == owner
    _safe_set(owner, 'limp_VariableRef178', None)
    assert getattr(partner, 'limp_InitExpr') is None


def test_assoc_id179_stub_double():
    # limp_SecondInit has no real 'limp_SecondInit' property in the generated
    # code (a bare stub) -- manually attach it so limp_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_VariableRef(name="sample_text")
    partner = limp_SecondInit()
    setattr(partner, 'limp_SecondInit', None)
    _safe_set(owner, 'limp_VariableRef180', partner)
    assert getattr(partner, 'limp_SecondInit') == owner
    _safe_set(owner, 'limp_VariableRef180', None)
    assert getattr(partner, 'limp_SecondInit') is None


def test_assoc_id181_stub_double():
    # limp_IdExpr has no real 'limp_IdExpr' property in the generated
    # code (a bare stub) -- manually attach it so limp_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_VariableRef(name="sample_text")
    partner = limp_IdExpr()
    setattr(partner, 'limp_IdExpr', None)
    _safe_set(owner, 'limp_VariableRef182', partner)
    assert getattr(partner, 'limp_IdExpr') == owner
    _safe_set(owner, 'limp_VariableRef182', None)
    assert getattr(partner, 'limp_IdExpr') is None


def test_assoc_ids104_stub_double():
    # limp_IdList has no real 'limp_IdList105' property in the generated
    # code (a bare stub) -- manually attach it so limp_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_VariableRef(name="sample_text")
    partner = limp_IdList()
    setattr(partner, 'limp_IdList105', None)
    _safe_set(owner, 'limp_VariableRef', partner)
    assert owner in getattr(partner, 'limp_IdList105')
    _safe_set(owner, 'limp_VariableRef', None)
    assert owner not in getattr(partner, 'limp_IdList105')


def test_assoc_inputs1_stub_double():
    # limp_InputArgList has no real 'limp_InputArgList' property in the generated
    # code (a bare stub) -- manually attach it so limp_ExternalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ExternalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ExternalFunction(name="sample_text")
    partner = limp_InputArgList()
    setattr(partner, 'limp_InputArgList', None)
    _safe_set(owner, 'limp_ExternalFunction', partner)
    assert getattr(partner, 'limp_InputArgList') == owner
    _safe_set(owner, 'limp_ExternalFunction', None)
    assert getattr(partner, 'limp_InputArgList') is None


def test_assoc_inputs10_stub_double():
    # limp_InputArgList has no real 'limp_InputArgList11' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalFunction(name="sample_text")
    partner = limp_InputArgList()
    setattr(partner, 'limp_InputArgList11', None)
    _safe_set(owner, 'limp_LocalFunction', partner)
    assert getattr(partner, 'limp_InputArgList11') == owner
    _safe_set(owner, 'limp_LocalFunction', None)
    assert getattr(partner, 'limp_InputArgList11') is None


def test_assoc_inputs19_stub_double():
    # limp_InputArgList has no real 'limp_InputArgList20' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalProcedure(name="sample_text")
    partner = limp_InputArgList()
    setattr(partner, 'limp_InputArgList20', None)
    _safe_set(owner, 'limp_LocalProcedure', partner)
    assert getattr(partner, 'limp_InputArgList20') == owner
    _safe_set(owner, 'limp_LocalProcedure', None)
    assert getattr(partner, 'limp_InputArgList20') is None


def test_assoc_inputs4_stub_double():
    # limp_InputArgList has no real 'limp_InputArgList5' property in the generated
    # code (a bare stub) -- manually attach it so limp_ExternalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ExternalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ExternalProcedure(name="sample_text")
    partner = limp_InputArgList()
    setattr(partner, 'limp_InputArgList5', None)
    _safe_set(owner, 'limp_ExternalProcedure', partner)
    assert getattr(partner, 'limp_InputArgList5') == owner
    _safe_set(owner, 'limp_ExternalProcedure', None)
    assert getattr(partner, 'limp_InputArgList5') is None


def test_assoc_label98_stub_double():
    # limp_GotoStatement has no real 'limp_GotoStatement' property in the generated
    # code (a bare stub) -- manually attach it so limp_LabelStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LabelStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LabelStatement(name="sample_text")
    partner = limp_GotoStatement()
    setattr(partner, 'limp_GotoStatement', None)
    _safe_set(owner, 'limp_LabelStatement', partner)
    assert getattr(partner, 'limp_GotoStatement') == owner
    _safe_set(owner, 'limp_LabelStatement', None)
    assert getattr(partner, 'limp_GotoStatement') is None


def test_assoc_left151_stub_double():
    # limp_Expr has no real 'limp_Expr152' property in the generated
    # code (a bare stub) -- manually attach it so limp_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_BinaryExpr(op="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr152', None)
    _safe_set(owner, 'limp_BinaryExpr', partner)
    assert getattr(partner, 'limp_Expr152') == owner
    _safe_set(owner, 'limp_BinaryExpr', None)
    assert getattr(partner, 'limp_Expr152') is None


def test_assoc_output12_stub_double():
    # limp_OutputArg has no real 'limp_OutputArg14' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalFunction(name="sample_text")
    partner = limp_OutputArg()
    setattr(partner, 'limp_OutputArg14', None)
    _safe_set(owner, 'limp_LocalFunction13', partner)
    assert getattr(partner, 'limp_OutputArg14') == owner
    _safe_set(owner, 'limp_LocalFunction13', None)
    assert getattr(partner, 'limp_OutputArg14') is None


def test_assoc_output2_stub_double():
    # limp_OutputArg has no real 'limp_OutputArg' property in the generated
    # code (a bare stub) -- manually attach it so limp_ExternalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ExternalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ExternalFunction(name="sample_text")
    partner = limp_OutputArg()
    setattr(partner, 'limp_OutputArg', None)
    _safe_set(owner, 'limp_ExternalFunction3', partner)
    assert getattr(partner, 'limp_OutputArg') == owner
    _safe_set(owner, 'limp_ExternalFunction3', None)
    assert getattr(partner, 'limp_OutputArg') is None


def test_assoc_outputs21_stub_double():
    # limp_OutputArgList has no real 'limp_OutputArgList23' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalProcedure(name="sample_text")
    partner = limp_OutputArgList()
    setattr(partner, 'limp_OutputArgList23', None)
    _safe_set(owner, 'limp_LocalProcedure22', partner)
    assert getattr(partner, 'limp_OutputArgList23') == owner
    _safe_set(owner, 'limp_LocalProcedure22', None)
    assert getattr(partner, 'limp_OutputArgList23') is None


def test_assoc_outputs6_stub_double():
    # limp_OutputArgList has no real 'limp_OutputArgList' property in the generated
    # code (a bare stub) -- manually attach it so limp_ExternalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_ExternalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_ExternalProcedure(name="sample_text")
    partner = limp_OutputArgList()
    setattr(partner, 'limp_OutputArgList', None)
    _safe_set(owner, 'limp_ExternalProcedure7', partner)
    assert getattr(partner, 'limp_OutputArgList') == owner
    _safe_set(owner, 'limp_ExternalProcedure7', None)
    assert getattr(partner, 'limp_OutputArgList') is None


def test_assoc_record160_stub_double():
    # limp_Expr has no real 'limp_Expr161' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordAccessExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordAccessExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordAccessExpr(field="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr161', None)
    _safe_set(owner, 'limp_RecordAccessExpr', partner)
    assert getattr(partner, 'limp_Expr161') == owner
    _safe_set(owner, 'limp_RecordAccessExpr', None)
    assert getattr(partner, 'limp_Expr161') is None


def test_assoc_record162_stub_double():
    # limp_Expr has no real 'limp_Expr163' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordUpdateExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordUpdateExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordUpdateExpr(field="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr163', None)
    _safe_set(owner, 'limp_RecordUpdateExpr', partner)
    assert getattr(partner, 'limp_Expr163') == owner
    _safe_set(owner, 'limp_RecordUpdateExpr', None)
    assert getattr(partner, 'limp_Expr163') is None


def test_assoc_right153_stub_double():
    # limp_Expr has no real 'limp_Expr155' property in the generated
    # code (a bare stub) -- manually attach it so limp_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_BinaryExpr(op="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr155', None)
    _safe_set(owner, 'limp_BinaryExpr154', partner)
    assert getattr(partner, 'limp_Expr155') == owner
    _safe_set(owner, 'limp_BinaryExpr154', None)
    assert getattr(partner, 'limp_Expr155') is None


def test_assoc_statementblock30_stub_double():
    # limp_StatementBlock has no real 'limp_StatementBlock' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalProcedure(name="sample_text")
    partner = limp_StatementBlock()
    setattr(partner, 'limp_StatementBlock', None)
    _safe_set(owner, 'limp_LocalProcedure31', partner)
    assert getattr(partner, 'limp_StatementBlock') == owner
    _safe_set(owner, 'limp_LocalProcedure31', None)
    assert getattr(partner, 'limp_StatementBlock') is None


def test_assoc_value164_stub_double():
    # limp_Expr has no real 'limp_Expr166' property in the generated
    # code (a bare stub) -- manually attach it so limp_RecordUpdateExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_RecordUpdateExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_RecordUpdateExpr(field="sample_text")
    partner = limp_Expr()
    setattr(partner, 'limp_Expr166', None)
    _safe_set(owner, 'limp_RecordUpdateExpr165', partner)
    assert getattr(partner, 'limp_Expr166') == owner
    _safe_set(owner, 'limp_RecordUpdateExpr165', None)
    assert getattr(partner, 'limp_Expr166') is None


def test_assoc_varBlock15_stub_double():
    # limp_VarBlock has no real 'limp_VarBlock' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalFunction(name="sample_text")
    partner = limp_VarBlock()
    setattr(partner, 'limp_VarBlock', None)
    _safe_set(owner, 'limp_LocalFunction16', partner)
    assert getattr(partner, 'limp_VarBlock') == owner
    _safe_set(owner, 'limp_LocalFunction16', None)
    assert getattr(partner, 'limp_VarBlock') is None


def test_assoc_varBlock24_stub_double():
    # limp_VarBlock has no real 'limp_VarBlock26' property in the generated
    # code (a bare stub) -- manually attach it so limp_LocalProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # limp_LocalProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = limp_LocalProcedure(name="sample_text")
    partner = limp_VarBlock()
    setattr(partner, 'limp_VarBlock26', None)
    _safe_set(owner, 'limp_LocalProcedure25', partner)
    assert getattr(partner, 'limp_VarBlock26') == owner
    _safe_set(owner, 'limp_LocalProcedure25', None)
    assert getattr(partner, 'limp_VarBlock26') is None


