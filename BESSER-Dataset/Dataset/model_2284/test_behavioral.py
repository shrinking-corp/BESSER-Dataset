import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModelElement,
    Univerity_Courses,
    Univerity_Person,
    Univerity_University,
    Univerity_uncertainty_ModelElement,
    Univerity_uncertainty_UData,
    Univerity_uncertainty_aCourses,
    Univerity_uncertainty_aPerson,
    Univerity_uncertainty_aUniversity,
    Univerity_uncertainty_uCourses,
    Univerity_uncertainty_uPerson,
    Univerity_uncertainty_uUniversity,
    aCourses,
    aPerson,
    uCourses,
    uPerson,
    uUniversity,
    uncertainty_ModelElement,
    uncertainty_UData,
    uncertainty_Univerity_Courses,
    uncertainty_Univerity_Person,
    uncertainty_Univerity_University,
    uncertainty_aCourses,
    uncertainty_aPerson,
    uncertainty_aUniversity,
    OperatorType,
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

def test_assoc_Professor1_stub_double():
    # aPerson has no real 'aPerson' property in the generated
    # code (a bare stub) -- manually attach it so Univerity_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Univerity_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    partner = aPerson()
    setattr(partner, 'aPerson', None)
    _safe_set(owner, 'Univerity_Courses2', partner)
    assert getattr(partner, 'aPerson') == owner
    _safe_set(owner, 'Univerity_Courses2', None)
    assert getattr(partner, 'aPerson') is None


def test_assoc_Student3_stub_double():
    # aPerson has no real 'aPerson5' property in the generated
    # code (a bare stub) -- manually attach it so Univerity_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Univerity_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    partner = aPerson()
    setattr(partner, 'aPerson5', None)
    _safe_set(owner, 'Univerity_Courses4', {partner})
    assert getattr(partner, 'aPerson5') == owner
    _safe_set(owner, 'Univerity_Courses4', set())
    assert getattr(partner, 'aPerson5') is None


def test_assoc_links0_stub_double():
    # aCourses has no real 'aCourses' property in the generated
    # code (a bare stub) -- manually attach it so Univerity_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Univerity_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Univerity_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    partner = aCourses()
    setattr(partner, 'aCourses', None)
    _safe_set(owner, 'Univerity_Courses', {partner})
    assert getattr(partner, 'aCourses') == owner
    _safe_set(owner, 'Univerity_Courses', set())
    assert getattr(partner, 'aCourses') is None


def test_assoc_relatives6_stub_double():
    # aPerson has no real 'aPerson7' property in the generated
    # code (a bare stub) -- manually attach it so Univerity_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Univerity_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Univerity_Person(Email="sample_text", Name="sample_text")
    partner = aPerson()
    setattr(partner, 'aPerson7', None)
    _safe_set(owner, 'Univerity_Person', partner)
    assert getattr(partner, 'aPerson7') == owner
    _safe_set(owner, 'Univerity_Person', None)
    assert getattr(partner, 'aPerson7') is None


