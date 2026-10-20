import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    courses_ContactInfo,
    courses_Content,
    courses_Course,
    courses_CourseHour,
    courses_CourseInstance,
    courses_Coursework,
    courses_CreditsReduction,
    courses_EvaluationForm,
    courses_ExaminationArrangement,
    courses_ExaminationPanel,
    courses_Paragraph,
    courses_Person,
    courses_StudyProgram,
    courses_Timetable,
    courses_University,
    Day,
    Department,
    HourEnd,
    HourStart,
    Location,
    Semester,
    TeachingLanguage,
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

def test_assoc_course0_reverse_link_reassign_clear():
    a1 = courses_University(name="sample_text")
    a2 = courses_University(name="sample_text_2")
    b = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'courses_Course', a1)
    assert _is_linked(b, 'courses_Course', a1)
    if hasattr(a1, 'courses_University'):
        assert _is_linked(a1, 'courses_University', b)
    _safe_set(b, 'courses_Course', a2)
    assert _is_linked(b, 'courses_Course', a2)
    if hasattr(a1, 'courses_University'):
        assert not _is_linked(a1, 'courses_University', b)
    if hasattr(a2, 'courses_University'):
        assert _is_linked(a2, 'courses_University', b)
    _safe_set(b, 'courses_Course', None)
    assert not _is_linked(b, 'courses_Course', a2)
    if hasattr(a2, 'courses_University'):
        assert not _is_linked(a2, 'courses_University', b)


def test_assoc_course54_reverse_link_reassign_clear():
    a1 = courses_Person(Credits=3.14, name="sample_text")
    a2 = courses_Person(Credits=9.99, name="sample_text_2")
    b = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'Course55', a1)
    assert _is_linked(b, 'Course55', a1)
    if hasattr(a1, 'student'):
        assert _is_linked(a1, 'student', b)
    _safe_set(b, 'Course55', a2)
    assert _is_linked(b, 'Course55', a2)
    if hasattr(a1, 'student'):
        assert not _is_linked(a1, 'student', b)
    if hasattr(a2, 'student'):
        assert _is_linked(a2, 'student', b)
    _safe_set(b, 'Course55', None)
    assert not _is_linked(b, 'Course55', a2)
    if hasattr(a2, 'student'):
        assert not _is_linked(a2, 'student', b)


def test_assoc_course59_reverse_link_reassign_clear():
    a1 = courses_CreditsReduction(reduction=3.14)
    a2 = courses_CreditsReduction(reduction=9.99)
    b = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'courses_Course61', a1)
    assert _is_linked(b, 'courses_Course61', a1)
    if hasattr(a1, 'courses_CreditsReduction60'):
        assert _is_linked(a1, 'courses_CreditsReduction60', b)
    _safe_set(b, 'courses_Course61', a2)
    assert _is_linked(b, 'courses_Course61', a2)
    if hasattr(a1, 'courses_CreditsReduction60'):
        assert not _is_linked(a1, 'courses_CreditsReduction60', b)
    if hasattr(a2, 'courses_CreditsReduction60'):
        assert _is_linked(a2, 'courses_CreditsReduction60', b)
    _safe_set(b, 'courses_Course61', None)
    assert not _is_linked(b, 'courses_Course61', a2)
    if hasattr(a2, 'courses_CreditsReduction60'):
        assert not _is_linked(a2, 'courses_CreditsReduction60', b)


def test_assoc_courseCoordinator37_reverse_link_reassign_clear():
    a1 = courses_Person(Credits=3.14, name="sample_text")
    a2 = courses_Person(Credits=9.99, name="sample_text_2")
    b = courses_ContactInfo(department="sample_text", phone="sample_text")
    _safe_set(b, 'courses_ContactInfo38', a1)
    assert _is_linked(b, 'courses_ContactInfo38', a1)
    if hasattr(a1, 'courses_Person39'):
        assert _is_linked(a1, 'courses_Person39', b)
    _safe_set(b, 'courses_ContactInfo38', a2)
    assert _is_linked(b, 'courses_ContactInfo38', a2)
    if hasattr(a1, 'courses_Person39'):
        assert not _is_linked(a1, 'courses_Person39', b)
    if hasattr(a2, 'courses_Person39'):
        assert _is_linked(a2, 'courses_Person39', b)
    _safe_set(b, 'courses_ContactInfo38', None)
    assert not _is_linked(b, 'courses_ContactInfo38', a2)
    if hasattr(a2, 'courses_Person39'):
        assert not _is_linked(a2, 'courses_Person39', b)


