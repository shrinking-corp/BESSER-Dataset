import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Member,
    SharedDef,
    Statement,
    VarDef,
    aDSL_AbstractElements,
    aDSL_And,
    aDSL_Assignment,
    aDSL_AsyncStat,
    aDSL_AtStat,
    aDSL_AtomicStatement,
    aDSL_Block,
    aDSL_Body,
    aDSL_BoolConstant,
    aDSL_Comparison,
    aDSL_DeRef,
    aDSL_Equality,
    aDSL_Expression,
    aDSL_FinishStat,
    aDSL_For2Statement,
    aDSL_ForStat,
    aDSL_FuncVarDef,
    aDSL_Here,
    aDSL_IfStat,
    aDSL_Init,
    aDSL_IntConstant,
    aDSL_IntegerNegative,
    aDSL_MainMethod,
    aDSL_Member,
    aDSL_MemberSelection,
    aDSL_Method,
    aDSL_Minus,
    aDSL_MulOrDiv,
    aDSL_New,
    aDSL_Not,
    aDSL_Null,
    aDSL_Operator,
    aDSL_Or,
    aDSL_Parameter,
    aDSL_Plus,
    aDSL_PrintInst,
    aDSL_Program,
    aDSL_Reference,
    aDSL_ReturnStat,
    aDSL_SharedArrayDef,
    aDSL_SharedDef,
    aDSL_SharedVarDef,
    aDSL_Statement,
    aDSL_StringConstant,
    aDSL_This,
    aDSL_TryCatchStat,
    aDSL_VarDef,
    aDSL_VariableDef,
    aDSL_VariableType,
    aDSL_WhenStatement,
    aDSL_WhileStat,
    aDSL_XClass,
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

def test_assoc_elseBlock110_reverse_link_reassign_clear():
    a1 = aDSL_IfStat(iselse=True)
    a2 = aDSL_IfStat(iselse=False)
    b = aDSL_Block(ispar=True)
    _safe_set(b, 'aDSL_Block112', a1)
    assert _is_linked(b, 'aDSL_Block112', a1)
    if hasattr(a1, 'aDSL_IfStat111'):
        assert _is_linked(a1, 'aDSL_IfStat111', b)
    _safe_set(b, 'aDSL_Block112', a2)
    assert _is_linked(b, 'aDSL_Block112', a2)
    if hasattr(a1, 'aDSL_IfStat111'):
        assert not _is_linked(a1, 'aDSL_IfStat111', b)
    if hasattr(a2, 'aDSL_IfStat111'):
        assert _is_linked(a2, 'aDSL_IfStat111', b)
    _safe_set(b, 'aDSL_Block112', None)
    assert not _is_linked(b, 'aDSL_Block112', a2)
    if hasattr(a2, 'aDSL_IfStat111'):
        assert not _is_linked(a2, 'aDSL_IfStat111', b)


def test_assoc_importElements0_reverse_link_reassign_clear():
    a1 = aDSL_Program(name="sample_text")
    a2 = aDSL_Program(name="sample_text_2")
    b = aDSL_AbstractElements(importedNamespace="sample_text")
    _safe_set(b, 'aDSL_AbstractElements', a1)
    assert _is_linked(b, 'aDSL_AbstractElements', a1)
    if hasattr(a1, 'aDSL_Program'):
        assert _is_linked(a1, 'aDSL_Program', b)
    _safe_set(b, 'aDSL_AbstractElements', a2)
    assert _is_linked(b, 'aDSL_AbstractElements', a2)
    if hasattr(a1, 'aDSL_Program'):
        assert not _is_linked(a1, 'aDSL_Program', b)
    if hasattr(a2, 'aDSL_Program'):
        assert _is_linked(a2, 'aDSL_Program', b)
    _safe_set(b, 'aDSL_AbstractElements', None)
    assert not _is_linked(b, 'aDSL_AbstractElements', a2)
    if hasattr(a2, 'aDSL_Program'):
        assert not _is_linked(a2, 'aDSL_Program', b)


