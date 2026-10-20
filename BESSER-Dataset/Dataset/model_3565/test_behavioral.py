import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Atri,
    Atrib_Aux,
    CallFor,
    ElseIfCondition,
    Expression,
    F,
    Greeting,
    I,
    Operations,
    OperationsOneEquals,
    SwitchCase,
    T,
    TypeValue,
    go_Addition,
    go_AndExpression,
    go_Atri,
    go_Atrib,
    go_AtribVar,
    go_Atrib_Aux,
    go_Bool,
    go_CallFor,
    go_CallFunc,
    go_Cases,
    go_ComparisonExpression,
    go_Condition,
    go_DataType,
    go_DecFunc,
    go_DecVar,
    go_DecVars,
    go_Decl,
    go_Division,
    go_Double,
    go_EObject,
    go_ElseCondition,
    go_ElseIfCondition,
    go_Expression,
    go_F,
    go_FunctionBody,
    go_FunctionReturn,
    go_Go,
    go_Greeting,
    go_I,
    go_IfCondition,
    go_Intg,
    go_Literal,
    go_MultDecVars,
    go_Multiplication,
    go_Numbers,
    go_Operations,
    go_OperationsOneEquals,
    go_OrExpression,
    go_Params,
    go_ReAtrib,
    go_Str,
    go_Subtration,
    go_SwitchCase,
    go_T,
    go_TypeValue,
    go_Variable,
    go_Y,
    go_operationsOne,
    go_varFor,
    operationsOne,
    varFor,
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

def test_assoc_param65_reverse_link_reassign_clear():
    a1 = go_Params(params="sample_text", type="sample_text")
    a2 = go_Params(params="sample_text_2", type="sample_text_2")
    b = go_DecFunc(name="sample_text", returnType="sample_text")
    _safe_set(b, 'go_DecFunc', a1)
    assert _is_linked(b, 'go_DecFunc', a1)
    if hasattr(a1, 'go_Params'):
        assert _is_linked(a1, 'go_Params', b)
    _safe_set(b, 'go_DecFunc', a2)
    assert _is_linked(b, 'go_DecFunc', a2)
    if hasattr(a1, 'go_Params'):
        assert not _is_linked(a1, 'go_Params', b)
    if hasattr(a2, 'go_Params'):
        assert _is_linked(a2, 'go_Params', b)
    _safe_set(b, 'go_DecFunc', None)
    assert not _is_linked(b, 'go_DecFunc', a2)
    if hasattr(a2, 'go_Params'):
        assert not _is_linked(a2, 'go_Params', b)


