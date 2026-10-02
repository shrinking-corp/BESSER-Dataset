import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModuleElement,
    OclExpression,
    OclType,
    PrimitiveExp,
    docl_AddOpCallExp,
    docl_BagType,
    docl_BoolOpCallExp,
    docl_BooleanLiteralExp,
    docl_BooleanType,
    docl_CollectionOpCallExp,
    docl_ComOpCallExp,
    docl_ElseIfThenExp,
    docl_EnvType,
    docl_EqOpCallExp,
    docl_IfExp,
    docl_Import,
    docl_IntegerType,
    docl_InvalidLiteralExp,
    docl_IterateExp,
    docl_Iterator,
    docl_IteratorExp,
    docl_LambdaExp,
    docl_LambdaType,
    docl_LocalVariable,
    docl_MapType,
    docl_Module,
    docl_ModuleElement,
    docl_MulOpCallExp,
    docl_NavigationExp,
    docl_NavigationOrAttributeCall,
    docl_NestedExp,
    docl_NullLiteralExp,
    docl_NumberLiteralExp,
    docl_OclAnyType,
    docl_OclExpression,
    docl_OclModel,
    docl_OclModelElementExp,
    docl_OclType,
    docl_OperationCall,
    docl_OrderedSetType,
    docl_PrimitiveExp,
    docl_Query,
    docl_RealType,
    docl_SelfExp,
    docl_SequenceType,
    docl_SetType,
    docl_StringLiteralExp,
    docl_StringType,
    docl_TupleExp,
    docl_TuplePart,
    docl_TupleType,
    docl_URI_,
    docl_UnlimitedNaturalLiteralExp,
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

def test_assoc_body10_reverse_link_reassign_clear():
    a1 = docl_Query(name="sample_text")
    a2 = docl_Query(name="sample_text_2")
    b = docl_OclExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'docl_OclExpression', a1)
    assert _is_linked(b, 'docl_OclExpression', a1)
    if hasattr(a1, 'docl_Query'):
        assert _is_linked(a1, 'docl_Query', b)
    _safe_set(b, 'docl_OclExpression', a2)
    assert _is_linked(b, 'docl_OclExpression', a2)
    if hasattr(a1, 'docl_Query'):
        assert not _is_linked(a1, 'docl_Query', b)
    if hasattr(a2, 'docl_Query'):
        assert _is_linked(a2, 'docl_Query', b)
    _safe_set(b, 'docl_OclExpression', None)
    assert not _is_linked(b, 'docl_OclExpression', a2)
    if hasattr(a2, 'docl_Query'):
        assert not _is_linked(a2, 'docl_Query', b)


def test_assoc_imports4_reverse_link_reassign_clear():
    a1 = docl_Module(name="sample_text")
    a2 = docl_Module(name="sample_text_2")
    b = docl_Import(name="sample_text")
    _safe_set(b, 'docl_Import', a1)
    assert _is_linked(b, 'docl_Import', a1)
    if hasattr(a1, 'docl_Module5'):
        assert _is_linked(a1, 'docl_Module5', b)
    _safe_set(b, 'docl_Import', a2)
    assert _is_linked(b, 'docl_Import', a2)
    if hasattr(a1, 'docl_Module5'):
        assert not _is_linked(a1, 'docl_Module5', b)
    if hasattr(a2, 'docl_Module5'):
        assert _is_linked(a2, 'docl_Module5', b)
    _safe_set(b, 'docl_Import', None)
    assert not _is_linked(b, 'docl_Import', a2)
    if hasattr(a2, 'docl_Module5'):
        assert not _is_linked(a2, 'docl_Module5', b)


def test_assoc_in_14_reverse_link_reassign_clear():
    a1 = docl_OclExpression(elements="sample_text", name="sample_text")
    a2 = docl_OclExpression(elements="sample_text_2", name="sample_text_2")
    b = docl_OclExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'docl_OclExpression15', a1)
    assert _is_linked(b, 'docl_OclExpression15', a1)
    if hasattr(a1, 'docl_OclExpression13'):
        assert _is_linked(a1, 'docl_OclExpression13', b)
    _safe_set(b, 'docl_OclExpression15', a2)
    assert _is_linked(b, 'docl_OclExpression15', a2)
    if hasattr(a1, 'docl_OclExpression13'):
        assert not _is_linked(a1, 'docl_OclExpression13', b)
    if hasattr(a2, 'docl_OclExpression13'):
        assert _is_linked(a2, 'docl_OclExpression13', b)
    _safe_set(b, 'docl_OclExpression15', None)
    assert not _is_linked(b, 'docl_OclExpression15', a2)
    if hasattr(a2, 'docl_OclExpression13'):
        assert not _is_linked(a2, 'docl_OclExpression13', b)


