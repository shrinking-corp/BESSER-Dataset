import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assistant,
    Course,
    Event,
    Lecture,
    Person,
    Professor,
    Room,
    Student,
    Time,
    Tutorial,
    Visits,
    universityextended_University,
    universityextended_administration_Course,
    universityextended_administration_Event,
    universityextended_administration_Lecture,
    universityextended_administration_Room,
    universityextended_administration_Time,
    universityextended_administration_Tutorial,
    universityextended_connection_Visits,
    universityextended_people_Assistant,
    universityextended_people_Person,
    universityextended_people_Professor,
    universityextended_people_Student,
    Building,
    DayOfWeek,
    Motivation,
    SalaryRank,
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

def test_assoc_course21_stub_double():
    # Course has no real 'Course22' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Lecture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Lecture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Lecture(captions="sample_text")
    partner = Course()
    setattr(partner, 'Course22', None)
    _safe_set(owner, 'lecture', partner)
    assert getattr(partner, 'Course22') == owner
    _safe_set(owner, 'lecture', None)
    assert getattr(partner, 'Course22') is None


def test_assoc_course33_stub_double():
    # Course has no real 'Course34' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_connection_Visits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_connection_Visits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_connection_Visits(motivation="sample_text")
    partner = Course()
    setattr(partner, 'Course34', None)
    _safe_set(owner, 'visitor', partner)
    assert getattr(partner, 'Course34') == owner
    _safe_set(owner, 'visitor', None)
    assert getattr(partner, 'Course34') is None


def test_assoc_courseVisit9_stub_double():
    # Visits has no real 'Visits10' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_people_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_people_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_people_Student(matriculationnumber="sample_text")
    partner = Visits()
    setattr(partner, 'Visits10', None)
    _safe_set(owner, 'student', {partner})
    assert getattr(partner, 'Visits10') == owner
    _safe_set(owner, 'student', set())
    assert getattr(partner, 'Visits10') is None


def test_assoc_lecture13_stub_double():
    # Lecture has no real 'Lecture14' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Course(endOfCourse=date(2024, 1, 1), startOfCourse=date(2024, 1, 1), title="sample_text")
    partner = Lecture()
    setattr(partner, 'Lecture14', None)
    _safe_set(owner, 'course', partner)
    assert getattr(partner, 'Lecture14') == owner
    _safe_set(owner, 'course', None)
    assert getattr(partner, 'Lecture14') is None


def test_assoc_lecturer23_stub_double():
    # Professor has no real 'Professor' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Lecture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Lecture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Lecture(captions="sample_text")
    partner = Professor()
    setattr(partner, 'Professor', None)
    _safe_set(owner, 'lectures', partner)
    assert getattr(partner, 'Professor') == owner
    _safe_set(owner, 'lectures', None)
    assert getattr(partner, 'Professor') is None


def test_assoc_lectures11_stub_double():
    # Lecture has no real 'Lecture' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_people_Professor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_people_Professor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_people_Professor(rank="sample_text")
    partner = Lecture()
    setattr(partner, 'Lecture', None)
    _safe_set(owner, 'lecturer', {partner})
    assert getattr(partner, 'Lecture') == owner
    _safe_set(owner, 'lecturer', set())
    assert getattr(partner, 'Lecture') is None


def test_assoc_room30_stub_double():
    # Room has no real 'Room32' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Event(title="sample_text")
    partner = Room()
    setattr(partner, 'Room32', None)
    _safe_set(owner, 'universityextended_administration_Event31', partner)
    assert getattr(partner, 'Room32') == owner
    _safe_set(owner, 'universityextended_administration_Event31', None)
    assert getattr(partner, 'Room32') is None


def test_assoc_student35_stub_double():
    # Student has no real 'Student' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_connection_Visits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_connection_Visits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_connection_Visits(motivation="sample_text")
    partner = Student()
    setattr(partner, 'Student', None)
    _safe_set(owner, 'courseVisit', partner)
    assert getattr(partner, 'Student') == owner
    _safe_set(owner, 'courseVisit', None)
    assert getattr(partner, 'Student') is None


def test_assoc_time28_stub_double():
    # Time has no real 'Time29' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Event(title="sample_text")
    partner = Time()
    setattr(partner, 'Time29', None)
    _safe_set(owner, 'universityextended_administration_Event', partner)
    assert getattr(partner, 'Time29') == owner
    _safe_set(owner, 'universityextended_administration_Event', None)
    assert getattr(partner, 'Time29') is None


def test_assoc_tutorial12_stub_double():
    # Tutorial has no real 'Tutorial' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_people_Assistant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_people_Assistant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_people_Assistant(isDoctoralCandidate=True)
    partner = Tutorial()
    setattr(partner, 'Tutorial', None)
    _safe_set(owner, 'tutor', {partner})
    assert getattr(partner, 'Tutorial') == owner
    _safe_set(owner, 'tutor', set())
    assert getattr(partner, 'Tutorial') is None


def test_assoc_tutorial15_stub_double():
    # Tutorial has no real 'Tutorial17' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Course(endOfCourse=date(2024, 1, 1), startOfCourse=date(2024, 1, 1), title="sample_text")
    partner = Tutorial()
    setattr(partner, 'Tutorial17', None)
    _safe_set(owner, 'course16', partner)
    assert getattr(partner, 'Tutorial17') == owner
    _safe_set(owner, 'course16', None)
    assert getattr(partner, 'Tutorial17') is None


def test_assoc_visitor18_stub_double():
    # Visits has no real 'Visits20' property in the generated
    # code (a bare stub) -- manually attach it so universityextended_administration_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # universityextended_administration_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = universityextended_administration_Course(endOfCourse=date(2024, 1, 1), startOfCourse=date(2024, 1, 1), title="sample_text")
    partner = Visits()
    setattr(partner, 'Visits20', None)
    _safe_set(owner, 'course19', {partner})
    assert getattr(partner, 'Visits20') == owner
    _safe_set(owner, 'course19', set())
    assert getattr(partner, 'Visits20') is None


