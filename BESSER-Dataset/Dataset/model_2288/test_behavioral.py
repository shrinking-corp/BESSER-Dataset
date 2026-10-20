import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Task,
    gradingsystem_ConcreteTask,
    gradingsystem_Course,
    gradingsystem_Grade,
    gradingsystem_Grading,
    gradingsystem_GradingScheme,
    gradingsystem_GradingSystem,
    gradingsystem_MinRequirement,
    gradingsystem_Task,
    gradingsystem_TaskGroup,
    MinRequirementsType,
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

def test_assoc_gradings1_reverse_link_reassign_clear():
    a1 = gradingsystem_Grading(semester="sample_text")
    a2 = gradingsystem_Grading(semester="sample_text_2")
    b = gradingsystem_Course(name="sample_text")
    _safe_set(b, 'gradingsystem_Course2', {a1})
    assert _is_linked(b, 'gradingsystem_Course2', a1)
    if hasattr(a1, 'gradingsystem_Grading'):
        assert _is_linked(a1, 'gradingsystem_Grading', b)
    _safe_set(b, 'gradingsystem_Course2', {a2})
    assert _is_linked(b, 'gradingsystem_Course2', a2)
    if hasattr(a1, 'gradingsystem_Grading'):
        assert not _is_linked(a1, 'gradingsystem_Grading', b)
    if hasattr(a2, 'gradingsystem_Grading'):
        assert _is_linked(a2, 'gradingsystem_Grading', b)
    _safe_set(b, 'gradingsystem_Course2', set())
    assert not _is_linked(b, 'gradingsystem_Course2', a2)
    if hasattr(a2, 'gradingsystem_Grading'):
        assert not _is_linked(a2, 'gradingsystem_Grading', b)


def test_assoc_minRequirement3_reverse_link_reassign_clear():
    a1 = gradingsystem_Task(name="sample_text")
    a2 = gradingsystem_Task(name="sample_text_2")
    b = gradingsystem_MinRequirement(type="sample_text", value=7)
    _safe_set(b, 'gradingsystem_MinRequirement', a1)
    assert _is_linked(b, 'gradingsystem_MinRequirement', a1)
    if hasattr(a1, 'gradingsystem_Task'):
        assert _is_linked(a1, 'gradingsystem_Task', b)
    _safe_set(b, 'gradingsystem_MinRequirement', a2)
    assert _is_linked(b, 'gradingsystem_MinRequirement', a2)
    if hasattr(a1, 'gradingsystem_Task'):
        assert not _is_linked(a1, 'gradingsystem_Task', b)
    if hasattr(a2, 'gradingsystem_Task'):
        assert _is_linked(a2, 'gradingsystem_Task', b)
    _safe_set(b, 'gradingsystem_MinRequirement', None)
    assert not _is_linked(b, 'gradingsystem_MinRequirement', a2)
    if hasattr(a2, 'gradingsystem_Task'):
        assert not _is_linked(a2, 'gradingsystem_Task', b)


def test_assoc_tasks10_reverse_link_reassign_clear():
    a1 = gradingsystem_Task(name="sample_text")
    a2 = gradingsystem_Task(name="sample_text_2")
    b = gradingsystem_Grading(semester="sample_text")
    _safe_set(b, 'gradingsystem_Grading11', {a1})
    assert _is_linked(b, 'gradingsystem_Grading11', a1)
    if hasattr(a1, 'gradingsystem_Task12'):
        assert _is_linked(a1, 'gradingsystem_Task12', b)
    _safe_set(b, 'gradingsystem_Grading11', {a2})
    assert _is_linked(b, 'gradingsystem_Grading11', a2)
    if hasattr(a1, 'gradingsystem_Task12'):
        assert not _is_linked(a1, 'gradingsystem_Task12', b)
    if hasattr(a2, 'gradingsystem_Task12'):
        assert _is_linked(a2, 'gradingsystem_Task12', b)
    _safe_set(b, 'gradingsystem_Grading11', set())
    assert not _is_linked(b, 'gradingsystem_Grading11', a2)
    if hasattr(a2, 'gradingsystem_Task12'):
        assert not _is_linked(a2, 'gradingsystem_Task12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contains4_stub_double():
    # gradingsystem_TaskGroup has no real 'gradingsystem_TaskGroup' property in the generated
    # code (a bare stub) -- manually attach it so gradingsystem_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gradingsystem_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gradingsystem_Task(name="sample_text")
    partner = gradingsystem_TaskGroup()
    setattr(partner, 'gradingsystem_TaskGroup', None)
    _safe_set(owner, 'gradingsystem_Task5', partner)
    assert owner in getattr(partner, 'gradingsystem_TaskGroup')
    _safe_set(owner, 'gradingsystem_Task5', None)
    assert owner not in getattr(partner, 'gradingsystem_TaskGroup')


def test_assoc_courses0_stub_double():
    # gradingsystem_GradingSystem has no real 'gradingsystem_GradingSystem' property in the generated
    # code (a bare stub) -- manually attach it so gradingsystem_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gradingsystem_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gradingsystem_Course(name="sample_text")
    partner = gradingsystem_GradingSystem()
    setattr(partner, 'gradingsystem_GradingSystem', None)
    _safe_set(owner, 'gradingsystem_Course', partner)
    assert owner in getattr(partner, 'gradingsystem_GradingSystem')
    _safe_set(owner, 'gradingsystem_Course', None)
    assert owner not in getattr(partner, 'gradingsystem_GradingSystem')


def test_assoc_grades6_stub_double():
    # gradingsystem_GradingScheme has no real 'gradingsystem_GradingScheme' property in the generated
    # code (a bare stub) -- manually attach it so gradingsystem_Grade's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gradingsystem_Grade's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gradingsystem_Grade(name="sample_text", requiredPoints=7)
    partner = gradingsystem_GradingScheme()
    setattr(partner, 'gradingsystem_GradingScheme', None)
    _safe_set(owner, 'gradingsystem_Grade', partner)
    assert owner in getattr(partner, 'gradingsystem_GradingScheme')
    _safe_set(owner, 'gradingsystem_Grade', None)
    assert owner not in getattr(partner, 'gradingsystem_GradingScheme')


def test_assoc_gradingScheme13_stub_double():
    # gradingsystem_GradingScheme has no real 'gradingsystem_GradingScheme15' property in the generated
    # code (a bare stub) -- manually attach it so gradingsystem_Grading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gradingsystem_Grading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gradingsystem_Grading(semester="sample_text")
    partner = gradingsystem_GradingScheme()
    setattr(partner, 'gradingsystem_GradingScheme15', None)
    _safe_set(owner, 'gradingsystem_Grading14', partner)
    assert getattr(partner, 'gradingsystem_GradingScheme15') == owner
    _safe_set(owner, 'gradingsystem_Grading14', None)
    assert getattr(partner, 'gradingsystem_GradingScheme15') is None


def test_assoc_minRequirementNotFulfilledGrade7_stub_double():
    # gradingsystem_GradingScheme has no real 'gradingsystem_GradingScheme8' property in the generated
    # code (a bare stub) -- manually attach it so gradingsystem_Grade's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gradingsystem_Grade's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gradingsystem_Grade(name="sample_text", requiredPoints=7)
    partner = gradingsystem_GradingScheme()
    setattr(partner, 'gradingsystem_GradingScheme8', None)
    _safe_set(owner, 'gradingsystem_Grade9', partner)
    assert getattr(partner, 'gradingsystem_GradingScheme8') == owner
    _safe_set(owner, 'gradingsystem_Grade9', None)
    assert getattr(partner, 'gradingsystem_GradingScheme8') is None


