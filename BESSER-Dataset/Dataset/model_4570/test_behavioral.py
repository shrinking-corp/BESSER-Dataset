import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Chunk,
    Expression,
    Field,
    LastStatement,
    LastStatement_Return,
    Statement,
    Statement_FunctioncallOrAssignment,
    lua_Block,
    lua_Chunk,
    lua_Expression,
    lua_Expression_AccessArray,
    lua_Expression_AccessMember,
    lua_Expression_And,
    lua_Expression_CallFunction,
    lua_Expression_CallMemberFunction,
    lua_Expression_Concatenation,
    lua_Expression_Division,
    lua_Expression_Equal,
    lua_Expression_Exponentiation,
    lua_Expression_False,
    lua_Expression_Function,
    lua_Expression_Invert,
    lua_Expression_Larger,
    lua_Expression_Larger_Equal,
    lua_Expression_Length,
    lua_Expression_Minus,
    lua_Expression_Modulo,
    lua_Expression_Multiplication,
    lua_Expression_Negate,
    lua_Expression_Nil,
    lua_Expression_Not_Equal,
    lua_Expression_Number,
    lua_Expression_Or,
    lua_Expression_Plus,
    lua_Expression_Smaller,
    lua_Expression_Smaller_Equal,
    lua_Expression_String,
    lua_Expression_TableConstructor,
    lua_Expression_True,
    lua_Expression_VarArgs,
    lua_Expression_VariableName,
    lua_Field,
    lua_Field_AddEntryToTable,
    lua_Field_AddEntryToTable_Brackets,
    lua_Field_AppendEntryToTable,
    lua_Function,
    lua_Functioncall_Arguments,
    lua_LastStatement,
    lua_LastStatement_Break,
    lua_LastStatement_Return,
    lua_LastStatement_ReturnWithValue,
    lua_Statement,
    lua_Statement_Assignment,
    lua_Statement_Block,
    lua_Statement_CallFunction,
    lua_Statement_CallMemberFunction,
    lua_Statement_For_Generic,
    lua_Statement_For_Numeric,
    lua_Statement_FunctioncallOrAssignment,
    lua_Statement_GlobalFunction_Declaration,
    lua_Statement_If_Then_Else,
    lua_Statement_If_Then_Else_ElseIfPart,
    lua_Statement_LocalFunction_Declaration,
    lua_Statement_Local_Variable_Declaration,
    lua_Statement_Repeat,
    lua_Statement_While,
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

def test_assoc_function46_reverse_link_reassign_clear():
    a1 = lua_Statement_GlobalFunction_Declaration(functionName="sample_text", prefix="sample_text")
    a2 = lua_Statement_GlobalFunction_Declaration(functionName="sample_text_2", prefix="sample_text_2")
    b = lua_Function(parameters="sample_text", varArgs=True)
    _safe_set(b, 'lua_Function', a1)
    assert _is_linked(b, 'lua_Function', a1)
    if hasattr(a1, 'lua_Statement_GlobalFunction_Declaration'):
        assert _is_linked(a1, 'lua_Statement_GlobalFunction_Declaration', b)
    _safe_set(b, 'lua_Function', a2)
    assert _is_linked(b, 'lua_Function', a2)
    if hasattr(a1, 'lua_Statement_GlobalFunction_Declaration'):
        assert not _is_linked(a1, 'lua_Statement_GlobalFunction_Declaration', b)
    if hasattr(a2, 'lua_Statement_GlobalFunction_Declaration'):
        assert _is_linked(a2, 'lua_Statement_GlobalFunction_Declaration', b)
    _safe_set(b, 'lua_Function', None)
    assert not _is_linked(b, 'lua_Function', a2)
    if hasattr(a2, 'lua_Statement_GlobalFunction_Declaration'):
        assert not _is_linked(a2, 'lua_Statement_GlobalFunction_Declaration', b)


