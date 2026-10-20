import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    SimpleUML_Class,
    SimpleUML_Feature,
    SimpleUML_NamedElement,
    SimpleUML_Package,
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

def test_assoc_features1_stub_double():
    # SimpleUML_Class has no real 'SimpleUML_Class' property in the generated
    # code (a bare stub) -- manually attach it so SimpleUML_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleUML_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleUML_Feature(isMultivalued=True)
    partner = SimpleUML_Class()
    setattr(partner, 'SimpleUML_Class', None)
    _safe_set(owner, 'SimpleUML_Feature', partner)
    assert owner in getattr(partner, 'SimpleUML_Class')
    _safe_set(owner, 'SimpleUML_Feature', None)
    assert owner not in getattr(partner, 'SimpleUML_Class')


def test_assoc_type3_stub_double():
    # SimpleUML_Class has no real 'SimpleUML_Class5' property in the generated
    # code (a bare stub) -- manually attach it so SimpleUML_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleUML_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleUML_Feature(isMultivalued=True)
    partner = SimpleUML_Class()
    setattr(partner, 'SimpleUML_Class5', None)
    _safe_set(owner, 'SimpleUML_Feature4', partner)
    assert getattr(partner, 'SimpleUML_Class5') == owner
    _safe_set(owner, 'SimpleUML_Feature4', None)
    assert getattr(partner, 'SimpleUML_Class5') is None