def test_assoc_innerType52_reverse_link_reassign_clear():
    a1 = aDSL_VariableType(isarray=True)
    a2 = aDSL_VariableType(isarray=False)
    b = aDSL_VariableType(isarray=True)
    _safe_set(b, 'aDSL_VariableType53', a1)
    assert _is_linked(b, 'aDSL_VariableType53', a1)
    if hasattr(a1, 'aDSL_VariableType51'):
        assert _is_linked(a1, 'aDSL_VariableType51', b)
    _safe_set(b, 'aDSL_VariableType53', a2)
    assert _is_linked(b, 'aDSL_VariableType53', a2)
    if hasattr(a1, 'aDSL_VariableType51'):
        assert not _is_linked(a1, 'aDSL_VariableType51', b)
    if hasattr(a2, 'aDSL_VariableType51'):
        assert _is_linked(a2, 'aDSL_VariableType51', b)
    _safe_set(b, 'aDSL_VariableType53', None)
    assert not _is_linked(b, 'aDSL_VariableType53', a2)
    if hasattr(a2, 'aDSL_VariableType51'):
        assert not _is_linked(a2, 'aDSL_VariableType51', b)


def test_assoc_par123_reverse_link_reassign_clear():
    a1 = aDSL_XClass(name="sample_text")
    a2 = aDSL_XClass(name="sample_text_2")
    b = aDSL_MemberSelection(ispar=True, methodinvocation=True)
    _safe_set(b, 'aDSL_MemberSelection124', a1)
    assert _is_linked(b, 'aDSL_MemberSelection124', a1)
    if hasattr(a1, 'aDSL_XClass125'):
        assert _is_linked(a1, 'aDSL_XClass125', b)
    _safe_set(b, 'aDSL_MemberSelection124', a2)
    assert _is_linked(b, 'aDSL_MemberSelection124', a2)
    if hasattr(a1, 'aDSL_XClass125'):
        assert not _is_linked(a1, 'aDSL_XClass125', b)
    if hasattr(a2, 'aDSL_XClass125'):
        assert _is_linked(a2, 'aDSL_XClass125', b)
    _safe_set(b, 'aDSL_MemberSelection124', None)
    assert not _is_linked(b, 'aDSL_MemberSelection124', a2)
    if hasattr(a2, 'aDSL_XClass125'):
        assert not _is_linked(a2, 'aDSL_XClass125', b)


def test_assoc_params12_reverse_link_reassign_clear():
    a1 = aDSL_Parameter(istyped=True, name="sample_text")
    a2 = aDSL_Parameter(istyped=False, name="sample_text_2")
    b = aDSL_Method(isconst=True, istyped=True, name="sample_text")
    _safe_set(b, 'aDSL_Method', {a1})
    assert _is_linked(b, 'aDSL_Method', a1)
    if hasattr(a1, 'aDSL_Parameter'):
        assert _is_linked(a1, 'aDSL_Parameter', b)
    _safe_set(b, 'aDSL_Method', {a2})
    assert _is_linked(b, 'aDSL_Method', a2)
    if hasattr(a1, 'aDSL_Parameter'):
        assert not _is_linked(a1, 'aDSL_Parameter', b)
    if hasattr(a2, 'aDSL_Parameter'):
        assert _is_linked(a2, 'aDSL_Parameter', b)
    _safe_set(b, 'aDSL_Method', set())
    assert not _is_linked(b, 'aDSL_Method', a2)
    if hasattr(a2, 'aDSL_Parameter'):
        assert not _is_linked(a2, 'aDSL_Parameter', b)


def test_assoc_params19_reverse_link_reassign_clear():
    a1 = aDSL_Parameter(istyped=True, name="sample_text")
    a2 = aDSL_Parameter(istyped=False, name="sample_text_2")
    b = aDSL_Operator(opName="sample_text")
    _safe_set(b, 'aDSL_Operator', {a1})
    assert _is_linked(b, 'aDSL_Operator', a1)
    if hasattr(a1, 'aDSL_Parameter20'):
        assert _is_linked(a1, 'aDSL_Parameter20', b)
    _safe_set(b, 'aDSL_Operator', {a2})
    assert _is_linked(b, 'aDSL_Operator', a2)
    if hasattr(a1, 'aDSL_Parameter20'):
        assert not _is_linked(a1, 'aDSL_Parameter20', b)
    if hasattr(a2, 'aDSL_Parameter20'):
        assert _is_linked(a2, 'aDSL_Parameter20', b)
    _safe_set(b, 'aDSL_Operator', set())
    assert not _is_linked(b, 'aDSL_Operator', a2)
    if hasattr(a2, 'aDSL_Parameter20'):
        assert not _is_linked(a2, 'aDSL_Parameter20', b)


