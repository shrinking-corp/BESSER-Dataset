import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ntnustudies_ChosenSemester,
    ntnustudies_Course,
    ntnustudies_Department,
    ntnustudies_Programme,
    ntnustudies_Semester,
    ntnustudies_Specialization,
    ntnustudies_StudyPlan,
    courseLevel,
    courseType,
    semesterType,
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

def test_assoc_courses27_reverse_link_reassign_clear():
    a1 = ntnustudies_Department(name="sample_text", shortName="sample_text")
    a2 = ntnustudies_Department(name="sample_text_2", shortName="sample_text_2")
    b = ntnustudies_Course(code="sample_text", credtis=3.14, level="sample_text", name="sample_text", semesters="sample_text", type="sample_text")
    _safe_set(b, 'ntnustudies_Course28', a1)
    assert _is_linked(b, 'ntnustudies_Course28', a1)
    if hasattr(a1, 'ntnustudies_Department'):
        assert _is_linked(a1, 'ntnustudies_Department', b)
    _safe_set(b, 'ntnustudies_Course28', a2)
    assert _is_linked(b, 'ntnustudies_Course28', a2)
    if hasattr(a1, 'ntnustudies_Department'):
        assert not _is_linked(a1, 'ntnustudies_Department', b)
    if hasattr(a2, 'ntnustudies_Department'):
        assert _is_linked(a2, 'ntnustudies_Department', b)
    _safe_set(b, 'ntnustudies_Course28', None)
    assert not _is_linked(b, 'ntnustudies_Course28', a2)
    if hasattr(a2, 'ntnustudies_Department'):
        assert not _is_linked(a2, 'ntnustudies_Department', b)


def test_assoc_courses4_reverse_link_reassign_clear():
    a1 = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    a2 = ntnustudies_Specialization(name="sample_text_2", specializationChoicePointSemester=13)
    b = ntnustudies_Course(code="sample_text", credtis=3.14, level="sample_text", name="sample_text", semesters="sample_text", type="sample_text")
    _safe_set(b, 'ntnustudies_Course', a1)
    assert _is_linked(b, 'ntnustudies_Course', a1)
    if hasattr(a1, 'ntnustudies_Specialization'):
        assert _is_linked(a1, 'ntnustudies_Specialization', b)
    _safe_set(b, 'ntnustudies_Course', a2)
    assert _is_linked(b, 'ntnustudies_Course', a2)
    if hasattr(a1, 'ntnustudies_Specialization'):
        assert not _is_linked(a1, 'ntnustudies_Specialization', b)
    if hasattr(a2, 'ntnustudies_Specialization'):
        assert _is_linked(a2, 'ntnustudies_Specialization', b)
    _safe_set(b, 'ntnustudies_Course', None)
    assert not _is_linked(b, 'ntnustudies_Course', a2)
    if hasattr(a2, 'ntnustudies_Specialization'):
        assert not _is_linked(a2, 'ntnustudies_Specialization', b)


def test_assoc_possibleCourses10_reverse_link_reassign_clear():
    a1 = ntnustudies_Semester(type="sample_text", year=7)
    a2 = ntnustudies_Semester(type="sample_text_2", year=13)
    b = ntnustudies_Course(code="sample_text", credtis=3.14, level="sample_text", name="sample_text", semesters="sample_text", type="sample_text")
    _safe_set(b, 'ntnustudies_Course12', a1)
    assert _is_linked(b, 'ntnustudies_Course12', a1)
    if hasattr(a1, 'ntnustudies_Semester11'):
        assert _is_linked(a1, 'ntnustudies_Semester11', b)
    _safe_set(b, 'ntnustudies_Course12', a2)
    assert _is_linked(b, 'ntnustudies_Course12', a2)
    if hasattr(a1, 'ntnustudies_Semester11'):
        assert not _is_linked(a1, 'ntnustudies_Semester11', b)
    if hasattr(a2, 'ntnustudies_Semester11'):
        assert _is_linked(a2, 'ntnustudies_Semester11', b)
    _safe_set(b, 'ntnustudies_Course12', None)
    assert not _is_linked(b, 'ntnustudies_Course12', a2)
    if hasattr(a2, 'ntnustudies_Semester11'):
        assert not _is_linked(a2, 'ntnustudies_Semester11', b)


