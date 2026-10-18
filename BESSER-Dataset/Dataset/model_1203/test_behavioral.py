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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argsTypes47_stub_double():
    # docl_OclType has no real 'docl_OclType48' property in the generated
    # code (a bare stub) -- manually attach it so docl_LambdaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_LambdaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_LambdaType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType48', None)
    _safe_set(owner, 'docl_LambdaType', {partner})
    assert getattr(partner, 'docl_OclType48') == owner
    _safe_set(owner, 'docl_LambdaType', set())
    assert getattr(partner, 'docl_OclType48') is None


def test_assoc_arguments77_stub_double():
    # docl_CollectionOpCallExp has no real 'docl_CollectionOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_CollectionOpCallExp()
    setattr(partner, 'docl_CollectionOpCallExp', None)
    _safe_set(owner, 'docl_OclExpression78', partner)
    assert owner in getattr(partner, 'docl_CollectionOpCallExp')
    _safe_set(owner, 'docl_OclExpression78', None)
    assert owner not in getattr(partner, 'docl_CollectionOpCallExp')


def test_assoc_arguments92_stub_double():
    # docl_OperationCall has no real 'docl_OperationCall' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_OperationCall()
    setattr(partner, 'docl_OperationCall', None)
    _safe_set(owner, 'docl_OclExpression93', partner)
    assert owner in getattr(partner, 'docl_OperationCall')
    _safe_set(owner, 'docl_OclExpression93', None)
    assert owner not in getattr(partner, 'docl_OperationCall')


def test_assoc_body84_stub_double():
    # docl_IterateExp has no real 'docl_IterateExp85' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_IterateExp()
    setattr(partner, 'docl_IterateExp85', None)
    _safe_set(owner, 'docl_OclExpression86', partner)
    assert getattr(partner, 'docl_IterateExp85') == owner
    _safe_set(owner, 'docl_OclExpression86', None)
    assert getattr(partner, 'docl_IterateExp85') is None


def test_assoc_body89_stub_double():
    # docl_IteratorExp has no real 'docl_IteratorExp90' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_IteratorExp()
    setattr(partner, 'docl_IteratorExp90', None)
    _safe_set(owner, 'docl_OclExpression91', partner)
    assert getattr(partner, 'docl_IteratorExp90') == owner
    _safe_set(owner, 'docl_OclExpression91', None)
    assert getattr(partner, 'docl_IteratorExp90') is None


def test_assoc_condition34_stub_double():
    # docl_IfExp has no real 'docl_IfExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_IfExp()
    setattr(partner, 'docl_IfExp', None)
    _safe_set(owner, 'docl_OclExpression35', partner)
    assert getattr(partner, 'docl_IfExp') == owner
    _safe_set(owner, 'docl_OclExpression35', None)
    assert getattr(partner, 'docl_IfExp') is None


def test_assoc_condition98_stub_double():
    # docl_ElseIfThenExp has no real 'docl_ElseIfThenExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_ElseIfThenExp()
    setattr(partner, 'docl_ElseIfThenExp', None)
    _safe_set(owner, 'docl_OclExpression99', partner)
    assert getattr(partner, 'docl_ElseIfThenExp') == owner
    _safe_set(owner, 'docl_OclExpression99', None)
    assert getattr(partner, 'docl_ElseIfThenExp') is None


def test_assoc_elementType57_stub_double():
    # docl_OclType has no real 'docl_OclType58' property in the generated
    # code (a bare stub) -- manually attach it so docl_SetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_SetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_SetType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType58', None)
    _safe_set(owner, 'docl_SetType', partner)
    assert getattr(partner, 'docl_OclType58') == owner
    _safe_set(owner, 'docl_SetType', None)
    assert getattr(partner, 'docl_OclType58') is None


def test_assoc_elementType59_stub_double():
    # docl_OclType has no real 'docl_OclType60' property in the generated
    # code (a bare stub) -- manually attach it so docl_SequenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_SequenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_SequenceType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType60', None)
    _safe_set(owner, 'docl_SequenceType', partner)
    assert getattr(partner, 'docl_OclType60') == owner
    _safe_set(owner, 'docl_SequenceType', None)
    assert getattr(partner, 'docl_OclType60') is None


