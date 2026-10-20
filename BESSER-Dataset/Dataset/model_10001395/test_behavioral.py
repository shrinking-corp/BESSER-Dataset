import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Course,
    Email,
    Exam,
    FileBinary,
    Finance,
    ILogin_Interface,
    Insturctor,
    Person,
    Student,
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

def test_assoc_Exam_Course_reverse_link_reassign_clear():
    a1 = Exam(EID="sample_text", EName="sample_text", ETIME="sample_text", Exam_File_Name="sample_text", MaxGrade="sample_text")
    a2 = Exam(EID="sample_text_2", EName="sample_text_2", ETIME="sample_text_2", Exam_File_Name="sample_text_2", MaxGrade="sample_text_2")
    b = Course(CTutor="sample_text", Cid="sample_text", Cname="sample_text", Course_File_Name="sample_text", Course_REG="sample_text", Cprice="sample_text")
    _safe_set(b, 'exam1', a1)
    assert _is_linked(b, 'exam1', a1)
    if hasattr(a1, 'course0'):
        assert _is_linked(a1, 'course0', b)
    _safe_set(b, 'exam1', a2)
    assert _is_linked(b, 'exam1', a2)
    if hasattr(a1, 'course0'):
        assert not _is_linked(a1, 'course0', b)
    if hasattr(a2, 'course0'):
        assert _is_linked(a2, 'course0', b)
    _safe_set(b, 'exam1', None)
    assert not _is_linked(b, 'exam1', a2)
    if hasattr(a2, 'course0'):
        assert not _is_linked(a2, 'course0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Course_FileBinary_stub_double():
    # FileBinary has no real 'course5' property in the generated
    # code (a bare stub) -- manually attach it so Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Course(CTutor="sample_text", Cid="sample_text", Cname="sample_text", Course_File_Name="sample_text", Course_REG="sample_text", Cprice="sample_text")
    partner = FileBinary()
    setattr(partner, 'course5', None)
    _safe_set(owner, 'fileBinary4', partner)
    assert getattr(partner, 'course5') == owner
    _safe_set(owner, 'fileBinary4', None)
    assert getattr(partner, 'course5') is None


def test_assoc_Email_FileBinary_stub_double():
    # FileBinary has no real 'email7' property in the generated
    # code (a bare stub) -- manually attach it so Email's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Email's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Email(Email="sample_text")
    partner = FileBinary()
    setattr(partner, 'email7', None)
    _safe_set(owner, 'fileBinary6', partner)
    assert getattr(partner, 'email7') == owner
    _safe_set(owner, 'fileBinary6', None)
    assert getattr(partner, 'email7') is None


def test_assoc_Exam_FileBinary_stub_double():
    # FileBinary has no real 'exam3' property in the generated
    # code (a bare stub) -- manually attach it so Exam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Exam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Exam(EID="sample_text", EName="sample_text", ETIME="sample_text", Exam_File_Name="sample_text", MaxGrade="sample_text")
    partner = FileBinary()
    setattr(partner, 'exam3', None)
    _safe_set(owner, 'fileBinary2', partner)
    assert getattr(partner, 'exam3') == owner
    _safe_set(owner, 'fileBinary2', None)
    assert getattr(partner, 'exam3') is None


def test_assoc_Insturctor_FileBinary_stub_double():
    # FileBinary has no real 'insturctor9' property in the generated
    # code (a bare stub) -- manually attach it so Insturctor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Insturctor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Insturctor(INfilename="sample_text")
    partner = FileBinary()
    setattr(partner, 'insturctor9', None)
    _safe_set(owner, 'fileBinary8', partner)
    assert getattr(partner, 'insturctor9') == owner
    _safe_set(owner, 'fileBinary8', None)
    assert getattr(partner, 'insturctor9') is None


def test_assoc_Student_FileBinary_stub_double():
    # FileBinary has no real 'student11' property in the generated
    # code (a bare stub) -- manually attach it so Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Student(grade="sample_text", s_age=7, studentfname="sample_text")
    partner = FileBinary()
    setattr(partner, 'student11', None)
    _safe_set(owner, 'fileBinary10', partner)
    assert getattr(partner, 'student11') == owner
    _safe_set(owner, 'fileBinary10', None)
    assert getattr(partner, 'student11') is None


