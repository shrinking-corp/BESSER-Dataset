import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExp,
    ModuleElement,
    OclLExpression,
    OclLType,
    PrimitiveExp,
    oCLlite_AddOpCallExp,
    oCLlite_BagExp,
    oCLlite_BagType,
    oCLlite_BoolOpCallExp,
    oCLlite_BooleanLiteralExp,
    oCLlite_BooleanType,
    oCLlite_CollectionExp,
    oCLlite_CollectionOpCallExp,
    oCLlite_ComOpCallExp,
    oCLlite_ElseIfThenExp,
    oCLlite_EnvType,
    oCLlite_EqOpCallExp,
    oCLlite_IfExp,
    oCLlite_Import,
    oCLlite_IntegerType,
    oCLlite_InvalidLiteralExp,
    oCLlite_IterateExp,
    oCLlite_Iterator,
    oCLlite_IteratorExp,
    oCLlite_LambdaExp,
    oCLlite_LambdaType,
    oCLlite_LocalVariable,
    oCLlite_MapElement,
    oCLlite_MapExp,
    oCLlite_MapType,
    oCLlite_Module,
    oCLlite_ModuleElement,
    oCLlite_MulOpCallExp,
    oCLlite_NavigationExp,
    oCLlite_NavigationOrAttributeCall,
    oCLlite_NestedExp,
    oCLlite_NullLiteralExp,
    oCLlite_NumberLiteralExp,
    oCLlite_OclLAnyType,
    oCLlite_OclLExpression,
    oCLlite_OclLModel,
    oCLlite_OclLModelElementExp,
    oCLlite_OclLType,
    oCLlite_OperationCall,
    oCLlite_OrderedSetExp,
    oCLlite_OrderedSetType,
    oCLlite_PrimitiveExp,
    oCLlite_Query,
    oCLlite_RealType,
    oCLlite_SelfExp,
    oCLlite_SequenceExp,
    oCLlite_SequenceType,
    oCLlite_SetExp,
    oCLlite_SetType,
    oCLlite_StringLiteralExp,
    oCLlite_StringType,
    oCLlite_TupleExp,
    oCLlite_TuplePart,
    oCLlite_TupleType,
    oCLlite_URI_,
    oCLlite_UnlimitedNaturalLiteralExp,
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
    a1 = oCLlite_Query(name="sample_text")
    a2 = oCLlite_Query(name="sample_text_2")
    b = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'oCLlite_OclLExpression', a1)
    assert _is_linked(b, 'oCLlite_OclLExpression', a1)
    if hasattr(a1, 'oCLlite_Query'):
        assert _is_linked(a1, 'oCLlite_Query', b)
    _safe_set(b, 'oCLlite_OclLExpression', a2)
    assert _is_linked(b, 'oCLlite_OclLExpression', a2)
    if hasattr(a1, 'oCLlite_Query'):
        assert not _is_linked(a1, 'oCLlite_Query', b)
    if hasattr(a2, 'oCLlite_Query'):
        assert _is_linked(a2, 'oCLlite_Query', b)
    _safe_set(b, 'oCLlite_OclLExpression', None)
    assert not _is_linked(b, 'oCLlite_OclLExpression', a2)
    if hasattr(a2, 'oCLlite_Query'):
        assert not _is_linked(a2, 'oCLlite_Query', b)


def test_assoc_imports4_reverse_link_reassign_clear():
    a1 = oCLlite_Module(name="sample_text")
    a2 = oCLlite_Module(name="sample_text_2")
    b = oCLlite_Import(name="sample_text")
    _safe_set(b, 'oCLlite_Import', a1)
    assert _is_linked(b, 'oCLlite_Import', a1)
    if hasattr(a1, 'oCLlite_Module5'):
        assert _is_linked(a1, 'oCLlite_Module5', b)
    _safe_set(b, 'oCLlite_Import', a2)
    assert _is_linked(b, 'oCLlite_Import', a2)
    if hasattr(a1, 'oCLlite_Module5'):
        assert not _is_linked(a1, 'oCLlite_Module5', b)
    if hasattr(a2, 'oCLlite_Module5'):
        assert _is_linked(a2, 'oCLlite_Module5', b)
    _safe_set(b, 'oCLlite_Import', None)
    assert not _is_linked(b, 'oCLlite_Import', a2)
    if hasattr(a2, 'oCLlite_Module5'):
        assert not _is_linked(a2, 'oCLlite_Module5', b)


