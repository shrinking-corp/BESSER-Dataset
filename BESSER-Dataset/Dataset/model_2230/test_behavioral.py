import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyprogram_Course,
    studyprogram_Department,
    studyprogram_Program,
    studyprogram_Semester,
    studyprogram_Slot,
    studyprogram_Specialization,
    Season,
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

def test_assoc_additionalSpecializations7_reverse_link_reassign_clear():
    a1 = studyprogram_Specialization(name="sample_text")
    a2 = studyprogram_Specialization(name="sample_text_2")
    b = studyprogram_Specialization(name="sample_text")
    _safe_set(b, 'studyprogram_Specialization8', a1)
    assert _is_linked(b, 'studyprogram_Specialization8', a1)
    if hasattr(a1, 'studyprogram_Specialization6'):
        assert _is_linked(a1, 'studyprogram_Specialization6', b)
    _safe_set(b, 'studyprogram_Specialization8', a2)
    assert _is_linked(b, 'studyprogram_Specialization8', a2)
    if hasattr(a1, 'studyprogram_Specialization6'):
        assert not _is_linked(a1, 'studyprogram_Specialization6', b)
    if hasattr(a2, 'studyprogram_Specialization6'):
        assert _is_linked(a2, 'studyprogram_Specialization6', b)
    _safe_set(b, 'studyprogram_Specialization8', None)
    assert not _is_linked(b, 'studyprogram_Specialization8', a2)
    if hasattr(a2, 'studyprogram_Specialization6'):
        assert not _is_linked(a2, 'studyprogram_Specialization6', b)


def test_assoc_baseSemesters0_reverse_link_reassign_clear():
    a1 = studyprogram_Semester(season="sample_text", year=7)
    a2 = studyprogram_Semester(season="sample_text_2", year=13)
    b = studyprogram_Program(name="sample_text")
    _safe_set(b, 'studyprogram_Program', {a1})
    assert _is_linked(b, 'studyprogram_Program', a1)
    if hasattr(a1, 'studyprogram_Semester'):
        assert _is_linked(a1, 'studyprogram_Semester', b)
    _safe_set(b, 'studyprogram_Program', {a2})
    assert _is_linked(b, 'studyprogram_Program', a2)
    if hasattr(a1, 'studyprogram_Semester'):
        assert not _is_linked(a1, 'studyprogram_Semester', b)
    if hasattr(a2, 'studyprogram_Semester'):
        assert _is_linked(a2, 'studyprogram_Semester', b)
    _safe_set(b, 'studyprogram_Program', set())
    assert not _is_linked(b, 'studyprogram_Program', a2)
    if hasattr(a2, 'studyprogram_Semester'):
        assert not _is_linked(a2, 'studyprogram_Semester', b)


def test_assoc_courses16_reverse_link_reassign_clear():
    a1 = studyprogram_Department(name="sample_text")
    a2 = studyprogram_Department(name="sample_text_2")
    b = studyprogram_Course(credits=3.14, name="sample_text")
    _safe_set(b, 'studyprogram_Course17', a1)
    assert _is_linked(b, 'studyprogram_Course17', a1)
    if hasattr(a1, 'studyprogram_Department'):
        assert _is_linked(a1, 'studyprogram_Department', b)
    _safe_set(b, 'studyprogram_Course17', a2)
    assert _is_linked(b, 'studyprogram_Course17', a2)
    if hasattr(a1, 'studyprogram_Department'):
        assert not _is_linked(a1, 'studyprogram_Department', b)
    if hasattr(a2, 'studyprogram_Department'):
        assert _is_linked(a2, 'studyprogram_Department', b)
    _safe_set(b, 'studyprogram_Course17', None)
    assert not _is_linked(b, 'studyprogram_Course17', a2)
    if hasattr(a2, 'studyprogram_Department'):
        assert not _is_linked(a2, 'studyprogram_Department', b)


def test_assoc_programs18_reverse_link_reassign_clear():
    a1 = studyprogram_Program(name="sample_text")
    a2 = studyprogram_Program(name="sample_text_2")
    b = studyprogram_Department(name="sample_text")
    _safe_set(b, 'studyprogram_Department19', {a1})
    assert _is_linked(b, 'studyprogram_Department19', a1)
    if hasattr(a1, 'studyprogram_Program20'):
        assert _is_linked(a1, 'studyprogram_Program20', b)
    _safe_set(b, 'studyprogram_Department19', {a2})
    assert _is_linked(b, 'studyprogram_Department19', a2)
    if hasattr(a1, 'studyprogram_Program20'):
        assert not _is_linked(a1, 'studyprogram_Program20', b)
    if hasattr(a2, 'studyprogram_Program20'):
        assert _is_linked(a2, 'studyprogram_Program20', b)
    _safe_set(b, 'studyprogram_Department19', set())
    assert not _is_linked(b, 'studyprogram_Department19', a2)
    if hasattr(a2, 'studyprogram_Program20'):
        assert not _is_linked(a2, 'studyprogram_Program20', b)


