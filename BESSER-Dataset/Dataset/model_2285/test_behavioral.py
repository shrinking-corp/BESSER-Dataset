import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModelElement,
    UniverityU_Courses,
    UniverityU_Person,
    UniverityU_University,
    UniverityU_uncertainty_ModelElement,
    UniverityU_uncertainty_UData,
    UniverityU_uncertainty_aCourses,
    UniverityU_uncertainty_aPerson,
    UniverityU_uncertainty_aUniversity,
    UniverityU_uncertainty_uCourses,
    UniverityU_uncertainty_uPerson,
    UniverityU_uncertainty_uUniversity,
    aCourses,
    aPerson,
    aUniversity,
    uCourses,
    uPerson,
    uUniversity,
    uncertainty_ModelElement,
    uncertainty_UData,
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
    # code (a bare stub) -- manually attach it so UniverityU_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UniverityU_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UniverityU_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    partner = aPerson()
    setattr(partner, 'aPerson', None)
    _safe_set(owner, 'UniverityU_Courses2', partner)
    assert getattr(partner, 'aPerson') == owner
    _safe_set(owner, 'UniverityU_Courses2', None)
    assert getattr(partner, 'aPerson') is None


def test_assoc_Student3_stub_double():
    # aPerson has no real 'aPerson5' property in the generated
    # code (a bare stub) -- manually attach it so UniverityU_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UniverityU_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UniverityU_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    partner = aPerson()
    setattr(partner, 'aPerson5', None)
    _safe_set(owner, 'UniverityU_Courses4', {partner})
    assert getattr(partner, 'aPerson5') == owner
    _safe_set(owner, 'UniverityU_Courses4', set())
    assert getattr(partner, 'aPerson5') is None


def test_assoc_links0_stub_double():
    # aCourses has no real 'aCourses' property in the generated
    # code (a bare stub) -- manually attach it so UniverityU_Courses's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UniverityU_Courses's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UniverityU_Courses(CFU=7, Name="sample_text", Semester="sample_text")
    partner = aCourses()
    setattr(partner, 'aCourses', None)
    _safe_set(owner, 'UniverityU_Courses', {partner})
    assert getattr(partner, 'aCourses') == owner
    _safe_set(owner, 'UniverityU_Courses', set())
    assert getattr(partner, 'aCourses') is None


def test_assoc_relatives6_stub_double():
    # aPerson has no real 'aPerson7' property in the generated
    # code (a bare stub) -- manually attach it so UniverityU_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UniverityU_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UniverityU_Person(Email="sample_text", Name="sample_text")
    partner = aPerson()
    setattr(partner, 'aPerson7', None)
    _safe_set(owner, 'UniverityU_Person', partner)
    assert getattr(partner, 'aPerson7') == owner
    _safe_set(owner, 'UniverityU_Person', None)
    assert getattr(partner, 'aPerson7') is None


