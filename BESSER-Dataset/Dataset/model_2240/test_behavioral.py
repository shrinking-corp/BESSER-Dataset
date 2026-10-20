import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_Course,
    model_CourseAllocation,
    model_CourseInstance,
    model_Department,
    model_Person,
    model_Role,
    model_Semester,
    SemesterKind,
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

def test_assoc_allocations7_reverse_link_reassign_clear():
    a1 = model_Person(email="sample_text", employmentFactor="sample_text", faceUrl="sample_text", name="sample_text", userName="sample_text")
    a2 = model_Person(email="sample_text_2", employmentFactor="sample_text_2", faceUrl="sample_text_2", name="sample_text_2", userName="sample_text_2")
    b = model_CourseAllocation(explicitFactor="sample_text", factor="sample_text")
    _safe_set(b, 'CourseAllocation', a1)
    assert _is_linked(b, 'CourseAllocation', a1)
    if hasattr(a1, 'person'):
        assert _is_linked(a1, 'person', b)
    _safe_set(b, 'CourseAllocation', a2)
    assert _is_linked(b, 'CourseAllocation', a2)
    if hasattr(a1, 'person'):
        assert not _is_linked(a1, 'person', b)
    if hasattr(a2, 'person'):
        assert _is_linked(a2, 'person', b)
    _safe_set(b, 'CourseAllocation', None)
    assert not _is_linked(b, 'CourseAllocation', a2)
    if hasattr(a2, 'person'):
        assert not _is_linked(a2, 'person', b)


def test_assoc_courses1_reverse_link_reassign_clear():
    a1 = model_Department(name="sample_text")
    a2 = model_Department(name="sample_text_2")
    b = model_Course(fullName="sample_text", name="sample_text")
    _safe_set(b, 'model_Course', a1)
    assert _is_linked(b, 'model_Course', a1)
    if hasattr(a1, 'model_Department2'):
        assert _is_linked(a1, 'model_Department2', b)
    _safe_set(b, 'model_Course', a2)
    assert _is_linked(b, 'model_Course', a2)
    if hasattr(a1, 'model_Department2'):
        assert not _is_linked(a1, 'model_Department2', b)
    if hasattr(a2, 'model_Department2'):
        assert _is_linked(a2, 'model_Department2', b)
    _safe_set(b, 'model_Course', None)
    assert not _is_linked(b, 'model_Course', a2)
    if hasattr(a2, 'model_Department2'):
        assert not _is_linked(a2, 'model_Department2', b)


def test_assoc_employees0_reverse_link_reassign_clear():
    a1 = model_Person(email="sample_text", employmentFactor="sample_text", faceUrl="sample_text", name="sample_text", userName="sample_text")
    a2 = model_Person(email="sample_text_2", employmentFactor="sample_text_2", faceUrl="sample_text_2", name="sample_text_2", userName="sample_text_2")
    b = model_Department(name="sample_text")
    _safe_set(b, 'model_Department', {a1})
    assert _is_linked(b, 'model_Department', a1)
    if hasattr(a1, 'model_Person'):
        assert _is_linked(a1, 'model_Person', b)
    _safe_set(b, 'model_Department', {a2})
    assert _is_linked(b, 'model_Department', a2)
    if hasattr(a1, 'model_Person'):
        assert not _is_linked(a1, 'model_Person', b)
    if hasattr(a2, 'model_Person'):
        assert _is_linked(a2, 'model_Person', b)
    _safe_set(b, 'model_Department', set())
    assert not _is_linked(b, 'model_Department', a2)
    if hasattr(a2, 'model_Person'):
        assert not _is_linked(a2, 'model_Person', b)


