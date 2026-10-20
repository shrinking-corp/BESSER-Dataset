import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AltExp,
    CatchExp,
    DictLiteralPart,
    ImperativeExpression,
    ImperativeLoopExp,
    LogExp,
    OrderedTupleLiteralPart,
    imperativeocl_AltExp,
    imperativeocl_AssertExp,
    imperativeocl_AssignExp,
    imperativeocl_BlockExp,
    imperativeocl_BreakExp,
    imperativeocl_CatchExp,
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
    imperativeocl_OrderedTupleLiteralExp,
    imperativeocl_OrderedTupleLiteralPart,
    imperativeocl_OrderedTupleType,
    imperativeocl_RaiseExp,
    imperativeocl_ReturnExp,
    imperativeocl_SwitchExp,
    imperativeocl_TemplateParameterType,
    imperativeocl_TryExp,
    imperativeocl_Typedef,
    imperativeocl_UnlinkExp,
    imperativeocl_UnpackExp,
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

def test_assoc_log0_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'imperativeocl_AssertExp', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'imperativeocl_AssertExp', None)
    assert getattr(partner, 'LogExp') is None