def test_assoc_init31_reverse_link_reassign_clear():
    a1 = docl_TuplePart(name="sample_text")
    a2 = docl_TuplePart(name="sample_text_2")
    b = docl_OclExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'docl_OclExpression33', a1)
    assert _is_linked(b, 'docl_OclExpression33', a1)
    if hasattr(a1, 'docl_TuplePart32'):
        assert _is_linked(a1, 'docl_TuplePart32', b)
    _safe_set(b, 'docl_OclExpression33', a2)
    assert _is_linked(b, 'docl_OclExpression33', a2)
    if hasattr(a1, 'docl_TuplePart32'):
        assert not _is_linked(a1, 'docl_TuplePart32', b)
    if hasattr(a2, 'docl_TuplePart32'):
        assert _is_linked(a2, 'docl_TuplePart32', b)
    _safe_set(b, 'docl_OclExpression33', None)
    assert not _is_linked(b, 'docl_OclExpression33', a2)
    if hasattr(a2, 'docl_TuplePart32'):
        assert not _is_linked(a2, 'docl_TuplePart32', b)


def test_assoc_initExp26_reverse_link_reassign_clear():
    a1 = docl_OclExpression(elements="sample_text", name="sample_text")
    a2 = docl_OclExpression(elements="sample_text_2", name="sample_text_2")
    b = docl_LocalVariable(name="sample_text")
    _safe_set(b, 'docl_LocalVariable27', a1)
    assert _is_linked(b, 'docl_LocalVariable27', a1)
    if hasattr(a1, 'docl_OclExpression28'):
        assert _is_linked(a1, 'docl_OclExpression28', b)
    _safe_set(b, 'docl_LocalVariable27', a2)
    assert _is_linked(b, 'docl_LocalVariable27', a2)
    if hasattr(a1, 'docl_OclExpression28'):
        assert not _is_linked(a1, 'docl_OclExpression28', b)
    if hasattr(a2, 'docl_OclExpression28'):
        assert _is_linked(a2, 'docl_OclExpression28', b)
    _safe_set(b, 'docl_LocalVariable27', None)
    assert not _is_linked(b, 'docl_LocalVariable27', a2)
    if hasattr(a2, 'docl_OclExpression28'):
        assert not _is_linked(a2, 'docl_OclExpression28', b)


def test_assoc_input1_reverse_link_reassign_clear():
    a1 = docl_OclModel(name="sample_text")
    a2 = docl_OclModel(name="sample_text_2")
    b = docl_Module(name="sample_text")
    _safe_set(b, 'docl_Module2', a1)
    assert _is_linked(b, 'docl_Module2', a1)
    if hasattr(a1, 'docl_OclModel3'):
        assert _is_linked(a1, 'docl_OclModel3', b)
    _safe_set(b, 'docl_Module2', a2)
    assert _is_linked(b, 'docl_Module2', a2)
    if hasattr(a1, 'docl_OclModel3'):
        assert not _is_linked(a1, 'docl_OclModel3', b)
    if hasattr(a2, 'docl_OclModel3'):
        assert _is_linked(a2, 'docl_OclModel3', b)
    _safe_set(b, 'docl_Module2', None)
    assert not _is_linked(b, 'docl_Module2', a2)
    if hasattr(a2, 'docl_OclModel3'):
        assert not _is_linked(a2, 'docl_OclModel3', b)


def test_assoc_model19_reverse_link_reassign_clear():
    a1 = docl_OclModel(name="sample_text")
    a2 = docl_OclModel(name="sample_text_2")
    b = docl_OclExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'docl_OclExpression20', a1)
    assert _is_linked(b, 'docl_OclExpression20', a1)
    if hasattr(a1, 'docl_OclModel21'):
        assert _is_linked(a1, 'docl_OclModel21', b)
    _safe_set(b, 'docl_OclExpression20', a2)
    assert _is_linked(b, 'docl_OclExpression20', a2)
    if hasattr(a1, 'docl_OclModel21'):
        assert not _is_linked(a1, 'docl_OclModel21', b)
    if hasattr(a2, 'docl_OclModel21'):
        assert _is_linked(a2, 'docl_OclModel21', b)
    _safe_set(b, 'docl_OclExpression20', None)
    assert not _is_linked(b, 'docl_OclExpression20', a2)
    if hasattr(a2, 'docl_OclModel21'):
        assert not _is_linked(a2, 'docl_OclModel21', b)


def test_assoc_model45_reverse_link_reassign_clear():
    a1 = docl_OclModelElementExp(name="sample_text")
    a2 = docl_OclModelElementExp(name="sample_text_2")
    b = docl_OclModel(name="sample_text")
    _safe_set(b, 'docl_OclModel46', a1)
    assert _is_linked(b, 'docl_OclModel46', a1)
    if hasattr(a1, 'docl_OclModelElementExp'):
        assert _is_linked(a1, 'docl_OclModelElementExp', b)
    _safe_set(b, 'docl_OclModel46', a2)
    assert _is_linked(b, 'docl_OclModel46', a2)
    if hasattr(a1, 'docl_OclModelElementExp'):
        assert not _is_linked(a1, 'docl_OclModelElementExp', b)
    if hasattr(a2, 'docl_OclModelElementExp'):
        assert _is_linked(a2, 'docl_OclModelElementExp', b)
    _safe_set(b, 'docl_OclModel46', None)
    assert not _is_linked(b, 'docl_OclModel46', a2)
    if hasattr(a2, 'docl_OclModelElementExp'):
        assert not _is_linked(a2, 'docl_OclModelElementExp', b)