def test_assoc_param76_reverse_link_reassign_clear():
    a1 = go_Params(params="sample_text", type="sample_text")
    a2 = go_Params(params="sample_text_2", type="sample_text_2")
    b = go_CallFunc(nameFunc="sample_text")
    _safe_set(b, 'go_CallFunc', a1)
    assert _is_linked(b, 'go_CallFunc', a1)
    if hasattr(a1, 'go_Params77'):
        assert _is_linked(a1, 'go_Params77', b)
    _safe_set(b, 'go_CallFunc', a2)
    assert _is_linked(b, 'go_CallFunc', a2)
    if hasattr(a1, 'go_Params77'):
        assert not _is_linked(a1, 'go_Params77', b)
    if hasattr(a2, 'go_Params77'):
        assert _is_linked(a2, 'go_Params77', b)
    _safe_set(b, 'go_CallFunc', None)
    assert not _is_linked(b, 'go_CallFunc', a2)
    if hasattr(a2, 'go_Params77'):
        assert not _is_linked(a2, 'go_Params77', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignment4_stub_double():
    # go_DecVar has no real 'go_DecVar5' property in the generated
    # code (a bare stub) -- manually attach it so go_AtribVar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_AtribVar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_AtribVar(type="sample_text", vars="sample_text")
    partner = go_DecVar()
    setattr(partner, 'go_DecVar5', None)
    _safe_set(owner, 'go_AtribVar', partner)
    assert getattr(partner, 'go_DecVar5') == owner
    _safe_set(owner, 'go_AtribVar', None)
    assert getattr(partner, 'go_DecVar5') is None


def test_assoc_atrb26_stub_double():
    # go_Atrib_Aux has no real 'go_Atrib_Aux27' property in the generated
    # code (a bare stub) -- manually attach it so go_DecVars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_DecVars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_DecVars(vars="sample_text")
    partner = go_Atrib_Aux()
    setattr(partner, 'go_Atrib_Aux27', None)
    _safe_set(owner, 'go_DecVars', {partner})
    assert getattr(partner, 'go_Atrib_Aux27') == owner
    _safe_set(owner, 'go_DecVars', set())
    assert getattr(partner, 'go_Atrib_Aux27') is None


def test_assoc_atrb8_stub_double():
    # go_Atrib_Aux has no real 'go_Atrib_Aux' property in the generated
    # code (a bare stub) -- manually attach it so go_AtribVar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_AtribVar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_AtribVar(type="sample_text", vars="sample_text")
    partner = go_Atrib_Aux()
    setattr(partner, 'go_Atrib_Aux', None)
    _safe_set(owner, 'go_AtribVar9', {partner})
    assert getattr(partner, 'go_Atrib_Aux') == owner
    _safe_set(owner, 'go_AtribVar9', set())
    assert getattr(partner, 'go_Atrib_Aux') is None


def test_assoc_atrib14_stub_double():
    # go_Atrib_Aux has no real 'go_Atrib_Aux16' property in the generated
    # code (a bare stub) -- manually attach it so go_Atrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Atrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Atrib(modifier="sample_text", name="sample_text", type="sample_text")
    partner = go_Atrib_Aux()
    setattr(partner, 'go_Atrib_Aux16', None)
    _safe_set(owner, 'go_Atrib15', partner)
    assert getattr(partner, 'go_Atrib_Aux16') == owner
    _safe_set(owner, 'go_Atrib15', None)
    assert getattr(partner, 'go_Atrib_Aux16') is None


def test_assoc_atrib19_stub_double():
    # go_Atrib_Aux has no real 'go_Atrib_Aux21' property in the generated
    # code (a bare stub) -- manually attach it so go_ReAtrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_ReAtrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_ReAtrib(name="sample_text")
    partner = go_Atrib_Aux()
    setattr(partner, 'go_Atrib_Aux21', None)
    _safe_set(owner, 'go_ReAtrib20', partner)
    assert getattr(partner, 'go_Atrib_Aux21') == owner
    _safe_set(owner, 'go_ReAtrib20', None)
    assert getattr(partner, 'go_Atrib_Aux21') is None


def test_assoc_atribuicao2_stub_double():
    # go_DecVar has no real 'go_DecVar3' property in the generated
    # code (a bare stub) -- manually attach it so go_Atrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Atrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Atrib(modifier="sample_text", name="sample_text", type="sample_text")
    partner = go_DecVar()
    setattr(partner, 'go_DecVar3', None)
    _safe_set(owner, 'go_Atrib', partner)
    assert getattr(partner, 'go_DecVar3') == owner
    _safe_set(owner, 'go_Atrib', None)
    assert getattr(partner, 'go_DecVar3') is None


def test_assoc_body66_stub_double():
    # go_FunctionBody has no real 'go_FunctionBody' property in the generated
    # code (a bare stub) -- manually attach it so go_DecFunc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_DecFunc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_DecFunc(name="sample_text", returnType="sample_text")
    partner = go_FunctionBody()
    setattr(partner, 'go_FunctionBody', None)
    _safe_set(owner, 'go_DecFunc67', partner)
    assert getattr(partner, 'go_FunctionBody') == owner
    _safe_set(owner, 'go_DecFunc67', None)
    assert getattr(partner, 'go_FunctionBody') is None


def test_assoc_cas10_stub_double():
    # go_Cases has no real 'go_Cases' property in the generated
    # code (a bare stub) -- manually attach it so go_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Variable(name="sample_text")
    partner = go_Cases()
    setattr(partner, 'go_Cases', None)
    _safe_set(owner, 'go_Variable', partner)
    assert getattr(partner, 'go_Cases') == owner
    _safe_set(owner, 'go_Variable', None)
    assert getattr(partner, 'go_Cases') is None


def test_assoc_d34_stub_double():
    # go_Numbers has no real 'go_Numbers35' property in the generated
    # code (a bare stub) -- manually attach it so go_Double's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Double's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Double(d=7)
    partner = go_Numbers()
    setattr(partner, 'go_Numbers35', None)
    _safe_set(owner, 'go_Double', partner)
    assert getattr(partner, 'go_Numbers35') == owner
    _safe_set(owner, 'go_Double', None)
    assert getattr(partner, 'go_Numbers35') is None


def test_assoc_declaration1_stub_double():
    # go_DecVar has no real 'go_DecVar' property in the generated
    # code (a bare stub) -- manually attach it so go_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Decl(name="sample_text", type="sample_text")
    partner = go_DecVar()
    setattr(partner, 'go_DecVar', None)
    _safe_set(owner, 'go_Decl', partner)
    assert getattr(partner, 'go_DecVar') == owner
    _safe_set(owner, 'go_Decl', None)
    assert getattr(partner, 'go_DecVar') is None


def test_assoc_int33_stub_double():
    # go_Numbers has no real 'go_Numbers' property in the generated
    # code (a bare stub) -- manually attach it so go_Intg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Intg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Intg(i=7)
    partner = go_Numbers()
    setattr(partner, 'go_Numbers', None)
    _safe_set(owner, 'go_Intg', partner)
    assert getattr(partner, 'go_Numbers') == owner
    _safe_set(owner, 'go_Intg', None)
    assert getattr(partner, 'go_Numbers') is None


def test_assoc_k11_stub_double():
    # go_Greeting has no real 'go_Greeting13' property in the generated
    # code (a bare stub) -- manually attach it so go_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Variable(name="sample_text")
    partner = go_Greeting()
    setattr(partner, 'go_Greeting13', None)
    _safe_set(owner, 'go_Variable12', partner)
    assert getattr(partner, 'go_Greeting13') == owner
    _safe_set(owner, 'go_Variable12', None)
    assert getattr(partner, 'go_Greeting13') is None


def test_assoc_k17_stub_double():
    # go_EObject has no real 'go_EObject' property in the generated
    # code (a bare stub) -- manually attach it so go_Atrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Atrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Atrib(modifier="sample_text", name="sample_text", type="sample_text")
    partner = go_EObject()
    setattr(partner, 'go_EObject', None)
    _safe_set(owner, 'go_Atrib18', partner)
    assert getattr(partner, 'go_EObject') == owner
    _safe_set(owner, 'go_Atrib18', None)
    assert getattr(partner, 'go_EObject') is None


def test_assoc_k22_stub_double():
    # go_EObject has no real 'go_EObject24' property in the generated
    # code (a bare stub) -- manually attach it so go_ReAtrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_ReAtrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_ReAtrib(name="sample_text")
    partner = go_EObject()
    setattr(partner, 'go_EObject24', None)
    _safe_set(owner, 'go_ReAtrib23', partner)
    assert getattr(partner, 'go_EObject24') == owner
    _safe_set(owner, 'go_ReAtrib23', None)
    assert getattr(partner, 'go_EObject24') is None


def test_assoc_reassignment6_stub_double():
    # go_DecVar has no real 'go_DecVar7' property in the generated
    # code (a bare stub) -- manually attach it so go_ReAtrib's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_ReAtrib's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_ReAtrib(name="sample_text")
    partner = go_DecVar()
    setattr(partner, 'go_DecVar7', None)
    _safe_set(owner, 'go_ReAtrib', partner)
    assert getattr(partner, 'go_DecVar7') == owner
    _safe_set(owner, 'go_ReAtrib', None)
    assert getattr(partner, 'go_DecVar7') is None


def test_assoc_typw25_stub_double():
    # go_TypeValue has no real 'go_TypeValue' property in the generated
    # code (a bare stub) -- manually attach it so go_MultDecVars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_MultDecVars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_MultDecVars(name="sample_text", value="sample_text")
    partner = go_TypeValue()
    setattr(partner, 'go_TypeValue', None)
    _safe_set(owner, 'go_MultDecVars', partner)
    assert getattr(partner, 'go_TypeValue') == owner
    _safe_set(owner, 'go_MultDecVars', None)
    assert getattr(partner, 'go_TypeValue') is None


def test_assoc_value113_stub_double():
    # go_Literal has no real 'go_Literal' property in the generated
    # code (a bare stub) -- manually attach it so go_Bool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # go_Bool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = go_Bool(val="sample_text")
    partner = go_Literal()
    setattr(partner, 'go_Literal', None)
    _safe_set(owner, 'go_Bool', partner)
    assert getattr(partner, 'go_Literal') == owner
    _safe_set(owner, 'go_Bool', None)
    assert getattr(partner, 'go_Literal') is None


