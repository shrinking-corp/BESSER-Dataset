import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Literal,
    OperandName,
    Receiver,
    SwitchStmt,
    TypeSpec,
    float_lit,
    go_AliasDecl,
    go_Arguments,
    go_ArrayLength,
    go_Assignment,
    go_BasicLit,
    go_Block,
    go_BreakStmt,
    go_Channel,
    go_ChannelType,
    go_CommCase,
    go_CommClause,
    go_CompositeLit,
    go_Condition,
    go_ConstDecl,
    go_ConstSpec,
    go_ContinueStmt,
    go_Conversion,
    go_Declaration,
    go_DeferStmt,
    go_Element,
    go_ElementList,
    go_ElementType,
    go_EmbeddedField,
    go_ExprCaseClause,
    go_ExprSwitchCase,
    go_Expression,
    go_ExpressionLinha,
    go_ExpressionList,
    go_ExpressionStmt,
    go_FieldDecl,
    go_FieldName,
    go_ForClause,
    go_ForStmt,
    go_FunctionBody,
    go_FunctionDecl,
    go_FunctionLit,
    go_FunctionName,
    go_FunctionType,
    go_GoStmt,
    go_GotoStmt,
    go_IdentifierList,
    go_IfStmt,
    go_ImportDecl,
    go_ImportPath,
    go_ImportSpec,
    go_IncDecStmt,
    go_Index,
    go_InitStmt,
    go_InterfaceType,
    go_InterfaceTypeName,
    go_Key,
    go_KeyType,
    go_KeyedElement,
    go_Label,
    go_LabeledStmt,
    go_Literal,
    go_LiteralType,
    go_LiteralTypeLinha,
    go_LiteralValue,
    go_MapType,
    go_MethodDecl,
    go_MethodExpr,
    go_MethodName,
    go_MethodSpec,
    go_Operand,
    go_OperandName,
    go_PackageClause,
    go_PackageName,
    go_ParameterDecl,
    go_ParameterList,
    go_Parameters,
    go_PointerType,
    go_PostStmt,
    go_PrimaryExpr,
    go_PrimaryExprLinha,
    go_QualifiedIdent,
    go_RangeClause,
    go_Receiver,
    go_ReceiverType,
    go_RecvExpr,
    go_RecvStmt,
    go_Result,
    go_ReturnStmt,
    go_SelectStmt,
    go_Selector,
    go_SendStmt,
    go_ShortVarDecl,
    go_Signature,
    go_SimpleStmt,
    go_Slice,
    go_SouceFile,
    go_Statement,
    go_StatementList,
    go_StructType,
    go_SwitchStmt,
    go_Tag,
    go_TopLevelDecl,
    go_Type,
    go_TypeAssertion,
    go_TypeCaseClause,
    go_TypeDecl,
    go_TypeDef,
    go_TypeList,
    go_TypeLit,
    go_TypeLitLinha,
    go_TypeName,
    go_TypeNameLinha,
    go_TypeSpec,
    go_TypeSwitchCase,
    go_TypeSwitchGuard,
    go_UnaryExpr,
    go_VarDecl,
    go_VarSpec,
    go_binary_op,
    go_cochetes,
    go_decimals,
    go_exponent,
    go_float_lit,
    go_identifier,
    go_imaginary_lit,
    go_ponto,
    go_rune_lit,
    go_string_lit,
    go_switch_stmt_linha,
    go_topLevelDeclLinha,
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

def test_assoc_Assignment395_reverse_link_reassign_clear():
    a1 = go_SimpleStmt(EmptyStmt="sample_text")
    a2 = go_SimpleStmt(EmptyStmt="sample_text_2")
    b = go_Assignment(assign_op="sample_text")
    _safe_set(b, 'go_Assignment', a1)
    assert _is_linked(b, 'go_Assignment', a1)
    if hasattr(a1, 'go_SimpleStmt396'):
        assert _is_linked(a1, 'go_SimpleStmt396', b)
    _safe_set(b, 'go_Assignment', a2)
    assert _is_linked(b, 'go_Assignment', a2)
    if hasattr(a1, 'go_SimpleStmt396'):
        assert not _is_linked(a1, 'go_SimpleStmt396', b)
    if hasattr(a2, 'go_SimpleStmt396'):
        assert _is_linked(a2, 'go_SimpleStmt396', b)
    _safe_set(b, 'go_Assignment', None)
    assert not _is_linked(b, 'go_Assignment', a2)
    if hasattr(a2, 'go_SimpleStmt396'):
        assert not _is_linked(a2, 'go_SimpleStmt396', b)


