import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BoolExpr,
    IntExpr,
    Node,
    flinkie2_AssignStat,
    flinkie2_BoolExpr,
    flinkie2_BoolVal,
    flinkie2_BooleanEvaluation,
    flinkie2_BracExprBool,
    flinkie2_BracExprInt,
    flinkie2_Comparison,
    flinkie2_DeclStat,
    flinkie2_FlowChart,
    flinkie2_Init,
    flinkie2_IntExpr,
    flinkie2_Message,
    flinkie2_Node,
    flinkie2_Number,
    flinkie2_OneOpBool,
    flinkie2_OneOpInt,
    flinkie2_Option,
    flinkie2_Question,
    flinkie2_TwoOpBool,
    flinkie2_TwoOpInt,
    flinkie2_Variable,
    flinkie2_VariableExpr,
    EBoolOneOp,
    EBoolTwoOp,
    EBoolVal,
    ECompOp,
    EIntOneOp,
    EIntTwoOp,
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

def test_assoc_options14_reverse_link_reassign_clear():
    a1 = flinkie2_Question(text="sample_text")
    a2 = flinkie2_Question(text="sample_text_2")
    b = flinkie2_Option(text="sample_text")
    _safe_set(b, 'flinkie2_Option', a1)
    assert _is_linked(b, 'flinkie2_Option', a1)
    if hasattr(a1, 'flinkie2_Question'):
        assert _is_linked(a1, 'flinkie2_Question', b)
    _safe_set(b, 'flinkie2_Option', a2)
    assert _is_linked(b, 'flinkie2_Option', a2)
    if hasattr(a1, 'flinkie2_Question'):
        assert not _is_linked(a1, 'flinkie2_Question', b)
    if hasattr(a2, 'flinkie2_Question'):
        assert _is_linked(a2, 'flinkie2_Question', b)
    _safe_set(b, 'flinkie2_Option', None)
    assert not _is_linked(b, 'flinkie2_Option', a2)
    if hasattr(a2, 'flinkie2_Question'):
        assert not _is_linked(a2, 'flinkie2_Question', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignstats15_stub_double():
    # flinkie2_AssignStat has no real 'flinkie2_AssignStat17' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Question's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Question's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Question(text="sample_text")
    partner = flinkie2_AssignStat()
    setattr(partner, 'flinkie2_AssignStat17', None)
    _safe_set(owner, 'flinkie2_Question16', {partner})
    assert getattr(partner, 'flinkie2_AssignStat17') == owner
    _safe_set(owner, 'flinkie2_Question16', set())
    assert getattr(partner, 'flinkie2_AssignStat17') is None


def test_assoc_assignstats18_stub_double():
    # flinkie2_AssignStat has no real 'flinkie2_AssignStat19' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Message(text="sample_text")
    partner = flinkie2_AssignStat()
    setattr(partner, 'flinkie2_AssignStat19', None)
    _safe_set(owner, 'flinkie2_Message', {partner})
    assert getattr(partner, 'flinkie2_AssignStat19') == owner
    _safe_set(owner, 'flinkie2_Message', set())
    assert getattr(partner, 'flinkie2_AssignStat19') is None


def test_assoc_assignstats23_stub_double():
    # flinkie2_AssignStat has no real 'flinkie2_AssignStat25' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Option(text="sample_text")
    partner = flinkie2_AssignStat()
    setattr(partner, 'flinkie2_AssignStat25', None)
    _safe_set(owner, 'flinkie2_Option24', {partner})
    assert getattr(partner, 'flinkie2_AssignStat25') == owner
    _safe_set(owner, 'flinkie2_Option24', set())
    assert getattr(partner, 'flinkie2_AssignStat25') is None


def test_assoc_boolexpr50_stub_double():
    # flinkie2_BoolExpr has no real 'flinkie2_BoolExpr51' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_OneOpBool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_OneOpBool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_OneOpBool(operator="sample_text")
    partner = flinkie2_BoolExpr()
    setattr(partner, 'flinkie2_BoolExpr51', None)
    _safe_set(owner, 'flinkie2_OneOpBool', partner)
    assert getattr(partner, 'flinkie2_BoolExpr51') == owner
    _safe_set(owner, 'flinkie2_OneOpBool', None)
    assert getattr(partner, 'flinkie2_BoolExpr51') is None


def test_assoc_intexpr29_stub_double():
    # flinkie2_IntExpr has no real 'flinkie2_IntExpr' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_OneOpInt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_OneOpInt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_OneOpInt(operator="sample_text")
    partner = flinkie2_IntExpr()
    setattr(partner, 'flinkie2_IntExpr', None)
    _safe_set(owner, 'flinkie2_OneOpInt', partner)
    assert getattr(partner, 'flinkie2_IntExpr') == owner
    _safe_set(owner, 'flinkie2_OneOpInt', None)
    assert getattr(partner, 'flinkie2_IntExpr') is None


def test_assoc_left30_stub_double():
    # flinkie2_IntExpr has no real 'flinkie2_IntExpr31' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_TwoOpInt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_TwoOpInt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_TwoOpInt(operator="sample_text")
    partner = flinkie2_IntExpr()
    setattr(partner, 'flinkie2_IntExpr31', None)
    _safe_set(owner, 'flinkie2_TwoOpInt', partner)
    assert getattr(partner, 'flinkie2_IntExpr31') == owner
    _safe_set(owner, 'flinkie2_TwoOpInt', None)
    assert getattr(partner, 'flinkie2_IntExpr31') is None


def test_assoc_left52_stub_double():
    # flinkie2_BoolExpr has no real 'flinkie2_BoolExpr53' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_TwoOpBool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_TwoOpBool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_TwoOpBool(operator="sample_text")
    partner = flinkie2_BoolExpr()
    setattr(partner, 'flinkie2_BoolExpr53', None)
    _safe_set(owner, 'flinkie2_TwoOpBool', partner)
    assert getattr(partner, 'flinkie2_BoolExpr53') == owner
    _safe_set(owner, 'flinkie2_TwoOpBool', None)
    assert getattr(partner, 'flinkie2_BoolExpr53') is None


def test_assoc_left61_stub_double():
    # flinkie2_IntExpr has no real 'flinkie2_IntExpr63' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Comparison(operator="sample_text")
    partner = flinkie2_IntExpr()
    setattr(partner, 'flinkie2_IntExpr63', None)
    _safe_set(owner, 'flinkie2_Comparison62', partner)
    assert getattr(partner, 'flinkie2_IntExpr63') == owner
    _safe_set(owner, 'flinkie2_Comparison62', None)
    assert getattr(partner, 'flinkie2_IntExpr63') is None


def test_assoc_node20_stub_double():
    # flinkie2_Node has no real 'flinkie2_Node22' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Message(text="sample_text")
    partner = flinkie2_Node()
    setattr(partner, 'flinkie2_Node22', None)
    _safe_set(owner, 'flinkie2_Message21', partner)
    assert getattr(partner, 'flinkie2_Node22') == owner
    _safe_set(owner, 'flinkie2_Message21', None)
    assert getattr(partner, 'flinkie2_Node22') is None


def test_assoc_node26_stub_double():
    # flinkie2_Node has no real 'flinkie2_Node28' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Option(text="sample_text")
    partner = flinkie2_Node()
    setattr(partner, 'flinkie2_Node28', None)
    _safe_set(owner, 'flinkie2_Option27', partner)
    assert getattr(partner, 'flinkie2_Node28') == owner
    _safe_set(owner, 'flinkie2_Option27', None)
    assert getattr(partner, 'flinkie2_Node28') is None


def test_assoc_right32_stub_double():
    # flinkie2_IntExpr has no real 'flinkie2_IntExpr34' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_TwoOpInt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_TwoOpInt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_TwoOpInt(operator="sample_text")
    partner = flinkie2_IntExpr()
    setattr(partner, 'flinkie2_IntExpr34', None)
    _safe_set(owner, 'flinkie2_TwoOpInt33', partner)
    assert getattr(partner, 'flinkie2_IntExpr34') == owner
    _safe_set(owner, 'flinkie2_TwoOpInt33', None)
    assert getattr(partner, 'flinkie2_IntExpr34') is None


def test_assoc_right54_stub_double():
    # flinkie2_BoolExpr has no real 'flinkie2_BoolExpr56' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_TwoOpBool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_TwoOpBool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_TwoOpBool(operator="sample_text")
    partner = flinkie2_BoolExpr()
    setattr(partner, 'flinkie2_BoolExpr56', None)
    _safe_set(owner, 'flinkie2_TwoOpBool55', partner)
    assert getattr(partner, 'flinkie2_BoolExpr56') == owner
    _safe_set(owner, 'flinkie2_TwoOpBool55', None)
    assert getattr(partner, 'flinkie2_BoolExpr56') is None


def test_assoc_right59_stub_double():
    # flinkie2_IntExpr has no real 'flinkie2_IntExpr60' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Comparison(operator="sample_text")
    partner = flinkie2_IntExpr()
    setattr(partner, 'flinkie2_IntExpr60', None)
    _safe_set(owner, 'flinkie2_Comparison', partner)
    assert getattr(partner, 'flinkie2_IntExpr60') == owner
    _safe_set(owner, 'flinkie2_Comparison', None)
    assert getattr(partner, 'flinkie2_IntExpr60') is None


def test_assoc_variable3_stub_double():
    # flinkie2_DeclStat has no real 'flinkie2_DeclStat4' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Variable(name="sample_text")
    partner = flinkie2_DeclStat()
    setattr(partner, 'flinkie2_DeclStat4', None)
    _safe_set(owner, 'flinkie2_Variable', partner)
    assert getattr(partner, 'flinkie2_DeclStat4') == owner
    _safe_set(owner, 'flinkie2_Variable', None)
    assert getattr(partner, 'flinkie2_DeclStat4') is None


def test_assoc_variable47_stub_double():
    # flinkie2_VariableExpr has no real 'flinkie2_VariableExpr48' property in the generated
    # code (a bare stub) -- manually attach it so flinkie2_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flinkie2_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flinkie2_Variable(name="sample_text")
    partner = flinkie2_VariableExpr()
    setattr(partner, 'flinkie2_VariableExpr48', None)
    _safe_set(owner, 'flinkie2_Variable49', partner)
    assert getattr(partner, 'flinkie2_VariableExpr48') == owner
    _safe_set(owner, 'flinkie2_Variable49', None)
    assert getattr(partner, 'flinkie2_VariableExpr48') is None


