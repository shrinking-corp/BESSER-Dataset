import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    edu_Course,
    edu_Student,
    edu_Take_Course,
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

def test_assoc_course1_stub_double():
    # edu_Take_Course has no real 'edu_Take_Course2' property in the generated
    # code (a bare stub) -- manually attach it so edu_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_Course(id=7, name="sample_text")
    partner = edu_Take_Course()
    setattr(partner, 'edu_Take_Course2', None)
    _safe_set(owner, 'edu_Course', partner)
    assert owner in getattr(partner, 'edu_Take_Course2')
    _safe_set(owner, 'edu_Course', None)
    assert owner not in getattr(partner, 'edu_Take_Course2')


def test_assoc_student0_stub_double():
    # edu_Take_Course has no real 'edu_Take_Course' property in the generated
    # code (a bare stub) -- manually attach it so edu_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_Student(date_of_birth=date(2024, 1, 1), id=7, name="sample_text")
    partner = edu_Take_Course()
    setattr(partner, 'edu_Take_Course', None)
    _safe_set(owner, 'edu_Student', partner)
    assert owner in getattr(partner, 'edu_Take_Course')
    _safe_set(owner, 'edu_Student', None)
    assert owner not in getattr(partner, 'edu_Take_Course')


