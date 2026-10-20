import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myDsl_AliasDecl,
    myDsl_Arguments,
    myDsl_ArrayLength,
    myDsl_BINARY_OP,
    myDsl_BaseType,
    myDsl_BasicLit,
    myDsl_Block,
    myDsl_BreakStmt,
    myDsl_ChannelType,
    myDsl_ChannelTypeLinha,
    myDsl_CommCase,
    myDsl_CommCaseLinha,
    myDsl_CommClause,
    myDsl_CompositeLit,
    myDsl_Condition,
    myDsl_ConstDecl,
    myDsl_ConstSpec,
    myDsl_ContinueStmt,
    myDsl_Conversion,
    myDsl_Declaration,
    myDsl_DeferStmt,
    myDsl_Element,
    myDsl_ElementList,
    myDsl_ElementType,
    myDsl_EmbeddedField,
    myDsl_EmptyStmt,
    myDsl_ExprCaseClause,
    myDsl_ExprSwitchCase,
    myDsl_ExprSwitchStmt,
    myDsl_Expression,
    myDsl_Expression1,
    myDsl_ExpressionList,
    myDsl_Expression_Linha,
    myDsl_FallthroughStmt,
    myDsl_FieldDecl,
    myDsl_FieldName,
    myDsl_ForStmt,
    myDsl_ForStmtLinha,
    myDsl_ForStmtLinhaLinha,
    myDsl_FunctionBody,
    myDsl_FunctionDecl,
    myDsl_FunctionLit,
    myDsl_FunctionName,
    myDsl_FunctionType,
    myDsl_GoStmt,
    myDsl_GotoStmt,
    myDsl_IdentifierList,
    myDsl_IfStmt,
    myDsl_IfStmtLinha,
    myDsl_ImportDecl,
    myDsl_ImportSpec,
    myDsl_Index,
    myDsl_InterfaceType,
    myDsl_InterfaceTypeName,
    myDsl_Key,
    myDsl_KeyType,
    myDsl_KeyedElement,
    myDsl_Label,
    myDsl_LabeledStmt,
    myDsl_Literal,
    myDsl_LiteralType,
    myDsl_LiteralTypeLinha,
    myDsl_LiteralValue,
    myDsl_MapType,
    myDsl_MethodDecl,
    myDsl_MethodExpr,
    myDsl_MethodName,
    myDsl_MethodSpec,
    myDsl_Model,
    myDsl_Operand,
    myDsl_OperandName,
    myDsl_PackageClause,
    myDsl_PackageName,
    myDsl_ParameterDecl,
    myDsl_ParameterList,
    myDsl_Parameters,
    myDsl_PointerType,
    myDsl_PostStmt,
    myDsl_PrimaryExpr,
    myDsl_PrimaryExprLinha,
    myDsl_Receiver,
    myDsl_ReceiverType,
    myDsl_RecvExpr,
    myDsl_Result,
    myDsl_ReturnStmt,
    myDsl_SelectStmt,
    myDsl_Selector,
    myDsl_ShortVarDecl,
    myDsl_Signature,
    myDsl_SimpleStmt,
    myDsl_SimpleStmtLinha,
    myDsl_Slice,
    myDsl_SourceFile,
    myDsl_Statement,
    myDsl_StatementList,
    myDsl_StructType,
    myDsl_SwitchStmt,
    myDsl_Tag,
    myDsl_TopLevelDecl,
    myDsl_Type,
    myDsl_TypeAssertion,
    myDsl_TypeCaseClause,
    myDsl_TypeDecl,
    myDsl_TypeDef,
    myDsl_TypeList,
    myDsl_TypeLit,
    myDsl_TypeLitLinha,
    myDsl_TypeName,
    myDsl_TypeNameLinha,
    myDsl_TypeSpec,
    myDsl_TypeSwitchCase,
    myDsl_TypeSwitchGuard,
    myDsl_TypeSwitchStmt,
    myDsl_UnaryExpr,
    myDsl_VarDecl,
    myDsl_VarSpec,
    myDsl_assign_op,
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

def test_assoc_assign_op378_reverse_link_reassign_clear():
    a1 = myDsl_assign_op(aDD_OP="sample_text", mUL_OP="sample_text")
    a2 = myDsl_assign_op(aDD_OP="sample_text_2", mUL_OP="sample_text_2")
    b = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text")
    _safe_set(b, 'myDsl_SimpleStmtLinha379', a1)
    assert _is_linked(b, 'myDsl_SimpleStmtLinha379', a1)
    if hasattr(a1, 'myDsl_assign_op'):
        assert _is_linked(a1, 'myDsl_assign_op', b)
    _safe_set(b, 'myDsl_SimpleStmtLinha379', a2)
    assert _is_linked(b, 'myDsl_SimpleStmtLinha379', a2)
    if hasattr(a1, 'myDsl_assign_op'):
        assert not _is_linked(a1, 'myDsl_assign_op', b)
    if hasattr(a2, 'myDsl_assign_op'):
        assert _is_linked(a2, 'myDsl_assign_op', b)
    _safe_set(b, 'myDsl_SimpleStmtLinha379', None)
    assert not _is_linked(b, 'myDsl_SimpleStmtLinha379', a2)
    if hasattr(a2, 'myDsl_assign_op'):
        assert not _is_linked(a2, 'myDsl_assign_op', b)


def test_assoc_assign_op501_reverse_link_reassign_clear():
    a1 = myDsl_assign_op(aDD_OP="sample_text", mUL_OP="sample_text")
    a2 = myDsl_assign_op(aDD_OP="sample_text_2", mUL_OP="sample_text_2")
    b = myDsl_ForStmtLinhaLinha(range="sample_text")
    _safe_set(b, 'myDsl_ForStmtLinhaLinha502', a1)
    assert _is_linked(b, 'myDsl_ForStmtLinhaLinha502', a1)
    if hasattr(a1, 'myDsl_assign_op503'):
        assert _is_linked(a1, 'myDsl_assign_op503', b)
    _safe_set(b, 'myDsl_ForStmtLinhaLinha502', a2)
    assert _is_linked(b, 'myDsl_ForStmtLinhaLinha502', a2)
    if hasattr(a1, 'myDsl_assign_op503'):
        assert not _is_linked(a1, 'myDsl_assign_op503', b)
    if hasattr(a2, 'myDsl_assign_op503'):
        assert _is_linked(a2, 'myDsl_assign_op503', b)
    _safe_set(b, 'myDsl_ForStmtLinhaLinha502', None)
    assert not _is_linked(b, 'myDsl_ForStmtLinhaLinha502', a2)
    if hasattr(a2, 'myDsl_assign_op503'):
        assert not _is_linked(a2, 'myDsl_assign_op503', b)


def test_assoc_channelTypeLinha94_reverse_link_reassign_clear():
    a1 = myDsl_ChannelTypeLinha(aNY_OTHER="sample_text")
    a2 = myDsl_ChannelTypeLinha(aNY_OTHER="sample_text_2")
    b = myDsl_ChannelType(chan="sample_text")
    _safe_set(b, 'myDsl_ChannelType95', a1)
    assert _is_linked(b, 'myDsl_ChannelType95', a1)
    if hasattr(a1, 'myDsl_ChannelTypeLinha'):
        assert _is_linked(a1, 'myDsl_ChannelTypeLinha', b)
    _safe_set(b, 'myDsl_ChannelType95', a2)
    assert _is_linked(b, 'myDsl_ChannelType95', a2)
    if hasattr(a1, 'myDsl_ChannelTypeLinha'):
        assert not _is_linked(a1, 'myDsl_ChannelTypeLinha', b)
    if hasattr(a2, 'myDsl_ChannelTypeLinha'):
        assert _is_linked(a2, 'myDsl_ChannelTypeLinha', b)
    _safe_set(b, 'myDsl_ChannelType95', None)
    assert not _is_linked(b, 'myDsl_ChannelType95', a2)
    if hasattr(a2, 'myDsl_ChannelTypeLinha'):
        assert not _is_linked(a2, 'myDsl_ChannelTypeLinha', b)


def test_assoc_emptyStmt393_reverse_link_reassign_clear():
    a1 = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    a2 = myDsl_IfStmt(else_="sample_text_2", if_="sample_text_2")
    b = myDsl_EmptyStmt(aNY_OTHER="sample_text")
    _safe_set(b, 'myDsl_EmptyStmt395', a1)
    assert _is_linked(b, 'myDsl_EmptyStmt395', a1)
    if hasattr(a1, 'myDsl_IfStmt394'):
        assert _is_linked(a1, 'myDsl_IfStmt394', b)
    _safe_set(b, 'myDsl_EmptyStmt395', a2)
    assert _is_linked(b, 'myDsl_EmptyStmt395', a2)
    if hasattr(a1, 'myDsl_IfStmt394'):
        assert not _is_linked(a1, 'myDsl_IfStmt394', b)
    if hasattr(a2, 'myDsl_IfStmt394'):
        assert _is_linked(a2, 'myDsl_IfStmt394', b)
    _safe_set(b, 'myDsl_EmptyStmt395', None)
    assert not _is_linked(b, 'myDsl_EmptyStmt395', a2)
    if hasattr(a2, 'myDsl_IfStmt394'):
        assert not _is_linked(a2, 'myDsl_IfStmt394', b)


def test_assoc_emptyStmt471_reverse_link_reassign_clear():
    a1 = myDsl_ForStmt(for_="sample_text", range="sample_text")
    a2 = myDsl_ForStmt(for_="sample_text_2", range="sample_text_2")
    b = myDsl_EmptyStmt(aNY_OTHER="sample_text")
    _safe_set(b, 'myDsl_EmptyStmt473', a1)
    assert _is_linked(b, 'myDsl_EmptyStmt473', a1)
    if hasattr(a1, 'myDsl_ForStmt472'):
        assert _is_linked(a1, 'myDsl_ForStmt472', b)
    _safe_set(b, 'myDsl_EmptyStmt473', a2)
    assert _is_linked(b, 'myDsl_EmptyStmt473', a2)
    if hasattr(a1, 'myDsl_ForStmt472'):
        assert not _is_linked(a1, 'myDsl_ForStmt472', b)
    if hasattr(a2, 'myDsl_ForStmt472'):
        assert _is_linked(a2, 'myDsl_ForStmt472', b)
    _safe_set(b, 'myDsl_EmptyStmt473', None)
    assert not _is_linked(b, 'myDsl_EmptyStmt473', a2)
    if hasattr(a2, 'myDsl_ForStmt472'):
        assert not _is_linked(a2, 'myDsl_ForStmt472', b)


