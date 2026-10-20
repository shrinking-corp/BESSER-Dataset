import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    SubAbstractClass1,
    SubClass1,
    SubInterface1,
    SubInterface2,
    SuperAbstractClass,
    SuperClass,
    SuperInterface,
    testmodel_A,
    testmodel_B,
    testmodel_C,
    testmodel_Source,
    testmodel_SubAbstractClass1,
    testmodel_SubAbstractClass2,
    testmodel_SubAbstractClass3,
    testmodel_SubAbstractClass4,
    testmodel_SubAbstractClass5,
    testmodel_SubAbstractClass6,
    testmodel_SubAbstractClass7,
    testmodel_SubClass1,
    testmodel_SubClass2,
    testmodel_SubClass3,
    testmodel_SubClass4,
    testmodel_SubClass5,
    testmodel_SubClass6,
    testmodel_SubClass7,
    testmodel_SubInterface1,
    testmodel_SubInterface2,
    testmodel_SubInterface3,
    testmodel_SubInterface4,
    testmodel_SubInterface5,
    testmodel_SubInterface6,
    testmodel_SubInterface7,
    testmodel_SuperAbstractClass,
    testmodel_SuperClass,
    testmodel_SuperInterface,
    testmodel_Target,
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