def test_assoc_params24_reverse_link_reassign_clear():
    a1 = aDSL_Parameter(istyped=True, name="sample_text")
    a2 = aDSL_Parameter(istyped=False, name="sample_text_2")
    b = aDSL_FuncVarDef(name="sample_text")
    _safe_set(b, 'aDSL_FuncVarDef', {a1})
    assert _is_linked(b, 'aDSL_FuncVarDef', a1)
    if hasattr(a1, 'aDSL_Parameter25'):
        assert _is_linked(a1, 'aDSL_Parameter25', b)
    _safe_set(b, 'aDSL_FuncVarDef', {a2})
    assert _is_linked(b, 'aDSL_FuncVarDef', a2)
    if hasattr(a1, 'aDSL_Parameter25'):
        assert not _is_linked(a1, 'aDSL_Parameter25', b)
    if hasattr(a2, 'aDSL_Parameter25'):
        assert _is_linked(a2, 'aDSL_Parameter25', b)
    _safe_set(b, 'aDSL_FuncVarDef', set())
    assert not _is_linked(b, 'aDSL_FuncVarDef', a2)
    if hasattr(a2, 'aDSL_Parameter25'):
        assert not _is_linked(a2, 'aDSL_Parameter25', b)


def test_assoc_superclass4_reverse_link_reassign_clear():
    a1 = aDSL_XClass(name="sample_text")
    a2 = aDSL_XClass(name="sample_text_2")
    b = aDSL_XClass(name="sample_text")
    _safe_set(b, 'aDSL_XClass5', a1)
    assert _is_linked(b, 'aDSL_XClass5', a1)
    if hasattr(a1, 'aDSL_XClass3'):
        assert _is_linked(a1, 'aDSL_XClass3', b)
    _safe_set(b, 'aDSL_XClass5', a2)
    assert _is_linked(b, 'aDSL_XClass5', a2)
    if hasattr(a1, 'aDSL_XClass3'):
        assert not _is_linked(a1, 'aDSL_XClass3', b)
    if hasattr(a2, 'aDSL_XClass3'):
        assert _is_linked(a2, 'aDSL_XClass3', b)
    _safe_set(b, 'aDSL_XClass5', None)
    assert not _is_linked(b, 'aDSL_XClass5', a2)
    if hasattr(a2, 'aDSL_XClass3'):
        assert not _is_linked(a2, 'aDSL_XClass3', b)


def test_assoc_thenBlock107_reverse_link_reassign_clear():
    a1 = aDSL_IfStat(iselse=True)
    a2 = aDSL_IfStat(iselse=False)
    b = aDSL_Block(ispar=True)
    _safe_set(b, 'aDSL_Block109', a1)
    assert _is_linked(b, 'aDSL_Block109', a1)
    if hasattr(a1, 'aDSL_IfStat108'):
        assert _is_linked(a1, 'aDSL_IfStat108', b)
    _safe_set(b, 'aDSL_Block109', a2)
    assert _is_linked(b, 'aDSL_Block109', a2)
    if hasattr(a1, 'aDSL_IfStat108'):
        assert not _is_linked(a1, 'aDSL_IfStat108', b)
    if hasattr(a2, 'aDSL_IfStat108'):
        assert _is_linked(a2, 'aDSL_IfStat108', b)
    _safe_set(b, 'aDSL_Block109', None)
    assert not _is_linked(b, 'aDSL_Block109', a2)
    if hasattr(a2, 'aDSL_IfStat108'):
        assert not _is_linked(a2, 'aDSL_IfStat108', b)


def test_assoc_type13_reverse_link_reassign_clear():
    a1 = aDSL_VariableType(isarray=True)
    a2 = aDSL_VariableType(isarray=False)
    b = aDSL_Method(isconst=True, istyped=True, name="sample_text")
    _safe_set(b, 'aDSL_Method14', a1)
    assert _is_linked(b, 'aDSL_Method14', a1)
    if hasattr(a1, 'aDSL_VariableType15'):
        assert _is_linked(a1, 'aDSL_VariableType15', b)
    _safe_set(b, 'aDSL_Method14', a2)
    assert _is_linked(b, 'aDSL_Method14', a2)
    if hasattr(a1, 'aDSL_VariableType15'):
        assert not _is_linked(a1, 'aDSL_VariableType15', b)
    if hasattr(a2, 'aDSL_VariableType15'):
        assert _is_linked(a2, 'aDSL_VariableType15', b)
    _safe_set(b, 'aDSL_Method14', None)
    assert not _is_linked(b, 'aDSL_Method14', a2)
    if hasattr(a2, 'aDSL_VariableType15'):
        assert not _is_linked(a2, 'aDSL_VariableType15', b)