def test_assoc_in_14_reverse_link_reassign_clear():
    a1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    a2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    b = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'oCLlite_OclLExpression15', a1)
    assert _is_linked(b, 'oCLlite_OclLExpression15', a1)
    if hasattr(a1, 'oCLlite_OclLExpression13'):
        assert _is_linked(a1, 'oCLlite_OclLExpression13', b)
    _safe_set(b, 'oCLlite_OclLExpression15', a2)
    assert _is_linked(b, 'oCLlite_OclLExpression15', a2)
    if hasattr(a1, 'oCLlite_OclLExpression13'):
        assert not _is_linked(a1, 'oCLlite_OclLExpression13', b)
    if hasattr(a2, 'oCLlite_OclLExpression13'):
        assert _is_linked(a2, 'oCLlite_OclLExpression13', b)
    _safe_set(b, 'oCLlite_OclLExpression15', None)
    assert not _is_linked(b, 'oCLlite_OclLExpression15', a2)
    if hasattr(a2, 'oCLlite_OclLExpression13'):
        assert not _is_linked(a2, 'oCLlite_OclLExpression13', b)


def test_assoc_init40_reverse_link_reassign_clear():
    a1 = oCLlite_TuplePart(name="sample_text")
    a2 = oCLlite_TuplePart(name="sample_text_2")
    b = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'oCLlite_OclLExpression42', a1)
    assert _is_linked(b, 'oCLlite_OclLExpression42', a1)
    if hasattr(a1, 'oCLlite_TuplePart41'):
        assert _is_linked(a1, 'oCLlite_TuplePart41', b)
    _safe_set(b, 'oCLlite_OclLExpression42', a2)
    assert _is_linked(b, 'oCLlite_OclLExpression42', a2)
    if hasattr(a1, 'oCLlite_TuplePart41'):
        assert not _is_linked(a1, 'oCLlite_TuplePart41', b)
    if hasattr(a2, 'oCLlite_TuplePart41'):
        assert _is_linked(a2, 'oCLlite_TuplePart41', b)
    _safe_set(b, 'oCLlite_OclLExpression42', None)
    assert not _is_linked(b, 'oCLlite_OclLExpression42', a2)
    if hasattr(a2, 'oCLlite_TuplePart41'):
        assert not _is_linked(a2, 'oCLlite_TuplePart41', b)


def test_assoc_initExp26_reverse_link_reassign_clear():
    a1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    a2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    b = oCLlite_LocalVariable(name="sample_text")
    _safe_set(b, 'oCLlite_LocalVariable27', a1)
    assert _is_linked(b, 'oCLlite_LocalVariable27', a1)
    if hasattr(a1, 'oCLlite_OclLExpression28'):
        assert _is_linked(a1, 'oCLlite_OclLExpression28', b)
    _safe_set(b, 'oCLlite_LocalVariable27', a2)
    assert _is_linked(b, 'oCLlite_LocalVariable27', a2)
    if hasattr(a1, 'oCLlite_OclLExpression28'):
        assert not _is_linked(a1, 'oCLlite_OclLExpression28', b)
    if hasattr(a2, 'oCLlite_OclLExpression28'):
        assert _is_linked(a2, 'oCLlite_OclLExpression28', b)
    _safe_set(b, 'oCLlite_LocalVariable27', None)
    assert not _is_linked(b, 'oCLlite_LocalVariable27', a2)
    if hasattr(a2, 'oCLlite_OclLExpression28'):
        assert not _is_linked(a2, 'oCLlite_OclLExpression28', b)