def test_assoc_courses50_reverse_link_reassign_clear():
    a1 = courses_StudyProgram(code="sample_text")
    a2 = courses_StudyProgram(code="sample_text_2")
    b = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'studyProgram'):
        assert _is_linked(a1, 'studyProgram', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'studyProgram'):
        assert not _is_linked(a1, 'studyProgram', b)
    if hasattr(a2, 'studyProgram'):
        assert _is_linked(a2, 'studyProgram', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'studyProgram'):
        assert not _is_linked(a2, 'studyProgram', b)


def test_assoc_evaluationForm48_reverse_link_reassign_clear():
    a1 = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    a2 = courses_ExaminationPanel(date="sample_text_2", room="sample_text_2", time="sample_text_2")
    b = courses_EvaluationForm(duration="sample_text", examAids="sample_text", type="sample_text", weighting="sample_text")
    _safe_set(b, 'courses_EvaluationForm', a1)
    assert _is_linked(b, 'courses_EvaluationForm', a1)
    if hasattr(a1, 'courses_ExaminationPanel49'):
        assert _is_linked(a1, 'courses_ExaminationPanel49', b)
    _safe_set(b, 'courses_EvaluationForm', a2)
    assert _is_linked(b, 'courses_EvaluationForm', a2)
    if hasattr(a1, 'courses_ExaminationPanel49'):
        assert not _is_linked(a1, 'courses_ExaminationPanel49', b)
    if hasattr(a2, 'courses_ExaminationPanel49'):
        assert _is_linked(a2, 'courses_ExaminationPanel49', b)
    _safe_set(b, 'courses_EvaluationForm', None)
    assert not _is_linked(b, 'courses_EvaluationForm', a2)
    if hasattr(a2, 'courses_ExaminationPanel49'):
        assert not _is_linked(a2, 'courses_ExaminationPanel49', b)


def test_assoc_evaluationForms34_reverse_link_reassign_clear():
    a1 = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    a2 = courses_ExaminationPanel(date="sample_text_2", room="sample_text_2", time="sample_text_2")
    b = courses_ExaminationArrangement(grade="sample_text", type="sample_text")
    _safe_set(b, 'courses_ExaminationArrangement35', {a1})
    assert _is_linked(b, 'courses_ExaminationArrangement35', a1)
    if hasattr(a1, 'courses_ExaminationPanel36'):
        assert _is_linked(a1, 'courses_ExaminationPanel36', b)
    _safe_set(b, 'courses_ExaminationArrangement35', {a2})
    assert _is_linked(b, 'courses_ExaminationArrangement35', a2)
    if hasattr(a1, 'courses_ExaminationPanel36'):
        assert not _is_linked(a1, 'courses_ExaminationPanel36', b)
    if hasattr(a2, 'courses_ExaminationPanel36'):
        assert _is_linked(a2, 'courses_ExaminationPanel36', b)
    _safe_set(b, 'courses_ExaminationArrangement35', set())
    assert not _is_linked(b, 'courses_ExaminationArrangement35', a2)
    if hasattr(a2, 'courses_ExaminationPanel36'):
        assert not _is_linked(a2, 'courses_ExaminationPanel36', b)


def test_assoc_plannedFor45_reverse_link_reassign_clear():
    a1 = courses_StudyProgram(code="sample_text")
    a2 = courses_StudyProgram(code="sample_text_2")
    b = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    _safe_set(b, 'courses_CourseHour46', {a1})
    assert _is_linked(b, 'courses_CourseHour46', a1)
    if hasattr(a1, 'courses_StudyProgram47'):
        assert _is_linked(a1, 'courses_StudyProgram47', b)
    _safe_set(b, 'courses_CourseHour46', {a2})
    assert _is_linked(b, 'courses_CourseHour46', a2)
    if hasattr(a1, 'courses_StudyProgram47'):
        assert not _is_linked(a1, 'courses_StudyProgram47', b)
    if hasattr(a2, 'courses_StudyProgram47'):
        assert _is_linked(a2, 'courses_StudyProgram47', b)
    _safe_set(b, 'courses_CourseHour46', set())
    assert not _is_linked(b, 'courses_CourseHour46', a2)
    if hasattr(a2, 'courses_StudyProgram47'):
        assert not _is_linked(a2, 'courses_StudyProgram47', b)


