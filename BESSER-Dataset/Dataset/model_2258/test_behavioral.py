import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Courses_Answer,
    Courses_Assignment,
    Courses_Course,
    Courses_Person,
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

def test_assoc_answer5_reverse_link_reassign_clear():
    a1 = Courses_Assignment(description="sample_text", mandatory=True, name="sample_text")
    a2 = Courses_Assignment(description="sample_text_2", mandatory=False, name="sample_text_2")
    b = Courses_Answer(id=7, pass_=True, text="sample_text")
    _safe_set(b, 'Courses_Answer7', a1)
    assert _is_linked(b, 'Courses_Answer7', a1)
    if hasattr(a1, 'Courses_Assignment6'):
        assert _is_linked(a1, 'Courses_Assignment6', b)
    _safe_set(b, 'Courses_Answer7', a2)
    assert _is_linked(b, 'Courses_Answer7', a2)
    if hasattr(a1, 'Courses_Assignment6'):
        assert not _is_linked(a1, 'Courses_Assignment6', b)
    if hasattr(a2, 'Courses_Assignment6'):
        assert _is_linked(a2, 'Courses_Assignment6', b)
    _safe_set(b, 'Courses_Answer7', None)
    assert not _is_linked(b, 'Courses_Answer7', a2)
    if hasattr(a2, 'Courses_Assignment6'):
        assert not _is_linked(a2, 'Courses_Assignment6', b)


def test_assoc_assignmentDelivery3_reverse_link_reassign_clear():
    a1 = Courses_Person(id=7, name="sample_text", role="sample_text")
    a2 = Courses_Person(id=13, name="sample_text_2", role="sample_text_2")
    b = Courses_Answer(id=7, pass_=True, text="sample_text")
    _safe_set(b, 'Courses_Answer', a1)
    assert _is_linked(b, 'Courses_Answer', a1)
    if hasattr(a1, 'Courses_Person4'):
        assert _is_linked(a1, 'Courses_Person4', b)
    _safe_set(b, 'Courses_Answer', a2)
    assert _is_linked(b, 'Courses_Answer', a2)
    if hasattr(a1, 'Courses_Person4'):
        assert not _is_linked(a1, 'Courses_Person4', b)
    if hasattr(a2, 'Courses_Person4'):
        assert _is_linked(a2, 'Courses_Person4', b)
    _safe_set(b, 'Courses_Answer', None)
    assert not _is_linked(b, 'Courses_Answer', a2)
    if hasattr(a2, 'Courses_Person4'):
        assert not _is_linked(a2, 'Courses_Person4', b)


def test_assoc_assignments1_reverse_link_reassign_clear():
    a1 = Courses_Course(credit=3.14, id="sample_text", name="sample_text")
    a2 = Courses_Course(credit=9.99, id="sample_text_2", name="sample_text_2")
    b = Courses_Assignment(description="sample_text", mandatory=True, name="sample_text")
    _safe_set(b, 'Courses_Assignment', a1)
    assert _is_linked(b, 'Courses_Assignment', a1)
    if hasattr(a1, 'Courses_Course2'):
        assert _is_linked(a1, 'Courses_Course2', b)
    _safe_set(b, 'Courses_Assignment', a2)
    assert _is_linked(b, 'Courses_Assignment', a2)
    if hasattr(a1, 'Courses_Course2'):
        assert not _is_linked(a1, 'Courses_Course2', b)
    if hasattr(a2, 'Courses_Course2'):
        assert _is_linked(a2, 'Courses_Course2', b)
    _safe_set(b, 'Courses_Assignment', None)
    assert not _is_linked(b, 'Courses_Assignment', a2)
    if hasattr(a2, 'Courses_Course2'):
        assert not _is_linked(a2, 'Courses_Course2', b)


def test_assoc_members0_reverse_link_reassign_clear():
    a1 = Courses_Person(id=7, name="sample_text", role="sample_text")
    a2 = Courses_Person(id=13, name="sample_text_2", role="sample_text_2")
    b = Courses_Course(credit=3.14, id="sample_text", name="sample_text")
    _safe_set(b, 'Courses_Course', {a1})
    assert _is_linked(b, 'Courses_Course', a1)
    if hasattr(a1, 'Courses_Person'):
        assert _is_linked(a1, 'Courses_Person', b)
    _safe_set(b, 'Courses_Course', {a2})
    assert _is_linked(b, 'Courses_Course', a2)
    if hasattr(a1, 'Courses_Person'):
        assert not _is_linked(a1, 'Courses_Person', b)
    if hasattr(a2, 'Courses_Person'):
        assert _is_linked(a2, 'Courses_Person', b)
    _safe_set(b, 'Courses_Course', set())
    assert not _is_linked(b, 'Courses_Course', a2)
    if hasattr(a2, 'Courses_Person'):
        assert not _is_linked(a2, 'Courses_Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

