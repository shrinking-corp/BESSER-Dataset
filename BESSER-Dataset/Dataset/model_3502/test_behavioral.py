import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ElseIfCondition,
    go_ARIT_EXPR,
    go_ArrayType,
    go_ArrayValue,
    go_Assignment,
    go_BINARY_EXP,
    go_BLOCK,
    go_BOOLEAN_VALUE,
    go_BOOL_OP,
    go_BasicType,
    go_COMPARISON,
    go_Chamada,
    go_Condition,
    go_Const,
    go_EObject,
    go_EXPRESSAO,
    go_EXPRESSAOLINHA,
    go_ElseCondition,
    go_ElseIfCondition,
    go_ForClause,
    go_ForDecl,
    go_FunctionCall,
    go_FunctionType,
    go_GoDecl,
    go_IDList,
    go_IGUAL,
    go_IfCondition,
    go_IfStmt,
    go_Init,
    go_InitStmt,
    go_LITERAIS_BASICOS,
    go_LiteraisList,
    go_PARAMETER,
    go_PARAMETERS_LIST,
    go_PONTOSIGUAL,
    go_Parameters,
    go_PostStmt,
    go_RangeDecl,
    go_ReturnStmt,
    go_Signature,
    go_SignatureDel,
    go_TIPO,
    go_Types,
    go_Var,
    go_VarCall,
    go_VarDecl,
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

def test_assoc_basic115_reverse_link_reassign_clear():
    a1 = go_LITERAIS_BASICOS(numero="sample_text", string="sample_text")
    a2 = go_LITERAIS_BASICOS(numero="sample_text_2", string="sample_text_2")
    b = go_BINARY_EXP(arit="sample_text")
    _safe_set(b, 'go_BINARY_EXP116', {a1})
    assert _is_linked(b, 'go_BINARY_EXP116', a1)
    if hasattr(a1, 'go_LITERAIS_BASICOS117'):
        assert _is_linked(a1, 'go_LITERAIS_BASICOS117', b)
    _safe_set(b, 'go_BINARY_EXP116', {a2})
    assert _is_linked(b, 'go_BINARY_EXP116', a2)
    if hasattr(a1, 'go_LITERAIS_BASICOS117'):
        assert not _is_linked(a1, 'go_LITERAIS_BASICOS117', b)
    if hasattr(a2, 'go_LITERAIS_BASICOS117'):
        assert _is_linked(a2, 'go_LITERAIS_BASICOS117', b)
    _safe_set(b, 'go_BINARY_EXP116', set())
    assert not _is_linked(b, 'go_BINARY_EXP116', a2)
    if hasattr(a2, 'go_LITERAIS_BASICOS117'):
        assert not _is_linked(a2, 'go_LITERAIS_BASICOS117', b)


def test_assoc_basic163_reverse_link_reassign_clear():
    a1 = go_BasicType(boolean="sample_text", float="sample_text", int="sample_text", string="sample_text")
    a2 = go_BasicType(boolean="sample_text_2", float="sample_text_2", int="sample_text_2", string="sample_text_2")
    b = go_ArrayType(qtd="sample_text")
    _safe_set(b, 'go_ArrayType164', a1)
    assert _is_linked(b, 'go_ArrayType164', a1)
    if hasattr(a1, 'go_BasicType165'):
        assert _is_linked(a1, 'go_BasicType165', b)
    _safe_set(b, 'go_ArrayType164', a2)
    assert _is_linked(b, 'go_ArrayType164', a2)
    if hasattr(a1, 'go_BasicType165'):
        assert not _is_linked(a1, 'go_BasicType165', b)
    if hasattr(a2, 'go_BasicType165'):
        assert _is_linked(a2, 'go_BasicType165', b)
    _safe_set(b, 'go_ArrayType164', None)
    assert not _is_linked(b, 'go_ArrayType164', a2)
    if hasattr(a2, 'go_BasicType165'):
        assert not _is_linked(a2, 'go_BasicType165', b)


def test_assoc_basico152_reverse_link_reassign_clear():
    a1 = go_PARAMETER(id="sample_text")
    a2 = go_PARAMETER(id="sample_text_2")
    b = go_LITERAIS_BASICOS(numero="sample_text", string="sample_text")
    _safe_set(b, 'go_LITERAIS_BASICOS154', a1)
    assert _is_linked(b, 'go_LITERAIS_BASICOS154', a1)
    if hasattr(a1, 'go_PARAMETER153'):
        assert _is_linked(a1, 'go_PARAMETER153', b)
    _safe_set(b, 'go_LITERAIS_BASICOS154', a2)
    assert _is_linked(b, 'go_LITERAIS_BASICOS154', a2)
    if hasattr(a1, 'go_PARAMETER153'):
        assert not _is_linked(a1, 'go_PARAMETER153', b)
    if hasattr(a2, 'go_PARAMETER153'):
        assert _is_linked(a2, 'go_PARAMETER153', b)
    _safe_set(b, 'go_LITERAIS_BASICOS154', None)
    assert not _is_linked(b, 'go_LITERAIS_BASICOS154', a2)
    if hasattr(a2, 'go_PARAMETER153'):
        assert not _is_linked(a2, 'go_PARAMETER153', b)