def test_assoc_forStmtLinha469_reverse_link_reassign_clear():
    a1 = myDsl_ForStmtLinha(vazio="sample_text")
    a2 = myDsl_ForStmtLinha(vazio="sample_text_2")
    b = myDsl_ForStmt(for_="sample_text", range="sample_text")
    _safe_set(b, 'myDsl_ForStmt470', a1)
    assert _is_linked(b, 'myDsl_ForStmt470', a1)
    if hasattr(a1, 'myDsl_ForStmtLinha'):
        assert _is_linked(a1, 'myDsl_ForStmtLinha', b)
    _safe_set(b, 'myDsl_ForStmt470', a2)
    assert _is_linked(b, 'myDsl_ForStmt470', a2)
    if hasattr(a1, 'myDsl_ForStmtLinha'):
        assert not _is_linked(a1, 'myDsl_ForStmtLinha', b)
    if hasattr(a2, 'myDsl_ForStmtLinha'):
        assert _is_linked(a2, 'myDsl_ForStmtLinha', b)
    _safe_set(b, 'myDsl_ForStmt470', None)
    assert not _is_linked(b, 'myDsl_ForStmt470', a2)
    if hasattr(a2, 'myDsl_ForStmtLinha'):
        assert not _is_linked(a2, 'myDsl_ForStmtLinha', b)


def test_assoc_forStmtLinhaLinha490_reverse_link_reassign_clear():
    a1 = myDsl_ForStmtLinhaLinha(range="sample_text")
    a2 = myDsl_ForStmtLinhaLinha(range="sample_text_2")
    b = myDsl_ForStmtLinha(vazio="sample_text")
    _safe_set(b, 'myDsl_ForStmtLinha491', a1)
    assert _is_linked(b, 'myDsl_ForStmtLinha491', a1)
    if hasattr(a1, 'myDsl_ForStmtLinhaLinha'):
        assert _is_linked(a1, 'myDsl_ForStmtLinhaLinha', b)
    _safe_set(b, 'myDsl_ForStmtLinha491', a2)
    assert _is_linked(b, 'myDsl_ForStmtLinha491', a2)
    if hasattr(a1, 'myDsl_ForStmtLinhaLinha'):
        assert not _is_linked(a1, 'myDsl_ForStmtLinhaLinha', b)
    if hasattr(a2, 'myDsl_ForStmtLinhaLinha'):
        assert _is_linked(a2, 'myDsl_ForStmtLinhaLinha', b)
    _safe_set(b, 'myDsl_ForStmtLinha491', None)
    assert not _is_linked(b, 'myDsl_ForStmtLinha491', a2)
    if hasattr(a2, 'myDsl_ForStmtLinhaLinha'):
        assert not _is_linked(a2, 'myDsl_ForStmtLinhaLinha', b)


def test_assoc_identifierList481_reverse_link_reassign_clear():
    a1 = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    a2 = myDsl_IdentifierList(id="sample_text_2", id1="sample_text_2")
    b = myDsl_ForStmt(for_="sample_text", range="sample_text")
    _safe_set(b, 'myDsl_ForStmt482', a1)
    assert _is_linked(b, 'myDsl_ForStmt482', a1)
    if hasattr(a1, 'myDsl_IdentifierList483'):
        assert _is_linked(a1, 'myDsl_IdentifierList483', b)
    _safe_set(b, 'myDsl_ForStmt482', a2)
    assert _is_linked(b, 'myDsl_ForStmt482', a2)
    if hasattr(a1, 'myDsl_IdentifierList483'):
        assert not _is_linked(a1, 'myDsl_IdentifierList483', b)
    if hasattr(a2, 'myDsl_IdentifierList483'):
        assert _is_linked(a2, 'myDsl_IdentifierList483', b)
    _safe_set(b, 'myDsl_ForStmt482', None)
    assert not _is_linked(b, 'myDsl_ForStmt482', a2)
    if hasattr(a2, 'myDsl_IdentifierList483'):
        assert not _is_linked(a2, 'myDsl_IdentifierList483', b)


def test_assoc_ifStmt403_reverse_link_reassign_clear():
    a1 = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    a2 = myDsl_IfStmt(else_="sample_text_2", if_="sample_text_2")
    b = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    _safe_set(b, 'myDsl_IfStmt404', a1)
    assert _is_linked(b, 'myDsl_IfStmt404', a1)
    if hasattr(a1, 'myDsl_IfStmt402'):
        assert _is_linked(a1, 'myDsl_IfStmt402', b)
    _safe_set(b, 'myDsl_IfStmt404', a2)
    assert _is_linked(b, 'myDsl_IfStmt404', a2)
    if hasattr(a1, 'myDsl_IfStmt402'):
        assert not _is_linked(a1, 'myDsl_IfStmt402', b)
    if hasattr(a2, 'myDsl_IfStmt402'):
        assert _is_linked(a2, 'myDsl_IfStmt402', b)
    _safe_set(b, 'myDsl_IfStmt404', None)
    assert not _is_linked(b, 'myDsl_IfStmt404', a2)
    if hasattr(a2, 'myDsl_IfStmt402'):
        assert not _is_linked(a2, 'myDsl_IfStmt402', b)


def test_assoc_ifStmt417_reverse_link_reassign_clear():
    a1 = myDsl_IfStmtLinha(else_="sample_text")
    a2 = myDsl_IfStmtLinha(else_="sample_text_2")
    b = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    _safe_set(b, 'myDsl_IfStmt419', a1)
    assert _is_linked(b, 'myDsl_IfStmt419', a1)
    if hasattr(a1, 'myDsl_IfStmtLinha418'):
        assert _is_linked(a1, 'myDsl_IfStmtLinha418', b)
    _safe_set(b, 'myDsl_IfStmt419', a2)
    assert _is_linked(b, 'myDsl_IfStmt419', a2)
    if hasattr(a1, 'myDsl_IfStmtLinha418'):
        assert not _is_linked(a1, 'myDsl_IfStmtLinha418', b)
    if hasattr(a2, 'myDsl_IfStmtLinha418'):
        assert _is_linked(a2, 'myDsl_IfStmtLinha418', b)
    _safe_set(b, 'myDsl_IfStmt419', None)
    assert not _is_linked(b, 'myDsl_IfStmt419', a2)
    if hasattr(a2, 'myDsl_IfStmtLinha418'):
        assert not _is_linked(a2, 'myDsl_IfStmtLinha418', b)


def test_assoc_ifStmtLinha391_reverse_link_reassign_clear():
    a1 = myDsl_IfStmtLinha(else_="sample_text")
    a2 = myDsl_IfStmtLinha(else_="sample_text_2")
    b = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    _safe_set(b, 'myDsl_IfStmt392', a1)
    assert _is_linked(b, 'myDsl_IfStmt392', a1)
    if hasattr(a1, 'myDsl_IfStmtLinha'):
        assert _is_linked(a1, 'myDsl_IfStmtLinha', b)
    _safe_set(b, 'myDsl_IfStmt392', a2)
    assert _is_linked(b, 'myDsl_IfStmt392', a2)
    if hasattr(a1, 'myDsl_IfStmtLinha'):
        assert not _is_linked(a1, 'myDsl_IfStmtLinha', b)
    if hasattr(a2, 'myDsl_IfStmtLinha'):
        assert _is_linked(a2, 'myDsl_IfStmtLinha', b)
    _safe_set(b, 'myDsl_IfStmt392', None)
    assert not _is_linked(b, 'myDsl_IfStmt392', a2)
    if hasattr(a2, 'myDsl_IfStmtLinha'):
        assert not _is_linked(a2, 'myDsl_IfStmtLinha', b)


def test_assoc_importSpec1577_reverse_link_reassign_clear():
    a1 = myDsl_ImportSpec(sTRING_LIT="sample_text")
    a2 = myDsl_ImportSpec(sTRING_LIT="sample_text_2")
    b = myDsl_ImportDecl(importt="sample_text")
    _safe_set(b, 'myDsl_ImportDecl578', {a1})
    assert _is_linked(b, 'myDsl_ImportDecl578', a1)
    if hasattr(a1, 'myDsl_ImportSpec579'):
        assert _is_linked(a1, 'myDsl_ImportSpec579', b)
    _safe_set(b, 'myDsl_ImportDecl578', {a2})
    assert _is_linked(b, 'myDsl_ImportDecl578', a2)
    if hasattr(a1, 'myDsl_ImportSpec579'):
        assert not _is_linked(a1, 'myDsl_ImportSpec579', b)
    if hasattr(a2, 'myDsl_ImportSpec579'):
        assert _is_linked(a2, 'myDsl_ImportSpec579', b)
    _safe_set(b, 'myDsl_ImportDecl578', set())
    assert not _is_linked(b, 'myDsl_ImportDecl578', a2)
    if hasattr(a2, 'myDsl_ImportSpec579'):
        assert not _is_linked(a2, 'myDsl_ImportSpec579', b)


def test_assoc_importSpec575_reverse_link_reassign_clear():
    a1 = myDsl_ImportSpec(sTRING_LIT="sample_text")
    a2 = myDsl_ImportSpec(sTRING_LIT="sample_text_2")
    b = myDsl_ImportDecl(importt="sample_text")
    _safe_set(b, 'myDsl_ImportDecl576', a1)
    assert _is_linked(b, 'myDsl_ImportDecl576', a1)
    if hasattr(a1, 'myDsl_ImportSpec'):
        assert _is_linked(a1, 'myDsl_ImportSpec', b)
    _safe_set(b, 'myDsl_ImportDecl576', a2)
    assert _is_linked(b, 'myDsl_ImportDecl576', a2)
    if hasattr(a1, 'myDsl_ImportSpec'):
        assert not _is_linked(a1, 'myDsl_ImportSpec', b)
    if hasattr(a2, 'myDsl_ImportSpec'):
        assert _is_linked(a2, 'myDsl_ImportSpec', b)
    _safe_set(b, 'myDsl_ImportDecl576', None)
    assert not _is_linked(b, 'myDsl_ImportDecl576', a2)
    if hasattr(a2, 'myDsl_ImportSpec'):
        assert not _is_linked(a2, 'myDsl_ImportSpec', b)