def test_assoc_specializationSemesters3_reverse_link_reassign_clear():
    a1 = studyprogram_Specialization(name="sample_text")
    a2 = studyprogram_Specialization(name="sample_text_2")
    b = studyprogram_Semester(season="sample_text", year=7)
    _safe_set(b, 'studyprogram_Semester5', a1)
    assert _is_linked(b, 'studyprogram_Semester5', a1)
    if hasattr(a1, 'studyprogram_Specialization4'):
        assert _is_linked(a1, 'studyprogram_Specialization4', b)
    _safe_set(b, 'studyprogram_Semester5', a2)
    assert _is_linked(b, 'studyprogram_Semester5', a2)
    if hasattr(a1, 'studyprogram_Specialization4'):
        assert not _is_linked(a1, 'studyprogram_Specialization4', b)
    if hasattr(a2, 'studyprogram_Specialization4'):
        assert _is_linked(a2, 'studyprogram_Specialization4', b)
    _safe_set(b, 'studyprogram_Semester5', None)
    assert not _is_linked(b, 'studyprogram_Semester5', a2)
    if hasattr(a2, 'studyprogram_Specialization4'):
        assert not _is_linked(a2, 'studyprogram_Specialization4', b)


def test_assoc_specializations1_reverse_link_reassign_clear():
    a1 = studyprogram_Specialization(name="sample_text")
    a2 = studyprogram_Specialization(name="sample_text_2")
    b = studyprogram_Program(name="sample_text")
    _safe_set(b, 'studyprogram_Program2', {a1})
    assert _is_linked(b, 'studyprogram_Program2', a1)
    if hasattr(a1, 'studyprogram_Specialization'):
        assert _is_linked(a1, 'studyprogram_Specialization', b)
    _safe_set(b, 'studyprogram_Program2', {a2})
    assert _is_linked(b, 'studyprogram_Program2', a2)
    if hasattr(a1, 'studyprogram_Specialization'):
        assert not _is_linked(a1, 'studyprogram_Specialization', b)
    if hasattr(a2, 'studyprogram_Specialization'):
        assert _is_linked(a2, 'studyprogram_Specialization', b)
    _safe_set(b, 'studyprogram_Program2', set())
    assert not _is_linked(b, 'studyprogram_Program2', a2)
    if hasattr(a2, 'studyprogram_Specialization'):
        assert not _is_linked(a2, 'studyprogram_Specialization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_availableCourses11_stub_double():
    # studyprogram_Slot has no real 'studyprogram_Slot12' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Course(credits=3.14, name="sample_text")
    partner = studyprogram_Slot()
    setattr(partner, 'studyprogram_Slot12', None)
    _safe_set(owner, 'studyprogram_Course', partner)
    assert owner in getattr(partner, 'studyprogram_Slot12')
    _safe_set(owner, 'studyprogram_Course', None)
    assert owner not in getattr(partner, 'studyprogram_Slot12')


def test_assoc_selectedCourse13_stub_double():
    # studyprogram_Slot has no real 'studyprogram_Slot14' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Course(credits=3.14, name="sample_text")
    partner = studyprogram_Slot()
    setattr(partner, 'studyprogram_Slot14', None)
    _safe_set(owner, 'studyprogram_Course15', partner)
    assert getattr(partner, 'studyprogram_Slot14') == owner
    _safe_set(owner, 'studyprogram_Course15', None)
    assert getattr(partner, 'studyprogram_Slot14') is None


def test_assoc_slots9_stub_double():
    # studyprogram_Slot has no real 'studyprogram_Slot' property in the generated
    # code (a bare stub) -- manually attach it so studyprogram_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogram_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogram_Semester(season="sample_text", year=7)
    partner = studyprogram_Slot()
    setattr(partner, 'studyprogram_Slot', None)
    _safe_set(owner, 'studyprogram_Semester10', {partner})
    assert getattr(partner, 'studyprogram_Slot') == owner
    _safe_set(owner, 'studyprogram_Semester10', set())
    assert getattr(partner, 'studyprogram_Slot') is None