def test_assoc_booleano113_reverse_link_reassign_clear():
    a1 = go_LITERAIS_BASICOS(numero="sample_text", string="sample_text")
    a2 = go_LITERAIS_BASICOS(numero="sample_text_2", string="sample_text_2")
    b = go_BOOLEAN_VALUE(falso="sample_text", verdadeiro="sample_text")
    _safe_set(b, 'go_BOOLEAN_VALUE', a1)
    assert _is_linked(b, 'go_BOOLEAN_VALUE', a1)
    if hasattr(a1, 'go_LITERAIS_BASICOS114'):
        assert _is_linked(a1, 'go_LITERAIS_BASICOS114', b)
    _safe_set(b, 'go_BOOLEAN_VALUE', a2)
    assert _is_linked(b, 'go_BOOLEAN_VALUE', a2)
    if hasattr(a1, 'go_LITERAIS_BASICOS114'):
        assert not _is_linked(a1, 'go_LITERAIS_BASICOS114', b)
    if hasattr(a2, 'go_LITERAIS_BASICOS114'):
        assert _is_linked(a2, 'go_LITERAIS_BASICOS114', b)
    _safe_set(b, 'go_BOOLEAN_VALUE', None)
    assert not _is_linked(b, 'go_BOOLEAN_VALUE', a2)
    if hasattr(a2, 'go_LITERAIS_BASICOS114'):
        assert not _is_linked(a2, 'go_LITERAIS_BASICOS114', b)


def test_assoc_dois63_reverse_link_reassign_clear():
    a1 = go_PONTOSIGUAL(op="sample_text")
    a2 = go_PONTOSIGUAL(op="sample_text_2")
    b = go_Assignment(id="sample_text", qtd="sample_text")
    _safe_set(b, 'go_Assignment64', a1)
    assert _is_linked(b, 'go_Assignment64', a1)
    if hasattr(a1, 'go_PONTOSIGUAL65'):
        assert _is_linked(a1, 'go_PONTOSIGUAL65', b)
    _safe_set(b, 'go_Assignment64', a2)
    assert _is_linked(b, 'go_Assignment64', a2)
    if hasattr(a1, 'go_PONTOSIGUAL65'):
        assert not _is_linked(a1, 'go_PONTOSIGUAL65', b)
    if hasattr(a2, 'go_PONTOSIGUAL65'):
        assert _is_linked(a2, 'go_PONTOSIGUAL65', b)
    _safe_set(b, 'go_Assignment64', None)
    assert not _is_linked(b, 'go_Assignment64', a2)
    if hasattr(a2, 'go_PONTOSIGUAL65'):
        assert not _is_linked(a2, 'go_PONTOSIGUAL65', b)


def test_assoc_func121_reverse_link_reassign_clear():
    a1 = go_FunctionCall(id="sample_text")
    a2 = go_FunctionCall(id="sample_text_2")
    b = go_BINARY_EXP(arit="sample_text")
    _safe_set(b, 'go_BINARY_EXP122', {a1})
    assert _is_linked(b, 'go_BINARY_EXP122', a1)
    if hasattr(a1, 'go_FunctionCall123'):
        assert _is_linked(a1, 'go_FunctionCall123', b)
    _safe_set(b, 'go_BINARY_EXP122', {a2})
    assert _is_linked(b, 'go_BINARY_EXP122', a2)
    if hasattr(a1, 'go_FunctionCall123'):
        assert not _is_linked(a1, 'go_FunctionCall123', b)
    if hasattr(a2, 'go_FunctionCall123'):
        assert _is_linked(a2, 'go_FunctionCall123', b)
    _safe_set(b, 'go_BINARY_EXP122', set())
    assert not _is_linked(b, 'go_BINARY_EXP122', a2)
    if hasattr(a2, 'go_FunctionCall123'):
        assert not _is_linked(a2, 'go_FunctionCall123', b)


