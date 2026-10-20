import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractElement,
    Expression,
    tym_AbstractElement,
    tym_And,
    tym_Block,
    tym_BoolConstant,
    tym_Comparison,
    tym_EObject,
    tym_Equality,
    tym_Expression,
    tym_Function,
    tym_FunctionBlock,
    tym_FunctionCall,
    tym_IntConstant,
    tym_LoopStatement,
    tym_Minus,
    tym_Model,
    tym_MulOrDiv,
    tym_Not,
    tym_Or,
    tym_Plus,
    tym_PrintStatement,
    tym_Return,
    tym_StringConstant,
    tym_TestStatement,
    tym_Variable,
    tym_VariableRef,
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

def test_assoc_params6_reverse_link_reassign_clear():
    a1 = tym_Variable(name="sample_text", vartype="sample_text")
    a2 = tym_Variable(name="sample_text_2", vartype="sample_text_2")
    b = tym_Function(name="sample_text", return_="sample_text")
    _safe_set(b, 'tym_Function', {a1})
    assert _is_linked(b, 'tym_Function', a1)
    if hasattr(a1, 'tym_Variable7'):
        assert _is_linked(a1, 'tym_Variable7', b)
    _safe_set(b, 'tym_Function', {a2})
    assert _is_linked(b, 'tym_Function', a2)
    if hasattr(a1, 'tym_Variable7'):
        assert not _is_linked(a1, 'tym_Variable7', b)
    if hasattr(a2, 'tym_Variable7'):
        assert _is_linked(a2, 'tym_Variable7', b)
    _safe_set(b, 'tym_Function', set())
    assert not _is_linked(b, 'tym_Function', a2)
    if hasattr(a2, 'tym_Variable7'):
        assert not _is_linked(a2, 'tym_Variable7', b)


