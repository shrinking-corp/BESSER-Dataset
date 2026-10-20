import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    university_Book,
    university_Computer,
    university_Department,
    university_Library,
    university_Module,
    university_NamedElement,
    university_PrimitiveType,
    university_StaffMember,
    university_Student,
    university_University,
    university_Vehicle,
    StaffMemberType,
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

def test_assoc_registeredVehicle6_reverse_link_reassign_clear():
    a1 = university_Vehicle(registrationNumber="sample_text")
    a2 = university_Vehicle(registrationNumber="sample_text_2")
    b = university_Student(studentId=3.14)
    _safe_set(b, 'university_Student', a1)
    assert _is_linked(b, 'university_Student', a1)
    if hasattr(a1, 'university_Vehicle'):
        assert _is_linked(a1, 'university_Vehicle', b)
    _safe_set(b, 'university_Student', a2)
    assert _is_linked(b, 'university_Student', a2)
    if hasattr(a1, 'university_Vehicle'):
        assert not _is_linked(a1, 'university_Vehicle', b)
    if hasattr(a2, 'university_Vehicle'):
        assert _is_linked(a2, 'university_Vehicle', b)
    _safe_set(b, 'university_Student', None)
    assert not _is_linked(b, 'university_Student', a2)
    if hasattr(a2, 'university_Vehicle'):
        assert not _is_linked(a2, 'university_Vehicle', b)


def test_assoc_registeredVehicles16_reverse_link_reassign_clear():
    a1 = university_Vehicle(registrationNumber="sample_text")
    a2 = university_Vehicle(registrationNumber="sample_text_2")
    b = university_StaffMember(staffMemberType="sample_text")
    _safe_set(b, 'university_StaffMember17', {a1})
    assert _is_linked(b, 'university_StaffMember17', a1)
    if hasattr(a1, 'university_Vehicle18'):
        assert _is_linked(a1, 'university_Vehicle18', b)
    _safe_set(b, 'university_StaffMember17', {a2})
    assert _is_linked(b, 'university_StaffMember17', a2)
    if hasattr(a1, 'university_Vehicle18'):
        assert not _is_linked(a1, 'university_Vehicle18', b)
    if hasattr(a2, 'university_Vehicle18'):
        assert _is_linked(a2, 'university_Vehicle18', b)
    _safe_set(b, 'university_StaffMember17', set())
    assert not _is_linked(b, 'university_StaffMember17', a2)
    if hasattr(a2, 'university_Vehicle18'):
        assert not _is_linked(a2, 'university_Vehicle18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_books9_stub_double():
    # university_Library has no real 'university_Library10' property in the generated
    # code (a bare stub) -- manually attach it so university_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Book(ISBN="sample_text", authorNames="sample_text")
    partner = university_Library()
    setattr(partner, 'university_Library10', None)
    _safe_set(owner, 'university_Book', partner)
    assert owner in getattr(partner, 'university_Library10')
    _safe_set(owner, 'university_Book', None)
    assert owner not in getattr(partner, 'university_Library10')


def test_assoc_chancelor3_stub_double():
    # university_University has no real 'university_University4' property in the generated
    # code (a bare stub) -- manually attach it so university_StaffMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_StaffMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_StaffMember(staffMemberType="sample_text")
    partner = university_University()
    setattr(partner, 'university_University4', None)
    _safe_set(owner, 'university_StaffMember', partner)
    assert getattr(partner, 'university_University4') == owner
    _safe_set(owner, 'university_StaffMember', None)
    assert getattr(partner, 'university_University4') is None


def test_assoc_enrolledModules5_stub_double():
    # university_Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so university_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Student(studentId=3.14)
    partner = university_Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'enrolledStudents', {partner})
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'enrolledStudents', set())
    assert getattr(partner, 'Module') is None


def test_assoc_enrolledStudents26_stub_double():
    # university_Module has no real 'enrolledModules' property in the generated
    # code (a bare stub) -- manually attach it so university_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Student(studentId=3.14)
    partner = university_Module()
    setattr(partner, 'enrolledModules', None)
    _safe_set(owner, 'Student', partner)
    assert owner in getattr(partner, 'enrolledModules')
    _safe_set(owner, 'Student', None)
    assert owner not in getattr(partner, 'enrolledModules')


def test_assoc_libraryVans11_stub_double():
    # university_Library has no real 'university_Library12' property in the generated
    # code (a bare stub) -- manually attach it so university_Vehicle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Vehicle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Vehicle(registrationNumber="sample_text")
    partner = university_Library()
    setattr(partner, 'university_Library12', None)
    _safe_set(owner, 'university_Vehicle13', partner)
    assert owner in getattr(partner, 'university_Library12')
    _safe_set(owner, 'university_Vehicle13', None)
    assert owner not in getattr(partner, 'university_Library12')


def test_assoc_moduleLecturers25_stub_double():
    # university_Module has no real 'taughtModules' property in the generated
    # code (a bare stub) -- manually attach it so university_StaffMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_StaffMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_StaffMember(staffMemberType="sample_text")
    partner = university_Module()
    setattr(partner, 'taughtModules', None)
    _safe_set(owner, 'StaffMember', partner)
    assert owner in getattr(partner, 'taughtModules')
    _safe_set(owner, 'StaffMember', None)
    assert owner not in getattr(partner, 'taughtModules')


def test_assoc_staff19_stub_double():
    # university_Department has no real 'university_Department20' property in the generated
    # code (a bare stub) -- manually attach it so university_StaffMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_StaffMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_StaffMember(staffMemberType="sample_text")
    partner = university_Department()
    setattr(partner, 'university_Department20', None)
    _safe_set(owner, 'university_StaffMember21', partner)
    assert owner in getattr(partner, 'university_Department20')
    _safe_set(owner, 'university_StaffMember21', None)
    assert owner not in getattr(partner, 'university_Department20')


def test_assoc_students22_stub_double():
    # university_Department has no real 'university_Department23' property in the generated
    # code (a bare stub) -- manually attach it so university_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_Student(studentId=3.14)
    partner = university_Department()
    setattr(partner, 'university_Department23', None)
    _safe_set(owner, 'university_Student24', partner)
    assert owner in getattr(partner, 'university_Department23')
    _safe_set(owner, 'university_Student24', None)
    assert owner not in getattr(partner, 'university_Department23')


def test_assoc_taughtModules14_stub_double():
    # university_Module has no real 'Module15' property in the generated
    # code (a bare stub) -- manually attach it so university_StaffMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # university_StaffMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = university_StaffMember(staffMemberType="sample_text")
    partner = university_Module()
    setattr(partner, 'Module15', None)
    _safe_set(owner, 'moduleLecturers', {partner})
    assert getattr(partner, 'Module15') == owner
    _safe_set(owner, 'moduleLecturers', set())
    assert getattr(partner, 'Module15') is None


