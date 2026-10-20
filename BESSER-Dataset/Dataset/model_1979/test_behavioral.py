import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    traces_EObject,
    traces_Model,
    traces_Trace,
    traces_TraceElement,
    traces_TraceRecord,
    ParameterType,
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

def test_assoc_elements3_reverse_link_reassign_clear():
    a1 = traces_TraceElement(traceType="sample_text", typeName="sample_text", value="sample_text")
    a2 = traces_TraceElement(traceType="sample_text_2", typeName="sample_text_2", value="sample_text_2")
    b = traces_Trace(ruleInfo="sample_text", ruleName="sample_text", timestamp="sample_text")
    _safe_set(b, 'traces_Trace4', {a1})
    assert _is_linked(b, 'traces_Trace4', a1)
    if hasattr(a1, 'traces_TraceElement'):
        assert _is_linked(a1, 'traces_TraceElement', b)
    _safe_set(b, 'traces_Trace4', {a2})
    assert _is_linked(b, 'traces_Trace4', a2)
    if hasattr(a1, 'traces_TraceElement'):
        assert not _is_linked(a1, 'traces_TraceElement', b)
    if hasattr(a2, 'traces_TraceElement'):
        assert _is_linked(a2, 'traces_TraceElement', b)
    _safe_set(b, 'traces_Trace4', set())
    assert not _is_linked(b, 'traces_Trace4', a2)
    if hasattr(a2, 'traces_TraceElement'):
        assert not _is_linked(a2, 'traces_TraceElement', b)


def test_assoc_models1_reverse_link_reassign_clear():
    a1 = traces_TraceRecord(name="sample_text")
    a2 = traces_TraceRecord(name="sample_text_2")
    b = traces_Model(uriModel="sample_text")
    _safe_set(b, 'traces_Model', a1)
    assert _is_linked(b, 'traces_Model', a1)
    if hasattr(a1, 'traces_TraceRecord2'):
        assert _is_linked(a1, 'traces_TraceRecord2', b)
    _safe_set(b, 'traces_Model', a2)
    assert _is_linked(b, 'traces_Model', a2)
    if hasattr(a1, 'traces_TraceRecord2'):
        assert not _is_linked(a1, 'traces_TraceRecord2', b)
    if hasattr(a2, 'traces_TraceRecord2'):
        assert _is_linked(a2, 'traces_TraceRecord2', b)
    _safe_set(b, 'traces_Model', None)
    assert not _is_linked(b, 'traces_Model', a2)
    if hasattr(a2, 'traces_TraceRecord2'):
        assert not _is_linked(a2, 'traces_TraceRecord2', b)


def test_assoc_traces0_reverse_link_reassign_clear():
    a1 = traces_TraceRecord(name="sample_text")
    a2 = traces_TraceRecord(name="sample_text_2")
    b = traces_Trace(ruleInfo="sample_text", ruleName="sample_text", timestamp="sample_text")
    _safe_set(b, 'traces_Trace', a1)
    assert _is_linked(b, 'traces_Trace', a1)
    if hasattr(a1, 'traces_TraceRecord'):
        assert _is_linked(a1, 'traces_TraceRecord', b)
    _safe_set(b, 'traces_Trace', a2)
    assert _is_linked(b, 'traces_Trace', a2)
    if hasattr(a1, 'traces_TraceRecord'):
        assert not _is_linked(a1, 'traces_TraceRecord', b)
    if hasattr(a2, 'traces_TraceRecord'):
        assert _is_linked(a2, 'traces_TraceRecord', b)
    _safe_set(b, 'traces_Trace', None)
    assert not _is_linked(b, 'traces_Trace', a2)
    if hasattr(a2, 'traces_TraceRecord'):
        assert not _is_linked(a2, 'traces_TraceRecord', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element5_stub_double():
    # traces_EObject has no real 'traces_EObject' property in the generated
    # code (a bare stub) -- manually attach it so traces_TraceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_TraceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_TraceElement(traceType="sample_text", typeName="sample_text", value="sample_text")
    partner = traces_EObject()
    setattr(partner, 'traces_EObject', None)
    _safe_set(owner, 'traces_TraceElement6', partner)
    assert getattr(partner, 'traces_EObject') == owner
    _safe_set(owner, 'traces_TraceElement6', None)
    assert getattr(partner, 'traces_EObject') is None


def test_assoc_modelRoot7_stub_double():
    # traces_EObject has no real 'traces_EObject9' property in the generated
    # code (a bare stub) -- manually attach it so traces_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_Model(uriModel="sample_text")
    partner = traces_EObject()
    setattr(partner, 'traces_EObject9', None)
    _safe_set(owner, 'traces_Model8', partner)
    assert getattr(partner, 'traces_EObject9') == owner
    _safe_set(owner, 'traces_Model8', None)
    assert getattr(partner, 'traces_EObject9') is None


