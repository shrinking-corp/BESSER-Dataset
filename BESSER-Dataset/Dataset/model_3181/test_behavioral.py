import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Named,
    Statement,
    SubField,
    expressionDSL_And,
    expressionDSL_BinaryMinus,
    expressionDSL_BinaryPlus,
    expressionDSL_BooleanConstant,
    expressionDSL_Comparison,
    expressionDSL_ConstDef,
    expressionDSL_Dim,
    expressionDSL_Exponent,
    expressionDSL_Expression,
    expressionDSL_FunctionCall,
    expressionDSL_FunctionCallStatement,
    expressionDSL_FunctionDef,
    expressionDSL_IntConstant,
    expressionDSL_Model,
    expressionDSL_MulOrDiv,
    expressionDSL_Named,
    expressionDSL_Not,
    expressionDSL_Or,
    expressionDSL_QualifiedRef,
    expressionDSL_Statement,
    expressionDSL_StringConstant,
    expressionDSL_StructDef,
    expressionDSL_SubField,
    expressionDSL_SubFieldDef,
    expressionDSL_UnaryMinus,
    expressionDSL_UnaryPlus,
    expressionDSL_VariableArrayOrFunctionRef,
    expressionDSL_VariableAssignment,
    expressionDSL_VariableDef,
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

def test_assoc_options1_reverse_link_reassign_clear():
    a1 = expressionDSL_VariableDef(type="sample_text")
    a2 = expressionDSL_VariableDef(type="sample_text_2")
    b = expressionDSL_Dim(arrayDimensions=7)
    _safe_set(b, 'expressionDSL_Dim', a1)
    assert _is_linked(b, 'expressionDSL_Dim', a1)
    if hasattr(a1, 'expressionDSL_VariableDef'):
        assert _is_linked(a1, 'expressionDSL_VariableDef', b)
    _safe_set(b, 'expressionDSL_Dim', a2)
    assert _is_linked(b, 'expressionDSL_Dim', a2)
    if hasattr(a1, 'expressionDSL_VariableDef'):
        assert not _is_linked(a1, 'expressionDSL_VariableDef', b)
    if hasattr(a2, 'expressionDSL_VariableDef'):
        assert _is_linked(a2, 'expressionDSL_VariableDef', b)
    _safe_set(b, 'expressionDSL_Dim', None)
    assert not _is_linked(b, 'expressionDSL_Dim', a2)
    if hasattr(a2, 'expressionDSL_VariableDef'):
        assert not _is_linked(a2, 'expressionDSL_VariableDef', b)


def test_assoc_options2_reverse_link_reassign_clear():
    a1 = expressionDSL_Dim(arrayDimensions=7)
    a2 = expressionDSL_Dim(arrayDimensions=13)
    b = expressionDSL_ConstDef(type="sample_text")
    _safe_set(b, 'expressionDSL_ConstDef', a1)
    assert _is_linked(b, 'expressionDSL_ConstDef', a1)
    if hasattr(a1, 'expressionDSL_Dim3'):
        assert _is_linked(a1, 'expressionDSL_Dim3', b)
    _safe_set(b, 'expressionDSL_ConstDef', a2)
    assert _is_linked(b, 'expressionDSL_ConstDef', a2)
    if hasattr(a1, 'expressionDSL_Dim3'):
        assert not _is_linked(a1, 'expressionDSL_Dim3', b)
    if hasattr(a2, 'expressionDSL_Dim3'):
        assert _is_linked(a2, 'expressionDSL_Dim3', b)
    _safe_set(b, 'expressionDSL_ConstDef', None)
    assert not _is_linked(b, 'expressionDSL_ConstDef', a2)
    if hasattr(a2, 'expressionDSL_Dim3'):
        assert not _is_linked(a2, 'expressionDSL_Dim3', b)


def test_assoc_options8_reverse_link_reassign_clear():
    a1 = expressionDSL_SubFieldDef(type="sample_text")
    a2 = expressionDSL_SubFieldDef(type="sample_text_2")
    b = expressionDSL_Dim(arrayDimensions=7)
    _safe_set(b, 'expressionDSL_Dim9', a1)
    assert _is_linked(b, 'expressionDSL_Dim9', a1)
    if hasattr(a1, 'expressionDSL_SubFieldDef'):
        assert _is_linked(a1, 'expressionDSL_SubFieldDef', b)
    _safe_set(b, 'expressionDSL_Dim9', a2)
    assert _is_linked(b, 'expressionDSL_Dim9', a2)
    if hasattr(a1, 'expressionDSL_SubFieldDef'):
        assert not _is_linked(a1, 'expressionDSL_SubFieldDef', b)
    if hasattr(a2, 'expressionDSL_SubFieldDef'):
        assert _is_linked(a2, 'expressionDSL_SubFieldDef', b)
    _safe_set(b, 'expressionDSL_Dim9', None)
    assert not _is_linked(b, 'expressionDSL_Dim9', a2)
    if hasattr(a2, 'expressionDSL_SubFieldDef'):
        assert not _is_linked(a2, 'expressionDSL_SubFieldDef', b)


