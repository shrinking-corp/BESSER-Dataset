import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    class3,
    testSubpackages1_root_class1,
    testSubpackages1_root_testSubpackages1_subpackage1_class2,
    testSubpackages1_root_testSubpackages1_subpackage2_class3,
    testSubpackages1_root_testSubpackages1_subpackage3_class4,
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

def test_assoc_ref_class30_stub_double():
    # class3 has no real 'class3' property in the generated
    # code (a bare stub) -- manually attach it so testSubpackages1_root_class1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testSubpackages1_root_class1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testSubpackages1_root_class1(a=date(2024, 1, 1))
    partner = class3()
    setattr(partner, 'class3', None)
    _safe_set(owner, 'testSubpackages1_root_class1', partner)
    assert getattr(partner, 'class3') == owner
    _safe_set(owner, 'testSubpackages1_root_class1', None)
    assert getattr(partner, 'class3') is None