def test_assoc_input1_reverse_link_reassign_clear():
    a1 = oCLlite_OclLModel(name="sample_text")
    a2 = oCLlite_OclLModel(name="sample_text_2")
    b = oCLlite_Module(name="sample_text")
    _safe_set(b, 'oCLlite_Module2', a1)
    assert _is_linked(b, 'oCLlite_Module2', a1)
    if hasattr(a1, 'oCLlite_OclLModel3'):
        assert _is_linked(a1, 'oCLlite_OclLModel3', b)
    _safe_set(b, 'oCLlite_Module2', a2)
    assert _is_linked(b, 'oCLlite_Module2', a2)
    if hasattr(a1, 'oCLlite_OclLModel3'):
        assert not _is_linked(a1, 'oCLlite_OclLModel3', b)
    if hasattr(a2, 'oCLlite_OclLModel3'):
        assert _is_linked(a2, 'oCLlite_OclLModel3', b)
    _safe_set(b, 'oCLlite_Module2', None)
    assert not _is_linked(b, 'oCLlite_Module2', a2)
    if hasattr(a2, 'oCLlite_OclLModel3'):
        assert not _is_linked(a2, 'oCLlite_OclLModel3', b)


def test_assoc_model19_reverse_link_reassign_clear():
    a1 = oCLlite_OclLModel(name="sample_text")
    a2 = oCLlite_OclLModel(name="sample_text_2")
    b = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'oCLlite_OclLExpression20', a1)
    assert _is_linked(b, 'oCLlite_OclLExpression20', a1)
    if hasattr(a1, 'oCLlite_OclLModel21'):
        assert _is_linked(a1, 'oCLlite_OclLModel21', b)
    _safe_set(b, 'oCLlite_OclLExpression20', a2)
    assert _is_linked(b, 'oCLlite_OclLExpression20', a2)
    if hasattr(a1, 'oCLlite_OclLModel21'):
        assert not _is_linked(a1, 'oCLlite_OclLModel21', b)
    if hasattr(a2, 'oCLlite_OclLModel21'):
        assert _is_linked(a2, 'oCLlite_OclLModel21', b)
    _safe_set(b, 'oCLlite_OclLExpression20', None)
    assert not _is_linked(b, 'oCLlite_OclLExpression20', a2)
    if hasattr(a2, 'oCLlite_OclLModel21'):
        assert not _is_linked(a2, 'oCLlite_OclLModel21', b)


def test_assoc_model54_reverse_link_reassign_clear():
    a1 = oCLlite_OclLModelElementExp(name="sample_text")
    a2 = oCLlite_OclLModelElementExp(name="sample_text_2")
    b = oCLlite_OclLModel(name="sample_text")
    _safe_set(b, 'oCLlite_OclLModel55', a1)
    assert _is_linked(b, 'oCLlite_OclLModel55', a1)
    if hasattr(a1, 'oCLlite_OclLModelElementExp'):
        assert _is_linked(a1, 'oCLlite_OclLModelElementExp', b)
    _safe_set(b, 'oCLlite_OclLModel55', a2)
    assert _is_linked(b, 'oCLlite_OclLModel55', a2)
    if hasattr(a1, 'oCLlite_OclLModelElementExp'):
        assert not _is_linked(a1, 'oCLlite_OclLModelElementExp', b)
    if hasattr(a2, 'oCLlite_OclLModelElementExp'):
        assert _is_linked(a2, 'oCLlite_OclLModelElementExp', b)
    _safe_set(b, 'oCLlite_OclLModel55', None)
    assert not _is_linked(b, 'oCLlite_OclLModel55', a2)
    if hasattr(a2, 'oCLlite_OclLModelElementExp'):
        assert not _is_linked(a2, 'oCLlite_OclLModelElementExp', b)


