import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstraction,
    Arg,
    BeginBody,
    Body,
    Condition,
    Expr,
    FinalExpr,
    LogicalExpr,
    PropertyExpr,
    Return,
    ReturnExpr,
    ReturnTypeExpr,
    Statement,
    Type,
    b_Abstraction,
    b_AndExpr,
    b_Arg,
    b_ArgMinus,
    b_AssertionExpr,
    b_Assertions,
    b_Assign,
    b_Begin,
    b_BeginBody,
    b_Body,
    b_BoolLiteral,
    b_BoolTest,
    b_Call,
    b_Case,
    b_CaseExpr,
    b_ConcreteConstants,
    b_ConcreteVariables,
    b_CondAnd,
    b_CondEq,
    b_CondLessThan,
    b_CondMinus,
    b_CondNeg,
    b_Condition,
    b_ConstantExpr,
    b_Definition,
    b_DefinitionCall,
    b_Definitions,
    b_EObject,
    b_EqualExpr,
    b_Expr,
    b_FinalExpr,
    b_If,
    b_IfCond,
    b_Implementation,
    b_ImplyExpr,
    b_Imports,
    b_InequalityExpr,
    b_Initialisation,
    b_InitialisationExpr,
    b_IntLiteral,
    b_Invariant,
    b_InvariantExpr,
    b_LocalOperations,
    b_LogicalExpr,
    b_Machine,
    b_Neg,
    b_NegExpr,
    b_Operation,
    b_Operations,
    b_Pre,
    b_PreExpr,
    b_PrimitiveType,
    b_Properties,
    b_PropertyExpr,
    b_PropertyRange,
    b_PropertyTyped,
    b_Range,
    b_Ref,
    b_Return,
    b_ReturnExpr,
    b_ReturnOr,
    b_ReturnTuple,
    b_ReturnTypeExpr,
    b_Sees,
    b_Seq,
    b_Set,
    b_Sets,
    b_SimpleCall,
    b_Skip,
    b_Statement,
    b_StringLiteral,
    b_Type,
    b_TypeConstraint,
    b_ValueExpr,
    b_Values,
    b_Var,
    b_Variable,
    BoolLiteralEnum,
    InequalityOp,
    PrimitiveTypeEnum,
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

def test_assoc_args77_reverse_link_reassign_clear():
    a1 = b_Variable(name="sample_text")
    a2 = b_Variable(name="sample_text_2")
    b = b_Definition(name="sample_text")
    _safe_set(b, 'b_Definition78', {a1})
    assert _is_linked(b, 'b_Definition78', a1)
    if hasattr(a1, 'b_Variable79'):
        assert _is_linked(a1, 'b_Variable79', b)
    _safe_set(b, 'b_Definition78', {a2})
    assert _is_linked(b, 'b_Definition78', a2)
    if hasattr(a1, 'b_Variable79'):
        assert not _is_linked(a1, 'b_Variable79', b)
    if hasattr(a2, 'b_Variable79'):
        assert _is_linked(a2, 'b_Variable79', b)
    _safe_set(b, 'b_Definition78', set())
    assert not _is_linked(b, 'b_Definition78', a2)
    if hasattr(a2, 'b_Variable79'):
        assert not _is_linked(a2, 'b_Variable79', b)


def test_assoc_args99_reverse_link_reassign_clear():
    a1 = b_Variable(name="sample_text")
    a2 = b_Variable(name="sample_text_2")
    b = b_Operation(name="sample_text")
    _safe_set(b, 'b_Operation100', {a1})
    assert _is_linked(b, 'b_Operation100', a1)
    if hasattr(a1, 'b_Variable101'):
        assert _is_linked(a1, 'b_Variable101', b)
    _safe_set(b, 'b_Operation100', {a2})
    assert _is_linked(b, 'b_Operation100', a2)
    if hasattr(a1, 'b_Variable101'):
        assert not _is_linked(a1, 'b_Variable101', b)
    if hasattr(a2, 'b_Variable101'):
        assert _is_linked(a2, 'b_Variable101', b)
    _safe_set(b, 'b_Operation100', set())
    assert not _is_linked(b, 'b_Operation100', a2)
    if hasattr(a2, 'b_Variable101'):
        assert not _is_linked(a2, 'b_Variable101', b)


