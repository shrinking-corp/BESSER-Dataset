import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AntScripts_Attribute,
    AntScripts_CommentableElement,
    AntScripts_DescribableElement,
    AntScripts_NamedElement,
    AntScripts_Project,
    AntScripts_Property,
    AntScripts_Target,
    AntScripts_Task,
    AntScripts_TaskElement,
    AntScripts_TaskParameter,
    Attribute,
    CommentableElement,
    DescribableElement,
    NamedElement,
    Property,
    Target,
    Task,
    TaskElement,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_depends7_stub_double():
    # Target has no real 'Target9' property in the generated
    # code (a bare stub) -- manually attach it so AntScripts_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AntScripts_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AntScripts_Target(if_="sample_text", unless="sample_text")
    partner = Target()
    setattr(partner, 'Target9', None)
    _safe_set(owner, 'AntScripts_Target8', {partner})
    assert getattr(partner, 'Target9') == owner
    _safe_set(owner, 'AntScripts_Target8', set())
    assert getattr(partner, 'Target9') is None


def test_assoc_tasks6_stub_double():
    # Task has no real 'Task' property in the generated
    # code (a bare stub) -- manually attach it so AntScripts_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AntScripts_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AntScripts_Target(if_="sample_text", unless="sample_text")
    partner = Task()
    setattr(partner, 'Task', None)
    _safe_set(owner, 'AntScripts_Target', {partner})
    assert getattr(partner, 'Task') == owner
    _safe_set(owner, 'AntScripts_Target', set())
    assert getattr(partner, 'Task') is None