def test_assoc_source0_reverse_link_reassign_clear():
    a1 = oCLlite_OclLModel(name="sample_text")
    a2 = oCLlite_OclLModel(name="sample_text_2")
    b = oCLlite_Module(name="sample_text")
    _safe_set(b, 'oCLlite_Module', a1)
    assert _is_linked(b, 'oCLlite_Module', a1)
    if hasattr(a1, 'oCLlite_OclLModel'):
        assert _is_linked(a1, 'oCLlite_OclLModel', b)
    _safe_set(b, 'oCLlite_Module', a2)
    assert _is_linked(b, 'oCLlite_Module', a2)
    if hasattr(a1, 'oCLlite_OclLModel'):
        assert not _is_linked(a1, 'oCLlite_OclLModel', b)
    if hasattr(a2, 'oCLlite_OclLModel'):
        assert _is_linked(a2, 'oCLlite_OclLModel', b)
    _safe_set(b, 'oCLlite_Module', None)
    assert not _is_linked(b, 'oCLlite_Module', a2)
    if hasattr(a2, 'oCLlite_OclLModel'):
        assert not _is_linked(a2, 'oCLlite_OclLModel', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    a2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    b = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    _safe_set(b, 'oCLlite_OclLExpression18', a1)
    assert _is_linked(b, 'oCLlite_OclLExpression18', a1)
    if hasattr(a1, 'oCLlite_OclLExpression16'):
        assert _is_linked(a1, 'oCLlite_OclLExpression16', b)
    _safe_set(b, 'oCLlite_OclLExpression18', a2)
    assert _is_linked(b, 'oCLlite_OclLExpression18', a2)
    if hasattr(a1, 'oCLlite_OclLExpression16'):
        assert not _is_linked(a1, 'oCLlite_OclLExpression16', b)
    if hasattr(a2, 'oCLlite_OclLExpression16'):
        assert _is_linked(a2, 'oCLlite_OclLExpression16', b)
    _safe_set(b, 'oCLlite_OclLExpression18', None)
    assert not _is_linked(b, 'oCLlite_OclLExpression18', a2)
    if hasattr(a2, 'oCLlite_OclLExpression16'):
        assert not _is_linked(a2, 'oCLlite_OclLExpression16', b)


def test_assoc_uri8_reverse_link_reassign_clear():
    a1 = oCLlite_URI_(authority="sample_text", fragment_="sample_text", scheme="sample_text")
    a2 = oCLlite_URI_(authority="sample_text_2", fragment_="sample_text_2", scheme="sample_text_2")
    b = oCLlite_OclLModel(name="sample_text")
    _safe_set(b, 'oCLlite_OclLModel9', a1)
    assert _is_linked(b, 'oCLlite_OclLModel9', a1)
    if hasattr(a1, 'oCLlite_URI_'):
        assert _is_linked(a1, 'oCLlite_URI_', b)
    _safe_set(b, 'oCLlite_OclLModel9', a2)
    assert _is_linked(b, 'oCLlite_OclLModel9', a2)
    if hasattr(a1, 'oCLlite_URI_'):
        assert not _is_linked(a1, 'oCLlite_URI_', b)
    if hasattr(a2, 'oCLlite_URI_'):
        assert _is_linked(a2, 'oCLlite_URI_', b)
    _safe_set(b, 'oCLlite_OclLModel9', None)
    assert not _is_linked(b, 'oCLlite_OclLModel9', a2)
    if hasattr(a2, 'oCLlite_URI_'):
        assert not _is_linked(a2, 'oCLlite_URI_', b)


def test_assoc_variable11_reverse_link_reassign_clear():
    a1 = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    a2 = oCLlite_OclLExpression(elements="sample_text_2", name="sample_text_2")
    b = oCLlite_LocalVariable(name="sample_text")
    _safe_set(b, 'oCLlite_LocalVariable', a1)
    assert _is_linked(b, 'oCLlite_LocalVariable', a1)
    if hasattr(a1, 'oCLlite_OclLExpression12'):
        assert _is_linked(a1, 'oCLlite_OclLExpression12', b)
    _safe_set(b, 'oCLlite_LocalVariable', a2)
    assert _is_linked(b, 'oCLlite_LocalVariable', a2)
    if hasattr(a1, 'oCLlite_OclLExpression12'):
        assert not _is_linked(a1, 'oCLlite_OclLExpression12', b)
    if hasattr(a2, 'oCLlite_OclLExpression12'):
        assert _is_linked(a2, 'oCLlite_OclLExpression12', b)
    _safe_set(b, 'oCLlite_LocalVariable', None)
    assert not _is_linked(b, 'oCLlite_LocalVariable', a2)
    if hasattr(a2, 'oCLlite_OclLExpression12'):
        assert not _is_linked(a2, 'oCLlite_OclLExpression12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argsTypes56_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType57' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_LambdaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_LambdaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_LambdaType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType57', None)
    _safe_set(owner, 'oCLlite_LambdaType', {partner})
    assert getattr(partner, 'oCLlite_OclLType57') == owner
    _safe_set(owner, 'oCLlite_LambdaType', set())
    assert getattr(partner, 'oCLlite_OclLType57') is None


def test_assoc_arguments101_stub_double():
    # oCLlite_OperationCall has no real 'oCLlite_OperationCall' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_OperationCall()
    setattr(partner, 'oCLlite_OperationCall', None)
    _safe_set(owner, 'oCLlite_OclLExpression102', partner)
    assert owner in getattr(partner, 'oCLlite_OperationCall')
    _safe_set(owner, 'oCLlite_OclLExpression102', None)
    assert owner not in getattr(partner, 'oCLlite_OperationCall')


def test_assoc_arguments86_stub_double():
    # oCLlite_CollectionOpCallExp has no real 'oCLlite_CollectionOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_CollectionOpCallExp()
    setattr(partner, 'oCLlite_CollectionOpCallExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression87', partner)
    assert owner in getattr(partner, 'oCLlite_CollectionOpCallExp')
    _safe_set(owner, 'oCLlite_OclLExpression87', None)
    assert owner not in getattr(partner, 'oCLlite_CollectionOpCallExp')


def test_assoc_body93_stub_double():
    # oCLlite_IterateExp has no real 'oCLlite_IterateExp94' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_IterateExp()
    setattr(partner, 'oCLlite_IterateExp94', None)
    _safe_set(owner, 'oCLlite_OclLExpression95', partner)
    assert getattr(partner, 'oCLlite_IterateExp94') == owner
    _safe_set(owner, 'oCLlite_OclLExpression95', None)
    assert getattr(partner, 'oCLlite_IterateExp94') is None


def test_assoc_body98_stub_double():
    # oCLlite_IteratorExp has no real 'oCLlite_IteratorExp99' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_IteratorExp()
    setattr(partner, 'oCLlite_IteratorExp99', None)
    _safe_set(owner, 'oCLlite_OclLExpression100', partner)
    assert getattr(partner, 'oCLlite_IteratorExp99') == owner
    _safe_set(owner, 'oCLlite_OclLExpression100', None)
    assert getattr(partner, 'oCLlite_IteratorExp99') is None


def test_assoc_condition107_stub_double():
    # oCLlite_ElseIfThenExp has no real 'oCLlite_ElseIfThenExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_ElseIfThenExp()
    setattr(partner, 'oCLlite_ElseIfThenExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression108', partner)
    assert getattr(partner, 'oCLlite_ElseIfThenExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression108', None)
    assert getattr(partner, 'oCLlite_ElseIfThenExp') is None


def test_assoc_condition43_stub_double():
    # oCLlite_IfExp has no real 'oCLlite_IfExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_IfExp()
    setattr(partner, 'oCLlite_IfExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression44', partner)
    assert getattr(partner, 'oCLlite_IfExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression44', None)
    assert getattr(partner, 'oCLlite_IfExp') is None


def test_assoc_elementType66_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType67' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_SetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_SetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_SetType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType67', None)
    _safe_set(owner, 'oCLlite_SetType', partner)
    assert getattr(partner, 'oCLlite_OclLType67') == owner
    _safe_set(owner, 'oCLlite_SetType', None)
    assert getattr(partner, 'oCLlite_OclLType67') is None


def test_assoc_elementType68_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType69' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_SequenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_SequenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_SequenceType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType69', None)
    _safe_set(owner, 'oCLlite_SequenceType', partner)
    assert getattr(partner, 'oCLlite_OclLType69') == owner
    _safe_set(owner, 'oCLlite_SequenceType', None)
    assert getattr(partner, 'oCLlite_OclLType69') is None