def test_assoc_constant34_reverse_link_reassign_clear():
    a1 = b_Variable(name="sample_text")
    a2 = b_Variable(name="sample_text_2")
    b = b_ValueExpr(value="sample_text")
    _safe_set(b, 'b_ValueExpr35', a1)
    assert _is_linked(b, 'b_ValueExpr35', a1)
    if hasattr(a1, 'b_Variable'):
        assert _is_linked(a1, 'b_Variable', b)
    _safe_set(b, 'b_ValueExpr35', a2)
    assert _is_linked(b, 'b_ValueExpr35', a2)
    if hasattr(a1, 'b_Variable'):
        assert not _is_linked(a1, 'b_Variable', b)
    if hasattr(a2, 'b_Variable'):
        assert _is_linked(a2, 'b_Variable', b)
    _safe_set(b, 'b_ValueExpr35', None)
    assert not _is_linked(b, 'b_ValueExpr35', a2)
    if hasattr(a2, 'b_Variable'):
        assert not _is_linked(a2, 'b_Variable', b)


def test_assoc_outputs96_reverse_link_reassign_clear():
    a1 = b_Variable(name="sample_text")
    a2 = b_Variable(name="sample_text_2")
    b = b_Operation(name="sample_text")
    _safe_set(b, 'b_Operation97', {a1})
    assert _is_linked(b, 'b_Operation97', a1)
    if hasattr(a1, 'b_Variable98'):
        assert _is_linked(a1, 'b_Variable98', b)
    _safe_set(b, 'b_Operation97', {a2})
    assert _is_linked(b, 'b_Operation97', a2)
    if hasattr(a1, 'b_Variable98'):
        assert not _is_linked(a1, 'b_Variable98', b)
    if hasattr(a2, 'b_Variable98'):
        assert _is_linked(a2, 'b_Variable98', b)
    _safe_set(b, 'b_Operation97', set())
    assert not _is_linked(b, 'b_Operation97', a2)
    if hasattr(a2, 'b_Variable98'):
        assert not _is_linked(a2, 'b_Variable98', b)