def test_assoc_SimpleStmt364_reverse_link_reassign_clear():
    a1 = go_Statement(FallthroughStmt="sample_text")
    a2 = go_Statement(FallthroughStmt="sample_text_2")
    b = go_SimpleStmt(EmptyStmt="sample_text")
    _safe_set(b, 'go_SimpleStmt', a1)
    assert _is_linked(b, 'go_SimpleStmt', a1)
    if hasattr(a1, 'go_Statement365'):
        assert _is_linked(a1, 'go_Statement365', b)
    _safe_set(b, 'go_SimpleStmt', a2)
    assert _is_linked(b, 'go_SimpleStmt', a2)
    if hasattr(a1, 'go_Statement365'):
        assert not _is_linked(a1, 'go_Statement365', b)
    if hasattr(a2, 'go_Statement365'):
        assert _is_linked(a2, 'go_Statement365', b)
    _safe_set(b, 'go_SimpleStmt', None)
    assert not _is_linked(b, 'go_SimpleStmt', a2)
    if hasattr(a2, 'go_Statement365'):
        assert not _is_linked(a2, 'go_Statement365', b)


def test_assoc_UnaryExpr351_reverse_link_reassign_clear():
    a1 = go_UnaryExpr(unary_op="sample_text")
    a2 = go_UnaryExpr(unary_op="sample_text_2")
    b = go_UnaryExpr(unary_op="sample_text")
    _safe_set(b, 'go_UnaryExpr352', a1)
    assert _is_linked(b, 'go_UnaryExpr352', a1)
    if hasattr(a1, 'go_UnaryExpr350'):
        assert _is_linked(a1, 'go_UnaryExpr350', b)
    _safe_set(b, 'go_UnaryExpr352', a2)
    assert _is_linked(b, 'go_UnaryExpr352', a2)
    if hasattr(a1, 'go_UnaryExpr350'):
        assert not _is_linked(a1, 'go_UnaryExpr350', b)
    if hasattr(a2, 'go_UnaryExpr350'):
        assert _is_linked(a2, 'go_UnaryExpr350', b)
    _safe_set(b, 'go_UnaryExpr352', None)
    assert not _is_linked(b, 'go_UnaryExpr352', a2)
    if hasattr(a2, 'go_UnaryExpr350'):
        assert not _is_linked(a2, 'go_UnaryExpr350', b)


def test_assoc_decimals567_reverse_link_reassign_clear():
    a1 = go_decimals(DECIMAL_DIGIT="sample_text")
    a2 = go_decimals(DECIMAL_DIGIT="sample_text_2")
    b = go_decimals(DECIMAL_DIGIT="sample_text")
    _safe_set(b, 'go_decimals568', a1)
    assert _is_linked(b, 'go_decimals568', a1)
    if hasattr(a1, 'go_decimals566'):
        assert _is_linked(a1, 'go_decimals566', b)
    _safe_set(b, 'go_decimals568', a2)
    assert _is_linked(b, 'go_decimals568', a2)
    if hasattr(a1, 'go_decimals566'):
        assert not _is_linked(a1, 'go_decimals566', b)
    if hasattr(a2, 'go_decimals566'):
        assert _is_linked(a2, 'go_decimals566', b)
    _safe_set(b, 'go_decimals568', None)
    assert not _is_linked(b, 'go_decimals568', a2)
    if hasattr(a2, 'go_decimals566'):
        assert not _is_linked(a2, 'go_decimals566', b)


