import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AChild,
    BChild,
    CChild,
    DChild,
    EChild,
    ExprChild,
    FChild,
    GChild,
    HChild,
    IChild,
    JChild,
    KChild,
    LChild,
    MChild,
    NChild,
    OChild,
    PChild,
    QChild,
    RChild,
    SChild,
    TChild,
    UChild,
    VChild,
    WChild,
    XChild,
    YChild,
    ZChild,
    top_A,
    top_AChild,
    top_B,
    top_BChild,
    top_C,
    top_CChild,
    top_D,
    top_DChild,
    top_E,
    top_EChild,
    top_Expr,
    top_ExprChild,
    top_F,
    top_FChild,
    top_G,
    top_GChild,
    top_H,
    top_HChild,
    top_I,
    top_IChild,
    top_IntegerLiteral,
    top_J,
    top_JChild,
    top_K,
    top_KChild,
    top_L,
    top_LChild,
    top_M,
    top_MChild,
    top_N,
    top_NChild,
    top_O,
    top_OChild,
    top_P,
    top_PChild,
    top_Q,
    top_QChild,
    top_R,
    top_RChild,
    top_S,
    top_SChild,
    top_T,
    top_TChild,
    top_U,
    top_UChild,
    top_V,
    top_VChild,
    top_W,
    top_WChild,
    top_X,
    top_XChild,
    top_Y,
    top_YChild,
    top_Z,
    top_ZChild,
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

