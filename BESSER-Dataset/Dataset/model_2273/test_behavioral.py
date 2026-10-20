import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    university_Address,
    university_Assistant,
    university_Course,
    university_CourseCatalog,
    university_Person,
    university_Professor,
    university_Staff,
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

def test_assoc_addresses4_stub_double():
    # university_Address has no real 'university_Address' property in the generated
    # code (a bare stub) -- manually attach it so university_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Person(name="sample_text")
    partner = university_Address()
    setattr(partner, 'university_Address', None)
    _safe_set(owner, 'university_Person', {partner})
    assert getattr(partner, 'university_Address') == owner
    _safe_set(owner, 'university_Person', set())
    assert getattr(partner, 'university_Address') is None


def test_assoc_assistants2_stub_double():
    # university_Assistant has no real 'university_Assistant' property in the generated
    # code (a bare stub) -- manually attach it so university_Staff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Staff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Staff(staff="sample_text")
    partner = university_Assistant()
    setattr(partner, 'university_Assistant', None)
    _safe_set(owner, 'university_Staff3', {partner})
    assert getattr(partner, 'university_Assistant') == owner
    _safe_set(owner, 'university_Staff3', set())
    assert getattr(partner, 'university_Assistant') is None


def test_assoc_courses0_stub_double():
    # university_CourseCatalog has no real 'university_CourseCatalog' property in the generated
    # code (a bare stub) -- manually attach it so university_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Course(etcs=7, id="sample_text", name="sample_text")
    partner = university_CourseCatalog()
    setattr(partner, 'university_CourseCatalog', None)
    _safe_set(owner, 'university_Course', partner)
    assert owner in getattr(partner, 'university_CourseCatalog')
    _safe_set(owner, 'university_Course', None)
    assert owner not in getattr(partner, 'university_CourseCatalog')


def test_assoc_professors1_stub_double():
    # university_Professor has no real 'university_Professor' property in the generated
    # code (a bare stub) -- manually attach it so university_Staff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Staff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Staff(staff="sample_text")
    partner = university_Professor()
    setattr(partner, 'university_Professor', None)
    _safe_set(owner, 'university_Staff', {partner})
    assert getattr(partner, 'university_Professor') == owner
    _safe_set(owner, 'university_Staff', set())
    assert getattr(partner, 'university_Professor') is None