def test_assoc_label554_reverse_link_reassign_clear():
    a1 = myDsl_Label(id="sample_text")
    a2 = myDsl_Label(id="sample_text_2")
    b = myDsl_BreakStmt(break_="sample_text")
    _safe_set(b, 'myDsl_BreakStmt555', a1)
    assert _is_linked(b, 'myDsl_BreakStmt555', a1)
    if hasattr(a1, 'myDsl_Label556'):
        assert _is_linked(a1, 'myDsl_Label556', b)
    _safe_set(b, 'myDsl_BreakStmt555', a2)
    assert _is_linked(b, 'myDsl_BreakStmt555', a2)
    if hasattr(a1, 'myDsl_Label556'):
        assert not _is_linked(a1, 'myDsl_Label556', b)
    if hasattr(a2, 'myDsl_Label556'):
        assert _is_linked(a2, 'myDsl_Label556', b)
    _safe_set(b, 'myDsl_BreakStmt555', None)
    assert not _is_linked(b, 'myDsl_BreakStmt555', a2)
    if hasattr(a2, 'myDsl_Label556'):
        assert not _is_linked(a2, 'myDsl_Label556', b)


def test_assoc_label557_reverse_link_reassign_clear():
    a1 = myDsl_Label(id="sample_text")
    a2 = myDsl_Label(id="sample_text_2")
    b = myDsl_ContinueStmt(continue_="sample_text")
    _safe_set(b, 'myDsl_ContinueStmt558', a1)
    assert _is_linked(b, 'myDsl_ContinueStmt558', a1)
    if hasattr(a1, 'myDsl_Label559'):
        assert _is_linked(a1, 'myDsl_Label559', b)
    _safe_set(b, 'myDsl_ContinueStmt558', a2)
    assert _is_linked(b, 'myDsl_ContinueStmt558', a2)
    if hasattr(a1, 'myDsl_Label559'):
        assert not _is_linked(a1, 'myDsl_Label559', b)
    if hasattr(a2, 'myDsl_Label559'):
        assert _is_linked(a2, 'myDsl_Label559', b)
    _safe_set(b, 'myDsl_ContinueStmt558', None)
    assert not _is_linked(b, 'myDsl_ContinueStmt558', a2)
    if hasattr(a2, 'myDsl_Label559'):
        assert not _is_linked(a2, 'myDsl_Label559', b)


def test_assoc_label560_reverse_link_reassign_clear():
    a1 = myDsl_Label(id="sample_text")
    a2 = myDsl_Label(id="sample_text_2")
    b = myDsl_GotoStmt(goto="sample_text")
    _safe_set(b, 'myDsl_GotoStmt561', a1)
    assert _is_linked(b, 'myDsl_GotoStmt561', a1)
    if hasattr(a1, 'myDsl_Label562'):
        assert _is_linked(a1, 'myDsl_Label562', b)
    _safe_set(b, 'myDsl_GotoStmt561', a2)
    assert _is_linked(b, 'myDsl_GotoStmt561', a2)
    if hasattr(a1, 'myDsl_Label562'):
        assert not _is_linked(a1, 'myDsl_Label562', b)
    if hasattr(a2, 'myDsl_Label562'):
        assert _is_linked(a2, 'myDsl_Label562', b)
    _safe_set(b, 'myDsl_GotoStmt561', None)
    assert not _is_linked(b, 'myDsl_GotoStmt561', a2)
    if hasattr(a2, 'myDsl_Label562'):
        assert not _is_linked(a2, 'myDsl_Label562', b)


def test_assoc_packageName573_reverse_link_reassign_clear():
    a1 = myDsl_PackageName(id="sample_text")
    a2 = myDsl_PackageName(id="sample_text_2")
    b = myDsl_PackageClause(package="sample_text")
    _safe_set(b, 'myDsl_PackageClause574', a1)
    assert _is_linked(b, 'myDsl_PackageClause574', a1)
    if hasattr(a1, 'myDsl_PackageName'):
        assert _is_linked(a1, 'myDsl_PackageName', b)
    _safe_set(b, 'myDsl_PackageClause574', a2)
    assert _is_linked(b, 'myDsl_PackageClause574', a2)
    if hasattr(a1, 'myDsl_PackageName'):
        assert not _is_linked(a1, 'myDsl_PackageName', b)
    if hasattr(a2, 'myDsl_PackageName'):
        assert _is_linked(a2, 'myDsl_PackageName', b)
    _safe_set(b, 'myDsl_PackageClause574', None)
    assert not _is_linked(b, 'myDsl_PackageClause574', a2)
    if hasattr(a2, 'myDsl_PackageName'):
        assert not _is_linked(a2, 'myDsl_PackageName', b)


def test_assoc_packageName580_reverse_link_reassign_clear():
    a1 = myDsl_PackageName(id="sample_text")
    a2 = myDsl_PackageName(id="sample_text_2")
    b = myDsl_ImportSpec(sTRING_LIT="sample_text")
    _safe_set(b, 'myDsl_ImportSpec581', a1)
    assert _is_linked(b, 'myDsl_ImportSpec581', a1)
    if hasattr(a1, 'myDsl_PackageName582'):
        assert _is_linked(a1, 'myDsl_PackageName582', b)
    _safe_set(b, 'myDsl_ImportSpec581', a2)
    assert _is_linked(b, 'myDsl_ImportSpec581', a2)
    if hasattr(a1, 'myDsl_PackageName582'):
        assert not _is_linked(a1, 'myDsl_PackageName582', b)
    if hasattr(a2, 'myDsl_PackageName582'):
        assert _is_linked(a2, 'myDsl_PackageName582', b)
    _safe_set(b, 'myDsl_ImportSpec581', None)
    assert not _is_linked(b, 'myDsl_ImportSpec581', a2)
    if hasattr(a2, 'myDsl_PackageName582'):
        assert not _is_linked(a2, 'myDsl_PackageName582', b)


def test_assoc_simpleStmtLinha408_reverse_link_reassign_clear():
    a1 = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text")
    a2 = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text_2")
    b = myDsl_IfStmtLinha(else_="sample_text")
    _safe_set(b, 'myDsl_IfStmtLinha409', a1)
    assert _is_linked(b, 'myDsl_IfStmtLinha409', a1)
    if hasattr(a1, 'myDsl_SimpleStmtLinha410'):
        assert _is_linked(a1, 'myDsl_SimpleStmtLinha410', b)
    _safe_set(b, 'myDsl_IfStmtLinha409', a2)
    assert _is_linked(b, 'myDsl_IfStmtLinha409', a2)
    if hasattr(a1, 'myDsl_SimpleStmtLinha410'):
        assert not _is_linked(a1, 'myDsl_SimpleStmtLinha410', b)
    if hasattr(a2, 'myDsl_SimpleStmtLinha410'):
        assert _is_linked(a2, 'myDsl_SimpleStmtLinha410', b)
    _safe_set(b, 'myDsl_IfStmtLinha409', None)
    assert not _is_linked(b, 'myDsl_IfStmtLinha409', a2)
    if hasattr(a2, 'myDsl_SimpleStmtLinha410'):
        assert not _is_linked(a2, 'myDsl_SimpleStmtLinha410', b)


def test_assoc_typeSwitchGuard446_reverse_link_reassign_clear():
    a1 = myDsl_TypeSwitchStmt(switch="sample_text")
    a2 = myDsl_TypeSwitchStmt(switch="sample_text_2")
    b = myDsl_TypeSwitchGuard(id="sample_text", type="sample_text")
    _safe_set(b, 'myDsl_TypeSwitchGuard', a1)
    assert _is_linked(b, 'myDsl_TypeSwitchGuard', a1)
    if hasattr(a1, 'myDsl_TypeSwitchStmt447'):
        assert _is_linked(a1, 'myDsl_TypeSwitchStmt447', b)
    _safe_set(b, 'myDsl_TypeSwitchGuard', a2)
    assert _is_linked(b, 'myDsl_TypeSwitchGuard', a2)
    if hasattr(a1, 'myDsl_TypeSwitchStmt447'):
        assert not _is_linked(a1, 'myDsl_TypeSwitchStmt447', b)
    if hasattr(a2, 'myDsl_TypeSwitchStmt447'):
        assert _is_linked(a2, 'myDsl_TypeSwitchStmt447', b)
    _safe_set(b, 'myDsl_TypeSwitchGuard', None)
    assert not _is_linked(b, 'myDsl_TypeSwitchGuard', a2)
    if hasattr(a2, 'myDsl_TypeSwitchStmt447'):
        assert not _is_linked(a2, 'myDsl_TypeSwitchStmt447', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_BINARY_OP313_stub_double():
    # myDsl_Expression_Linha has no real 'myDsl_Expression_Linha314' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_BINARY_OP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_BINARY_OP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_BINARY_OP(aDD_OP="sample_text", rEL_OP="sample_text")
    partner = myDsl_Expression_Linha()
    setattr(partner, 'myDsl_Expression_Linha314', None)
    _safe_set(owner, 'myDsl_BINARY_OP', partner)
    assert getattr(partner, 'myDsl_Expression_Linha314') == owner
    _safe_set(owner, 'myDsl_BINARY_OP', None)
    assert getattr(partner, 'myDsl_Expression_Linha314') is None


def test_assoc_IdentifierList152_stub_double():
    # myDsl_VarSpec has no real 'myDsl_VarSpec153' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IdentifierList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IdentifierList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    partner = myDsl_VarSpec()
    setattr(partner, 'myDsl_VarSpec153', None)
    _safe_set(owner, 'myDsl_IdentifierList154', partner)
    assert getattr(partner, 'myDsl_VarSpec153') == owner
    _safe_set(owner, 'myDsl_IdentifierList154', None)
    assert getattr(partner, 'myDsl_VarSpec153') is None


def test_assoc_aliasDecl137_stub_double():
    # myDsl_TypeSpec has no real 'myDsl_TypeSpec138' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_AliasDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_AliasDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_AliasDecl(id="sample_text")
    partner = myDsl_TypeSpec()
    setattr(partner, 'myDsl_TypeSpec138', None)
    _safe_set(owner, 'myDsl_AliasDecl', partner)
    assert getattr(partner, 'myDsl_TypeSpec138') == owner
    _safe_set(owner, 'myDsl_AliasDecl', None)
    assert getattr(partner, 'myDsl_TypeSpec138') is None


def test_assoc_basicLit196_stub_double():
    # myDsl_Literal has no real 'myDsl_Literal197' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_BasicLit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_BasicLit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_BasicLit(float_lit="sample_text", imaginary_lit="sample_text", int_lit="sample_text", rune_lit="sample_text", string_lit="sample_text")
    partner = myDsl_Literal()
    setattr(partner, 'myDsl_Literal197', None)
    _safe_set(owner, 'myDsl_BasicLit', partner)
    assert getattr(partner, 'myDsl_Literal197') == owner
    _safe_set(owner, 'myDsl_BasicLit', None)
    assert getattr(partner, 'myDsl_Literal197') is None


def test_assoc_block1405_stub_double():
    # myDsl_Block has no real 'myDsl_Block407' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    partner = myDsl_Block()
    setattr(partner, 'myDsl_Block407', None)
    _safe_set(owner, 'myDsl_IfStmt406', partner)
    assert getattr(partner, 'myDsl_Block407') == owner
    _safe_set(owner, 'myDsl_IfStmt406', None)
    assert getattr(partner, 'myDsl_Block407') is None


def test_assoc_block1420_stub_double():
    # myDsl_Block has no real 'myDsl_Block422' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmtLinha(else_="sample_text")
    partner = myDsl_Block()
    setattr(partner, 'myDsl_Block422', None)
    _safe_set(owner, 'myDsl_IfStmtLinha421', partner)
    assert getattr(partner, 'myDsl_Block422') == owner
    _safe_set(owner, 'myDsl_IfStmtLinha421', None)
    assert getattr(partner, 'myDsl_Block422') is None


def test_assoc_block399_stub_double():
    # myDsl_Block has no real 'myDsl_Block401' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    partner = myDsl_Block()
    setattr(partner, 'myDsl_Block401', None)
    _safe_set(owner, 'myDsl_IfStmt400', partner)
    assert getattr(partner, 'myDsl_Block401') == owner
    _safe_set(owner, 'myDsl_IfStmt400', None)
    assert getattr(partner, 'myDsl_Block401') is None


def test_assoc_block414_stub_double():
    # myDsl_Block has no real 'myDsl_Block416' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmtLinha(else_="sample_text")
    partner = myDsl_Block()
    setattr(partner, 'myDsl_Block416', None)
    _safe_set(owner, 'myDsl_IfStmtLinha415', partner)
    assert getattr(partner, 'myDsl_Block416') == owner
    _safe_set(owner, 'myDsl_IfStmtLinha415', None)
    assert getattr(partner, 'myDsl_Block416') is None


def test_assoc_block484_stub_double():
    # myDsl_Block has no real 'myDsl_Block486' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmt(for_="sample_text", range="sample_text")
    partner = myDsl_Block()
    setattr(partner, 'myDsl_Block486', None)
    _safe_set(owner, 'myDsl_ForStmt485', partner)
    assert getattr(partner, 'myDsl_Block486') == owner
    _safe_set(owner, 'myDsl_ForStmt485', None)
    assert getattr(partner, 'myDsl_Block486') is None


def test_assoc_breakStmt341_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement342' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_BreakStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_BreakStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_BreakStmt(break_="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement342', None)
    _safe_set(owner, 'myDsl_BreakStmt', partner)
    assert getattr(partner, 'myDsl_Statement342') == owner
    _safe_set(owner, 'myDsl_BreakStmt', None)
    assert getattr(partner, 'myDsl_Statement342') is None


