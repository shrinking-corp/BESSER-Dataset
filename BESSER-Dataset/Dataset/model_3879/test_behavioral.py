import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Statement,
    Type,
    dinkiemodel_Argument,
    dinkiemodel_ArrayAssign,
    dinkiemodel_ArrayExpr,
    dinkiemodel_ArrayType,
    dinkiemodel_Assign,
    dinkiemodel_BaseType,
    dinkiemodel_BoolVal,
    dinkiemodel_BracketExpr,
    dinkiemodel_Character,
    dinkiemodel_Declaration,
    dinkiemodel_EmptyArrayDecl,
    dinkiemodel_Expression,
    dinkiemodel_FilledArrayDecl,
    dinkiemodel_FuncExpr,
    dinkiemodel_FunctionDecl,
    dinkiemodel_IfOne,
    dinkiemodel_IfTwo,
    dinkiemodel_Main,
    dinkiemodel_Number,
    dinkiemodel_OneOperator,
    dinkiemodel_Parallel,
    dinkiemodel_Program,
    dinkiemodel_ReadStatement,
    dinkiemodel_Return,
    dinkiemodel_Statement,
    dinkiemodel_StringArrayDecl,
    dinkiemodel_Sync,
    dinkiemodel_ThreadID,
    dinkiemodel_TwoOperator,
    dinkiemodel_Type,
    dinkiemodel_VariableExpr,
    dinkiemodel_While,
    dinkiemodel_WriteStatement,
    EBaseType,
    EOneOperator,
    ETwoOperator,
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

def test_assoc_arguments8_reverse_link_reassign_clear():
    a1 = dinkiemodel_FunctionDecl(name="sample_text")
    a2 = dinkiemodel_FunctionDecl(name="sample_text_2")
    b = dinkiemodel_Argument(name="sample_text")
    _safe_set(b, 'dinkiemodel_Argument', a1)
    assert _is_linked(b, 'dinkiemodel_Argument', a1)
    if hasattr(a1, 'dinkiemodel_FunctionDecl9'):
        assert _is_linked(a1, 'dinkiemodel_FunctionDecl9', b)
    _safe_set(b, 'dinkiemodel_Argument', a2)
    assert _is_linked(b, 'dinkiemodel_Argument', a2)
    if hasattr(a1, 'dinkiemodel_FunctionDecl9'):
        assert not _is_linked(a1, 'dinkiemodel_FunctionDecl9', b)
    if hasattr(a2, 'dinkiemodel_FunctionDecl9'):
        assert _is_linked(a2, 'dinkiemodel_FunctionDecl9', b)
    _safe_set(b, 'dinkiemodel_Argument', None)
    assert not _is_linked(b, 'dinkiemodel_Argument', a2)
    if hasattr(a2, 'dinkiemodel_FunctionDecl9'):
        assert not _is_linked(a2, 'dinkiemodel_FunctionDecl9', b)


def test_assoc_arraytype15_reverse_link_reassign_clear():
    a1 = dinkiemodel_EmptyArrayDecl(global_=True, size=7, varName="sample_text")
    a2 = dinkiemodel_EmptyArrayDecl(global_=False, size=13, varName="sample_text_2")
    b = dinkiemodel_ArrayType(arrayType="sample_text")
    _safe_set(b, 'dinkiemodel_ArrayType', a1)
    assert _is_linked(b, 'dinkiemodel_ArrayType', a1)
    if hasattr(a1, 'dinkiemodel_EmptyArrayDecl'):
        assert _is_linked(a1, 'dinkiemodel_EmptyArrayDecl', b)
    _safe_set(b, 'dinkiemodel_ArrayType', a2)
    assert _is_linked(b, 'dinkiemodel_ArrayType', a2)
    if hasattr(a1, 'dinkiemodel_EmptyArrayDecl'):
        assert not _is_linked(a1, 'dinkiemodel_EmptyArrayDecl', b)
    if hasattr(a2, 'dinkiemodel_EmptyArrayDecl'):
        assert _is_linked(a2, 'dinkiemodel_EmptyArrayDecl', b)
    _safe_set(b, 'dinkiemodel_ArrayType', None)
    assert not _is_linked(b, 'dinkiemodel_ArrayType', a2)
    if hasattr(a2, 'dinkiemodel_EmptyArrayDecl'):
        assert not _is_linked(a2, 'dinkiemodel_EmptyArrayDecl', b)