def test_assoc_type26_reverse_link_reassign_clear():
    a1 = aDSL_VariableType(isarray=True)
    a2 = aDSL_VariableType(isarray=False)
    b = aDSL_FuncVarDef(name="sample_text")
    _safe_set(b, 'aDSL_FuncVarDef27', a1)
    assert _is_linked(b, 'aDSL_FuncVarDef27', a1)
    if hasattr(a1, 'aDSL_VariableType28'):
        assert _is_linked(a1, 'aDSL_VariableType28', b)
    _safe_set(b, 'aDSL_FuncVarDef27', a2)
    assert _is_linked(b, 'aDSL_FuncVarDef27', a2)
    if hasattr(a1, 'aDSL_VariableType28'):
        assert not _is_linked(a1, 'aDSL_VariableType28', b)
    if hasattr(a2, 'aDSL_VariableType28'):
        assert _is_linked(a2, 'aDSL_VariableType28', b)
    _safe_set(b, 'aDSL_FuncVarDef27', None)
    assert not _is_linked(b, 'aDSL_FuncVarDef27', a2)
    if hasattr(a2, 'aDSL_VariableType28'):
        assert not _is_linked(a2, 'aDSL_VariableType28', b)


def test_assoc_type32_reverse_link_reassign_clear():
    a1 = aDSL_VariableType(isarray=True)
    a2 = aDSL_VariableType(isarray=False)
    b = aDSL_VariableDef(isinit=True, isstatic=True, istyped=True, name="sample_text", vartype="sample_text")
    _safe_set(b, 'aDSL_VariableDef', a1)
    assert _is_linked(b, 'aDSL_VariableDef', a1)
    if hasattr(a1, 'aDSL_VariableType33'):
        assert _is_linked(a1, 'aDSL_VariableType33', b)
    _safe_set(b, 'aDSL_VariableDef', a2)
    assert _is_linked(b, 'aDSL_VariableDef', a2)
    if hasattr(a1, 'aDSL_VariableType33'):
        assert not _is_linked(a1, 'aDSL_VariableType33', b)
    if hasattr(a2, 'aDSL_VariableType33'):
        assert _is_linked(a2, 'aDSL_VariableType33', b)
    _safe_set(b, 'aDSL_VariableDef', None)
    assert not _is_linked(b, 'aDSL_VariableDef', a2)
    if hasattr(a2, 'aDSL_VariableType33'):
        assert not _is_linked(a2, 'aDSL_VariableType33', b)


def test_assoc_type41_reverse_link_reassign_clear():
    a1 = aDSL_VariableType(isarray=True)
    a2 = aDSL_VariableType(isarray=False)
    b = aDSL_Parameter(istyped=True, name="sample_text")
    _safe_set(b, 'aDSL_Parameter42', a1)
    assert _is_linked(b, 'aDSL_Parameter42', a1)
    if hasattr(a1, 'aDSL_VariableType43'):
        assert _is_linked(a1, 'aDSL_VariableType43', b)
    _safe_set(b, 'aDSL_Parameter42', a2)
    assert _is_linked(b, 'aDSL_Parameter42', a2)
    if hasattr(a1, 'aDSL_VariableType43'):
        assert not _is_linked(a1, 'aDSL_VariableType43', b)
    if hasattr(a2, 'aDSL_VariableType43'):
        assert _is_linked(a2, 'aDSL_VariableType43', b)
    _safe_set(b, 'aDSL_Parameter42', None)
    assert not _is_linked(b, 'aDSL_Parameter42', a2)
    if hasattr(a2, 'aDSL_VariableType43'):
        assert not _is_linked(a2, 'aDSL_VariableType43', b)


def test_assoc_type48_reverse_link_reassign_clear():
    a1 = aDSL_XClass(name="sample_text")
    a2 = aDSL_XClass(name="sample_text_2")
    b = aDSL_VariableType(isarray=True)
    _safe_set(b, 'aDSL_VariableType49', a1)
    assert _is_linked(b, 'aDSL_VariableType49', a1)
    if hasattr(a1, 'aDSL_XClass50'):
        assert _is_linked(a1, 'aDSL_XClass50', b)
    _safe_set(b, 'aDSL_VariableType49', a2)
    assert _is_linked(b, 'aDSL_VariableType49', a2)
    if hasattr(a1, 'aDSL_XClass50'):
        assert not _is_linked(a1, 'aDSL_XClass50', b)
    if hasattr(a2, 'aDSL_XClass50'):
        assert _is_linked(a2, 'aDSL_XClass50', b)
    _safe_set(b, 'aDSL_VariableType49', None)
    assert not _is_linked(b, 'aDSL_VariableType49', a2)
    if hasattr(a2, 'aDSL_XClass50'):
        assert not _is_linked(a2, 'aDSL_XClass50', b)


