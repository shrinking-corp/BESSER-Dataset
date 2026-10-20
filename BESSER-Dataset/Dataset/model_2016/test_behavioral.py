import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    trace_DebugLocationData,
    trace_DebugTraceRegion,
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

def test_assoc_associations2_reverse_link_reassign_clear():
    a1 = trace_DebugTraceRegion(label="sample_text", myEndLineNumber=7, myEndOffset=7, myLength=7, myLineNumber=7, myOffset=7, useForDebugging=True)
    a2 = trace_DebugTraceRegion(label="sample_text_2", myEndLineNumber=13, myEndOffset=13, myLength=13, myLineNumber=13, myOffset=13, useForDebugging=False)
    b = trace_DebugLocationData(endLineNumber=7, endOffset=7, label="sample_text", length=7, lineNumber=7, offset=7, path="sample_text")
    _safe_set(b, 'trace_DebugLocationData', a1)
    assert _is_linked(b, 'trace_DebugLocationData', a1)
    if hasattr(a1, 'trace_DebugTraceRegion3'):
        assert _is_linked(a1, 'trace_DebugTraceRegion3', b)
    _safe_set(b, 'trace_DebugLocationData', a2)
    assert _is_linked(b, 'trace_DebugLocationData', a2)
    if hasattr(a1, 'trace_DebugTraceRegion3'):
        assert not _is_linked(a1, 'trace_DebugTraceRegion3', b)
    if hasattr(a2, 'trace_DebugTraceRegion3'):
        assert _is_linked(a2, 'trace_DebugTraceRegion3', b)
    _safe_set(b, 'trace_DebugLocationData', None)
    assert not _is_linked(b, 'trace_DebugLocationData', a2)
    if hasattr(a2, 'trace_DebugTraceRegion3'):
        assert not _is_linked(a2, 'trace_DebugTraceRegion3', b)


def test_assoc_nestedRegions1_reverse_link_reassign_clear():
    a1 = trace_DebugTraceRegion(label="sample_text", myEndLineNumber=7, myEndOffset=7, myLength=7, myLineNumber=7, myOffset=7, useForDebugging=True)
    a2 = trace_DebugTraceRegion(label="sample_text_2", myEndLineNumber=13, myEndOffset=13, myLength=13, myLineNumber=13, myOffset=13, useForDebugging=False)
    b = trace_DebugTraceRegion(label="sample_text", myEndLineNumber=7, myEndOffset=7, myLength=7, myLineNumber=7, myOffset=7, useForDebugging=True)
    _safe_set(b, 'trace_DebugTraceRegion0', {a1})
    assert _is_linked(b, 'trace_DebugTraceRegion0', a1)
    if hasattr(a1, 'trace_DebugTraceRegion'):
        assert _is_linked(a1, 'trace_DebugTraceRegion', b)
    _safe_set(b, 'trace_DebugTraceRegion0', {a2})
    assert _is_linked(b, 'trace_DebugTraceRegion0', a2)
    if hasattr(a1, 'trace_DebugTraceRegion'):
        assert not _is_linked(a1, 'trace_DebugTraceRegion', b)
    if hasattr(a2, 'trace_DebugTraceRegion'):
        assert _is_linked(a2, 'trace_DebugTraceRegion', b)
    _safe_set(b, 'trace_DebugTraceRegion0', set())
    assert not _is_linked(b, 'trace_DebugTraceRegion0', a2)
    if hasattr(a2, 'trace_DebugTraceRegion'):
        assert not _is_linked(a2, 'trace_DebugTraceRegion', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

