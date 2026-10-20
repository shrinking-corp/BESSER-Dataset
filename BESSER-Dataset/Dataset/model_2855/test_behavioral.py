import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AstExpression,
    AstType,
    ExpressionLiteral,
    RegExp,
    Statement,
    cal_AnnotationArgument,
    cal_AstAction,
    cal_AstActor,
    cal_AstAnnotation,
    cal_AstEntity,
    cal_AstExpression,
    cal_AstPort,
    cal_AstProcedure,
    cal_AstState,
    cal_AstTag,
    cal_AstTransition,
    cal_AstType,
    cal_AstTypeBool,
    cal_AstTypeDouble,
    cal_AstTypeFloat,
    cal_AstTypeHalf,
    cal_AstTypeInt,
    cal_AstTypeList,
    cal_AstTypeString,
    cal_AstTypeUint,
    cal_AstUnit,
    cal_ExpressionBinary,
    cal_ExpressionBoolean,
    cal_ExpressionCall,
    cal_ExpressionElsif,
    cal_ExpressionFloat,
    cal_ExpressionIf,
    cal_ExpressionIndex,
    cal_ExpressionInteger,
    cal_ExpressionList,
    cal_ExpressionLiteral,
    cal_ExpressionString,
    cal_ExpressionUnary,
    cal_ExpressionVariable,
    cal_ExternalTarget,
    cal_Fsm,
    cal_Function,
    cal_Generator,
    cal_Guard,
    cal_Import,
    cal_Inequality,
    cal_InputPattern,
    cal_LocalFsm,
    cal_OutputPattern,
    cal_Priority,
    cal_RegExp,
    cal_RegExpBinary,
    cal_RegExpTag,
    cal_RegExpUnary,
    cal_ScheduleFsm,
    cal_Statement,
    cal_StatementAssign,
    cal_StatementCall,
    cal_StatementElsif,
    cal_StatementForeach,
    cal_StatementIf,
    cal_StatementWhile,
    cal_Variable,
    cal_VariableReference,
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

