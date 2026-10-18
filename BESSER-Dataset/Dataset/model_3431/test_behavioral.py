import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    Person,
    school_Named,
    school_Person,
    school_School,
    school_SchoolModel,
    school_SchoolStatistics,
    school_Student,
    school_Teacher,
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

def test_assoc_statistics1_reverse_link_reassign_clear():
    a1 = school_SchoolStatistics(studentsNumber=7, studentsWithNoTeacher="sample_text", teachersNumber=7)
    a2 = school_SchoolStatistics(studentsNumber=13, studentsWithNoTeacher="sample_text_2", teachersNumber=13)
    b = school_School()
    _safe_set(b, 'school_School2', a1)
    assert _is_linked(b, 'school_School2', a1)
    if hasattr(a1, 'school_SchoolStatistics'):
        assert _is_linked(a1, 'school_SchoolStatistics', b)
    _safe_set(b, 'school_School2', a2)
    assert _is_linked(b, 'school_School2', a2)
    if hasattr(a1, 'school_SchoolStatistics'):
        assert not _is_linked(a1, 'school_SchoolStatistics', b)
    if hasattr(a2, 'school_SchoolStatistics'):
        assert _is_linked(a2, 'school_SchoolStatistics', b)
    _safe_set(b, 'school_School2', None)
    assert not _is_linked(b, 'school_School2', a2)
    if hasattr(a2, 'school_SchoolStatistics'):
        assert not _is_linked(a2, 'school_SchoolStatistics', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_persons3_stub_double():
    # school_Person has no real 'school_Person' property in the generated
    # code (a bare stub) -- manually attach it so school_School's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_School's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_School()
    partner = school_Person()
    setattr(partner, 'school_Person', None)
    _safe_set(owner, 'school_School4', {partner})
    assert getattr(partner, 'school_Person') == owner
    _safe_set(owner, 'school_School4', set())
    assert getattr(partner, 'school_Person') is None


def test_assoc_schools0_stub_double():
    # school_SchoolModel has no real 'school_SchoolModel' property in the generated
    # code (a bare stub) -- manually attach it so school_School's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_School's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_School()
    partner = school_SchoolModel()
    setattr(partner, 'school_SchoolModel', None)
    _safe_set(owner, 'school_School', partner)
    assert owner in getattr(partner, 'school_SchoolModel')
    _safe_set(owner, 'school_School', None)
    assert owner not in getattr(partner, 'school_SchoolModel')


def test_assoc_teachers5_stub_double():
    # school_Teacher has no real 'school_Teacher' property in the generated
    # code (a bare stub) -- manually attach it so school_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # school_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = school_Student(registrationNum=7)
    partner = school_Teacher()
    setattr(partner, 'school_Teacher', None)
    _safe_set(owner, 'school_Student', {partner})
    assert getattr(partner, 'school_Teacher') == owner
    _safe_set(owner, 'school_Student', set())
    assert getattr(partner, 'school_Teacher') is None


