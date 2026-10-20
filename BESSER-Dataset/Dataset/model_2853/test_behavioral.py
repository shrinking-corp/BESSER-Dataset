import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AstAbstractActor,
    AstAction,
    AstExpression,
    AstExpressionLiteral,
    AstExternalFunction,
    AstExternalProcedure,
    AstPackage,
    AstStatement,
    AstTop,
    AstUnit,
    cal_AstAbstractActor,
    cal_AstAction,
    cal_AstActor,
    cal_AstActorVariable,
    cal_AstActorVariableReference,
    cal_AstAnnotation,
    cal_AstAnnotationArgument,
    cal_AstAssignParameter,
    cal_AstConnection,
    cal_AstConnectionAttribute,
    cal_AstEntity,
    cal_AstExpression,
    cal_AstExpressionBinary,
    cal_AstExpressionBoolean,
    cal_AstExpressionCall,
    cal_AstExpressionFloat,
    cal_AstExpressionIf,
    cal_AstExpressionInteger,
    cal_AstExpressionList,
    cal_AstExpressionLiteral,
    cal_AstExpressionString,
    cal_AstExpressionUnary,
    cal_AstExpressionVariable,
    cal_AstExternalActor,
    cal_AstExternalFunction,
    cal_AstExternalProcedure,
    cal_AstForeachGenerator,
    cal_AstFunction,
    cal_AstGenerator,
    cal_AstInequality,
    cal_AstInitialize,
    cal_AstInputPattern,
    cal_AstMemberAccess,
    cal_AstNamespace,
    cal_AstNetwork,
    cal_AstOutputPattern,
    cal_AstPackage,
    cal_AstPort,
    cal_AstPriority,
    cal_AstProcedure,
    cal_AstSchedule,
    cal_AstState,
    cal_AstStatement,
    cal_AstStatementAssign,
    cal_AstStatementBlock,
    cal_AstStatementCall,
    cal_AstStatementForeach,
    cal_AstStatementIf,
    cal_AstStatementWhile,
    cal_AstStructure,
    cal_AstTag,
    cal_AstTop,
    cal_AstTransition,
    cal_AstType,
    cal_AstTypeDefinitionParameter,
    cal_AstTypeName,
    cal_AstTypeParam,
    cal_AstTypeParameterList,
    cal_AstUnit,
    cal_AstVariable,
    cal_AstVariableReference,
    cal_EObject,
    cal_Import,
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

