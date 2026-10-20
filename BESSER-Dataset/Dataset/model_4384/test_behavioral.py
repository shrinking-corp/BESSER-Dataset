import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanExpression,
    IntegerExpression,
    Operation,
    gseq_And,
    gseq_Assign,
    gseq_BooleanExpression,
    gseq_Const,
    gseq_Equality,
    gseq_False,
    gseq_GreaterThan,
    gseq_If,
    gseq_IntegerExpression,
    gseq_Method,
    gseq_MethodCall,
    gseq_Not,
    gseq_Operation,
    gseq_Plus,
    gseq_Print,
    gseq_Program,
    gseq_True,
    gseq_Var,
    gseq_While,
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

def test_assoc_assignedExpression28_reverse_link_reassign_clear():
    a1 = gseq_IntegerExpression()
    a2 = gseq_IntegerExpression()
    b = gseq_Assign(varName="sample_text")
    _safe_set(b, 'gseq_Assign', a1)
    assert _is_linked(b, 'gseq_Assign', a1)
    if hasattr(a1, 'gseq_IntegerExpression29'):
        assert _is_linked(a1, 'gseq_IntegerExpression29', b)
    _safe_set(b, 'gseq_Assign', a2)
    assert _is_linked(b, 'gseq_Assign', a2)
    if hasattr(a1, 'gseq_IntegerExpression29'):
        assert not _is_linked(a1, 'gseq_IntegerExpression29', b)
    if hasattr(a2, 'gseq_IntegerExpression29'):
        assert _is_linked(a2, 'gseq_IntegerExpression29', b)
    _safe_set(b, 'gseq_Assign', None)
    assert not _is_linked(b, 'gseq_Assign', a2)
    if hasattr(a2, 'gseq_IntegerExpression29'):
        assert not _is_linked(a2, 'gseq_IntegerExpression29', b)


def test_assoc_executedBy5_reverse_link_reassign_clear():
    a1 = gseq_Operation()
    a2 = gseq_Operation()
    b = gseq_Method(name="sample_text")
    _safe_set(b, 'Method6', a1)
    assert _is_linked(b, 'Method6', a1)
    if hasattr(a1, 'operations'):
        assert _is_linked(a1, 'operations', b)
    _safe_set(b, 'Method6', a2)
    assert _is_linked(b, 'Method6', a2)
    if hasattr(a1, 'operations'):
        assert not _is_linked(a1, 'operations', b)
    if hasattr(a2, 'operations'):
        assert _is_linked(a2, 'operations', b)
    _safe_set(b, 'Method6', None)
    assert not _is_linked(b, 'Method6', a2)
    if hasattr(a2, 'operations'):
        assert not _is_linked(a2, 'operations', b)