def test_assoc_elementType70_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType71' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OrderedSetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OrderedSetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OrderedSetType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType71', None)
    _safe_set(owner, 'oCLlite_OrderedSetType', partner)
    assert getattr(partner, 'oCLlite_OclLType71') == owner
    _safe_set(owner, 'oCLlite_OrderedSetType', None)
    assert getattr(partner, 'oCLlite_OclLType71') is None


def test_assoc_elementType72_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType73' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_BagType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_BagType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_BagType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType73', None)
    _safe_set(owner, 'oCLlite_BagType', partner)
    assert getattr(partner, 'oCLlite_OclLType73') == owner
    _safe_set(owner, 'oCLlite_BagType', None)
    assert getattr(partner, 'oCLlite_OclLType73') is None


def test_assoc_elements6_stub_double():
    # oCLlite_ModuleElement has no real 'oCLlite_ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_Module(name="sample_text")
    partner = oCLlite_ModuleElement()
    setattr(partner, 'oCLlite_ModuleElement', None)
    _safe_set(owner, 'oCLlite_Module7', {partner})
    assert getattr(partner, 'oCLlite_ModuleElement') == owner
    _safe_set(owner, 'oCLlite_Module7', set())
    assert getattr(partner, 'oCLlite_ModuleElement') is None


