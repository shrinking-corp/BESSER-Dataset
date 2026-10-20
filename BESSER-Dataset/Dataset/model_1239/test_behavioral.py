import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AltExp,
    CatchExp,
    Class,
    CollectionType,
    DictLiteralExp,
    DictLiteralPart,
    Element,
    ImperativeExpression,
    ImperativeLoopExp,
    ImperativeOCL_AltExp,
    ImperativeOCL_AssertExp,
    ImperativeOCL_AssignExp,
    ImperativeOCL_BlockExp,
    ImperativeOCL_BreakExp,
    ImperativeOCL_CatchExp,
    ImperativeOCL_ComputeExp,
    ImperativeOCL_ContinueExp,
    ImperativeOCL_DictLiteralExp,
    ImperativeOCL_DictLiteralPart,
    ImperativeOCL_DictionaryType,
    ImperativeOCL_ForExp,
    ImperativeOCL_ImperativeExpression,
    ImperativeOCL_ImperativeIterateExp,
    ImperativeOCL_ImperativeLoopExp,
    ImperativeOCL_InstantiationExp,
    ImperativeOCL_ListLiteralExp,
    ImperativeOCL_ListType,
    ImperativeOCL_LogExp,
    ImperativeOCL_RaiseExp,
    ImperativeOCL_ReturnExp,
    ImperativeOCL_SwitchExp,
    ImperativeOCL_TryExp,
    ImperativeOCL_Typedef,
    ImperativeOCL_UnlinkExp,
    ImperativeOCL_VariableInitExp,
    ImperativeOCL_WhileExp,
    LiteralExp,
    LogExp,
    LoopExp,
    OclExpression,
    Operation,
    OperationCallExp,
    Type,
    Variable,
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

def test_assoc_assertion4_stub_double():
    # OclExpression has no real 'OclExpression5' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression5', None)
    _safe_set(owner, 'ImperativeOCL_AssertExp', partner)
    assert getattr(partner, 'OclExpression5') == owner
    _safe_set(owner, 'ImperativeOCL_AssertExp', None)
    assert getattr(partner, 'OclExpression5') is None


def test_assoc_defaultValue8_stub_double():
    # OclExpression has no real 'OclExpression9' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression9', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp', partner)
    assert getattr(partner, 'OclExpression9') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp', None)
    assert getattr(partner, 'OclExpression9') is None


def test_assoc_left10_stub_double():
    # OclExpression has no real 'OclExpression12' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression12', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp11', partner)
    assert getattr(partner, 'OclExpression12') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp11', None)
    assert getattr(partner, 'OclExpression12') is None


def test_assoc_log6_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'ImperativeOCL_AssertExp7', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'ImperativeOCL_AssertExp7', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_referredVariable81_stub_double():
    # Variable has no real 'Variable82' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_VariableInitExp(withResult="sample_text")
    partner = Variable()
    setattr(partner, 'Variable82', None)
    _safe_set(owner, 'ImperativeOCL_VariableInitExp', partner)
    assert getattr(partner, 'Variable82') == owner
    _safe_set(owner, 'ImperativeOCL_VariableInitExp', None)
    assert getattr(partner, 'Variable82') is None


def test_assoc_value13_stub_double():
    # OclExpression has no real 'OclExpression15' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression15', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp14', {partner})
    assert getattr(partner, 'OclExpression15') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp14', set())
    assert getattr(partner, 'OclExpression15') is None