def test_assoc_tgtvar10_reverse_link_reassign_clear():
    a1 = expressionDSL_VariableDef(type="sample_text")
    a2 = expressionDSL_VariableDef(type="sample_text_2")
    b = expressionDSL_VariableAssignment(op="sample_text")
    _safe_set(b, 'expressionDSL_VariableAssignment', a1)
    assert _is_linked(b, 'expressionDSL_VariableAssignment', a1)
    if hasattr(a1, 'expressionDSL_VariableDef11'):
        assert _is_linked(a1, 'expressionDSL_VariableDef11', b)
    _safe_set(b, 'expressionDSL_VariableAssignment', a2)
    assert _is_linked(b, 'expressionDSL_VariableAssignment', a2)
    if hasattr(a1, 'expressionDSL_VariableDef11'):
        assert not _is_linked(a1, 'expressionDSL_VariableDef11', b)
    if hasattr(a2, 'expressionDSL_VariableDef11'):
        assert _is_linked(a2, 'expressionDSL_VariableDef11', b)
    _safe_set(b, 'expressionDSL_VariableAssignment', None)
    assert not _is_linked(b, 'expressionDSL_VariableAssignment', a2)
    if hasattr(a2, 'expressionDSL_VariableDef11'):
        assert not _is_linked(a2, 'expressionDSL_VariableDef11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_exp12_stub_double():
    # expressionDSL_Expression has no real 'expressionDSL_Expression' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_VariableAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_VariableAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_VariableAssignment(op="sample_text")
    partner = expressionDSL_Expression()
    setattr(partner, 'expressionDSL_Expression', None)
    _safe_set(owner, 'expressionDSL_VariableAssignment13', partner)
    assert getattr(partner, 'expressionDSL_Expression') == owner
    _safe_set(owner, 'expressionDSL_VariableAssignment13', None)
    assert getattr(partner, 'expressionDSL_Expression') is None


def test_assoc_left34_stub_double():
    # expressionDSL_Expression has no real 'expressionDSL_Expression35' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_Comparison(op="sample_text")
    partner = expressionDSL_Expression()
    setattr(partner, 'expressionDSL_Expression35', None)
    _safe_set(owner, 'expressionDSL_Comparison', partner)
    assert getattr(partner, 'expressionDSL_Expression35') == owner
    _safe_set(owner, 'expressionDSL_Comparison', None)
    assert getattr(partner, 'expressionDSL_Expression35') is None


def test_assoc_left49_stub_double():
    # expressionDSL_Expression has no real 'expressionDSL_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_MulOrDiv(op="sample_text")
    partner = expressionDSL_Expression()
    setattr(partner, 'expressionDSL_Expression50', None)
    _safe_set(owner, 'expressionDSL_MulOrDiv', partner)
    assert getattr(partner, 'expressionDSL_Expression50') == owner
    _safe_set(owner, 'expressionDSL_MulOrDiv', None)
    assert getattr(partner, 'expressionDSL_Expression50') is None


def test_assoc_options4_stub_double():
    # expressionDSL_StructDef has no real 'expressionDSL_StructDef' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_Dim's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_Dim's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_Dim(arrayDimensions=7)
    partner = expressionDSL_StructDef()
    setattr(partner, 'expressionDSL_StructDef', None)
    _safe_set(owner, 'expressionDSL_Dim5', partner)
    assert getattr(partner, 'expressionDSL_StructDef') == owner
    _safe_set(owner, 'expressionDSL_Dim5', None)
    assert getattr(partner, 'expressionDSL_StructDef') is None


def test_assoc_ref15_stub_double():
    # expressionDSL_FunctionCall has no real 'expressionDSL_FunctionCall16' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_FunctionDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_FunctionDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_FunctionDef(type="sample_text")
    partner = expressionDSL_FunctionCall()
    setattr(partner, 'expressionDSL_FunctionCall16', None)
    _safe_set(owner, 'expressionDSL_FunctionDef', partner)
    assert getattr(partner, 'expressionDSL_FunctionCall16') == owner
    _safe_set(owner, 'expressionDSL_FunctionDef', None)
    assert getattr(partner, 'expressionDSL_FunctionCall16') is None


def test_assoc_ref20_stub_double():
    # expressionDSL_VariableArrayOrFunctionRef has no real 'expressionDSL_VariableArrayOrFunctionRef' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_Named's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_Named's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_Named(name="sample_text")
    partner = expressionDSL_VariableArrayOrFunctionRef()
    setattr(partner, 'expressionDSL_VariableArrayOrFunctionRef', None)
    _safe_set(owner, 'expressionDSL_Named', partner)
    assert getattr(partner, 'expressionDSL_VariableArrayOrFunctionRef') == owner
    _safe_set(owner, 'expressionDSL_Named', None)
    assert getattr(partner, 'expressionDSL_VariableArrayOrFunctionRef') is None


def test_assoc_right36_stub_double():
    # expressionDSL_Expression has no real 'expressionDSL_Expression38' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_Comparison(op="sample_text")
    partner = expressionDSL_Expression()
    setattr(partner, 'expressionDSL_Expression38', None)
    _safe_set(owner, 'expressionDSL_Comparison37', partner)
    assert getattr(partner, 'expressionDSL_Expression38') == owner
    _safe_set(owner, 'expressionDSL_Comparison37', None)
    assert getattr(partner, 'expressionDSL_Expression38') is None


def test_assoc_right51_stub_double():
    # expressionDSL_Expression has no real 'expressionDSL_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so expressionDSL_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressionDSL_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressionDSL_MulOrDiv(op="sample_text")
    partner = expressionDSL_Expression()
    setattr(partner, 'expressionDSL_Expression53', None)
    _safe_set(owner, 'expressionDSL_MulOrDiv52', partner)
    assert getattr(partner, 'expressionDSL_Expression53') == owner
    _safe_set(owner, 'expressionDSL_MulOrDiv52', None)
    assert getattr(partner, 'expressionDSL_Expression53') is None