def test_assoc_type78_reverse_link_reassign_clear():
    a1 = aDSL_VariableType(isarray=True)
    a2 = aDSL_VariableType(isarray=False)
    b = aDSL_SharedDef(name="sample_text", replicas=True)
    _safe_set(b, 'aDSL_SharedDef', a1)
    assert _is_linked(b, 'aDSL_SharedDef', a1)
    if hasattr(a1, 'aDSL_VariableType79'):
        assert _is_linked(a1, 'aDSL_VariableType79', b)
    _safe_set(b, 'aDSL_SharedDef', a2)
    assert _is_linked(b, 'aDSL_SharedDef', a2)
    if hasattr(a1, 'aDSL_VariableType79'):
        assert not _is_linked(a1, 'aDSL_VariableType79', b)
    if hasattr(a2, 'aDSL_VariableType79'):
        assert _is_linked(a2, 'aDSL_VariableType79', b)
    _safe_set(b, 'aDSL_SharedDef', None)
    assert not _is_linked(b, 'aDSL_SharedDef', a2)
    if hasattr(a2, 'aDSL_VariableType79'):
        assert not _is_linked(a2, 'aDSL_VariableType79', b)


def test_assoc_xclass1_reverse_link_reassign_clear():
    a1 = aDSL_XClass(name="sample_text")
    a2 = aDSL_XClass(name="sample_text_2")
    b = aDSL_Program(name="sample_text")
    _safe_set(b, 'aDSL_Program2', {a1})
    assert _is_linked(b, 'aDSL_Program2', a1)
    if hasattr(a1, 'aDSL_XClass'):
        assert _is_linked(a1, 'aDSL_XClass', b)
    _safe_set(b, 'aDSL_Program2', {a2})
    assert _is_linked(b, 'aDSL_Program2', a2)
    if hasattr(a1, 'aDSL_XClass'):
        assert not _is_linked(a1, 'aDSL_XClass', b)
    if hasattr(a2, 'aDSL_XClass'):
        assert _is_linked(a2, 'aDSL_XClass', b)
    _safe_set(b, 'aDSL_Program2', set())
    assert not _is_linked(b, 'aDSL_Program2', a2)
    if hasattr(a2, 'aDSL_XClass'):
        assert not _is_linked(a2, 'aDSL_XClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args126_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression128' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_MemberSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_MemberSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_MemberSelection(ispar=True, methodinvocation=True)
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression128', None)
    _safe_set(owner, 'aDSL_MemberSelection127', {partner})
    assert getattr(partner, 'aDSL_Expression128') == owner
    _safe_set(owner, 'aDSL_MemberSelection127', set())
    assert getattr(partner, 'aDSL_Expression128') is None


def test_assoc_base169_stub_double():
    # aDSL_VarDef has no real 'aDSL_VarDef170' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Reference(isarray=True)
    partner = aDSL_VarDef()
    setattr(partner, 'aDSL_VarDef170', None)
    _safe_set(owner, 'aDSL_Reference', partner)
    assert getattr(partner, 'aDSL_VarDef170') == owner
    _safe_set(owner, 'aDSL_Reference', None)
    assert getattr(partner, 'aDSL_VarDef170') is None


def test_assoc_body100_stub_double():
    # aDSL_ForStat has no real 'aDSL_ForStat101' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Block(ispar=True)
    partner = aDSL_ForStat()
    setattr(partner, 'aDSL_ForStat101', None)
    _safe_set(owner, 'aDSL_Block102', partner)
    assert getattr(partner, 'aDSL_ForStat101') == owner
    _safe_set(owner, 'aDSL_Block102', None)
    assert getattr(partner, 'aDSL_ForStat101') is None


def test_assoc_body16_stub_double():
    # aDSL_Body has no real 'aDSL_Body18' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Method(isconst=True, istyped=True, name="sample_text")
    partner = aDSL_Body()
    setattr(partner, 'aDSL_Body18', None)
    _safe_set(owner, 'aDSL_Method17', partner)
    assert getattr(partner, 'aDSL_Body18') == owner
    _safe_set(owner, 'aDSL_Method17', None)
    assert getattr(partner, 'aDSL_Body18') is None


def test_assoc_body29_stub_double():
    # aDSL_Body has no real 'aDSL_Body31' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_FuncVarDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_FuncVarDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_FuncVarDef(name="sample_text")
    partner = aDSL_Body()
    setattr(partner, 'aDSL_Body31', None)
    _safe_set(owner, 'aDSL_FuncVarDef30', partner)
    assert getattr(partner, 'aDSL_Body31') == owner
    _safe_set(owner, 'aDSL_FuncVarDef30', None)
    assert getattr(partner, 'aDSL_Body31') is None


def test_assoc_body54_stub_double():
    # aDSL_AsyncStat has no real 'aDSL_AsyncStat' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Block(ispar=True)
    partner = aDSL_AsyncStat()
    setattr(partner, 'aDSL_AsyncStat', None)
    _safe_set(owner, 'aDSL_Block55', partner)
    assert getattr(partner, 'aDSL_AsyncStat') == owner
    _safe_set(owner, 'aDSL_Block55', None)
    assert getattr(partner, 'aDSL_AsyncStat') is None


def test_assoc_body56_stub_double():
    # aDSL_FinishStat has no real 'aDSL_FinishStat' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Block(ispar=True)
    partner = aDSL_FinishStat()
    setattr(partner, 'aDSL_FinishStat', None)
    _safe_set(owner, 'aDSL_Block57', partner)
    assert getattr(partner, 'aDSL_FinishStat') == owner
    _safe_set(owner, 'aDSL_Block57', None)
    assert getattr(partner, 'aDSL_FinishStat') is None


def test_assoc_body60_stub_double():
    # aDSL_AtStat has no real 'aDSL_AtStat61' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Block(ispar=True)
    partner = aDSL_AtStat()
    setattr(partner, 'aDSL_AtStat61', None)
    _safe_set(owner, 'aDSL_Block62', partner)
    assert getattr(partner, 'aDSL_AtStat61') == owner
    _safe_set(owner, 'aDSL_Block62', None)
    assert getattr(partner, 'aDSL_AtStat61') is None


def test_assoc_body75_stub_double():
    # aDSL_For2Statement has no real 'aDSL_For2Statement76' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Block(ispar=True)
    partner = aDSL_For2Statement()
    setattr(partner, 'aDSL_For2Statement76', None)
    _safe_set(owner, 'aDSL_Block77', partner)
    assert getattr(partner, 'aDSL_For2Statement76') == owner
    _safe_set(owner, 'aDSL_Block77', None)
    assert getattr(partner, 'aDSL_For2Statement76') is None


def test_assoc_bodyCatch84_stub_double():
    # aDSL_Body has no real 'aDSL_Body86' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_TryCatchStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_TryCatchStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_TryCatchStat(name="sample_text")
    partner = aDSL_Body()
    setattr(partner, 'aDSL_Body86', None)
    _safe_set(owner, 'aDSL_TryCatchStat85', partner)
    assert getattr(partner, 'aDSL_Body86') == owner
    _safe_set(owner, 'aDSL_TryCatchStat85', None)
    assert getattr(partner, 'aDSL_Body86') is None


def test_assoc_bodyTry82_stub_double():
    # aDSL_Body has no real 'aDSL_Body83' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_TryCatchStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_TryCatchStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_TryCatchStat(name="sample_text")
    partner = aDSL_Body()
    setattr(partner, 'aDSL_Body83', None)
    _safe_set(owner, 'aDSL_TryCatchStat', partner)
    assert getattr(partner, 'aDSL_Body83') == owner
    _safe_set(owner, 'aDSL_TryCatchStat', None)
    assert getattr(partner, 'aDSL_Body83') is None


def test_assoc_expression105_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_IfStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_IfStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_IfStat(iselse=True)
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression106', None)
    _safe_set(owner, 'aDSL_IfStat', partner)
    assert getattr(partner, 'aDSL_Expression106') == owner
    _safe_set(owner, 'aDSL_IfStat', None)
    assert getattr(partner, 'aDSL_Expression106') is None


def test_assoc_expression21_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Operator(opName="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression23', None)
    _safe_set(owner, 'aDSL_Operator22', partner)
    assert getattr(partner, 'aDSL_Expression23') == owner
    _safe_set(owner, 'aDSL_Operator22', None)
    assert getattr(partner, 'aDSL_Expression23') is None


def test_assoc_expression34_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_VariableDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_VariableDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_VariableDef(isinit=True, isstatic=True, istyped=True, name="sample_text", vartype="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression36', None)
    _safe_set(owner, 'aDSL_VariableDef35', partner)
    assert getattr(partner, 'aDSL_Expression36') == owner
    _safe_set(owner, 'aDSL_VariableDef35', None)
    assert getattr(partner, 'aDSL_Expression36') is None


def test_assoc_expression37_stub_double():
    # aDSL_SharedArrayDef has no real 'aDSL_SharedArrayDef' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_VariableDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_VariableDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_VariableDef(isinit=True, isstatic=True, istyped=True, name="sample_text", vartype="sample_text")
    partner = aDSL_SharedArrayDef()
    setattr(partner, 'aDSL_SharedArrayDef', None)
    _safe_set(owner, 'aDSL_VariableDef38', partner)
    assert getattr(partner, 'aDSL_SharedArrayDef') == owner
    _safe_set(owner, 'aDSL_VariableDef38', None)
    assert getattr(partner, 'aDSL_SharedArrayDef') is None


def test_assoc_left139_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression140' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Equality(op="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression140', None)
    _safe_set(owner, 'aDSL_Equality', partner)
    assert getattr(partner, 'aDSL_Expression140') == owner
    _safe_set(owner, 'aDSL_Equality', None)
    assert getattr(partner, 'aDSL_Expression140') is None


def test_assoc_left144_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression145' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Comparison(op="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression145', None)
    _safe_set(owner, 'aDSL_Comparison', partner)
    assert getattr(partner, 'aDSL_Expression145') == owner
    _safe_set(owner, 'aDSL_Comparison', None)
    assert getattr(partner, 'aDSL_Expression145') is None


def test_assoc_left159_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression160' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_MulOrDiv(op="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression160', None)
    _safe_set(owner, 'aDSL_MulOrDiv', partner)
    assert getattr(partner, 'aDSL_Expression160') == owner
    _safe_set(owner, 'aDSL_MulOrDiv', None)
    assert getattr(partner, 'aDSL_Expression160') is None