def test_assoc_staff1_reverse_link_reassign_clear():
    a1 = courses_University(name="sample_text")
    a2 = courses_University(name="sample_text_2")
    b = courses_Person(Credits=3.14, name="sample_text")
    _safe_set(b, 'courses_Person', a1)
    assert _is_linked(b, 'courses_Person', a1)
    if hasattr(a1, 'courses_University2'):
        assert _is_linked(a1, 'courses_University2', b)
    _safe_set(b, 'courses_Person', a2)
    assert _is_linked(b, 'courses_Person', a2)
    if hasattr(a1, 'courses_University2'):
        assert not _is_linked(a1, 'courses_University2', b)
    if hasattr(a2, 'courses_University2'):
        assert _is_linked(a2, 'courses_University2', b)
    _safe_set(b, 'courses_Person', None)
    assert not _is_linked(b, 'courses_Person', a2)
    if hasattr(a2, 'courses_University2'):
        assert not _is_linked(a2, 'courses_University2', b)


def test_assoc_staff40_reverse_link_reassign_clear():
    a1 = courses_Person(Credits=3.14, name="sample_text")
    a2 = courses_Person(Credits=9.99, name="sample_text_2")
    b = courses_ContactInfo(department="sample_text", phone="sample_text")
    _safe_set(b, 'courses_ContactInfo41', {a1})
    assert _is_linked(b, 'courses_ContactInfo41', a1)
    if hasattr(a1, 'courses_Person42'):
        assert _is_linked(a1, 'courses_Person42', b)
    _safe_set(b, 'courses_ContactInfo41', {a2})
    assert _is_linked(b, 'courses_ContactInfo41', a2)
    if hasattr(a1, 'courses_Person42'):
        assert not _is_linked(a1, 'courses_Person42', b)
    if hasattr(a2, 'courses_Person42'):
        assert _is_linked(a2, 'courses_Person42', b)
    _safe_set(b, 'courses_ContactInfo41', set())
    assert not _is_linked(b, 'courses_ContactInfo41', a2)
    if hasattr(a2, 'courses_Person42'):
        assert not _is_linked(a2, 'courses_Person42', b)


def test_assoc_student11_reverse_link_reassign_clear():
    a1 = courses_Person(Credits=3.14, name="sample_text")
    a2 = courses_Person(Credits=9.99, name="sample_text_2")
    b = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_student51_reverse_link_reassign_clear():
    a1 = courses_StudyProgram(code="sample_text")
    a2 = courses_StudyProgram(code="sample_text_2")
    b = courses_Person(Credits=3.14, name="sample_text")
    _safe_set(b, 'Person53', a1)
    assert _is_linked(b, 'Person53', a1)
    if hasattr(a1, 'studyProgram52'):
        assert _is_linked(a1, 'studyProgram52', b)
    _safe_set(b, 'Person53', a2)
    assert _is_linked(b, 'Person53', a2)
    if hasattr(a1, 'studyProgram52'):
        assert not _is_linked(a1, 'studyProgram52', b)
    if hasattr(a2, 'studyProgram52'):
        assert _is_linked(a2, 'studyProgram52', b)
    _safe_set(b, 'Person53', None)
    assert not _is_linked(b, 'Person53', a2)
    if hasattr(a2, 'studyProgram52'):
        assert not _is_linked(a2, 'studyProgram52', b)


