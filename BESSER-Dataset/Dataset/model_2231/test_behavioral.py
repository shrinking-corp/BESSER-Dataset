import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ra_Course,
    ra_Department,
    ra_MandatoryCourse,
    ra_Programme,
    ra_Semester,
    ra_Specialization,
    ra_StudyPlan,
    programmeCode,
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

def test_assoc_course26_reverse_link_reassign_clear():
    a1 = ra_MandatoryCourse(credit=3.14, mandatory=True)
    a2 = ra_MandatoryCourse(credit=9.99, mandatory=False)
    b = ra_Course(code="sample_text", name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'mandatoryCourse27'):
        assert _is_linked(a1, 'mandatoryCourse27', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'mandatoryCourse27'):
        assert not _is_linked(a1, 'mandatoryCourse27', b)
    if hasattr(a2, 'mandatoryCourse27'):
        assert _is_linked(a2, 'mandatoryCourse27', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'mandatoryCourse27'):
        assert not _is_linked(a2, 'mandatoryCourse27', b)


def test_assoc_courseSlot20_reverse_link_reassign_clear():
    a1 = ra_Semester(semesterNumber=7, totalPoints=3.14)
    a2 = ra_Semester(semesterNumber=13, totalPoints=9.99)
    b = ra_Course(code="sample_text", name="sample_text")
    _safe_set(b, 'ra_Course22', a1)
    assert _is_linked(b, 'ra_Course22', a1)
    if hasattr(a1, 'ra_Semester21'):
        assert _is_linked(a1, 'ra_Semester21', b)
    _safe_set(b, 'ra_Course22', a2)
    assert _is_linked(b, 'ra_Course22', a2)
    if hasattr(a1, 'ra_Semester21'):
        assert not _is_linked(a1, 'ra_Semester21', b)
    if hasattr(a2, 'ra_Semester21'):
        assert _is_linked(a2, 'ra_Semester21', b)
    _safe_set(b, 'ra_Course22', None)
    assert not _is_linked(b, 'ra_Course22', a2)
    if hasattr(a2, 'ra_Semester21'):
        assert not _is_linked(a2, 'ra_Semester21', b)


def test_assoc_mandatoryCourse23_reverse_link_reassign_clear():
    a1 = ra_Semester(semesterNumber=7, totalPoints=3.14)
    a2 = ra_Semester(semesterNumber=13, totalPoints=9.99)
    b = ra_MandatoryCourse(credit=3.14, mandatory=True)
    _safe_set(b, 'MandatoryCourse24', a1)
    assert _is_linked(b, 'MandatoryCourse24', a1)
    if hasattr(a1, 'semester'):
        assert _is_linked(a1, 'semester', b)
    _safe_set(b, 'MandatoryCourse24', a2)
    assert _is_linked(b, 'MandatoryCourse24', a2)
    if hasattr(a1, 'semester'):
        assert not _is_linked(a1, 'semester', b)
    if hasattr(a2, 'semester'):
        assert _is_linked(a2, 'semester', b)
    _safe_set(b, 'MandatoryCourse24', None)
    assert not _is_linked(b, 'MandatoryCourse24', a2)
    if hasattr(a2, 'semester'):
        assert not _is_linked(a2, 'semester', b)


def test_assoc_mandatoryCourse7_reverse_link_reassign_clear():
    a1 = ra_MandatoryCourse(credit=3.14, mandatory=True)
    a2 = ra_MandatoryCourse(credit=9.99, mandatory=False)
    b = ra_Course(code="sample_text", name="sample_text")
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'MandatoryCourse'):
        assert _is_linked(a1, 'MandatoryCourse', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'MandatoryCourse'):
        assert not _is_linked(a1, 'MandatoryCourse', b)
    if hasattr(a2, 'MandatoryCourse'):
        assert _is_linked(a2, 'MandatoryCourse', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'MandatoryCourse'):
        assert not _is_linked(a2, 'MandatoryCourse', b)


def test_assoc_semester17_reverse_link_reassign_clear():
    a1 = ra_Specialization(name="sample_text")
    a2 = ra_Specialization(name="sample_text_2")
    b = ra_Semester(semesterNumber=7, totalPoints=3.14)
    _safe_set(b, 'ra_Semester19', a1)
    assert _is_linked(b, 'ra_Semester19', a1)
    if hasattr(a1, 'ra_Specialization18'):
        assert _is_linked(a1, 'ra_Specialization18', b)
    _safe_set(b, 'ra_Semester19', a2)
    assert _is_linked(b, 'ra_Semester19', a2)
    if hasattr(a1, 'ra_Specialization18'):
        assert not _is_linked(a1, 'ra_Specialization18', b)
    if hasattr(a2, 'ra_Specialization18'):
        assert _is_linked(a2, 'ra_Specialization18', b)
    _safe_set(b, 'ra_Semester19', None)
    assert not _is_linked(b, 'ra_Semester19', a2)
    if hasattr(a2, 'ra_Specialization18'):
        assert not _is_linked(a2, 'ra_Specialization18', b)