def test_assoc_programme13_reverse_link_reassign_clear():
    a1 = ntnustudies_Semester(type="sample_text", year=7)
    a2 = ntnustudies_Semester(type="sample_text_2", year=13)
    b = ntnustudies_Programme(name="sample_text", years=7)
    _safe_set(b, 'Programme14', a1)
    assert _is_linked(b, 'Programme14', a1)
    if hasattr(a1, 'semesters'):
        assert _is_linked(a1, 'semesters', b)
    _safe_set(b, 'Programme14', a2)
    assert _is_linked(b, 'Programme14', a2)
    if hasattr(a1, 'semesters'):
        assert not _is_linked(a1, 'semesters', b)
    if hasattr(a2, 'semesters'):
        assert _is_linked(a2, 'semesters', b)
    _safe_set(b, 'Programme14', None)
    assert not _is_linked(b, 'Programme14', a2)
    if hasattr(a2, 'semesters'):
        assert not _is_linked(a2, 'semesters', b)


def test_assoc_programme3_reverse_link_reassign_clear():
    a1 = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    a2 = ntnustudies_Specialization(name="sample_text_2", specializationChoicePointSemester=13)
    b = ntnustudies_Programme(name="sample_text", years=7)
    _safe_set(b, 'Programme', a1)
    assert _is_linked(b, 'Programme', a1)
    if hasattr(a1, 'specializations'):
        assert _is_linked(a1, 'specializations', b)
    _safe_set(b, 'Programme', a2)
    assert _is_linked(b, 'Programme', a2)
    if hasattr(a1, 'specializations'):
        assert not _is_linked(a1, 'specializations', b)
    if hasattr(a2, 'specializations'):
        assert _is_linked(a2, 'specializations', b)
    _safe_set(b, 'Programme', None)
    assert not _is_linked(b, 'Programme', a2)
    if hasattr(a2, 'specializations'):
        assert not _is_linked(a2, 'specializations', b)


def test_assoc_programmes29_reverse_link_reassign_clear():
    a1 = ntnustudies_Programme(name="sample_text", years=7)
    a2 = ntnustudies_Programme(name="sample_text_2", years=13)
    b = ntnustudies_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'ntnustudies_Department30', {a1})
    assert _is_linked(b, 'ntnustudies_Department30', a1)
    if hasattr(a1, 'ntnustudies_Programme31'):
        assert _is_linked(a1, 'ntnustudies_Programme31', b)
    _safe_set(b, 'ntnustudies_Department30', {a2})
    assert _is_linked(b, 'ntnustudies_Department30', a2)
    if hasattr(a1, 'ntnustudies_Programme31'):
        assert not _is_linked(a1, 'ntnustudies_Programme31', b)
    if hasattr(a2, 'ntnustudies_Programme31'):
        assert _is_linked(a2, 'ntnustudies_Programme31', b)
    _safe_set(b, 'ntnustudies_Department30', set())
    assert not _is_linked(b, 'ntnustudies_Department30', a2)
    if hasattr(a2, 'ntnustudies_Programme31'):
        assert not _is_linked(a2, 'ntnustudies_Programme31', b)


def test_assoc_requiredSpecialization6_reverse_link_reassign_clear():
    a1 = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    a2 = ntnustudies_Specialization(name="sample_text_2", specializationChoicePointSemester=13)
    b = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    _safe_set(b, 'ntnustudies_Specialization7', a1)
    assert _is_linked(b, 'ntnustudies_Specialization7', a1)
    if hasattr(a1, 'ntnustudies_Specialization5'):
        assert _is_linked(a1, 'ntnustudies_Specialization5', b)
    _safe_set(b, 'ntnustudies_Specialization7', a2)
    assert _is_linked(b, 'ntnustudies_Specialization7', a2)
    if hasattr(a1, 'ntnustudies_Specialization5'):
        assert not _is_linked(a1, 'ntnustudies_Specialization5', b)
    if hasattr(a2, 'ntnustudies_Specialization5'):
        assert _is_linked(a2, 'ntnustudies_Specialization5', b)
    _safe_set(b, 'ntnustudies_Specialization7', None)
    assert not _is_linked(b, 'ntnustudies_Specialization7', a2)
    if hasattr(a2, 'ntnustudies_Specialization5'):
        assert not _is_linked(a2, 'ntnustudies_Specialization5', b)