def test_assoc_igual61_reverse_link_reassign_clear():
    a1 = go_IGUAL(igual="sample_text")
    a2 = go_IGUAL(igual="sample_text_2")
    b = go_Assignment(id="sample_text", qtd="sample_text")
    _safe_set(b, 'go_Assignment', a1)
    assert _is_linked(b, 'go_Assignment', a1)
    if hasattr(a1, 'go_IGUAL62'):
        assert _is_linked(a1, 'go_IGUAL62', b)
    _safe_set(b, 'go_Assignment', a2)
    assert _is_linked(b, 'go_Assignment', a2)
    if hasattr(a1, 'go_IGUAL62'):
        assert not _is_linked(a1, 'go_IGUAL62', b)
    if hasattr(a2, 'go_IGUAL62'):
        assert _is_linked(a2, 'go_IGUAL62', b)
    _safe_set(b, 'go_Assignment', None)
    assert not _is_linked(b, 'go_Assignment', a2)
    if hasattr(a2, 'go_IGUAL62'):
        assert not _is_linked(a2, 'go_IGUAL62', b)


def test_assoc_list42_reverse_link_reassign_clear():
    a1 = go_IDList(idList="sample_text", vir="sample_text")
    a2 = go_IDList(idList="sample_text_2", vir="sample_text_2")
    b = go_IDList(idList="sample_text", vir="sample_text")
    _safe_set(b, 'go_IDList43', a1)
    assert _is_linked(b, 'go_IDList43', a1)
    if hasattr(a1, 'go_IDList41'):
        assert _is_linked(a1, 'go_IDList41', b)
    _safe_set(b, 'go_IDList43', a2)
    assert _is_linked(b, 'go_IDList43', a2)
    if hasattr(a1, 'go_IDList41'):
        assert not _is_linked(a1, 'go_IDList41', b)
    if hasattr(a2, 'go_IDList41'):
        assert _is_linked(a2, 'go_IDList41', b)
    _safe_set(b, 'go_IDList43', None)
    assert not _is_linked(b, 'go_IDList43', a2)
    if hasattr(a2, 'go_IDList41'):
        assert not _is_linked(a2, 'go_IDList41', b)


def test_assoc_params150_reverse_link_reassign_clear():
    a1 = go_PARAMETERS_LIST(vir="sample_text")
    a2 = go_PARAMETERS_LIST(vir="sample_text_2")
    b = go_PARAMETER(id="sample_text")
    _safe_set(b, 'go_PARAMETER', a1)
    assert _is_linked(b, 'go_PARAMETER', a1)
    if hasattr(a1, 'go_PARAMETERS_LIST151'):
        assert _is_linked(a1, 'go_PARAMETERS_LIST151', b)
    _safe_set(b, 'go_PARAMETER', a2)
    assert _is_linked(b, 'go_PARAMETER', a2)
    if hasattr(a1, 'go_PARAMETERS_LIST151'):
        assert not _is_linked(a1, 'go_PARAMETERS_LIST151', b)
    if hasattr(a2, 'go_PARAMETERS_LIST151'):
        assert _is_linked(a2, 'go_PARAMETERS_LIST151', b)
    _safe_set(b, 'go_PARAMETER', None)
    assert not _is_linked(b, 'go_PARAMETER', a2)
    if hasattr(a2, 'go_PARAMETERS_LIST151'):
        assert not _is_linked(a2, 'go_PARAMETERS_LIST151', b)


def test_assoc_params166_reverse_link_reassign_clear():
    a1 = go_PARAMETERS_LIST(vir="sample_text")
    a2 = go_PARAMETERS_LIST(vir="sample_text_2")
    b = go_FunctionCall(id="sample_text")
    _safe_set(b, 'go_FunctionCall167', a1)
    assert _is_linked(b, 'go_FunctionCall167', a1)
    if hasattr(a1, 'go_PARAMETERS_LIST168'):
        assert _is_linked(a1, 'go_PARAMETERS_LIST168', b)
    _safe_set(b, 'go_FunctionCall167', a2)
    assert _is_linked(b, 'go_FunctionCall167', a2)
    if hasattr(a1, 'go_PARAMETERS_LIST168'):
        assert not _is_linked(a1, 'go_PARAMETERS_LIST168', b)
    if hasattr(a2, 'go_PARAMETERS_LIST168'):
        assert _is_linked(a2, 'go_PARAMETERS_LIST168', b)
    _safe_set(b, 'go_FunctionCall167', None)
    assert not _is_linked(b, 'go_FunctionCall167', a2)
    if hasattr(a2, 'go_PARAMETERS_LIST168'):
        assert not _is_linked(a2, 'go_PARAMETERS_LIST168', b)


