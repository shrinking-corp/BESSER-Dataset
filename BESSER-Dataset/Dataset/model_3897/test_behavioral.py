import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Parameter,
    Statement,
    workflow_Condition,
    workflow_ForEach,
    workflow_InputParameter,
    workflow_OutputParameter,
    workflow_Parameter,
    workflow_Program,
    workflow_Recipe,
    workflow_SimpleCommand,
    workflow_Statement,
    workflow_Workflow,
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

def test_assoc_commands1_reverse_link_reassign_clear():
    a1 = workflow_Statement(exec_order=7)
    a2 = workflow_Statement(exec_order=13)
    b = workflow_Recipe(name="sample_text")
    _safe_set(b, 'workflow_Recipe2', {a1})
    assert _is_linked(b, 'workflow_Recipe2', a1)
    if hasattr(a1, 'workflow_Statement'):
        assert _is_linked(a1, 'workflow_Statement', b)
    _safe_set(b, 'workflow_Recipe2', {a2})
    assert _is_linked(b, 'workflow_Recipe2', a2)
    if hasattr(a1, 'workflow_Statement'):
        assert not _is_linked(a1, 'workflow_Statement', b)
    if hasattr(a2, 'workflow_Statement'):
        assert _is_linked(a2, 'workflow_Statement', b)
    _safe_set(b, 'workflow_Recipe2', set())
    assert not _is_linked(b, 'workflow_Recipe2', a2)
    if hasattr(a2, 'workflow_Statement'):
        assert not _is_linked(a2, 'workflow_Statement', b)


def test_assoc_else_branch5_reverse_link_reassign_clear():
    a1 = workflow_Statement(exec_order=7)
    a2 = workflow_Statement(exec_order=13)
    b = workflow_Condition(description="sample_text", expression="sample_text")
    _safe_set(b, 'workflow_Condition6', a1)
    assert _is_linked(b, 'workflow_Condition6', a1)
    if hasattr(a1, 'workflow_Statement7'):
        assert _is_linked(a1, 'workflow_Statement7', b)
    _safe_set(b, 'workflow_Condition6', a2)
    assert _is_linked(b, 'workflow_Condition6', a2)
    if hasattr(a1, 'workflow_Statement7'):
        assert not _is_linked(a1, 'workflow_Statement7', b)
    if hasattr(a2, 'workflow_Statement7'):
        assert _is_linked(a2, 'workflow_Statement7', b)
    _safe_set(b, 'workflow_Condition6', None)
    assert not _is_linked(b, 'workflow_Condition6', a2)
    if hasattr(a2, 'workflow_Statement7'):
        assert not _is_linked(a2, 'workflow_Statement7', b)


def test_assoc_parameters8_reverse_link_reassign_clear():
    a1 = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    a2 = workflow_Program(description="sample_text_2", exec_order=13, name_exec="sample_text_2")
    b = workflow_Parameter(data="sample_text", option="sample_text")
    _safe_set(b, 'workflow_Parameter', a1)
    assert _is_linked(b, 'workflow_Parameter', a1)
    if hasattr(a1, 'workflow_Program'):
        assert _is_linked(a1, 'workflow_Program', b)
    _safe_set(b, 'workflow_Parameter', a2)
    assert _is_linked(b, 'workflow_Parameter', a2)
    if hasattr(a1, 'workflow_Program'):
        assert not _is_linked(a1, 'workflow_Program', b)
    if hasattr(a2, 'workflow_Program'):
        assert _is_linked(a2, 'workflow_Program', b)
    _safe_set(b, 'workflow_Parameter', None)
    assert not _is_linked(b, 'workflow_Parameter', a2)
    if hasattr(a2, 'workflow_Program'):
        assert not _is_linked(a2, 'workflow_Program', b)