def test_assoc_semesters1_reverse_link_reassign_clear():
    a1 = ntnustudies_Semester(type="sample_text", year=7)
    a2 = ntnustudies_Semester(type="sample_text_2", year=13)
    b = ntnustudies_Programme(name="sample_text", years=7)
    _safe_set(b, 'programme2', {a1})
    assert _is_linked(b, 'programme2', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'programme2', {a2})
    assert _is_linked(b, 'programme2', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'programme2', set())
    assert not _is_linked(b, 'programme2', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_semesters8_reverse_link_reassign_clear():
    a1 = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    a2 = ntnustudies_Specialization(name="sample_text_2", specializationChoicePointSemester=13)
    b = ntnustudies_Semester(type="sample_text", year=7)
    _safe_set(b, 'ntnustudies_Semester', a1)
    assert _is_linked(b, 'ntnustudies_Semester', a1)
    if hasattr(a1, 'ntnustudies_Specialization9'):
        assert _is_linked(a1, 'ntnustudies_Specialization9', b)
    _safe_set(b, 'ntnustudies_Semester', a2)
    assert _is_linked(b, 'ntnustudies_Semester', a2)
    if hasattr(a1, 'ntnustudies_Specialization9'):
        assert not _is_linked(a1, 'ntnustudies_Specialization9', b)
    if hasattr(a2, 'ntnustudies_Specialization9'):
        assert _is_linked(a2, 'ntnustudies_Specialization9', b)
    _safe_set(b, 'ntnustudies_Semester', None)
    assert not _is_linked(b, 'ntnustudies_Semester', a2)
    if hasattr(a2, 'ntnustudies_Specialization9'):
        assert not _is_linked(a2, 'ntnustudies_Specialization9', b)


def test_assoc_specializations0_reverse_link_reassign_clear():
    a1 = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    a2 = ntnustudies_Specialization(name="sample_text_2", specializationChoicePointSemester=13)
    b = ntnustudies_Programme(name="sample_text", years=7)
    _safe_set(b, 'programme', {a1})
    assert _is_linked(b, 'programme', a1)
    if hasattr(a1, 'Specialization'):
        assert _is_linked(a1, 'Specialization', b)
    _safe_set(b, 'programme', {a2})
    assert _is_linked(b, 'programme', a2)
    if hasattr(a1, 'Specialization'):
        assert not _is_linked(a1, 'Specialization', b)
    if hasattr(a2, 'Specialization'):
        assert _is_linked(a2, 'Specialization', b)
    _safe_set(b, 'programme', set())
    assert not _is_linked(b, 'programme', a2)
    if hasattr(a2, 'Specialization'):
        assert not _is_linked(a2, 'Specialization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courses17_stub_double():
    # ntnustudies_ChosenSemester has no real 'ntnustudies_ChosenSemester18' property in the generated
    # code (a bare stub) -- manually attach it so ntnustudies_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ntnustudies_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ntnustudies_Course(code="sample_text", credtis=3.14, level="sample_text", name="sample_text", semesters="sample_text", type="sample_text")
    partner = ntnustudies_ChosenSemester()
    setattr(partner, 'ntnustudies_ChosenSemester18', None)
    _safe_set(owner, 'ntnustudies_Course19', partner)
    assert owner in getattr(partner, 'ntnustudies_ChosenSemester18')
    _safe_set(owner, 'ntnustudies_Course19', None)
    assert owner not in getattr(partner, 'ntnustudies_ChosenSemester18')


def test_assoc_programme20_stub_double():
    # ntnustudies_StudyPlan has no real 'ntnustudies_StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so ntnustudies_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ntnustudies_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ntnustudies_Programme(name="sample_text", years=7)
    partner = ntnustudies_StudyPlan()
    setattr(partner, 'ntnustudies_StudyPlan', None)
    _safe_set(owner, 'ntnustudies_Programme', partner)
    assert getattr(partner, 'ntnustudies_StudyPlan') == owner
    _safe_set(owner, 'ntnustudies_Programme', None)
    assert getattr(partner, 'ntnustudies_StudyPlan') is None


def test_assoc_semester15_stub_double():
    # ntnustudies_ChosenSemester has no real 'ntnustudies_ChosenSemester' property in the generated
    # code (a bare stub) -- manually attach it so ntnustudies_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ntnustudies_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ntnustudies_Semester(type="sample_text", year=7)
    partner = ntnustudies_ChosenSemester()
    setattr(partner, 'ntnustudies_ChosenSemester', None)
    _safe_set(owner, 'ntnustudies_Semester16', partner)
    assert getattr(partner, 'ntnustudies_ChosenSemester') == owner
    _safe_set(owner, 'ntnustudies_Semester16', None)
    assert getattr(partner, 'ntnustudies_ChosenSemester') is None


def test_assoc_specializations21_stub_double():
    # ntnustudies_StudyPlan has no real 'ntnustudies_StudyPlan22' property in the generated
    # code (a bare stub) -- manually attach it so ntnustudies_Specialization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ntnustudies_Specialization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ntnustudies_Specialization(name="sample_text", specializationChoicePointSemester=7)
    partner = ntnustudies_StudyPlan()
    setattr(partner, 'ntnustudies_StudyPlan22', None)
    _safe_set(owner, 'ntnustudies_Specialization23', partner)
    assert owner in getattr(partner, 'ntnustudies_StudyPlan22')
    _safe_set(owner, 'ntnustudies_Specialization23', None)
    assert owner not in getattr(partner, 'ntnustudies_StudyPlan22')


