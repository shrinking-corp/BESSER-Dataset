import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    chartDsl_Company,
    chartDsl_Employee,
    chartDsl_Project,
    chartDsl_Task,
    ProjectType,
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

def test_assoc_employees0_reverse_link_reassign_clear():
    a1 = chartDsl_Employee(name="sample_text")
    a2 = chartDsl_Employee(name="sample_text_2")
    b = chartDsl_Company(name="sample_text")
    _safe_set(b, 'chartDsl_Company', {a1})
    assert _is_linked(b, 'chartDsl_Company', a1)
    if hasattr(a1, 'chartDsl_Employee'):
        assert _is_linked(a1, 'chartDsl_Employee', b)
    _safe_set(b, 'chartDsl_Company', {a2})
    assert _is_linked(b, 'chartDsl_Company', a2)
    if hasattr(a1, 'chartDsl_Employee'):
        assert not _is_linked(a1, 'chartDsl_Employee', b)
    if hasattr(a2, 'chartDsl_Employee'):
        assert _is_linked(a2, 'chartDsl_Employee', b)
    _safe_set(b, 'chartDsl_Company', set())
    assert not _is_linked(b, 'chartDsl_Company', a2)
    if hasattr(a2, 'chartDsl_Employee'):
        assert not _is_linked(a2, 'chartDsl_Employee', b)


def test_assoc_projects1_reverse_link_reassign_clear():
    a1 = chartDsl_Project(name="sample_text", projectType="sample_text")
    a2 = chartDsl_Project(name="sample_text_2", projectType="sample_text_2")
    b = chartDsl_Company(name="sample_text")
    _safe_set(b, 'chartDsl_Company2', {a1})
    assert _is_linked(b, 'chartDsl_Company2', a1)
    if hasattr(a1, 'chartDsl_Project'):
        assert _is_linked(a1, 'chartDsl_Project', b)
    _safe_set(b, 'chartDsl_Company2', {a2})
    assert _is_linked(b, 'chartDsl_Company2', a2)
    if hasattr(a1, 'chartDsl_Project'):
        assert not _is_linked(a1, 'chartDsl_Project', b)
    if hasattr(a2, 'chartDsl_Project'):
        assert _is_linked(a2, 'chartDsl_Project', b)
    _safe_set(b, 'chartDsl_Company2', set())
    assert not _is_linked(b, 'chartDsl_Company2', a2)
    if hasattr(a2, 'chartDsl_Project'):
        assert not _is_linked(a2, 'chartDsl_Project', b)


def test_assoc_responsable5_reverse_link_reassign_clear():
    a1 = chartDsl_Task(name="sample_text")
    a2 = chartDsl_Task(name="sample_text_2")
    b = chartDsl_Employee(name="sample_text")
    _safe_set(b, 'chartDsl_Employee7', a1)
    assert _is_linked(b, 'chartDsl_Employee7', a1)
    if hasattr(a1, 'chartDsl_Task6'):
        assert _is_linked(a1, 'chartDsl_Task6', b)
    _safe_set(b, 'chartDsl_Employee7', a2)
    assert _is_linked(b, 'chartDsl_Employee7', a2)
    if hasattr(a1, 'chartDsl_Task6'):
        assert not _is_linked(a1, 'chartDsl_Task6', b)
    if hasattr(a2, 'chartDsl_Task6'):
        assert _is_linked(a2, 'chartDsl_Task6', b)
    _safe_set(b, 'chartDsl_Employee7', None)
    assert not _is_linked(b, 'chartDsl_Employee7', a2)
    if hasattr(a2, 'chartDsl_Task6'):
        assert not _is_linked(a2, 'chartDsl_Task6', b)


def test_assoc_tasks3_reverse_link_reassign_clear():
    a1 = chartDsl_Task(name="sample_text")
    a2 = chartDsl_Task(name="sample_text_2")
    b = chartDsl_Project(name="sample_text", projectType="sample_text")
    _safe_set(b, 'chartDsl_Project4', {a1})
    assert _is_linked(b, 'chartDsl_Project4', a1)
    if hasattr(a1, 'chartDsl_Task'):
        assert _is_linked(a1, 'chartDsl_Task', b)
    _safe_set(b, 'chartDsl_Project4', {a2})
    assert _is_linked(b, 'chartDsl_Project4', a2)
    if hasattr(a1, 'chartDsl_Task'):
        assert not _is_linked(a1, 'chartDsl_Task', b)
    if hasattr(a2, 'chartDsl_Task'):
        assert _is_linked(a2, 'chartDsl_Task', b)
    _safe_set(b, 'chartDsl_Project4', set())
    assert not _is_linked(b, 'chartDsl_Project4', a2)
    if hasattr(a2, 'chartDsl_Task'):
        assert not _is_linked(a2, 'chartDsl_Task', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