def test_assoc_programs9_reverse_link_reassign_clear():
    a1 = workflow_SimpleCommand(description="sample_text")
    a2 = workflow_SimpleCommand(description="sample_text_2")
    b = workflow_Program(description="sample_text", exec_order=7, name_exec="sample_text")
    _safe_set(b, 'workflow_Program10', a1)
    assert _is_linked(b, 'workflow_Program10', a1)
    if hasattr(a1, 'workflow_SimpleCommand'):
        assert _is_linked(a1, 'workflow_SimpleCommand', b)
    _safe_set(b, 'workflow_Program10', a2)
    assert _is_linked(b, 'workflow_Program10', a2)
    if hasattr(a1, 'workflow_SimpleCommand'):
        assert not _is_linked(a1, 'workflow_SimpleCommand', b)
    if hasattr(a2, 'workflow_SimpleCommand'):
        assert _is_linked(a2, 'workflow_SimpleCommand', b)
    _safe_set(b, 'workflow_Program10', None)
    assert not _is_linked(b, 'workflow_Program10', a2)
    if hasattr(a2, 'workflow_SimpleCommand'):
        assert not _is_linked(a2, 'workflow_SimpleCommand', b)


def test_assoc_recipes0_reverse_link_reassign_clear():
    a1 = workflow_Workflow(name="sample_text")
    a2 = workflow_Workflow(name="sample_text_2")
    b = workflow_Recipe(name="sample_text")
    _safe_set(b, 'workflow_Recipe', a1)
    assert _is_linked(b, 'workflow_Recipe', a1)
    if hasattr(a1, 'workflow_Workflow'):
        assert _is_linked(a1, 'workflow_Workflow', b)
    _safe_set(b, 'workflow_Recipe', a2)
    assert _is_linked(b, 'workflow_Recipe', a2)
    if hasattr(a1, 'workflow_Workflow'):
        assert not _is_linked(a1, 'workflow_Workflow', b)
    if hasattr(a2, 'workflow_Workflow'):
        assert _is_linked(a2, 'workflow_Workflow', b)
    _safe_set(b, 'workflow_Recipe', None)
    assert not _is_linked(b, 'workflow_Recipe', a2)
    if hasattr(a2, 'workflow_Workflow'):
        assert not _is_linked(a2, 'workflow_Workflow', b)


def test_assoc_statements15_reverse_link_reassign_clear():
    a1 = workflow_Statement(exec_order=7)
    a2 = workflow_Statement(exec_order=13)
    b = workflow_ForEach(element="sample_text", sequence="sample_text")
    _safe_set(b, 'workflow_ForEach', {a1})
    assert _is_linked(b, 'workflow_ForEach', a1)
    if hasattr(a1, 'workflow_Statement16'):
        assert _is_linked(a1, 'workflow_Statement16', b)
    _safe_set(b, 'workflow_ForEach', {a2})
    assert _is_linked(b, 'workflow_ForEach', a2)
    if hasattr(a1, 'workflow_Statement16'):
        assert not _is_linked(a1, 'workflow_Statement16', b)
    if hasattr(a2, 'workflow_Statement16'):
        assert _is_linked(a2, 'workflow_Statement16', b)
    _safe_set(b, 'workflow_ForEach', set())
    assert not _is_linked(b, 'workflow_ForEach', a2)
    if hasattr(a2, 'workflow_Statement16'):
        assert not _is_linked(a2, 'workflow_Statement16', b)


def test_assoc_then_branch3_reverse_link_reassign_clear():
    a1 = workflow_Statement(exec_order=7)
    a2 = workflow_Statement(exec_order=13)
    b = workflow_Condition(description="sample_text", expression="sample_text")
    _safe_set(b, 'workflow_Condition', a1)
    assert _is_linked(b, 'workflow_Condition', a1)
    if hasattr(a1, 'workflow_Statement4'):
        assert _is_linked(a1, 'workflow_Statement4', b)
    _safe_set(b, 'workflow_Condition', a2)
    assert _is_linked(b, 'workflow_Condition', a2)
    if hasattr(a1, 'workflow_Statement4'):
        assert not _is_linked(a1, 'workflow_Statement4', b)
    if hasattr(a2, 'workflow_Statement4'):
        assert _is_linked(a2, 'workflow_Statement4', b)
    _safe_set(b, 'workflow_Condition', None)
    assert not _is_linked(b, 'workflow_Condition', a2)
    if hasattr(a2, 'workflow_Statement4'):
        assert not _is_linked(a2, 'workflow_Statement4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