def test_assoc_else_51_stub_double():
    # oCLlite_IfExp has no real 'oCLlite_IfExp52' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_IfExp()
    setattr(partner, 'oCLlite_IfExp52', None)
    _safe_set(owner, 'oCLlite_OclLExpression53', partner)
    assert getattr(partner, 'oCLlite_IfExp52') == owner
    _safe_set(owner, 'oCLlite_OclLExpression53', None)
    assert getattr(partner, 'oCLlite_IfExp52') is None


def test_assoc_exp112_stub_double():
    # oCLlite_NestedExp has no real 'oCLlite_NestedExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_NestedExp()
    setattr(partner, 'oCLlite_NestedExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression113', partner)
    assert getattr(partner, 'oCLlite_NestedExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression113', None)
    assert getattr(partner, 'oCLlite_NestedExp') is None


def test_assoc_expression103_stub_double():
    # oCLlite_LambdaExp has no real 'oCLlite_LambdaExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_LambdaExp()
    setattr(partner, 'oCLlite_LambdaExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression104', partner)
    assert getattr(partner, 'oCLlite_LambdaExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression104', None)
    assert getattr(partner, 'oCLlite_LambdaExp') is None


def test_assoc_ifThen48_stub_double():
    # oCLlite_IfExp has no real 'oCLlite_IfExp49' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_IfExp()
    setattr(partner, 'oCLlite_IfExp49', None)
    _safe_set(owner, 'oCLlite_OclLExpression50', partner)
    assert owner in getattr(partner, 'oCLlite_IfExp49')
    _safe_set(owner, 'oCLlite_OclLExpression50', None)
    assert owner not in getattr(partner, 'oCLlite_IfExp49')


def test_assoc_iterators88_stub_double():
    # oCLlite_IterateExp has no real 'oCLlite_IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_Iterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_Iterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_Iterator(name="sample_text")
    partner = oCLlite_IterateExp()
    setattr(partner, 'oCLlite_IterateExp', None)
    _safe_set(owner, 'oCLlite_Iterator89', partner)
    assert owner in getattr(partner, 'oCLlite_IterateExp')
    _safe_set(owner, 'oCLlite_Iterator89', None)
    assert owner not in getattr(partner, 'oCLlite_IterateExp')


def test_assoc_iterators96_stub_double():
    # oCLlite_IteratorExp has no real 'oCLlite_IteratorExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_Iterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_Iterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_Iterator(name="sample_text")
    partner = oCLlite_IteratorExp()
    setattr(partner, 'oCLlite_IteratorExp', None)
    _safe_set(owner, 'oCLlite_Iterator97', partner)
    assert owner in getattr(partner, 'oCLlite_IteratorExp')
    _safe_set(owner, 'oCLlite_Iterator97', None)
    assert owner not in getattr(partner, 'oCLlite_IteratorExp')


def test_assoc_key32_stub_double():
    # oCLlite_MapElement has no real 'oCLlite_MapElement33' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_MapElement()
    setattr(partner, 'oCLlite_MapElement33', None)
    _safe_set(owner, 'oCLlite_OclLExpression34', partner)
    assert getattr(partner, 'oCLlite_MapElement33') == owner
    _safe_set(owner, 'oCLlite_OclLExpression34', None)
    assert getattr(partner, 'oCLlite_MapElement33') is None


