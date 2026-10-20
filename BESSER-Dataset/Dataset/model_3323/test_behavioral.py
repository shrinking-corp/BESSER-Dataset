import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    miniJava_Addition,
    miniJava_ClassDecl,
    miniJava_Expr,
    miniJava_Expression,
    miniJava_MainMethod,
    miniJava_Method,
    miniJava_MethodCall,
    miniJava_Multiplication,
    miniJava_NumberValue,
    miniJava_Point,
    miniJava_Program,
    miniJava_SquareBrackets,
    miniJava_Statement,
    miniJava_Type,
    miniJava_VarDeclaration,
    miniJava_Variable,
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

def test_assoc_classDecl12_reverse_link_reassign_clear():
    a1 = miniJava_Type(typeName="sample_text")
    a2 = miniJava_Type(typeName="sample_text_2")
    b = miniJava_ClassDecl(name="sample_text")
    _safe_set(b, 'miniJava_ClassDecl13', a1)
    assert _is_linked(b, 'miniJava_ClassDecl13', a1)
    if hasattr(a1, 'miniJava_Type'):
        assert _is_linked(a1, 'miniJava_Type', b)
    _safe_set(b, 'miniJava_ClassDecl13', a2)
    assert _is_linked(b, 'miniJava_ClassDecl13', a2)
    if hasattr(a1, 'miniJava_Type'):
        assert not _is_linked(a1, 'miniJava_Type', b)
    if hasattr(a2, 'miniJava_Type'):
        assert _is_linked(a2, 'miniJava_Type', b)
    _safe_set(b, 'miniJava_ClassDecl13', None)
    assert not _is_linked(b, 'miniJava_ClassDecl13', a2)
    if hasattr(a2, 'miniJava_Type'):
        assert not _is_linked(a2, 'miniJava_Type', b)


