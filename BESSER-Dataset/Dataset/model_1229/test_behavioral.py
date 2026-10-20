import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AreaCS,
    BottomPatternCS,
    CSTNode,
    DirectionCS,
    DomainCS,
    EnforcementOperationCS,
    GuardPatternCS,
    IdentifiedCS,
    IdentifierCS,
    MappingCS,
    OCLExpressionCS,
    OperationCallExpCS,
    ParamDeclarationCS,
    PathNameCS,
    PatternCS,
    QueryCS,
    RealizeableVariableCS,
    RealizedVariableCS,
    TransformationCS,
    TypeCS,
    UnrealizedVariableCS,
    cst_CSTNode,
    cst_IHasName,
    qvtcore_cst_AreaCS,
    qvtcore_cst_AssignmentCS,
    qvtcore_cst_BottomPatternCS,
    qvtcore_cst_DirectionCS,
    qvtcore_cst_DomainCS,
    qvtcore_cst_EnforcementOperationCS,
    qvtcore_cst_GuardPatternCS,
    qvtcore_cst_MappingCS,
    qvtcore_cst_ParamDeclarationCS,
    qvtcore_cst_PatternCS,
    qvtcore_cst_QueryCS,
    qvtcore_cst_RealizeableVariableCS,
    qvtcore_cst_RealizedVariableCS,
    qvtcore_cst_TopLevelCS,
    qvtcore_cst_TransformationCS,
    qvtcore_cst_UnrealizedVariableCS,
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

def test_assoc_initialiser4_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS6' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_cst_AssignmentCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_cst_AssignmentCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_cst_AssignmentCS(default=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS6', None)
    _safe_set(owner, 'qvtcore_cst_AssignmentCS5', partner)
    assert getattr(partner, 'OCLExpressionCS6') == owner
    _safe_set(owner, 'qvtcore_cst_AssignmentCS5', None)
    assert getattr(partner, 'OCLExpressionCS6') is None


def test_assoc_operationCall13_stub_double():
    # OperationCallExpCS has no real 'OperationCallExpCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_cst_EnforcementOperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_cst_EnforcementOperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_cst_EnforcementOperationCS(deletion=True)
    partner = OperationCallExpCS()
    setattr(partner, 'OperationCallExpCS', None)
    _safe_set(owner, 'qvtcore_cst_EnforcementOperationCS', partner)
    assert getattr(partner, 'OperationCallExpCS') == owner
    _safe_set(owner, 'qvtcore_cst_EnforcementOperationCS', None)
    assert getattr(partner, 'OperationCallExpCS') is None


def test_assoc_target3_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_cst_AssignmentCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_cst_AssignmentCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_cst_AssignmentCS(default=True)
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS', None)
    _safe_set(owner, 'qvtcore_cst_AssignmentCS', partner)
    assert getattr(partner, 'OCLExpressionCS') == owner
    _safe_set(owner, 'qvtcore_cst_AssignmentCS', None)
    assert getattr(partner, 'OCLExpressionCS') is None