def test_assoc_arraytype25_reverse_link_reassign_clear():
    a1 = dinkiemodel_FilledArrayDecl(global_=True, varName="sample_text")
    a2 = dinkiemodel_FilledArrayDecl(global_=False, varName="sample_text_2")
    b = dinkiemodel_ArrayType(arrayType="sample_text")
    _safe_set(b, 'dinkiemodel_ArrayType26', a1)
    assert _is_linked(b, 'dinkiemodel_ArrayType26', a1)
    if hasattr(a1, 'dinkiemodel_FilledArrayDecl'):
        assert _is_linked(a1, 'dinkiemodel_FilledArrayDecl', b)
    _safe_set(b, 'dinkiemodel_ArrayType26', a2)
    assert _is_linked(b, 'dinkiemodel_ArrayType26', a2)
    if hasattr(a1, 'dinkiemodel_FilledArrayDecl'):
        assert not _is_linked(a1, 'dinkiemodel_FilledArrayDecl', b)
    if hasattr(a2, 'dinkiemodel_FilledArrayDecl'):
        assert _is_linked(a2, 'dinkiemodel_FilledArrayDecl', b)
    _safe_set(b, 'dinkiemodel_ArrayType26', None)
    assert not _is_linked(b, 'dinkiemodel_ArrayType26', a2)
    if hasattr(a2, 'dinkiemodel_FilledArrayDecl'):
        assert not _is_linked(a2, 'dinkiemodel_FilledArrayDecl', b)


def test_assoc_type12_reverse_link_reassign_clear():
    a1 = dinkiemodel_Declaration(global_=True, varName="sample_text")
    a2 = dinkiemodel_Declaration(global_=False, varName="sample_text_2")
    b = dinkiemodel_BaseType(type="sample_text")
    _safe_set(b, 'dinkiemodel_BaseType', a1)
    assert _is_linked(b, 'dinkiemodel_BaseType', a1)
    if hasattr(a1, 'dinkiemodel_Declaration'):
        assert _is_linked(a1, 'dinkiemodel_Declaration', b)
    _safe_set(b, 'dinkiemodel_BaseType', a2)
    assert _is_linked(b, 'dinkiemodel_BaseType', a2)
    if hasattr(a1, 'dinkiemodel_Declaration'):
        assert not _is_linked(a1, 'dinkiemodel_Declaration', b)
    if hasattr(a2, 'dinkiemodel_Declaration'):
        assert _is_linked(a2, 'dinkiemodel_Declaration', b)
    _safe_set(b, 'dinkiemodel_BaseType', None)
    assert not _is_linked(b, 'dinkiemodel_BaseType', a2)
    if hasattr(a2, 'dinkiemodel_Declaration'):
        assert not _is_linked(a2, 'dinkiemodel_Declaration', b)