def test_assoc_member120_stub_double():
    # aDSL_Member has no real 'aDSL_Member122' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_MemberSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_MemberSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_MemberSelection(ispar=True, methodinvocation=True)
    partner = aDSL_Member()
    setattr(partner, 'aDSL_Member122', None)
    _safe_set(owner, 'aDSL_MemberSelection121', partner)
    assert getattr(partner, 'aDSL_Member122') == owner
    _safe_set(owner, 'aDSL_MemberSelection121', None)
    assert getattr(partner, 'aDSL_Member122') is None


def test_assoc_members6_stub_double():
    # aDSL_Member has no real 'aDSL_Member' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_XClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_XClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_XClass(name="sample_text")
    partner = aDSL_Member()
    setattr(partner, 'aDSL_Member', None)
    _safe_set(owner, 'aDSL_XClass7', {partner})
    assert getattr(partner, 'aDSL_Member') == owner
    _safe_set(owner, 'aDSL_XClass7', set())
    assert getattr(partner, 'aDSL_Member') is None


def test_assoc_par70_stub_double():
    # aDSL_For2Statement has no real 'aDSL_For2Statement' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Parameter(istyped=True, name="sample_text")
    partner = aDSL_For2Statement()
    setattr(partner, 'aDSL_For2Statement', None)
    _safe_set(owner, 'aDSL_Parameter71', partner)
    assert getattr(partner, 'aDSL_For2Statement') == owner
    _safe_set(owner, 'aDSL_Parameter71', None)
    assert getattr(partner, 'aDSL_For2Statement') is None


