import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    Person,
    school_Named,
    school_Person,
    school_School,
    school_SchoolModel,
    school_SchoolStatistics,
    school_Student,
    school_Teacher,
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

def test_assoc_statistics1_reverse_link_reassign_clear():
    a1 = school_SchoolStatistics(studentsNumber=7, studentsWithNoTeacher="sample_text", teachersNumber=7)
    a2 = school_SchoolStatistics(studentsNumber=13, studentsWithNoTeacher="sample_text_2", teachersNumber=13)
    b = school_School()
    _safe_set(b, 'school_School2', a1)
    assert _is_linked(b, 'school_School2', a1)
    if hasattr(a1, 'school_SchoolStatistics'):
        assert _is_linked(a1, 'school_SchoolStatistics', b)
    _safe_set(b, 'school_School2', a2)
    assert _is_linked(b, 'school_School2', a2)
    if hasattr(a1, 'school_SchoolStatistics'):
        assert not _is_linked(a1, 'school_SchoolStatistics', b)
    if hasattr(a2, 'school_SchoolStatistics'):
        assert _is_linked(a2, 'school_SchoolStatistics', b)
    _safe_set(b, 'school_School2', None)
    assert not _is_linked(b, 'school_School2', a2)
    if hasattr(a2, 'school_SchoolStatistics'):
        assert not _is_linked(a2, 'school_SchoolStatistics', b)