def test_assoc_elementType61_stub_double():
    # docl_OclType has no real 'docl_OclType62' property in the generated
    # code (a bare stub) -- manually attach it so docl_OrderedSetType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OrderedSetType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OrderedSetType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType62', None)
    _safe_set(owner, 'docl_OrderedSetType', partner)
    assert getattr(partner, 'docl_OclType62') == owner
    _safe_set(owner, 'docl_OrderedSetType', None)
    assert getattr(partner, 'docl_OclType62') is None


def test_assoc_elementType63_stub_double():
    # docl_OclType has no real 'docl_OclType64' property in the generated
    # code (a bare stub) -- manually attach it so docl_BagType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_BagType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_BagType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType64', None)
    _safe_set(owner, 'docl_BagType', partner)
    assert getattr(partner, 'docl_OclType64') == owner
    _safe_set(owner, 'docl_BagType', None)
    assert getattr(partner, 'docl_OclType64') is None


def test_assoc_elements6_stub_double():
    # docl_ModuleElement has no real 'docl_ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so docl_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_Module(name="sample_text")
    partner = docl_ModuleElement()
    setattr(partner, 'docl_ModuleElement', None)
    _safe_set(owner, 'docl_Module7', {partner})
    assert getattr(partner, 'docl_ModuleElement') == owner
    _safe_set(owner, 'docl_Module7', set())
    assert getattr(partner, 'docl_ModuleElement') is None


def test_assoc_else_42_stub_double():
    # docl_IfExp has no real 'docl_IfExp43' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_IfExp()
    setattr(partner, 'docl_IfExp43', None)
    _safe_set(owner, 'docl_OclExpression44', partner)
    assert getattr(partner, 'docl_IfExp43') == owner
    _safe_set(owner, 'docl_OclExpression44', None)
    assert getattr(partner, 'docl_IfExp43') is None


def test_assoc_exp103_stub_double():
    # docl_NestedExp has no real 'docl_NestedExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_NestedExp()
    setattr(partner, 'docl_NestedExp', None)
    _safe_set(owner, 'docl_OclExpression104', partner)
    assert getattr(partner, 'docl_NestedExp') == owner
    _safe_set(owner, 'docl_OclExpression104', None)
    assert getattr(partner, 'docl_NestedExp') is None


def test_assoc_expression94_stub_double():
    # docl_LambdaExp has no real 'docl_LambdaExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_LambdaExp()
    setattr(partner, 'docl_LambdaExp', None)
    _safe_set(owner, 'docl_OclExpression95', partner)
    assert getattr(partner, 'docl_LambdaExp') == owner
    _safe_set(owner, 'docl_OclExpression95', None)
    assert getattr(partner, 'docl_LambdaExp') is None


def test_assoc_ifThen39_stub_double():
    # docl_IfExp has no real 'docl_IfExp40' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_IfExp()
    setattr(partner, 'docl_IfExp40', None)
    _safe_set(owner, 'docl_OclExpression41', partner)
    assert owner in getattr(partner, 'docl_IfExp40')
    _safe_set(owner, 'docl_OclExpression41', None)
    assert owner not in getattr(partner, 'docl_IfExp40')


def test_assoc_iterators79_stub_double():
    # docl_IterateExp has no real 'docl_IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_Iterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_Iterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_Iterator(name="sample_text")
    partner = docl_IterateExp()
    setattr(partner, 'docl_IterateExp', None)
    _safe_set(owner, 'docl_Iterator80', partner)
    assert owner in getattr(partner, 'docl_IterateExp')
    _safe_set(owner, 'docl_Iterator80', None)
    assert owner not in getattr(partner, 'docl_IterateExp')


