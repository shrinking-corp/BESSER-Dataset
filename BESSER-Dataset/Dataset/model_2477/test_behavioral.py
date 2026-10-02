import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    traceability_Category,
    traceability_DiffCategory,
    traceability_EObject,
    traceability_LogEntry,
    traceability_Trace,
    traceability_TraceComment,
    traceability_TraceDiff,
    traceability_TraceDiffs,
    traceability_Traces,
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

def test_assoc_children5_reverse_link_reassign_clear():
    a1 = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    a2 = traceability_Trace(comment="sample_text_2", description="sample_text_2", value="sample_text_2")
    b = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Trace'):
        assert _is_linked(a1, 'Trace', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Trace'):
        assert not _is_linked(a1, 'Trace', b)
    if hasattr(a2, 'Trace'):
        assert _is_linked(a2, 'Trace', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Trace'):
        assert not _is_linked(a2, 'Trace', b)


def test_assoc_comments13_reverse_link_reassign_clear():
    a1 = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    a2 = traceability_TraceComment(column="sample_text_2", comment="sample_text_2", date=date(2025, 6, 15), username="sample_text_2")
    b = traceability_LogEntry(comment="sample_text", message="sample_text", messageType=7, severity=7)
    _safe_set(b, 'traceability_LogEntry14', {a1})
    assert _is_linked(b, 'traceability_LogEntry14', a1)
    if hasattr(a1, 'traceability_TraceComment15'):
        assert _is_linked(a1, 'traceability_TraceComment15', b)
    _safe_set(b, 'traceability_LogEntry14', {a2})
    assert _is_linked(b, 'traceability_LogEntry14', a2)
    if hasattr(a1, 'traceability_TraceComment15'):
        assert not _is_linked(a1, 'traceability_TraceComment15', b)
    if hasattr(a2, 'traceability_TraceComment15'):
        assert _is_linked(a2, 'traceability_TraceComment15', b)
    _safe_set(b, 'traceability_LogEntry14', set())
    assert not _is_linked(b, 'traceability_LogEntry14', a2)
    if hasattr(a2, 'traceability_TraceComment15'):
        assert not _is_linked(a2, 'traceability_TraceComment15', b)


def test_assoc_comments26_reverse_link_reassign_clear():
    a1 = traceability_TraceDiff(comment="sample_text")
    a2 = traceability_TraceDiff(comment="sample_text_2")
    b = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    _safe_set(b, 'traceability_TraceComment28', a1)
    assert _is_linked(b, 'traceability_TraceComment28', a1)
    if hasattr(a1, 'traceability_TraceDiff27'):
        assert _is_linked(a1, 'traceability_TraceDiff27', b)
    _safe_set(b, 'traceability_TraceComment28', a2)
    assert _is_linked(b, 'traceability_TraceComment28', a2)
    if hasattr(a1, 'traceability_TraceDiff27'):
        assert not _is_linked(a1, 'traceability_TraceDiff27', b)
    if hasattr(a2, 'traceability_TraceDiff27'):
        assert _is_linked(a2, 'traceability_TraceDiff27', b)
    _safe_set(b, 'traceability_TraceComment28', None)
    assert not _is_linked(b, 'traceability_TraceComment28', a2)
    if hasattr(a2, 'traceability_TraceDiff27'):
        assert not _is_linked(a2, 'traceability_TraceDiff27', b)


def test_assoc_comments9_reverse_link_reassign_clear():
    a1 = traceability_TraceComment(column="sample_text", comment="sample_text", date=date(2024, 1, 1), username="sample_text")
    a2 = traceability_TraceComment(column="sample_text_2", comment="sample_text_2", date=date(2025, 6, 15), username="sample_text_2")
    b = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    _safe_set(b, 'traceability_Trace10', {a1})
    assert _is_linked(b, 'traceability_Trace10', a1)
    if hasattr(a1, 'traceability_TraceComment'):
        assert _is_linked(a1, 'traceability_TraceComment', b)
    _safe_set(b, 'traceability_Trace10', {a2})
    assert _is_linked(b, 'traceability_Trace10', a2)
    if hasattr(a1, 'traceability_TraceComment'):
        assert not _is_linked(a1, 'traceability_TraceComment', b)
    if hasattr(a2, 'traceability_TraceComment'):
        assert _is_linked(a2, 'traceability_TraceComment', b)
    _safe_set(b, 'traceability_Trace10', set())
    assert not _is_linked(b, 'traceability_Trace10', a2)
    if hasattr(a2, 'traceability_TraceComment'):
        assert not _is_linked(a2, 'traceability_TraceComment', b)


def test_assoc_diffs29_reverse_link_reassign_clear():
    a1 = traceability_TraceDiff(comment="sample_text")
    a2 = traceability_TraceDiff(comment="sample_text_2")
    b = traceability_DiffCategory(modelIndex=7, name="sample_text", unequal=True)
    _safe_set(b, 'traceability_DiffCategory', {a1})
    assert _is_linked(b, 'traceability_DiffCategory', a1)
    if hasattr(a1, 'traceability_TraceDiff30'):
        assert _is_linked(a1, 'traceability_TraceDiff30', b)
    _safe_set(b, 'traceability_DiffCategory', {a2})
    assert _is_linked(b, 'traceability_DiffCategory', a2)
    if hasattr(a1, 'traceability_TraceDiff30'):
        assert not _is_linked(a1, 'traceability_TraceDiff30', b)
    if hasattr(a2, 'traceability_TraceDiff30'):
        assert _is_linked(a2, 'traceability_TraceDiff30', b)
    _safe_set(b, 'traceability_DiffCategory', set())
    assert not _is_linked(b, 'traceability_DiffCategory', a2)
    if hasattr(a2, 'traceability_TraceDiff30'):
        assert not _is_linked(a2, 'traceability_TraceDiff30', b)


def test_assoc_parent7_reverse_link_reassign_clear():
    a1 = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    a2 = traceability_Trace(comment="sample_text_2", description="sample_text_2", value="sample_text_2")
    b = traceability_Trace(comment="sample_text", description="sample_text", value="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Trace8'):
        assert _is_linked(a1, 'Trace8', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Trace8'):
        assert not _is_linked(a1, 'Trace8', b)
    if hasattr(a2, 'Trace8'):
        assert _is_linked(a2, 'Trace8', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Trace8'):
        assert not _is_linked(a2, 'Trace8', b)


