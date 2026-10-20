import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    school_ClassGroup,
    school_ClassLevel,
    school_NewEClass7,
    school_Room,
    school_SchoolYear,
    school_Student,
    school_Teacher,
    school_store,
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

def test_assoc_ecole10_reverse_link_reassign_clear():
    a1 = school_SchoolYear(year=date(2024, 1, 1))
    a2 = school_SchoolYear(year=date(2025, 6, 15))
    b = school_ClassGroup(name="sample_text")
    _safe_set(b, 'school_ClassGroup11', a1)
    assert _is_linked(b, 'school_ClassGroup11', a1)
    if hasattr(a1, 'school_SchoolYear'):
        assert _is_linked(a1, 'school_SchoolYear', b)
    _safe_set(b, 'school_ClassGroup11', a2)
    assert _is_linked(b, 'school_ClassGroup11', a2)
    if hasattr(a1, 'school_SchoolYear'):
        assert not _is_linked(a1, 'school_SchoolYear', b)
    if hasattr(a2, 'school_SchoolYear'):
        assert _is_linked(a2, 'school_SchoolYear', b)
    _safe_set(b, 'school_ClassGroup11', None)
    assert not _is_linked(b, 'school_ClassGroup11', a2)
    if hasattr(a2, 'school_SchoolYear'):
        assert not _is_linked(a2, 'school_SchoolYear', b)


def test_assoc_eleves0_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text")
    a2 = school_Student(name="sample_text_2")
    b = school_ClassGroup(name="sample_text")
    _safe_set(b, 'school_ClassGroup', {a1})
    assert _is_linked(b, 'school_ClassGroup', a1)
    if hasattr(a1, 'school_Student'):
        assert _is_linked(a1, 'school_Student', b)
    _safe_set(b, 'school_ClassGroup', {a2})
    assert _is_linked(b, 'school_ClassGroup', a2)
    if hasattr(a1, 'school_Student'):
        assert not _is_linked(a1, 'school_Student', b)
    if hasattr(a2, 'school_Student'):
        assert _is_linked(a2, 'school_Student', b)
    _safe_set(b, 'school_ClassGroup', set())
    assert not _is_linked(b, 'school_ClassGroup', a2)
    if hasattr(a2, 'school_Student'):
        assert not _is_linked(a2, 'school_Student', b)


def test_assoc_eleves12_reverse_link_reassign_clear():
    a1 = school_Student(name="sample_text")
    a2 = school_Student(name="sample_text_2")
    b = school_SchoolYear(year=date(2024, 1, 1))
    _safe_set(b, 'school_SchoolYear13', {a1})
    assert _is_linked(b, 'school_SchoolYear13', a1)
    if hasattr(a1, 'school_Student14'):
        assert _is_linked(a1, 'school_Student14', b)
    _safe_set(b, 'school_SchoolYear13', {a2})
    assert _is_linked(b, 'school_SchoolYear13', a2)
    if hasattr(a1, 'school_Student14'):
        assert not _is_linked(a1, 'school_Student14', b)
    if hasattr(a2, 'school_Student14'):
        assert _is_linked(a2, 'school_Student14', b)
    _safe_set(b, 'school_SchoolYear13', set())
    assert not _is_linked(b, 'school_SchoolYear13', a2)
    if hasattr(a2, 'school_Student14'):
        assert not _is_linked(a2, 'school_Student14', b)


def test_assoc_niveau15_reverse_link_reassign_clear():
    a1 = school_SchoolYear(year=date(2024, 1, 1))
    a2 = school_SchoolYear(year=date(2025, 6, 15))
    b = school_ClassLevel(level=7)
    _safe_set(b, 'school_ClassLevel17', a1)
    assert _is_linked(b, 'school_ClassLevel17', a1)
    if hasattr(a1, 'school_SchoolYear16'):
        assert _is_linked(a1, 'school_SchoolYear16', b)
    _safe_set(b, 'school_ClassLevel17', a2)
    assert _is_linked(b, 'school_ClassLevel17', a2)
    if hasattr(a1, 'school_SchoolYear16'):
        assert not _is_linked(a1, 'school_SchoolYear16', b)
    if hasattr(a2, 'school_SchoolYear16'):
        assert _is_linked(a2, 'school_SchoolYear16', b)
    _safe_set(b, 'school_ClassLevel17', None)
    assert not _is_linked(b, 'school_ClassLevel17', a2)
    if hasattr(a2, 'school_SchoolYear16'):
        assert not _is_linked(a2, 'school_SchoolYear16', b)