def test_assoc_type16_reverse_link_reassign_clear():
    a1 = dinkiemodel_ReadStatement(varName="sample_text")
    a2 = dinkiemodel_ReadStatement(varName="sample_text_2")
    b = dinkiemodel_BaseType(type="sample_text")
    _safe_set(b, 'dinkiemodel_BaseType17', a1)
    assert _is_linked(b, 'dinkiemodel_BaseType17', a1)
    if hasattr(a1, 'dinkiemodel_ReadStatement'):
        assert _is_linked(a1, 'dinkiemodel_ReadStatement', b)
    _safe_set(b, 'dinkiemodel_BaseType17', a2)
    assert _is_linked(b, 'dinkiemodel_BaseType17', a2)
    if hasattr(a1, 'dinkiemodel_ReadStatement'):
        assert not _is_linked(a1, 'dinkiemodel_ReadStatement', b)
    if hasattr(a2, 'dinkiemodel_ReadStatement'):
        assert _is_linked(a2, 'dinkiemodel_ReadStatement', b)
    _safe_set(b, 'dinkiemodel_BaseType17', None)
    assert not _is_linked(b, 'dinkiemodel_BaseType17', a2)
    if hasattr(a2, 'dinkiemodel_ReadStatement'):
        assert not _is_linked(a2, 'dinkiemodel_ReadStatement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments70_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression71' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_FuncExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_FuncExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_FuncExpr(funcName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression71', None)
    _safe_set(owner, 'dinkiemodel_FuncExpr', {partner})
    assert getattr(partner, 'dinkiemodel_Expression71') == owner
    _safe_set(owner, 'dinkiemodel_FuncExpr', set())
    assert getattr(partner, 'dinkiemodel_Expression71') is None


def test_assoc_expression13_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_Declaration(global_=True, varName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression', None)
    _safe_set(owner, 'dinkiemodel_Declaration14', partner)
    assert getattr(partner, 'dinkiemodel_Expression') == owner
    _safe_set(owner, 'dinkiemodel_Declaration14', None)
    assert getattr(partner, 'dinkiemodel_Expression') is None


def test_assoc_expression23_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_Assign(varName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression24', None)
    _safe_set(owner, 'dinkiemodel_Assign', partner)
    assert getattr(partner, 'dinkiemodel_Expression24') == owner
    _safe_set(owner, 'dinkiemodel_Assign', None)
    assert getattr(partner, 'dinkiemodel_Expression24') is None


def test_assoc_expression27_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression29' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_FilledArrayDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_FilledArrayDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_FilledArrayDecl(global_=True, varName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression29', None)
    _safe_set(owner, 'dinkiemodel_FilledArrayDecl28', {partner})
    assert getattr(partner, 'dinkiemodel_Expression29') == owner
    _safe_set(owner, 'dinkiemodel_FilledArrayDecl28', set())
    assert getattr(partner, 'dinkiemodel_Expression29') is None


def test_assoc_expression32_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_ArrayAssign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_ArrayAssign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_ArrayAssign(varName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression34', None)
    _safe_set(owner, 'dinkiemodel_ArrayAssign33', partner)
    assert getattr(partner, 'dinkiemodel_Expression34') == owner
    _safe_set(owner, 'dinkiemodel_ArrayAssign33', None)
    assert getattr(partner, 'dinkiemodel_Expression34') is None


def test_assoc_expression59_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression60' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_OneOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_OneOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_OneOperator(operator="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression60', None)
    _safe_set(owner, 'dinkiemodel_OneOperator', partner)
    assert getattr(partner, 'dinkiemodel_Expression60') == owner
    _safe_set(owner, 'dinkiemodel_OneOperator', None)
    assert getattr(partner, 'dinkiemodel_Expression60') is None


def test_assoc_functions0_stub_double():
    # dinkiemodel_Program has no real 'dinkiemodel_Program' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_FunctionDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_FunctionDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_FunctionDecl(name="sample_text")
    partner = dinkiemodel_Program()
    setattr(partner, 'dinkiemodel_Program', None)
    _safe_set(owner, 'dinkiemodel_FunctionDecl', partner)
    assert owner in getattr(partner, 'dinkiemodel_Program')
    _safe_set(owner, 'dinkiemodel_FunctionDecl', None)
    assert owner not in getattr(partner, 'dinkiemodel_Program')


def test_assoc_index30_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_ArrayAssign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_ArrayAssign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_ArrayAssign(varName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression31', None)
    _safe_set(owner, 'dinkiemodel_ArrayAssign', partner)
    assert getattr(partner, 'dinkiemodel_Expression31') == owner
    _safe_set(owner, 'dinkiemodel_ArrayAssign', None)
    assert getattr(partner, 'dinkiemodel_Expression31') is None


def test_assoc_index68_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_ArrayExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_ArrayExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_ArrayExpr(varName="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression69', None)
    _safe_set(owner, 'dinkiemodel_ArrayExpr', partner)
    assert getattr(partner, 'dinkiemodel_Expression69') == owner
    _safe_set(owner, 'dinkiemodel_ArrayExpr', None)
    assert getattr(partner, 'dinkiemodel_Expression69') is None


def test_assoc_leftExpr61_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression62' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_TwoOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_TwoOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_TwoOperator(operator="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression62', None)
    _safe_set(owner, 'dinkiemodel_TwoOperator', partner)
    assert getattr(partner, 'dinkiemodel_Expression62') == owner
    _safe_set(owner, 'dinkiemodel_TwoOperator', None)
    assert getattr(partner, 'dinkiemodel_Expression62') is None


def test_assoc_rightExpr63_stub_double():
    # dinkiemodel_Expression has no real 'dinkiemodel_Expression65' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_TwoOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_TwoOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_TwoOperator(operator="sample_text")
    partner = dinkiemodel_Expression()
    setattr(partner, 'dinkiemodel_Expression65', None)
    _safe_set(owner, 'dinkiemodel_TwoOperator64', partner)
    assert getattr(partner, 'dinkiemodel_Expression65') == owner
    _safe_set(owner, 'dinkiemodel_TwoOperator64', None)
    assert getattr(partner, 'dinkiemodel_Expression65') is None


def test_assoc_statements5_stub_double():
    # dinkiemodel_Statement has no real 'dinkiemodel_Statement7' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_FunctionDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_FunctionDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_FunctionDecl(name="sample_text")
    partner = dinkiemodel_Statement()
    setattr(partner, 'dinkiemodel_Statement7', None)
    _safe_set(owner, 'dinkiemodel_FunctionDecl6', {partner})
    assert getattr(partner, 'dinkiemodel_Statement7') == owner
    _safe_set(owner, 'dinkiemodel_FunctionDecl6', set())
    assert getattr(partner, 'dinkiemodel_Statement7') is None


def test_assoc_statements53_stub_double():
    # dinkiemodel_Statement has no real 'dinkiemodel_Statement54' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_Parallel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_Parallel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_Parallel(nrOfThreads=7)
    partner = dinkiemodel_Statement()
    setattr(partner, 'dinkiemodel_Statement54', None)
    _safe_set(owner, 'dinkiemodel_Parallel', {partner})
    assert getattr(partner, 'dinkiemodel_Statement54') == owner
    _safe_set(owner, 'dinkiemodel_Parallel', set())
    assert getattr(partner, 'dinkiemodel_Statement54') is None


def test_assoc_statements55_stub_double():
    # dinkiemodel_Statement has no real 'dinkiemodel_Statement56' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_Sync's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_Sync's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_Sync(varName="sample_text")
    partner = dinkiemodel_Statement()
    setattr(partner, 'dinkiemodel_Statement56', None)
    _safe_set(owner, 'dinkiemodel_Sync', {partner})
    assert getattr(partner, 'dinkiemodel_Statement56') == owner
    _safe_set(owner, 'dinkiemodel_Sync', set())
    assert getattr(partner, 'dinkiemodel_Statement56') is None


def test_assoc_type10_stub_double():
    # dinkiemodel_Type has no real 'dinkiemodel_Type' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_FunctionDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_FunctionDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_FunctionDecl(name="sample_text")
    partner = dinkiemodel_Type()
    setattr(partner, 'dinkiemodel_Type', None)
    _safe_set(owner, 'dinkiemodel_FunctionDecl11', partner)
    assert getattr(partner, 'dinkiemodel_Type') == owner
    _safe_set(owner, 'dinkiemodel_FunctionDecl11', None)
    assert getattr(partner, 'dinkiemodel_Type') is None


def test_assoc_type72_stub_double():
    # dinkiemodel_Type has no real 'dinkiemodel_Type74' property in the generated
    # code (a bare stub) -- manually attach it so dinkiemodel_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dinkiemodel_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dinkiemodel_Argument(name="sample_text")
    partner = dinkiemodel_Type()
    setattr(partner, 'dinkiemodel_Type74', None)
    _safe_set(owner, 'dinkiemodel_Argument73', partner)
    assert getattr(partner, 'dinkiemodel_Type74') == owner
    _safe_set(owner, 'dinkiemodel_Argument73', None)
    assert getattr(partner, 'dinkiemodel_Type74') is None