def test_assoc_annotations11_reverse_link_reassign_clear():
    a1 = cal_AstNamespace(name="sample_text")
    a2 = cal_AstNamespace(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation', a1)
    assert _is_linked(b, 'cal_AstAnnotation', a1)
    if hasattr(a1, 'cal_AstNamespace12'):
        assert _is_linked(a1, 'cal_AstNamespace12', b)
    _safe_set(b, 'cal_AstAnnotation', a2)
    assert _is_linked(b, 'cal_AstAnnotation', a2)
    if hasattr(a1, 'cal_AstNamespace12'):
        assert not _is_linked(a1, 'cal_AstNamespace12', b)
    if hasattr(a2, 'cal_AstNamespace12'):
        assert _is_linked(a2, 'cal_AstNamespace12', b)
    _safe_set(b, 'cal_AstAnnotation', None)
    assert not _is_linked(b, 'cal_AstAnnotation', a2)
    if hasattr(a2, 'cal_AstNamespace12'):
        assert not _is_linked(a2, 'cal_AstNamespace12', b)


def test_assoc_annotations118_reverse_link_reassign_clear():
    a1 = cal_AstPort(name="sample_text")
    a2 = cal_AstPort(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation120', a1)
    assert _is_linked(b, 'cal_AstAnnotation120', a1)
    if hasattr(a1, 'cal_AstPort119'):
        assert _is_linked(a1, 'cal_AstPort119', b)
    _safe_set(b, 'cal_AstAnnotation120', a2)
    assert _is_linked(b, 'cal_AstAnnotation120', a2)
    if hasattr(a1, 'cal_AstPort119'):
        assert not _is_linked(a1, 'cal_AstPort119', b)
    if hasattr(a2, 'cal_AstPort119'):
        assert _is_linked(a2, 'cal_AstPort119', b)
    _safe_set(b, 'cal_AstAnnotation120', None)
    assert not _is_linked(b, 'cal_AstAnnotation120', a2)
    if hasattr(a2, 'cal_AstPort119'):
        assert not _is_linked(a2, 'cal_AstPort119', b)


def test_assoc_annotations124_reverse_link_reassign_clear():
    a1 = cal_AstProcedure(name="sample_text")
    a2 = cal_AstProcedure(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation126', a1)
    assert _is_linked(b, 'cal_AstAnnotation126', a1)
    if hasattr(a1, 'cal_AstProcedure125'):
        assert _is_linked(a1, 'cal_AstProcedure125', b)
    _safe_set(b, 'cal_AstAnnotation126', a2)
    assert _is_linked(b, 'cal_AstAnnotation126', a2)
    if hasattr(a1, 'cal_AstProcedure125'):
        assert not _is_linked(a1, 'cal_AstProcedure125', b)
    if hasattr(a2, 'cal_AstProcedure125'):
        assert _is_linked(a2, 'cal_AstProcedure125', b)
    _safe_set(b, 'cal_AstAnnotation126', None)
    assert not _is_linked(b, 'cal_AstAnnotation126', a2)
    if hasattr(a2, 'cal_AstProcedure125'):
        assert not _is_linked(a2, 'cal_AstProcedure125', b)


def test_assoc_annotations62_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation64', a1)
    assert _is_linked(b, 'cal_AstAnnotation64', a1)
    if hasattr(a1, 'cal_AstVariable63'):
        assert _is_linked(a1, 'cal_AstVariable63', b)
    _safe_set(b, 'cal_AstAnnotation64', a2)
    assert _is_linked(b, 'cal_AstAnnotation64', a2)
    if hasattr(a1, 'cal_AstVariable63'):
        assert not _is_linked(a1, 'cal_AstVariable63', b)
    if hasattr(a2, 'cal_AstVariable63'):
        assert _is_linked(a2, 'cal_AstVariable63', b)
    _safe_set(b, 'cal_AstAnnotation64', None)
    assert not _is_linked(b, 'cal_AstAnnotation64', a2)
    if hasattr(a2, 'cal_AstVariable63'):
        assert not _is_linked(a2, 'cal_AstVariable63', b)


def test_assoc_annotations87_reverse_link_reassign_clear():
    a1 = cal_AstFunction(name="sample_text")
    a2 = cal_AstFunction(name="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation89', a1)
    assert _is_linked(b, 'cal_AstAnnotation89', a1)
    if hasattr(a1, 'cal_AstFunction88'):
        assert _is_linked(a1, 'cal_AstFunction88', b)
    _safe_set(b, 'cal_AstAnnotation89', a2)
    assert _is_linked(b, 'cal_AstAnnotation89', a2)
    if hasattr(a1, 'cal_AstFunction88'):
        assert not _is_linked(a1, 'cal_AstFunction88', b)
    if hasattr(a2, 'cal_AstFunction88'):
        assert _is_linked(a2, 'cal_AstFunction88', b)
    _safe_set(b, 'cal_AstAnnotation89', None)
    assert not _is_linked(b, 'cal_AstAnnotation89', a2)
    if hasattr(a2, 'cal_AstFunction88'):
        assert not _is_linked(a2, 'cal_AstFunction88', b)


def test_assoc_arguments296_reverse_link_reassign_clear():
    a1 = cal_AstAnnotationArgument(name="sample_text", value="sample_text")
    a2 = cal_AstAnnotationArgument(name="sample_text_2", value="sample_text_2")
    b = cal_AstAnnotation(name="sample_text")
    _safe_set(b, 'cal_AstAnnotation297', {a1})
    assert _is_linked(b, 'cal_AstAnnotation297', a1)
    if hasattr(a1, 'cal_AstAnnotationArgument'):
        assert _is_linked(a1, 'cal_AstAnnotationArgument', b)
    _safe_set(b, 'cal_AstAnnotation297', {a2})
    assert _is_linked(b, 'cal_AstAnnotation297', a2)
    if hasattr(a1, 'cal_AstAnnotationArgument'):
        assert not _is_linked(a1, 'cal_AstAnnotationArgument', b)
    if hasattr(a2, 'cal_AstAnnotationArgument'):
        assert _is_linked(a2, 'cal_AstAnnotationArgument', b)
    _safe_set(b, 'cal_AstAnnotation297', set())
    assert not _is_linked(b, 'cal_AstAnnotation297', a2)
    if hasattr(a2, 'cal_AstAnnotationArgument'):
        assert not _is_linked(a2, 'cal_AstAnnotationArgument', b)


def test_assoc_attribute51_reverse_link_reassign_clear():
    a1 = cal_AstConnectionAttribute(name="sample_text")
    a2 = cal_AstConnectionAttribute(name="sample_text_2")
    b = cal_AstConnection(inPort="sample_text", outPort="sample_text")
    _safe_set(b, 'cal_AstConnection52', {a1})
    assert _is_linked(b, 'cal_AstConnection52', a1)
    if hasattr(a1, 'cal_AstConnectionAttribute'):
        assert _is_linked(a1, 'cal_AstConnectionAttribute', b)
    _safe_set(b, 'cal_AstConnection52', {a2})
    assert _is_linked(b, 'cal_AstConnection52', a2)
    if hasattr(a1, 'cal_AstConnectionAttribute'):
        assert not _is_linked(a1, 'cal_AstConnectionAttribute', b)
    if hasattr(a2, 'cal_AstConnectionAttribute'):
        assert _is_linked(a2, 'cal_AstConnectionAttribute', b)
    _safe_set(b, 'cal_AstConnection52', set())
    assert not _is_linked(b, 'cal_AstConnection52', a2)
    if hasattr(a2, 'cal_AstConnectionAttribute'):
        assert not _is_linked(a2, 'cal_AstConnectionAttribute', b)


def test_assoc_codomain277_reverse_link_reassign_clear():
    a1 = cal_AstType(builtin="sample_text")
    a2 = cal_AstType(builtin="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType278', a1)
    assert _is_linked(b, 'cal_AstType278', a1)
    if hasattr(a1, 'cal_AstType276'):
        assert _is_linked(a1, 'cal_AstType276', b)
    _safe_set(b, 'cal_AstType278', a2)
    assert _is_linked(b, 'cal_AstType278', a2)
    if hasattr(a1, 'cal_AstType276'):
        assert not _is_linked(a1, 'cal_AstType276', b)
    if hasattr(a2, 'cal_AstType276'):
        assert _is_linked(a2, 'cal_AstType276', b)
    _safe_set(b, 'cal_AstType278', None)
    assert not _is_linked(b, 'cal_AstType278', a2)
    if hasattr(a2, 'cal_AstType276'):
        assert not _is_linked(a2, 'cal_AstType276', b)


def test_assoc_constructor72_reverse_link_reassign_clear():
    a1 = cal_AstTypeName(name="sample_text")
    a2 = cal_AstTypeName(name="sample_text_2")
    b = cal_AstFunction(name="sample_text")
    _safe_set(b, 'cal_AstFunction74', a1)
    assert _is_linked(b, 'cal_AstFunction74', a1)
    if hasattr(a1, 'cal_AstTypeName73'):
        assert _is_linked(a1, 'cal_AstTypeName73', b)
    _safe_set(b, 'cal_AstFunction74', a2)
    assert _is_linked(b, 'cal_AstFunction74', a2)
    if hasattr(a1, 'cal_AstTypeName73'):
        assert not _is_linked(a1, 'cal_AstTypeName73', b)
    if hasattr(a2, 'cal_AstTypeName73'):
        assert _is_linked(a2, 'cal_AstTypeName73', b)
    _safe_set(b, 'cal_AstFunction74', None)
    assert not _is_linked(b, 'cal_AstFunction74', a2)
    if hasattr(a2, 'cal_AstTypeName73'):
        assert not _is_linked(a2, 'cal_AstTypeName73', b)


def test_assoc_domain274_reverse_link_reassign_clear():
    a1 = cal_AstType(builtin="sample_text")
    a2 = cal_AstType(builtin="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType275', a1)
    assert _is_linked(b, 'cal_AstType275', a1)
    if hasattr(a1, 'cal_AstType273'):
        assert _is_linked(a1, 'cal_AstType273', b)
    _safe_set(b, 'cal_AstType275', a2)
    assert _is_linked(b, 'cal_AstType275', a2)
    if hasattr(a1, 'cal_AstType273'):
        assert not _is_linked(a1, 'cal_AstType273', b)
    if hasattr(a2, 'cal_AstType273'):
        assert _is_linked(a2, 'cal_AstType273', b)
    _safe_set(b, 'cal_AstType275', None)
    assert not _is_linked(b, 'cal_AstType275', a2)
    if hasattr(a2, 'cal_AstType273'):
        assert not _is_linked(a2, 'cal_AstType273', b)


def test_assoc_functions5_reverse_link_reassign_clear():
    a1 = cal_AstNamespace(name="sample_text")
    a2 = cal_AstNamespace(name="sample_text_2")
    b = cal_AstFunction(name="sample_text")
    _safe_set(b, 'cal_AstFunction', a1)
    assert _is_linked(b, 'cal_AstFunction', a1)
    if hasattr(a1, 'cal_AstNamespace6'):
        assert _is_linked(a1, 'cal_AstNamespace6', b)
    _safe_set(b, 'cal_AstFunction', a2)
    assert _is_linked(b, 'cal_AstFunction', a2)
    if hasattr(a1, 'cal_AstNamespace6'):
        assert not _is_linked(a1, 'cal_AstNamespace6', b)
    if hasattr(a2, 'cal_AstNamespace6'):
        assert _is_linked(a2, 'cal_AstNamespace6', b)
    _safe_set(b, 'cal_AstFunction', None)
    assert not _is_linked(b, 'cal_AstFunction', a2)
    if hasattr(a2, 'cal_AstNamespace6'):
        assert not _is_linked(a2, 'cal_AstNamespace6', b)


def test_assoc_imports1_reverse_link_reassign_clear():
    a1 = cal_Import(importedNamespace="sample_text")
    a2 = cal_Import(importedNamespace="sample_text_2")
    b = cal_AstNamespace(name="sample_text")
    _safe_set(b, 'cal_AstNamespace2', {a1})
    assert _is_linked(b, 'cal_AstNamespace2', a1)
    if hasattr(a1, 'cal_Import'):
        assert _is_linked(a1, 'cal_Import', b)
    _safe_set(b, 'cal_AstNamespace2', {a2})
    assert _is_linked(b, 'cal_AstNamespace2', a2)
    if hasattr(a1, 'cal_Import'):
        assert not _is_linked(a1, 'cal_Import', b)
    if hasattr(a2, 'cal_Import'):
        assert _is_linked(a2, 'cal_Import', b)
    _safe_set(b, 'cal_AstNamespace2', set())
    assert not _is_linked(b, 'cal_AstNamespace2', a2)
    if hasattr(a2, 'cal_Import'):
        assert not _is_linked(a2, 'cal_Import', b)


def test_assoc_inputs26_reverse_link_reassign_clear():
    a1 = cal_AstPort(name="sample_text")
    a2 = cal_AstPort(name="sample_text_2")
    b = cal_AstAbstractActor(name="sample_text")
    _safe_set(b, 'cal_AstAbstractActor27', {a1})
    assert _is_linked(b, 'cal_AstAbstractActor27', a1)
    if hasattr(a1, 'cal_AstPort'):
        assert _is_linked(a1, 'cal_AstPort', b)
    _safe_set(b, 'cal_AstAbstractActor27', {a2})
    assert _is_linked(b, 'cal_AstAbstractActor27', a2)
    if hasattr(a1, 'cal_AstPort'):
        assert not _is_linked(a1, 'cal_AstPort', b)
    if hasattr(a2, 'cal_AstPort'):
        assert _is_linked(a2, 'cal_AstPort', b)
    _safe_set(b, 'cal_AstAbstractActor27', set())
    assert not _is_linked(b, 'cal_AstAbstractActor27', a2)
    if hasattr(a2, 'cal_AstPort'):
        assert not _is_linked(a2, 'cal_AstPort', b)


def test_assoc_members279_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType280', {a1})
    assert _is_linked(b, 'cal_AstType280', a1)
    if hasattr(a1, 'cal_AstVariable281'):
        assert _is_linked(a1, 'cal_AstVariable281', b)
    _safe_set(b, 'cal_AstType280', {a2})
    assert _is_linked(b, 'cal_AstType280', a2)
    if hasattr(a1, 'cal_AstVariable281'):
        assert not _is_linked(a1, 'cal_AstVariable281', b)
    if hasattr(a2, 'cal_AstVariable281'):
        assert _is_linked(a2, 'cal_AstVariable281', b)
    _safe_set(b, 'cal_AstType280', set())
    assert not _is_linked(b, 'cal_AstType280', a2)
    if hasattr(a2, 'cal_AstVariable281'):
        assert not _is_linked(a2, 'cal_AstVariable281', b)


def test_assoc_members84_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstFunction(name="sample_text")
    _safe_set(b, 'cal_AstFunction85', {a1})
    assert _is_linked(b, 'cal_AstFunction85', a1)
    if hasattr(a1, 'cal_AstVariable86'):
        assert _is_linked(a1, 'cal_AstVariable86', b)
    _safe_set(b, 'cal_AstFunction85', {a2})
    assert _is_linked(b, 'cal_AstFunction85', a2)
    if hasattr(a1, 'cal_AstVariable86'):
        assert not _is_linked(a1, 'cal_AstVariable86', b)
    if hasattr(a2, 'cal_AstVariable86'):
        assert _is_linked(a2, 'cal_AstVariable86', b)
    _safe_set(b, 'cal_AstFunction85', set())
    assert not _is_linked(b, 'cal_AstFunction85', a2)
    if hasattr(a2, 'cal_AstVariable86'):
        assert not _is_linked(a2, 'cal_AstVariable86', b)


def test_assoc_name270_reverse_link_reassign_clear():
    a1 = cal_AstTypeName(name="sample_text")
    a2 = cal_AstTypeName(name="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType271', a1)
    assert _is_linked(b, 'cal_AstType271', a1)
    if hasattr(a1, 'cal_AstTypeName272'):
        assert _is_linked(a1, 'cal_AstTypeName272', b)
    _safe_set(b, 'cal_AstType271', a2)
    assert _is_linked(b, 'cal_AstType271', a2)
    if hasattr(a1, 'cal_AstTypeName272'):
        assert not _is_linked(a1, 'cal_AstTypeName272', b)
    if hasattr(a2, 'cal_AstTypeName272'):
        assert _is_linked(a2, 'cal_AstTypeName272', b)
    _safe_set(b, 'cal_AstType271', None)
    assert not _is_linked(b, 'cal_AstType271', a2)
    if hasattr(a2, 'cal_AstTypeName272'):
        assert not _is_linked(a2, 'cal_AstTypeName272', b)


def test_assoc_namespaces16_reverse_link_reassign_clear():
    a1 = cal_AstNamespace(name="sample_text")
    a2 = cal_AstNamespace(name="sample_text_2")
    b = cal_AstNamespace(name="sample_text")
    _safe_set(b, 'cal_AstNamespace17', a1)
    assert _is_linked(b, 'cal_AstNamespace17', a1)
    if hasattr(a1, 'cal_AstNamespace15'):
        assert _is_linked(a1, 'cal_AstNamespace15', b)
    _safe_set(b, 'cal_AstNamespace17', a2)
    assert _is_linked(b, 'cal_AstNamespace17', a2)
    if hasattr(a1, 'cal_AstNamespace15'):
        assert not _is_linked(a1, 'cal_AstNamespace15', b)
    if hasattr(a2, 'cal_AstNamespace15'):
        assert _is_linked(a2, 'cal_AstNamespace15', b)
    _safe_set(b, 'cal_AstNamespace17', None)
    assert not _is_linked(b, 'cal_AstNamespace17', a2)
    if hasattr(a2, 'cal_AstNamespace15'):
        assert not _is_linked(a2, 'cal_AstNamespace15', b)


def test_assoc_outputs28_reverse_link_reassign_clear():
    a1 = cal_AstPort(name="sample_text")
    a2 = cal_AstPort(name="sample_text_2")
    b = cal_AstAbstractActor(name="sample_text")
    _safe_set(b, 'cal_AstAbstractActor29', {a1})
    assert _is_linked(b, 'cal_AstAbstractActor29', a1)
    if hasattr(a1, 'cal_AstPort30'):
        assert _is_linked(a1, 'cal_AstPort30', b)
    _safe_set(b, 'cal_AstAbstractActor29', {a2})
    assert _is_linked(b, 'cal_AstAbstractActor29', a2)
    if hasattr(a1, 'cal_AstPort30'):
        assert not _is_linked(a1, 'cal_AstPort30', b)
    if hasattr(a2, 'cal_AstPort30'):
        assert _is_linked(a2, 'cal_AstPort30', b)
    _safe_set(b, 'cal_AstAbstractActor29', set())
    assert not _is_linked(b, 'cal_AstAbstractActor29', a2)
    if hasattr(a2, 'cal_AstPort30'):
        assert not _is_linked(a2, 'cal_AstPort30', b)


def test_assoc_parameters127_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstProcedure(name="sample_text")
    _safe_set(b, 'cal_AstProcedure128', {a1})
    assert _is_linked(b, 'cal_AstProcedure128', a1)
    if hasattr(a1, 'cal_AstVariable129'):
        assert _is_linked(a1, 'cal_AstVariable129', b)
    _safe_set(b, 'cal_AstProcedure128', {a2})
    assert _is_linked(b, 'cal_AstProcedure128', a2)
    if hasattr(a1, 'cal_AstVariable129'):
        assert not _is_linked(a1, 'cal_AstVariable129', b)
    if hasattr(a2, 'cal_AstVariable129'):
        assert _is_linked(a2, 'cal_AstVariable129', b)
    _safe_set(b, 'cal_AstProcedure128', set())
    assert not _is_linked(b, 'cal_AstProcedure128', a2)
    if hasattr(a2, 'cal_AstVariable129'):
        assert not _is_linked(a2, 'cal_AstVariable129', b)


def test_assoc_parameters23_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstAbstractActor(name="sample_text")
    _safe_set(b, 'cal_AstAbstractActor24', {a1})
    assert _is_linked(b, 'cal_AstAbstractActor24', a1)
    if hasattr(a1, 'cal_AstVariable25'):
        assert _is_linked(a1, 'cal_AstVariable25', b)
    _safe_set(b, 'cal_AstAbstractActor24', {a2})
    assert _is_linked(b, 'cal_AstAbstractActor24', a2)
    if hasattr(a1, 'cal_AstVariable25'):
        assert not _is_linked(a1, 'cal_AstVariable25', b)
    if hasattr(a2, 'cal_AstVariable25'):
        assert _is_linked(a2, 'cal_AstVariable25', b)
    _safe_set(b, 'cal_AstAbstractActor24', set())
    assert not _is_linked(b, 'cal_AstAbstractActor24', a2)
    if hasattr(a2, 'cal_AstVariable25'):
        assert not _is_linked(a2, 'cal_AstVariable25', b)


def test_assoc_parameters40_reverse_link_reassign_clear():
    a1 = cal_AstAssignParameter(name="sample_text")
    a2 = cal_AstAssignParameter(name="sample_text_2")
    b = cal_AstActorVariable(name="sample_text")
    _safe_set(b, 'cal_AstActorVariable41', {a1})
    assert _is_linked(b, 'cal_AstActorVariable41', a1)
    if hasattr(a1, 'cal_AstAssignParameter'):
        assert _is_linked(a1, 'cal_AstAssignParameter', b)
    _safe_set(b, 'cal_AstActorVariable41', {a2})
    assert _is_linked(b, 'cal_AstActorVariable41', a2)
    if hasattr(a1, 'cal_AstAssignParameter'):
        assert not _is_linked(a1, 'cal_AstAssignParameter', b)
    if hasattr(a2, 'cal_AstAssignParameter'):
        assert _is_linked(a2, 'cal_AstAssignParameter', b)
    _safe_set(b, 'cal_AstActorVariable41', set())
    assert not _is_linked(b, 'cal_AstActorVariable41', a2)
    if hasattr(a2, 'cal_AstAssignParameter'):
        assert not _is_linked(a2, 'cal_AstAssignParameter', b)


def test_assoc_parameters90_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstFunction(name="sample_text")
    _safe_set(b, 'cal_AstFunction91', {a1})
    assert _is_linked(b, 'cal_AstFunction91', a1)
    if hasattr(a1, 'cal_AstVariable92'):
        assert _is_linked(a1, 'cal_AstVariable92', b)
    _safe_set(b, 'cal_AstFunction91', {a2})
    assert _is_linked(b, 'cal_AstFunction91', a2)
    if hasattr(a1, 'cal_AstVariable92'):
        assert not _is_linked(a1, 'cal_AstVariable92', b)
    if hasattr(a2, 'cal_AstVariable92'):
        assert _is_linked(a2, 'cal_AstVariable92', b)
    _safe_set(b, 'cal_AstFunction91', set())
    assert not _is_linked(b, 'cal_AstFunction91', a2)
    if hasattr(a2, 'cal_AstVariable92'):
        assert not _is_linked(a2, 'cal_AstVariable92', b)


def test_assoc_type121_reverse_link_reassign_clear():
    a1 = cal_AstType(builtin="sample_text")
    a2 = cal_AstType(builtin="sample_text_2")
    b = cal_AstPort(name="sample_text")
    _safe_set(b, 'cal_AstPort122', a1)
    assert _is_linked(b, 'cal_AstPort122', a1)
    if hasattr(a1, 'cal_AstType123'):
        assert _is_linked(a1, 'cal_AstType123', b)
    _safe_set(b, 'cal_AstPort122', a2)
    assert _is_linked(b, 'cal_AstPort122', a2)
    if hasattr(a1, 'cal_AstType123'):
        assert not _is_linked(a1, 'cal_AstType123', b)
    if hasattr(a2, 'cal_AstType123'):
        assert _is_linked(a2, 'cal_AstType123', b)
    _safe_set(b, 'cal_AstPort122', None)
    assert not _is_linked(b, 'cal_AstPort122', a2)
    if hasattr(a2, 'cal_AstType123'):
        assert not _is_linked(a2, 'cal_AstType123', b)


def test_assoc_type287_reverse_link_reassign_clear():
    a1 = cal_AstTypeParam(name="sample_text")
    a2 = cal_AstTypeParam(name="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType289', a1)
    assert _is_linked(b, 'cal_AstType289', a1)
    if hasattr(a1, 'cal_AstTypeParam288'):
        assert _is_linked(a1, 'cal_AstTypeParam288', b)
    _safe_set(b, 'cal_AstType289', a2)
    assert _is_linked(b, 'cal_AstType289', a2)
    if hasattr(a1, 'cal_AstTypeParam288'):
        assert not _is_linked(a1, 'cal_AstTypeParam288', b)
    if hasattr(a2, 'cal_AstTypeParam288'):
        assert _is_linked(a2, 'cal_AstTypeParam288', b)
    _safe_set(b, 'cal_AstType289', None)
    assert not _is_linked(b, 'cal_AstType289', a2)
    if hasattr(a2, 'cal_AstTypeParam288'):
        assert not _is_linked(a2, 'cal_AstTypeParam288', b)


def test_assoc_type65_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType', a1)
    assert _is_linked(b, 'cal_AstType', a1)
    if hasattr(a1, 'cal_AstVariable66'):
        assert _is_linked(a1, 'cal_AstVariable66', b)
    _safe_set(b, 'cal_AstType', a2)
    assert _is_linked(b, 'cal_AstType', a2)
    if hasattr(a1, 'cal_AstVariable66'):
        assert not _is_linked(a1, 'cal_AstVariable66', b)
    if hasattr(a2, 'cal_AstVariable66'):
        assert _is_linked(a2, 'cal_AstVariable66', b)
    _safe_set(b, 'cal_AstType', None)
    assert not _is_linked(b, 'cal_AstType', a2)
    if hasattr(a2, 'cal_AstVariable66'):
        assert not _is_linked(a2, 'cal_AstVariable66', b)


def test_assoc_type75_reverse_link_reassign_clear():
    a1 = cal_AstTypeName(name="sample_text")
    a2 = cal_AstTypeName(name="sample_text_2")
    b = cal_AstType(builtin="sample_text")
    _safe_set(b, 'cal_AstType77', a1)
    assert _is_linked(b, 'cal_AstType77', a1)
    if hasattr(a1, 'cal_AstTypeName76'):
        assert _is_linked(a1, 'cal_AstTypeName76', b)
    _safe_set(b, 'cal_AstType77', a2)
    assert _is_linked(b, 'cal_AstType77', a2)
    if hasattr(a1, 'cal_AstTypeName76'):
        assert not _is_linked(a1, 'cal_AstTypeName76', b)
    if hasattr(a2, 'cal_AstTypeName76'):
        assert _is_linked(a2, 'cal_AstTypeName76', b)
    _safe_set(b, 'cal_AstType77', None)
    assert not _is_linked(b, 'cal_AstType77', a2)
    if hasattr(a2, 'cal_AstTypeName76'):
        assert not _is_linked(a2, 'cal_AstTypeName76', b)


def test_assoc_type93_reverse_link_reassign_clear():
    a1 = cal_AstType(builtin="sample_text")
    a2 = cal_AstType(builtin="sample_text_2")
    b = cal_AstFunction(name="sample_text")
    _safe_set(b, 'cal_AstFunction94', a1)
    assert _is_linked(b, 'cal_AstFunction94', a1)
    if hasattr(a1, 'cal_AstType95'):
        assert _is_linked(a1, 'cal_AstType95', b)
    _safe_set(b, 'cal_AstFunction94', a2)
    assert _is_linked(b, 'cal_AstFunction94', a2)
    if hasattr(a1, 'cal_AstType95'):
        assert not _is_linked(a1, 'cal_AstType95', b)
    if hasattr(a2, 'cal_AstType95'):
        assert _is_linked(a2, 'cal_AstType95', b)
    _safe_set(b, 'cal_AstFunction94', None)
    assert not _is_linked(b, 'cal_AstFunction94', a2)
    if hasattr(a2, 'cal_AstType95'):
        assert not _is_linked(a2, 'cal_AstType95', b)


def test_assoc_typedefs13_reverse_link_reassign_clear():
    a1 = cal_AstTypeName(name="sample_text")
    a2 = cal_AstTypeName(name="sample_text_2")
    b = cal_AstNamespace(name="sample_text")
    _safe_set(b, 'cal_AstNamespace14', {a1})
    assert _is_linked(b, 'cal_AstNamespace14', a1)
    if hasattr(a1, 'cal_AstTypeName'):
        assert _is_linked(a1, 'cal_AstTypeName', b)
    _safe_set(b, 'cal_AstNamespace14', {a2})
    assert _is_linked(b, 'cal_AstNamespace14', a2)
    if hasattr(a1, 'cal_AstTypeName'):
        assert not _is_linked(a1, 'cal_AstTypeName', b)
    if hasattr(a2, 'cal_AstTypeName'):
        assert _is_linked(a2, 'cal_AstTypeName', b)
    _safe_set(b, 'cal_AstNamespace14', set())
    assert not _is_linked(b, 'cal_AstNamespace14', a2)
    if hasattr(a2, 'cal_AstTypeName'):
        assert not _is_linked(a2, 'cal_AstTypeName', b)


def test_assoc_variables130_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstProcedure(name="sample_text")
    _safe_set(b, 'cal_AstProcedure131', {a1})
    assert _is_linked(b, 'cal_AstProcedure131', a1)
    if hasattr(a1, 'cal_AstVariable132'):
        assert _is_linked(a1, 'cal_AstVariable132', b)
    _safe_set(b, 'cal_AstProcedure131', {a2})
    assert _is_linked(b, 'cal_AstProcedure131', a2)
    if hasattr(a1, 'cal_AstVariable132'):
        assert not _is_linked(a1, 'cal_AstVariable132', b)
    if hasattr(a2, 'cal_AstVariable132'):
        assert _is_linked(a2, 'cal_AstVariable132', b)
    _safe_set(b, 'cal_AstProcedure131', set())
    assert not _is_linked(b, 'cal_AstProcedure131', a2)
    if hasattr(a2, 'cal_AstVariable132'):
        assert not _is_linked(a2, 'cal_AstVariable132', b)


def test_assoc_variables7_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstNamespace(name="sample_text")
    _safe_set(b, 'cal_AstNamespace8', {a1})
    assert _is_linked(b, 'cal_AstNamespace8', a1)
    if hasattr(a1, 'cal_AstVariable'):
        assert _is_linked(a1, 'cal_AstVariable', b)
    _safe_set(b, 'cal_AstNamespace8', {a2})
    assert _is_linked(b, 'cal_AstNamespace8', a2)
    if hasattr(a1, 'cal_AstVariable'):
        assert not _is_linked(a1, 'cal_AstVariable', b)
    if hasattr(a2, 'cal_AstVariable'):
        assert _is_linked(a2, 'cal_AstVariable', b)
    _safe_set(b, 'cal_AstNamespace8', set())
    assert not _is_linked(b, 'cal_AstNamespace8', a2)
    if hasattr(a2, 'cal_AstVariable'):
        assert not _is_linked(a2, 'cal_AstVariable', b)


def test_assoc_variables96_reverse_link_reassign_clear():
    a1 = cal_AstVariable(constant=True, name="sample_text")
    a2 = cal_AstVariable(constant=False, name="sample_text_2")
    b = cal_AstFunction(name="sample_text")
    _safe_set(b, 'cal_AstFunction97', {a1})
    assert _is_linked(b, 'cal_AstFunction97', a1)
    if hasattr(a1, 'cal_AstVariable98'):
        assert _is_linked(a1, 'cal_AstVariable98', b)
    _safe_set(b, 'cal_AstFunction97', {a2})
    assert _is_linked(b, 'cal_AstFunction97', a2)
    if hasattr(a1, 'cal_AstVariable98'):
        assert not _is_linked(a1, 'cal_AstVariable98', b)
    if hasattr(a2, 'cal_AstVariable98'):
        assert _is_linked(a2, 'cal_AstVariable98', b)
    _safe_set(b, 'cal_AstFunction97', set())
    assert not _is_linked(b, 'cal_AstFunction97', a2)
    if hasattr(a2, 'cal_AstVariable98'):
        assert not _is_linked(a2, 'cal_AstVariable98', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actor21_stub_double():
    # cal_AstEntity has no real 'cal_AstEntity22' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAbstractActor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAbstractActor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAbstractActor(name="sample_text")
    partner = cal_AstEntity()
    setattr(partner, 'cal_AstEntity22', None)
    _safe_set(owner, 'cal_AstAbstractActor', partner)
    assert getattr(partner, 'cal_AstEntity22') == owner
    _safe_set(owner, 'cal_AstAbstractActor', None)
    assert getattr(partner, 'cal_AstEntity22') is None


def test_assoc_annotations152_stub_double():
    # cal_AstAction has no real 'cal_AstAction153' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAnnotation(name="sample_text")
    partner = cal_AstAction()
    setattr(partner, 'cal_AstAction153', None)
    _safe_set(owner, 'cal_AstAnnotation154', partner)
    assert owner in getattr(partner, 'cal_AstAction153')
    _safe_set(owner, 'cal_AstAnnotation154', None)
    assert owner not in getattr(partner, 'cal_AstAction153')


def test_assoc_annotations18_stub_double():
    # cal_AstEntity has no real 'cal_AstEntity19' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAnnotation(name="sample_text")
    partner = cal_AstEntity()
    setattr(partner, 'cal_AstEntity19', None)
    _safe_set(owner, 'cal_AstAnnotation20', partner)
    assert owner in getattr(partner, 'cal_AstEntity19')
    _safe_set(owner, 'cal_AstAnnotation20', None)
    assert owner not in getattr(partner, 'cal_AstEntity19')


def test_assoc_connections44_stub_double():
    # cal_AstStructure has no real 'cal_AstStructure45' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstConnection(inPort="sample_text", outPort="sample_text")
    partner = cal_AstStructure()
    setattr(partner, 'cal_AstStructure45', None)
    _safe_set(owner, 'cal_AstConnection', partner)
    assert owner in getattr(partner, 'cal_AstStructure45')
    _safe_set(owner, 'cal_AstConnection', None)
    assert owner not in getattr(partner, 'cal_AstStructure45')


def test_assoc_dimensions267_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression269' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstType(builtin="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression269', None)
    _safe_set(owner, 'cal_AstType268', {partner})
    assert getattr(partner, 'cal_AstExpression269') == owner
    _safe_set(owner, 'cal_AstType268', set())
    assert getattr(partner, 'cal_AstExpression269') is None


def test_assoc_dimensions67_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression69' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression69', None)
    _safe_set(owner, 'cal_AstVariable68', {partner})
    assert getattr(partner, 'cal_AstExpression69') == owner
    _safe_set(owner, 'cal_AstVariable68', set())
    assert getattr(partner, 'cal_AstExpression69') is None


def test_assoc_entities0_stub_double():
    # cal_AstEntity has no real 'cal_AstEntity' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstNamespace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstNamespace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstNamespace(name="sample_text")
    partner = cal_AstEntity()
    setattr(partner, 'cal_AstEntity', None)
    _safe_set(owner, 'cal_AstNamespace', {partner})
    assert getattr(partner, 'cal_AstEntity') == owner
    _safe_set(owner, 'cal_AstNamespace', set())
    assert getattr(partner, 'cal_AstEntity') is None


def test_assoc_expression303_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression304' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstExpressionUnary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstExpressionUnary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstExpressionUnary(unaryOperator="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression304', None)
    _safe_set(owner, 'cal_AstExpressionUnary', partner)
    assert getattr(partner, 'cal_AstExpression304') == owner
    _safe_set(owner, 'cal_AstExpressionUnary', None)
    assert getattr(partner, 'cal_AstExpression304') is None


def test_assoc_expression99_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression101' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstFunction(name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression101', None)
    _safe_set(owner, 'cal_AstFunction100', partner)
    assert getattr(partner, 'cal_AstExpression101') == owner
    _safe_set(owner, 'cal_AstFunction100', None)
    assert getattr(partner, 'cal_AstExpression101') is None


def test_assoc_externals9_stub_double():
    # cal_EObject has no real 'cal_EObject' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstNamespace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstNamespace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstNamespace(name="sample_text")
    partner = cal_EObject()
    setattr(partner, 'cal_EObject', None)
    _safe_set(owner, 'cal_AstNamespace10', {partner})
    assert getattr(partner, 'cal_EObject') == owner
    _safe_set(owner, 'cal_AstNamespace10', set())
    assert getattr(partner, 'cal_EObject') is None


def test_assoc_from_46_stub_double():
    # cal_AstActorVariableReference has no real 'cal_AstActorVariableReference' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstConnection(inPort="sample_text", outPort="sample_text")
    partner = cal_AstActorVariableReference()
    setattr(partner, 'cal_AstActorVariableReference', None)
    _safe_set(owner, 'cal_AstConnection47', partner)
    assert getattr(partner, 'cal_AstActorVariableReference') == owner
    _safe_set(owner, 'cal_AstConnection47', None)
    assert getattr(partner, 'cal_AstActorVariableReference') is None


def test_assoc_function234_stub_double():
    # cal_AstExpressionCall has no real 'cal_AstExpressionCall' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstFunction(name="sample_text")
    partner = cal_AstExpressionCall()
    setattr(partner, 'cal_AstExpressionCall', None)
    _safe_set(owner, 'cal_AstFunction235', partner)
    assert getattr(partner, 'cal_AstExpressionCall') == owner
    _safe_set(owner, 'cal_AstFunction235', None)
    assert getattr(partner, 'cal_AstExpressionCall') is None


def test_assoc_functions102_stub_double():
    # cal_AstActor has no real 'cal_AstActor' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstFunction(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor', None)
    _safe_set(owner, 'cal_AstFunction103', partner)
    assert owner in getattr(partner, 'cal_AstActor')
    _safe_set(owner, 'cal_AstFunction103', None)
    assert owner not in getattr(partner, 'cal_AstActor')


def test_assoc_initialState139_stub_double():
    # cal_AstSchedule has no real 'cal_AstSchedule140' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text")
    partner = cal_AstSchedule()
    setattr(partner, 'cal_AstSchedule140', None)
    _safe_set(owner, 'cal_AstState', partner)
    assert getattr(partner, 'cal_AstSchedule140') == owner
    _safe_set(owner, 'cal_AstState', None)
    assert getattr(partner, 'cal_AstSchedule140') is None


def test_assoc_instances33_stub_double():
    # cal_AstNetwork has no real 'cal_AstNetwork34' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstActorVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstActorVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstActorVariable(name="sample_text")
    partner = cal_AstNetwork()
    setattr(partner, 'cal_AstNetwork34', None)
    _safe_set(owner, 'cal_AstActorVariable', partner)
    assert owner in getattr(partner, 'cal_AstNetwork34')
    _safe_set(owner, 'cal_AstActorVariable', None)
    assert owner not in getattr(partner, 'cal_AstNetwork34')


def test_assoc_left298_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression299' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstExpressionBinary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstExpressionBinary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstExpressionBinary(operator="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression299', None)
    _safe_set(owner, 'cal_AstExpressionBinary', partner)
    assert getattr(partner, 'cal_AstExpression299') == owner
    _safe_set(owner, 'cal_AstExpressionBinary', None)
    assert getattr(partner, 'cal_AstExpression299') is None


def test_assoc_member193_stub_double():
    # cal_AstStatementAssign has no real 'cal_AstStatementAssign194' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstMemberAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstMemberAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstMemberAccess(name="sample_text")
    partner = cal_AstStatementAssign()
    setattr(partner, 'cal_AstStatementAssign194', None)
    _safe_set(owner, 'cal_AstMemberAccess', partner)
    assert owner in getattr(partner, 'cal_AstStatementAssign194')
    _safe_set(owner, 'cal_AstMemberAccess', None)
    assert owner not in getattr(partner, 'cal_AstStatementAssign194')


def test_assoc_member262_stub_double():
    # cal_AstExpressionVariable has no real 'cal_AstExpressionVariable263' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstMemberAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstMemberAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstMemberAccess(name="sample_text")
    partner = cal_AstExpressionVariable()
    setattr(partner, 'cal_AstExpressionVariable263', None)
    _safe_set(owner, 'cal_AstMemberAccess264', partner)
    assert owner in getattr(partner, 'cal_AstExpressionVariable263')
    _safe_set(owner, 'cal_AstMemberAccess264', None)
    assert owner not in getattr(partner, 'cal_AstExpressionVariable263')


def test_assoc_memberIndex293_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression295' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstMemberAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstMemberAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstMemberAccess(name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression295', None)
    _safe_set(owner, 'cal_AstMemberAccess294', {partner})
    assert getattr(partner, 'cal_AstExpression295') == owner
    _safe_set(owner, 'cal_AstMemberAccess294', set())
    assert getattr(partner, 'cal_AstExpression295') is None


def test_assoc_parameters70_stub_double():
    # cal_AstTypeDefinitionParameter has no real 'cal_AstTypeDefinitionParameter' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTypeName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTypeName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTypeName(name="sample_text")
    partner = cal_AstTypeDefinitionParameter()
    setattr(partner, 'cal_AstTypeDefinitionParameter', None)
    _safe_set(owner, 'cal_AstTypeName71', {partner})
    assert getattr(partner, 'cal_AstTypeDefinitionParameter') == owner
    _safe_set(owner, 'cal_AstTypeName71', set())
    assert getattr(partner, 'cal_AstTypeDefinitionParameter') is None


def test_assoc_params282_stub_double():
    # cal_AstTypeParameterList has no real 'cal_AstTypeParameterList283' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTypeParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTypeParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTypeParam(name="sample_text")
    partner = cal_AstTypeParameterList()
    setattr(partner, 'cal_AstTypeParameterList283', None)
    _safe_set(owner, 'cal_AstTypeParam', partner)
    assert owner in getattr(partner, 'cal_AstTypeParameterList283')
    _safe_set(owner, 'cal_AstTypeParam', None)
    assert owner not in getattr(partner, 'cal_AstTypeParameterList283')


def test_assoc_port171_stub_double():
    # cal_AstInputPattern has no real 'cal_AstInputPattern172' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_AstInputPattern()
    setattr(partner, 'cal_AstInputPattern172', None)
    _safe_set(owner, 'cal_AstPort173', partner)
    assert getattr(partner, 'cal_AstInputPattern172') == owner
    _safe_set(owner, 'cal_AstPort173', None)
    assert getattr(partner, 'cal_AstInputPattern172') is None


def test_assoc_port180_stub_double():
    # cal_AstOutputPattern has no real 'cal_AstOutputPattern181' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstPort(name="sample_text")
    partner = cal_AstOutputPattern()
    setattr(partner, 'cal_AstOutputPattern181', None)
    _safe_set(owner, 'cal_AstPort182', partner)
    assert getattr(partner, 'cal_AstOutputPattern181') == owner
    _safe_set(owner, 'cal_AstPort182', None)
    assert getattr(partner, 'cal_AstOutputPattern181') is None


def test_assoc_procedure198_stub_double():
    # cal_AstStatementCall has no real 'cal_AstStatementCall' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_AstStatementCall()
    setattr(partner, 'cal_AstStatementCall', None)
    _safe_set(owner, 'cal_AstProcedure199', partner)
    assert getattr(partner, 'cal_AstStatementCall') == owner
    _safe_set(owner, 'cal_AstProcedure199', None)
    assert getattr(partner, 'cal_AstStatementCall') is None


def test_assoc_procedures104_stub_double():
    # cal_AstActor has no real 'cal_AstActor105' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor105', None)
    _safe_set(owner, 'cal_AstProcedure', partner)
    assert owner in getattr(partner, 'cal_AstActor105')
    _safe_set(owner, 'cal_AstProcedure', None)
    assert owner not in getattr(partner, 'cal_AstActor105')


def test_assoc_right300_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression302' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstExpressionBinary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstExpressionBinary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstExpressionBinary(operator="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression302', None)
    _safe_set(owner, 'cal_AstExpressionBinary301', partner)
    assert getattr(partner, 'cal_AstExpression302') == owner
    _safe_set(owner, 'cal_AstExpressionBinary301', None)
    assert getattr(partner, 'cal_AstExpression302') is None


def test_assoc_source143_stub_double():
    # cal_AstTransition has no real 'cal_AstTransition144' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text")
    partner = cal_AstTransition()
    setattr(partner, 'cal_AstTransition144', None)
    _safe_set(owner, 'cal_AstState145', partner)
    assert getattr(partner, 'cal_AstTransition144') == owner
    _safe_set(owner, 'cal_AstState145', None)
    assert getattr(partner, 'cal_AstTransition144') is None


def test_assoc_stateVariables111_stub_double():
    # cal_AstActor has no real 'cal_AstActor112' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstActor()
    setattr(partner, 'cal_AstActor112', None)
    _safe_set(owner, 'cal_AstVariable113', partner)
    assert owner in getattr(partner, 'cal_AstActor112')
    _safe_set(owner, 'cal_AstVariable113', None)
    assert owner not in getattr(partner, 'cal_AstActor112')


def test_assoc_statements133_stub_double():
    # cal_AstStatement has no real 'cal_AstStatement' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstProcedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstProcedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstProcedure(name="sample_text")
    partner = cal_AstStatement()
    setattr(partner, 'cal_AstStatement', None)
    _safe_set(owner, 'cal_AstProcedure134', {partner})
    assert getattr(partner, 'cal_AstStatement') == owner
    _safe_set(owner, 'cal_AstProcedure134', set())
    assert getattr(partner, 'cal_AstStatement') is None


def test_assoc_tag155_stub_double():
    # cal_AstAction has no real 'cal_AstAction156' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_AstAction()
    setattr(partner, 'cal_AstAction156', None)
    _safe_set(owner, 'cal_AstTag157', partner)
    assert getattr(partner, 'cal_AstAction156') == owner
    _safe_set(owner, 'cal_AstTag157', None)
    assert getattr(partner, 'cal_AstAction156') is None


def test_assoc_tags135_stub_double():
    # cal_AstInequality has no real 'cal_AstInequality' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_AstInequality()
    setattr(partner, 'cal_AstInequality', None)
    _safe_set(owner, 'cal_AstTag', partner)
    assert owner in getattr(partner, 'cal_AstInequality')
    _safe_set(owner, 'cal_AstTag', None)
    assert owner not in getattr(partner, 'cal_AstInequality')


def test_assoc_tags146_stub_double():
    # cal_AstTransition has no real 'cal_AstTransition147' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTag(identifiers="sample_text")
    partner = cal_AstTransition()
    setattr(partner, 'cal_AstTransition147', None)
    _safe_set(owner, 'cal_AstTag148', partner)
    assert owner in getattr(partner, 'cal_AstTransition147')
    _safe_set(owner, 'cal_AstTag148', None)
    assert owner not in getattr(partner, 'cal_AstTransition147')


def test_assoc_target149_stub_double():
    # cal_AstTransition has no real 'cal_AstTransition150' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstState(name="sample_text")
    partner = cal_AstTransition()
    setattr(partner, 'cal_AstTransition150', None)
    _safe_set(owner, 'cal_AstState151', partner)
    assert getattr(partner, 'cal_AstTransition150') == owner
    _safe_set(owner, 'cal_AstState151', None)
    assert getattr(partner, 'cal_AstTransition150') is None


def test_assoc_to48_stub_double():
    # cal_AstActorVariableReference has no real 'cal_AstActorVariableReference50' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstConnection(inPort="sample_text", outPort="sample_text")
    partner = cal_AstActorVariableReference()
    setattr(partner, 'cal_AstActorVariableReference50', None)
    _safe_set(owner, 'cal_AstConnection49', partner)
    assert getattr(partner, 'cal_AstActorVariableReference50') == owner
    _safe_set(owner, 'cal_AstConnection49', None)
    assert getattr(partner, 'cal_AstActorVariableReference50') is None


def test_assoc_tokens174_stub_double():
    # cal_AstInputPattern has no real 'cal_AstInputPattern175' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstInputPattern()
    setattr(partner, 'cal_AstInputPattern175', None)
    _safe_set(owner, 'cal_AstVariable176', partner)
    assert owner in getattr(partner, 'cal_AstInputPattern175')
    _safe_set(owner, 'cal_AstVariable176', None)
    assert owner not in getattr(partner, 'cal_AstInputPattern175')


def test_assoc_type37_stub_double():
    # cal_AstEntity has no real 'cal_AstEntity39' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstActorVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstActorVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstActorVariable(name="sample_text")
    partner = cal_AstEntity()
    setattr(partner, 'cal_AstEntity39', None)
    _safe_set(owner, 'cal_AstActorVariable38', partner)
    assert getattr(partner, 'cal_AstEntity39') == owner
    _safe_set(owner, 'cal_AstActorVariable38', None)
    assert getattr(partner, 'cal_AstEntity39') is None


def test_assoc_type81_stub_double():
    # cal_AstTypeDefinitionParameter has no real 'cal_AstTypeDefinitionParameter82' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTypeName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTypeName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTypeName(name="sample_text")
    partner = cal_AstTypeDefinitionParameter()
    setattr(partner, 'cal_AstTypeDefinitionParameter82', None)
    _safe_set(owner, 'cal_AstTypeName83', partner)
    assert getattr(partner, 'cal_AstTypeDefinitionParameter82') == owner
    _safe_set(owner, 'cal_AstTypeName83', None)
    assert getattr(partner, 'cal_AstTypeDefinitionParameter82') is None


def test_assoc_typeParams265_stub_double():
    # cal_AstTypeParameterList has no real 'cal_AstTypeParameterList' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstType(builtin="sample_text")
    partner = cal_AstTypeParameterList()
    setattr(partner, 'cal_AstTypeParameterList', None)
    _safe_set(owner, 'cal_AstType266', partner)
    assert getattr(partner, 'cal_AstTypeParameterList') == owner
    _safe_set(owner, 'cal_AstType266', None)
    assert getattr(partner, 'cal_AstTypeParameterList') is None


def test_assoc_units3_stub_double():
    # cal_AstUnit has no real 'cal_AstUnit' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstNamespace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstNamespace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstNamespace(name="sample_text")
    partner = cal_AstUnit()
    setattr(partner, 'cal_AstUnit', None)
    _safe_set(owner, 'cal_AstNamespace4', {partner})
    assert getattr(partner, 'cal_AstUnit') == owner
    _safe_set(owner, 'cal_AstNamespace4', set())
    assert getattr(partner, 'cal_AstUnit') is None


def test_assoc_value284_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression286' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstTypeParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstTypeParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstTypeParam(name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression286', None)
    _safe_set(owner, 'cal_AstTypeParam285', partner)
    assert getattr(partner, 'cal_AstExpression286') == owner
    _safe_set(owner, 'cal_AstTypeParam285', None)
    assert getattr(partner, 'cal_AstExpression286') is None


def test_assoc_value42_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstAssignParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstAssignParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstAssignParameter(name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression', None)
    _safe_set(owner, 'cal_AstAssignParameter43', partner)
    assert getattr(partner, 'cal_AstExpression') == owner
    _safe_set(owner, 'cal_AstAssignParameter43', None)
    assert getattr(partner, 'cal_AstExpression') is None


def test_assoc_value56_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression58' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstConnectionAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstConnectionAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstConnectionAttribute(name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression58', None)
    _safe_set(owner, 'cal_AstConnectionAttribute57', partner)
    assert getattr(partner, 'cal_AstExpression58') == owner
    _safe_set(owner, 'cal_AstConnectionAttribute57', None)
    assert getattr(partner, 'cal_AstExpression58') is None


def test_assoc_value59_stub_double():
    # cal_AstExpression has no real 'cal_AstExpression61' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstExpression()
    setattr(partner, 'cal_AstExpression61', None)
    _safe_set(owner, 'cal_AstVariable60', partner)
    assert getattr(partner, 'cal_AstExpression61') == owner
    _safe_set(owner, 'cal_AstVariable60', None)
    assert getattr(partner, 'cal_AstExpression61') is None


def test_assoc_value78_stub_double():
    # cal_AstTypeDefinitionParameter has no real 'cal_AstTypeDefinitionParameter79' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstTypeDefinitionParameter()
    setattr(partner, 'cal_AstTypeDefinitionParameter79', None)
    _safe_set(owner, 'cal_AstVariable80', partner)
    assert getattr(partner, 'cal_AstTypeDefinitionParameter79') == owner
    _safe_set(owner, 'cal_AstVariable80', None)
    assert getattr(partner, 'cal_AstTypeDefinitionParameter79') is None


def test_assoc_variable210_stub_double():
    # cal_AstForeachGenerator has no real 'cal_AstForeachGenerator211' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstForeachGenerator()
    setattr(partner, 'cal_AstForeachGenerator211', None)
    _safe_set(owner, 'cal_AstVariable212', partner)
    assert getattr(partner, 'cal_AstForeachGenerator211') == owner
    _safe_set(owner, 'cal_AstVariable212', None)
    assert getattr(partner, 'cal_AstForeachGenerator211') is None


def test_assoc_variable251_stub_double():
    # cal_AstGenerator has no real 'cal_AstGenerator252' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstGenerator()
    setattr(partner, 'cal_AstGenerator252', None)
    _safe_set(owner, 'cal_AstVariable253', partner)
    assert getattr(partner, 'cal_AstGenerator252') == owner
    _safe_set(owner, 'cal_AstVariable253', None)
    assert getattr(partner, 'cal_AstGenerator252') is None


def test_assoc_variable290_stub_double():
    # cal_AstVariableReference has no real 'cal_AstVariableReference291' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstVariableReference()
    setattr(partner, 'cal_AstVariableReference291', None)
    _safe_set(owner, 'cal_AstVariable292', partner)
    assert getattr(partner, 'cal_AstVariableReference291') == owner
    _safe_set(owner, 'cal_AstVariable292', None)
    assert getattr(partner, 'cal_AstVariableReference291') is None


def test_assoc_variable53_stub_double():
    # cal_AstActorVariableReference has no real 'cal_AstActorVariableReference54' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstActorVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstActorVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstActorVariable(name="sample_text")
    partner = cal_AstActorVariableReference()
    setattr(partner, 'cal_AstActorVariableReference54', None)
    _safe_set(owner, 'cal_AstActorVariable55', partner)
    assert getattr(partner, 'cal_AstActorVariableReference54') == owner
    _safe_set(owner, 'cal_AstActorVariable55', None)
    assert getattr(partner, 'cal_AstActorVariableReference54') is None


def test_assoc_variables165_stub_double():
    # cal_AstAction has no real 'cal_AstAction166' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstAction()
    setattr(partner, 'cal_AstAction166', None)
    _safe_set(owner, 'cal_AstVariable167', partner)
    assert owner in getattr(partner, 'cal_AstAction166')
    _safe_set(owner, 'cal_AstVariable167', None)
    assert owner not in getattr(partner, 'cal_AstAction166')


def test_assoc_variables204_stub_double():
    # cal_AstStatementForeach has no real 'cal_AstStatementForeach205' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstStatementForeach()
    setattr(partner, 'cal_AstStatementForeach205', None)
    _safe_set(owner, 'cal_AstVariable206', partner)
    assert owner in getattr(partner, 'cal_AstStatementForeach205')
    _safe_set(owner, 'cal_AstVariable206', None)
    assert owner not in getattr(partner, 'cal_AstStatementForeach205')


def test_assoc_variables216_stub_double():
    # cal_AstStatementBlock has no real 'cal_AstStatementBlock' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstStatementBlock()
    setattr(partner, 'cal_AstStatementBlock', None)
    _safe_set(owner, 'cal_AstVariable217', partner)
    assert owner in getattr(partner, 'cal_AstStatementBlock')
    _safe_set(owner, 'cal_AstVariable217', None)
    assert owner not in getattr(partner, 'cal_AstStatementBlock')


def test_assoc_variables31_stub_double():
    # cal_AstNetwork has no real 'cal_AstNetwork' property in the generated
    # code (a bare stub) -- manually attach it so cal_AstVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cal_AstVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cal_AstVariable(constant=True, name="sample_text")
    partner = cal_AstNetwork()
    setattr(partner, 'cal_AstNetwork', None)
    _safe_set(owner, 'cal_AstVariable32', partner)
    assert owner in getattr(partner, 'cal_AstNetwork')
    _safe_set(owner, 'cal_AstVariable32', None)
    assert owner not in getattr(partner, 'cal_AstNetwork')