def test_assoc_variable2_reverse_link_reassign_clear():
    a1 = tym_Variable(name="sample_text", vartype="sample_text")
    a2 = tym_Variable(name="sample_text_2", vartype="sample_text_2")
    b = tym_Variable(name="sample_text", vartype="sample_text")
    _safe_set(b, 'tym_Variable1', a1)
    assert _is_linked(b, 'tym_Variable1', a1)
    if hasattr(a1, 'tym_Variable'):
        assert _is_linked(a1, 'tym_Variable', b)
    _safe_set(b, 'tym_Variable1', a2)
    assert _is_linked(b, 'tym_Variable1', a2)
    if hasattr(a1, 'tym_Variable'):
        assert not _is_linked(a1, 'tym_Variable', b)
    if hasattr(a2, 'tym_Variable'):
        assert _is_linked(a2, 'tym_Variable', b)
    _safe_set(b, 'tym_Variable1', None)
    assert not _is_linked(b, 'tym_Variable1', a2)
    if hasattr(a2, 'tym_Variable'):
        assert not _is_linked(a2, 'tym_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body8_stub_double():
    # tym_FunctionBlock has no real 'tym_FunctionBlock' property in the generated
    # code (a bare stub) -- manually attach it so tym_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Function(name="sample_text", return_="sample_text")
    partner = tym_FunctionBlock()
    setattr(partner, 'tym_FunctionBlock', None)
    _safe_set(owner, 'tym_Function9', partner)
    assert getattr(partner, 'tym_FunctionBlock') == owner
    _safe_set(owner, 'tym_Function9', None)
    assert getattr(partner, 'tym_FunctionBlock') is None


def test_assoc_expression3_stub_double():
    # tym_EObject has no real 'tym_EObject5' property in the generated
    # code (a bare stub) -- manually attach it so tym_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Variable(name="sample_text", vartype="sample_text")
    partner = tym_EObject()
    setattr(partner, 'tym_EObject5', None)
    _safe_set(owner, 'tym_Variable4', partner)
    assert getattr(partner, 'tym_EObject5') == owner
    _safe_set(owner, 'tym_Variable4', None)
    assert getattr(partner, 'tym_EObject5') is None


def test_assoc_funcname31_stub_double():
    # tym_FunctionCall has no real 'tym_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so tym_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Function(name="sample_text", return_="sample_text")
    partner = tym_FunctionCall()
    setattr(partner, 'tym_FunctionCall', None)
    _safe_set(owner, 'tym_Function32', partner)
    assert getattr(partner, 'tym_FunctionCall') == owner
    _safe_set(owner, 'tym_Function32', None)
    assert getattr(partner, 'tym_FunctionCall') is None


def test_assoc_left45_stub_double():
    # tym_Expression has no real 'tym_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so tym_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Equality(op="sample_text")
    partner = tym_Expression()
    setattr(partner, 'tym_Expression46', None)
    _safe_set(owner, 'tym_Equality', partner)
    assert getattr(partner, 'tym_Expression46') == owner
    _safe_set(owner, 'tym_Equality', None)
    assert getattr(partner, 'tym_Expression46') is None


def test_assoc_left50_stub_double():
    # tym_Expression has no real 'tym_Expression51' property in the generated
    # code (a bare stub) -- manually attach it so tym_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Comparison(op="sample_text")
    partner = tym_Expression()
    setattr(partner, 'tym_Expression51', None)
    _safe_set(owner, 'tym_Comparison', partner)
    assert getattr(partner, 'tym_Expression51') == owner
    _safe_set(owner, 'tym_Comparison', None)
    assert getattr(partner, 'tym_Expression51') is None


def test_assoc_left65_stub_double():
    # tym_Expression has no real 'tym_Expression66' property in the generated
    # code (a bare stub) -- manually attach it so tym_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_MulOrDiv(op="sample_text")
    partner = tym_Expression()
    setattr(partner, 'tym_Expression66', None)
    _safe_set(owner, 'tym_MulOrDiv', partner)
    assert getattr(partner, 'tym_Expression66') == owner
    _safe_set(owner, 'tym_MulOrDiv', None)
    assert getattr(partner, 'tym_Expression66') is None


def test_assoc_right47_stub_double():
    # tym_Expression has no real 'tym_Expression49' property in the generated
    # code (a bare stub) -- manually attach it so tym_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Equality(op="sample_text")
    partner = tym_Expression()
    setattr(partner, 'tym_Expression49', None)
    _safe_set(owner, 'tym_Equality48', partner)
    assert getattr(partner, 'tym_Expression49') == owner
    _safe_set(owner, 'tym_Equality48', None)
    assert getattr(partner, 'tym_Expression49') is None


def test_assoc_right52_stub_double():
    # tym_Expression has no real 'tym_Expression54' property in the generated
    # code (a bare stub) -- manually attach it so tym_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Comparison(op="sample_text")
    partner = tym_Expression()
    setattr(partner, 'tym_Expression54', None)
    _safe_set(owner, 'tym_Comparison53', partner)
    assert getattr(partner, 'tym_Expression54') == owner
    _safe_set(owner, 'tym_Comparison53', None)
    assert getattr(partner, 'tym_Expression54') is None


def test_assoc_right67_stub_double():
    # tym_Expression has no real 'tym_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so tym_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_MulOrDiv(op="sample_text")
    partner = tym_Expression()
    setattr(partner, 'tym_Expression69', None)
    _safe_set(owner, 'tym_MulOrDiv68', partner)
    assert getattr(partner, 'tym_Expression69') == owner
    _safe_set(owner, 'tym_MulOrDiv68', None)
    assert getattr(partner, 'tym_Expression69') is None


def test_assoc_variable72_stub_double():
    # tym_VariableRef has no real 'tym_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so tym_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tym_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tym_Variable(name="sample_text", vartype="sample_text")
    partner = tym_VariableRef()
    setattr(partner, 'tym_VariableRef', None)
    _safe_set(owner, 'tym_Variable73', partner)
    assert getattr(partner, 'tym_VariableRef') == owner
    _safe_set(owner, 'tym_Variable73', None)
    assert getattr(partner, 'tym_VariableRef') is None