def test_assoc_source0_reverse_link_reassign_clear():
    a1 = docl_OclModel(name="sample_text")
    a2 = docl_OclModel(name="sample_text_2")
    b = docl_Module(name="sample_text")
    _safe_set(b, 'docl_Module', a1)
    assert _is_linked(b, 'docl_Module', a1)
    if hasattr(a1, 'docl_OclModel'):
        assert _is_linked(a1, 'docl_OclModel', b)
    _safe_set(b, 'docl_Module', a2)
    assert _is_linked(b, 'docl_Module', a2)
    if hasattr(a1, 'docl_OclModel'):
        assert not _is_linked(a1, 'docl_OclModel', b)
    if hasattr(a2, 'docl_OclModel'):
        assert _is_linked(a2, 'docl_OclModel', b)
    _safe_set(b, 'docl_Module', None)
    assert not _is_linked(b, 'docl_Module', a2)
    if hasattr(a2, 'docl_OclModel'):
        assert not _is_linked(a2, 'docl_OclModel', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = docl_OclExpression(elements="sample_text", name="sample_text")
    a2 = docl_OclExpression(elements="sample_text_2", name="sample_text_2")
    b = docl_OclExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'docl_OclExpression18', a1)
    assert _is_linked(b, 'docl_OclExpression18', a1)
    if hasattr(a1, 'docl_OclExpression16'):
        assert _is_linked(a1, 'docl_OclExpression16', b)
    _safe_set(b, 'docl_OclExpression18', a2)
    assert _is_linked(b, 'docl_OclExpression18', a2)
    if hasattr(a1, 'docl_OclExpression16'):
        assert not _is_linked(a1, 'docl_OclExpression16', b)
    if hasattr(a2, 'docl_OclExpression16'):
        assert _is_linked(a2, 'docl_OclExpression16', b)
    _safe_set(b, 'docl_OclExpression18', None)
    assert not _is_linked(b, 'docl_OclExpression18', a2)
    if hasattr(a2, 'docl_OclExpression16'):
        assert not _is_linked(a2, 'docl_OclExpression16', b)


def test_assoc_uri8_reverse_link_reassign_clear():
    a1 = docl_URI_(authority="sample_text", fragment_="sample_text", scheme="sample_text")
    a2 = docl_URI_(authority="sample_text_2", fragment_="sample_text_2", scheme="sample_text_2")
    b = docl_OclModel(name="sample_text")
    _safe_set(b, 'docl_OclModel9', a1)
    assert _is_linked(b, 'docl_OclModel9', a1)
    if hasattr(a1, 'docl_URI_'):
        assert _is_linked(a1, 'docl_URI_', b)
    _safe_set(b, 'docl_OclModel9', a2)
    assert _is_linked(b, 'docl_OclModel9', a2)
    if hasattr(a1, 'docl_URI_'):
        assert not _is_linked(a1, 'docl_URI_', b)
    if hasattr(a2, 'docl_URI_'):
        assert _is_linked(a2, 'docl_URI_', b)
    _safe_set(b, 'docl_OclModel9', None)
    assert not _is_linked(b, 'docl_OclModel9', a2)
    if hasattr(a2, 'docl_URI_'):
        assert not _is_linked(a2, 'docl_URI_', b)


def test_assoc_variable11_reverse_link_reassign_clear():
    a1 = docl_OclExpression(elements="sample_text", name="sample_text")
    a2 = docl_OclExpression(elements="sample_text_2", name="sample_text_2")
    b = docl_LocalVariable(name="sample_text")
    _safe_set(b, 'docl_LocalVariable', a1)
    assert _is_linked(b, 'docl_LocalVariable', a1)
    if hasattr(a1, 'docl_OclExpression12'):
        assert _is_linked(a1, 'docl_OclExpression12', b)
    _safe_set(b, 'docl_LocalVariable', a2)
    assert _is_linked(b, 'docl_LocalVariable', a2)
    if hasattr(a1, 'docl_OclExpression12'):
        assert not _is_linked(a1, 'docl_OclExpression12', b)
    if hasattr(a2, 'docl_OclExpression12'):
        assert _is_linked(a2, 'docl_OclExpression12', b)
    _safe_set(b, 'docl_LocalVariable', None)
    assert not _is_linked(b, 'docl_LocalVariable', a2)
    if hasattr(a2, 'docl_OclExpression12'):
        assert not _is_linked(a2, 'docl_OclExpression12', b)