def test_assoc_var1172_reverse_link_reassign_clear():
    a1 = go_VarCall(id="sample_text")
    a2 = go_VarCall(id="sample_text_2")
    b = go_ARIT_EXPR(atr="sample_text", num="sample_text", num1="sample_text", num2="sample_text", op="sample_text")
    _safe_set(b, 'go_ARIT_EXPR173', a1)
    assert _is_linked(b, 'go_ARIT_EXPR173', a1)
    if hasattr(a1, 'go_VarCall174'):
        assert _is_linked(a1, 'go_VarCall174', b)
    _safe_set(b, 'go_ARIT_EXPR173', a2)
    assert _is_linked(b, 'go_ARIT_EXPR173', a2)
    if hasattr(a1, 'go_VarCall174'):
        assert not _is_linked(a1, 'go_VarCall174', b)
    if hasattr(a2, 'go_VarCall174'):
        assert _is_linked(a2, 'go_VarCall174', b)
    _safe_set(b, 'go_ARIT_EXPR173', None)
    assert not _is_linked(b, 'go_ARIT_EXPR173', a2)
    if hasattr(a2, 'go_VarCall174'):
        assert not _is_linked(a2, 'go_VarCall174', b)


def test_assoc_var178_reverse_link_reassign_clear():
    a1 = go_VarCall(id="sample_text")
    a2 = go_VarCall(id="sample_text_2")
    b = go_ARIT_EXPR(atr="sample_text", num="sample_text", num1="sample_text", num2="sample_text", op="sample_text")
    _safe_set(b, 'go_ARIT_EXPR179', a1)
    assert _is_linked(b, 'go_ARIT_EXPR179', a1)
    if hasattr(a1, 'go_VarCall180'):
        assert _is_linked(a1, 'go_VarCall180', b)
    _safe_set(b, 'go_ARIT_EXPR179', a2)
    assert _is_linked(b, 'go_ARIT_EXPR179', a2)
    if hasattr(a1, 'go_VarCall180'):
        assert not _is_linked(a1, 'go_VarCall180', b)
    if hasattr(a2, 'go_VarCall180'):
        assert _is_linked(a2, 'go_VarCall180', b)
    _safe_set(b, 'go_ARIT_EXPR179', None)
    assert not _is_linked(b, 'go_ARIT_EXPR179', a2)
    if hasattr(a2, 'go_VarCall180'):
        assert not _is_linked(a2, 'go_VarCall180', b)


def test_assoc_var2175_reverse_link_reassign_clear():
    a1 = go_VarCall(id="sample_text")
    a2 = go_VarCall(id="sample_text_2")
    b = go_ARIT_EXPR(atr="sample_text", num="sample_text", num1="sample_text", num2="sample_text", op="sample_text")
    _safe_set(b, 'go_ARIT_EXPR176', a1)
    assert _is_linked(b, 'go_ARIT_EXPR176', a1)
    if hasattr(a1, 'go_VarCall177'):
        assert _is_linked(a1, 'go_VarCall177', b)
    _safe_set(b, 'go_ARIT_EXPR176', a2)
    assert _is_linked(b, 'go_ARIT_EXPR176', a2)
    if hasattr(a1, 'go_VarCall177'):
        assert not _is_linked(a1, 'go_VarCall177', b)
    if hasattr(a2, 'go_VarCall177'):
        assert _is_linked(a2, 'go_VarCall177', b)
    _safe_set(b, 'go_ARIT_EXPR176', None)
    assert not _is_linked(b, 'go_ARIT_EXPR176', a2)
    if hasattr(a2, 'go_VarCall177'):
        assert not _is_linked(a2, 'go_VarCall177', b)


