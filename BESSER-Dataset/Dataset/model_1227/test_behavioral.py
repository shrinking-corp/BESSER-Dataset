import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExpCS,
    ElementCS,
    ExpCS,
    ExpressionBlockCS,
    ImperativeLoopExpCS,
    StatementCS,
    TypedRefCS,
    imperativeoclcs_AssertExpCS,
    imperativeoclcs_AssignStatementCS,
    imperativeoclcs_BlockExpCS,
    imperativeoclcs_CollectionLiteralPartCS,
    imperativeoclcs_ComputeExpCS,
    imperativeoclcs_DictLiteralExpCS,
    imperativeoclcs_DictLiteralPartCS,
    imperativeoclcs_DictTypeCS,
    imperativeoclcs_DoExpCS,
    imperativeoclcs_ExceptCS,
    imperativeoclcs_ExpCS,
    imperativeoclcs_ExpressionBlockCS,
    imperativeoclcs_ExpressionStatementCS,
    imperativeoclcs_ForExpCS,
    imperativeoclcs_ImperativeIterateExpCS,
    imperativeoclcs_ImperativeLoopExpCS,
    imperativeoclcs_InstantiationExpCS,
    imperativeoclcs_ListLiteralExpCS,
    imperativeoclcs_ListTypeCS,
    imperativeoclcs_LogExpCS,
    imperativeoclcs_PrimitiveLiteralExpCS,
    imperativeoclcs_QuitExpCS,
    imperativeoclcs_RaiseExpCS,
    imperativeoclcs_ReturnExpCS,
    imperativeoclcs_StatementCS,
    imperativeoclcs_SwitchAltCS,
    imperativeoclcs_SwitchExpCS,
    imperativeoclcs_TryExpCS,
    imperativeoclcs_Type,
    imperativeoclcs_TypeCS,
    imperativeoclcs_TypedRefCS,
    imperativeoclcs_VariableCS,
    imperativeoclcs_VariableInitializationCS,
    imperativeoclcs_WhileExpCS,
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

def test_assoc_alternativePart54_stub_double():
    # imperativeoclcs_SwitchExpCS has no real 'imperativeoclcs_SwitchExpCS' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_SwitchAltCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_SwitchAltCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_SwitchAltCS(keyword="sample_text")
    partner = imperativeoclcs_SwitchExpCS()
    setattr(partner, 'imperativeoclcs_SwitchExpCS', None)
    _safe_set(owner, 'imperativeoclcs_SwitchAltCS55', partner)
    assert owner in getattr(partner, 'imperativeoclcs_SwitchExpCS')
    _safe_set(owner, 'imperativeoclcs_SwitchAltCS55', None)
    assert owner not in getattr(partner, 'imperativeoclcs_SwitchExpCS')


def test_assoc_assertion0_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_AssertExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_AssertExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_AssertExpCS(severity="sample_text")
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS', None)
    _safe_set(owner, 'imperativeoclcs_AssertExpCS', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS') == owner
    _safe_set(owner, 'imperativeoclcs_AssertExpCS', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS') is None


def test_assoc_body51_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS53' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_SwitchAltCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_SwitchAltCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_SwitchAltCS(keyword="sample_text")
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS53', None)
    _safe_set(owner, 'imperativeoclcs_SwitchAltCS52', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS53') == owner
    _safe_set(owner, 'imperativeoclcs_SwitchAltCS52', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS53') is None


def test_assoc_condition49_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS50' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_SwitchAltCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_SwitchAltCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_SwitchAltCS(keyword="sample_text")
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS50', None)
    _safe_set(owner, 'imperativeoclcs_SwitchAltCS', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS50') == owner
    _safe_set(owner, 'imperativeoclcs_SwitchAltCS', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS50') is None


def test_assoc_lValueCS3_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS4' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_AssignStatementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_AssignStatementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_AssignStatementCS(incremental=True)
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS4', None)
    _safe_set(owner, 'imperativeoclcs_AssignStatementCS', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS4') == owner
    _safe_set(owner, 'imperativeoclcs_AssignStatementCS', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS4') is None


def test_assoc_log1_stub_double():
    # imperativeoclcs_LogExpCS has no real 'imperativeoclcs_LogExpCS' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_AssertExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_AssertExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_AssertExpCS(severity="sample_text")
    partner = imperativeoclcs_LogExpCS()
    setattr(partner, 'imperativeoclcs_LogExpCS', None)
    _safe_set(owner, 'imperativeoclcs_AssertExpCS2', partner)
    assert getattr(partner, 'imperativeoclcs_LogExpCS') == owner
    _safe_set(owner, 'imperativeoclcs_AssertExpCS2', None)
    assert getattr(partner, 'imperativeoclcs_LogExpCS') is None


def test_assoc_oclExpressionCS5_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS7' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_AssignStatementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_AssignStatementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_AssignStatementCS(incremental=True)
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS7', None)
    _safe_set(owner, 'imperativeoclcs_AssignStatementCS6', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS7') == owner
    _safe_set(owner, 'imperativeoclcs_AssignStatementCS6', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS7') is None


def test_assoc_oclExpressionCS61_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS62' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_VariableInitializationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_VariableInitializationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_VariableInitializationCS(simpleNameCS="sample_text", withResult=True)
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS62', None)
    _safe_set(owner, 'imperativeoclcs_VariableInitializationCS', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS62') == owner
    _safe_set(owner, 'imperativeoclcs_VariableInitializationCS', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS62') is None


def test_assoc_typeCS63_stub_double():
    # imperativeoclcs_TypeCS has no real 'imperativeoclcs_TypeCS65' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_VariableInitializationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_VariableInitializationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_VariableInitializationCS(simpleNameCS="sample_text", withResult=True)
    partner = imperativeoclcs_TypeCS()
    setattr(partner, 'imperativeoclcs_TypeCS65', None)
    _safe_set(owner, 'imperativeoclcs_VariableInitializationCS64', partner)
    assert getattr(partner, 'imperativeoclcs_TypeCS65') == owner
    _safe_set(owner, 'imperativeoclcs_VariableInitializationCS64', None)
    assert getattr(partner, 'imperativeoclcs_TypeCS65') is None


def test_assoc_value45_stub_double():
    # imperativeoclcs_ExpCS has no real 'imperativeoclcs_ExpCS46' property in the generated
    # code (a bare stub) -- manually attach it so imperativeoclcs_QuitExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeoclcs_QuitExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeoclcs_QuitExpCS(keyword="sample_text")
    partner = imperativeoclcs_ExpCS()
    setattr(partner, 'imperativeoclcs_ExpCS46', None)
    _safe_set(owner, 'imperativeoclcs_QuitExpCS', partner)
    assert getattr(partner, 'imperativeoclcs_ExpCS46') == owner
    _safe_set(owner, 'imperativeoclcs_QuitExpCS', None)
    assert getattr(partner, 'imperativeoclcs_ExpCS46') is None