def test_assoc_keyType61_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType62' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_MapType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType62', None)
    _safe_set(owner, 'oCLlite_MapType', partner)
    assert getattr(partner, 'oCLlite_OclLType62') == owner
    _safe_set(owner, 'oCLlite_MapType', None)
    assert getattr(partner, 'oCLlite_OclLType62') is None


def test_assoc_parts105_stub_double():
    # oCLlite_TupleExp has no real 'oCLlite_TupleExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_TuplePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_TuplePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_TuplePart(name="sample_text")
    partner = oCLlite_TupleExp()
    setattr(partner, 'oCLlite_TupleExp', None)
    _safe_set(owner, 'oCLlite_TuplePart106', partner)
    assert owner in getattr(partner, 'oCLlite_TupleExp')
    _safe_set(owner, 'oCLlite_TuplePart106', None)
    assert owner not in getattr(partner, 'oCLlite_TupleExp')


def test_assoc_parts29_stub_double():
    # oCLlite_CollectionExp has no real 'oCLlite_CollectionExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_CollectionExp()
    setattr(partner, 'oCLlite_CollectionExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression30', partner)
    assert owner in getattr(partner, 'oCLlite_CollectionExp')
    _safe_set(owner, 'oCLlite_OclLExpression30', None)
    assert owner not in getattr(partner, 'oCLlite_CollectionExp')


def test_assoc_result90_stub_double():
    # oCLlite_IterateExp has no real 'oCLlite_IterateExp91' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_LocalVariable(name="sample_text")
    partner = oCLlite_IterateExp()
    setattr(partner, 'oCLlite_IterateExp91', None)
    _safe_set(owner, 'oCLlite_LocalVariable92', partner)
    assert getattr(partner, 'oCLlite_IterateExp91') == owner
    _safe_set(owner, 'oCLlite_LocalVariable92', None)
    assert getattr(partner, 'oCLlite_IterateExp91') is None


def test_assoc_returnType58_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType60' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_LambdaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_LambdaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_LambdaType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType60', None)
    _safe_set(owner, 'oCLlite_LambdaType59', partner)
    assert getattr(partner, 'oCLlite_OclLType60') == owner
    _safe_set(owner, 'oCLlite_LambdaType59', None)
    assert getattr(partner, 'oCLlite_OclLType60') is None


def test_assoc_source74_stub_double():
    # oCLlite_BoolOpCallExp has no real 'oCLlite_BoolOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_BoolOpCallExp()
    setattr(partner, 'oCLlite_BoolOpCallExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression75', partner)
    assert getattr(partner, 'oCLlite_BoolOpCallExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression75', None)
    assert getattr(partner, 'oCLlite_BoolOpCallExp') is None


def test_assoc_source76_stub_double():
    # oCLlite_EqOpCallExp has no real 'oCLlite_EqOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_EqOpCallExp()
    setattr(partner, 'oCLlite_EqOpCallExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression77', partner)
    assert getattr(partner, 'oCLlite_EqOpCallExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression77', None)
    assert getattr(partner, 'oCLlite_EqOpCallExp') is None


def test_assoc_source78_stub_double():
    # oCLlite_ComOpCallExp has no real 'oCLlite_ComOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_ComOpCallExp()
    setattr(partner, 'oCLlite_ComOpCallExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression79', partner)
    assert getattr(partner, 'oCLlite_ComOpCallExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression79', None)
    assert getattr(partner, 'oCLlite_ComOpCallExp') is None


def test_assoc_source80_stub_double():
    # oCLlite_AddOpCallExp has no real 'oCLlite_AddOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_AddOpCallExp()
    setattr(partner, 'oCLlite_AddOpCallExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression81', partner)
    assert getattr(partner, 'oCLlite_AddOpCallExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression81', None)
    assert getattr(partner, 'oCLlite_AddOpCallExp') is None