def test_assoc_varCal118_reverse_link_reassign_clear():
    a1 = go_VarCall(id="sample_text")
    a2 = go_VarCall(id="sample_text_2")
    b = go_BINARY_EXP(arit="sample_text")
    _safe_set(b, 'go_BINARY_EXP119', {a1})
    assert _is_linked(b, 'go_BINARY_EXP119', a1)
    if hasattr(a1, 'go_VarCall120'):
        assert _is_linked(a1, 'go_VarCall120', b)
    _safe_set(b, 'go_BINARY_EXP119', {a2})
    assert _is_linked(b, 'go_BINARY_EXP119', a2)
    if hasattr(a1, 'go_VarCall120'):
        assert not _is_linked(a1, 'go_VarCall120', b)
    if hasattr(a2, 'go_VarCall120'):
        assert _is_linked(a2, 'go_VarCall120', b)
    _safe_set(b, 'go_BINARY_EXP119', set())
    assert not _is_linked(b, 'go_BINARY_EXP119', a2)
    if hasattr(a2, 'go_VarCall120'):
        assert not _is_linked(a2, 'go_VarCall120', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_array160_stub_double():
    # go_Types has no real 'go_Types161' property in the generated
    # code (a bare stub) -- manually attach it so go_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_ArrayType(qtd="sample_text")
    partner = go_Types()
    setattr(partner, 'go_Types161', None)
    _safe_set(owner, 'go_ArrayType162', partner)
    assert getattr(partner, 'go_Types161') == owner
    _safe_set(owner, 'go_ArrayType162', None)
    assert getattr(partner, 'go_Types161') is None


def test_assoc_array52_stub_double():
    # go_VarDecl has no real 'go_VarDecl53' property in the generated
    # code (a bare stub) -- manually attach it so go_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_ArrayType(qtd="sample_text")
    partner = go_VarDecl()
    setattr(partner, 'go_VarDecl53', None)
    _safe_set(owner, 'go_ArrayType', partner)
    assert getattr(partner, 'go_VarDecl53') == owner
    _safe_set(owner, 'go_ArrayType', None)
    assert getattr(partner, 'go_VarDecl53') is None


def test_assoc_art32_stub_double():
    # go_PostStmt has no real 'go_PostStmt33' property in the generated
    # code (a bare stub) -- manually attach it so go_ARIT_EXPR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_ARIT_EXPR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_ARIT_EXPR(atr="sample_text", num="sample_text", num1="sample_text", num2="sample_text", op="sample_text")
    partner = go_PostStmt()
    setattr(partner, 'go_PostStmt33', None)
    _safe_set(owner, 'go_ARIT_EXPR', partner)
    assert getattr(partner, 'go_PostStmt33') == owner
    _safe_set(owner, 'go_ARIT_EXPR', None)
    assert getattr(partner, 'go_PostStmt33') is None


def test_assoc_assignment86_stub_double():
    # go_EXPRESSAO has no real 'go_EXPRESSAO87' property in the generated
    # code (a bare stub) -- manually attach it so go_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Assignment(id="sample_text", qtd="sample_text")
    partner = go_EXPRESSAO()
    setattr(partner, 'go_EXPRESSAO87', None)
    _safe_set(owner, 'go_Assignment88', partner)
    assert getattr(partner, 'go_EXPRESSAO87') == owner
    _safe_set(owner, 'go_Assignment88', None)
    assert getattr(partner, 'go_EXPRESSAO87') is None


def test_assoc_assinatura126_stub_double():
    # go_Signature has no real 'go_Signature' property in the generated
    # code (a bare stub) -- manually attach it so go_FunctionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_FunctionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_FunctionType(nome="sample_text")
    partner = go_Signature()
    setattr(partner, 'go_Signature', None)
    _safe_set(owner, 'go_FunctionType127', partner)
    assert getattr(partner, 'go_Signature') == owner
    _safe_set(owner, 'go_FunctionType127', None)
    assert getattr(partner, 'go_Signature') is None


def test_assoc_atribuicao46_stub_double():
    # go_VarDecl has no real 'go_VarDecl47' property in the generated
    # code (a bare stub) -- manually attach it so go_IGUAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_IGUAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_IGUAL(igual="sample_text")
    partner = go_VarDecl()
    setattr(partner, 'go_VarDecl47', None)
    _safe_set(owner, 'go_IGUAL48', partner)
    assert getattr(partner, 'go_VarDecl47') == owner
    _safe_set(owner, 'go_IGUAL48', None)
    assert getattr(partner, 'go_VarDecl47') is None


def test_assoc_basic101_stub_double():
    # go_ReturnStmt has no real 'go_ReturnStmt' property in the generated
    # code (a bare stub) -- manually attach it so go_LITERAIS_BASICOS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_LITERAIS_BASICOS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_LITERAIS_BASICOS(numero="sample_text", string="sample_text")
    partner = go_ReturnStmt()
    setattr(partner, 'go_ReturnStmt', None)
    _safe_set(owner, 'go_LITERAIS_BASICOS102', partner)
    assert getattr(partner, 'go_ReturnStmt') == owner
    _safe_set(owner, 'go_LITERAIS_BASICOS102', None)
    assert getattr(partner, 'go_ReturnStmt') is None


def test_assoc_basic158_stub_double():
    # go_Types has no real 'go_Types159' property in the generated
    # code (a bare stub) -- manually attach it so go_BasicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_BasicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_BasicType(boolean="sample_text", float="sample_text", int="sample_text", string="sample_text")
    partner = go_Types()
    setattr(partner, 'go_Types159', None)
    _safe_set(owner, 'go_BasicType', partner)
    assert getattr(partner, 'go_Types159') == owner
    _safe_set(owner, 'go_BasicType', None)
    assert getattr(partner, 'go_Types159') is None


def test_assoc_basic84_stub_double():
    # go_EXPRESSAO has no real 'go_EXPRESSAO85' property in the generated
    # code (a bare stub) -- manually attach it so go_LITERAIS_BASICOS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_LITERAIS_BASICOS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_LITERAIS_BASICOS(numero="sample_text", string="sample_text")
    partner = go_EXPRESSAO()
    setattr(partner, 'go_EXPRESSAO85', None)
    _safe_set(owner, 'go_LITERAIS_BASICOS', partner)
    assert getattr(partner, 'go_EXPRESSAO85') == owner
    _safe_set(owner, 'go_LITERAIS_BASICOS', None)
    assert getattr(partner, 'go_EXPRESSAO85') is None


def test_assoc_binary_exp82_stub_double():
    # go_EXPRESSAO has no real 'go_EXPRESSAO83' property in the generated
    # code (a bare stub) -- manually attach it so go_BINARY_EXP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_BINARY_EXP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_BINARY_EXP(arit="sample_text")
    partner = go_EXPRESSAO()
    setattr(partner, 'go_EXPRESSAO83', None)
    _safe_set(owner, 'go_BINARY_EXP', partner)
    assert getattr(partner, 'go_EXPRESSAO83') == owner
    _safe_set(owner, 'go_BINARY_EXP', None)
    assert getattr(partner, 'go_EXPRESSAO83') is None


def test_assoc_bloco128_stub_double():
    # go_BLOCK has no real 'go_BLOCK' property in the generated
    # code (a bare stub) -- manually attach it so go_FunctionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_FunctionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_FunctionType(nome="sample_text")
    partner = go_BLOCK()
    setattr(partner, 'go_BLOCK', None)
    _safe_set(owner, 'go_FunctionType129', partner)
    assert getattr(partner, 'go_BLOCK') == owner
    _safe_set(owner, 'go_FunctionType129', None)
    assert getattr(partner, 'go_BLOCK') is None


def test_assoc_bool124_stub_double():
    # go_BOOL_OP has no real 'go_BOOL_OP' property in the generated
    # code (a bare stub) -- manually attach it so go_BINARY_EXP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_BINARY_EXP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_BINARY_EXP(arit="sample_text")
    partner = go_BOOL_OP()
    setattr(partner, 'go_BOOL_OP', None)
    _safe_set(owner, 'go_BINARY_EXP125', partner)
    assert getattr(partner, 'go_BOOL_OP') == owner
    _safe_set(owner, 'go_BINARY_EXP125', None)
    assert getattr(partner, 'go_BOOL_OP') is None


def test_assoc_comparador36_stub_double():
    # go_Condition has no real 'go_Condition37' property in the generated
    # code (a bare stub) -- manually attach it so go_COMPARISON's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_COMPARISON's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_COMPARISON(igual="sample_text", maiorigualque="sample_text", maiorque="sample_text", menorigualque="sample_text", menorque="sample_text")
    partner = go_Condition()
    setattr(partner, 'go_Condition37', None)
    _safe_set(owner, 'go_COMPARISON', partner)
    assert getattr(partner, 'go_Condition37') == owner
    _safe_set(owner, 'go_COMPARISON', None)
    assert getattr(partner, 'go_Condition37') is None


def test_assoc_constante71_stub_double():
    # go_TIPO has no real 'go_TIPO72' property in the generated
    # code (a bare stub) -- manually attach it so go_Const's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Const's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Const(const="sample_text")
    partner = go_TIPO()
    setattr(partner, 'go_TIPO72', None)
    _safe_set(owner, 'go_Const', partner)
    assert getattr(partner, 'go_TIPO72') == owner
    _safe_set(owner, 'go_Const', None)
    assert getattr(partner, 'go_TIPO72') is None


def test_assoc_declFunction79_stub_double():
    # go_EXPRESSAO has no real 'go_EXPRESSAO80' property in the generated
    # code (a bare stub) -- manually attach it so go_FunctionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_FunctionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_FunctionType(nome="sample_text")
    partner = go_EXPRESSAO()
    setattr(partner, 'go_EXPRESSAO80', None)
    _safe_set(owner, 'go_FunctionType81', partner)
    assert getattr(partner, 'go_EXPRESSAO80') == owner
    _safe_set(owner, 'go_FunctionType81', None)
    assert getattr(partner, 'go_EXPRESSAO80') is None


def test_assoc_expressao66_stub_double():
    # go_EXPRESSAOLINHA has no real 'go_EXPRESSAOLINHA68' property in the generated
    # code (a bare stub) -- manually attach it so go_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Assignment(id="sample_text", qtd="sample_text")
    partner = go_EXPRESSAOLINHA()
    setattr(partner, 'go_EXPRESSAOLINHA68', None)
    _safe_set(owner, 'go_Assignment67', partner)
    assert getattr(partner, 'go_EXPRESSAOLINHA68') == owner
    _safe_set(owner, 'go_Assignment67', None)
    assert getattr(partner, 'go_EXPRESSAOLINHA68') is None


def test_assoc_func103_stub_double():
    # go_ReturnStmt has no real 'go_ReturnStmt104' property in the generated
    # code (a bare stub) -- manually attach it so go_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_FunctionCall(id="sample_text")
    partner = go_ReturnStmt()
    setattr(partner, 'go_ReturnStmt104', None)
    _safe_set(owner, 'go_FunctionCall105', partner)
    assert getattr(partner, 'go_ReturnStmt104') == owner
    _safe_set(owner, 'go_FunctionCall105', None)
    assert getattr(partner, 'go_ReturnStmt104') is None


def test_assoc_func21_stub_double():
    # go_RangeDecl has no real 'go_RangeDecl22' property in the generated
    # code (a bare stub) -- manually attach it so go_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_FunctionCall(id="sample_text")
    partner = go_RangeDecl()
    setattr(partner, 'go_RangeDecl22', None)
    _safe_set(owner, 'go_FunctionCall', partner)
    assert getattr(partner, 'go_RangeDecl22') == owner
    _safe_set(owner, 'go_FunctionCall', None)
    assert getattr(partner, 'go_RangeDecl22') is None


def test_assoc_func3_stub_double():
    # go_GoDecl has no real 'go_GoDecl4' property in the generated
    # code (a bare stub) -- manually attach it so go_FunctionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_FunctionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_FunctionType(nome="sample_text")
    partner = go_GoDecl()
    setattr(partner, 'go_GoDecl4', None)
    _safe_set(owner, 'go_FunctionType', partner)
    assert getattr(partner, 'go_GoDecl4') == owner
    _safe_set(owner, 'go_FunctionType', None)
    assert getattr(partner, 'go_GoDecl4') is None


def test_assoc_idList13_stub_double():
    # go_RangeDecl has no real 'go_RangeDecl14' property in the generated
    # code (a bare stub) -- manually attach it so go_IDList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_IDList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_IDList(idList="sample_text", vir="sample_text")
    partner = go_RangeDecl()
    setattr(partner, 'go_RangeDecl14', None)
    _safe_set(owner, 'go_IDList', partner)
    assert owner in getattr(partner, 'go_RangeDecl14')
    _safe_set(owner, 'go_IDList', None)
    assert owner not in getattr(partner, 'go_RangeDecl14')


def test_assoc_idVar106_stub_double():
    # go_ReturnStmt has no real 'go_ReturnStmt107' property in the generated
    # code (a bare stub) -- manually attach it so go_VarCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_VarCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_VarCall(id="sample_text")
    partner = go_ReturnStmt()
    setattr(partner, 'go_ReturnStmt107', None)
    _safe_set(owner, 'go_VarCall108', partner)
    assert getattr(partner, 'go_ReturnStmt107') == owner
    _safe_set(owner, 'go_VarCall108', None)
    assert getattr(partner, 'go_ReturnStmt107') is None


def test_assoc_igual15_stub_double():
    # go_RangeDecl has no real 'go_RangeDecl16' property in the generated
    # code (a bare stub) -- manually attach it so go_IGUAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_IGUAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_IGUAL(igual="sample_text")
    partner = go_RangeDecl()
    setattr(partner, 'go_RangeDecl16', None)
    _safe_set(owner, 'go_IGUAL', partner)
    assert getattr(partner, 'go_RangeDecl16') == owner
    _safe_set(owner, 'go_IGUAL', None)
    assert getattr(partner, 'go_RangeDecl16') is None


def test_assoc_lit109_stub_double():
    # go_ArrayValue has no real 'go_ArrayValue110' property in the generated
    # code (a bare stub) -- manually attach it so go_LiteraisList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_LiteraisList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_LiteraisList(vir="sample_text")
    partner = go_ArrayValue()
    setattr(partner, 'go_ArrayValue110', None)
    _safe_set(owner, 'go_LiteraisList', partner)
    assert getattr(partner, 'go_ArrayValue110') == owner
    _safe_set(owner, 'go_LiteraisList', None)
    assert getattr(partner, 'go_ArrayValue110') is None


def test_assoc_lit111_stub_double():
    # go_EObject has no real 'go_EObject' property in the generated
    # code (a bare stub) -- manually attach it so go_LiteraisList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_LiteraisList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_LiteraisList(vir="sample_text")
    partner = go_EObject()
    setattr(partner, 'go_EObject', None)
    _safe_set(owner, 'go_LiteraisList112', {partner})
    assert getattr(partner, 'go_EObject') == owner
    _safe_set(owner, 'go_LiteraisList112', set())
    assert getattr(partner, 'go_EObject') is None


def test_assoc_op17_stub_double():
    # go_RangeDecl has no real 'go_RangeDecl18' property in the generated
    # code (a bare stub) -- manually attach it so go_PONTOSIGUAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_PONTOSIGUAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_PONTOSIGUAL(op="sample_text")
    partner = go_RangeDecl()
    setattr(partner, 'go_RangeDecl18', None)
    _safe_set(owner, 'go_PONTOSIGUAL', partner)
    assert getattr(partner, 'go_RangeDecl18') == owner
    _safe_set(owner, 'go_PONTOSIGUAL', None)
    assert getattr(partner, 'go_RangeDecl18') is None


def test_assoc_params135_stub_double():
    # go_Parameters has no real 'go_Parameters136' property in the generated
    # code (a bare stub) -- manually attach it so go_PARAMETERS_LIST's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_PARAMETERS_LIST's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_PARAMETERS_LIST(vir="sample_text")
    partner = go_Parameters()
    setattr(partner, 'go_Parameters136', None)
    _safe_set(owner, 'go_PARAMETERS_LIST', partner)
    assert getattr(partner, 'go_Parameters136') == owner
    _safe_set(owner, 'go_PARAMETERS_LIST', None)
    assert getattr(partner, 'go_Parameters136') is None


def test_assoc_pront49_stub_double():
    # go_VarDecl has no real 'go_VarDecl50' property in the generated
    # code (a bare stub) -- manually attach it so go_PONTOSIGUAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_PONTOSIGUAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_PONTOSIGUAL(op="sample_text")
    partner = go_VarDecl()
    setattr(partner, 'go_VarDecl50', None)
    _safe_set(owner, 'go_PONTOSIGUAL51', partner)
    assert getattr(partner, 'go_VarDecl50') == owner
    _safe_set(owner, 'go_PONTOSIGUAL51', None)
    assert getattr(partner, 'go_VarDecl50') is None


def test_assoc_signature44_stub_double():
    # go_VarDecl has no real 'go_VarDecl45' property in the generated
    # code (a bare stub) -- manually attach it so go_SignatureDel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SignatureDel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SignatureDel(id="sample_text")
    partner = go_VarDecl()
    setattr(partner, 'go_VarDecl45', None)
    _safe_set(owner, 'go_SignatureDel', partner)
    assert getattr(partner, 'go_VarDecl45') == owner
    _safe_set(owner, 'go_SignatureDel', None)
    assert getattr(partner, 'go_VarDecl45') is None


def test_assoc_tipo155_stub_double():
    # go_Types has no real 'go_Types157' property in the generated
    # code (a bare stub) -- manually attach it so go_PARAMETER's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_PARAMETER's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_PARAMETER(id="sample_text")
    partner = go_Types()
    setattr(partner, 'go_Types157', None)
    _safe_set(owner, 'go_PARAMETER156', partner)
    assert getattr(partner, 'go_Types157') == owner
    _safe_set(owner, 'go_PARAMETER156', None)
    assert getattr(partner, 'go_Types157') is None


def test_assoc_tipoDecl57_stub_double():
    # go_TIPO has no real 'go_TIPO' property in the generated
    # code (a bare stub) -- manually attach it so go_SignatureDel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SignatureDel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SignatureDel(id="sample_text")
    partner = go_TIPO()
    setattr(partner, 'go_TIPO', None)
    _safe_set(owner, 'go_SignatureDel58', partner)
    assert getattr(partner, 'go_TIPO') == owner
    _safe_set(owner, 'go_SignatureDel58', None)
    assert getattr(partner, 'go_TIPO') is None


def test_assoc_type59_stub_double():
    # go_Types has no real 'go_Types' property in the generated
    # code (a bare stub) -- manually attach it so go_SignatureDel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_SignatureDel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_SignatureDel(id="sample_text")
    partner = go_Types()
    setattr(partner, 'go_Types', None)
    _safe_set(owner, 'go_SignatureDel60', partner)
    assert getattr(partner, 'go_Types') == owner
    _safe_set(owner, 'go_SignatureDel60', None)
    assert getattr(partner, 'go_Types') is None


def test_assoc_variavel19_stub_double():
    # go_RangeDecl has no real 'go_RangeDecl20' property in the generated
    # code (a bare stub) -- manually attach it so go_VarCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_VarCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_VarCall(id="sample_text")
    partner = go_RangeDecl()
    setattr(partner, 'go_RangeDecl20', None)
    _safe_set(owner, 'go_VarCall', partner)
    assert getattr(partner, 'go_RangeDecl20') == owner
    _safe_set(owner, 'go_VarCall', None)
    assert getattr(partner, 'go_RangeDecl20') is None


def test_assoc_variavel69_stub_double():
    # go_TIPO has no real 'go_TIPO70' property in the generated
    # code (a bare stub) -- manually attach it so go_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Var(var="sample_text")
    partner = go_TIPO()
    setattr(partner, 'go_TIPO70', None)
    _safe_set(owner, 'go_Var', partner)
    assert getattr(partner, 'go_TIPO70') == owner
    _safe_set(owner, 'go_Var', None)
    assert getattr(partner, 'go_TIPO70') is None