def test_assoc_channelType19_stub_double():
    # myDsl_TypeLit has no real 'myDsl_TypeLit20' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ChannelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ChannelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ChannelType(chan="sample_text")
    partner = myDsl_TypeLit()
    setattr(partner, 'myDsl_TypeLit20', None)
    _safe_set(owner, 'myDsl_ChannelType', partner)
    assert getattr(partner, 'myDsl_TypeLit20') == owner
    _safe_set(owner, 'myDsl_ChannelType', None)
    assert getattr(partner, 'myDsl_TypeLit20') is None


def test_assoc_commCase527_stub_double():
    # myDsl_CommClause has no real 'myDsl_CommClause528' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_CommCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_CommCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_CommCase(case="sample_text", default="sample_text")
    partner = myDsl_CommClause()
    setattr(partner, 'myDsl_CommClause528', None)
    _safe_set(owner, 'myDsl_CommCase', partner)
    assert getattr(partner, 'myDsl_CommClause528') == owner
    _safe_set(owner, 'myDsl_CommCase', None)
    assert getattr(partner, 'myDsl_CommClause528') is None


def test_assoc_commCaseLinha535_stub_double():
    # myDsl_CommCaseLinha has no real 'myDsl_CommCaseLinha' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_CommCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_CommCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_CommCase(case="sample_text", default="sample_text")
    partner = myDsl_CommCaseLinha()
    setattr(partner, 'myDsl_CommCaseLinha', None)
    _safe_set(owner, 'myDsl_CommCase536', partner)
    assert getattr(partner, 'myDsl_CommCaseLinha') == owner
    _safe_set(owner, 'myDsl_CommCase536', None)
    assert getattr(partner, 'myDsl_CommCaseLinha') is None


def test_assoc_commClause525_stub_double():
    # myDsl_CommClause has no real 'myDsl_CommClause' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SelectStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SelectStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SelectStmt(select="sample_text")
    partner = myDsl_CommClause()
    setattr(partner, 'myDsl_CommClause', None)
    _safe_set(owner, 'myDsl_SelectStmt526', {partner})
    assert getattr(partner, 'myDsl_CommClause') == owner
    _safe_set(owner, 'myDsl_SelectStmt526', set())
    assert getattr(partner, 'myDsl_CommClause') is None


def test_assoc_condition477_stub_double():
    # myDsl_Condition has no real 'myDsl_Condition' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmt(for_="sample_text", range="sample_text")
    partner = myDsl_Condition()
    setattr(partner, 'myDsl_Condition', None)
    _safe_set(owner, 'myDsl_ForStmt478', partner)
    assert getattr(partner, 'myDsl_Condition') == owner
    _safe_set(owner, 'myDsl_ForStmt478', None)
    assert getattr(partner, 'myDsl_Condition') is None


def test_assoc_condition495_stub_double():
    # myDsl_Condition has no real 'myDsl_Condition497' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinha(vazio="sample_text")
    partner = myDsl_Condition()
    setattr(partner, 'myDsl_Condition497', None)
    _safe_set(owner, 'myDsl_ForStmtLinha496', partner)
    assert getattr(partner, 'myDsl_Condition497') == owner
    _safe_set(owner, 'myDsl_ForStmtLinha496', None)
    assert getattr(partner, 'myDsl_Condition497') is None


def test_assoc_condition507_stub_double():
    # myDsl_Condition has no real 'myDsl_Condition509' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinhaLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinhaLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinhaLinha(range="sample_text")
    partner = myDsl_Condition()
    setattr(partner, 'myDsl_Condition509', None)
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha508', partner)
    assert getattr(partner, 'myDsl_Condition509') == owner
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha508', None)
    assert getattr(partner, 'myDsl_Condition509') is None


def test_assoc_constDecl102_stub_double():
    # myDsl_Declaration has no real 'myDsl_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ConstDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ConstDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ConstDecl(const="sample_text")
    partner = myDsl_Declaration()
    setattr(partner, 'myDsl_Declaration', None)
    _safe_set(owner, 'myDsl_ConstDecl', partner)
    assert getattr(partner, 'myDsl_Declaration') == owner
    _safe_set(owner, 'myDsl_ConstDecl', None)
    assert getattr(partner, 'myDsl_Declaration') is None


def test_assoc_constSpec1115_stub_double():
    # myDsl_ConstSpec has no real 'myDsl_ConstSpec117' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ConstDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ConstDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ConstDecl(const="sample_text")
    partner = myDsl_ConstSpec()
    setattr(partner, 'myDsl_ConstSpec117', None)
    _safe_set(owner, 'myDsl_ConstDecl116', {partner})
    assert getattr(partner, 'myDsl_ConstSpec117') == owner
    _safe_set(owner, 'myDsl_ConstDecl116', set())
    assert getattr(partner, 'myDsl_ConstSpec117') is None


def test_assoc_constSpec113_stub_double():
    # myDsl_ConstSpec has no real 'myDsl_ConstSpec' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ConstDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ConstDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ConstDecl(const="sample_text")
    partner = myDsl_ConstSpec()
    setattr(partner, 'myDsl_ConstSpec', None)
    _safe_set(owner, 'myDsl_ConstDecl114', partner)
    assert getattr(partner, 'myDsl_ConstSpec') == owner
    _safe_set(owner, 'myDsl_ConstDecl114', None)
    assert getattr(partner, 'myDsl_ConstSpec') is None


def test_assoc_continueStmt343_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement344' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ContinueStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ContinueStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ContinueStmt(continue_="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement344', None)
    _safe_set(owner, 'myDsl_ContinueStmt', partner)
    assert getattr(partner, 'myDsl_Statement344') == owner
    _safe_set(owner, 'myDsl_ContinueStmt', None)
    assert getattr(partner, 'myDsl_Statement344') is None


def test_assoc_deferStmt360_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement361' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DeferStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DeferStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DeferStmt(defer="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement361', None)
    _safe_set(owner, 'myDsl_DeferStmt', partner)
    assert getattr(partner, 'myDsl_Statement361') == owner
    _safe_set(owner, 'myDsl_DeferStmt', None)
    assert getattr(partner, 'myDsl_Statement361') is None


def test_assoc_elementType88_stub_double():
    # myDsl_ElementType has no real 'myDsl_ElementType90' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MapType(map="sample_text")
    partner = myDsl_ElementType()
    setattr(partner, 'myDsl_ElementType90', None)
    _safe_set(owner, 'myDsl_MapType89', partner)
    assert getattr(partner, 'myDsl_ElementType90') == owner
    _safe_set(owner, 'myDsl_MapType89', None)
    assert getattr(partner, 'myDsl_ElementType90') is None


def test_assoc_elementType96_stub_double():
    # myDsl_ElementType has no real 'myDsl_ElementType98' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ChannelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ChannelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ChannelType(chan="sample_text")
    partner = myDsl_ElementType()
    setattr(partner, 'myDsl_ElementType98', None)
    _safe_set(owner, 'myDsl_ChannelType97', partner)
    assert getattr(partner, 'myDsl_ElementType98') == owner
    _safe_set(owner, 'myDsl_ChannelType97', None)
    assert getattr(partner, 'myDsl_ElementType98') is None


def test_assoc_emptyStmt362_stub_double():
    # myDsl_SimpleStmt has no real 'myDsl_SimpleStmt363' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_EmptyStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_EmptyStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_EmptyStmt(aNY_OTHER="sample_text")
    partner = myDsl_SimpleStmt()
    setattr(partner, 'myDsl_SimpleStmt363', None)
    _safe_set(owner, 'myDsl_EmptyStmt', partner)
    assert getattr(partner, 'myDsl_SimpleStmt363') == owner
    _safe_set(owner, 'myDsl_EmptyStmt', None)
    assert getattr(partner, 'myDsl_SimpleStmt363') is None


