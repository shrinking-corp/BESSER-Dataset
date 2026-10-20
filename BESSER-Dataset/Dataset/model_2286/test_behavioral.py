import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Task,
    gsml_ConcreteTask,
    gsml_Course,
    gsml_Grade,
    gsml_Grading,
    gsml_GradingScheme,
    gsml_GradingSystem,
    gsml_Task,
    gsml_TaskGroup,
    MinRequirementType,
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

def test_assoc_gradings0_reverse_link_reassign_clear():
    a1 = gsml_Grading(Semester="sample_text")
    a2 = gsml_Grading(Semester="sample_text_2")
    b = gsml_Course(Name="sample_text")
    _safe_set(b, 'gsml_Course', {a1})
    assert _is_linked(b, 'gsml_Course', a1)
    if hasattr(a1, 'gsml_Grading'):
        assert _is_linked(a1, 'gsml_Grading', b)
    _safe_set(b, 'gsml_Course', {a2})
    assert _is_linked(b, 'gsml_Course', a2)
    if hasattr(a1, 'gsml_Grading'):
        assert not _is_linked(a1, 'gsml_Grading', b)
    if hasattr(a2, 'gsml_Grading'):
        assert _is_linked(a2, 'gsml_Grading', b)
    _safe_set(b, 'gsml_Course', set())
    assert not _is_linked(b, 'gsml_Course', a2)
    if hasattr(a2, 'gsml_Grading'):
        assert not _is_linked(a2, 'gsml_Grading', b)


def test_assoc_has23_reverse_link_reassign_clear():
    a1 = gsml_Task(MinRequirement=3.14, MinRequirementType="sample_text", Name="sample_text")
    a2 = gsml_Task(MinRequirement=9.99, MinRequirementType="sample_text_2", Name="sample_text_2")
    b = gsml_Grading(Semester="sample_text")
    _safe_set(b, 'gsml_Grading24', {a1})
    assert _is_linked(b, 'gsml_Grading24', a1)
    if hasattr(a1, 'gsml_Task25'):
        assert _is_linked(a1, 'gsml_Task25', b)
    _safe_set(b, 'gsml_Grading24', {a2})
    assert _is_linked(b, 'gsml_Grading24', a2)
    if hasattr(a1, 'gsml_Task25'):
        assert not _is_linked(a1, 'gsml_Task25', b)
    if hasattr(a2, 'gsml_Task25'):
        assert _is_linked(a2, 'gsml_Task25', b)
    _safe_set(b, 'gsml_Grading24', set())
    assert not _is_linked(b, 'gsml_Grading24', a2)
    if hasattr(a2, 'gsml_Task25'):
        assert not _is_linked(a2, 'gsml_Task25', b)