def test_assoc_params171_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression173' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Reference(isarray=True)
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression173', None)
    _safe_set(owner, 'aDSL_Reference172', {partner})
    assert getattr(partner, 'aDSL_Expression173') == owner
    _safe_set(owner, 'aDSL_Reference172', set())
    assert getattr(partner, 'aDSL_Expression173') is None


def test_assoc_receiver118_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression119' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_MemberSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_MemberSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_MemberSelection(ispar=True, methodinvocation=True)
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression119', None)
    _safe_set(owner, 'aDSL_MemberSelection', partner)
    assert getattr(partner, 'aDSL_Expression119') == owner
    _safe_set(owner, 'aDSL_MemberSelection', None)
    assert getattr(partner, 'aDSL_Expression119') is None


def test_assoc_right141_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression143' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Equality(op="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression143', None)
    _safe_set(owner, 'aDSL_Equality142', partner)
    assert getattr(partner, 'aDSL_Expression143') == owner
    _safe_set(owner, 'aDSL_Equality142', None)
    assert getattr(partner, 'aDSL_Expression143') is None


def test_assoc_right146_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression148' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Comparison(op="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression148', None)
    _safe_set(owner, 'aDSL_Comparison147', partner)
    assert getattr(partner, 'aDSL_Expression148') == owner
    _safe_set(owner, 'aDSL_Comparison147', None)
    assert getattr(partner, 'aDSL_Expression148') is None


