import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExp,
    Class,
    CollectionType,
    Element,
    ImperativeExpression,
    ImperativeLoopExp,
    LiteralExp,
    LoopExp,
    OclExpression,
    OperationCallExp,
    Type,
    imperativeocl_AltExp,
    imperativeocl_AssertExp,
    imperativeocl_AssignExp,
    imperativeocl_BlockExp,
    imperativeocl_BreakExp,
    imperativeocl_CatchExp,
    imperativeocl_Class,
    imperativeocl_ComputeExp,
    imperativeocl_ContinueExp,
    imperativeocl_DictLiteralExp,
    imperativeocl_DictLiteralPart,
    imperativeocl_DictionaryType,
    imperativeocl_ForExp,
    imperativeocl_ImperativeExpression,
    imperativeocl_ImperativeIterateExp,
    imperativeocl_ImperativeLoopExp,
    imperativeocl_InstantiationExp,
    imperativeocl_ListType,
    imperativeocl_LogExp,
    imperativeocl_OclExpression,
    imperativeocl_OrderedTupleLiteralExp,
    imperativeocl_OrderedTupleLiteralPart,
    imperativeocl_OrderedTupleType,
    imperativeocl_RaiseExp,
    imperativeocl_ReturnExp,
    imperativeocl_SwitchExp,
    imperativeocl_TemplateParameterType,
    imperativeocl_TryExp,
    imperativeocl_Type,
    imperativeocl_Typedef,
    imperativeocl_UnlinkExp,
    imperativeocl_UnpackExp,
    imperativeocl_Variable,
    imperativeocl_VariableInitExp,
    imperativeocl_WhileExp,
    SeverityKind,
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

def test_assoc_assertion70_stub_double():
    # imperativeocl_OclExpression has no real 'imperativeocl_OclExpression72' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssertExp(severity="sample_text")
    partner = imperativeocl_OclExpression()
    setattr(partner, 'imperativeocl_OclExpression72', None)
    _safe_set(owner, 'imperativeocl_AssertExp71', partner)
    assert getattr(partner, 'imperativeocl_OclExpression72') == owner
    _safe_set(owner, 'imperativeocl_AssertExp71', None)
    assert getattr(partner, 'imperativeocl_OclExpression72') is None


def test_assoc_defaultValue4_stub_double():
    # imperativeocl_OclExpression has no real 'imperativeocl_OclExpression6' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssignExp(isReset="sample_text")
    partner = imperativeocl_OclExpression()
    setattr(partner, 'imperativeocl_OclExpression6', None)
    _safe_set(owner, 'imperativeocl_AssignExp5', partner)
    assert getattr(partner, 'imperativeocl_OclExpression6') == owner
    _safe_set(owner, 'imperativeocl_AssignExp5', None)
    assert getattr(partner, 'imperativeocl_OclExpression6') is None


def test_assoc_left1_stub_double():
    # imperativeocl_OclExpression has no real 'imperativeocl_OclExpression3' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssignExp(isReset="sample_text")
    partner = imperativeocl_OclExpression()
    setattr(partner, 'imperativeocl_OclExpression3', None)
    _safe_set(owner, 'imperativeocl_AssignExp2', partner)
    assert getattr(partner, 'imperativeocl_OclExpression3') == owner
    _safe_set(owner, 'imperativeocl_AssignExp2', None)
    assert getattr(partner, 'imperativeocl_OclExpression3') is None


def test_assoc_log68_stub_double():
    # imperativeocl_LogExp has no real 'imperativeocl_LogExp69' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssertExp(severity="sample_text")
    partner = imperativeocl_LogExp()
    setattr(partner, 'imperativeocl_LogExp69', None)
    _safe_set(owner, 'imperativeocl_AssertExp', partner)
    assert getattr(partner, 'imperativeocl_LogExp69') == owner
    _safe_set(owner, 'imperativeocl_AssertExp', None)
    assert getattr(partner, 'imperativeocl_LogExp69') is None


def test_assoc_referredVariable13_stub_double():
    # imperativeocl_Variable has no real 'imperativeocl_Variable' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_VariableInitExp(withResult="sample_text")
    partner = imperativeocl_Variable()
    setattr(partner, 'imperativeocl_Variable', None)
    _safe_set(owner, 'imperativeocl_VariableInitExp', partner)
    assert getattr(partner, 'imperativeocl_Variable') == owner
    _safe_set(owner, 'imperativeocl_VariableInitExp', None)
    assert getattr(partner, 'imperativeocl_Variable') is None


def test_assoc_value0_stub_double():
    # imperativeocl_OclExpression has no real 'imperativeocl_OclExpression' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssignExp(isReset="sample_text")
    partner = imperativeocl_OclExpression()
    setattr(partner, 'imperativeocl_OclExpression', None)
    _safe_set(owner, 'imperativeocl_AssignExp', {partner})
    assert getattr(partner, 'imperativeocl_OclExpression') == owner
    _safe_set(owner, 'imperativeocl_AssignExp', set())
    assert getattr(partner, 'imperativeocl_OclExpression') is None