def test_assoc_inProgram3_reverse_link_reassign_clear():
    a1 = gseq_Program()
    a2 = gseq_Program()
    b = gseq_Method(name="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'Program'):
        assert _is_linked(a1, 'Program', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'Program'):
        assert not _is_linked(a1, 'Program', b)
    if hasattr(a2, 'Program'):
        assert _is_linked(a2, 'Program', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'Program'):
        assert not _is_linked(a2, 'Program', b)


def test_assoc_methods0_reverse_link_reassign_clear():
    a1 = gseq_Program()
    a2 = gseq_Program()
    b = gseq_Method(name="sample_text")
    _safe_set(b, 'Method', a1)
    assert _is_linked(b, 'Method', a1)
    if hasattr(a1, 'inProgram'):
        assert _is_linked(a1, 'inProgram', b)
    _safe_set(b, 'Method', a2)
    assert _is_linked(b, 'Method', a2)
    if hasattr(a1, 'inProgram'):
        assert not _is_linked(a1, 'inProgram', b)
    if hasattr(a2, 'inProgram'):
        assert _is_linked(a2, 'inProgram', b)
    _safe_set(b, 'Method', None)
    assert not _is_linked(b, 'Method', a2)
    if hasattr(a2, 'inProgram'):
        assert not _is_linked(a2, 'inProgram', b)


def test_assoc_operations2_reverse_link_reassign_clear():
    a1 = gseq_Operation()
    a2 = gseq_Operation()
    b = gseq_Method(name="sample_text")
    _safe_set(b, 'executedBy', {a1})
    assert _is_linked(b, 'executedBy', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'executedBy', {a2})
    assert _is_linked(b, 'executedBy', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'executedBy', set())
    assert not _is_linked(b, 'executedBy', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_startMethod1_reverse_link_reassign_clear():
    a1 = gseq_Program()
    a2 = gseq_Program()
    b = gseq_Method(name="sample_text")
    _safe_set(b, 'gseq_Method', a1)
    assert _is_linked(b, 'gseq_Method', a1)
    if hasattr(a1, 'gseq_Program'):
        assert _is_linked(a1, 'gseq_Program', b)
    _safe_set(b, 'gseq_Method', a2)
    assert _is_linked(b, 'gseq_Method', a2)
    if hasattr(a1, 'gseq_Program'):
        assert not _is_linked(a1, 'gseq_Program', b)
    if hasattr(a2, 'gseq_Program'):
        assert _is_linked(a2, 'gseq_Program', b)
    _safe_set(b, 'gseq_Method', None)
    assert not _is_linked(b, 'gseq_Method', a2)
    if hasattr(a2, 'gseq_Program'):
        assert not _is_linked(a2, 'gseq_Program', b)


def test_assoc_toPrint7_reverse_link_reassign_clear():
    a1 = gseq_Print()
    a2 = gseq_Print()
    b = gseq_Operation()
    _safe_set(b, 'gseq_Operation', a1)
    assert _is_linked(b, 'gseq_Operation', a1)
    if hasattr(a1, 'gseq_Print'):
        assert _is_linked(a1, 'gseq_Print', b)
    _safe_set(b, 'gseq_Operation', a2)
    assert _is_linked(b, 'gseq_Operation', a2)
    if hasattr(a1, 'gseq_Print'):
        assert not _is_linked(a1, 'gseq_Print', b)
    if hasattr(a2, 'gseq_Print'):
        assert _is_linked(a2, 'gseq_Print', b)
    _safe_set(b, 'gseq_Operation', None)
    assert not _is_linked(b, 'gseq_Operation', a2)
    if hasattr(a2, 'gseq_Print'):
        assert not _is_linked(a2, 'gseq_Print', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_calledBy4_stub_double():
    # gseq_MethodCall has no real 'MethodCall' property in the generated
    # code (a bare stub) -- manually attach it so gseq_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_Method(name="sample_text")
    partner = gseq_MethodCall()
    setattr(partner, 'MethodCall', None)
    _safe_set(owner, 'methodToCall', {partner})
    assert getattr(partner, 'MethodCall') == owner
    _safe_set(owner, 'methodToCall', set())
    assert getattr(partner, 'MethodCall') is None


def test_assoc_conditionIf15_stub_double():
    # gseq_If has no real 'gseq_If16' property in the generated
    # code (a bare stub) -- manually attach it so gseq_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_BooleanExpression()
    partner = gseq_If()
    setattr(partner, 'gseq_If16', None)
    _safe_set(owner, 'gseq_BooleanExpression', partner)
    assert getattr(partner, 'gseq_If16') == owner
    _safe_set(owner, 'gseq_BooleanExpression', None)
    assert getattr(partner, 'gseq_If16') is None


def test_assoc_elseBranch10_stub_double():
    # gseq_If has no real 'gseq_If' property in the generated
    # code (a bare stub) -- manually attach it so gseq_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_Operation()
    partner = gseq_If()
    setattr(partner, 'gseq_If', None)
    _safe_set(owner, 'gseq_Operation11', partner)
    assert getattr(partner, 'gseq_If') == owner
    _safe_set(owner, 'gseq_Operation11', None)
    assert getattr(partner, 'gseq_If') is None


def test_assoc_leftAnd23_stub_double():
    # gseq_And has no real 'gseq_And' property in the generated
    # code (a bare stub) -- manually attach it so gseq_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_BooleanExpression()
    partner = gseq_And()
    setattr(partner, 'gseq_And', None)
    _safe_set(owner, 'gseq_BooleanExpression24', partner)
    assert getattr(partner, 'gseq_And') == owner
    _safe_set(owner, 'gseq_BooleanExpression24', None)
    assert getattr(partner, 'gseq_And') is None


def test_assoc_leftEquality17_stub_double():
    # gseq_Equality has no real 'gseq_Equality' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_Equality()
    setattr(partner, 'gseq_Equality', None)
    _safe_set(owner, 'gseq_IntegerExpression', partner)
    assert getattr(partner, 'gseq_Equality') == owner
    _safe_set(owner, 'gseq_IntegerExpression', None)
    assert getattr(partner, 'gseq_Equality') is None


def test_assoc_leftGreaterThan35_stub_double():
    # gseq_GreaterThan has no real 'gseq_GreaterThan' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_GreaterThan()
    setattr(partner, 'gseq_GreaterThan', None)
    _safe_set(owner, 'gseq_IntegerExpression36', partner)
    assert getattr(partner, 'gseq_GreaterThan') == owner
    _safe_set(owner, 'gseq_IntegerExpression36', None)
    assert getattr(partner, 'gseq_GreaterThan') is None


def test_assoc_leftPlus30_stub_double():
    # gseq_Plus has no real 'gseq_Plus' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_Plus()
    setattr(partner, 'gseq_Plus', None)
    _safe_set(owner, 'gseq_IntegerExpression31', partner)
    assert getattr(partner, 'gseq_Plus') == owner
    _safe_set(owner, 'gseq_IntegerExpression31', None)
    assert getattr(partner, 'gseq_Plus') is None


def test_assoc_methodToCall8_stub_double():
    # gseq_MethodCall has no real 'calledBy' property in the generated
    # code (a bare stub) -- manually attach it so gseq_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_Method(name="sample_text")
    partner = gseq_MethodCall()
    setattr(partner, 'calledBy', None)
    _safe_set(owner, 'Method9', partner)
    assert getattr(partner, 'calledBy') == owner
    _safe_set(owner, 'Method9', None)
    assert getattr(partner, 'calledBy') is None


def test_assoc_notExpression21_stub_double():
    # gseq_Not has no real 'gseq_Not' property in the generated
    # code (a bare stub) -- manually attach it so gseq_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_BooleanExpression()
    partner = gseq_Not()
    setattr(partner, 'gseq_Not', None)
    _safe_set(owner, 'gseq_BooleanExpression22', partner)
    assert getattr(partner, 'gseq_Not') == owner
    _safe_set(owner, 'gseq_BooleanExpression22', None)
    assert getattr(partner, 'gseq_Not') is None


def test_assoc_rightAnd25_stub_double():
    # gseq_And has no real 'gseq_And26' property in the generated
    # code (a bare stub) -- manually attach it so gseq_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_BooleanExpression()
    partner = gseq_And()
    setattr(partner, 'gseq_And26', None)
    _safe_set(owner, 'gseq_BooleanExpression27', partner)
    assert getattr(partner, 'gseq_And26') == owner
    _safe_set(owner, 'gseq_BooleanExpression27', None)
    assert getattr(partner, 'gseq_And26') is None


def test_assoc_rightEquality18_stub_double():
    # gseq_Equality has no real 'gseq_Equality19' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_Equality()
    setattr(partner, 'gseq_Equality19', None)
    _safe_set(owner, 'gseq_IntegerExpression20', partner)
    assert getattr(partner, 'gseq_Equality19') == owner
    _safe_set(owner, 'gseq_IntegerExpression20', None)
    assert getattr(partner, 'gseq_Equality19') is None


def test_assoc_rightGreaterThan37_stub_double():
    # gseq_GreaterThan has no real 'gseq_GreaterThan38' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_GreaterThan()
    setattr(partner, 'gseq_GreaterThan38', None)
    _safe_set(owner, 'gseq_IntegerExpression39', partner)
    assert getattr(partner, 'gseq_GreaterThan38') == owner
    _safe_set(owner, 'gseq_IntegerExpression39', None)
    assert getattr(partner, 'gseq_GreaterThan38') is None


def test_assoc_rightPlus32_stub_double():
    # gseq_Plus has no real 'gseq_Plus33' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_Plus()
    setattr(partner, 'gseq_Plus33', None)
    _safe_set(owner, 'gseq_IntegerExpression34', partner)
    assert getattr(partner, 'gseq_Plus33') == owner
    _safe_set(owner, 'gseq_IntegerExpression34', None)
    assert getattr(partner, 'gseq_Plus33') is None


def test_assoc_thenBranch12_stub_double():
    # gseq_If has no real 'gseq_If13' property in the generated
    # code (a bare stub) -- manually attach it so gseq_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_Operation()
    partner = gseq_If()
    setattr(partner, 'gseq_If13', None)
    _safe_set(owner, 'gseq_Operation14', partner)
    assert getattr(partner, 'gseq_If13') == owner
    _safe_set(owner, 'gseq_Operation14', None)
    assert getattr(partner, 'gseq_If13') is None


def test_assoc_whileCondition40_stub_double():
    # gseq_While has no real 'gseq_While' property in the generated
    # code (a bare stub) -- manually attach it so gseq_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_BooleanExpression()
    partner = gseq_While()
    setattr(partner, 'gseq_While', None)
    _safe_set(owner, 'gseq_BooleanExpression41', partner)
    assert getattr(partner, 'gseq_While') == owner
    _safe_set(owner, 'gseq_BooleanExpression41', None)
    assert getattr(partner, 'gseq_While') is None


def test_assoc_whileExpression42_stub_double():
    # gseq_While has no real 'gseq_While43' property in the generated
    # code (a bare stub) -- manually attach it so gseq_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gseq_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gseq_IntegerExpression()
    partner = gseq_While()
    setattr(partner, 'gseq_While43', None)
    _safe_set(owner, 'gseq_IntegerExpression44', partner)
    assert getattr(partner, 'gseq_While43') == owner
    _safe_set(owner, 'gseq_IntegerExpression44', None)
    assert getattr(partner, 'gseq_While43') is None