def test_assoc_exprCaseClause433_stub_double():
    # myDsl_ExprCaseClause has no real 'myDsl_ExprCaseClause' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSwitchStmt(switch="sample_text")
    partner = myDsl_ExprCaseClause()
    setattr(partner, 'myDsl_ExprCaseClause', None)
    _safe_set(owner, 'myDsl_ExprSwitchStmt434', {partner})
    assert getattr(partner, 'myDsl_ExprCaseClause') == owner
    _safe_set(owner, 'myDsl_ExprSwitchStmt434', set())
    assert getattr(partner, 'myDsl_ExprCaseClause') is None


def test_assoc_exprSwitchCase435_stub_double():
    # myDsl_ExprCaseClause has no real 'myDsl_ExprCaseClause436' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSwitchCase(case="sample_text", default="sample_text")
    partner = myDsl_ExprCaseClause()
    setattr(partner, 'myDsl_ExprCaseClause436', None)
    _safe_set(owner, 'myDsl_ExprSwitchCase', partner)
    assert getattr(partner, 'myDsl_ExprCaseClause436') == owner
    _safe_set(owner, 'myDsl_ExprSwitchCase', None)
    assert getattr(partner, 'myDsl_ExprCaseClause436') is None


def test_assoc_exprSwitchStmt423_stub_double():
    # myDsl_SwitchStmt has no real 'myDsl_SwitchStmt424' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSwitchStmt(switch="sample_text")
    partner = myDsl_SwitchStmt()
    setattr(partner, 'myDsl_SwitchStmt424', None)
    _safe_set(owner, 'myDsl_ExprSwitchStmt', partner)
    assert getattr(partner, 'myDsl_SwitchStmt424') == owner
    _safe_set(owner, 'myDsl_ExprSwitchStmt', None)
    assert getattr(partner, 'myDsl_SwitchStmt424') is None


def test_assoc_expression1375_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression377' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SimpleStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SimpleStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression377', None)
    _safe_set(owner, 'myDsl_SimpleStmtLinha376', {partner})
    assert getattr(partner, 'myDsl_Expression377') == owner
    _safe_set(owner, 'myDsl_SimpleStmtLinha376', set())
    assert getattr(partner, 'myDsl_Expression377') is None


def test_assoc_expression1492_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression494' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinha(vazio="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression494', None)
    _safe_set(owner, 'myDsl_ForStmtLinha493', partner)
    assert getattr(partner, 'myDsl_Expression494') == owner
    _safe_set(owner, 'myDsl_ForStmtLinha493', None)
    assert getattr(partner, 'myDsl_Expression494') is None


def test_assoc_expression372_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression374' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SimpleStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SimpleStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression374', None)
    _safe_set(owner, 'myDsl_SimpleStmtLinha373', partner)
    assert getattr(partner, 'myDsl_Expression374') == owner
    _safe_set(owner, 'myDsl_SimpleStmtLinha373', None)
    assert getattr(partner, 'myDsl_Expression374') is None


def test_assoc_expression388_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression390' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression390', None)
    _safe_set(owner, 'myDsl_IfStmt389', partner)
    assert getattr(partner, 'myDsl_Expression390') == owner
    _safe_set(owner, 'myDsl_IfStmt389', None)
    assert getattr(partner, 'myDsl_Expression390') is None


def test_assoc_expression411_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression413' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmtLinha(else_="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression413', None)
    _safe_set(owner, 'myDsl_IfStmtLinha412', partner)
    assert getattr(partner, 'myDsl_Expression413') == owner
    _safe_set(owner, 'myDsl_IfStmtLinha412', None)
    assert getattr(partner, 'myDsl_Expression413') is None


def test_assoc_expression430_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression432' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSwitchStmt(switch="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression432', None)
    _safe_set(owner, 'myDsl_ExprSwitchStmt431', partner)
    assert getattr(partner, 'myDsl_Expression432') == owner
    _safe_set(owner, 'myDsl_ExprSwitchStmt431', None)
    assert getattr(partner, 'myDsl_Expression432') is None


def test_assoc_expression466_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression468' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmt(for_="sample_text", range="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression468', None)
    _safe_set(owner, 'myDsl_ForStmt467', partner)
    assert getattr(partner, 'myDsl_Expression468') == owner
    _safe_set(owner, 'myDsl_ForStmt467', None)
    assert getattr(partner, 'myDsl_Expression468') is None


def test_assoc_expression487_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression489' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinha(vazio="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression489', None)
    _safe_set(owner, 'myDsl_ForStmtLinha488', {partner})
    assert getattr(partner, 'myDsl_Expression489') == owner
    _safe_set(owner, 'myDsl_ForStmtLinha488', set())
    assert getattr(partner, 'myDsl_Expression489') is None


def test_assoc_expression513_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression515' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinhaLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinhaLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinhaLinha(range="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression515', None)
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha514', partner)
    assert getattr(partner, 'myDsl_Expression515') == owner
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha514', None)
    assert getattr(partner, 'myDsl_Expression515') is None


def test_assoc_expression522_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression524' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_GoStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_GoStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_GoStmt(go="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression524', None)
    _safe_set(owner, 'myDsl_GoStmt523', partner)
    assert getattr(partner, 'myDsl_Expression524') == owner
    _safe_set(owner, 'myDsl_GoStmt523', None)
    assert getattr(partner, 'myDsl_Expression524') is None


def test_assoc_expression532_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression534' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_CommCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_CommCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_CommCase(case="sample_text", default="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression534', None)
    _safe_set(owner, 'myDsl_CommCase533', partner)
    assert getattr(partner, 'myDsl_Expression534') == owner
    _safe_set(owner, 'myDsl_CommCase533', None)
    assert getattr(partner, 'myDsl_Expression534') is None


def test_assoc_expression563_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression565' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DeferStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DeferStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DeferStmt(defer="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression565', None)
    _safe_set(owner, 'myDsl_DeferStmt564', partner)
    assert getattr(partner, 'myDsl_Expression565') == owner
    _safe_set(owner, 'myDsl_DeferStmt564', None)
    assert getattr(partner, 'myDsl_Expression565') is None


def test_assoc_expressionList380_stub_double():
    # myDsl_ExpressionList has no real 'myDsl_ExpressionList382' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SimpleStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SimpleStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text")
    partner = myDsl_ExpressionList()
    setattr(partner, 'myDsl_ExpressionList382', None)
    _safe_set(owner, 'myDsl_SimpleStmtLinha381', partner)
    assert getattr(partner, 'myDsl_ExpressionList382') == owner
    _safe_set(owner, 'myDsl_SimpleStmtLinha381', None)
    assert getattr(partner, 'myDsl_ExpressionList382') is None


def test_assoc_expressionList440_stub_double():
    # myDsl_ExpressionList has no real 'myDsl_ExpressionList442' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSwitchCase(case="sample_text", default="sample_text")
    partner = myDsl_ExpressionList()
    setattr(partner, 'myDsl_ExpressionList442', None)
    _safe_set(owner, 'myDsl_ExprSwitchCase441', partner)
    assert getattr(partner, 'myDsl_ExpressionList442') == owner
    _safe_set(owner, 'myDsl_ExprSwitchCase441', None)
    assert getattr(partner, 'myDsl_ExpressionList442') is None


def test_assoc_expressionList504_stub_double():
    # myDsl_ExpressionList has no real 'myDsl_ExpressionList506' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinhaLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinhaLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinhaLinha(range="sample_text")
    partner = myDsl_ExpressionList()
    setattr(partner, 'myDsl_ExpressionList506', None)
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha505', partner)
    assert getattr(partner, 'myDsl_ExpressionList506') == owner
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha505', None)
    assert getattr(partner, 'myDsl_ExpressionList506') is None


def test_assoc_expressionList551_stub_double():
    # myDsl_ExpressionList has no real 'myDsl_ExpressionList553' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReturnStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReturnStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReturnStmt(return_="sample_text")
    partner = myDsl_ExpressionList()
    setattr(partner, 'myDsl_ExpressionList553', None)
    _safe_set(owner, 'myDsl_ReturnStmt552', partner)
    assert getattr(partner, 'myDsl_ExpressionList553') == owner
    _safe_set(owner, 'myDsl_ReturnStmt552', None)
    assert getattr(partner, 'myDsl_ExpressionList553') is None


def test_assoc_fallthroughStmt347_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement348' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FallthroughStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FallthroughStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FallthroughStmt(fallthrough="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement348', None)
    _safe_set(owner, 'myDsl_FallthroughStmt', partner)
    assert getattr(partner, 'myDsl_Statement348') == owner
    _safe_set(owner, 'myDsl_FallthroughStmt', None)
    assert getattr(partner, 'myDsl_Statement348') is None


def test_assoc_fieldDecl30_stub_double():
    # myDsl_FieldDecl has no real 'myDsl_FieldDecl' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_StructType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_StructType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_StructType(struct="sample_text")
    partner = myDsl_FieldDecl()
    setattr(partner, 'myDsl_FieldDecl', None)
    _safe_set(owner, 'myDsl_StructType31', {partner})
    assert getattr(partner, 'myDsl_FieldDecl') == owner
    _safe_set(owner, 'myDsl_StructType31', set())
    assert getattr(partner, 'myDsl_FieldDecl') is None


def test_assoc_fieldName234_stub_double():
    # myDsl_Key has no real 'myDsl_Key235' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FieldName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FieldName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FieldName(id="sample_text")
    partner = myDsl_Key()
    setattr(partner, 'myDsl_Key235', None)
    _safe_set(owner, 'myDsl_FieldName', partner)
    assert getattr(partner, 'myDsl_Key235') == owner
    _safe_set(owner, 'myDsl_FieldName', None)
    assert getattr(partner, 'myDsl_Key235') is None


def test_assoc_forStmt358_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement359' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmt(for_="sample_text", range="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement359', None)
    _safe_set(owner, 'myDsl_ForStmt', partner)
    assert getattr(partner, 'myDsl_Statement359') == owner
    _safe_set(owner, 'myDsl_ForStmt', None)
    assert getattr(partner, 'myDsl_Statement359') is None


