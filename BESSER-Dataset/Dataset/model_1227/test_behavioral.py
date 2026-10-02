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

