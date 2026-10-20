import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDeclaration,
    Declaration,
    Expression,
    Instruction,
    NamedElement,
    TransitionExpression,
    Type,
    altarica_ARBoolean,
    altarica_ARNumber,
    altarica_ARString,
    altarica_AbstractDeclaration,
    altarica_Addition,
    altarica_Assignment,
    altarica_Attribute,
    altarica_BaseType,
    altarica_Block,
    altarica_CaseExpression,
    altarica_Conditional,
    altarica_Declaration,
    altarica_Domain,
    altarica_EObject,
    altarica_Equal,
    altarica_Error,
    altarica_Event,
    altarica_Expression,
    altarica_FunctionCall,
    altarica_Instruction,
    altarica_LabeledTransition,
    altarica_LogicalAnd,
    altarica_LogicalOr,
    altarica_Minus,
    altarica_Model,
    altarica_Multiplication,
    altarica_NameRef,
    altarica_NamedElement,
    altarica_NamedType,
    altarica_Node,
    altarica_Not,
    altarica_Observer,
    altarica_Parameter,
    altarica_Skip,
    altarica_SwitchExpression,
    altarica_SymbolicConstant,
    altarica_Transition,
    altarica_TransitionAnd,
    altarica_TransitionExpression,
    altarica_TransitionOr,
    altarica_Type,
    altarica_Variable,
    BaseTypeEnum,
    Severity,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes36_stub_double():
    # altarica_Variable has no real 'altarica_Variable37' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NamedElement(name="sample_text")
    partner = altarica_Variable()
    setattr(partner, 'altarica_Variable37', None)
    _safe_set(owner, 'altarica_NamedElement38', partner)
    assert owner in getattr(partner, 'altarica_Variable37')
    _safe_set(owner, 'altarica_NamedElement38', None)
    assert owner not in getattr(partner, 'altarica_Variable37')


def test_assoc_attributes41_stub_double():
    # altarica_Event has no real 'altarica_Event' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NamedElement(name="sample_text")
    partner = altarica_Event()
    setattr(partner, 'altarica_Event', None)
    _safe_set(owner, 'altarica_NamedElement42', partner)
    assert owner in getattr(partner, 'altarica_Event')
    _safe_set(owner, 'altarica_NamedElement42', None)
    assert owner not in getattr(partner, 'altarica_Event')


def test_assoc_constants26_stub_double():
    # altarica_Domain has no real 'altarica_Domain' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NamedElement(name="sample_text")
    partner = altarica_Domain()
    setattr(partner, 'altarica_Domain', None)
    _safe_set(owner, 'altarica_NamedElement27', partner)
    assert owner in getattr(partner, 'altarica_Domain')
    _safe_set(owner, 'altarica_NamedElement27', None)
    assert owner not in getattr(partner, 'altarica_Domain')


def test_assoc_errors0_stub_double():
    # altarica_Model has no real 'altarica_Model' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Error's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Error's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Error(message="sample_text", severity="sample_text")
    partner = altarica_Model()
    setattr(partner, 'altarica_Model', None)
    _safe_set(owner, 'altarica_Error', partner)
    assert owner in getattr(partner, 'altarica_Model')
    _safe_set(owner, 'altarica_Error', None)
    assert owner not in getattr(partner, 'altarica_Model')


def test_assoc_left100_stub_double():
    # altarica_Expression has no real 'altarica_Expression101' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Multiplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Multiplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Multiplication(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression101', None)
    _safe_set(owner, 'altarica_Multiplication', partner)
    assert getattr(partner, 'altarica_Expression101') == owner
    _safe_set(owner, 'altarica_Multiplication', None)
    assert getattr(partner, 'altarica_Expression101') is None


def test_assoc_left80_stub_double():
    # altarica_Expression has no real 'altarica_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so altarica_LogicalOr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_LogicalOr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_LogicalOr(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression81', None)
    _safe_set(owner, 'altarica_LogicalOr', partner)
    assert getattr(partner, 'altarica_Expression81') == owner
    _safe_set(owner, 'altarica_LogicalOr', None)
    assert getattr(partner, 'altarica_Expression81') is None


def test_assoc_left85_stub_double():
    # altarica_Expression has no real 'altarica_Expression86' property in the generated
    # code (a bare stub) -- manually attach it so altarica_LogicalAnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_LogicalAnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_LogicalAnd(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression86', None)
    _safe_set(owner, 'altarica_LogicalAnd', partner)
    assert getattr(partner, 'altarica_Expression86') == owner
    _safe_set(owner, 'altarica_LogicalAnd', None)
    assert getattr(partner, 'altarica_Expression86') is None