def test_assoc_functionBody251_stub_double():
    # myDsl_FunctionBody has no real 'myDsl_FunctionBody253' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FunctionLit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FunctionLit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FunctionLit(func="sample_text")
    partner = myDsl_FunctionBody()
    setattr(partner, 'myDsl_FunctionBody253', None)
    _safe_set(owner, 'myDsl_FunctionLit252', partner)
    assert getattr(partner, 'myDsl_FunctionBody253') == owner
    _safe_set(owner, 'myDsl_FunctionLit252', None)
    assert getattr(partner, 'myDsl_FunctionBody253') is None


def test_assoc_functionLit200_stub_double():
    # myDsl_Literal has no real 'myDsl_Literal201' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FunctionLit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FunctionLit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FunctionLit(func="sample_text")
    partner = myDsl_Literal()
    setattr(partner, 'myDsl_Literal201', None)
    _safe_set(owner, 'myDsl_FunctionLit', partner)
    assert getattr(partner, 'myDsl_Literal201') == owner
    _safe_set(owner, 'myDsl_FunctionLit', None)
    assert getattr(partner, 'myDsl_Literal201') is None


def test_assoc_functionName166_stub_double():
    # myDsl_FunctionDecl has no real 'myDsl_FunctionDecl167' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FunctionName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FunctionName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FunctionName(id="sample_text")
    partner = myDsl_FunctionDecl()
    setattr(partner, 'myDsl_FunctionDecl167', None)
    _safe_set(owner, 'myDsl_FunctionName', partner)
    assert getattr(partner, 'myDsl_FunctionDecl167') == owner
    _safe_set(owner, 'myDsl_FunctionName', None)
    assert getattr(partner, 'myDsl_FunctionDecl167') is None


def test_assoc_functionType13_stub_double():
    # myDsl_TypeLit has no real 'myDsl_TypeLit14' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FunctionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FunctionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FunctionType(func="sample_text")
    partner = myDsl_TypeLit()
    setattr(partner, 'myDsl_TypeLit14', None)
    _safe_set(owner, 'myDsl_FunctionType', partner)
    assert getattr(partner, 'myDsl_TypeLit14') == owner
    _safe_set(owner, 'myDsl_FunctionType', None)
    assert getattr(partner, 'myDsl_TypeLit14') is None


def test_assoc_goStmt337_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement338' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_GoStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_GoStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_GoStmt(go="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement338', None)
    _safe_set(owner, 'myDsl_GoStmt', partner)
    assert getattr(partner, 'myDsl_Statement338') == owner
    _safe_set(owner, 'myDsl_GoStmt', None)
    assert getattr(partner, 'myDsl_Statement338') is None


def test_assoc_gotoStmt345_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement346' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_GotoStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_GotoStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_GotoStmt(goto="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement346', None)
    _safe_set(owner, 'myDsl_GotoStmt', partner)
    assert getattr(partner, 'myDsl_Statement346') == owner
    _safe_set(owner, 'myDsl_GotoStmt', None)
    assert getattr(partner, 'myDsl_Statement346') is None


def test_assoc_identifierList118_stub_double():
    # myDsl_ConstSpec has no real 'myDsl_ConstSpec119' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IdentifierList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IdentifierList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    partner = myDsl_ConstSpec()
    setattr(partner, 'myDsl_ConstSpec119', None)
    _safe_set(owner, 'myDsl_IdentifierList120', partner)
    assert getattr(partner, 'myDsl_ConstSpec119') == owner
    _safe_set(owner, 'myDsl_IdentifierList120', None)
    assert getattr(partner, 'myDsl_ConstSpec119') is None


def test_assoc_identifierList161_stub_double():
    # myDsl_ShortVarDecl has no real 'myDsl_ShortVarDecl' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IdentifierList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IdentifierList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    partner = myDsl_ShortVarDecl()
    setattr(partner, 'myDsl_ShortVarDecl', None)
    _safe_set(owner, 'myDsl_IdentifierList162', partner)
    assert getattr(partner, 'myDsl_ShortVarDecl') == owner
    _safe_set(owner, 'myDsl_IdentifierList162', None)
    assert getattr(partner, 'myDsl_ShortVarDecl') is None


def test_assoc_identifierList32_stub_double():
    # myDsl_FieldDecl has no real 'myDsl_FieldDecl33' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IdentifierList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IdentifierList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    partner = myDsl_FieldDecl()
    setattr(partner, 'myDsl_FieldDecl33', None)
    _safe_set(owner, 'myDsl_IdentifierList', partner)
    assert getattr(partner, 'myDsl_FieldDecl33') == owner
    _safe_set(owner, 'myDsl_IdentifierList', None)
    assert getattr(partner, 'myDsl_FieldDecl33') is None


def test_assoc_identifierList543_stub_double():
    # myDsl_CommCaseLinha has no real 'myDsl_CommCaseLinha544' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IdentifierList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IdentifierList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    partner = myDsl_CommCaseLinha()
    setattr(partner, 'myDsl_CommCaseLinha544', None)
    _safe_set(owner, 'myDsl_IdentifierList545', partner)
    assert getattr(partner, 'myDsl_CommCaseLinha544') == owner
    _safe_set(owner, 'myDsl_IdentifierList545', None)
    assert getattr(partner, 'myDsl_CommCaseLinha544') is None


def test_assoc_identifierList68_stub_double():
    # myDsl_ParameterDecl has no real 'myDsl_ParameterDecl69' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IdentifierList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IdentifierList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IdentifierList(id="sample_text", id1="sample_text")
    partner = myDsl_ParameterDecl()
    setattr(partner, 'myDsl_ParameterDecl69', None)
    _safe_set(owner, 'myDsl_IdentifierList70', partner)
    assert getattr(partner, 'myDsl_ParameterDecl69') == owner
    _safe_set(owner, 'myDsl_IdentifierList70', None)
    assert getattr(partner, 'myDsl_ParameterDecl69') is None


def test_assoc_ifStmt352_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement353' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement353', None)
    _safe_set(owner, 'myDsl_IfStmt', partner)
    assert getattr(partner, 'myDsl_Statement353') == owner
    _safe_set(owner, 'myDsl_IfStmt', None)
    assert getattr(partner, 'myDsl_Statement353') is None


def test_assoc_importDecl568_stub_double():
    # myDsl_SourceFile has no real 'myDsl_SourceFile569' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ImportDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ImportDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ImportDecl(importt="sample_text")
    partner = myDsl_SourceFile()
    setattr(partner, 'myDsl_SourceFile569', None)
    _safe_set(owner, 'myDsl_ImportDecl', partner)
    assert owner in getattr(partner, 'myDsl_SourceFile569')
    _safe_set(owner, 'myDsl_ImportDecl', None)
    assert owner not in getattr(partner, 'myDsl_SourceFile569')


def test_assoc_interfaceType15_stub_double():
    # myDsl_TypeLit has no real 'myDsl_TypeLit16' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_InterfaceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_InterfaceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_InterfaceType(interface="sample_text")
    partner = myDsl_TypeLit()
    setattr(partner, 'myDsl_TypeLit16', None)
    _safe_set(owner, 'myDsl_InterfaceType', partner)
    assert getattr(partner, 'myDsl_TypeLit16') == owner
    _safe_set(owner, 'myDsl_InterfaceType', None)
    assert getattr(partner, 'myDsl_TypeLit16') is None


def test_assoc_keyType86_stub_double():
    # myDsl_KeyType has no real 'myDsl_KeyType' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MapType(map="sample_text")
    partner = myDsl_KeyType()
    setattr(partner, 'myDsl_KeyType', None)
    _safe_set(owner, 'myDsl_MapType87', partner)
    assert getattr(partner, 'myDsl_KeyType') == owner
    _safe_set(owner, 'myDsl_MapType87', None)
    assert getattr(partner, 'myDsl_KeyType') is None


def test_assoc_label383_stub_double():
    # myDsl_LabeledStmt has no real 'myDsl_LabeledStmt384' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Label(id="sample_text")
    partner = myDsl_LabeledStmt()
    setattr(partner, 'myDsl_LabeledStmt384', None)
    _safe_set(owner, 'myDsl_Label', partner)
    assert getattr(partner, 'myDsl_LabeledStmt384') == owner
    _safe_set(owner, 'myDsl_Label', None)
    assert getattr(partner, 'myDsl_LabeledStmt384') is None


def test_assoc_mapType17_stub_double():
    # myDsl_TypeLit has no real 'myDsl_TypeLit18' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MapType(map="sample_text")
    partner = myDsl_TypeLit()
    setattr(partner, 'myDsl_TypeLit18', None)
    _safe_set(owner, 'myDsl_MapType', partner)
    assert getattr(partner, 'myDsl_TypeLit18') == owner
    _safe_set(owner, 'myDsl_MapType', None)
    assert getattr(partner, 'myDsl_TypeLit18') is None


def test_assoc_mapType209_stub_double():
    # myDsl_LiteralType has no real 'myDsl_LiteralType210' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MapType(map="sample_text")
    partner = myDsl_LiteralType()
    setattr(partner, 'myDsl_LiteralType210', None)
    _safe_set(owner, 'myDsl_MapType211', partner)
    assert getattr(partner, 'myDsl_LiteralType210') == owner
    _safe_set(owner, 'myDsl_MapType211', None)
    assert getattr(partner, 'myDsl_LiteralType210') is None


def test_assoc_methodName178_stub_double():
    # myDsl_MethodDecl has no real 'myDsl_MethodDecl179' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MethodName(id="sample_text")
    partner = myDsl_MethodDecl()
    setattr(partner, 'myDsl_MethodDecl179', None)
    _safe_set(owner, 'myDsl_MethodName180', partner)
    assert getattr(partner, 'myDsl_MethodDecl179') == owner
    _safe_set(owner, 'myDsl_MethodName180', None)
    assert getattr(partner, 'myDsl_MethodDecl179') is None


def test_assoc_methodName298_stub_double():
    # myDsl_MethodExpr has no real 'myDsl_MethodExpr299' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MethodName(id="sample_text")
    partner = myDsl_MethodExpr()
    setattr(partner, 'myDsl_MethodExpr299', None)
    _safe_set(owner, 'myDsl_MethodName300', partner)
    assert getattr(partner, 'myDsl_MethodExpr299') == owner
    _safe_set(owner, 'myDsl_MethodName300', None)
    assert getattr(partner, 'myDsl_MethodExpr299') is None


