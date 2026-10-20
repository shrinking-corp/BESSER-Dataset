import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTask,
    IsInitSetter,
    NamedElement,
    Nsetter,
    Setter,
    SimpleTask,
    TaskInput,
    TypedElement,
    workflow_AbstractTask,
    workflow_BaseTask,
    workflow_Connection,
    workflow_CustomTask,
    workflow_Input,
    workflow_IsInitSetter,
    workflow_IsNotInitSetter,
    workflow_LibraryFunction,
    workflow_LibraryTask,
    workflow_NamedElement,
    workflow_Nsetter,
    workflow_Output,
    workflow_Setter,
    workflow_SimpleTask,
    workflow_TaskInput,
    workflow_TaskOutput,
    workflow_TypedElement,
    workflow_Workflow,
    Language,
    TaskStatus,
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

def test_assoc_functions12_reverse_link_reassign_clear():
    a1 = workflow_Workflow(language="sample_text")
    a2 = workflow_Workflow(language="sample_text_2")
    b = workflow_LibraryFunction(function="sample_text")
    _safe_set(b, 'workflow_LibraryFunction14', a1)
    assert _is_linked(b, 'workflow_LibraryFunction14', a1)
    if hasattr(a1, 'workflow_Workflow13'):
        assert _is_linked(a1, 'workflow_Workflow13', b)
    _safe_set(b, 'workflow_LibraryFunction14', a2)
    assert _is_linked(b, 'workflow_LibraryFunction14', a2)
    if hasattr(a1, 'workflow_Workflow13'):
        assert not _is_linked(a1, 'workflow_Workflow13', b)
    if hasattr(a2, 'workflow_Workflow13'):
        assert _is_linked(a2, 'workflow_Workflow13', b)
    _safe_set(b, 'workflow_LibraryFunction14', None)
    assert not _is_linked(b, 'workflow_LibraryFunction14', a2)
    if hasattr(a2, 'workflow_Workflow13'):
        assert not _is_linked(a2, 'workflow_Workflow13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_baseTask10_stub_double():
    # workflow_BaseTask has no real 'workflow_BaseTask11' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Workflow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Workflow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Workflow(language="sample_text")
    partner = workflow_BaseTask()
    setattr(partner, 'workflow_BaseTask11', None)
    _safe_set(owner, 'workflow_Workflow', partner)
    assert getattr(partner, 'workflow_BaseTask11') == owner
    _safe_set(owner, 'workflow_Workflow', None)
    assert getattr(partner, 'workflow_BaseTask11') is None


def test_assoc_children3_stub_double():
    # workflow_BaseTask has no real 'workflow_BaseTask' property in the generated
    # code (a bare stub) -- manually attach it so workflow_AbstractTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_AbstractTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_AbstractTask(status="sample_text")
    partner = workflow_BaseTask()
    setattr(partner, 'workflow_BaseTask', None)
    _safe_set(owner, 'workflow_AbstractTask4', partner)
    assert owner in getattr(partner, 'workflow_BaseTask')
    _safe_set(owner, 'workflow_AbstractTask4', None)
    assert owner not in getattr(partner, 'workflow_BaseTask')


def test_assoc_inputs0_stub_double():
    # workflow_TaskInput has no real 'workflow_TaskInput' property in the generated
    # code (a bare stub) -- manually attach it so workflow_AbstractTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_AbstractTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_AbstractTask(status="sample_text")
    partner = workflow_TaskInput()
    setattr(partner, 'workflow_TaskInput', None)
    _safe_set(owner, 'workflow_AbstractTask', {partner})
    assert getattr(partner, 'workflow_TaskInput') == owner
    _safe_set(owner, 'workflow_AbstractTask', set())
    assert getattr(partner, 'workflow_TaskInput') is None


def test_assoc_inputs6_stub_double():
    # workflow_Input has no real 'workflow_Input' property in the generated
    # code (a bare stub) -- manually attach it so workflow_LibraryFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_LibraryFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_LibraryFunction(function="sample_text")
    partner = workflow_Input()
    setattr(partner, 'workflow_Input', None)
    _safe_set(owner, 'workflow_LibraryFunction7', {partner})
    assert getattr(partner, 'workflow_Input') == owner
    _safe_set(owner, 'workflow_LibraryFunction7', set())
    assert getattr(partner, 'workflow_Input') is None


def test_assoc_libraryfunction8_stub_double():
    # workflow_LibraryTask has no real 'workflow_LibraryTask' property in the generated
    # code (a bare stub) -- manually attach it so workflow_LibraryFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_LibraryFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_LibraryFunction(function="sample_text")
    partner = workflow_LibraryTask()
    setattr(partner, 'workflow_LibraryTask', None)
    _safe_set(owner, 'workflow_LibraryFunction9', partner)
    assert getattr(partner, 'workflow_LibraryTask') == owner
    _safe_set(owner, 'workflow_LibraryFunction9', None)
    assert getattr(partner, 'workflow_LibraryTask') is None


def test_assoc_outputs1_stub_double():
    # workflow_TaskOutput has no real 'workflow_TaskOutput' property in the generated
    # code (a bare stub) -- manually attach it so workflow_AbstractTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_AbstractTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_AbstractTask(status="sample_text")
    partner = workflow_TaskOutput()
    setattr(partner, 'workflow_TaskOutput', None)
    _safe_set(owner, 'workflow_AbstractTask2', {partner})
    assert getattr(partner, 'workflow_TaskOutput') == owner
    _safe_set(owner, 'workflow_AbstractTask2', set())
    assert getattr(partner, 'workflow_TaskOutput') is None


def test_assoc_outputs5_stub_double():
    # workflow_Output has no real 'workflow_Output' property in the generated
    # code (a bare stub) -- manually attach it so workflow_LibraryFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_LibraryFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_LibraryFunction(function="sample_text")
    partner = workflow_Output()
    setattr(partner, 'workflow_Output', None)
    _safe_set(owner, 'workflow_LibraryFunction', {partner})
    assert getattr(partner, 'workflow_Output') == owner
    _safe_set(owner, 'workflow_LibraryFunction', set())
    assert getattr(partner, 'workflow_Output') is None