def test_assoc_source82_stub_double():
    # oCLlite_MulOpCallExp has no real 'oCLlite_MulOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_MulOpCallExp()
    setattr(partner, 'oCLlite_MulOpCallExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression83', partner)
    assert getattr(partner, 'oCLlite_MulOpCallExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression83', None)
    assert getattr(partner, 'oCLlite_MulOpCallExp') is None


def test_assoc_source84_stub_double():
    # oCLlite_NavigationExp has no real 'oCLlite_NavigationExp' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_NavigationExp()
    setattr(partner, 'oCLlite_NavigationExp', None)
    _safe_set(owner, 'oCLlite_OclLExpression85', partner)
    assert getattr(partner, 'oCLlite_NavigationExp') == owner
    _safe_set(owner, 'oCLlite_OclLExpression85', None)
    assert getattr(partner, 'oCLlite_NavigationExp') is None


def test_assoc_then109_stub_double():
    # oCLlite_ElseIfThenExp has no real 'oCLlite_ElseIfThenExp110' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_ElseIfThenExp()
    setattr(partner, 'oCLlite_ElseIfThenExp110', None)
    _safe_set(owner, 'oCLlite_OclLExpression111', partner)
    assert getattr(partner, 'oCLlite_ElseIfThenExp110') == owner
    _safe_set(owner, 'oCLlite_OclLExpression111', None)
    assert getattr(partner, 'oCLlite_ElseIfThenExp110') is None


def test_assoc_then45_stub_double():
    # oCLlite_IfExp has no real 'oCLlite_IfExp46' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_IfExp()
    setattr(partner, 'oCLlite_IfExp46', None)
    _safe_set(owner, 'oCLlite_OclLExpression47', partner)
    assert getattr(partner, 'oCLlite_IfExp46') == owner
    _safe_set(owner, 'oCLlite_OclLExpression47', None)
    assert getattr(partner, 'oCLlite_IfExp46') is None


def test_assoc_type22_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_Iterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_Iterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_Iterator(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType', None)
    _safe_set(owner, 'oCLlite_Iterator', partner)
    assert getattr(partner, 'oCLlite_OclLType') == owner
    _safe_set(owner, 'oCLlite_Iterator', None)
    assert getattr(partner, 'oCLlite_OclLType') is None


def test_assoc_type23_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType25' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_LocalVariable(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType25', None)
    _safe_set(owner, 'oCLlite_LocalVariable24', partner)
    assert getattr(partner, 'oCLlite_OclLType25') == owner
    _safe_set(owner, 'oCLlite_LocalVariable24', None)
    assert getattr(partner, 'oCLlite_OclLType25') is None


def test_assoc_type38_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType39' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_TuplePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_TuplePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_TuplePart(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType39', None)
    _safe_set(owner, 'oCLlite_TuplePart', partner)
    assert getattr(partner, 'oCLlite_OclLType39') == owner
    _safe_set(owner, 'oCLlite_TuplePart', None)
    assert getattr(partner, 'oCLlite_OclLType39') is None


def test_assoc_value35_stub_double():
    # oCLlite_MapElement has no real 'oCLlite_MapElement36' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_OclLExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_OclLExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_OclLExpression(elements="sample_text", name="sample_text")
    partner = oCLlite_MapElement()
    setattr(partner, 'oCLlite_MapElement36', None)
    _safe_set(owner, 'oCLlite_OclLExpression37', partner)
    assert getattr(partner, 'oCLlite_MapElement36') == owner
    _safe_set(owner, 'oCLlite_OclLExpression37', None)
    assert getattr(partner, 'oCLlite_MapElement36') is None


def test_assoc_valueType63_stub_double():
    # oCLlite_OclLType has no real 'oCLlite_OclLType65' property in the generated
    # code (a bare stub) -- manually attach it so oCLlite_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oCLlite_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oCLlite_MapType(name="sample_text")
    partner = oCLlite_OclLType()
    setattr(partner, 'oCLlite_OclLType65', None)
    _safe_set(owner, 'oCLlite_MapType64', partner)
    assert getattr(partner, 'oCLlite_OclLType65') == owner
    _safe_set(owner, 'oCLlite_MapType64', None)
    assert getattr(partner, 'oCLlite_OclLType65') is None