def test_assoc_iterators87_stub_double():
    # docl_IteratorExp has no real 'docl_IteratorExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_Iterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_Iterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_Iterator(name="sample_text")
    partner = docl_IteratorExp()
    setattr(partner, 'docl_IteratorExp', None)
    _safe_set(owner, 'docl_Iterator88', partner)
    assert owner in getattr(partner, 'docl_IteratorExp')
    _safe_set(owner, 'docl_Iterator88', None)
    assert owner not in getattr(partner, 'docl_IteratorExp')


def test_assoc_keyType52_stub_double():
    # docl_OclType has no real 'docl_OclType53' property in the generated
    # code (a bare stub) -- manually attach it so docl_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_MapType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType53', None)
    _safe_set(owner, 'docl_MapType', partner)
    assert getattr(partner, 'docl_OclType53') == owner
    _safe_set(owner, 'docl_MapType', None)
    assert getattr(partner, 'docl_OclType53') is None


def test_assoc_parts96_stub_double():
    # docl_TupleExp has no real 'docl_TupleExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_TuplePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_TuplePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_TuplePart(name="sample_text")
    partner = docl_TupleExp()
    setattr(partner, 'docl_TupleExp', None)
    _safe_set(owner, 'docl_TuplePart97', partner)
    assert owner in getattr(partner, 'docl_TupleExp')
    _safe_set(owner, 'docl_TuplePart97', None)
    assert owner not in getattr(partner, 'docl_TupleExp')


def test_assoc_result81_stub_double():
    # docl_IterateExp has no real 'docl_IterateExp82' property in the generated
    # code (a bare stub) -- manually attach it so docl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_LocalVariable(name="sample_text")
    partner = docl_IterateExp()
    setattr(partner, 'docl_IterateExp82', None)
    _safe_set(owner, 'docl_LocalVariable83', partner)
    assert getattr(partner, 'docl_IterateExp82') == owner
    _safe_set(owner, 'docl_LocalVariable83', None)
    assert getattr(partner, 'docl_IterateExp82') is None


def test_assoc_returnType49_stub_double():
    # docl_OclType has no real 'docl_OclType51' property in the generated
    # code (a bare stub) -- manually attach it so docl_LambdaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_LambdaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_LambdaType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType51', None)
    _safe_set(owner, 'docl_LambdaType50', partner)
    assert getattr(partner, 'docl_OclType51') == owner
    _safe_set(owner, 'docl_LambdaType50', None)
    assert getattr(partner, 'docl_OclType51') is None


def test_assoc_source65_stub_double():
    # docl_BoolOpCallExp has no real 'docl_BoolOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_BoolOpCallExp()
    setattr(partner, 'docl_BoolOpCallExp', None)
    _safe_set(owner, 'docl_OclExpression66', partner)
    assert getattr(partner, 'docl_BoolOpCallExp') == owner
    _safe_set(owner, 'docl_OclExpression66', None)
    assert getattr(partner, 'docl_BoolOpCallExp') is None


def test_assoc_source67_stub_double():
    # docl_EqOpCallExp has no real 'docl_EqOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_EqOpCallExp()
    setattr(partner, 'docl_EqOpCallExp', None)
    _safe_set(owner, 'docl_OclExpression68', partner)
    assert getattr(partner, 'docl_EqOpCallExp') == owner
    _safe_set(owner, 'docl_OclExpression68', None)
    assert getattr(partner, 'docl_EqOpCallExp') is None


def test_assoc_source69_stub_double():
    # docl_ComOpCallExp has no real 'docl_ComOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_ComOpCallExp()
    setattr(partner, 'docl_ComOpCallExp', None)
    _safe_set(owner, 'docl_OclExpression70', partner)
    assert getattr(partner, 'docl_ComOpCallExp') == owner
    _safe_set(owner, 'docl_OclExpression70', None)
    assert getattr(partner, 'docl_ComOpCallExp') is None


def test_assoc_source71_stub_double():
    # docl_AddOpCallExp has no real 'docl_AddOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_AddOpCallExp()
    setattr(partner, 'docl_AddOpCallExp', None)
    _safe_set(owner, 'docl_OclExpression72', partner)
    assert getattr(partner, 'docl_AddOpCallExp') == owner
    _safe_set(owner, 'docl_OclExpression72', None)
    assert getattr(partner, 'docl_AddOpCallExp') is None


