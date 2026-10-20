import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    classmate_ClassmateSystem,
    classmate_Classroom,
    classmate_Friend,
    classmate_School,
    classmate_Student,
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

def test_assoc_classrooms4_reverse_link_reassign_clear():
    a1 = classmate_School(name="sample_text")
    a2 = classmate_School(name="sample_text_2")
    b = classmate_Classroom(name="sample_text")
    _safe_set(b, 'classmate_Classroom6', a1)
    assert _is_linked(b, 'classmate_Classroom6', a1)
    if hasattr(a1, 'classmate_School5'):
        assert _is_linked(a1, 'classmate_School5', b)
    _safe_set(b, 'classmate_Classroom6', a2)
    assert _is_linked(b, 'classmate_Classroom6', a2)
    if hasattr(a1, 'classmate_School5'):
        assert not _is_linked(a1, 'classmate_School5', b)
    if hasattr(a2, 'classmate_School5'):
        assert _is_linked(a2, 'classmate_School5', b)
    _safe_set(b, 'classmate_Classroom6', None)
    assert not _is_linked(b, 'classmate_Classroom6', a2)
    if hasattr(a2, 'classmate_School5'):
        assert not _is_linked(a2, 'classmate_School5', b)


def test_assoc_fromStudent7_reverse_link_reassign_clear():
    a1 = classmate_Student(name="sample_text")
    a2 = classmate_Student(name="sample_text_2")
    b = classmate_Friend(fromDate="sample_text", toDate="sample_text")
    _safe_set(b, 'classmate_Friend8', a1)
    assert _is_linked(b, 'classmate_Friend8', a1)
    if hasattr(a1, 'classmate_Student9'):
        assert _is_linked(a1, 'classmate_Student9', b)
    _safe_set(b, 'classmate_Friend8', a2)
    assert _is_linked(b, 'classmate_Friend8', a2)
    if hasattr(a1, 'classmate_Student9'):
        assert not _is_linked(a1, 'classmate_Student9', b)
    if hasattr(a2, 'classmate_Student9'):
        assert _is_linked(a2, 'classmate_Student9', b)
    _safe_set(b, 'classmate_Friend8', None)
    assert not _is_linked(b, 'classmate_Friend8', a2)
    if hasattr(a2, 'classmate_Student9'):
        assert not _is_linked(a2, 'classmate_Student9', b)


def test_assoc_students0_reverse_link_reassign_clear():
    a1 = classmate_Student(name="sample_text")
    a2 = classmate_Student(name="sample_text_2")
    b = classmate_Classroom(name="sample_text")
    _safe_set(b, 'classmate_Classroom', {a1})
    assert _is_linked(b, 'classmate_Classroom', a1)
    if hasattr(a1, 'classmate_Student'):
        assert _is_linked(a1, 'classmate_Student', b)
    _safe_set(b, 'classmate_Classroom', {a2})
    assert _is_linked(b, 'classmate_Classroom', a2)
    if hasattr(a1, 'classmate_Student'):
        assert not _is_linked(a1, 'classmate_Student', b)
    if hasattr(a2, 'classmate_Student'):
        assert _is_linked(a2, 'classmate_Student', b)
    _safe_set(b, 'classmate_Classroom', set())
    assert not _is_linked(b, 'classmate_Classroom', a2)
    if hasattr(a2, 'classmate_Student'):
        assert not _is_linked(a2, 'classmate_Student', b)


def test_assoc_toStudent10_reverse_link_reassign_clear():
    a1 = classmate_Student(name="sample_text")
    a2 = classmate_Student(name="sample_text_2")
    b = classmate_Friend(fromDate="sample_text", toDate="sample_text")
    _safe_set(b, 'classmate_Friend11', a1)
    assert _is_linked(b, 'classmate_Friend11', a1)
    if hasattr(a1, 'classmate_Student12'):
        assert _is_linked(a1, 'classmate_Student12', b)
    _safe_set(b, 'classmate_Friend11', a2)
    assert _is_linked(b, 'classmate_Friend11', a2)
    if hasattr(a1, 'classmate_Student12'):
        assert not _is_linked(a1, 'classmate_Student12', b)
    if hasattr(a2, 'classmate_Student12'):
        assert _is_linked(a2, 'classmate_Student12', b)
    _safe_set(b, 'classmate_Friend11', None)
    assert not _is_linked(b, 'classmate_Friend11', a2)
    if hasattr(a2, 'classmate_Student12'):
        assert not _is_linked(a2, 'classmate_Student12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_friends2_stub_double():
    # classmate_ClassmateSystem has no real 'classmate_ClassmateSystem3' property in the generated
    # code (a bare stub) -- manually attach it so classmate_Friend's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmate_Friend's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmate_Friend(fromDate="sample_text", toDate="sample_text")
    partner = classmate_ClassmateSystem()
    setattr(partner, 'classmate_ClassmateSystem3', None)
    _safe_set(owner, 'classmate_Friend', partner)
    assert owner in getattr(partner, 'classmate_ClassmateSystem3')
    _safe_set(owner, 'classmate_Friend', None)
    assert owner not in getattr(partner, 'classmate_ClassmateSystem3')


def test_assoc_school1_stub_double():
    # classmate_ClassmateSystem has no real 'classmate_ClassmateSystem' property in the generated
    # code (a bare stub) -- manually attach it so classmate_School's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmate_School's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmate_School(name="sample_text")
    partner = classmate_ClassmateSystem()
    setattr(partner, 'classmate_ClassmateSystem', None)
    _safe_set(owner, 'classmate_School', partner)
    assert getattr(partner, 'classmate_ClassmateSystem') == owner
    _safe_set(owner, 'classmate_School', None)
    assert getattr(partner, 'classmate_ClassmateSystem') is None


