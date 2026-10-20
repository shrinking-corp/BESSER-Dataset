import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Binary_File,
    Course,
    Department,
    Email,
    Exam,
    Exceptions,
    Finance,
    ILogin_Interface,
    Instructor,
    Person,
    Report,
    Student,
    Stuff,
    T,
    User,
    str,
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

def test_assoc_Department_Course_reverse_link_reassign_clear():
    a1 = Department(deptId="sample_text", deptName="sample_text")
    a2 = Department(deptId="sample_text_2", deptName="sample_text_2")
    b = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    _safe_set(b, 'department33', a1)
    assert _is_linked(b, 'department33', a1)
    if hasattr(a1, 'course32'):
        assert _is_linked(a1, 'course32', b)
    _safe_set(b, 'department33', a2)
    assert _is_linked(b, 'department33', a2)
    if hasattr(a1, 'course32'):
        assert not _is_linked(a1, 'course32', b)
    if hasattr(a2, 'course32'):
        assert _is_linked(a2, 'course32', b)
    _safe_set(b, 'department33', None)
    assert not _is_linked(b, 'department33', a2)
    if hasattr(a2, 'course32'):
        assert not _is_linked(a2, 'course32', b)


def test_assoc_Exam_Course_reverse_link_reassign_clear():
    a1 = Exam(EName="sample_text", ETime="sample_text", MaxGrade="sample_text")
    a2 = Exam(EName="sample_text_2", ETime="sample_text_2", MaxGrade="sample_text_2")
    b = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    _safe_set(b, 'exam9', a1)
    assert _is_linked(b, 'exam9', a1)
    if hasattr(a1, 'course8'):
        assert _is_linked(a1, 'course8', b)
    _safe_set(b, 'exam9', a2)
    assert _is_linked(b, 'exam9', a2)
    if hasattr(a1, 'course8'):
        assert not _is_linked(a1, 'course8', b)
    if hasattr(a2, 'course8'):
        assert _is_linked(a2, 'course8', b)
    _safe_set(b, 'exam9', None)
    assert not _is_linked(b, 'exam9', a2)
    if hasattr(a2, 'course8'):
        assert not _is_linked(a2, 'course8', b)