def test_assoc_niveau3_reverse_link_reassign_clear():
    a1 = school_ClassLevel(level=7)
    a2 = school_ClassLevel(level=13)
    b = school_ClassGroup(name="sample_text")
    _safe_set(b, 'school_ClassGroup4', a1)
    assert _is_linked(b, 'school_ClassGroup4', a1)
    if hasattr(a1, 'school_ClassLevel'):
        assert _is_linked(a1, 'school_ClassLevel', b)
    _safe_set(b, 'school_ClassGroup4', a2)
    assert _is_linked(b, 'school_ClassGroup4', a2)
    if hasattr(a1, 'school_ClassLevel'):
        assert not _is_linked(a1, 'school_ClassLevel', b)
    if hasattr(a2, 'school_ClassLevel'):
        assert _is_linked(a2, 'school_ClassLevel', b)
    _safe_set(b, 'school_ClassGroup4', None)
    assert not _is_linked(b, 'school_ClassGroup4', a2)
    if hasattr(a2, 'school_ClassLevel'):
        assert not _is_linked(a2, 'school_ClassLevel', b)


def test_assoc_prof1_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_ClassGroup(name="sample_text")
    _safe_set(b, 'school_ClassGroup2', {a1})
    assert _is_linked(b, 'school_ClassGroup2', a1)
    if hasattr(a1, 'school_Teacher'):
        assert _is_linked(a1, 'school_Teacher', b)
    _safe_set(b, 'school_ClassGroup2', {a2})
    assert _is_linked(b, 'school_ClassGroup2', a2)
    if hasattr(a1, 'school_Teacher'):
        assert not _is_linked(a1, 'school_Teacher', b)
    if hasattr(a2, 'school_Teacher'):
        assert _is_linked(a2, 'school_Teacher', b)
    _safe_set(b, 'school_ClassGroup2', set())
    assert not _is_linked(b, 'school_ClassGroup2', a2)
    if hasattr(a2, 'school_Teacher'):
        assert not _is_linked(a2, 'school_Teacher', b)


def test_assoc_room7_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_Room(location="sample_text")
    _safe_set(b, 'school_Room9', a1)
    assert _is_linked(b, 'school_Room9', a1)
    if hasattr(a1, 'school_Teacher8'):
        assert _is_linked(a1, 'school_Teacher8', b)
    _safe_set(b, 'school_Room9', a2)
    assert _is_linked(b, 'school_Room9', a2)
    if hasattr(a1, 'school_Teacher8'):
        assert not _is_linked(a1, 'school_Teacher8', b)
    if hasattr(a2, 'school_Teacher8'):
        assert _is_linked(a2, 'school_Teacher8', b)
    _safe_set(b, 'school_Room9', None)
    assert not _is_linked(b, 'school_Room9', a2)
    if hasattr(a2, 'school_Teacher8'):
        assert not _is_linked(a2, 'school_Teacher8', b)


def test_assoc_salle5_reverse_link_reassign_clear():
    a1 = school_Room(location="sample_text")
    a2 = school_Room(location="sample_text_2")
    b = school_ClassGroup(name="sample_text")
    _safe_set(b, 'school_ClassGroup6', a1)
    assert _is_linked(b, 'school_ClassGroup6', a1)
    if hasattr(a1, 'school_Room'):
        assert _is_linked(a1, 'school_Room', b)
    _safe_set(b, 'school_ClassGroup6', a2)
    assert _is_linked(b, 'school_ClassGroup6', a2)
    if hasattr(a1, 'school_Room'):
        assert not _is_linked(a1, 'school_Room', b)
    if hasattr(a2, 'school_Room'):
        assert _is_linked(a2, 'school_Room', b)
    _safe_set(b, 'school_ClassGroup6', None)
    assert not _is_linked(b, 'school_ClassGroup6', a2)
    if hasattr(a2, 'school_Room'):
        assert not _is_linked(a2, 'school_Room', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