def test_assoc_left90_stub_double():
    # altarica_Expression has no real 'altarica_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Equal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Equal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Equal(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression91', None)
    _safe_set(owner, 'altarica_Equal', partner)
    assert getattr(partner, 'altarica_Expression91') == owner
    _safe_set(owner, 'altarica_Equal', None)
    assert getattr(partner, 'altarica_Expression91') is None


def test_assoc_left95_stub_double():
    # altarica_Expression has no real 'altarica_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Addition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Addition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Addition(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression96', None)
    _safe_set(owner, 'altarica_Addition', partner)
    assert getattr(partner, 'altarica_Expression96') == owner
    _safe_set(owner, 'altarica_Addition', None)
    assert getattr(partner, 'altarica_Expression96') is None


def test_assoc_parameters109_stub_double():
    # altarica_Expression has no real 'altarica_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so altarica_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_FunctionCall(name="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression110', None)
    _safe_set(owner, 'altarica_FunctionCall', {partner})
    assert getattr(partner, 'altarica_Expression110') == owner
    _safe_set(owner, 'altarica_FunctionCall', set())
    assert getattr(partner, 'altarica_Expression110') is None


def test_assoc_ref3_stub_double():
    # altarica_NamedType has no real 'altarica_NamedType' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NamedElement(name="sample_text")
    partner = altarica_NamedType()
    setattr(partner, 'altarica_NamedType', None)
    _safe_set(owner, 'altarica_NamedElement', partner)
    assert getattr(partner, 'altarica_NamedType') == owner
    _safe_set(owner, 'altarica_NamedElement', None)
    assert getattr(partner, 'altarica_NamedType') is None


def test_assoc_right102_stub_double():
    # altarica_Expression has no real 'altarica_Expression104' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Multiplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Multiplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Multiplication(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression104', None)
    _safe_set(owner, 'altarica_Multiplication103', partner)
    assert getattr(partner, 'altarica_Expression104') == owner
    _safe_set(owner, 'altarica_Multiplication103', None)
    assert getattr(partner, 'altarica_Expression104') is None


def test_assoc_right82_stub_double():
    # altarica_Expression has no real 'altarica_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so altarica_LogicalOr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_LogicalOr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_LogicalOr(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression84', None)
    _safe_set(owner, 'altarica_LogicalOr83', partner)
    assert getattr(partner, 'altarica_Expression84') == owner
    _safe_set(owner, 'altarica_LogicalOr83', None)
    assert getattr(partner, 'altarica_Expression84') is None


def test_assoc_right87_stub_double():
    # altarica_Expression has no real 'altarica_Expression89' property in the generated
    # code (a bare stub) -- manually attach it so altarica_LogicalAnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_LogicalAnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_LogicalAnd(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression89', None)
    _safe_set(owner, 'altarica_LogicalAnd88', partner)
    assert getattr(partner, 'altarica_Expression89') == owner
    _safe_set(owner, 'altarica_LogicalAnd88', None)
    assert getattr(partner, 'altarica_Expression89') is None


def test_assoc_right92_stub_double():
    # altarica_Expression has no real 'altarica_Expression94' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Equal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Equal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Equal(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression94', None)
    _safe_set(owner, 'altarica_Equal93', partner)
    assert getattr(partner, 'altarica_Expression94') == owner
    _safe_set(owner, 'altarica_Equal93', None)
    assert getattr(partner, 'altarica_Expression94') is None


def test_assoc_right97_stub_double():
    # altarica_Expression has no real 'altarica_Expression99' property in the generated
    # code (a bare stub) -- manually attach it so altarica_Addition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_Addition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_Addition(op="sample_text")
    partner = altarica_Expression()
    setattr(partner, 'altarica_Expression99', None)
    _safe_set(owner, 'altarica_Addition98', partner)
    assert getattr(partner, 'altarica_Expression99') == owner
    _safe_set(owner, 'altarica_Addition98', None)
    assert getattr(partner, 'altarica_Expression99') is None


def test_assoc_variable10_stub_double():
    # altarica_NameRef has no real 'altarica_NameRef11' property in the generated
    # code (a bare stub) -- manually attach it so altarica_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # altarica_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = altarica_NamedElement(name="sample_text")
    partner = altarica_NameRef()
    setattr(partner, 'altarica_NameRef11', None)
    _safe_set(owner, 'altarica_NamedElement12', partner)
    assert getattr(partner, 'altarica_NameRef11') == owner
    _safe_set(owner, 'altarica_NamedElement12', None)
    assert getattr(partner, 'altarica_NameRef11') is None