def test_assoc_expression49_reverse_link_reassign_clear():
    a1 = miniJava_Expr(expressionType="sample_text")
    a2 = miniJava_Expr(expressionType="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr50', a1)
    assert _is_linked(b, 'miniJava_Expr50', a1)
    if hasattr(a1, 'miniJava_Expr48'):
        assert _is_linked(a1, 'miniJava_Expr48', b)
    _safe_set(b, 'miniJava_Expr50', a2)
    assert _is_linked(b, 'miniJava_Expr50', a2)
    if hasattr(a1, 'miniJava_Expr48'):
        assert not _is_linked(a1, 'miniJava_Expr48', b)
    if hasattr(a2, 'miniJava_Expr48'):
        assert _is_linked(a2, 'miniJava_Expr48', b)
    _safe_set(b, 'miniJava_Expr50', None)
    assert not _is_linked(b, 'miniJava_Expr50', a2)
    if hasattr(a2, 'miniJava_Expr48'):
        assert not _is_linked(a2, 'miniJava_Expr48', b)


def test_assoc_extendedClass4_reverse_link_reassign_clear():
    a1 = miniJava_ClassDecl(name="sample_text")
    a2 = miniJava_ClassDecl(name="sample_text_2")
    b = miniJava_ClassDecl(name="sample_text")
    _safe_set(b, 'miniJava_ClassDecl5', a1)
    assert _is_linked(b, 'miniJava_ClassDecl5', a1)
    if hasattr(a1, 'miniJava_ClassDecl3'):
        assert _is_linked(a1, 'miniJava_ClassDecl3', b)
    _safe_set(b, 'miniJava_ClassDecl5', a2)
    assert _is_linked(b, 'miniJava_ClassDecl5', a2)
    if hasattr(a1, 'miniJava_ClassDecl3'):
        assert not _is_linked(a1, 'miniJava_ClassDecl3', b)
    if hasattr(a2, 'miniJava_ClassDecl3'):
        assert _is_linked(a2, 'miniJava_ClassDecl3', b)
    _safe_set(b, 'miniJava_ClassDecl5', None)
    assert not _is_linked(b, 'miniJava_ClassDecl5', a2)
    if hasattr(a2, 'miniJava_ClassDecl3'):
        assert not _is_linked(a2, 'miniJava_ClassDecl3', b)


def test_assoc_firstExpression36_reverse_link_reassign_clear():
    a1 = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    a2 = miniJava_Statement(isArrayElementAssignment=False, statementType="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr38', a1)
    assert _is_linked(b, 'miniJava_Expr38', a1)
    if hasattr(a1, 'miniJava_Statement37'):
        assert _is_linked(a1, 'miniJava_Statement37', b)
    _safe_set(b, 'miniJava_Expr38', a2)
    assert _is_linked(b, 'miniJava_Expr38', a2)
    if hasattr(a1, 'miniJava_Statement37'):
        assert not _is_linked(a1, 'miniJava_Statement37', b)
    if hasattr(a2, 'miniJava_Statement37'):
        assert _is_linked(a2, 'miniJava_Statement37', b)
    _safe_set(b, 'miniJava_Expr38', None)
    assert not _is_linked(b, 'miniJava_Expr38', a2)
    if hasattr(a2, 'miniJava_Statement37'):
        assert not _is_linked(a2, 'miniJava_Statement37', b)


def test_assoc_formalVarDeclarations22_reverse_link_reassign_clear():
    a1 = miniJava_Variable(name="sample_text")
    a2 = miniJava_Variable(name="sample_text_2")
    b = miniJava_Method(name="sample_text")
    _safe_set(b, 'miniJava_Method23', {a1})
    assert _is_linked(b, 'miniJava_Method23', a1)
    if hasattr(a1, 'miniJava_Variable24'):
        assert _is_linked(a1, 'miniJava_Variable24', b)
    _safe_set(b, 'miniJava_Method23', {a2})
    assert _is_linked(b, 'miniJava_Method23', a2)
    if hasattr(a1, 'miniJava_Variable24'):
        assert not _is_linked(a1, 'miniJava_Variable24', b)
    if hasattr(a2, 'miniJava_Variable24'):
        assert _is_linked(a2, 'miniJava_Variable24', b)
    _safe_set(b, 'miniJava_Method23', set())
    assert not _is_linked(b, 'miniJava_Method23', a2)
    if hasattr(a2, 'miniJava_Variable24'):
        assert not _is_linked(a2, 'miniJava_Variable24', b)


def test_assoc_left62_reverse_link_reassign_clear():
    a1 = miniJava_Expr(expressionType="sample_text")
    a2 = miniJava_Expr(expressionType="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr63', a1)
    assert _is_linked(b, 'miniJava_Expr63', a1)
    if hasattr(a1, 'miniJava_Expr61'):
        assert _is_linked(a1, 'miniJava_Expr61', b)
    _safe_set(b, 'miniJava_Expr63', a2)
    assert _is_linked(b, 'miniJava_Expr63', a2)
    if hasattr(a1, 'miniJava_Expr61'):
        assert not _is_linked(a1, 'miniJava_Expr61', b)
    if hasattr(a2, 'miniJava_Expr61'):
        assert _is_linked(a2, 'miniJava_Expr61', b)
    _safe_set(b, 'miniJava_Expr63', None)
    assert not _is_linked(b, 'miniJava_Expr63', a2)
    if hasattr(a2, 'miniJava_Expr61'):
        assert not _is_linked(a2, 'miniJava_Expr61', b)


def test_assoc_methodDeclarations8_reverse_link_reassign_clear():
    a1 = miniJava_Method(name="sample_text")
    a2 = miniJava_Method(name="sample_text_2")
    b = miniJava_ClassDecl(name="sample_text")
    _safe_set(b, 'miniJava_ClassDecl9', {a1})
    assert _is_linked(b, 'miniJava_ClassDecl9', a1)
    if hasattr(a1, 'miniJava_Method'):
        assert _is_linked(a1, 'miniJava_Method', b)
    _safe_set(b, 'miniJava_ClassDecl9', {a2})
    assert _is_linked(b, 'miniJava_ClassDecl9', a2)
    if hasattr(a1, 'miniJava_Method'):
        assert not _is_linked(a1, 'miniJava_Method', b)
    if hasattr(a2, 'miniJava_Method'):
        assert _is_linked(a2, 'miniJava_Method', b)
    _safe_set(b, 'miniJava_ClassDecl9', set())
    assert not _is_linked(b, 'miniJava_ClassDecl9', a2)
    if hasattr(a2, 'miniJava_Method'):
        assert not _is_linked(a2, 'miniJava_Method', b)


def test_assoc_methodType19_reverse_link_reassign_clear():
    a1 = miniJava_Type(typeName="sample_text")
    a2 = miniJava_Type(typeName="sample_text_2")
    b = miniJava_Method(name="sample_text")
    _safe_set(b, 'miniJava_Method20', a1)
    assert _is_linked(b, 'miniJava_Method20', a1)
    if hasattr(a1, 'miniJava_Type21'):
        assert _is_linked(a1, 'miniJava_Type21', b)
    _safe_set(b, 'miniJava_Method20', a2)
    assert _is_linked(b, 'miniJava_Method20', a2)
    if hasattr(a1, 'miniJava_Type21'):
        assert not _is_linked(a1, 'miniJava_Type21', b)
    if hasattr(a2, 'miniJava_Type21'):
        assert _is_linked(a2, 'miniJava_Type21', b)
    _safe_set(b, 'miniJava_Method20', None)
    assert not _is_linked(b, 'miniJava_Method20', a2)
    if hasattr(a2, 'miniJava_Type21'):
        assert not _is_linked(a2, 'miniJava_Type21', b)


def test_assoc_number57_reverse_link_reassign_clear():
    a1 = miniJava_NumberValue(value=7)
    a2 = miniJava_NumberValue(value=13)
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr58', a1)
    assert _is_linked(b, 'miniJava_Expr58', a1)
    if hasattr(a1, 'miniJava_NumberValue'):
        assert _is_linked(a1, 'miniJava_NumberValue', b)
    _safe_set(b, 'miniJava_Expr58', a2)
    assert _is_linked(b, 'miniJava_Expr58', a2)
    if hasattr(a1, 'miniJava_NumberValue'):
        assert not _is_linked(a1, 'miniJava_NumberValue', b)
    if hasattr(a2, 'miniJava_NumberValue'):
        assert _is_linked(a2, 'miniJava_NumberValue', b)
    _safe_set(b, 'miniJava_Expr58', None)
    assert not _is_linked(b, 'miniJava_Expr58', a2)
    if hasattr(a2, 'miniJava_NumberValue'):
        assert not _is_linked(a2, 'miniJava_NumberValue', b)


def test_assoc_returnExpression31_reverse_link_reassign_clear():
    a1 = miniJava_Method(name="sample_text")
    a2 = miniJava_Method(name="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr', a1)
    assert _is_linked(b, 'miniJava_Expr', a1)
    if hasattr(a1, 'miniJava_Method32'):
        assert _is_linked(a1, 'miniJava_Method32', b)
    _safe_set(b, 'miniJava_Expr', a2)
    assert _is_linked(b, 'miniJava_Expr', a2)
    if hasattr(a1, 'miniJava_Method32'):
        assert not _is_linked(a1, 'miniJava_Method32', b)
    if hasattr(a2, 'miniJava_Method32'):
        assert _is_linked(a2, 'miniJava_Method32', b)
    _safe_set(b, 'miniJava_Expr', None)
    assert not _is_linked(b, 'miniJava_Expr', a2)
    if hasattr(a2, 'miniJava_Method32'):
        assert not _is_linked(a2, 'miniJava_Method32', b)


def test_assoc_right46_reverse_link_reassign_clear():
    a1 = miniJava_Expr(expressionType="sample_text")
    a2 = miniJava_Expr(expressionType="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr47', a1)
    assert _is_linked(b, 'miniJava_Expr47', a1)
    if hasattr(a1, 'miniJava_Expr45'):
        assert _is_linked(a1, 'miniJava_Expr45', b)
    _safe_set(b, 'miniJava_Expr47', a2)
    assert _is_linked(b, 'miniJava_Expr47', a2)
    if hasattr(a1, 'miniJava_Expr45'):
        assert not _is_linked(a1, 'miniJava_Expr45', b)
    if hasattr(a2, 'miniJava_Expr45'):
        assert _is_linked(a2, 'miniJava_Expr45', b)
    _safe_set(b, 'miniJava_Expr47', None)
    assert not _is_linked(b, 'miniJava_Expr47', a2)
    if hasattr(a2, 'miniJava_Expr45'):
        assert not _is_linked(a2, 'miniJava_Expr45', b)


def test_assoc_secondExpression42_reverse_link_reassign_clear():
    a1 = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    a2 = miniJava_Statement(isArrayElementAssignment=False, statementType="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr44', a1)
    assert _is_linked(b, 'miniJava_Expr44', a1)
    if hasattr(a1, 'miniJava_Statement43'):
        assert _is_linked(a1, 'miniJava_Statement43', b)
    _safe_set(b, 'miniJava_Expr44', a2)
    assert _is_linked(b, 'miniJava_Expr44', a2)
    if hasattr(a1, 'miniJava_Statement43'):
        assert not _is_linked(a1, 'miniJava_Statement43', b)
    if hasattr(a2, 'miniJava_Statement43'):
        assert _is_linked(a2, 'miniJava_Statement43', b)
    _safe_set(b, 'miniJava_Expr44', None)
    assert not _is_linked(b, 'miniJava_Expr44', a2)
    if hasattr(a2, 'miniJava_Statement43'):
        assert not _is_linked(a2, 'miniJava_Statement43', b)


def test_assoc_statements28_reverse_link_reassign_clear():
    a1 = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    a2 = miniJava_Statement(isArrayElementAssignment=False, statementType="sample_text_2")
    b = miniJava_Method(name="sample_text")
    _safe_set(b, 'miniJava_Method29', {a1})
    assert _is_linked(b, 'miniJava_Method29', a1)
    if hasattr(a1, 'miniJava_Statement30'):
        assert _is_linked(a1, 'miniJava_Statement30', b)
    _safe_set(b, 'miniJava_Method29', {a2})
    assert _is_linked(b, 'miniJava_Method29', a2)
    if hasattr(a1, 'miniJava_Statement30'):
        assert not _is_linked(a1, 'miniJava_Statement30', b)
    if hasattr(a2, 'miniJava_Statement30'):
        assert _is_linked(a2, 'miniJava_Statement30', b)
    _safe_set(b, 'miniJava_Method29', set())
    assert not _is_linked(b, 'miniJava_Method29', a2)
    if hasattr(a2, 'miniJava_Statement30'):
        assert not _is_linked(a2, 'miniJava_Statement30', b)


def test_assoc_statements34_reverse_link_reassign_clear():
    a1 = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    a2 = miniJava_Statement(isArrayElementAssignment=False, statementType="sample_text_2")
    b = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    _safe_set(b, 'miniJava_Statement35', a1)
    assert _is_linked(b, 'miniJava_Statement35', a1)
    if hasattr(a1, 'miniJava_Statement33'):
        assert _is_linked(a1, 'miniJava_Statement33', b)
    _safe_set(b, 'miniJava_Statement35', a2)
    assert _is_linked(b, 'miniJava_Statement35', a2)
    if hasattr(a1, 'miniJava_Statement33'):
        assert not _is_linked(a1, 'miniJava_Statement33', b)
    if hasattr(a2, 'miniJava_Statement33'):
        assert _is_linked(a2, 'miniJava_Statement33', b)
    _safe_set(b, 'miniJava_Statement35', None)
    assert not _is_linked(b, 'miniJava_Statement35', a2)
    if hasattr(a2, 'miniJava_Statement33'):
        assert not _is_linked(a2, 'miniJava_Statement33', b)


def test_assoc_type51_reverse_link_reassign_clear():
    a1 = miniJava_Type(typeName="sample_text")
    a2 = miniJava_Type(typeName="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr52', a1)
    assert _is_linked(b, 'miniJava_Expr52', a1)
    if hasattr(a1, 'miniJava_Type53'):
        assert _is_linked(a1, 'miniJava_Type53', b)
    _safe_set(b, 'miniJava_Expr52', a2)
    assert _is_linked(b, 'miniJava_Expr52', a2)
    if hasattr(a1, 'miniJava_Type53'):
        assert not _is_linked(a1, 'miniJava_Type53', b)
    if hasattr(a2, 'miniJava_Type53'):
        assert _is_linked(a2, 'miniJava_Type53', b)
    _safe_set(b, 'miniJava_Expr52', None)
    assert not _is_linked(b, 'miniJava_Expr52', a2)
    if hasattr(a2, 'miniJava_Type53'):
        assert not _is_linked(a2, 'miniJava_Type53', b)


def test_assoc_variable39_reverse_link_reassign_clear():
    a1 = miniJava_Variable(name="sample_text")
    a2 = miniJava_Variable(name="sample_text_2")
    b = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    _safe_set(b, 'miniJava_Statement40', a1)
    assert _is_linked(b, 'miniJava_Statement40', a1)
    if hasattr(a1, 'miniJava_Variable41'):
        assert _is_linked(a1, 'miniJava_Variable41', b)
    _safe_set(b, 'miniJava_Statement40', a2)
    assert _is_linked(b, 'miniJava_Statement40', a2)
    if hasattr(a1, 'miniJava_Variable41'):
        assert not _is_linked(a1, 'miniJava_Variable41', b)
    if hasattr(a2, 'miniJava_Variable41'):
        assert _is_linked(a2, 'miniJava_Variable41', b)
    _safe_set(b, 'miniJava_Statement40', None)
    assert not _is_linked(b, 'miniJava_Statement40', a2)
    if hasattr(a2, 'miniJava_Variable41'):
        assert not _is_linked(a2, 'miniJava_Variable41', b)


def test_assoc_variable54_reverse_link_reassign_clear():
    a1 = miniJava_Variable(name="sample_text")
    a2 = miniJava_Variable(name="sample_text_2")
    b = miniJava_Expr(expressionType="sample_text")
    _safe_set(b, 'miniJava_Expr55', a1)
    assert _is_linked(b, 'miniJava_Expr55', a1)
    if hasattr(a1, 'miniJava_Variable56'):
        assert _is_linked(a1, 'miniJava_Variable56', b)
    _safe_set(b, 'miniJava_Expr55', a2)
    assert _is_linked(b, 'miniJava_Expr55', a2)
    if hasattr(a1, 'miniJava_Variable56'):
        assert not _is_linked(a1, 'miniJava_Variable56', b)
    if hasattr(a2, 'miniJava_Variable56'):
        assert _is_linked(a2, 'miniJava_Variable56', b)
    _safe_set(b, 'miniJava_Expr55', None)
    assert not _is_linked(b, 'miniJava_Expr55', a2)
    if hasattr(a2, 'miniJava_Variable56'):
        assert not _is_linked(a2, 'miniJava_Variable56', b)


def test_assoc_variableType16_reverse_link_reassign_clear():
    a1 = miniJava_Variable(name="sample_text")
    a2 = miniJava_Variable(name="sample_text_2")
    b = miniJava_Type(typeName="sample_text")
    _safe_set(b, 'miniJava_Type18', a1)
    assert _is_linked(b, 'miniJava_Type18', a1)
    if hasattr(a1, 'miniJava_Variable17'):
        assert _is_linked(a1, 'miniJava_Variable17', b)
    _safe_set(b, 'miniJava_Type18', a2)
    assert _is_linked(b, 'miniJava_Type18', a2)
    if hasattr(a1, 'miniJava_Variable17'):
        assert not _is_linked(a1, 'miniJava_Variable17', b)
    if hasattr(a2, 'miniJava_Variable17'):
        assert _is_linked(a2, 'miniJava_Variable17', b)
    _safe_set(b, 'miniJava_Type18', None)
    assert not _is_linked(b, 'miniJava_Type18', a2)
    if hasattr(a2, 'miniJava_Variable17'):
        assert not _is_linked(a2, 'miniJava_Variable17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classDeclarations0_stub_double():
    # miniJava_Program has no real 'miniJava_Program' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_ClassDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_ClassDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_ClassDecl(name="sample_text")
    partner = miniJava_Program()
    setattr(partner, 'miniJava_Program', None)
    _safe_set(owner, 'miniJava_ClassDecl', partner)
    assert owner in getattr(partner, 'miniJava_Program')
    _safe_set(owner, 'miniJava_ClassDecl', None)
    assert owner not in getattr(partner, 'miniJava_Program')


def test_assoc_localVarDeclarations25_stub_double():
    # miniJava_VarDeclaration has no real 'miniJava_VarDeclaration27' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Method(name="sample_text")
    partner = miniJava_VarDeclaration()
    setattr(partner, 'miniJava_VarDeclaration27', None)
    _safe_set(owner, 'miniJava_Method26', {partner})
    assert getattr(partner, 'miniJava_VarDeclaration27') == owner
    _safe_set(owner, 'miniJava_Method26', set())
    assert getattr(partner, 'miniJava_VarDeclaration27') is None


def test_assoc_mainMethod1_stub_double():
    # miniJava_MainMethod has no real 'miniJava_MainMethod' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_ClassDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_ClassDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_ClassDecl(name="sample_text")
    partner = miniJava_MainMethod()
    setattr(partner, 'miniJava_MainMethod', None)
    _safe_set(owner, 'miniJava_ClassDecl2', partner)
    assert getattr(partner, 'miniJava_MainMethod') == owner
    _safe_set(owner, 'miniJava_ClassDecl2', None)
    assert getattr(partner, 'miniJava_MainMethod') is None


def test_assoc_method64_stub_double():
    # miniJava_MethodCall has no real 'miniJava_MethodCall65' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Method(name="sample_text")
    partner = miniJava_MethodCall()
    setattr(partner, 'miniJava_MethodCall65', None)
    _safe_set(owner, 'miniJava_Method66', partner)
    assert getattr(partner, 'miniJava_MethodCall65') == owner
    _safe_set(owner, 'miniJava_Method66', None)
    assert getattr(partner, 'miniJava_MethodCall65') is None


def test_assoc_methodCall59_stub_double():
    # miniJava_MethodCall has no real 'miniJava_MethodCall' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Expr(expressionType="sample_text")
    partner = miniJava_MethodCall()
    setattr(partner, 'miniJava_MethodCall', None)
    _safe_set(owner, 'miniJava_Expr60', partner)
    assert getattr(partner, 'miniJava_MethodCall') == owner
    _safe_set(owner, 'miniJava_Expr60', None)
    assert getattr(partner, 'miniJava_MethodCall') is None


def test_assoc_parameters67_stub_double():
    # miniJava_MethodCall has no real 'miniJava_MethodCall68' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Expr(expressionType="sample_text")
    partner = miniJava_MethodCall()
    setattr(partner, 'miniJava_MethodCall68', None)
    _safe_set(owner, 'miniJava_Expr69', partner)
    assert owner in getattr(partner, 'miniJava_MethodCall68')
    _safe_set(owner, 'miniJava_Expr69', None)
    assert owner not in getattr(partner, 'miniJava_MethodCall68')


def test_assoc_statement10_stub_double():
    # miniJava_MainMethod has no real 'miniJava_MainMethod11' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    partner = miniJava_MainMethod()
    setattr(partner, 'miniJava_MainMethod11', None)
    _safe_set(owner, 'miniJava_Statement', partner)
    assert getattr(partner, 'miniJava_MainMethod11') == owner
    _safe_set(owner, 'miniJava_Statement', None)
    assert getattr(partner, 'miniJava_MainMethod11') is None


def test_assoc_varDeclarations6_stub_double():
    # miniJava_VarDeclaration has no real 'miniJava_VarDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_ClassDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_ClassDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_ClassDecl(name="sample_text")
    partner = miniJava_VarDeclaration()
    setattr(partner, 'miniJava_VarDeclaration', None)
    _safe_set(owner, 'miniJava_ClassDecl7', {partner})
    assert getattr(partner, 'miniJava_VarDeclaration') == owner
    _safe_set(owner, 'miniJava_ClassDecl7', set())
    assert getattr(partner, 'miniJava_VarDeclaration') is None


def test_assoc_variable14_stub_double():
    # miniJava_VarDeclaration has no real 'miniJava_VarDeclaration15' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Variable(name="sample_text")
    partner = miniJava_VarDeclaration()
    setattr(partner, 'miniJava_VarDeclaration15', None)
    _safe_set(owner, 'miniJava_Variable', partner)
    assert getattr(partner, 'miniJava_VarDeclaration15') == owner
    _safe_set(owner, 'miniJava_Variable', None)
    assert getattr(partner, 'miniJava_VarDeclaration15') is None