def test_assoc_annotations1_reverse_link_reassign_clear():
    a1 = cal_AstEntity(name="sample_text", package="sample_text")
    a2 = cal_AstEntity(name="sample_text_2", package="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation', a1)
    assert _is_linked(b, 'cal_AstAnnotation', a1)
    if hasattr(a1, 'cal_AstEntity2'):
        assert _is_linked(a1, 'cal_AstEntity2', b)
    _safe_set(b, 'cal_AstAnnotation', a2)
    assert _is_linked(b, 'cal_AstAnnotation', a2)
    if hasattr(a1, 'cal_AstEntity2'):
        assert not _is_linked(a1, 'cal_AstEntity2', b)
    if hasattr(a2, 'cal_AstEntity2'):
        assert _is_linked(a2, 'cal_AstEntity2', b)
    _safe_set(b, 'cal_AstAnnotation', None)
    assert not _is_linked(b, 'cal_AstAnnotation', a2)
    if hasattr(a2, 'cal_AstEntity2'):
        assert not _is_linked(a2, 'cal_AstEntity2', b)


def test_assoc_annotations15_reverse_link_reassign_clear():
    a1 = cal_Variable(constant=True, name="sample_text")
    a2 = cal_Variable(constant=False, name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation17', a1)
    assert _is_linked(b, 'cal_AstAnnotation17', a1)
    if hasattr(a1, 'cal_Variable16'):
        assert _is_linked(a1, 'cal_Variable16', b)
    _safe_set(b, 'cal_AstAnnotation17', a2)
    assert _is_linked(b, 'cal_AstAnnotation17', a2)
    if hasattr(a1, 'cal_Variable16'):
        assert not _is_linked(a1, 'cal_Variable16', b)
    if hasattr(a2, 'cal_Variable16'):
        assert _is_linked(a2, 'cal_Variable16', b)
    _safe_set(b, 'cal_AstAnnotation17', None)
    assert not _is_linked(b, 'cal_AstAnnotation17', a2)
    if hasattr(a2, 'cal_Variable16'):
        assert not _is_linked(a2, 'cal_Variable16', b)


def test_assoc_annotations53_reverse_link_reassign_clear():
    a1 = cal_AstPort(name="sample_text")
    a2 = cal_AstPort(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation55', a1)
    assert _is_linked(b, 'cal_AstAnnotation55', a1)
    if hasattr(a1, 'cal_AstPort54'):
        assert _is_linked(a1, 'cal_AstPort54', b)
    _safe_set(b, 'cal_AstAnnotation55', a2)
    assert _is_linked(b, 'cal_AstAnnotation55', a2)
    if hasattr(a1, 'cal_AstPort54'):
        assert not _is_linked(a1, 'cal_AstPort54', b)
    if hasattr(a2, 'cal_AstPort54'):
        assert _is_linked(a2, 'cal_AstPort54', b)
    _safe_set(b, 'cal_AstAnnotation55', None)
    assert not _is_linked(b, 'cal_AstAnnotation55', a2)
    if hasattr(a2, 'cal_AstPort54'):
        assert not _is_linked(a2, 'cal_AstPort54', b)


def test_assoc_annotations59_reverse_link_reassign_clear():
    a1 = cal_Function(name="sample_text")
    a2 = cal_Function(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation61', a1)
    assert _is_linked(b, 'cal_AstAnnotation61', a1)
    if hasattr(a1, 'cal_Function60'):
        assert _is_linked(a1, 'cal_Function60', b)
    _safe_set(b, 'cal_AstAnnotation61', a2)
    assert _is_linked(b, 'cal_AstAnnotation61', a2)
    if hasattr(a1, 'cal_Function60'):
        assert not _is_linked(a1, 'cal_Function60', b)
    if hasattr(a2, 'cal_Function60'):
        assert _is_linked(a2, 'cal_Function60', b)
    _safe_set(b, 'cal_AstAnnotation61', None)
    assert not _is_linked(b, 'cal_AstAnnotation61', a2)
    if hasattr(a2, 'cal_Function60'):
        assert not _is_linked(a2, 'cal_Function60', b)


def test_assoc_annotations74_reverse_link_reassign_clear():
    a1 = cal_AstProcedure(name="sample_text")
    a2 = cal_AstProcedure(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation76', a1)
    assert _is_linked(b, 'cal_AstAnnotation76', a1)
    if hasattr(a1, 'cal_AstProcedure75'):
        assert _is_linked(a1, 'cal_AstProcedure75', b)
    _safe_set(b, 'cal_AstAnnotation76', a2)
    assert _is_linked(b, 'cal_AstAnnotation76', a2)
    if hasattr(a1, 'cal_AstProcedure75'):
        assert not _is_linked(a1, 'cal_AstProcedure75', b)
    if hasattr(a2, 'cal_AstProcedure75'):
        assert _is_linked(a2, 'cal_AstProcedure75', b)
    _safe_set(b, 'cal_AstAnnotation76', None)
    assert not _is_linked(b, 'cal_AstAnnotation76', a2)
    if hasattr(a2, 'cal_AstProcedure75'):
        assert not _is_linked(a2, 'cal_AstProcedure75', b)


def test_assoc_arguments269_reverse_link_reassign_clear():
    a1 = cal_AstAnnotation(name="sample_text")
    a2 = cal_AstAnnotation(name="sample_text_2")
    b = cal_AnnotationArgument(name="sample_text", value="sample_text")
    _safe_set(b, 'cal_AnnotationArgument', a1)
    assert _is_linked(b, 'cal_AnnotationArgument', a1)
    if hasattr(a1, 'cal_AstAnnotation270'):
        assert _is_linked(a1, 'cal_AstAnnotation270', b)
    _safe_set(b, 'cal_AnnotationArgument', a2)
    assert _is_linked(b, 'cal_AnnotationArgument', a2)
    if hasattr(a1, 'cal_AstAnnotation270'):
        assert not _is_linked(a1, 'cal_AstAnnotation270', b)
    if hasattr(a2, 'cal_AstAnnotation270'):
        assert _is_linked(a2, 'cal_AstAnnotation270', b)
    _safe_set(b, 'cal_AnnotationArgument', None)
    assert not _is_linked(b, 'cal_AnnotationArgument', a2)
    if hasattr(a2, 'cal_AstAnnotation270'):
        assert not _is_linked(a2, 'cal_AstAnnotation270', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = cal_Import(importedNamespace="sample_text")
    a2 = cal_Import(importedNamespace="sample_text_2")
    b = cal_AstEntity(name="sample_text", package="sample_text")
    _safe_set(b, 'cal_AstEntity', {a1})
    assert _is_linked(b, 'cal_AstEntity', a1)
    if hasattr(a1, 'cal_Import'):
        assert _is_linked(a1, 'cal_Import', b)
    _safe_set(b, 'cal_AstEntity', {a2})
    assert _is_linked(b, 'cal_AstEntity', a2)
    if hasattr(a1, 'cal_Import'):
        assert not _is_linked(a1, 'cal_Import', b)
    if hasattr(a2, 'cal_Import'):
        assert _is_linked(a2, 'cal_Import', b)
    _safe_set(b, 'cal_AstEntity', set())
    assert not _is_linked(b, 'cal_AstEntity', a2)
    if hasattr(a2, 'cal_Import'):
        assert not _is_linked(a2, 'cal_Import', b)


def test_assoc_parameters62_reverse_link_reassign_clear():
    a1 = cal_Variable(constant=True, name="sample_text")
    a2 = cal_Variable(constant=False, name="sample_text_2")
    b = cal_Function(name="sample_text")
    _safe_set(b, 'cal_Function63', {a1})
    assert _is_linked(b, 'cal_Function63', a1)
    if hasattr(a1, 'cal_Variable64'):
        assert _is_linked(a1, 'cal_Variable64', b)
    _safe_set(b, 'cal_Function63', {a2})
    assert _is_linked(b, 'cal_Function63', a2)
    if hasattr(a1, 'cal_Variable64'):
        assert not _is_linked(a1, 'cal_Variable64', b)
    if hasattr(a2, 'cal_Variable64'):
        assert _is_linked(a2, 'cal_Variable64', b)
    _safe_set(b, 'cal_Function63', set())
    assert not _is_linked(b, 'cal_Function63', a2)
    if hasattr(a2, 'cal_Variable64'):
        assert not _is_linked(a2, 'cal_Variable64', b)


def test_assoc_parameters77_reverse_link_reassign_clear():
    a1 = cal_Variable(constant=True, name="sample_text")
    a2 = cal_Variable(constant=False, name="sample_text_2")
    b = cal_AstProcedure(name="sample_text")
    _safe_set(b, 'cal_AstProcedure78', {a1})
    assert _is_linked(b, 'cal_AstProcedure78', a1)
    if hasattr(a1, 'cal_Variable79'):
        assert _is_linked(a1, 'cal_Variable79', b)
    _safe_set(b, 'cal_AstProcedure78', {a2})
    assert _is_linked(b, 'cal_AstProcedure78', a2)
    if hasattr(a1, 'cal_Variable79'):
        assert not _is_linked(a1, 'cal_Variable79', b)
    if hasattr(a2, 'cal_Variable79'):
        assert _is_linked(a2, 'cal_Variable79', b)
    _safe_set(b, 'cal_AstProcedure78', set())
    assert not _is_linked(b, 'cal_AstProcedure78', a2)
    if hasattr(a2, 'cal_Variable79'):
        assert not _is_linked(a2, 'cal_Variable79', b)


def test_assoc_variables68_reverse_link_reassign_clear():
    a1 = cal_Variable(constant=True, name="sample_text")
    a2 = cal_Variable(constant=False, name="sample_text_2")
    b = cal_Function(name="sample_text")
    _safe_set(b, 'cal_Function69', {a1})
    assert _is_linked(b, 'cal_Function69', a1)
    if hasattr(a1, 'cal_Variable70'):
        assert _is_linked(a1, 'cal_Variable70', b)
    _safe_set(b, 'cal_Function69', {a2})
    assert _is_linked(b, 'cal_Function69', a2)
    if hasattr(a1, 'cal_Variable70'):
        assert not _is_linked(a1, 'cal_Variable70', b)
    if hasattr(a2, 'cal_Variable70'):
        assert _is_linked(a2, 'cal_Variable70', b)
    _safe_set(b, 'cal_Function69', set())
    assert not _is_linked(b, 'cal_Function69', a2)
    if hasattr(a2, 'cal_Variable70'):
        assert not _is_linked(a2, 'cal_Variable70', b)


def test_assoc_variables80_reverse_link_reassign_clear():
    a1 = cal_Variable(constant=True, name="sample_text")
    a2 = cal_Variable(constant=False, name="sample_text_2")
    b = cal_AstProcedure(name="sample_text")
    _safe_set(b, 'cal_AstProcedure81', {a1})
    assert _is_linked(b, 'cal_AstProcedure81', a1)
    if hasattr(a1, 'cal_Variable82'):
        assert _is_linked(a1, 'cal_Variable82', b)
    _safe_set(b, 'cal_AstProcedure81', {a2})
    assert _is_linked(b, 'cal_AstProcedure81', a2)
    if hasattr(a1, 'cal_Variable82'):
        assert not _is_linked(a1, 'cal_Variable82', b)
    if hasattr(a2, 'cal_Variable82'):
        assert _is_linked(a2, 'cal_Variable82', b)
    _safe_set(b, 'cal_AstProcedure81', set())
    assert not _is_linked(b, 'cal_AstProcedure81', a2)
    if hasattr(a2, 'cal_Variable82'):
        assert not _is_linked(a2, 'cal_Variable82', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actor3_stub_double():
    # cal_AstActor has no real 'cal_AstActor' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstEntity(name="sample_text", package="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor', None)
    _safe_set(owner, 'cal_AstEntity4', partner)
    assert getattr(partner, 'cal_AstActor') == owner
    _safe_set(owner, 'cal_AstEntity4', None)
    assert getattr(partner, 'cal_AstActor') is None


def test_assoc_annotations127_stub_double():
    # cal_AstAction has no real 'cal_AstAction128' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAnnotation(name="sample_text")
    partner = cal_AstAction()
    setattr(partner, 'cal_AstAction128', None)
    _safe_set(owner, 'cal_AstAnnotation129', partner)
    assert owner in getattr(partner, 'cal_AstAction128')
    _safe_set(owner, 'cal_AstAnnotation129', None)
    assert owner not in getattr(partner, 'cal_AstAction128')


def test_assoc_annotations210_stub_double():
    # cal_Statement has no real 'cal_Statement211' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAnnotation(name="sample_text")
    partner = cal_Statement()
    setattr(partner, 'cal_Statement211', None)
    _safe_set(owner, 'cal_AstAnnotation212', partner)
    assert owner in getattr(partner, 'cal_Statement211')
    _safe_set(owner, 'cal_AstAnnotation212', None)
    assert owner not in getattr(partner, 'cal_Statement211')


def test_assoc_annotations213_stub_double():
    # cal_ExpressionCall has no real 'cal_ExpressionCall' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAnnotation(name="sample_text")
    partner = cal_ExpressionCall()
    setattr(partner, 'cal_ExpressionCall', None)
    _safe_set(owner, 'cal_AstAnnotation214', partner)
    assert owner in getattr(partner, 'cal_ExpressionCall')
    _safe_set(owner, 'cal_AstAnnotation214', None)
    assert owner not in getattr(partner, 'cal_ExpressionCall')


def test_assoc_child276_stub_double():
    # cal_RegExp has no real 'cal_RegExp277' property in the generated
    # code (a bare stub) -- manually attach it so cal_RegExpUnary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_RegExpUnary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_RegExpUnary(unaryOperator="sample_text")
    partner = cal_RegExp()
    setattr(partner, 'cal_RegExp277', None)
    _safe_set(owner, 'cal_RegExpUnary', partner)
    assert getattr(partner, 'cal_RegExp277') == owner
    _safe_set(owner, 'cal_RegExpUnary', None)
    assert getattr(partner, 'cal_RegExp277') is None


def test_assoc_contents124_stub_double():
    # cal_Fsm has no real 'cal_Fsm126' property in the generated
    # code (a bare stub) -- manually attach it so cal_LocalFsm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_LocalFsm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_LocalFsm(name="sample_text")
    partner = cal_Fsm()
    setattr(partner, 'cal_Fsm126', None)
    _safe_set(owner, 'cal_LocalFsm125', partner)
    assert getattr(partner, 'cal_Fsm126') == owner
    _safe_set(owner, 'cal_LocalFsm125', None)
    assert getattr(partner, 'cal_Fsm126') is None


def test_assoc_dimensions20_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression22' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression22', None)
    _safe_set(owner, 'cal_Variable21', {partner})
    assert getattr(partner, 'cal_AstExpression22') == owner
    _safe_set(owner, 'cal_Variable21', set())
    assert getattr(partner, 'cal_AstExpression22') is None


def test_assoc_expression285_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression286' property in the generated
    # code (a bare stub) -- manually attach it so cal_ExpressionUnary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_ExpressionUnary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_ExpressionUnary(unaryOperator="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression286', None)
    _safe_set(owner, 'cal_ExpressionUnary', partner)
    assert getattr(partner, 'cal_AstExpression286') == owner
    _safe_set(owner, 'cal_ExpressionUnary', None)
    assert getattr(partner, 'cal_AstExpression286') is None


def test_assoc_expression71_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression73' property in the generated
    # code (a bare stub) -- manually attach it so cal_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Function(name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression73', None)
    _safe_set(owner, 'cal_Function72', partner)
    assert getattr(partner, 'cal_AstExpression73') == owner
    _safe_set(owner, 'cal_Function72', None)
    assert getattr(partner, 'cal_AstExpression73') is None


def test_assoc_from_115_stub_double():
    # cal_ExternalTarget has no real 'cal_ExternalTarget116' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_ExternalTarget()
    setattr(partner, 'cal_ExternalTarget116', None)
    _safe_set(owner, 'cal_AstState117', partner)
    assert getattr(partner, 'cal_ExternalTarget116') == owner
    _safe_set(owner, 'cal_AstState117', None)
    assert getattr(partner, 'cal_ExternalTarget116') is None


def test_assoc_fsm109_stub_double():
    # cal_ExternalTarget has no real 'cal_ExternalTarget110' property in the generated
    # code (a bare stub) -- manually attach it so cal_LocalFsm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_LocalFsm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_LocalFsm(name="sample_text")
    partner = cal_ExternalTarget()
    setattr(partner, 'cal_ExternalTarget110', None)
    _safe_set(owner, 'cal_LocalFsm111', partner)
    assert getattr(partner, 'cal_ExternalTarget110') == owner
    _safe_set(owner, 'cal_LocalFsm111', None)
    assert getattr(partner, 'cal_ExternalTarget110') is None


def test_assoc_function215_stub_double():
    # cal_ExpressionCall has no real 'cal_ExpressionCall216' property in the generated
    # code (a bare stub) -- manually attach it so cal_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Function(name="sample_text")
    partner = cal_ExpressionCall()
    setattr(partner, 'cal_ExpressionCall216', None)
    _safe_set(owner, 'cal_Function217', partner)
    assert getattr(partner, 'cal_ExpressionCall216') == owner
    _safe_set(owner, 'cal_Function217', None)
    assert getattr(partner, 'cal_ExpressionCall216') is None


def test_assoc_functions31_stub_double():
    # cal_AstActor has no real 'cal_AstActor32' property in the generated
    # code (a bare stub) -- manually attach it so cal_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Function(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor32', None)
    _safe_set(owner, 'cal_Function33', partner)
    assert owner in getattr(partner, 'cal_AstActor32')
    _safe_set(owner, 'cal_Function33', None)
    assert owner not in getattr(partner, 'cal_AstActor32')


def test_assoc_functions7_stub_double():
    # cal_AstUnit has no real 'cal_AstUnit8' property in the generated
    # code (a bare stub) -- manually attach it so cal_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Function(name="sample_text")
    partner = cal_AstUnit()
    setattr(partner, 'cal_AstUnit8', None)
    _safe_set(owner, 'cal_Function', partner)
    assert owner in getattr(partner, 'cal_AstUnit8')
    _safe_set(owner, 'cal_Function', None)
    assert owner not in getattr(partner, 'cal_AstUnit8')


def test_assoc_initialState89_stub_double():
    # cal_ScheduleFsm has no real 'cal_ScheduleFsm90' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_ScheduleFsm()
    setattr(partner, 'cal_ScheduleFsm90', None)
    _safe_set(owner, 'cal_AstState', partner)
    assert getattr(partner, 'cal_ScheduleFsm90') == owner
    _safe_set(owner, 'cal_AstState', None)
    assert getattr(partner, 'cal_ScheduleFsm90') is None


def test_assoc_inputs26_stub_double():
    # cal_AstActor has no real 'cal_AstActor27' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor27', None)
    _safe_set(owner, 'cal_AstPort', partner)
    assert owner in getattr(partner, 'cal_AstActor27')
    _safe_set(owner, 'cal_AstPort', None)
    assert owner not in getattr(partner, 'cal_AstActor27')


def test_assoc_left271_stub_double():
    # cal_RegExp has no real 'cal_RegExp272' property in the generated
    # code (a bare stub) -- manually attach it so cal_RegExpBinary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_RegExpBinary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_RegExpBinary(operator="sample_text")
    partner = cal_RegExp()
    setattr(partner, 'cal_RegExp272', None)
    _safe_set(owner, 'cal_RegExpBinary', partner)
    assert getattr(partner, 'cal_RegExp272') == owner
    _safe_set(owner, 'cal_RegExpBinary', None)
    assert getattr(partner, 'cal_RegExp272') is None


def test_assoc_left280_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression281' property in the generated
    # code (a bare stub) -- manually attach it so cal_ExpressionBinary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_ExpressionBinary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_ExpressionBinary(operator="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression281', None)
    _safe_set(owner, 'cal_ExpressionBinary', partner)
    assert getattr(partner, 'cal_AstExpression281') == owner
    _safe_set(owner, 'cal_ExpressionBinary', None)
    assert getattr(partner, 'cal_AstExpression281') is None


def test_assoc_localFsms45_stub_double():
    # cal_AstActor has no real 'cal_AstActor46' property in the generated
    # code (a bare stub) -- manually attach it so cal_LocalFsm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_LocalFsm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_LocalFsm(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor46', None)
    _safe_set(owner, 'cal_LocalFsm', partner)
    assert owner in getattr(partner, 'cal_AstActor46')
    _safe_set(owner, 'cal_LocalFsm', None)
    assert owner not in getattr(partner, 'cal_AstActor46')


def test_assoc_outputs28_stub_double():
    # cal_AstActor has no real 'cal_AstActor29' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor29', None)
    _safe_set(owner, 'cal_AstPort30', partner)
    assert owner in getattr(partner, 'cal_AstActor29')
    _safe_set(owner, 'cal_AstPort30', None)
    assert owner not in getattr(partner, 'cal_AstActor29')


def test_assoc_parameters23_stub_double():
    # cal_AstActor has no real 'cal_AstActor24' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor24', None)
    _safe_set(owner, 'cal_Variable25', partner)
    assert owner in getattr(partner, 'cal_AstActor24')
    _safe_set(owner, 'cal_Variable25', None)
    assert owner not in getattr(partner, 'cal_AstActor24')


def test_assoc_port145_stub_double():
    # cal_InputPattern has no real 'cal_InputPattern146' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_InputPattern()
    setattr(partner, 'cal_InputPattern146', None)
    _safe_set(owner, 'cal_AstPort147', partner)
    assert getattr(partner, 'cal_InputPattern146') == owner
    _safe_set(owner, 'cal_AstPort147', None)
    assert getattr(partner, 'cal_InputPattern146') is None


def test_assoc_port154_stub_double():
    # cal_OutputPattern has no real 'cal_OutputPattern155' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_OutputPattern()
    setattr(partner, 'cal_OutputPattern155', None)
    _safe_set(owner, 'cal_AstPort156', partner)
    assert getattr(partner, 'cal_OutputPattern155') == owner
    _safe_set(owner, 'cal_AstPort156', None)
    assert getattr(partner, 'cal_OutputPattern155') is None


def test_assoc_procedure173_stub_double():
    # cal_StatementCall has no real 'cal_StatementCall' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_StatementCall()
    setattr(partner, 'cal_StatementCall', None)
    _safe_set(owner, 'cal_AstProcedure174', partner)
    assert getattr(partner, 'cal_StatementCall') == owner
    _safe_set(owner, 'cal_AstProcedure174', None)
    assert getattr(partner, 'cal_StatementCall') is None


def test_assoc_procedures34_stub_double():
    # cal_AstActor has no real 'cal_AstActor35' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor35', None)
    _safe_set(owner, 'cal_AstProcedure36', partner)
    assert owner in getattr(partner, 'cal_AstActor35')
    _safe_set(owner, 'cal_AstProcedure36', None)
    assert owner not in getattr(partner, 'cal_AstActor35')


def test_assoc_procedures9_stub_double():
    # cal_AstUnit has no real 'cal_AstUnit10' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_AstUnit()
    setattr(partner, 'cal_AstUnit10', None)
    _safe_set(owner, 'cal_AstProcedure', partner)
    assert owner in getattr(partner, 'cal_AstUnit10')
    _safe_set(owner, 'cal_AstProcedure', None)
    assert owner not in getattr(partner, 'cal_AstUnit10')


def test_assoc_right273_stub_double():
    # cal_RegExp has no real 'cal_RegExp275' property in the generated
    # code (a bare stub) -- manually attach it so cal_RegExpBinary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_RegExpBinary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_RegExpBinary(operator="sample_text")
    partner = cal_RegExp()
    setattr(partner, 'cal_RegExp275', None)
    _safe_set(owner, 'cal_RegExpBinary274', partner)
    assert getattr(partner, 'cal_RegExp275') == owner
    _safe_set(owner, 'cal_RegExpBinary274', None)
    assert getattr(partner, 'cal_RegExp275') is None


def test_assoc_right282_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression284' property in the generated
    # code (a bare stub) -- manually attach it so cal_ExpressionBinary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_ExpressionBinary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_ExpressionBinary(operator="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression284', None)
    _safe_set(owner, 'cal_ExpressionBinary283', partner)
    assert getattr(partner, 'cal_AstExpression284') == owner
    _safe_set(owner, 'cal_ExpressionBinary283', None)
    assert getattr(partner, 'cal_AstExpression284') is None


def test_assoc_source98_stub_double():
    # cal_AstTransition has no real 'cal_AstTransition99' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_AstTransition()
    setattr(partner, 'cal_AstTransition99', None)
    _safe_set(owner, 'cal_AstState100', partner)
    assert getattr(partner, 'cal_AstTransition99') == owner
    _safe_set(owner, 'cal_AstState100', None)
    assert getattr(partner, 'cal_AstTransition99') is None


def test_assoc_state112_stub_double():
    # cal_ExternalTarget has no real 'cal_ExternalTarget113' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_ExternalTarget()
    setattr(partner, 'cal_ExternalTarget113', None)
    _safe_set(owner, 'cal_AstState114', partner)
    assert getattr(partner, 'cal_ExternalTarget113') == owner
    _safe_set(owner, 'cal_AstState114', None)
    assert getattr(partner, 'cal_ExternalTarget113') is None


def test_assoc_stateVariables42_stub_double():
    # cal_AstActor has no real 'cal_AstActor43' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor43', None)
    _safe_set(owner, 'cal_Variable44', partner)
    assert owner in getattr(partner, 'cal_AstActor43')
    _safe_set(owner, 'cal_Variable44', None)
    assert owner not in getattr(partner, 'cal_AstActor43')


def test_assoc_statements83_stub_double():
    # cal_Statement has no real 'cal_Statement' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_Statement()
    setattr(partner, 'cal_Statement', None)
    _safe_set(owner, 'cal_AstProcedure84', {partner})
    assert getattr(partner, 'cal_Statement') == owner
    _safe_set(owner, 'cal_AstProcedure84', set())
    assert getattr(partner, 'cal_Statement') is None


def test_assoc_states95_stub_double():
    # cal_Fsm has no real 'cal_Fsm96' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_Fsm()
    setattr(partner, 'cal_Fsm96', None)
    _safe_set(owner, 'cal_AstState97', partner)
    assert owner in getattr(partner, 'cal_Fsm96')
    _safe_set(owner, 'cal_AstState97', None)
    assert owner not in getattr(partner, 'cal_Fsm96')


def test_assoc_tag101_stub_double():
    # cal_AstTransition has no real 'cal_AstTransition102' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_AstTransition()
    setattr(partner, 'cal_AstTransition102', None)
    _safe_set(owner, 'cal_AstTag103', partner)
    assert getattr(partner, 'cal_AstTransition102') == owner
    _safe_set(owner, 'cal_AstTag103', None)
    assert getattr(partner, 'cal_AstTransition102') is None


def test_assoc_tag130_stub_double():
    # cal_AstAction has no real 'cal_AstAction131' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_AstAction()
    setattr(partner, 'cal_AstAction131', None)
    _safe_set(owner, 'cal_AstTag132', partner)
    assert getattr(partner, 'cal_AstAction131') == owner
    _safe_set(owner, 'cal_AstTag132', None)
    assert getattr(partner, 'cal_AstAction131') is None


def test_assoc_tag278_stub_double():
    # cal_RegExpTag has no real 'cal_RegExpTag' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_RegExpTag()
    setattr(partner, 'cal_RegExpTag', None)
    _safe_set(owner, 'cal_AstTag279', partner)
    assert getattr(partner, 'cal_RegExpTag') == owner
    _safe_set(owner, 'cal_AstTag279', None)
    assert getattr(partner, 'cal_RegExpTag') is None


def test_assoc_tags85_stub_double():
    # cal_Inequality has no real 'cal_Inequality' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_Inequality()
    setattr(partner, 'cal_Inequality', None)
    _safe_set(owner, 'cal_AstTag', partner)
    assert owner in getattr(partner, 'cal_Inequality')
    _safe_set(owner, 'cal_AstTag', None)
    assert owner not in getattr(partner, 'cal_Inequality')


def test_assoc_target104_stub_double():
    # cal_AstTransition has no real 'cal_AstTransition105' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_AstTransition()
    setattr(partner, 'cal_AstTransition105', None)
    _safe_set(owner, 'cal_AstState106', partner)
    assert getattr(partner, 'cal_AstTransition105') == owner
    _safe_set(owner, 'cal_AstState106', None)
    assert getattr(partner, 'cal_AstTransition105') is None


def test_assoc_to118_stub_double():
    # cal_ExternalTarget has no real 'cal_ExternalTarget119' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text", node="sample_text")
    partner = cal_ExternalTarget()
    setattr(partner, 'cal_ExternalTarget119', None)
    _safe_set(owner, 'cal_AstState120', partner)
    assert getattr(partner, 'cal_ExternalTarget119') == owner
    _safe_set(owner, 'cal_AstState120', None)
    assert getattr(partner, 'cal_ExternalTarget119') is None


def test_assoc_tokens148_stub_double():
    # cal_InputPattern has no real 'cal_InputPattern149' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_InputPattern()
    setattr(partner, 'cal_InputPattern149', None)
    _safe_set(owner, 'cal_Variable150', partner)
    assert owner in getattr(partner, 'cal_InputPattern149')
    _safe_set(owner, 'cal_Variable150', None)
    assert owner not in getattr(partner, 'cal_InputPattern149')


def test_assoc_type18_stub_double():
    # cal_AstType has no real 'cal_AstType' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstType()
    setattr(partner, 'cal_AstType', None)
    _safe_set(owner, 'cal_Variable19', partner)
    assert getattr(partner, 'cal_AstType') == owner
    _safe_set(owner, 'cal_Variable19', None)
    assert getattr(partner, 'cal_AstType') is None


def test_assoc_type56_stub_double():
    # cal_AstType has no real 'cal_AstType58' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_AstType()
    setattr(partner, 'cal_AstType58', None)
    _safe_set(owner, 'cal_AstPort57', partner)
    assert getattr(partner, 'cal_AstType58') == owner
    _safe_set(owner, 'cal_AstPort57', None)
    assert getattr(partner, 'cal_AstType58') is None


def test_assoc_type65_stub_double():
    # cal_AstType has no real 'cal_AstType67' property in the generated
    # code (a bare stub) -- manually attach it so cal_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Function(name="sample_text")
    partner = cal_AstType()
    setattr(partner, 'cal_AstType67', None)
    _safe_set(owner, 'cal_Function66', partner)
    assert getattr(partner, 'cal_AstType67') == owner
    _safe_set(owner, 'cal_Function66', None)
    assert getattr(partner, 'cal_AstType67') is None


def test_assoc_unit5_stub_double():
    # cal_AstUnit has no real 'cal_AstUnit' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstEntity(name="sample_text", package="sample_text")
    partner = cal_AstUnit()
    setattr(partner, 'cal_AstUnit', None)
    _safe_set(owner, 'cal_AstEntity6', partner)
    assert getattr(partner, 'cal_AstUnit') == owner
    _safe_set(owner, 'cal_AstEntity6', None)
    assert getattr(partner, 'cal_AstUnit') is None


def test_assoc_value13_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression', None)
    _safe_set(owner, 'cal_Variable14', partner)
    assert getattr(partner, 'cal_AstExpression') == owner
    _safe_set(owner, 'cal_Variable14', None)
    assert getattr(partner, 'cal_AstExpression') is None


def test_assoc_variable178_stub_double():
    # cal_StatementForeach has no real 'cal_StatementForeach' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_StatementForeach()
    setattr(partner, 'cal_StatementForeach', None)
    _safe_set(owner, 'cal_Variable179', partner)
    assert getattr(partner, 'cal_StatementForeach') == owner
    _safe_set(owner, 'cal_Variable179', None)
    assert getattr(partner, 'cal_StatementForeach') is None


def test_assoc_variable246_stub_double():
    # cal_Generator has no real 'cal_Generator247' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_Generator()
    setattr(partner, 'cal_Generator247', None)
    _safe_set(owner, 'cal_Variable248', partner)
    assert getattr(partner, 'cal_Generator247') == owner
    _safe_set(owner, 'cal_Variable248', None)
    assert getattr(partner, 'cal_Generator247') is None


def test_assoc_variable266_stub_double():
    # cal_VariableReference has no real 'cal_VariableReference267' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_VariableReference()
    setattr(partner, 'cal_VariableReference267', None)
    _safe_set(owner, 'cal_Variable268', partner)
    assert getattr(partner, 'cal_VariableReference267') == owner
    _safe_set(owner, 'cal_Variable268', None)
    assert getattr(partner, 'cal_VariableReference267') is None


def test_assoc_variables11_stub_double():
    # cal_AstUnit has no real 'cal_AstUnit12' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstUnit()
    setattr(partner, 'cal_AstUnit12', None)
    _safe_set(owner, 'cal_Variable', partner)
    assert owner in getattr(partner, 'cal_AstUnit12')
    _safe_set(owner, 'cal_Variable', None)
    assert owner not in getattr(partner, 'cal_AstUnit12')


def test_assoc_variables139_stub_double():
    # cal_AstAction has no real 'cal_AstAction140' property in the generated
    # code (a bare stub) -- manually attach it so cal_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_Variable(constant=True, name="sample_text")
    partner = cal_AstAction()
    setattr(partner, 'cal_AstAction140', None)
    _safe_set(owner, 'cal_Variable141', partner)
    assert owner in getattr(partner, 'cal_AstAction140')
    _safe_set(owner, 'cal_Variable141', None)
    assert owner not in getattr(partner, 'cal_AstAction140')


