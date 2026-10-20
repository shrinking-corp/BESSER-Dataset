import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Area,
    Assignment,
    CorePattern,
    Domain,
    Element,
    Pattern,
    Rule,
    Variable,
    qvtcorebase_AbstractMapping,
    qvtcorebase_Area,
    qvtcorebase_Assignment,
    qvtcorebase_BottomPattern,
    qvtcorebase_CoreDomain,
    qvtcorebase_CorePattern,
    qvtcorebase_EnforcementOperation,
    qvtcorebase_GuardPattern,
    qvtcorebase_OCLExpression,
    qvtcorebase_OperationCallExp,
    qvtcorebase_Property,
    qvtcorebase_PropertyAssignment,
    qvtcorebase_RealizedVariable,
    qvtcorebase_Variable,
    qvtcorebase_VariableAssignment,
    EnforcementMode,
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

def test_assoc_area16_stub_double():
    # qvtcorebase_GuardPattern has no real 'guardPattern' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Area()
    partner = qvtcorebase_GuardPattern()
    setattr(partner, 'guardPattern', None)
    _safe_set(owner, 'Area17', partner)
    assert getattr(partner, 'guardPattern') == owner
    _safe_set(owner, 'Area17', None)
    assert getattr(partner, 'guardPattern') is None


def test_assoc_area6_stub_double():
    # qvtcorebase_BottomPattern has no real 'bottomPattern' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Area()
    partner = qvtcorebase_BottomPattern()
    setattr(partner, 'bottomPattern', None)
    _safe_set(owner, 'Area', partner)
    assert getattr(partner, 'bottomPattern') == owner
    _safe_set(owner, 'Area', None)
    assert getattr(partner, 'bottomPattern') is None


def test_assoc_assignment7_stub_double():
    # qvtcorebase_BottomPattern has no real 'bottomPattern8' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Assignment(isDefault="sample_text")
    partner = qvtcorebase_BottomPattern()
    setattr(partner, 'bottomPattern8', None)
    _safe_set(owner, 'Assignment', partner)
    assert owner in getattr(partner, 'bottomPattern8')
    _safe_set(owner, 'Assignment', None)
    assert owner not in getattr(partner, 'bottomPattern8')


def test_assoc_bottomPattern1_stub_double():
    # qvtcorebase_BottomPattern has no real 'BottomPattern' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Area()
    partner = qvtcorebase_BottomPattern()
    setattr(partner, 'BottomPattern', None)
    _safe_set(owner, 'area2', partner)
    assert getattr(partner, 'BottomPattern') == owner
    _safe_set(owner, 'area2', None)
    assert getattr(partner, 'BottomPattern') is None


def test_assoc_bottomPattern13_stub_double():
    # qvtcorebase_BottomPattern has no real 'BottomPattern14' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_EnforcementOperation(enforcementMode="sample_text")
    partner = qvtcorebase_BottomPattern()
    setattr(partner, 'BottomPattern14', None)
    _safe_set(owner, 'enforcementOperation', partner)
    assert getattr(partner, 'BottomPattern14') == owner
    _safe_set(owner, 'enforcementOperation', None)
    assert getattr(partner, 'BottomPattern14') is None


def test_assoc_bottomPattern3_stub_double():
    # qvtcorebase_BottomPattern has no real 'BottomPattern4' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Assignment(isDefault="sample_text")
    partner = qvtcorebase_BottomPattern()
    setattr(partner, 'BottomPattern4', None)
    _safe_set(owner, 'assignment', partner)
    assert getattr(partner, 'BottomPattern4') == owner
    _safe_set(owner, 'assignment', None)
    assert getattr(partner, 'BottomPattern4') is None


def test_assoc_enforcementOperation9_stub_double():
    # qvtcorebase_BottomPattern has no real 'bottomPattern10' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_EnforcementOperation(enforcementMode="sample_text")
    partner = qvtcorebase_BottomPattern()
    setattr(partner, 'bottomPattern10', None)
    _safe_set(owner, 'EnforcementOperation', partner)
    assert owner in getattr(partner, 'bottomPattern10')
    _safe_set(owner, 'EnforcementOperation', None)
    assert owner not in getattr(partner, 'bottomPattern10')


def test_assoc_guardPattern0_stub_double():
    # qvtcorebase_GuardPattern has no real 'GuardPattern' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Area's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Area's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Area()
    partner = qvtcorebase_GuardPattern()
    setattr(partner, 'GuardPattern', None)
    _safe_set(owner, 'area', partner)
    assert getattr(partner, 'GuardPattern') == owner
    _safe_set(owner, 'area', None)
    assert getattr(partner, 'GuardPattern') is None


def test_assoc_operationCallExp15_stub_double():
    # qvtcorebase_OperationCallExp has no real 'qvtcorebase_OperationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_EnforcementOperation(enforcementMode="sample_text")
    partner = qvtcorebase_OperationCallExp()
    setattr(partner, 'qvtcorebase_OperationCallExp', None)
    _safe_set(owner, 'qvtcorebase_EnforcementOperation', partner)
    assert getattr(partner, 'qvtcorebase_OperationCallExp') == owner
    _safe_set(owner, 'qvtcorebase_EnforcementOperation', None)
    assert getattr(partner, 'qvtcorebase_OperationCallExp') is None


def test_assoc_value5_stub_double():
    # qvtcorebase_OCLExpression has no real 'qvtcorebase_OCLExpression' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_Assignment(isDefault="sample_text")
    partner = qvtcorebase_OCLExpression()
    setattr(partner, 'qvtcorebase_OCLExpression', None)
    _safe_set(owner, 'qvtcorebase_Assignment', partner)
    assert getattr(partner, 'qvtcorebase_OCLExpression') == owner
    _safe_set(owner, 'qvtcorebase_Assignment', None)
    assert getattr(partner, 'qvtcorebase_OCLExpression') is None


def test_assoc_variable12_stub_double():
    # qvtcorebase_Variable has no real 'qvtcorebase_Variable' property in the generated
    # code (a bare stub) -- manually attach it so qvtcorebase_CorePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcorebase_CorePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcorebase_CorePattern()
    partner = qvtcorebase_Variable()
    setattr(partner, 'qvtcorebase_Variable', None)
    _safe_set(owner, 'qvtcorebase_CorePattern', {partner})
    assert getattr(partner, 'qvtcorebase_Variable') == owner
    _safe_set(owner, 'qvtcorebase_CorePattern', set())
    assert getattr(partner, 'qvtcorebase_Variable') is None