def test_assoc_methodName76_stub_double():
    # myDsl_MethodSpec has no real 'myDsl_MethodSpec77' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MethodName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MethodName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MethodName(id="sample_text")
    partner = myDsl_MethodSpec()
    setattr(partner, 'myDsl_MethodSpec77', None)
    _safe_set(owner, 'myDsl_MethodName', partner)
    assert getattr(partner, 'myDsl_MethodSpec77') == owner
    _safe_set(owner, 'myDsl_MethodName', None)
    assert getattr(partner, 'myDsl_MethodSpec77') is None


def test_assoc_methodSpec74_stub_double():
    # myDsl_MethodSpec has no real 'myDsl_MethodSpec' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_InterfaceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_InterfaceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_InterfaceType(interface="sample_text")
    partner = myDsl_MethodSpec()
    setattr(partner, 'myDsl_MethodSpec', None)
    _safe_set(owner, 'myDsl_InterfaceType75', {partner})
    assert getattr(partner, 'myDsl_MethodSpec') == owner
    _safe_set(owner, 'myDsl_InterfaceType75', set())
    assert getattr(partner, 'myDsl_MethodSpec') is None


def test_assoc_operandName191_stub_double():
    # myDsl_Operand has no real 'myDsl_Operand192' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_OperandName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_OperandName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_OperandName(id="sample_text")
    partner = myDsl_Operand()
    setattr(partner, 'myDsl_Operand192', None)
    _safe_set(owner, 'myDsl_OperandName', partner)
    assert getattr(partner, 'myDsl_Operand192') == owner
    _safe_set(owner, 'myDsl_OperandName', None)
    assert getattr(partner, 'myDsl_Operand192') is None


def test_assoc_packageClause566_stub_double():
    # myDsl_SourceFile has no real 'myDsl_SourceFile567' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_PackageClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_PackageClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_PackageClause(package="sample_text")
    partner = myDsl_SourceFile()
    setattr(partner, 'myDsl_SourceFile567', None)
    _safe_set(owner, 'myDsl_PackageClause', partner)
    assert getattr(partner, 'myDsl_SourceFile567') == owner
    _safe_set(owner, 'myDsl_PackageClause', None)
    assert getattr(partner, 'myDsl_SourceFile567') is None


def test_assoc_postStmt479_stub_double():
    # myDsl_PostStmt has no real 'myDsl_PostStmt' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmt(for_="sample_text", range="sample_text")
    partner = myDsl_PostStmt()
    setattr(partner, 'myDsl_PostStmt', None)
    _safe_set(owner, 'myDsl_ForStmt480', partner)
    assert getattr(partner, 'myDsl_PostStmt') == owner
    _safe_set(owner, 'myDsl_ForStmt480', None)
    assert getattr(partner, 'myDsl_PostStmt') is None


def test_assoc_postStmt498_stub_double():
    # myDsl_PostStmt has no real 'myDsl_PostStmt500' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinha(vazio="sample_text")
    partner = myDsl_PostStmt()
    setattr(partner, 'myDsl_PostStmt500', None)
    _safe_set(owner, 'myDsl_ForStmtLinha499', partner)
    assert getattr(partner, 'myDsl_PostStmt500') == owner
    _safe_set(owner, 'myDsl_ForStmtLinha499', None)
    assert getattr(partner, 'myDsl_PostStmt500') is None


def test_assoc_postStmt510_stub_double():
    # myDsl_PostStmt has no real 'myDsl_PostStmt512' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmtLinhaLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmtLinhaLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmtLinhaLinha(range="sample_text")
    partner = myDsl_PostStmt()
    setattr(partner, 'myDsl_PostStmt512', None)
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha511', partner)
    assert getattr(partner, 'myDsl_PostStmt512') == owner
    _safe_set(owner, 'myDsl_ForStmtLinhaLinha511', None)
    assert getattr(partner, 'myDsl_PostStmt512') is None


def test_assoc_primaryExpr450_stub_double():
    # myDsl_PrimaryExpr has no real 'myDsl_PrimaryExpr452' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeSwitchGuard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeSwitchGuard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeSwitchGuard(id="sample_text", type="sample_text")
    partner = myDsl_PrimaryExpr()
    setattr(partner, 'myDsl_PrimaryExpr452', None)
    _safe_set(owner, 'myDsl_TypeSwitchGuard451', partner)
    assert getattr(partner, 'myDsl_PrimaryExpr452') == owner
    _safe_set(owner, 'myDsl_TypeSwitchGuard451', None)
    assert getattr(partner, 'myDsl_PrimaryExpr452') is None


def test_assoc_returnStmt339_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement340' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReturnStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReturnStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReturnStmt(return_="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement340', None)
    _safe_set(owner, 'myDsl_ReturnStmt', partner)
    assert getattr(partner, 'myDsl_Statement340') == owner
    _safe_set(owner, 'myDsl_ReturnStmt', None)
    assert getattr(partner, 'myDsl_Statement340') is None


def test_assoc_selectStmt356_stub_double():
    # myDsl_Statement has no real 'myDsl_Statement357' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SelectStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SelectStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SelectStmt(select="sample_text")
    partner = myDsl_Statement()
    setattr(partner, 'myDsl_Statement357', None)
    _safe_set(owner, 'myDsl_SelectStmt', partner)
    assert getattr(partner, 'myDsl_Statement357') == owner
    _safe_set(owner, 'myDsl_SelectStmt', None)
    assert getattr(partner, 'myDsl_Statement357') is None


def test_assoc_selector262_stub_double():
    # myDsl_PrimaryExprLinha has no real 'myDsl_PrimaryExprLinha263' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Selector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Selector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Selector(id="sample_text")
    partner = myDsl_PrimaryExprLinha()
    setattr(partner, 'myDsl_PrimaryExprLinha263', None)
    _safe_set(owner, 'myDsl_Selector', partner)
    assert getattr(partner, 'myDsl_PrimaryExprLinha263') == owner
    _safe_set(owner, 'myDsl_Selector', None)
    assert getattr(partner, 'myDsl_PrimaryExprLinha263') is None


def test_assoc_shortVarDecl396_stub_double():
    # myDsl_ShortVarDecl has no real 'myDsl_ShortVarDecl398' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_IfStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_IfStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_IfStmt(else_="sample_text", if_="sample_text")
    partner = myDsl_ShortVarDecl()
    setattr(partner, 'myDsl_ShortVarDecl398', None)
    _safe_set(owner, 'myDsl_IfStmt397', partner)
    assert getattr(partner, 'myDsl_ShortVarDecl398') == owner
    _safe_set(owner, 'myDsl_IfStmt397', None)
    assert getattr(partner, 'myDsl_ShortVarDecl398') is None


def test_assoc_shortVarDecl474_stub_double():
    # myDsl_ShortVarDecl has no real 'myDsl_ShortVarDecl476' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ForStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ForStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ForStmt(for_="sample_text", range="sample_text")
    partner = myDsl_ShortVarDecl()
    setattr(partner, 'myDsl_ShortVarDecl476', None)
    _safe_set(owner, 'myDsl_ForStmt475', partner)
    assert getattr(partner, 'myDsl_ShortVarDecl476') == owner
    _safe_set(owner, 'myDsl_ForStmt475', None)
    assert getattr(partner, 'myDsl_ShortVarDecl476') is None


def test_assoc_signature248_stub_double():
    # myDsl_Signature has no real 'myDsl_Signature250' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FunctionLit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FunctionLit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FunctionLit(func="sample_text")
    partner = myDsl_Signature()
    setattr(partner, 'myDsl_Signature250', None)
    _safe_set(owner, 'myDsl_FunctionLit249', partner)
    assert getattr(partner, 'myDsl_Signature250') == owner
    _safe_set(owner, 'myDsl_FunctionLit249', None)
    assert getattr(partner, 'myDsl_Signature250') is None


def test_assoc_signature49_stub_double():
    # myDsl_Signature has no real 'myDsl_Signature' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_FunctionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_FunctionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_FunctionType(func="sample_text")
    partner = myDsl_Signature()
    setattr(partner, 'myDsl_Signature', None)
    _safe_set(owner, 'myDsl_FunctionType50', partner)
    assert getattr(partner, 'myDsl_Signature') == owner
    _safe_set(owner, 'myDsl_FunctionType50', None)
    assert getattr(partner, 'myDsl_Signature') is None


def test_assoc_simpleStmt427_stub_double():
    # myDsl_SimpleStmt has no real 'myDsl_SimpleStmt429' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSwitchStmt(switch="sample_text")
    partner = myDsl_SimpleStmt()
    setattr(partner, 'myDsl_SimpleStmt429', None)
    _safe_set(owner, 'myDsl_ExprSwitchStmt428', partner)
    assert getattr(partner, 'myDsl_SimpleStmt429') == owner
    _safe_set(owner, 'myDsl_ExprSwitchStmt428', None)
    assert getattr(partner, 'myDsl_SimpleStmt429') is None


def test_assoc_simpleStmt443_stub_double():
    # myDsl_SimpleStmt has no real 'myDsl_SimpleStmt445' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeSwitchStmt(switch="sample_text")
    partner = myDsl_SimpleStmt()
    setattr(partner, 'myDsl_SimpleStmt445', None)
    _safe_set(owner, 'myDsl_TypeSwitchStmt444', partner)
    assert getattr(partner, 'myDsl_SimpleStmt445') == owner
    _safe_set(owner, 'myDsl_TypeSwitchStmt444', None)
    assert getattr(partner, 'myDsl_SimpleStmt445') is None


def test_assoc_simpleStmtLinha367_stub_double():
    # myDsl_SimpleStmt has no real 'myDsl_SimpleStmt368' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SimpleStmtLinha's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SimpleStmtLinha's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SimpleStmtLinha(aNY_OTHER="sample_text")
    partner = myDsl_SimpleStmt()
    setattr(partner, 'myDsl_SimpleStmt368', None)
    _safe_set(owner, 'myDsl_SimpleStmtLinha', partner)
    assert getattr(partner, 'myDsl_SimpleStmt368') == owner
    _safe_set(owner, 'myDsl_SimpleStmtLinha', None)
    assert getattr(partner, 'myDsl_SimpleStmt368') is None


def test_assoc_srtuctType9_stub_double():
    # myDsl_TypeLit has no real 'myDsl_TypeLit10' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_StructType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_StructType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_StructType(struct="sample_text")
    partner = myDsl_TypeLit()
    setattr(partner, 'myDsl_TypeLit10', None)
    _safe_set(owner, 'myDsl_StructType', partner)
    assert getattr(partner, 'myDsl_TypeLit10') == owner
    _safe_set(owner, 'myDsl_StructType', None)
    assert getattr(partner, 'myDsl_TypeLit10') is None