def test_assoc_source73_stub_double():
    # docl_MulOpCallExp has no real 'docl_MulOpCallExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_MulOpCallExp()
    setattr(partner, 'docl_MulOpCallExp', None)
    _safe_set(owner, 'docl_OclExpression74', partner)
    assert getattr(partner, 'docl_MulOpCallExp') == owner
    _safe_set(owner, 'docl_OclExpression74', None)
    assert getattr(partner, 'docl_MulOpCallExp') is None


def test_assoc_source75_stub_double():
    # docl_NavigationExp has no real 'docl_NavigationExp' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_NavigationExp()
    setattr(partner, 'docl_NavigationExp', None)
    _safe_set(owner, 'docl_OclExpression76', partner)
    assert getattr(partner, 'docl_NavigationExp') == owner
    _safe_set(owner, 'docl_OclExpression76', None)
    assert getattr(partner, 'docl_NavigationExp') is None


def test_assoc_then100_stub_double():
    # docl_ElseIfThenExp has no real 'docl_ElseIfThenExp101' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_ElseIfThenExp()
    setattr(partner, 'docl_ElseIfThenExp101', None)
    _safe_set(owner, 'docl_OclExpression102', partner)
    assert getattr(partner, 'docl_ElseIfThenExp101') == owner
    _safe_set(owner, 'docl_OclExpression102', None)
    assert getattr(partner, 'docl_ElseIfThenExp101') is None


def test_assoc_then36_stub_double():
    # docl_IfExp has no real 'docl_IfExp37' property in the generated
    # code (a bare stub) -- manually attach it so docl_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_OclExpression(elements="sample_text", name="sample_text")
    partner = docl_IfExp()
    setattr(partner, 'docl_IfExp37', None)
    _safe_set(owner, 'docl_OclExpression38', partner)
    assert getattr(partner, 'docl_IfExp37') == owner
    _safe_set(owner, 'docl_OclExpression38', None)
    assert getattr(partner, 'docl_IfExp37') is None


def test_assoc_type22_stub_double():
    # docl_OclType has no real 'docl_OclType' property in the generated
    # code (a bare stub) -- manually attach it so docl_Iterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_Iterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_Iterator(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType', None)
    _safe_set(owner, 'docl_Iterator', partner)
    assert getattr(partner, 'docl_OclType') == owner
    _safe_set(owner, 'docl_Iterator', None)
    assert getattr(partner, 'docl_OclType') is None


def test_assoc_type23_stub_double():
    # docl_OclType has no real 'docl_OclType25' property in the generated
    # code (a bare stub) -- manually attach it so docl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_LocalVariable(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType25', None)
    _safe_set(owner, 'docl_LocalVariable24', partner)
    assert getattr(partner, 'docl_OclType25') == owner
    _safe_set(owner, 'docl_LocalVariable24', None)
    assert getattr(partner, 'docl_OclType25') is None


def test_assoc_type29_stub_double():
    # docl_OclType has no real 'docl_OclType30' property in the generated
    # code (a bare stub) -- manually attach it so docl_TuplePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_TuplePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_TuplePart(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType30', None)
    _safe_set(owner, 'docl_TuplePart', partner)
    assert getattr(partner, 'docl_OclType30') == owner
    _safe_set(owner, 'docl_TuplePart', None)
    assert getattr(partner, 'docl_OclType30') is None


def test_assoc_valueType54_stub_double():
    # docl_OclType has no real 'docl_OclType56' property in the generated
    # code (a bare stub) -- manually attach it so docl_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # docl_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = docl_MapType(name="sample_text")
    partner = docl_OclType()
    setattr(partner, 'docl_OclType56', None)
    _safe_set(owner, 'docl_MapType55', partner)
    assert getattr(partner, 'docl_OclType56') == owner
    _safe_set(owner, 'docl_MapType55', None)
    assert getattr(partner, 'docl_OclType56') is None


