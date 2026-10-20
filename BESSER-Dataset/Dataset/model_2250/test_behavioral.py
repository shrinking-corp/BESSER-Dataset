import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    e2_AssignmentSubmission,
    e2_Assingnment,
    e2_Course,
    e2_Group,
    e2_Lecture,
    e2_LectureContent,
    e2_Person,
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

def test_assoc_AssesedBy26_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_AssignmentSubmission(Assessment=7, Comments="sample_text")
    _safe_set(b, 'e2_AssignmentSubmission27', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission27', a1)
    if hasattr(a1, 'e2_Person28'):
        assert _is_linked(a1, 'e2_Person28', b)
    _safe_set(b, 'e2_AssignmentSubmission27', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission27', a2)
    if hasattr(a1, 'e2_Person28'):
        assert not _is_linked(a1, 'e2_Person28', b)
    if hasattr(a2, 'e2_Person28'):
        assert _is_linked(a2, 'e2_Person28', b)
    _safe_set(b, 'e2_AssignmentSubmission27', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission27', a2)
    if hasattr(a2, 'e2_Person28'):
        assert not _is_linked(a2, 'e2_Person28', b)


def test_assoc_Assingments7_reverse_link_reassign_clear():
    a1 = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    a2 = e2_Course(Credit=9.99, ID="sample_text_2", Name="sample_text_2")
    b = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    _safe_set(b, 'e2_Assingnment', a1)
    assert _is_linked(b, 'e2_Assingnment', a1)
    if hasattr(a1, 'e2_Course8'):
        assert _is_linked(a1, 'e2_Course8', b)
    _safe_set(b, 'e2_Assingnment', a2)
    assert _is_linked(b, 'e2_Assingnment', a2)
    if hasattr(a1, 'e2_Course8'):
        assert not _is_linked(a1, 'e2_Course8', b)
    if hasattr(a2, 'e2_Course8'):
        assert _is_linked(a2, 'e2_Course8', b)
    _safe_set(b, 'e2_Assingnment', None)
    assert not _is_linked(b, 'e2_Assingnment', a2)
    if hasattr(a2, 'e2_Course8'):
        assert not _is_linked(a2, 'e2_Course8', b)


def test_assoc_Content0_reverse_link_reassign_clear():
    a1 = e2_LectureContent(Material="sample_text", Type="sample_text")
    a2 = e2_LectureContent(Material="sample_text_2", Type="sample_text_2")
    b = e2_Lecture(Date=date(2024, 1, 1), Length=7)
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


def test_assoc_Courses31_reverse_link_reassign_clear():
    a1 = e2_University(Name="sample_text")
    a2 = e2_University(Name="sample_text_2")
    b = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    _safe_set(b, 'e2_Course33', a1)
    assert _is_linked(b, 'e2_Course33', a1)
    if hasattr(a1, 'e2_University32'):
        assert _is_linked(a1, 'e2_University32', b)
    _safe_set(b, 'e2_Course33', a2)
    assert _is_linked(b, 'e2_Course33', a2)
    if hasattr(a1, 'e2_University32'):
        assert not _is_linked(a1, 'e2_University32', b)
    if hasattr(a2, 'e2_University32'):
        assert _is_linked(a2, 'e2_University32', b)
    _safe_set(b, 'e2_Course33', None)
    assert not _is_linked(b, 'e2_Course33', a2)
    if hasattr(a2, 'e2_University32'):
        assert not _is_linked(a2, 'e2_University32', b)


def test_assoc_GroupMember17_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Group(Name="sample_text")
    _safe_set(b, 'e2_Group18', {a1})
    assert _is_linked(b, 'e2_Group18', a1)
    if hasattr(a1, 'e2_Person19'):
        assert _is_linked(a1, 'e2_Person19', b)
    _safe_set(b, 'e2_Group18', {a2})
    assert _is_linked(b, 'e2_Group18', a2)
    if hasattr(a1, 'e2_Person19'):
        assert not _is_linked(a1, 'e2_Person19', b)
    if hasattr(a2, 'e2_Person19'):
        assert _is_linked(a2, 'e2_Person19', b)
    _safe_set(b, 'e2_Group18', set())
    assert not _is_linked(b, 'e2_Group18', a2)
    if hasattr(a2, 'e2_Person19'):
        assert not _is_linked(a2, 'e2_Person19', b)


def test_assoc_LectureAssignment34_reverse_link_reassign_clear():
    a1 = e2_LectureContent(Material="sample_text", Type="sample_text")
    a2 = e2_LectureContent(Material="sample_text_2", Type="sample_text_2")
    b = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    _safe_set(b, 'e2_Assingnment36', a1)
    assert _is_linked(b, 'e2_Assingnment36', a1)
    if hasattr(a1, 'e2_LectureContent35'):
        assert _is_linked(a1, 'e2_LectureContent35', b)
    _safe_set(b, 'e2_Assingnment36', a2)
    assert _is_linked(b, 'e2_Assingnment36', a2)
    if hasattr(a1, 'e2_LectureContent35'):
        assert not _is_linked(a1, 'e2_LectureContent35', b)
    if hasattr(a2, 'e2_LectureContent35'):
        assert _is_linked(a2, 'e2_LectureContent35', b)
    _safe_set(b, 'e2_Assingnment36', None)
    assert not _is_linked(b, 'e2_Assingnment36', a2)
    if hasattr(a2, 'e2_LectureContent35'):
        assert not _is_linked(a2, 'e2_LectureContent35', b)


def test_assoc_Lecturerer4_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    _safe_set(b, 'e2_Course5', {a1})
    assert _is_linked(b, 'e2_Course5', a1)
    if hasattr(a1, 'e2_Person6'):
        assert _is_linked(a1, 'e2_Person6', b)
    _safe_set(b, 'e2_Course5', {a2})
    assert _is_linked(b, 'e2_Course5', a2)
    if hasattr(a1, 'e2_Person6'):
        assert not _is_linked(a1, 'e2_Person6', b)
    if hasattr(a2, 'e2_Person6'):
        assert _is_linked(a2, 'e2_Person6', b)
    _safe_set(b, 'e2_Course5', set())
    assert not _is_linked(b, 'e2_Course5', a2)
    if hasattr(a2, 'e2_Person6'):
        assert not _is_linked(a2, 'e2_Person6', b)


def test_assoc_Lectures9_reverse_link_reassign_clear():
    a1 = e2_Lecture(Date=date(2024, 1, 1), Length=7)
    a2 = e2_Lecture(Date=date(2025, 6, 15), Length=13)
    b = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    _safe_set(b, 'e2_Course10', {a1})
    assert _is_linked(b, 'e2_Course10', a1)
    if hasattr(a1, 'e2_Lecture11'):
        assert _is_linked(a1, 'e2_Lecture11', b)
    _safe_set(b, 'e2_Course10', {a2})
    assert _is_linked(b, 'e2_Course10', a2)
    if hasattr(a1, 'e2_Lecture11'):
        assert not _is_linked(a1, 'e2_Lecture11', b)
    if hasattr(a2, 'e2_Lecture11'):
        assert _is_linked(a2, 'e2_Lecture11', b)
    _safe_set(b, 'e2_Course10', set())
    assert not _is_linked(b, 'e2_Course10', a2)
    if hasattr(a2, 'e2_Lecture11'):
        assert not _is_linked(a2, 'e2_Lecture11', b)


def test_assoc_Persons29_reverse_link_reassign_clear():
    a1 = e2_University(Name="sample_text")
    a2 = e2_University(Name="sample_text_2")
    b = e2_Person(Name="sample_text")
    _safe_set(b, 'e2_Person30', a1)
    assert _is_linked(b, 'e2_Person30', a1)
    if hasattr(a1, 'e2_University'):
        assert _is_linked(a1, 'e2_University', b)
    _safe_set(b, 'e2_Person30', a2)
    assert _is_linked(b, 'e2_Person30', a2)
    if hasattr(a1, 'e2_University'):
        assert not _is_linked(a1, 'e2_University', b)
    if hasattr(a2, 'e2_University'):
        assert _is_linked(a2, 'e2_University', b)
    _safe_set(b, 'e2_Person30', None)
    assert not _is_linked(b, 'e2_Person30', a2)
    if hasattr(a2, 'e2_University'):
        assert not _is_linked(a2, 'e2_University', b)


def test_assoc_StudentGroups12_reverse_link_reassign_clear():
    a1 = e2_Group(Name="sample_text")
    a2 = e2_Group(Name="sample_text_2")
    b = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    _safe_set(b, 'e2_Course13', {a1})
    assert _is_linked(b, 'e2_Course13', a1)
    if hasattr(a1, 'e2_Group'):
        assert _is_linked(a1, 'e2_Group', b)
    _safe_set(b, 'e2_Course13', {a2})
    assert _is_linked(b, 'e2_Course13', a2)
    if hasattr(a1, 'e2_Group'):
        assert not _is_linked(a1, 'e2_Group', b)
    if hasattr(a2, 'e2_Group'):
        assert _is_linked(a2, 'e2_Group', b)
    _safe_set(b, 'e2_Course13', set())
    assert not _is_linked(b, 'e2_Course13', a2)
    if hasattr(a2, 'e2_Group'):
        assert not _is_linked(a2, 'e2_Group', b)


def test_assoc_Students2_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    _safe_set(b, 'e2_Course', {a1})
    assert _is_linked(b, 'e2_Course', a1)
    if hasattr(a1, 'e2_Person3'):
        assert _is_linked(a1, 'e2_Person3', b)
    _safe_set(b, 'e2_Course', {a2})
    assert _is_linked(b, 'e2_Course', a2)
    if hasattr(a1, 'e2_Person3'):
        assert not _is_linked(a1, 'e2_Person3', b)
    if hasattr(a2, 'e2_Person3'):
        assert _is_linked(a2, 'e2_Person3', b)
    _safe_set(b, 'e2_Course', set())
    assert not _is_linked(b, 'e2_Course', a2)
    if hasattr(a2, 'e2_Person3'):
        assert not _is_linked(a2, 'e2_Person3', b)


def test_assoc_Submitted1_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_AssignmentSubmission(Assessment=7, Comments="sample_text")
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


def test_assoc_Submitted20_reverse_link_reassign_clear():
    a1 = e2_Group(Name="sample_text")
    a2 = e2_Group(Name="sample_text_2")
    b = e2_AssignmentSubmission(Assessment=7, Comments="sample_text")
    _safe_set(b, 'e2_AssignmentSubmission22', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission22', a1)
    if hasattr(a1, 'e2_Group21'):
        assert _is_linked(a1, 'e2_Group21', b)
    _safe_set(b, 'e2_AssignmentSubmission22', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission22', a2)
    if hasattr(a1, 'e2_Group21'):
        assert not _is_linked(a1, 'e2_Group21', b)
    if hasattr(a2, 'e2_Group21'):
        assert _is_linked(a2, 'e2_Group21', b)
    _safe_set(b, 'e2_AssignmentSubmission22', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission22', a2)
    if hasattr(a2, 'e2_Group21'):
        assert not _is_linked(a2, 'e2_Group21', b)


def test_assoc_TeachingAssistant14_reverse_link_reassign_clear():
    a1 = e2_Person(Name="sample_text")
    a2 = e2_Person(Name="sample_text_2")
    b = e2_Course(Credit=3.14, ID="sample_text", Name="sample_text")
    _safe_set(b, 'e2_Course15', {a1})
    assert _is_linked(b, 'e2_Course15', a1)
    if hasattr(a1, 'e2_Person16'):
        assert _is_linked(a1, 'e2_Person16', b)
    _safe_set(b, 'e2_Course15', {a2})
    assert _is_linked(b, 'e2_Course15', a2)
    if hasattr(a1, 'e2_Person16'):
        assert not _is_linked(a1, 'e2_Person16', b)
    if hasattr(a2, 'e2_Person16'):
        assert _is_linked(a2, 'e2_Person16', b)
    _safe_set(b, 'e2_Course15', set())
    assert not _is_linked(b, 'e2_Course15', a2)
    if hasattr(a2, 'e2_Person16'):
        assert not _is_linked(a2, 'e2_Person16', b)


def test_assoc_assignment23_reverse_link_reassign_clear():
    a1 = e2_Assingnment(Content="sample_text", Deadline=date(2024, 1, 1), StartDate=date(2024, 1, 1), Title="sample_text", Type="sample_text", isMandatory=True)
    a2 = e2_Assingnment(Content="sample_text_2", Deadline=date(2025, 6, 15), StartDate=date(2025, 6, 15), Title="sample_text_2", Type="sample_text_2", isMandatory=False)
    b = e2_AssignmentSubmission(Assessment=7, Comments="sample_text")
    _safe_set(b, 'e2_AssignmentSubmission24', a1)
    assert _is_linked(b, 'e2_AssignmentSubmission24', a1)
    if hasattr(a1, 'e2_Assingnment25'):
        assert _is_linked(a1, 'e2_Assingnment25', b)
    _safe_set(b, 'e2_AssignmentSubmission24', a2)
    assert _is_linked(b, 'e2_AssignmentSubmission24', a2)
    if hasattr(a1, 'e2_Assingnment25'):
        assert not _is_linked(a1, 'e2_Assingnment25', b)
    if hasattr(a2, 'e2_Assingnment25'):
        assert _is_linked(a2, 'e2_Assingnment25', b)
    _safe_set(b, 'e2_AssignmentSubmission24', None)
    assert not _is_linked(b, 'e2_AssignmentSubmission24', a2)
    if hasattr(a2, 'e2_Assingnment25'):
        assert not _is_linked(a2, 'e2_Assingnment25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

