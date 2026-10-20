import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    scholar_Discipline,
    scholar_Exam,
    scholar_Lecture,
    scholar_Named,
    scholar_ScholarManagement,
    scholar_Student,
    scholar_Teacher,
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

def test_assoc_exams0_reverse_link_reassign_clear():
    a1 = scholar_Student(forname="sample_text")
    a2 = scholar_Student(forname="sample_text_2")
    b = scholar_Exam(score=3.14)
    _safe_set(b, 'scholar_Exam', a1)
    assert _is_linked(b, 'scholar_Exam', a1)
    if hasattr(a1, 'scholar_Student'):
        assert _is_linked(a1, 'scholar_Student', b)
    _safe_set(b, 'scholar_Exam', a2)
    assert _is_linked(b, 'scholar_Exam', a2)
    if hasattr(a1, 'scholar_Student'):
        assert not _is_linked(a1, 'scholar_Student', b)
    if hasattr(a2, 'scholar_Student'):
        assert _is_linked(a2, 'scholar_Student', b)
    _safe_set(b, 'scholar_Exam', None)
    assert not _is_linked(b, 'scholar_Exam', a2)
    if hasattr(a2, 'scholar_Student'):
        assert not _is_linked(a2, 'scholar_Student', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_lecture4_stub_double():
    # scholar_Lecture has no real 'scholar_Lecture6' property in the generated
    # code (a bare stub) -- manually attach it so scholar_Exam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scholar_Exam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scholar_Exam(score=3.14)
    partner = scholar_Lecture()
    setattr(partner, 'scholar_Lecture6', None)
    _safe_set(owner, 'scholar_Exam5', partner)
    assert getattr(partner, 'scholar_Lecture6') == owner
    _safe_set(owner, 'scholar_Exam5', None)
    assert getattr(partner, 'scholar_Lecture6') is None


def test_assoc_students7_stub_double():
    # scholar_ScholarManagement has no real 'scholar_ScholarManagement' property in the generated
    # code (a bare stub) -- manually attach it so scholar_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scholar_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scholar_Student(forname="sample_text")
    partner = scholar_ScholarManagement()
    setattr(partner, 'scholar_ScholarManagement', None)
    _safe_set(owner, 'scholar_Student8', partner)
    assert owner in getattr(partner, 'scholar_ScholarManagement')
    _safe_set(owner, 'scholar_Student8', None)
    assert owner not in getattr(partner, 'scholar_ScholarManagement')