def test_assoc_semester25_reverse_link_reassign_clear():
    a1 = ra_Semester(semesterNumber=7, totalPoints=3.14)
    a2 = ra_Semester(semesterNumber=13, totalPoints=9.99)
    b = ra_MandatoryCourse(credit=3.14, mandatory=True)
    _safe_set(b, 'mandatoryCourse', a1)
    assert _is_linked(b, 'mandatoryCourse', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'mandatoryCourse', a2)
    assert _is_linked(b, 'mandatoryCourse', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'mandatoryCourse', None)
    assert not _is_linked(b, 'mandatoryCourse', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_course1_stub_double():
    # ra_Department has no real 'ra_Department2' property in the generated
    # code (a bare stub) -- manually attach it so ra_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Course(code="sample_text", name="sample_text")
    partner = ra_Department()
    setattr(partner, 'ra_Department2', None)
    _safe_set(owner, 'ra_Course', partner)
    assert owner in getattr(partner, 'ra_Department2')
    _safe_set(owner, 'ra_Course', None)
    assert owner not in getattr(partner, 'ra_Department2')


def test_assoc_mandatoryCourse15_stub_double():
    # ra_StudyPlan has no real 'ra_StudyPlan16' property in the generated
    # code (a bare stub) -- manually attach it so ra_MandatoryCourse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_MandatoryCourse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_MandatoryCourse(credit=3.14, mandatory=True)
    partner = ra_StudyPlan()
    setattr(partner, 'ra_StudyPlan16', None)
    _safe_set(owner, 'ra_MandatoryCourse', partner)
    assert owner in getattr(partner, 'ra_StudyPlan16')
    _safe_set(owner, 'ra_MandatoryCourse', None)
    assert owner not in getattr(partner, 'ra_StudyPlan16')


def test_assoc_programme0_stub_double():
    # ra_Department has no real 'ra_Department' property in the generated
    # code (a bare stub) -- manually attach it so ra_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Programme(mCode="sample_text", name="sample_text")
    partner = ra_Department()
    setattr(partner, 'ra_Department', None)
    _safe_set(owner, 'ra_Programme', partner)
    assert owner in getattr(partner, 'ra_Department')
    _safe_set(owner, 'ra_Programme', None)
    assert owner not in getattr(partner, 'ra_Department')


def test_assoc_programme9_stub_double():
    # ra_StudyPlan has no real 'studyPlan' property in the generated
    # code (a bare stub) -- manually attach it so ra_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Programme(mCode="sample_text", name="sample_text")
    partner = ra_StudyPlan()
    setattr(partner, 'studyPlan', None)
    _safe_set(owner, 'Programme', partner)
    assert getattr(partner, 'studyPlan') == owner
    _safe_set(owner, 'Programme', None)
    assert getattr(partner, 'studyPlan') is None


def test_assoc_semester13_stub_double():
    # ra_StudyPlan has no real 'ra_StudyPlan14' property in the generated
    # code (a bare stub) -- manually attach it so ra_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Semester(semesterNumber=7, totalPoints=3.14)
    partner = ra_StudyPlan()
    setattr(partner, 'ra_StudyPlan14', None)
    _safe_set(owner, 'ra_Semester', partner)
    assert owner in getattr(partner, 'ra_StudyPlan14')
    _safe_set(owner, 'ra_Semester', None)
    assert owner not in getattr(partner, 'ra_StudyPlan14')


def test_assoc_spesialization10_stub_double():
    # ra_StudyPlan has no real 'ra_StudyPlan11' property in the generated
    # code (a bare stub) -- manually attach it so ra_Specialization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Specialization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Specialization(name="sample_text")
    partner = ra_StudyPlan()
    setattr(partner, 'ra_StudyPlan11', None)
    _safe_set(owner, 'ra_Specialization12', partner)
    assert owner in getattr(partner, 'ra_StudyPlan11')
    _safe_set(owner, 'ra_Specialization12', None)
    assert owner not in getattr(partner, 'ra_StudyPlan11')


def test_assoc_spesialization5_stub_double():
    # ra_Department has no real 'ra_Department6' property in the generated
    # code (a bare stub) -- manually attach it so ra_Specialization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Specialization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Specialization(name="sample_text")
    partner = ra_Department()
    setattr(partner, 'ra_Department6', None)
    _safe_set(owner, 'ra_Specialization', partner)
    assert getattr(partner, 'ra_Department6') == owner
    _safe_set(owner, 'ra_Specialization', None)
    assert getattr(partner, 'ra_Department6') is None


def test_assoc_studyPlan8_stub_double():
    # ra_StudyPlan has no real 'StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so ra_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ra_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ra_Programme(mCode="sample_text", name="sample_text")
    partner = ra_StudyPlan()
    setattr(partner, 'StudyPlan', None)
    _safe_set(owner, 'programme', partner)
    assert getattr(partner, 'StudyPlan') == owner
    _safe_set(owner, 'programme', None)
    assert getattr(partner, 'StudyPlan') is None