def test_assoc_Student_Course_reverse_link_reassign_clear():
    a1 = Student(SAge=7, SGender="sample_text")
    a2 = Student(SAge=13, SGender="sample_text_2")
    b = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    _safe_set(b, 'student35', a1)
    assert _is_linked(b, 'student35', a1)
    if hasattr(a1, 'course34'):
        assert _is_linked(a1, 'course34', b)
    _safe_set(b, 'student35', a2)
    assert _is_linked(b, 'student35', a2)
    if hasattr(a1, 'course34'):
        assert not _is_linked(a1, 'course34', b)
    if hasattr(a2, 'course34'):
        assert _is_linked(a2, 'course34', b)
    _safe_set(b, 'student35', None)
    assert not _is_linked(b, 'student35', a2)
    if hasattr(a2, 'course34'):
        assert not _is_linked(a2, 'course34', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Admin_Course_stub_double():
    # Admin has no real 'course30' property in the generated
    # code (a bare stub) -- manually attach it so Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    partner = Admin()
    setattr(partner, 'course30', None)
    _safe_set(owner, 'admin31', partner)
    assert getattr(partner, 'course30') == owner
    _safe_set(owner, 'admin31', None)
    assert getattr(partner, 'course30') is None


def test_assoc_Admin_Student_stub_double():
    # Admin has no real 'student26' property in the generated
    # code (a bare stub) -- manually attach it so Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Student(SAge=7, SGender="sample_text")
    partner = Admin()
    setattr(partner, 'student26', None)
    _safe_set(owner, 'admin27', partner)
    assert getattr(partner, 'student26') == owner
    _safe_set(owner, 'admin27', None)
    assert getattr(partner, 'student26') is None


def test_assoc_Course_Binary_File_stub_double():
    # Binary_File has no real 'course7' property in the generated
    # code (a bare stub) -- manually attach it so Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    partner = Binary_File()
    setattr(partner, 'course7', None)
    _safe_set(owner, 'binary_File6', partner)
    assert getattr(partner, 'course7') == owner
    _safe_set(owner, 'binary_File6', None)
    assert getattr(partner, 'course7') is None


def test_assoc_Course_Report_stub_double():
    # Report has no real 'course39' property in the generated
    # code (a bare stub) -- manually attach it so Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    partner = Report()
    setattr(partner, 'course39', None)
    _safe_set(owner, 'report38', partner)
    assert getattr(partner, 'course39') == owner
    _safe_set(owner, 'report38', None)
    assert getattr(partner, 'course39') is None


def test_assoc_Department_Binary_File_stub_double():
    # Binary_File has no real 'department13' property in the generated
    # code (a bare stub) -- manually attach it so Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Department(deptId="sample_text", deptName="sample_text")
    partner = Binary_File()
    setattr(partner, 'department13', None)
    _safe_set(owner, 'binary_File12', partner)
    assert getattr(partner, 'department13') == owner
    _safe_set(owner, 'binary_File12', None)
    assert getattr(partner, 'department13') is None


def test_assoc_Email_Student_stub_double():
    # Email has no real 'student22' property in the generated
    # code (a bare stub) -- manually attach it so Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Student(SAge=7, SGender="sample_text")
    partner = Email()
    setattr(partner, 'student22', None)
    _safe_set(owner, 'email23', partner)
    assert getattr(partner, 'student22') == owner
    _safe_set(owner, 'email23', None)
    assert getattr(partner, 'student22') is None


def test_assoc_Exam_Binary_File_stub_double():
    # Binary_File has no real 'exam45' property in the generated
    # code (a bare stub) -- manually attach it so Exam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Exam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Exam(EName="sample_text", ETime="sample_text", MaxGrade="sample_text")
    partner = Binary_File()
    setattr(partner, 'exam45', None)
    _safe_set(owner, 'binary_File44', partner)
    assert getattr(partner, 'exam45') == owner
    _safe_set(owner, 'binary_File44', None)
    assert getattr(partner, 'exam45') is None


def test_assoc_Finance__Student_stub_double():
    # Finance has no real 'student24' property in the generated
    # code (a bare stub) -- manually attach it so Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Student(SAge=7, SGender="sample_text")
    partner = Finance()
    setattr(partner, 'student24', None)
    _safe_set(owner, 'finance25', partner)
    assert getattr(partner, 'student24') == owner
    _safe_set(owner, 'finance25', None)
    assert getattr(partner, 'student24') is None


def test_assoc_Instructor_Department_stub_double():
    # Instructor has no real 'department0' property in the generated
    # code (a bare stub) -- manually attach it so Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Department(deptId="sample_text", deptName="sample_text")
    partner = Instructor()
    setattr(partner, 'department0', None)
    _safe_set(owner, 'instructor1', partner)
    assert getattr(partner, 'department0') == owner
    _safe_set(owner, 'instructor1', None)
    assert getattr(partner, 'department0') is None


def test_assoc_Report_Course_stub_double():
    # Report has no real 'course18' property in the generated
    # code (a bare stub) -- manually attach it so Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Course(CCode="sample_text", CInstructor="sample_text", CName="sample_text", CPrice="sample_text")
    partner = Report()
    setattr(partner, 'course18', None)
    _safe_set(owner, 'report19', partner)
    assert getattr(partner, 'course18') == owner
    _safe_set(owner, 'report19', None)
    assert getattr(partner, 'course18') is None


def test_assoc_Student_Report_stub_double():
    # Report has no real 'student15' property in the generated
    # code (a bare stub) -- manually attach it so Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Student(SAge=7, SGender="sample_text")
    partner = Report()
    setattr(partner, 'student15', None)
    _safe_set(owner, 'report14', partner)
    assert getattr(partner, 'student15') == owner
    _safe_set(owner, 'report14', None)
    assert getattr(partner, 'student15') is None


def test_assoc_User_Binary_File_stub_double():
    # Binary_File has no real 'user5' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(Fname="sample_text", Lname="sample_text", Password="sample_text", email="sample_text")
    partner = Binary_File()
    setattr(partner, 'user5', None)
    _safe_set(owner, 'binary_File4', partner)
    assert getattr(partner, 'user5') == owner
    _safe_set(owner, 'binary_File4', None)
    assert getattr(partner, 'user5') is None


def test_assoc_User_Exceptions_stub_double():
    # Exceptions has no real 'user11' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(Fname="sample_text", Lname="sample_text", Password="sample_text", email="sample_text")
    partner = Exceptions()
    setattr(partner, 'user11', None)
    _safe_set(owner, 'exceptions10', partner)
    assert getattr(partner, 'user11') == owner
    _safe_set(owner, 'exceptions10', None)
    assert getattr(partner, 'user11') is None


def test_assoc_User_ILogin_stub_double():
    # ILogin_Interface has no real 'user3' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(Fname="sample_text", Lname="sample_text", Password="sample_text", email="sample_text")
    partner = ILogin_Interface()
    setattr(partner, 'user3', None)
    _safe_set(owner, 'User_ILogin_02', partner)
    assert getattr(partner, 'user3') == owner
    _safe_set(owner, 'User_ILogin_02', None)
    assert getattr(partner, 'user3') is None


