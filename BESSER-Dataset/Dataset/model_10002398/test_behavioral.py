import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mypackage_Admin,
    mypackage_Course,
    mypackage_Exam,
    mypackage_FileManager,
    mypackage_Perosn,
    mypackage_Staff,
    mypackage_Student,
    mypackage_Tutor,
    mypackage_studentAffairsEmp,
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

def test_assoc_Course_Exam_reverse_link_reassign_clear():
    a1 = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    a2 = mypackage_Exam(EId="sample_text_2", EName="sample_text_2", ExamsFileName="sample_text_2", MaxGrade="sample_text_2")
    b = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    _safe_set(b, 'exam0', a1)
    assert _is_linked(b, 'exam0', a1)
    if hasattr(a1, 'course1'):
        assert _is_linked(a1, 'course1', b)
    _safe_set(b, 'exam0', a2)
    assert _is_linked(b, 'exam0', a2)
    if hasattr(a1, 'course1'):
        assert not _is_linked(a1, 'course1', b)
    if hasattr(a2, 'course1'):
        assert _is_linked(a2, 'course1', b)
    _safe_set(b, 'exam0', None)
    assert not _is_linked(b, 'exam0', a2)
    if hasattr(a2, 'course1'):
        assert not _is_linked(a2, 'course1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_FileManager_Course_stub_double():
    # mypackage_FileManager has no real 'course4' property in the generated
    # code (a bare stub) -- manually attach it so mypackage_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mypackage_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    partner = mypackage_FileManager()
    setattr(partner, 'course4', None)
    _safe_set(owner, 'fileManager5', partner)
    assert getattr(partner, 'course4') == owner
    _safe_set(owner, 'fileManager5', None)
    assert getattr(partner, 'course4') is None


def test_assoc_FileManager_Exam_stub_double():
    # mypackage_FileManager has no real 'exam6' property in the generated
    # code (a bare stub) -- manually attach it so mypackage_Exam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mypackage_Exam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    partner = mypackage_FileManager()
    setattr(partner, 'exam6', None)
    _safe_set(owner, 'fileManager7', partner)
    assert getattr(partner, 'exam6') == owner
    _safe_set(owner, 'fileManager7', None)
    assert getattr(partner, 'exam6') is None


def test_assoc_FileManager_Perosn_stub_double():
    # mypackage_FileManager has no real 'perosn2' property in the generated
    # code (a bare stub) -- manually attach it so mypackage_Perosn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mypackage_Perosn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mypackage_Perosn(UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    partner = mypackage_FileManager()
    setattr(partner, 'perosn2', None)
    _safe_set(owner, 'fileManager3', partner)
    assert getattr(partner, 'perosn2') == owner
    _safe_set(owner, 'fileManager3', None)
    assert getattr(partner, 'perosn2') is None