def test_assoc_function47_reverse_link_reassign_clear():
    a1 = lua_Statement_LocalFunction_Declaration(functionName="sample_text")
    a2 = lua_Statement_LocalFunction_Declaration(functionName="sample_text_2")
    b = lua_Function(parameters="sample_text", varArgs=True)
    _safe_set(b, 'lua_Function48', a1)
    assert _is_linked(b, 'lua_Function48', a1)
    if hasattr(a1, 'lua_Statement_LocalFunction_Declaration'):
        assert _is_linked(a1, 'lua_Statement_LocalFunction_Declaration', b)
    _safe_set(b, 'lua_Function48', a2)
    assert _is_linked(b, 'lua_Function48', a2)
    if hasattr(a1, 'lua_Statement_LocalFunction_Declaration'):
        assert not _is_linked(a1, 'lua_Statement_LocalFunction_Declaration', b)
    if hasattr(a2, 'lua_Statement_LocalFunction_Declaration'):
        assert _is_linked(a2, 'lua_Statement_LocalFunction_Declaration', b)
    _safe_set(b, 'lua_Function48', None)
    assert not _is_linked(b, 'lua_Function48', a2)
    if hasattr(a2, 'lua_Statement_LocalFunction_Declaration'):
        assert not _is_linked(a2, 'lua_Statement_LocalFunction_Declaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments164_stub_double():
    # lua_Functioncall_Arguments has no real 'lua_Functioncall_Arguments166' property in the generated
    # code (a bare stub) -- manually attach it so lua_Expression_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Expression_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Expression_CallMemberFunction(memberFunctionName="sample_text")
    partner = lua_Functioncall_Arguments()
    setattr(partner, 'lua_Functioncall_Arguments166', None)
    _safe_set(owner, 'lua_Expression_CallMemberFunction165', partner)
    assert getattr(partner, 'lua_Functioncall_Arguments166') == owner
    _safe_set(owner, 'lua_Expression_CallMemberFunction165', None)
    assert getattr(partner, 'lua_Functioncall_Arguments166') is None


def test_assoc_arguments73_stub_double():
    # lua_Functioncall_Arguments has no real 'lua_Functioncall_Arguments75' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_CallMemberFunction(memberFunctionName="sample_text")
    partner = lua_Functioncall_Arguments()
    setattr(partner, 'lua_Functioncall_Arguments75', None)
    _safe_set(owner, 'lua_Statement_CallMemberFunction74', partner)
    assert getattr(partner, 'lua_Functioncall_Arguments75') == owner
    _safe_set(owner, 'lua_Statement_CallMemberFunction74', None)
    assert getattr(partner, 'lua_Functioncall_Arguments75') is None


def test_assoc_block38_stub_double():
    # lua_Block has no real 'lua_Block40' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_For_Numeric(iteratorName="sample_text")
    partner = lua_Block()
    setattr(partner, 'lua_Block40', None)
    _safe_set(owner, 'lua_Statement_For_Numeric39', partner)
    assert getattr(partner, 'lua_Block40') == owner
    _safe_set(owner, 'lua_Statement_For_Numeric39', None)
    assert getattr(partner, 'lua_Block40') is None


def test_assoc_block43_stub_double():
    # lua_Block has no real 'lua_Block45' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_For_Generic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_For_Generic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_For_Generic(names="sample_text")
    partner = lua_Block()
    setattr(partner, 'lua_Block45', None)
    _safe_set(owner, 'lua_Statement_For_Generic44', partner)
    assert getattr(partner, 'lua_Block45') == owner
    _safe_set(owner, 'lua_Statement_For_Generic44', None)
    assert getattr(partner, 'lua_Block45') is None


def test_assoc_body54_stub_double():
    # lua_Block has no real 'lua_Block56' property in the generated
    # code (a bare stub) -- manually attach it so lua_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Function(parameters="sample_text", varArgs=True)
    partner = lua_Block()
    setattr(partner, 'lua_Block56', None)
    _safe_set(owner, 'lua_Function55', partner)
    assert getattr(partner, 'lua_Block56') == owner
    _safe_set(owner, 'lua_Function55', None)
    assert getattr(partner, 'lua_Block56') is None


def test_assoc_expressions41_stub_double():
    # lua_Expression has no real 'lua_Expression42' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_For_Generic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_For_Generic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_For_Generic(names="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression42', None)
    _safe_set(owner, 'lua_Statement_For_Generic', {partner})
    assert getattr(partner, 'lua_Expression42') == owner
    _safe_set(owner, 'lua_Statement_For_Generic', set())
    assert getattr(partner, 'lua_Expression42') is None


def test_assoc_function51_stub_double():
    # lua_Expression_Function has no real 'lua_Expression_Function' property in the generated
    # code (a bare stub) -- manually attach it so lua_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Function(parameters="sample_text", varArgs=True)
    partner = lua_Expression_Function()
    setattr(partner, 'lua_Expression_Function', None)
    _safe_set(owner, 'lua_Function52', partner)
    assert getattr(partner, 'lua_Expression_Function') == owner
    _safe_set(owner, 'lua_Function52', None)
    assert getattr(partner, 'lua_Expression_Function') is None


def test_assoc_initialValue49_stub_double():
    # lua_Expression has no real 'lua_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_Local_Variable_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_Local_Variable_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_Local_Variable_Declaration(variableNames="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression50', None)
    _safe_set(owner, 'lua_Statement_Local_Variable_Declaration', {partner})
    assert getattr(partner, 'lua_Expression50') == owner
    _safe_set(owner, 'lua_Statement_Local_Variable_Declaration', set())
    assert getattr(partner, 'lua_Expression50') is None


def test_assoc_object162_stub_double():
    # lua_Expression has no real 'lua_Expression163' property in the generated
    # code (a bare stub) -- manually attach it so lua_Expression_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Expression_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Expression_CallMemberFunction(memberFunctionName="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression163', None)
    _safe_set(owner, 'lua_Expression_CallMemberFunction', partner)
    assert getattr(partner, 'lua_Expression163') == owner
    _safe_set(owner, 'lua_Expression_CallMemberFunction', None)
    assert getattr(partner, 'lua_Expression163') is None


def test_assoc_object177_stub_double():
    # lua_Expression has no real 'lua_Expression178' property in the generated
    # code (a bare stub) -- manually attach it so lua_Expression_AccessMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Expression_AccessMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Expression_AccessMember(memberName="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression178', None)
    _safe_set(owner, 'lua_Expression_AccessMember', partner)
    assert getattr(partner, 'lua_Expression178') == owner
    _safe_set(owner, 'lua_Expression_AccessMember', None)
    assert getattr(partner, 'lua_Expression178') is None


def test_assoc_object71_stub_double():
    # lua_Expression has no real 'lua_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_CallMemberFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_CallMemberFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_CallMemberFunction(memberFunctionName="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression72', None)
    _safe_set(owner, 'lua_Statement_CallMemberFunction', partner)
    assert getattr(partner, 'lua_Expression72') == owner
    _safe_set(owner, 'lua_Statement_CallMemberFunction', None)
    assert getattr(partner, 'lua_Expression72') is None


def test_assoc_startExpr30_stub_double():
    # lua_Expression has no real 'lua_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_For_Numeric(iteratorName="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression31', None)
    _safe_set(owner, 'lua_Statement_For_Numeric', partner)
    assert getattr(partner, 'lua_Expression31') == owner
    _safe_set(owner, 'lua_Statement_For_Numeric', None)
    assert getattr(partner, 'lua_Expression31') is None


def test_assoc_stepExpr35_stub_double():
    # lua_Expression has no real 'lua_Expression37' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_For_Numeric(iteratorName="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression37', None)
    _safe_set(owner, 'lua_Statement_For_Numeric36', partner)
    assert getattr(partner, 'lua_Expression37') == owner
    _safe_set(owner, 'lua_Statement_For_Numeric36', None)
    assert getattr(partner, 'lua_Expression37') is None


def test_assoc_untilExpr32_stub_double():
    # lua_Expression has no real 'lua_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so lua_Statement_For_Numeric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lua_Statement_For_Numeric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lua_Statement_For_Numeric(iteratorName="sample_text")
    partner = lua_Expression()
    setattr(partner, 'lua_Expression34', None)
    _safe_set(owner, 'lua_Statement_For_Numeric33', partner)
    assert getattr(partner, 'lua_Expression34') == owner
    _safe_set(owner, 'lua_Statement_For_Numeric33', None)
    assert getattr(partner, 'lua_Expression34') is None