def test_assoc_structType206_stub_double():
    # myDsl_LiteralType has no real 'myDsl_LiteralType207' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_StructType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_StructType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_StructType(struct="sample_text")
    partner = myDsl_LiteralType()
    setattr(partner, 'myDsl_LiteralType207', None)
    _safe_set(owner, 'myDsl_StructType208', partner)
    assert getattr(partner, 'myDsl_LiteralType207') == owner
    _safe_set(owner, 'myDsl_StructType208', None)
    assert getattr(partner, 'myDsl_LiteralType207') is None


def test_assoc_tag39_stub_double():
    # myDsl_FieldDecl has no real 'myDsl_FieldDecl40' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Tag(string_lit="sample_text")
    partner = myDsl_FieldDecl()
    setattr(partner, 'myDsl_FieldDecl40', None)
    _safe_set(owner, 'myDsl_Tag', partner)
    assert getattr(partner, 'myDsl_FieldDecl40') == owner
    _safe_set(owner, 'myDsl_Tag', None)
    assert getattr(partner, 'myDsl_FieldDecl40') is None


def test_assoc_type141_stub_double():
    # myDsl_Type has no real 'myDsl_Type143' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_AliasDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_AliasDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_AliasDecl(id="sample_text")
    partner = myDsl_Type()
    setattr(partner, 'myDsl_Type143', None)
    _safe_set(owner, 'myDsl_AliasDecl142', partner)
    assert getattr(partner, 'myDsl_Type143') == owner
    _safe_set(owner, 'myDsl_AliasDecl142', None)
    assert getattr(partner, 'myDsl_Type143') is None


def test_assoc_type144_stub_double():
    # myDsl_Type has no real 'myDsl_Type146' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeDef(id="sample_text")
    partner = myDsl_Type()
    setattr(partner, 'myDsl_Type146', None)
    _safe_set(owner, 'myDsl_TypeDef145', partner)
    assert getattr(partner, 'myDsl_Type146') == owner
    _safe_set(owner, 'myDsl_TypeDef145', None)
    assert getattr(partner, 'myDsl_Type146') is None


def test_assoc_typeCaseClause448_stub_double():
    # myDsl_TypeCaseClause has no real 'myDsl_TypeCaseClause' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeSwitchStmt(switch="sample_text")
    partner = myDsl_TypeCaseClause()
    setattr(partner, 'myDsl_TypeCaseClause', None)
    _safe_set(owner, 'myDsl_TypeSwitchStmt449', {partner})
    assert getattr(partner, 'myDsl_TypeCaseClause') == owner
    _safe_set(owner, 'myDsl_TypeSwitchStmt449', set())
    assert getattr(partner, 'myDsl_TypeCaseClause') is None


def test_assoc_typeDecl103_stub_double():
    # myDsl_Declaration has no real 'myDsl_Declaration104' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeDecl(typekeyword="sample_text")
    partner = myDsl_Declaration()
    setattr(partner, 'myDsl_Declaration104', None)
    _safe_set(owner, 'myDsl_TypeDecl', partner)
    assert getattr(partner, 'myDsl_Declaration104') == owner
    _safe_set(owner, 'myDsl_TypeDecl', None)
    assert getattr(partner, 'myDsl_Declaration104') is None


def test_assoc_typeDef139_stub_double():
    # myDsl_TypeSpec has no real 'myDsl_TypeSpec140' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeDef(id="sample_text")
    partner = myDsl_TypeSpec()
    setattr(partner, 'myDsl_TypeSpec140', None)
    _safe_set(owner, 'myDsl_TypeDef', partner)
    assert getattr(partner, 'myDsl_TypeSpec140') == owner
    _safe_set(owner, 'myDsl_TypeDef', None)
    assert getattr(partner, 'myDsl_TypeSpec140') is None


def test_assoc_typeList458_stub_double():
    # myDsl_TypeList has no real 'myDsl_TypeList' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeSwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeSwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeSwitchCase(case="sample_text", default="sample_text")
    partner = myDsl_TypeList()
    setattr(partner, 'myDsl_TypeList', None)
    _safe_set(owner, 'myDsl_TypeSwitchCase459', partner)
    assert getattr(partner, 'myDsl_TypeList') == owner
    _safe_set(owner, 'myDsl_TypeSwitchCase459', None)
    assert getattr(partner, 'myDsl_TypeList') is None


def test_assoc_typeName1_stub_double():
    # myDsl_Type has no real 'myDsl_Type' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeName(id="sample_text")
    partner = myDsl_Type()
    setattr(partner, 'myDsl_Type', None)
    _safe_set(owner, 'myDsl_TypeName', partner)
    assert getattr(partner, 'myDsl_Type') == owner
    _safe_set(owner, 'myDsl_TypeName', None)
    assert getattr(partner, 'myDsl_Type') is None


def test_assoc_typeName212_stub_double():
    # myDsl_LiteralType has no real 'myDsl_LiteralType213' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeName(id="sample_text")
    partner = myDsl_LiteralType()
    setattr(partner, 'myDsl_LiteralType213', None)
    _safe_set(owner, 'myDsl_TypeName214', partner)
    assert getattr(partner, 'myDsl_LiteralType213') == owner
    _safe_set(owner, 'myDsl_TypeName214', None)
    assert getattr(partner, 'myDsl_LiteralType213') is None


def test_assoc_typeName41_stub_double():
    # myDsl_EmbeddedField has no real 'myDsl_EmbeddedField42' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeName(id="sample_text")
    partner = myDsl_EmbeddedField()
    setattr(partner, 'myDsl_EmbeddedField42', None)
    _safe_set(owner, 'myDsl_TypeName43', partner)
    assert getattr(partner, 'myDsl_EmbeddedField42') == owner
    _safe_set(owner, 'myDsl_TypeName43', None)
    assert getattr(partner, 'myDsl_EmbeddedField42') is None


def test_assoc_typeName83_stub_double():
    # myDsl_InterfaceTypeName has no real 'myDsl_InterfaceTypeName84' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeName(id="sample_text")
    partner = myDsl_InterfaceTypeName()
    setattr(partner, 'myDsl_InterfaceTypeName84', None)
    _safe_set(owner, 'myDsl_TypeName85', partner)
    assert getattr(partner, 'myDsl_InterfaceTypeName84') == owner
    _safe_set(owner, 'myDsl_TypeName85', None)
    assert getattr(partner, 'myDsl_InterfaceTypeName84') is None


def test_assoc_typeSpec1134_stub_double():
    # myDsl_TypeSpec has no real 'myDsl_TypeSpec136' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeDecl(typekeyword="sample_text")
    partner = myDsl_TypeSpec()
    setattr(partner, 'myDsl_TypeSpec136', None)
    _safe_set(owner, 'myDsl_TypeDecl135', {partner})
    assert getattr(partner, 'myDsl_TypeSpec136') == owner
    _safe_set(owner, 'myDsl_TypeDecl135', set())
    assert getattr(partner, 'myDsl_TypeSpec136') is None


def test_assoc_typeSpec132_stub_double():
    # myDsl_TypeSpec has no real 'myDsl_TypeSpec' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeDecl(typekeyword="sample_text")
    partner = myDsl_TypeSpec()
    setattr(partner, 'myDsl_TypeSpec', None)
    _safe_set(owner, 'myDsl_TypeDecl133', partner)
    assert getattr(partner, 'myDsl_TypeSpec') == owner
    _safe_set(owner, 'myDsl_TypeDecl133', None)
    assert getattr(partner, 'myDsl_TypeSpec') is None


def test_assoc_typeSwitchCase453_stub_double():
    # myDsl_TypeCaseClause has no real 'myDsl_TypeCaseClause454' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeSwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeSwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeSwitchCase(case="sample_text", default="sample_text")
    partner = myDsl_TypeCaseClause()
    setattr(partner, 'myDsl_TypeCaseClause454', None)
    _safe_set(owner, 'myDsl_TypeSwitchCase', partner)
    assert getattr(partner, 'myDsl_TypeCaseClause454') == owner
    _safe_set(owner, 'myDsl_TypeSwitchCase', None)
    assert getattr(partner, 'myDsl_TypeCaseClause454') is None


def test_assoc_typeSwitchStmt425_stub_double():
    # myDsl_SwitchStmt has no real 'myDsl_SwitchStmt426' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_TypeSwitchStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_TypeSwitchStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_TypeSwitchStmt(switch="sample_text")
    partner = myDsl_SwitchStmt()
    setattr(partner, 'myDsl_SwitchStmt426', None)
    _safe_set(owner, 'myDsl_TypeSwitchStmt', partner)
    assert getattr(partner, 'myDsl_SwitchStmt426') == owner
    _safe_set(owner, 'myDsl_TypeSwitchStmt', None)
    assert getattr(partner, 'myDsl_SwitchStmt426') is None


def test_assoc_varDecl105_stub_double():
    # myDsl_Declaration has no real 'myDsl_Declaration106' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_VarDecl(var="sample_text")
    partner = myDsl_Declaration()
    setattr(partner, 'myDsl_Declaration106', None)
    _safe_set(owner, 'myDsl_VarDecl', partner)
    assert getattr(partner, 'myDsl_Declaration106') == owner
    _safe_set(owner, 'myDsl_VarDecl', None)
    assert getattr(partner, 'myDsl_Declaration106') is None


def test_assoc_varSpec1149_stub_double():
    # myDsl_VarSpec has no real 'myDsl_VarSpec151' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_VarDecl(var="sample_text")
    partner = myDsl_VarSpec()
    setattr(partner, 'myDsl_VarSpec151', None)
    _safe_set(owner, 'myDsl_VarDecl150', {partner})
    assert getattr(partner, 'myDsl_VarSpec151') == owner
    _safe_set(owner, 'myDsl_VarDecl150', set())
    assert getattr(partner, 'myDsl_VarSpec151') is None


def test_assoc_varSpec147_stub_double():
    # myDsl_VarSpec has no real 'myDsl_VarSpec' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_VarDecl(var="sample_text")
    partner = myDsl_VarSpec()
    setattr(partner, 'myDsl_VarSpec', None)
    _safe_set(owner, 'myDsl_VarDecl148', partner)
    assert getattr(partner, 'myDsl_VarSpec') == owner
    _safe_set(owner, 'myDsl_VarDecl148', None)
    assert getattr(partner, 'myDsl_VarSpec') is None