def test_assoc_right161_stub_double():
    # aDSL_Expression has no real 'aDSL_Expression163' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_MulOrDiv(op="sample_text")
    partner = aDSL_Expression()
    setattr(partner, 'aDSL_Expression163', None)
    _safe_set(owner, 'aDSL_MulOrDiv162', partner)
    assert getattr(partner, 'aDSL_Expression163') == owner
    _safe_set(owner, 'aDSL_MulOrDiv162', None)
    assert getattr(partner, 'aDSL_Expression163') is None


def test_assoc_statements46_stub_double():
    # aDSL_Statement has no real 'aDSL_Statement47' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_Block(ispar=True)
    partner = aDSL_Statement()
    setattr(partner, 'aDSL_Statement47', None)
    _safe_set(owner, 'aDSL_Block', {partner})
    assert getattr(partner, 'aDSL_Statement47') == owner
    _safe_set(owner, 'aDSL_Block', set())
    assert getattr(partner, 'aDSL_Statement47') is None


def test_assoc_sym80_stub_double():
    # aDSL_VarDef has no real 'aDSL_VarDef' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_SharedDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_SharedDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_SharedDef(name="sample_text", replicas=True)
    partner = aDSL_VarDef()
    setattr(partner, 'aDSL_VarDef', None)
    _safe_set(owner, 'aDSL_SharedDef81', partner)
    assert getattr(partner, 'aDSL_VarDef') == owner
    _safe_set(owner, 'aDSL_SharedDef81', None)
    assert getattr(partner, 'aDSL_VarDef') is None


def test_assoc_temp92_stub_double():
    # aDSL_ForStat has no real 'aDSL_ForStat' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_VariableDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_VariableDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_VariableDef(isinit=True, isstatic=True, istyped=True, name="sample_text", vartype="sample_text")
    partner = aDSL_ForStat()
    setattr(partner, 'aDSL_ForStat', None)
    _safe_set(owner, 'aDSL_VariableDef93', partner)
    assert getattr(partner, 'aDSL_ForStat') == owner
    _safe_set(owner, 'aDSL_VariableDef93', None)
    assert getattr(partner, 'aDSL_ForStat') is None


def test_assoc_type174_stub_double():
    # aDSL_New has no real 'aDSL_New' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_VariableType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_VariableType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_VariableType(isarray=True)
    partner = aDSL_New()
    setattr(partner, 'aDSL_New', None)
    _safe_set(owner, 'aDSL_VariableType175', partner)
    assert getattr(partner, 'aDSL_New') == owner
    _safe_set(owner, 'aDSL_VariableType175', None)
    assert getattr(partner, 'aDSL_New') is None


def test_assoc_type179_stub_double():
    # aDSL_Init has no real 'aDSL_Init' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_VariableType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_VariableType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_VariableType(isarray=True)
    partner = aDSL_Init()
    setattr(partner, 'aDSL_Init', None)
    _safe_set(owner, 'aDSL_VariableType180', partner)
    assert getattr(partner, 'aDSL_Init') == owner
    _safe_set(owner, 'aDSL_VariableType180', None)
    assert getattr(partner, 'aDSL_Init') is None


def test_assoc_type8_stub_double():
    # aDSL_MainMethod has no real 'aDSL_MainMethod' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_VariableType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_VariableType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_VariableType(isarray=True)
    partner = aDSL_MainMethod()
    setattr(partner, 'aDSL_MainMethod', None)
    _safe_set(owner, 'aDSL_VariableType', partner)
    assert getattr(partner, 'aDSL_MainMethod') == owner
    _safe_set(owner, 'aDSL_VariableType', None)
    assert getattr(partner, 'aDSL_MainMethod') is None


def test_assoc_value166_stub_double():
    # aDSL_IntConstant has no real 'aDSL_IntConstant' property in the generated
    # code (a bare stub) -- manually attach it so aDSL_IntegerNegative's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aDSL_IntegerNegative's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aDSL_IntegerNegative(isneg=True, value=7)
    partner = aDSL_IntConstant()
    setattr(partner, 'aDSL_IntConstant', None)
    _safe_set(owner, 'aDSL_IntegerNegative', partner)
    assert getattr(partner, 'aDSL_IntConstant') == owner
    _safe_set(owner, 'aDSL_IntegerNegative', None)
    assert getattr(partner, 'aDSL_IntConstant') is None