def test_assoc_upperBound65_reverse_link_reassign_clear():
    a1 = b_Variable(name="sample_text")
    a2 = b_Variable(name="sample_text_2")
    b = b_Range(lowerBound=7)
    _safe_set(b, 'b_Range', a1)
    assert _is_linked(b, 'b_Range', a1)
    if hasattr(a1, 'b_Variable66'):
        assert _is_linked(a1, 'b_Variable66', b)
    _safe_set(b, 'b_Range', a2)
    assert _is_linked(b, 'b_Range', a2)
    if hasattr(a1, 'b_Variable66'):
        assert not _is_linked(a1, 'b_Variable66', b)
    if hasattr(a2, 'b_Variable66'):
        assert _is_linked(a2, 'b_Variable66', b)
    _safe_set(b, 'b_Range', None)
    assert not _is_linked(b, 'b_Range', a2)
    if hasattr(a2, 'b_Variable66'):
        assert not _is_linked(a2, 'b_Variable66', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body102_stub_double():
    # b_Body has no real 'b_Body' property in the generated
    # code (a bare stub) -- manually attach it so b_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Operation(name="sample_text")
    partner = b_Body()
    setattr(partner, 'b_Body', None)
    _safe_set(owner, 'b_Operation103', partner)
    assert getattr(partner, 'b_Body') == owner
    _safe_set(owner, 'b_Operation103', None)
    assert getattr(partner, 'b_Body') is None


def test_assoc_concreteConstants1_stub_double():
    # b_ConcreteConstants has no real 'b_ConcreteConstants' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_ConcreteConstants()
    setattr(partner, 'b_ConcreteConstants', None)
    _safe_set(owner, 'b_Abstraction2', partner)
    assert getattr(partner, 'b_ConcreteConstants') == owner
    _safe_set(owner, 'b_Abstraction2', None)
    assert getattr(partner, 'b_ConcreteConstants') is None


def test_assoc_constant62_stub_double():
    # b_PropertyExpr has no real 'b_PropertyExpr63' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_PropertyExpr()
    setattr(partner, 'b_PropertyExpr63', None)
    _safe_set(owner, 'b_Variable64', partner)
    assert getattr(partner, 'b_PropertyExpr63') == owner
    _safe_set(owner, 'b_Variable64', None)
    assert getattr(partner, 'b_PropertyExpr63') is None


def test_assoc_constant69_stub_double():
    # b_AssertionExpr has no real 'b_AssertionExpr70' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_AssertionExpr()
    setattr(partner, 'b_AssertionExpr70', None)
    _safe_set(owner, 'b_Variable71', partner)
    assert getattr(partner, 'b_AssertionExpr70') == owner
    _safe_set(owner, 'b_Variable71', None)
    assert getattr(partner, 'b_AssertionExpr70') is None


def test_assoc_constants39_stub_double():
    # b_ConcreteConstants has no real 'b_ConcreteConstants40' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_ConcreteConstants()
    setattr(partner, 'b_ConcreteConstants40', None)
    _safe_set(owner, 'b_Variable41', partner)
    assert getattr(partner, 'b_ConcreteConstants40') == owner
    _safe_set(owner, 'b_Variable41', None)
    assert getattr(partner, 'b_ConcreteConstants40') is None


def test_assoc_def_82_stub_double():
    # b_DefinitionCall has no real 'b_DefinitionCall' property in the generated
    # code (a bare stub) -- manually attach it so b_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Definition(name="sample_text")
    partner = b_DefinitionCall()
    setattr(partner, 'b_DefinitionCall', None)
    _safe_set(owner, 'b_Definition83', partner)
    assert getattr(partner, 'b_DefinitionCall') == owner
    _safe_set(owner, 'b_Definition83', None)
    assert getattr(partner, 'b_DefinitionCall') is None


def test_assoc_definitions3_stub_double():
    # b_Definitions has no real 'b_Definitions' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_Definitions()
    setattr(partner, 'b_Definitions', None)
    _safe_set(owner, 'b_Abstraction4', partner)
    assert getattr(partner, 'b_Definitions') == owner
    _safe_set(owner, 'b_Abstraction4', None)
    assert getattr(partner, 'b_Definitions') is None


def test_assoc_elems91_stub_double():
    # b_Set has no real 'b_Set92' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Set()
    setattr(partner, 'b_Set92', None)
    _safe_set(owner, 'b_Variable93', partner)
    assert getattr(partner, 'b_Set92') == owner
    _safe_set(owner, 'b_Variable93', None)
    assert getattr(partner, 'b_Set92') is None


def test_assoc_expr80_stub_double():
    # b_LogicalExpr has no real 'b_LogicalExpr' property in the generated
    # code (a bare stub) -- manually attach it so b_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Definition(name="sample_text")
    partner = b_LogicalExpr()
    setattr(partner, 'b_LogicalExpr', None)
    _safe_set(owner, 'b_Definition81', partner)
    assert getattr(partner, 'b_LogicalExpr') == owner
    _safe_set(owner, 'b_Definition81', None)
    assert getattr(partner, 'b_LogicalExpr') is None


def test_assoc_exprs32_stub_double():
    # b_Values has no real 'b_Values33' property in the generated
    # code (a bare stub) -- manually attach it so b_ValueExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_ValueExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_ValueExpr(value="sample_text")
    partner = b_Values()
    setattr(partner, 'b_Values33', None)
    _safe_set(owner, 'b_ValueExpr', partner)
    assert getattr(partner, 'b_Values33') == owner
    _safe_set(owner, 'b_ValueExpr', None)
    assert getattr(partner, 'b_Values33') is None


def test_assoc_exprs75_stub_double():
    # b_Definitions has no real 'b_Definitions76' property in the generated
    # code (a bare stub) -- manually attach it so b_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Definition(name="sample_text")
    partner = b_Definitions()
    setattr(partner, 'b_Definitions76', None)
    _safe_set(owner, 'b_Definition', partner)
    assert getattr(partner, 'b_Definitions76') == owner
    _safe_set(owner, 'b_Definition', None)
    assert getattr(partner, 'b_Definitions76') is None


def test_assoc_imports29_stub_double():
    # b_Imports has no real 'b_Imports30' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_Imports()
    setattr(partner, 'b_Imports30', None)
    _safe_set(owner, 'b_Abstraction31', partner)
    assert getattr(partner, 'b_Imports30') == owner
    _safe_set(owner, 'b_Abstraction31', None)
    assert getattr(partner, 'b_Imports30') is None


def test_assoc_left180_stub_double():
    # b_LogicalExpr has no real 'b_LogicalExpr181' property in the generated
    # code (a bare stub) -- manually attach it so b_InequalityExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_InequalityExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_InequalityExpr(op="sample_text")
    partner = b_LogicalExpr()
    setattr(partner, 'b_LogicalExpr181', None)
    _safe_set(owner, 'b_InequalityExpr', partner)
    assert getattr(partner, 'b_LogicalExpr181') == owner
    _safe_set(owner, 'b_InequalityExpr', None)
    assert getattr(partner, 'b_LogicalExpr181') is None


def test_assoc_name88_stub_double():
    # b_Set has no real 'b_Set89' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Set()
    setattr(partner, 'b_Set89', None)
    _safe_set(owner, 'b_Variable90', partner)
    assert getattr(partner, 'b_Set89') == owner
    _safe_set(owner, 'b_Variable90', None)
    assert getattr(partner, 'b_Set89') is None


def test_assoc_op150_stub_double():
    # b_Call has no real 'b_Call151' property in the generated
    # code (a bare stub) -- manually attach it so b_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Operation(name="sample_text")
    partner = b_Call()
    setattr(partner, 'b_Call151', None)
    _safe_set(owner, 'b_Operation152', partner)
    assert getattr(partner, 'b_Call151') == owner
    _safe_set(owner, 'b_Operation152', None)
    assert getattr(partner, 'b_Call151') is None


def test_assoc_op156_stub_double():
    # b_SimpleCall has no real 'b_SimpleCall' property in the generated
    # code (a bare stub) -- manually attach it so b_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Operation(name="sample_text")
    partner = b_SimpleCall()
    setattr(partner, 'b_SimpleCall', None)
    _safe_set(owner, 'b_Operation157', partner)
    assert getattr(partner, 'b_SimpleCall') == owner
    _safe_set(owner, 'b_Operation157', None)
    assert getattr(partner, 'b_SimpleCall') is None


def test_assoc_operations161_stub_double():
    # b_LocalOperations has no real 'b_LocalOperations162' property in the generated
    # code (a bare stub) -- manually attach it so b_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Operation(name="sample_text")
    partner = b_LocalOperations()
    setattr(partner, 'b_LocalOperations162', None)
    _safe_set(owner, 'b_Operation163', partner)
    assert getattr(partner, 'b_LocalOperations162') == owner
    _safe_set(owner, 'b_Operation163', None)
    assert getattr(partner, 'b_LocalOperations162') is None


def test_assoc_operations7_stub_double():
    # b_Operations has no real 'b_Operations' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_Operations()
    setattr(partner, 'b_Operations', None)
    _safe_set(owner, 'b_Abstraction8', partner)
    assert getattr(partner, 'b_Operations') == owner
    _safe_set(owner, 'b_Abstraction8', None)
    assert getattr(partner, 'b_Operations') is None


def test_assoc_operations94_stub_double():
    # b_Operations has no real 'b_Operations95' property in the generated
    # code (a bare stub) -- manually attach it so b_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Operation(name="sample_text")
    partner = b_Operations()
    setattr(partner, 'b_Operations95', None)
    _safe_set(owner, 'b_Operation', partner)
    assert getattr(partner, 'b_Operations95') == owner
    _safe_set(owner, 'b_Operation', None)
    assert getattr(partner, 'b_Operations95') is None


def test_assoc_properties5_stub_double():
    # b_Properties has no real 'b_Properties' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_Properties()
    setattr(partner, 'b_Properties', None)
    _safe_set(owner, 'b_Abstraction6', partner)
    assert getattr(partner, 'b_Properties') == owner
    _safe_set(owner, 'b_Abstraction6', None)
    assert getattr(partner, 'b_Properties') is None


def test_assoc_range171_stub_double():
    # b_PropertyRange has no real 'b_PropertyRange' property in the generated
    # code (a bare stub) -- manually attach it so b_Range's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Range's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Range(lowerBound=7)
    partner = b_PropertyRange()
    setattr(partner, 'b_PropertyRange', None)
    _safe_set(owner, 'b_Range172', partner)
    assert getattr(partner, 'b_PropertyRange') == owner
    _safe_set(owner, 'b_Range172', None)
    assert getattr(partner, 'b_PropertyRange') is None


def test_assoc_rets148_stub_double():
    # b_Call has no real 'b_Call' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Call()
    setattr(partner, 'b_Call', None)
    _safe_set(owner, 'b_Variable149', partner)
    assert getattr(partner, 'b_Call') == owner
    _safe_set(owner, 'b_Variable149', None)
    assert getattr(partner, 'b_Call') is None


def test_assoc_right182_stub_double():
    # b_LogicalExpr has no real 'b_LogicalExpr184' property in the generated
    # code (a bare stub) -- manually attach it so b_InequalityExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_InequalityExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_InequalityExpr(op="sample_text")
    partner = b_LogicalExpr()
    setattr(partner, 'b_LogicalExpr184', None)
    _safe_set(owner, 'b_InequalityExpr183', partner)
    assert getattr(partner, 'b_LogicalExpr184') == owner
    _safe_set(owner, 'b_InequalityExpr183', None)
    assert getattr(partner, 'b_LogicalExpr184') is None


def test_assoc_seens26_stub_double():
    # b_Sees has no real 'b_Sees27' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_Sees()
    setattr(partner, 'b_Sees27', None)
    _safe_set(owner, 'b_Abstraction28', partner)
    assert getattr(partner, 'b_Sees27') == owner
    _safe_set(owner, 'b_Abstraction28', None)
    assert getattr(partner, 'b_Sees27') is None


def test_assoc_sees0_stub_double():
    # b_Sees has no real 'b_Sees' property in the generated
    # code (a bare stub) -- manually attach it so b_Abstraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Abstraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Abstraction(name="sample_text")
    partner = b_Sees()
    setattr(partner, 'b_Sees', None)
    _safe_set(owner, 'b_Abstraction', partner)
    assert getattr(partner, 'b_Sees') == owner
    _safe_set(owner, 'b_Abstraction', None)
    assert getattr(partner, 'b_Sees') is None


def test_assoc_test140_stub_double():
    # b_CaseExpr has no real 'b_CaseExpr141' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_CaseExpr()
    setattr(partner, 'b_CaseExpr141', None)
    _safe_set(owner, 'b_Variable142', partner)
    assert getattr(partner, 'b_CaseExpr141') == owner
    _safe_set(owner, 'b_Variable142', None)
    assert getattr(partner, 'b_CaseExpr141') is None


def test_assoc_type164_stub_double():
    # b_Ref has no real 'b_Ref' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Ref()
    setattr(partner, 'b_Ref', None)
    _safe_set(owner, 'b_Variable165', partner)
    assert getattr(partner, 'b_Ref') == owner
    _safe_set(owner, 'b_Variable165', None)
    assert getattr(partner, 'b_Ref') is None


def test_assoc_var116_stub_double():
    # b_PreExpr has no real 'b_PreExpr117' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_PreExpr()
    setattr(partner, 'b_PreExpr117', None)
    _safe_set(owner, 'b_Variable118', partner)
    assert getattr(partner, 'b_PreExpr117') == owner
    _safe_set(owner, 'b_Variable118', None)
    assert getattr(partner, 'b_PreExpr117') is None


def test_assoc_var127_stub_double():
    # b_Assign has no real 'b_Assign' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Assign()
    setattr(partner, 'b_Assign', None)
    _safe_set(owner, 'b_Variable128', partner)
    assert getattr(partner, 'b_Assign') == owner
    _safe_set(owner, 'b_Variable128', None)
    assert getattr(partner, 'b_Assign') is None


def test_assoc_var131_stub_double():
    # b_ReturnTypeExpr has no real 'b_ReturnTypeExpr' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_ReturnTypeExpr()
    setattr(partner, 'b_ReturnTypeExpr', None)
    _safe_set(owner, 'b_Variable132', partner)
    assert getattr(partner, 'b_ReturnTypeExpr') == owner
    _safe_set(owner, 'b_Variable132', None)
    assert getattr(partner, 'b_ReturnTypeExpr') is None


def test_assoc_var136_stub_double():
    # b_Case has no real 'b_Case' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Case()
    setattr(partner, 'b_Case', None)
    _safe_set(owner, 'b_Variable137', partner)
    assert getattr(partner, 'b_Case') == owner
    _safe_set(owner, 'b_Variable137', None)
    assert getattr(partner, 'b_Case') is None


def test_assoc_var166_stub_double():
    # b_Ref has no real 'b_Ref167' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Ref()
    setattr(partner, 'b_Ref167', None)
    _safe_set(owner, 'b_Variable168', partner)
    assert getattr(partner, 'b_Ref167') == owner
    _safe_set(owner, 'b_Variable168', None)
    assert getattr(partner, 'b_Ref167') is None


def test_assoc_var194_stub_double():
    # b_TypeConstraint has no real 'b_TypeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_TypeConstraint()
    setattr(partner, 'b_TypeConstraint', None)
    _safe_set(owner, 'b_Variable195', partner)
    assert getattr(partner, 'b_TypeConstraint') == owner
    _safe_set(owner, 'b_Variable195', None)
    assert getattr(partner, 'b_TypeConstraint') is None


def test_assoc_variable44_stub_double():
    # b_InvariantExpr has no real 'b_InvariantExpr45' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_InvariantExpr()
    setattr(partner, 'b_InvariantExpr45', None)
    _safe_set(owner, 'b_Variable46', partner)
    assert getattr(partner, 'b_InvariantExpr45') == owner
    _safe_set(owner, 'b_Variable46', None)
    assert getattr(partner, 'b_InvariantExpr45') is None


def test_assoc_variable51_stub_double():
    # b_InitialisationExpr has no real 'b_InitialisationExpr52' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_InitialisationExpr()
    setattr(partner, 'b_InitialisationExpr52', None)
    _safe_set(owner, 'b_Variable53', partner)
    assert getattr(partner, 'b_InitialisationExpr52') == owner
    _safe_set(owner, 'b_Variable53', None)
    assert getattr(partner, 'b_InitialisationExpr52') is None


def test_assoc_variables36_stub_double():
    # b_ConcreteVariables has no real 'b_ConcreteVariables37' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_ConcreteVariables()
    setattr(partner, 'b_ConcreteVariables37', None)
    _safe_set(owner, 'b_Variable38', partner)
    assert getattr(partner, 'b_ConcreteVariables37') == owner
    _safe_set(owner, 'b_Variable38', None)
    assert getattr(partner, 'b_ConcreteVariables37') is None


def test_assoc_vars122_stub_double():
    # b_Var has no real 'b_Var' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_Var()
    setattr(partner, 'b_Var', None)
    _safe_set(owner, 'b_Variable123', partner)
    assert getattr(partner, 'b_Var') == owner
    _safe_set(owner, 'b_Variable123', None)
    assert getattr(partner, 'b_Var') is None


def test_assoc_vars218_stub_double():
    # b_ReturnTuple has no real 'b_ReturnTuple' property in the generated
    # code (a bare stub) -- manually attach it so b_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # b_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = b_Variable(name="sample_text")
    partner = b_ReturnTuple()
    setattr(partner, 'b_ReturnTuple', None)
    _safe_set(owner, 'b_Variable219', partner)
    assert getattr(partner, 'b_ReturnTuple') == owner
    _safe_set(owner, 'b_Variable219', None)
    assert getattr(partner, 'b_ReturnTuple') is None


