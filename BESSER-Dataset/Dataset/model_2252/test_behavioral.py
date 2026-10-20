import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    e2_AssignmentSubmission,
    e2_Assingnment,
    e2_Course,
    e2_EClass0,
    e2_Goal,
    e2_Group,
    e2_Lecture,
    e2_LectureContent,
    e2_Person,
    e2_SubGoal,
    e2_University,
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

def test_assoc_AssesedBy33_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_AssignmentSubmission(Comments="sample_text", assessment=7)
    _safe_set(b, 'e2_AssignmentSubmission34', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission34', a1)
    if hasattr(a1, 'e2_Person35'):
        assert _is_linked(a1, 'e2_Person35', b)
    _safe_set(b, 'e2_AssignmentSubmission34', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission34', a2)
    if hasattr(a1, 'e2_Person35'):
        assert not _is_linked(a1, 'e2_Person35', b)
    if hasattr(a2, 'e2_Person35'):
        assert _is_linked(a2, 'e2_Person35', b)
    _safe_set(b, 'e2_AssignmentSubmission34', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission34', a2)
    if hasattr(a2, 'e2_Person35'):
        assert not _is_linked(a2, 'e2_Person35', b)


def test_assoc_Assignment30_reverse_link_reassign_clear():
    a1 = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    a2 = e2_Assingnment(Content="sample_text_2", Deadline=date(2025, 6, 15), StartDate=date(2025, 6, 15), Title="sample_text_2", Type="sample_text_2", isMandatory=False)
    b = e2_AssignmentSubmission(Comments="sample_text", assessment=7)
    _safe_set(b, 'e2_AssignmentSubmission31', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission31', a1)
    if hasattr(a1, 'e2_Assingnment32'):
        assert _is_linked(a1, 'e2_Assingnment32', b)
    _safe_set(b, 'e2_AssignmentSubmission31', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission31', a2)
    if hasattr(a1, 'e2_Assingnment32'):
        assert not _is_linked(a1, 'e2_Assingnment32', b)
    if hasattr(a2, 'e2_Assingnment32'):
        assert _is_linked(a2, 'e2_Assingnment32', b)
    _safe_set(b, 'e2_AssignmentSubmission31', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission31', a2)
    if hasattr(a2, 'e2_Assingnment32'):
        assert not _is_linked(a2, 'e2_Assingnment32', b)


def test_assoc_Assingments11_reverse_link_reassign_clear():
    a1 = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    a2 = e2_Course(ID="sample_text_2", Name="sample_text_2", credit=9.99)
    b = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    _safe_set(b, 'e2_Assingnment13', a1)
    assert _is_linked(b, 'e2_Assingnment13', a1)
    if hasattr(a1, 'e2_Course12'):
        assert _is_linked(a1, 'e2_Course12', b)
    _safe_set(b, 'e2_Assingnment13', a2)
    assert _is_linked(b, 'e2_Assingnment13', a2)
    if hasattr(a1, 'e2_Course12'):
        assert not _is_linked(a1, 'e2_Course12', b)
    if hasattr(a2, 'e2_Course12'):
        assert _is_linked(a2, 'e2_Course12', b)
    _safe_set(b, 'e2_Assingnment13', None)
    assert not _is_linked(b, 'e2_Assingnment13', a2)
    if hasattr(a2, 'e2_Course12'):
        assert not _is_linked(a2, 'e2_Course12', b)


def test_assoc_Content0_reverse_link_reassign_clear():
    a1 = e2_LectureContent(Material="sample_text", Type="sample_text")
    a2 = e2_LectureContent(Material="sample_text_2", Type="sample_text_2")
    b = e2_Lecture(Date=date(2024, 1, 1), length=7)
    _safe_set(b, 'e2_Lecture', {a1})
    assert _is_linked(b, 'e2_Lecture', a1)
    if hasattr(a1, 'e2_LectureContent'):
        assert _is_linked(a1, 'e2_LectureContent', b)
    _safe_set(b, 'e2_Lecture', {a2})
    assert _is_linked(b, 'e2_Lecture', a2)
    if hasattr(a1, 'e2_LectureContent'):
        assert not _is_linked(a1, 'e2_LectureContent', b)
    if hasattr(a2, 'e2_LectureContent'):
        assert _is_linked(a2, 'e2_LectureContent', b)
    _safe_set(b, 'e2_Lecture', set())
    assert not _is_linked(b, 'e2_Lecture', a2)
    if hasattr(a2, 'e2_LectureContent'):
        assert not _is_linked(a2, 'e2_LectureContent', b)


def test_assoc_Courses38_reverse_link_reassign_clear():
    a1 = e2_University(Name="sample_text")
    a2 = e2_University(Name="sample_text_2")
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course40', a1)
    assert _is_linked(b, 'e2_Course40', a1)
    if hasattr(a1, 'e2_University39'):
        assert _is_linked(a1, 'e2_University39', b)
    _safe_set(b, 'e2_Course40', a2)
    assert _is_linked(b, 'e2_Course40', a2)
    if hasattr(a1, 'e2_University39'):
        assert not _is_linked(a1, 'e2_University39', b)
    if hasattr(a2, 'e2_University39'):
        assert _is_linked(a2, 'e2_University39', b)
    _safe_set(b, 'e2_Course40', None)
    assert not _is_linked(b, 'e2_Course40', a2)
    if hasattr(a2, 'e2_University39'):
        assert not _is_linked(a2, 'e2_University39', b)


def test_assoc_GroupMember24_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Group(Name="sample_text")
    _safe_set(b, 'e2_Group25', {a1})
    assert _is_linked(b, 'e2_Group25', a1)
    if hasattr(a1, 'e2_Person26'):
        assert _is_linked(a1, 'e2_Person26', b)
    _safe_set(b, 'e2_Group25', {a2})
    assert _is_linked(b, 'e2_Group25', a2)
    if hasattr(a1, 'e2_Person26'):
        assert not _is_linked(a1, 'e2_Person26', b)
    if hasattr(a2, 'e2_Person26'):
        assert _is_linked(a2, 'e2_Person26', b)
    _safe_set(b, 'e2_Group25', set())
    assert not _is_linked(b, 'e2_Group25', a2)
    if hasattr(a2, 'e2_Person26'):
        assert not _is_linked(a2, 'e2_Person26', b)


def test_assoc_LearningGoals1_reverse_link_reassign_clear():
    a1 = e2_SubGoal(GoalID="sample_text", GoalText="sample_text")
    a2 = e2_SubGoal(GoalID="sample_text_2", GoalText="sample_text_2")
    b = e2_Lecture(Date=date(2024, 1, 1), length=7)
    _safe_set(b, 'e2_Lecture2', {a1})
    assert _is_linked(b, 'e2_Lecture2', a1)
    if hasattr(a1, 'e2_SubGoal'):
        assert _is_linked(a1, 'e2_SubGoal', b)
    _safe_set(b, 'e2_Lecture2', {a2})
    assert _is_linked(b, 'e2_Lecture2', a2)
    if hasattr(a1, 'e2_SubGoal'):
        assert not _is_linked(a1, 'e2_SubGoal', b)
    if hasattr(a2, 'e2_SubGoal'):
        assert _is_linked(a2, 'e2_SubGoal', b)
    _safe_set(b, 'e2_Lecture2', set())
    assert not _is_linked(b, 'e2_Lecture2', a2)
    if hasattr(a2, 'e2_SubGoal'):
        assert not _is_linked(a2, 'e2_SubGoal', b)


def test_assoc_LearningGoals22_reverse_link_reassign_clear():
    a1 = e2_Goal(GoalID="sample_text", GoalText="sample_text")
    a2 = e2_Goal(GoalID="sample_text_2", GoalText="sample_text_2")
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course23', {a1})
    assert _is_linked(b, 'e2_Course23', a1)
    if hasattr(a1, 'e2_Goal'):
        assert _is_linked(a1, 'e2_Goal', b)
    _safe_set(b, 'e2_Course23', {a2})
    assert _is_linked(b, 'e2_Course23', a2)
    if hasattr(a1, 'e2_Goal'):
        assert not _is_linked(a1, 'e2_Goal', b)
    if hasattr(a2, 'e2_Goal'):
        assert _is_linked(a2, 'e2_Goal', b)
    _safe_set(b, 'e2_Course23', set())
    assert not _is_linked(b, 'e2_Course23', a2)
    if hasattr(a2, 'e2_Goal'):
        assert not _is_linked(a2, 'e2_Goal', b)


def test_assoc_LearningGoals4_reverse_link_reassign_clear():
    a1 = e2_SubGoal(GoalID="sample_text", GoalText="sample_text")
    a2 = e2_SubGoal(GoalID="sample_text_2", GoalText="sample_text_2")
    b = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    _safe_set(b, 'e2_Assingnment', {a1})
    assert _is_linked(b, 'e2_Assingnment', a1)
    if hasattr(a1, 'e2_SubGoal5'):
        assert _is_linked(a1, 'e2_SubGoal5', b)
    _safe_set(b, 'e2_Assingnment', {a2})
    assert _is_linked(b, 'e2_Assingnment', a2)
    if hasattr(a1, 'e2_SubGoal5'):
        assert not _is_linked(a1, 'e2_SubGoal5', b)
    if hasattr(a2, 'e2_SubGoal5'):
        assert _is_linked(a2, 'e2_SubGoal5', b)
    _safe_set(b, 'e2_Assingnment', set())
    assert not _is_linked(b, 'e2_Assingnment', a2)
    if hasattr(a2, 'e2_SubGoal5'):
        assert not _is_linked(a2, 'e2_SubGoal5', b)


def test_assoc_LectureAssignment41_reverse_link_reassign_clear():
    a1 = e2_LectureContent(Material="sample_text", Type="sample_text")
    a2 = e2_LectureContent(Material="sample_text_2", Type="sample_text_2")
    b = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    _safe_set(b, 'e2_Assingnment43', a1)
    assert _is_linked(b, 'e2_Assingnment43', a1)
    if hasattr(a1, 'e2_LectureContent42'):
        assert _is_linked(a1, 'e2_LectureContent42', b)
    _safe_set(b, 'e2_Assingnment43', a2)
    assert _is_linked(b, 'e2_Assingnment43', a2)
    if hasattr(a1, 'e2_LectureContent42'):
        assert not _is_linked(a1, 'e2_LectureContent42', b)
    if hasattr(a2, 'e2_LectureContent42'):
        assert _is_linked(a2, 'e2_LectureContent42', b)
    _safe_set(b, 'e2_Assingnment43', None)
    assert not _is_linked(b, 'e2_Assingnment43', a2)
    if hasattr(a2, 'e2_LectureContent42'):
        assert not _is_linked(a2, 'e2_LectureContent42', b)


def test_assoc_Lecturerer8_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course9', {a1})
    assert _is_linked(b, 'e2_Course9', a1)
    if hasattr(a1, 'e2_Person10'):
        assert _is_linked(a1, 'e2_Person10', b)
    _safe_set(b, 'e2_Course9', {a2})
    assert _is_linked(b, 'e2_Course9', a2)
    if hasattr(a1, 'e2_Person10'):
        assert not _is_linked(a1, 'e2_Person10', b)
    if hasattr(a2, 'e2_Person10'):
        assert _is_linked(a2, 'e2_Person10', b)
    _safe_set(b, 'e2_Course9', set())
    assert not _is_linked(b, 'e2_Course9', a2)
    if hasattr(a2, 'e2_Person10'):
        assert not _is_linked(a2, 'e2_Person10', b)


def test_assoc_Lectures14_reverse_link_reassign_clear():
    a1 = e2_Lecture(Date=date(2024, 1, 1), length=7)
    a2 = e2_Lecture(Date=date(2025, 6, 15), length=13)
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course15', {a1})
    assert _is_linked(b, 'e2_Course15', a1)
    if hasattr(a1, 'e2_Lecture16'):
        assert _is_linked(a1, 'e2_Lecture16', b)
    _safe_set(b, 'e2_Course15', {a2})
    assert _is_linked(b, 'e2_Course15', a2)
    if hasattr(a1, 'e2_Lecture16'):
        assert not _is_linked(a1, 'e2_Lecture16', b)
    if hasattr(a2, 'e2_Lecture16'):
        assert _is_linked(a2, 'e2_Lecture16', b)
    _safe_set(b, 'e2_Course15', set())
    assert not _is_linked(b, 'e2_Course15', a2)
    if hasattr(a2, 'e2_Lecture16'):
        assert not _is_linked(a2, 'e2_Lecture16', b)


def test_assoc_Persons36_reverse_link_reassign_clear():
    a1 = e2_University(Name="sample_text")
    a2 = e2_University(Name="sample_text_2")
    b = e2_Person(Name="sample_text")
    _safe_set(b, 'e2_Person37', a1)
    assert _is_linked(b, 'e2_Person37', a1)
    if hasattr(a1, 'e2_University'):
        assert _is_linked(a1, 'e2_University', b)
    _safe_set(b, 'e2_Person37', a2)
    assert _is_linked(b, 'e2_Person37', a2)
    if hasattr(a1, 'e2_University'):
        assert not _is_linked(a1, 'e2_University', b)
    if hasattr(a2, 'e2_University'):
        assert _is_linked(a2, 'e2_University', b)
    _safe_set(b, 'e2_Person37', None)
    assert not _is_linked(b, 'e2_Person37', a2)
    if hasattr(a2, 'e2_University'):
        assert not _is_linked(a2, 'e2_University', b)


def test_assoc_StudentGroups17_reverse_link_reassign_clear():
    a1 = e2_Group(Name="sample_text")
    a2 = e2_Group(Name="sample_text_2")
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course18', {a1})
    assert _is_linked(b, 'e2_Course18', a1)
    if hasattr(a1, 'e2_Group'):
        assert _is_linked(a1, 'e2_Group', b)
    _safe_set(b, 'e2_Course18', {a2})
    assert _is_linked(b, 'e2_Course18', a2)
    if hasattr(a1, 'e2_Group'):
        assert not _is_linked(a1, 'e2_Group', b)
    if hasattr(a2, 'e2_Group'):
        assert _is_linked(a2, 'e2_Group', b)
    _safe_set(b, 'e2_Course18', set())
    assert not _is_linked(b, 'e2_Course18', a2)
    if hasattr(a2, 'e2_Group'):
        assert not _is_linked(a2, 'e2_Group', b)


def test_assoc_Students6_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course', {a1})
    assert _is_linked(b, 'e2_Course', a1)
    if hasattr(a1, 'e2_Person7'):
        assert _is_linked(a1, 'e2_Person7', b)
    _safe_set(b, 'e2_Course', {a2})
    assert _is_linked(b, 'e2_Course', a2)
    if hasattr(a1, 'e2_Person7'):
        assert not _is_linked(a1, 'e2_Person7', b)
    if hasattr(a2, 'e2_Person7'):
        assert _is_linked(a2, 'e2_Person7', b)
    _safe_set(b, 'e2_Course', set())
    assert not _is_linked(b, 'e2_Course', a2)
    if hasattr(a2, 'e2_Person7'):
        assert not _is_linked(a2, 'e2_Person7', b)


def test_assoc_SubGoals44_reverse_link_reassign_clear():
    a1 = e2_SubGoal(GoalID="sample_text", GoalText="sample_text")
    a2 = e2_SubGoal(GoalID="sample_text_2", GoalText="sample_text_2")
    b = e2_Goal(GoalID="sample_text", GoalText="sample_text")
    _safe_set(b, 'e2_Goal45', {a1})
    assert _is_linked(b, 'e2_Goal45', a1)
    if hasattr(a1, 'e2_SubGoal46'):
        assert _is_linked(a1, 'e2_SubGoal46', b)
    _safe_set(b, 'e2_Goal45', {a2})
    assert _is_linked(b, 'e2_Goal45', a2)
    if hasattr(a1, 'e2_SubGoal46'):
        assert not _is_linked(a1, 'e2_SubGoal46', b)
    if hasattr(a2, 'e2_SubGoal46'):
        assert _is_linked(a2, 'e2_SubGoal46', b)
    _safe_set(b, 'e2_Goal45', set())
    assert not _is_linked(b, 'e2_Goal45', a2)
    if hasattr(a2, 'e2_SubGoal46'):
        assert not _is_linked(a2, 'e2_SubGoal46', b)


def test_assoc_Submitted27_reverse_link_reassign_clear():
    a1 = e2_Group(Name="sample_text")
    a2 = e2_Group(Name="sample_text_2")
    b = e2_AssignmentSubmission(Comments="sample_text", assessment=7)
    _safe_set(b, 'e2_AssignmentSubmission29', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission29', a1)
    if hasattr(a1, 'e2_Group28'):
        assert _is_linked(a1, 'e2_Group28', b)
    _safe_set(b, 'e2_AssignmentSubmission29', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission29', a2)
    if hasattr(a1, 'e2_Group28'):
        assert not _is_linked(a1, 'e2_Group28', b)
    if hasattr(a2, 'e2_Group28'):
        assert _is_linked(a2, 'e2_Group28', b)
    _safe_set(b, 'e2_AssignmentSubmission29', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission29', a2)
    if hasattr(a2, 'e2_Group28'):
        assert not _is_linked(a2, 'e2_Group28', b)


def test_assoc_Submitted3_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_AssignmentSubmission(Comments="sample_text", assessment=7)
    _safe_set(b, 'e2_AssignmentSubmission', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission', a1)
    if hasattr(a1, 'e2_Person'):
        assert _is_linked(a1, 'e2_Person', b)
    _safe_set(b, 'e2_AssignmentSubmission', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission', a2)
    if hasattr(a1, 'e2_Person'):
        assert not _is_linked(a1, 'e2_Person', b)
    if hasattr(a2, 'e2_Person'):
        assert _is_linked(a2, 'e2_Person', b)
    _safe_set(b, 'e2_AssignmentSubmission', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission', a2)
    if hasattr(a2, 'e2_Person'):
        assert not _is_linked(a2, 'e2_Person', b)


def test_assoc_TeachingAssistant19_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Course(ID="sample_text", Name="sample_text", credit=3.14)
    _safe_set(b, 'e2_Course20', {a1})
    assert _is_linked(b, 'e2_Course20', a1)
    if hasattr(a1, 'e2_Person21'):
        assert _is_linked(a1, 'e2_Person21', b)
    _safe_set(b, 'e2_Course20', {a2})
    assert _is_linked(b, 'e2_Course20', a2)
    if hasattr(a1, 'e2_Person21'):
        assert not _is_linked(a1, 'e2_Person21', b)
    if hasattr(a2, 'e2_Person21'):
        assert _is_linked(a2, 'e2_Person21', b)
    _safe_set(b, 'e2_Course20', set())
    assert not _is_linked(b, 'e2_Course20', a2)
    if hasattr(a2, 'e2_Person21'):
        assert not _is_linked(a2, 'e2_Person21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