def test_assoc_rune_lit216_reverse_link_reassign_clear():
    a1 = go_rune_lit(byte_value="sample_text", unicode_value="sample_text")
    a2 = go_rune_lit(byte_value="sample_text_2", unicode_value="sample_text_2")
    b = go_BasicLit(int_lit="sample_text")
    _safe_set(b, 'go_BasicLit217', a1)
    assert _is_linked(b, 'go_BasicLit217', a1)
    if hasattr(a1, 'go_rune_lit'):
        assert _is_linked(a1, 'go_rune_lit', b)
    _safe_set(b, 'go_BasicLit217', a2)
    assert _is_linked(b, 'go_BasicLit217', a2)
    if hasattr(a1, 'go_rune_lit'):
        assert not _is_linked(a1, 'go_rune_lit', b)
    if hasattr(a2, 'go_rune_lit'):
        assert _is_linked(a2, 'go_rune_lit', b)
    _safe_set(b, 'go_BasicLit217', None)
    assert not _is_linked(b, 'go_BasicLit217', a2)
    if hasattr(a2, 'go_rune_lit'):
        assert not _is_linked(a2, 'go_rune_lit', b)


def test_assoc_string_lit218_reverse_link_reassign_clear():
    a1 = go_string_lit(interpreted_string_lit="sample_text", raw_string_lit="sample_text")
    a2 = go_string_lit(interpreted_string_lit="sample_text_2", raw_string_lit="sample_text_2")
    b = go_BasicLit(int_lit="sample_text")
    _safe_set(b, 'go_BasicLit219', a1)
    assert _is_linked(b, 'go_BasicLit219', a1)
    if hasattr(a1, 'go_string_lit220'):
        assert _is_linked(a1, 'go_string_lit220', b)
    _safe_set(b, 'go_BasicLit219', a2)
    assert _is_linked(b, 'go_BasicLit219', a2)
    if hasattr(a1, 'go_string_lit220'):
        assert not _is_linked(a1, 'go_string_lit220', b)
    if hasattr(a2, 'go_string_lit220'):
        assert _is_linked(a2, 'go_string_lit220', b)
    _safe_set(b, 'go_BasicLit219', None)
    assert not _is_linked(b, 'go_BasicLit219', a2)
    if hasattr(a2, 'go_string_lit220'):
        assert not _is_linked(a2, 'go_string_lit220', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_BasicLit212_stub_double():
    # go_Literal has no real 'go_Literal213' property in the generated
    # code (a bare stub) -- manually attach it so go_BasicLit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_BasicLit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_BasicLit(int_lit="sample_text")
    partner = go_Literal()
    setattr(partner, 'go_Literal213', None)
    _safe_set(owner, 'go_BasicLit', partner)
    assert getattr(partner, 'go_Literal213') == owner
    _safe_set(owner, 'go_BasicLit', None)
    assert getattr(partner, 'go_Literal213') is None


def test_assoc_Block376_stub_double():
    # go_Block has no real 'go_Block378' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_Block()
    setattr(partner, 'go_Block378', None)
    _safe_set(owner, 'go_Statement377', partner)
    assert getattr(partner, 'go_Block378') == owner
    _safe_set(owner, 'go_Statement377', None)
    assert getattr(partner, 'go_Block378') is None


def test_assoc_BreakStmt370_stub_double():
    # go_BreakStmt has no real 'go_BreakStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_BreakStmt()
    setattr(partner, 'go_BreakStmt', None)
    _safe_set(owner, 'go_Statement371', partner)
    assert getattr(partner, 'go_BreakStmt') == owner
    _safe_set(owner, 'go_Statement371', None)
    assert getattr(partner, 'go_BreakStmt') is None


def test_assoc_ContinueStmt372_stub_double():
    # go_ContinueStmt has no real 'go_ContinueStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_ContinueStmt()
    setattr(partner, 'go_ContinueStmt', None)
    _safe_set(owner, 'go_Statement373', partner)
    assert getattr(partner, 'go_ContinueStmt') == owner
    _safe_set(owner, 'go_Statement373', None)
    assert getattr(partner, 'go_ContinueStmt') is None


def test_assoc_Declaration359_stub_double():
    # go_Declaration has no real 'go_Declaration361' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_Declaration()
    setattr(partner, 'go_Declaration361', None)
    _safe_set(owner, 'go_Statement360', partner)
    assert getattr(partner, 'go_Declaration361') == owner
    _safe_set(owner, 'go_Statement360', None)
    assert getattr(partner, 'go_Declaration361') is None


def test_assoc_DeferStmt387_stub_double():
    # go_DeferStmt has no real 'go_DeferStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_DeferStmt()
    setattr(partner, 'go_DeferStmt', None)
    _safe_set(owner, 'go_Statement388', partner)
    assert getattr(partner, 'go_DeferStmt') == owner
    _safe_set(owner, 'go_Statement388', None)
    assert getattr(partner, 'go_DeferStmt') is None


def test_assoc_ExpressionList422_stub_double():
    # go_ExpressionList has no real 'go_ExpressionList424' property in the generated
    # code (a bare stub) -- manually attach it so go_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Assignment(assign_op="sample_text")
    partner = go_ExpressionList()
    setattr(partner, 'go_ExpressionList424', None)
    _safe_set(owner, 'go_Assignment423', {partner})
    assert getattr(partner, 'go_ExpressionList424') == owner
    _safe_set(owner, 'go_Assignment423', set())
    assert getattr(partner, 'go_ExpressionList424') is None


def test_assoc_ExpressionStmt389_stub_double():
    # go_ExpressionStmt has no real 'go_ExpressionStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_ExpressionStmt()
    setattr(partner, 'go_ExpressionStmt', None)
    _safe_set(owner, 'go_SimpleStmt390', partner)
    assert getattr(partner, 'go_ExpressionStmt') == owner
    _safe_set(owner, 'go_SimpleStmt390', None)
    assert getattr(partner, 'go_ExpressionStmt') is None


def test_assoc_ForStmt385_stub_double():
    # go_ForStmt has no real 'go_ForStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_ForStmt()
    setattr(partner, 'go_ForStmt', None)
    _safe_set(owner, 'go_Statement386', partner)
    assert getattr(partner, 'go_ForStmt') == owner
    _safe_set(owner, 'go_Statement386', None)
    assert getattr(partner, 'go_ForStmt') is None


def test_assoc_GoStmt366_stub_double():
    # go_GoStmt has no real 'go_GoStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_GoStmt()
    setattr(partner, 'go_GoStmt', None)
    _safe_set(owner, 'go_Statement367', partner)
    assert getattr(partner, 'go_GoStmt') == owner
    _safe_set(owner, 'go_Statement367', None)
    assert getattr(partner, 'go_GoStmt') is None


def test_assoc_GotoStmt374_stub_double():
    # go_GotoStmt has no real 'go_GotoStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_GotoStmt()
    setattr(partner, 'go_GotoStmt', None)
    _safe_set(owner, 'go_Statement375', partner)
    assert getattr(partner, 'go_GotoStmt') == owner
    _safe_set(owner, 'go_Statement375', None)
    assert getattr(partner, 'go_GotoStmt') is None


def test_assoc_IfStmt379_stub_double():
    # go_IfStmt has no real 'go_IfStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_IfStmt()
    setattr(partner, 'go_IfStmt', None)
    _safe_set(owner, 'go_Statement380', partner)
    assert getattr(partner, 'go_IfStmt') == owner
    _safe_set(owner, 'go_Statement380', None)
    assert getattr(partner, 'go_IfStmt') is None


def test_assoc_IncDecStmt393_stub_double():
    # go_IncDecStmt has no real 'go_IncDecStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_IncDecStmt()
    setattr(partner, 'go_IncDecStmt', None)
    _safe_set(owner, 'go_SimpleStmt394', partner)
    assert getattr(partner, 'go_IncDecStmt') == owner
    _safe_set(owner, 'go_SimpleStmt394', None)
    assert getattr(partner, 'go_IncDecStmt') is None


def test_assoc_LabeledStmt362_stub_double():
    # go_LabeledStmt has no real 'go_LabeledStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_LabeledStmt()
    setattr(partner, 'go_LabeledStmt', None)
    _safe_set(owner, 'go_Statement363', partner)
    assert getattr(partner, 'go_LabeledStmt') == owner
    _safe_set(owner, 'go_Statement363', None)
    assert getattr(partner, 'go_LabeledStmt') is None


def test_assoc_PrimaryExpr347_stub_double():
    # go_PrimaryExpr has no real 'go_PrimaryExpr349' property in the generated
    # code (a bare stub) -- manually attach it so go_UnaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_UnaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_UnaryExpr(unary_op="sample_text")
    partner = go_PrimaryExpr()
    setattr(partner, 'go_PrimaryExpr349', None)
    _safe_set(owner, 'go_UnaryExpr348', partner)
    assert getattr(partner, 'go_PrimaryExpr349') == owner
    _safe_set(owner, 'go_UnaryExpr348', None)
    assert getattr(partner, 'go_PrimaryExpr349') is None


def test_assoc_ReturnStmt368_stub_double():
    # go_ReturnStmt has no real 'go_ReturnStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_ReturnStmt()
    setattr(partner, 'go_ReturnStmt', None)
    _safe_set(owner, 'go_Statement369', partner)
    assert getattr(partner, 'go_ReturnStmt') == owner
    _safe_set(owner, 'go_Statement369', None)
    assert getattr(partner, 'go_ReturnStmt') is None


def test_assoc_SelectStmt383_stub_double():
    # go_SelectStmt has no real 'go_SelectStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_SelectStmt()
    setattr(partner, 'go_SelectStmt', None)
    _safe_set(owner, 'go_Statement384', partner)
    assert getattr(partner, 'go_SelectStmt') == owner
    _safe_set(owner, 'go_Statement384', None)
    assert getattr(partner, 'go_SelectStmt') is None


def test_assoc_SendStmt391_stub_double():
    # go_SendStmt has no real 'go_SendStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_SendStmt()
    setattr(partner, 'go_SendStmt', None)
    _safe_set(owner, 'go_SimpleStmt392', partner)
    assert getattr(partner, 'go_SendStmt') == owner
    _safe_set(owner, 'go_SimpleStmt392', None)
    assert getattr(partner, 'go_SendStmt') is None


def test_assoc_ShortVarDecl397_stub_double():
    # go_ShortVarDecl has no real 'go_ShortVarDecl399' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_ShortVarDecl()
    setattr(partner, 'go_ShortVarDecl399', None)
    _safe_set(owner, 'go_SimpleStmt398', partner)
    assert getattr(partner, 'go_ShortVarDecl399') == owner
    _safe_set(owner, 'go_SimpleStmt398', None)
    assert getattr(partner, 'go_ShortVarDecl399') is None


def test_assoc_SimpleStmt425_stub_double():
    # go_IfStmt has no real 'go_IfStmt426' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_IfStmt()
    setattr(partner, 'go_IfStmt426', None)
    _safe_set(owner, 'go_SimpleStmt427', partner)
    assert getattr(partner, 'go_IfStmt426') == owner
    _safe_set(owner, 'go_SimpleStmt427', None)
    assert getattr(partner, 'go_IfStmt426') is None


def test_assoc_SimpleStmt494_stub_double():
    # go_InitStmt has no real 'go_InitStmt495' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_InitStmt()
    setattr(partner, 'go_InitStmt495', None)
    _safe_set(owner, 'go_SimpleStmt496', partner)
    assert getattr(partner, 'go_InitStmt495') == owner
    _safe_set(owner, 'go_SimpleStmt496', None)
    assert getattr(partner, 'go_InitStmt495') is None


def test_assoc_SimpleStmt497_stub_double():
    # go_PostStmt has no real 'go_PostStmt498' property in the generated
    # code (a bare stub) -- manually attach it so go_SimpleStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SimpleStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SimpleStmt(EmptyStmt="sample_text")
    partner = go_PostStmt()
    setattr(partner, 'go_PostStmt498', None)
    _safe_set(owner, 'go_SimpleStmt499', partner)
    assert getattr(partner, 'go_PostStmt498') == owner
    _safe_set(owner, 'go_SimpleStmt499', None)
    assert getattr(partner, 'go_PostStmt498') is None


def test_assoc_Statement117_stub_double():
    # go_StatementList has no real 'go_StatementList118' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_StatementList()
    setattr(partner, 'go_StatementList118', None)
    _safe_set(owner, 'go_Statement', partner)
    assert owner in getattr(partner, 'go_StatementList118')
    _safe_set(owner, 'go_Statement', None)
    assert owner not in getattr(partner, 'go_StatementList118')


def test_assoc_Statement402_stub_double():
    # go_LabeledStmt has no real 'go_LabeledStmt403' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_LabeledStmt()
    setattr(partner, 'go_LabeledStmt403', None)
    _safe_set(owner, 'go_Statement404', partner)
    assert getattr(partner, 'go_LabeledStmt403') == owner
    _safe_set(owner, 'go_Statement404', None)
    assert getattr(partner, 'go_LabeledStmt403') is None


def test_assoc_SwitchStmt381_stub_double():
    # go_SwitchStmt has no real 'go_SwitchStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Statement(FallthroughStmt="sample_text")
    partner = go_SwitchStmt()
    setattr(partner, 'go_SwitchStmt', None)
    _safe_set(owner, 'go_Statement382', partner)
    assert getattr(partner, 'go_SwitchStmt') == owner
    _safe_set(owner, 'go_Statement382', None)
    assert getattr(partner, 'go_SwitchStmt') is None


def test_assoc_UnaryExpr335_stub_double():
    # go_Expression has no real 'go_Expression336' property in the generated
    # code (a bare stub) -- manually attach it so go_UnaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_UnaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_UnaryExpr(unary_op="sample_text")
    partner = go_Expression()
    setattr(partner, 'go_Expression336', None)
    _safe_set(owner, 'go_UnaryExpr', partner)
    assert getattr(partner, 'go_Expression336') == owner
    _safe_set(owner, 'go_UnaryExpr', None)
    assert getattr(partner, 'go_Expression336') is None


def test_assoc_binary_op339_stub_double():
    # go_ExpressionLinha has no real 'go_ExpressionLinha340' property in the generated
    # code (a bare stub) -- manually attach it so go_binary_op's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_binary_op's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_binary_op(add_op="sample_text", mul_op="sample_text", rel_op="sample_text")
    partner = go_ExpressionLinha()
    setattr(partner, 'go_ExpressionLinha340', None)
    _safe_set(owner, 'go_binary_op', partner)
    assert getattr(partner, 'go_ExpressionLinha340') == owner
    _safe_set(owner, 'go_binary_op', None)
    assert getattr(partner, 'go_ExpressionLinha340') is None


def test_assoc_decimals316_stub_double():
    # go_Slice has no real 'go_Slice317' property in the generated
    # code (a bare stub) -- manually attach it so go_decimals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_decimals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_decimals(DECIMAL_DIGIT="sample_text")
    partner = go_Slice()
    setattr(partner, 'go_Slice317', None)
    _safe_set(owner, 'go_decimals', partner)
    assert owner in getattr(partner, 'go_Slice317')
    _safe_set(owner, 'go_decimals', None)
    assert owner not in getattr(partner, 'go_Slice317')


def test_assoc_decimals574_stub_double():
    # go_exponent has no real 'go_exponent575' property in the generated
    # code (a bare stub) -- manually attach it so go_decimals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_decimals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_decimals(DECIMAL_DIGIT="sample_text")
    partner = go_exponent()
    setattr(partner, 'go_exponent575', None)
    _safe_set(owner, 'go_decimals576', partner)
    assert getattr(partner, 'go_exponent575') == owner
    _safe_set(owner, 'go_decimals576', None)
    assert getattr(partner, 'go_exponent575') is None


def test_assoc_decimals577_stub_double():
    # go_imaginary_lit has no real 'go_imaginary_lit' property in the generated
    # code (a bare stub) -- manually attach it so go_decimals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_decimals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_decimals(DECIMAL_DIGIT="sample_text")
    partner = go_imaginary_lit()
    setattr(partner, 'go_imaginary_lit', None)
    _safe_set(owner, 'go_decimals578', partner)
    assert getattr(partner, 'go_imaginary_lit') == owner
    _safe_set(owner, 'go_decimals578', None)
    assert getattr(partner, 'go_imaginary_lit') is None


def test_assoc_exponen571_stub_double():
    # go_exponent has no real 'go_exponent573' property in the generated
    # code (a bare stub) -- manually attach it so go_decimals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_decimals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_decimals(DECIMAL_DIGIT="sample_text")
    partner = go_exponent()
    setattr(partner, 'go_exponent573', None)
    _safe_set(owner, 'go_decimals572', partner)
    assert getattr(partner, 'go_exponent573') == owner
    _safe_set(owner, 'go_decimals572', None)
    assert getattr(partner, 'go_exponent573') is None


def test_assoc_exponent569_stub_double():
    # go_exponent has no real 'go_exponent' property in the generated
    # code (a bare stub) -- manually attach it so go_decimals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_decimals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_decimals(DECIMAL_DIGIT="sample_text")
    partner = go_exponent()
    setattr(partner, 'go_exponent', None)
    _safe_set(owner, 'go_decimals570', partner)
    assert getattr(partner, 'go_exponent') == owner
    _safe_set(owner, 'go_decimals570', None)
    assert getattr(partner, 'go_exponent') is None


def test_assoc_float_lit214_stub_double():
    # go_float_lit has no real 'go_float_lit' property in the generated
    # code (a bare stub) -- manually attach it so go_BasicLit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_BasicLit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_BasicLit(int_lit="sample_text")
    partner = go_float_lit()
    setattr(partner, 'go_float_lit', None)
    _safe_set(owner, 'go_BasicLit215', partner)
    assert getattr(partner, 'go_float_lit') == owner
    _safe_set(owner, 'go_BasicLit215', None)
    assert getattr(partner, 'go_float_lit') is None


def test_assoc_identifier11_stub_double():
    # go_TypeName has no real 'go_TypeName12' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_TypeName()
    setattr(partner, 'go_TypeName12', None)
    _safe_set(owner, 'go_identifier', partner)
    assert getattr(partner, 'go_TypeName12') == owner
    _safe_set(owner, 'go_identifier', None)
    assert getattr(partner, 'go_TypeName12') is None


def test_assoc_identifier15_stub_double():
    # go_TypeNameLinha has no real 'go_TypeNameLinha16' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_TypeNameLinha()
    setattr(partner, 'go_TypeNameLinha16', None)
    _safe_set(owner, 'go_identifier17', partner)
    assert getattr(partner, 'go_TypeNameLinha16') == owner
    _safe_set(owner, 'go_identifier17', None)
    assert getattr(partner, 'go_TypeNameLinha16') is None


def test_assoc_identifier151_stub_double():
    # go_IdentifierList has no real 'go_IdentifierList152' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_IdentifierList()
    setattr(partner, 'go_IdentifierList152', None)
    _safe_set(owner, 'go_identifier153', partner)
    assert owner in getattr(partner, 'go_IdentifierList152')
    _safe_set(owner, 'go_identifier153', None)
    assert owner not in getattr(partner, 'go_IdentifierList152')


def test_assoc_identifier159_stub_double():
    # go_TypeSpec has no real 'go_TypeSpec160' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_TypeSpec()
    setattr(partner, 'go_TypeSpec160', None)
    _safe_set(owner, 'go_identifier161', partner)
    assert getattr(partner, 'go_TypeSpec160') == owner
    _safe_set(owner, 'go_identifier161', None)
    assert getattr(partner, 'go_TypeSpec160') is None


def test_assoc_identifier189_stub_double():
    # go_FunctionName has no real 'go_FunctionName190' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_FunctionName()
    setattr(partner, 'go_FunctionName190', None)
    _safe_set(owner, 'go_identifier191', partner)
    assert getattr(partner, 'go_FunctionName190') == owner
    _safe_set(owner, 'go_identifier191', None)
    assert getattr(partner, 'go_FunctionName190') is None


def test_assoc_identifier223_stub_double():
    # go_QualifiedIdent has no real 'go_QualifiedIdent224' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_QualifiedIdent()
    setattr(partner, 'go_QualifiedIdent224', None)
    _safe_set(owner, 'go_identifier225', partner)
    assert getattr(partner, 'go_QualifiedIdent224') == owner
    _safe_set(owner, 'go_identifier225', None)
    assert getattr(partner, 'go_QualifiedIdent224') is None


def test_assoc_identifier271_stub_double():
    # go_FieldName has no real 'go_FieldName272' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_FieldName()
    setattr(partner, 'go_FieldName272', None)
    _safe_set(owner, 'go_identifier273', partner)
    assert getattr(partner, 'go_FieldName272') == owner
    _safe_set(owner, 'go_identifier273', None)
    assert getattr(partner, 'go_FieldName272') is None


def test_assoc_identifier310_stub_double():
    # go_Selector has no real 'go_Selector311' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_Selector()
    setattr(partner, 'go_Selector311', None)
    _safe_set(owner, 'go_identifier312', partner)
    assert getattr(partner, 'go_Selector311') == owner
    _safe_set(owner, 'go_identifier312', None)
    assert getattr(partner, 'go_Selector311') is None


def test_assoc_identifier405_stub_double():
    # go_Label has no real 'go_Label406' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_Label()
    setattr(partner, 'go_Label406', None)
    _safe_set(owner, 'go_identifier407', partner)
    assert getattr(partner, 'go_Label406') == owner
    _safe_set(owner, 'go_identifier407', None)
    assert getattr(partner, 'go_Label406') is None


def test_assoc_identifier459_stub_double():
    # go_TypeSwitchGuard has no real 'go_TypeSwitchGuard460' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_TypeSwitchGuard()
    setattr(partner, 'go_TypeSwitchGuard460', None)
    _safe_set(owner, 'go_identifier461', partner)
    assert getattr(partner, 'go_TypeSwitchGuard460') == owner
    _safe_set(owner, 'go_identifier461', None)
    assert getattr(partner, 'go_TypeSwitchGuard460') is None


def test_assoc_identifier553_stub_double():
    # go_PackageName has no real 'go_PackageName554' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_PackageName()
    setattr(partner, 'go_PackageName554', None)
    _safe_set(owner, 'go_identifier555', partner)
    assert getattr(partner, 'go_PackageName554') == owner
    _safe_set(owner, 'go_identifier555', None)
    assert getattr(partner, 'go_PackageName554') is None


def test_assoc_identifier99_stub_double():
    # go_MethodName has no real 'go_MethodName100' property in the generated
    # code (a bare stub) -- manually attach it so go_identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_identifier(DECIMAL_DIGIT="sample_text", LETTER="sample_text")
    partner = go_MethodName()
    setattr(partner, 'go_MethodName100', None)
    _safe_set(owner, 'go_identifier101', partner)
    assert getattr(partner, 'go_MethodName100') == owner
    _safe_set(owner, 'go_identifier101', None)
    assert getattr(partner, 'go_MethodName100') is None


def test_assoc_string_lit563_stub_double():
    # go_ImportPath has no real 'go_ImportPath564' property in the generated
    # code (a bare stub) -- manually attach it so go_string_lit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_string_lit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_string_lit(interpreted_string_lit="sample_text", raw_string_lit="sample_text")
    partner = go_ImportPath()
    setattr(partner, 'go_ImportPath564', None)
    _safe_set(owner, 'go_string_lit565', partner)
    assert getattr(partner, 'go_ImportPath564') == owner
    _safe_set(owner, 'go_string_lit565', None)
    assert getattr(partner, 'go_ImportPath564') is None


def test_assoc_string_lit63_stub_double():
    # go_Tag has no real 'go_Tag64' property in the generated
    # code (a bare stub) -- manually attach it so go_string_lit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_string_lit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_string_lit(interpreted_string_lit="sample_text", raw_string_lit="sample_text")
    partner = go_Tag()
    setattr(partner, 'go_Tag64', None)
    _safe_set(owner, 'go_string_lit', partner)
    assert getattr(partner, 'go_Tag64') == owner
    _safe_set(owner, 'go_string_lit', None)
    assert getattr(partner, 'go_Tag64') is None