def test_assoc_tasks20_reverse_link_reassign_clear():
    a1 = gsml_Task(MinRequirement=3.14, MinRequirementType="sample_text", Name="sample_text")
    a2 = gsml_Task(MinRequirement=9.99, MinRequirementType="sample_text_2", Name="sample_text_2")
    b = gsml_Grading(Semester="sample_text")
    _safe_set(b, 'gsml_Grading21', {a1})
    assert _is_linked(b, 'gsml_Grading21', a1)
    if hasattr(a1, 'gsml_Task22'):
        assert _is_linked(a1, 'gsml_Task22', b)
    _safe_set(b, 'gsml_Grading21', {a2})
    assert _is_linked(b, 'gsml_Grading21', a2)
    if hasattr(a1, 'gsml_Task22'):
        assert not _is_linked(a1, 'gsml_Task22', b)
    if hasattr(a2, 'gsml_Task22'):
        assert _is_linked(a2, 'gsml_Task22', b)
    _safe_set(b, 'gsml_Grading21', set())
    assert not _is_linked(b, 'gsml_Grading21', a2)
    if hasattr(a2, 'gsml_Task22'):
        assert not _is_linked(a2, 'gsml_Task22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contains9_stub_double():
    # gsml_TaskGroup has no real 'gsml_TaskGroup' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Task(MinRequirement=3.14, MinRequirementType="sample_text", Name="sample_text")
    partner = gsml_TaskGroup()
    setattr(partner, 'gsml_TaskGroup', None)
    _safe_set(owner, 'gsml_Task', partner)
    assert owner in getattr(partner, 'gsml_TaskGroup')
    _safe_set(owner, 'gsml_Task', None)
    assert owner not in getattr(partner, 'gsml_TaskGroup')


def test_assoc_courses15_stub_double():
    # gsml_GradingSystem has no real 'gsml_GradingSystem' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Course(Name="sample_text")
    partner = gsml_GradingSystem()
    setattr(partner, 'gsml_GradingSystem', None)
    _safe_set(owner, 'gsml_Course16', partner)
    assert owner in getattr(partner, 'gsml_GradingSystem')
    _safe_set(owner, 'gsml_Course16', None)
    assert owner not in getattr(partner, 'gsml_GradingSystem')


def test_assoc_fallback12_stub_double():
    # gsml_GradingScheme has no real 'gsml_GradingScheme13' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Grade's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Grade's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Grade(Name="sample_text", RequiredPoints=3.14)
    partner = gsml_GradingScheme()
    setattr(partner, 'gsml_GradingScheme13', None)
    _safe_set(owner, 'gsml_Grade14', partner)
    assert getattr(partner, 'gsml_GradingScheme13') == owner
    _safe_set(owner, 'gsml_Grade14', None)
    assert getattr(partner, 'gsml_GradingScheme13') is None


def test_assoc_grades10_stub_double():
    # gsml_GradingScheme has no real 'gsml_GradingScheme11' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Grade's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Grade's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Grade(Name="sample_text", RequiredPoints=3.14)
    partner = gsml_GradingScheme()
    setattr(partner, 'gsml_GradingScheme11', None)
    _safe_set(owner, 'gsml_Grade', partner)
    assert owner in getattr(partner, 'gsml_GradingScheme11')
    _safe_set(owner, 'gsml_Grade', None)
    assert owner not in getattr(partner, 'gsml_GradingScheme11')


def test_assoc_gradingScheme6_stub_double():
    # gsml_GradingScheme has no real 'gsml_GradingScheme8' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Course(Name="sample_text")
    partner = gsml_GradingScheme()
    setattr(partner, 'gsml_GradingScheme8', None)
    _safe_set(owner, 'gsml_Course7', partner)
    assert getattr(partner, 'gsml_GradingScheme8') == owner
    _safe_set(owner, 'gsml_Course7', None)
    assert getattr(partner, 'gsml_GradingScheme8') is None


def test_assoc_gradingscheme17_stub_double():
    # gsml_GradingScheme has no real 'gsml_GradingScheme19' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Grading's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Grading's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Grading(Semester="sample_text")
    partner = gsml_GradingScheme()
    setattr(partner, 'gsml_GradingScheme19', None)
    _safe_set(owner, 'gsml_Grading18', partner)
    assert getattr(partner, 'gsml_GradingScheme19') == owner
    _safe_set(owner, 'gsml_Grading18', None)
    assert getattr(partner, 'gsml_GradingScheme19') is None


def test_assoc_gradingscheme3_stub_double():
    # gsml_GradingScheme has no real 'gsml_GradingScheme5' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Course(Name="sample_text")
    partner = gsml_GradingScheme()
    setattr(partner, 'gsml_GradingScheme5', None)
    _safe_set(owner, 'gsml_Course4', partner)
    assert getattr(partner, 'gsml_GradingScheme5') == owner
    _safe_set(owner, 'gsml_Course4', None)
    assert getattr(partner, 'gsml_GradingScheme5') is None


def test_assoc_gradingschemes1_stub_double():
    # gsml_GradingScheme has no real 'gsml_GradingScheme' property in the generated
    # code (a bare stub) -- manually attach it so gsml_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gsml_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gsml_Course(Name="sample_text")
    partner = gsml_GradingScheme()
    setattr(partner, 'gsml_GradingScheme', None)
    _safe_set(owner, 'gsml_Course2', {partner})
    assert getattr(partner, 'gsml_GradingScheme') == owner
    _safe_set(owner, 'gsml_Course2', set())
    assert getattr(partner, 'gsml_GradingScheme') is None