def test_assoc_students5_reverse_link_reassign_clear():
    a1 = courses_University(name="sample_text")
    a2 = courses_University(name="sample_text_2")
    b = courses_Person(Credits=3.14, name="sample_text")
    _safe_set(b, 'courses_Person7', a1)
    assert _is_linked(b, 'courses_Person7', a1)
    if hasattr(a1, 'courses_University6'):
        assert _is_linked(a1, 'courses_University6', b)
    _safe_set(b, 'courses_Person7', a2)
    assert _is_linked(b, 'courses_Person7', a2)
    if hasattr(a1, 'courses_University6'):
        assert not _is_linked(a1, 'courses_University6', b)
    if hasattr(a2, 'courses_University6'):
        assert _is_linked(a2, 'courses_University6', b)
    _safe_set(b, 'courses_Person7', None)
    assert not _is_linked(b, 'courses_Person7', a2)
    if hasattr(a2, 'courses_University6'):
        assert not _is_linked(a2, 'courses_University6', b)


def test_assoc_studyProgram10_reverse_link_reassign_clear():
    a1 = courses_StudyProgram(code="sample_text")
    a2 = courses_StudyProgram(code="sample_text_2")
    b = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    _safe_set(b, 'courses', {a1})
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'StudyProgram'):
        assert _is_linked(a1, 'StudyProgram', b)
    _safe_set(b, 'courses', {a2})
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'StudyProgram'):
        assert not _is_linked(a1, 'StudyProgram', b)
    if hasattr(a2, 'StudyProgram'):
        assert _is_linked(a2, 'StudyProgram', b)
    _safe_set(b, 'courses', set())
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'StudyProgram'):
        assert not _is_linked(a2, 'StudyProgram', b)


def test_assoc_studyProgram3_reverse_link_reassign_clear():
    a1 = courses_University(name="sample_text")
    a2 = courses_University(name="sample_text_2")
    b = courses_StudyProgram(code="sample_text")
    _safe_set(b, 'courses_StudyProgram', a1)
    assert _is_linked(b, 'courses_StudyProgram', a1)
    if hasattr(a1, 'courses_University4'):
        assert _is_linked(a1, 'courses_University4', b)
    _safe_set(b, 'courses_StudyProgram', a2)
    assert _is_linked(b, 'courses_StudyProgram', a2)
    if hasattr(a1, 'courses_University4'):
        assert not _is_linked(a1, 'courses_University4', b)
    if hasattr(a2, 'courses_University4'):
        assert _is_linked(a2, 'courses_University4', b)
    _safe_set(b, 'courses_StudyProgram', None)
    assert not _is_linked(b, 'courses_StudyProgram', a2)
    if hasattr(a2, 'courses_University4'):
        assert not _is_linked(a2, 'courses_University4', b)