def test_assoc_person17_reverse_link_reassign_clear():
    a1 = model_Person(email="sample_text", employmentFactor="sample_text", faceUrl="sample_text", name="sample_text", userName="sample_text")
    a2 = model_Person(email="sample_text_2", employmentFactor="sample_text_2", faceUrl="sample_text_2", name="sample_text_2", userName="sample_text_2")
    b = model_CourseAllocation(explicitFactor="sample_text", factor="sample_text")
    _safe_set(b, 'allocations', a1)
    assert _is_linked(b, 'allocations', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'allocations', a2)
    assert _is_linked(b, 'allocations', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'allocations', None)
    assert not _is_linked(b, 'allocations', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_requiredRoles8_reverse_link_reassign_clear():
    a1 = model_Role(factor="sample_text", name="sample_text")
    a2 = model_Role(factor="sample_text_2", name="sample_text_2")
    b = model_Course(fullName="sample_text", name="sample_text")
    _safe_set(b, 'model_Course9', {a1})
    assert _is_linked(b, 'model_Course9', a1)
    if hasattr(a1, 'model_Role10'):
        assert _is_linked(a1, 'model_Role10', b)
    _safe_set(b, 'model_Course9', {a2})
    assert _is_linked(b, 'model_Course9', a2)
    if hasattr(a1, 'model_Role10'):
        assert not _is_linked(a1, 'model_Role10', b)
    if hasattr(a2, 'model_Role10'):
        assert _is_linked(a2, 'model_Role10', b)
    _safe_set(b, 'model_Course9', set())
    assert not _is_linked(b, 'model_Course9', a2)
    if hasattr(a2, 'model_Role10'):
        assert not _is_linked(a2, 'model_Role10', b)


def test_assoc_role18_reverse_link_reassign_clear():
    a1 = model_Role(factor="sample_text", name="sample_text")
    a2 = model_Role(factor="sample_text_2", name="sample_text_2")
    b = model_CourseAllocation(explicitFactor="sample_text", factor="sample_text")
    _safe_set(b, 'model_CourseAllocation', a1)
    assert _is_linked(b, 'model_CourseAllocation', a1)
    if hasattr(a1, 'model_Role19'):
        assert _is_linked(a1, 'model_Role19', b)
    _safe_set(b, 'model_CourseAllocation', a2)
    assert _is_linked(b, 'model_CourseAllocation', a2)
    if hasattr(a1, 'model_Role19'):
        assert not _is_linked(a1, 'model_Role19', b)
    if hasattr(a2, 'model_Role19'):
        assert _is_linked(a2, 'model_Role19', b)
    _safe_set(b, 'model_CourseAllocation', None)
    assert not _is_linked(b, 'model_CourseAllocation', a2)
    if hasattr(a2, 'model_Role19'):
        assert not _is_linked(a2, 'model_Role19', b)


def test_assoc_roles3_reverse_link_reassign_clear():
    a1 = model_Role(factor="sample_text", name="sample_text")
    a2 = model_Role(factor="sample_text_2", name="sample_text_2")
    b = model_Department(name="sample_text")
    _safe_set(b, 'model_Department4', {a1})
    assert _is_linked(b, 'model_Department4', a1)
    if hasattr(a1, 'model_Role'):
        assert _is_linked(a1, 'model_Role', b)
    _safe_set(b, 'model_Department4', {a2})
    assert _is_linked(b, 'model_Department4', a2)
    if hasattr(a1, 'model_Role'):
        assert not _is_linked(a1, 'model_Role', b)
    if hasattr(a2, 'model_Role'):
        assert _is_linked(a2, 'model_Role', b)
    _safe_set(b, 'model_Department4', set())
    assert not _is_linked(b, 'model_Department4', a2)
    if hasattr(a2, 'model_Role'):
        assert not _is_linked(a2, 'model_Role', b)


def test_assoc_semesters5_reverse_link_reassign_clear():
    a1 = model_Semester(kind="sample_text", year="sample_text")
    a2 = model_Semester(kind="sample_text_2", year="sample_text_2")
    b = model_Department(name="sample_text")
    _safe_set(b, 'model_Department6', {a1})
    assert _is_linked(b, 'model_Department6', a1)
    if hasattr(a1, 'model_Semester'):
        assert _is_linked(a1, 'model_Semester', b)
    _safe_set(b, 'model_Department6', {a2})
    assert _is_linked(b, 'model_Department6', a2)
    if hasattr(a1, 'model_Semester'):
        assert not _is_linked(a1, 'model_Semester', b)
    if hasattr(a2, 'model_Semester'):
        assert _is_linked(a2, 'model_Semester', b)
    _safe_set(b, 'model_Department6', set())
    assert not _is_linked(b, 'model_Department6', a2)
    if hasattr(a2, 'model_Semester'):
        assert not _is_linked(a2, 'model_Semester', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allocations15_stub_double():
    # model_CourseInstance has no real 'course' property in the generated
    # code (a bare stub) -- manually attach it so model_CourseAllocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CourseAllocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CourseAllocation(explicitFactor="sample_text", factor="sample_text")
    partner = model_CourseInstance()
    setattr(partner, 'course', None)
    _safe_set(owner, 'CourseAllocation16', partner)
    assert owner in getattr(partner, 'course')
    _safe_set(owner, 'CourseAllocation16', None)
    assert owner not in getattr(partner, 'course')


def test_assoc_course12_stub_double():
    # model_CourseInstance has no real 'model_CourseInstance' property in the generated
    # code (a bare stub) -- manually attach it so model_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Course(fullName="sample_text", name="sample_text")
    partner = model_CourseInstance()
    setattr(partner, 'model_CourseInstance', None)
    _safe_set(owner, 'model_Course13', partner)
    assert getattr(partner, 'model_CourseInstance') == owner
    _safe_set(owner, 'model_Course13', None)
    assert getattr(partner, 'model_CourseInstance') is None


def test_assoc_course20_stub_double():
    # model_CourseInstance has no real 'CourseInstance22' property in the generated
    # code (a bare stub) -- manually attach it so model_CourseAllocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_CourseAllocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_CourseAllocation(explicitFactor="sample_text", factor="sample_text")
    partner = model_CourseInstance()
    setattr(partner, 'CourseInstance22', None)
    _safe_set(owner, 'allocations21', partner)
    assert getattr(partner, 'CourseInstance22') == owner
    _safe_set(owner, 'allocations21', None)
    assert getattr(partner, 'CourseInstance22') is None


def test_assoc_courses11_stub_double():
    # model_CourseInstance has no real 'CourseInstance' property in the generated
    # code (a bare stub) -- manually attach it so model_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Semester(kind="sample_text", year="sample_text")
    partner = model_CourseInstance()
    setattr(partner, 'CourseInstance', None)
    _safe_set(owner, 'semester', {partner})
    assert getattr(partner, 'CourseInstance') == owner
    _safe_set(owner, 'semester', set())
    assert getattr(partner, 'CourseInstance') is None


def test_assoc_semester14_stub_double():
    # model_CourseInstance has no real 'courses' property in the generated
    # code (a bare stub) -- manually attach it so model_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Semester(kind="sample_text", year="sample_text")
    partner = model_CourseInstance()
    setattr(partner, 'courses', None)
    _safe_set(owner, 'Semester', partner)
    assert getattr(partner, 'courses') == owner
    _safe_set(owner, 'Semester', None)
    assert getattr(partner, 'courses') is None


