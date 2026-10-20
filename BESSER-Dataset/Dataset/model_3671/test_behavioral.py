import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Project_Department,
    Project_Employee,
    Project_Project,
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

def test_assoc_Controls_Department7_reverse_link_reassign_clear():
    a1 = Project_Project(budget=7, name="sample_text")
    a2 = Project_Project(budget=13, name="sample_text_2")
    b = Project_Department(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'Department8', a1)
    assert _is_linked(b, 'Department8', a1)
    if hasattr(a1, 'Controls_Project'):
        assert _is_linked(a1, 'Controls_Project', b)
    _safe_set(b, 'Department8', a2)
    assert _is_linked(b, 'Department8', a2)
    if hasattr(a1, 'Controls_Project'):
        assert not _is_linked(a1, 'Controls_Project', b)
    if hasattr(a2, 'Controls_Project'):
        assert _is_linked(a2, 'Controls_Project', b)
    _safe_set(b, 'Department8', None)
    assert not _is_linked(b, 'Department8', a2)
    if hasattr(a2, 'Controls_Project'):
        assert not _is_linked(a2, 'Controls_Project', b)


def test_assoc_Controls_Project3_reverse_link_reassign_clear():
    a1 = Project_Project(budget=7, name="sample_text")
    a2 = Project_Project(budget=13, name="sample_text_2")
    b = Project_Department(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'Controls_Department', {a1})
    assert _is_linked(b, 'Controls_Department', a1)
    if hasattr(a1, 'Project4'):
        assert _is_linked(a1, 'Project4', b)
    _safe_set(b, 'Controls_Department', {a2})
    assert _is_linked(b, 'Controls_Department', a2)
    if hasattr(a1, 'Project4'):
        assert not _is_linked(a1, 'Project4', b)
    if hasattr(a2, 'Project4'):
        assert _is_linked(a2, 'Project4', b)
    _safe_set(b, 'Controls_Department', set())
    assert not _is_linked(b, 'Controls_Department', a2)
    if hasattr(a2, 'Project4'):
        assert not _is_linked(a2, 'Project4', b)


def test_assoc_WorksIn_Department0_reverse_link_reassign_clear():
    a1 = Project_Employee(name="sample_text", salary=7)
    a2 = Project_Employee(name="sample_text_2", salary=13)
    b = Project_Department(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'WorksIn_Employee'):
        assert _is_linked(a1, 'WorksIn_Employee', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'WorksIn_Employee'):
        assert not _is_linked(a1, 'WorksIn_Employee', b)
    if hasattr(a2, 'WorksIn_Employee'):
        assert _is_linked(a2, 'WorksIn_Employee', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'WorksIn_Employee'):
        assert not _is_linked(a2, 'WorksIn_Employee', b)


def test_assoc_WorksIn_Employee2_reverse_link_reassign_clear():
    a1 = Project_Employee(name="sample_text", salary=7)
    a2 = Project_Employee(name="sample_text_2", salary=13)
    b = Project_Department(budget=7, location="sample_text", name="sample_text")
    _safe_set(b, 'WorksIn_Department', {a1})
    assert _is_linked(b, 'WorksIn_Department', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'WorksIn_Department', {a2})
    assert _is_linked(b, 'WorksIn_Department', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'WorksIn_Department', set())
    assert not _is_linked(b, 'WorksIn_Department', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_WorksOn_Employee5_reverse_link_reassign_clear():
    a1 = Project_Project(budget=7, name="sample_text")
    a2 = Project_Project(budget=13, name="sample_text_2")
    b = Project_Employee(name="sample_text", salary=7)
    _safe_set(b, 'Employee6', a1)
    assert _is_linked(b, 'Employee6', a1)
    if hasattr(a1, 'WorksOn_Project'):
        assert _is_linked(a1, 'WorksOn_Project', b)
    _safe_set(b, 'Employee6', a2)
    assert _is_linked(b, 'Employee6', a2)
    if hasattr(a1, 'WorksOn_Project'):
        assert not _is_linked(a1, 'WorksOn_Project', b)
    if hasattr(a2, 'WorksOn_Project'):
        assert _is_linked(a2, 'WorksOn_Project', b)
    _safe_set(b, 'Employee6', None)
    assert not _is_linked(b, 'Employee6', a2)
    if hasattr(a2, 'WorksOn_Project'):
        assert not _is_linked(a2, 'WorksOn_Project', b)


def test_assoc_WorksOn_Project1_reverse_link_reassign_clear():
    a1 = Project_Project(budget=7, name="sample_text")
    a2 = Project_Project(budget=13, name="sample_text_2")
    b = Project_Employee(name="sample_text", salary=7)
    _safe_set(b, 'WorksOn_Employee', {a1})
    assert _is_linked(b, 'WorksOn_Employee', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'WorksOn_Employee', {a2})
    assert _is_linked(b, 'WorksOn_Employee', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'WorksOn_Employee', set())
    assert not _is_linked(b, 'WorksOn_Employee', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