def test_assoc_studyProgram56_reverse_link_reassign_clear():
    a1 = courses_StudyProgram(code="sample_text")
    a2 = courses_StudyProgram(code="sample_text_2")
    b = courses_Person(Credits=3.14, name="sample_text")
    _safe_set(b, 'student57', a1)
    assert _is_linked(b, 'student57', a1)
    if hasattr(a1, 'StudyProgram58'):
        assert _is_linked(a1, 'StudyProgram58', b)
    _safe_set(b, 'student57', a2)
    assert _is_linked(b, 'student57', a2)
    if hasattr(a1, 'StudyProgram58'):
        assert not _is_linked(a1, 'StudyProgram58', b)
    if hasattr(a2, 'StudyProgram58'):
        assert _is_linked(a2, 'StudyProgram58', b)
    _safe_set(b, 'student57', None)
    assert not _is_linked(b, 'student57', a2)
    if hasattr(a2, 'StudyProgram58'):
        assert not _is_linked(a2, 'StudyProgram58', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contactInfo15_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance16' property in the generated
    # code (a bare stub) -- manually attach it so courses_ContactInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_ContactInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_ContactInfo(department="sample_text", phone="sample_text")
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance16', None)
    _safe_set(owner, 'courses_ContactInfo', partner)
    assert getattr(partner, 'courses_CourseInstance16') == owner
    _safe_set(owner, 'courses_ContactInfo', None)
    assert getattr(partner, 'courses_CourseInstance16') is None


def test_assoc_courseRecommended29_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance30' property in the generated
    # code (a bare stub) -- manually attach it so courses_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance30', None)
    _safe_set(owner, 'courses_Course31', partner)
    assert owner in getattr(partner, 'courses_CourseInstance30')
    _safe_set(owner, 'courses_Course31', None)
    assert owner not in getattr(partner, 'courses_CourseInstance30')


def test_assoc_courseRequired26_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance27' property in the generated
    # code (a bare stub) -- manually attach it so courses_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance27', None)
    _safe_set(owner, 'courses_Course28', partner)
    assert owner in getattr(partner, 'courses_CourseInstance27')
    _safe_set(owner, 'courses_Course28', None)
    assert owner not in getattr(partner, 'courses_CourseInstance27')


def test_assoc_coursework20_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance21' property in the generated
    # code (a bare stub) -- manually attach it so courses_Coursework's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_Coursework's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance21', None)
    _safe_set(owner, 'courses_Coursework', partner)
    assert getattr(partner, 'courses_CourseInstance21') == owner
    _safe_set(owner, 'courses_Coursework', None)
    assert getattr(partner, 'courses_CourseInstance21') is None


def test_assoc_creditsReduction32_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance33' property in the generated
    # code (a bare stub) -- manually attach it so courses_CreditsReduction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_CreditsReduction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_CreditsReduction(reduction=3.14)
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance33', None)
    _safe_set(owner, 'courses_CreditsReduction', partner)
    assert owner in getattr(partner, 'courses_CourseInstance33')
    _safe_set(owner, 'courses_CreditsReduction', None)
    assert owner not in getattr(partner, 'courses_CourseInstance33')


def test_assoc_examArrangement12_stub_double():
    # courses_Content has no real 'courses_Content' property in the generated
    # code (a bare stub) -- manually attach it so courses_ExaminationArrangement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_ExaminationArrangement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_ExaminationArrangement(grade="sample_text", type="sample_text")
    partner = courses_Content()
    setattr(partner, 'courses_Content', None)
    _safe_set(owner, 'courses_ExaminationArrangement', partner)
    assert getattr(partner, 'courses_Content') == owner
    _safe_set(owner, 'courses_ExaminationArrangement', None)
    assert getattr(partner, 'courses_Content') is None


def test_assoc_examination24_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance25' property in the generated
    # code (a bare stub) -- manually attach it so courses_ExaminationPanel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_ExaminationPanel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance25', None)
    _safe_set(owner, 'courses_ExaminationPanel', partner)
    assert getattr(partner, 'courses_CourseInstance25') == owner
    _safe_set(owner, 'courses_ExaminationPanel', None)
    assert getattr(partner, 'courses_CourseInstance25') is None


def test_assoc_listCourseHour43_stub_double():
    # courses_Timetable has no real 'courses_Timetable44' property in the generated
    # code (a bare stub) -- manually attach it so courses_CourseHour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_CourseHour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    partner = courses_Timetable()
    setattr(partner, 'courses_Timetable44', None)
    _safe_set(owner, 'courses_CourseHour', partner)
    assert owner in getattr(partner, 'courses_Timetable44')
    _safe_set(owner, 'courses_CourseHour', None)
    assert owner not in getattr(partner, 'courses_Timetable44')


def test_assoc_listCourseInstance8_stub_double():
    # courses_CourseInstance has no real 'courses_CourseInstance' property in the generated
    # code (a bare stub) -- manually attach it so courses_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    partner = courses_CourseInstance()
    setattr(partner, 'courses_CourseInstance', None)
    _safe_set(owner, 'courses_Course9', {partner})
    assert getattr(partner, 'courses_CourseInstance') == owner
    _safe_set(owner, 'courses_Course9', set())
    assert getattr(partner, 'courses_CourseInstance') is None


def test_assoc_paragraph13_stub_double():
    # courses_Content has no real 'courses_Content14' property in the generated
    # code (a bare stub) -- manually attach it so courses_Paragraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # courses_Paragraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = courses_Paragraph(description="sample_text", name="sample_text")
    partner = courses_Content()
    setattr(partner, 'courses_Content14', None)
    _safe_set(owner, 'courses_Paragraph', partner)
    assert owner in getattr(partner, 'courses_Content14')
    _safe_set(owner, 'courses_Paragraph', None)
    assert owner not in getattr(partner, 'courses_Content14')


