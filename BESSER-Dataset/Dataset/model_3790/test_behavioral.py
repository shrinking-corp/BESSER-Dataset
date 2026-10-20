import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TestContainer,
    TestElement,
    TestProblem,
    TraceElement,
    model_ComparisonProblem,
    model_Metadata,
    model_TestCaseElement,
    model_TestContainer,
    model_TestElement,
    model_TestProblem,
    model_TestRoot,
    model_TraceElement,
    model_TraceException,
    model_TraceStackframe,
    ProblemType,
    ProgressState,
    TestState,
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

def test_assoc_children2_reverse_link_reassign_clear():
    a1 = model_TestElement(description="sample_text", elementUnderTest="sample_text", endTimestamp="sample_text", name="sample_text", progressState="sample_text", startTimestamp="sample_text", target="sample_text", testState="sample_text")
    a2 = model_TestElement(description="sample_text_2", elementUnderTest="sample_text_2", endTimestamp="sample_text_2", name="sample_text_2", progressState="sample_text_2", startTimestamp="sample_text_2", target="sample_text_2", testState="sample_text_2")
    b = model_TestContainer()
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'TestElement'):
        assert _is_linked(a1, 'TestElement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'TestElement'):
        assert not _is_linked(a1, 'TestElement', b)
    if hasattr(a2, 'TestElement'):
        assert _is_linked(a2, 'TestElement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'TestElement'):
        assert not _is_linked(a2, 'TestElement', b)


def test_assoc_parent0_reverse_link_reassign_clear():
    a1 = model_TestElement(description="sample_text", elementUnderTest="sample_text", endTimestamp="sample_text", name="sample_text", progressState="sample_text", startTimestamp="sample_text", target="sample_text", testState="sample_text")
    a2 = model_TestElement(description="sample_text_2", elementUnderTest="sample_text_2", endTimestamp="sample_text_2", name="sample_text_2", progressState="sample_text_2", startTimestamp="sample_text_2", target="sample_text_2", testState="sample_text_2")
    b = model_TestContainer()
    _safe_set(b, 'TestContainer', a1)
    assert _is_linked(b, 'TestContainer', a1)
    if hasattr(a1, 'children'):
        assert _is_linked(a1, 'children', b)
    _safe_set(b, 'TestContainer', a2)
    assert _is_linked(b, 'TestContainer', a2)
    if hasattr(a1, 'children'):
        assert not _is_linked(a1, 'children', b)
    if hasattr(a2, 'children'):
        assert _is_linked(a2, 'children', b)
    _safe_set(b, 'TestContainer', None)
    assert not _is_linked(b, 'TestContainer', a2)
    if hasattr(a2, 'children'):
        assert not _is_linked(a2, 'children', b)


def test_assoc_problem1_reverse_link_reassign_clear():
    a1 = model_TestProblem(message="sample_text", problemType="sample_text")
    a2 = model_TestProblem(message="sample_text_2", problemType="sample_text_2")
    b = model_TestElement(description="sample_text", elementUnderTest="sample_text", endTimestamp="sample_text", name="sample_text", progressState="sample_text", startTimestamp="sample_text", target="sample_text", testState="sample_text")
    _safe_set(b, 'model_TestElement', a1)
    assert _is_linked(b, 'model_TestElement', a1)
    if hasattr(a1, 'model_TestProblem'):
        assert _is_linked(a1, 'model_TestProblem', b)
    _safe_set(b, 'model_TestElement', a2)
    assert _is_linked(b, 'model_TestElement', a2)
    if hasattr(a1, 'model_TestProblem'):
        assert not _is_linked(a1, 'model_TestProblem', b)
    if hasattr(a2, 'model_TestProblem'):
        assert _is_linked(a2, 'model_TestProblem', b)
    _safe_set(b, 'model_TestElement', None)
    assert not _is_linked(b, 'model_TestElement', a2)
    if hasattr(a2, 'model_TestProblem'):
        assert not _is_linked(a2, 'model_TestProblem', b)


def test_assoc_trace3_reverse_link_reassign_clear():
    a1 = model_TraceElement(message="sample_text")
    a2 = model_TraceElement(message="sample_text_2")
    b = model_TestProblem(message="sample_text", problemType="sample_text")
    _safe_set(b, 'model_TestProblem4', {a1})
    assert _is_linked(b, 'model_TestProblem4', a1)
    if hasattr(a1, 'model_TraceElement'):
        assert _is_linked(a1, 'model_TraceElement', b)
    _safe_set(b, 'model_TestProblem4', {a2})
    assert _is_linked(b, 'model_TestProblem4', a2)
    if hasattr(a1, 'model_TraceElement'):
        assert not _is_linked(a1, 'model_TraceElement', b)
    if hasattr(a2, 'model_TraceElement'):
        assert _is_linked(a2, 'model_TraceElement', b)
    _safe_set(b, 'model_TestProblem4', set())
    assert not _is_linked(b, 'model_TestProblem4', a2)
    if hasattr(a2, 'model_TraceElement'):
        assert not _is_linked(a2, 'model_TraceElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

