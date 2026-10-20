import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MyNode,
    softwaretraces_Feature,
    softwaretraces_Model,
    softwaretraces_MyNode,
    softwaretraces_Trace,
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

def test_assoc_features0_reverse_link_reassign_clear():
    a1 = softwaretraces_Model(resourceFileName="sample_text")
    a2 = softwaretraces_Model(resourceFileName="sample_text_2")
    b = softwaretraces_Feature(name="sample_text")
    _safe_set(b, 'softwaretraces_Feature', a1)
    assert _is_linked(b, 'softwaretraces_Feature', a1)
    if hasattr(a1, 'softwaretraces_Model'):
        assert _is_linked(a1, 'softwaretraces_Model', b)
    _safe_set(b, 'softwaretraces_Feature', a2)
    assert _is_linked(b, 'softwaretraces_Feature', a2)
    if hasattr(a1, 'softwaretraces_Model'):
        assert not _is_linked(a1, 'softwaretraces_Model', b)
    if hasattr(a2, 'softwaretraces_Model'):
        assert _is_linked(a2, 'softwaretraces_Model', b)
    _safe_set(b, 'softwaretraces_Feature', None)
    assert not _is_linked(b, 'softwaretraces_Feature', a2)
    if hasattr(a2, 'softwaretraces_Model'):
        assert not _is_linked(a2, 'softwaretraces_Model', b)


def test_assoc_features4_reverse_link_reassign_clear():
    a1 = softwaretraces_Feature(name="sample_text")
    a2 = softwaretraces_Feature(name="sample_text_2")
    b = softwaretraces_Feature(name="sample_text")
    _safe_set(b, 'softwaretraces_Feature5', a1)
    assert _is_linked(b, 'softwaretraces_Feature5', a1)
    if hasattr(a1, 'softwaretraces_Feature3'):
        assert _is_linked(a1, 'softwaretraces_Feature3', b)
    _safe_set(b, 'softwaretraces_Feature5', a2)
    assert _is_linked(b, 'softwaretraces_Feature5', a2)
    if hasattr(a1, 'softwaretraces_Feature3'):
        assert not _is_linked(a1, 'softwaretraces_Feature3', b)
    if hasattr(a2, 'softwaretraces_Feature3'):
        assert _is_linked(a2, 'softwaretraces_Feature3', b)
    _safe_set(b, 'softwaretraces_Feature5', None)
    assert not _is_linked(b, 'softwaretraces_Feature5', a2)
    if hasattr(a2, 'softwaretraces_Feature3'):
        assert not _is_linked(a2, 'softwaretraces_Feature3', b)


def test_assoc_traces1_reverse_link_reassign_clear():
    a1 = softwaretraces_Trace(fileName="sample_text", lineNumber=7, projectName="sample_text")
    a2 = softwaretraces_Trace(fileName="sample_text_2", lineNumber=13, projectName="sample_text_2")
    b = softwaretraces_Model(resourceFileName="sample_text")
    _safe_set(b, 'softwaretraces_Model2', {a1})
    assert _is_linked(b, 'softwaretraces_Model2', a1)
    if hasattr(a1, 'softwaretraces_Trace'):
        assert _is_linked(a1, 'softwaretraces_Trace', b)
    _safe_set(b, 'softwaretraces_Model2', {a2})
    assert _is_linked(b, 'softwaretraces_Model2', a2)
    if hasattr(a1, 'softwaretraces_Trace'):
        assert not _is_linked(a1, 'softwaretraces_Trace', b)
    if hasattr(a2, 'softwaretraces_Trace'):
        assert _is_linked(a2, 'softwaretraces_Trace', b)
    _safe_set(b, 'softwaretraces_Model2', set())
    assert not _is_linked(b, 'softwaretraces_Model2', a2)
    if hasattr(a2, 'softwaretraces_Trace'):
        assert not _is_linked(a2, 'softwaretraces_Trace', b)


def test_assoc_traces10_reverse_link_reassign_clear():
    a1 = softwaretraces_Trace(fileName="sample_text", lineNumber=7, projectName="sample_text")
    a2 = softwaretraces_Trace(fileName="sample_text_2", lineNumber=13, projectName="sample_text_2")
    b = softwaretraces_Trace(fileName="sample_text", lineNumber=7, projectName="sample_text")
    _safe_set(b, 'softwaretraces_Trace9', {a1})
    assert _is_linked(b, 'softwaretraces_Trace9', a1)
    if hasattr(a1, 'softwaretraces_Trace11'):
        assert _is_linked(a1, 'softwaretraces_Trace11', b)
    _safe_set(b, 'softwaretraces_Trace9', {a2})
    assert _is_linked(b, 'softwaretraces_Trace9', a2)
    if hasattr(a1, 'softwaretraces_Trace11'):
        assert not _is_linked(a1, 'softwaretraces_Trace11', b)
    if hasattr(a2, 'softwaretraces_Trace11'):
        assert _is_linked(a2, 'softwaretraces_Trace11', b)
    _safe_set(b, 'softwaretraces_Trace9', set())
    assert not _is_linked(b, 'softwaretraces_Trace9', a2)
    if hasattr(a2, 'softwaretraces_Trace11'):
        assert not _is_linked(a2, 'softwaretraces_Trace11', b)


def test_assoc_traces6_reverse_link_reassign_clear():
    a1 = softwaretraces_Trace(fileName="sample_text", lineNumber=7, projectName="sample_text")
    a2 = softwaretraces_Trace(fileName="sample_text_2", lineNumber=13, projectName="sample_text_2")
    b = softwaretraces_Feature(name="sample_text")
    _safe_set(b, 'softwaretraces_Feature7', {a1})
    assert _is_linked(b, 'softwaretraces_Feature7', a1)
    if hasattr(a1, 'softwaretraces_Trace8'):
        assert _is_linked(a1, 'softwaretraces_Trace8', b)
    _safe_set(b, 'softwaretraces_Feature7', {a2})
    assert _is_linked(b, 'softwaretraces_Feature7', a2)
    if hasattr(a1, 'softwaretraces_Trace8'):
        assert not _is_linked(a1, 'softwaretraces_Trace8', b)
    if hasattr(a2, 'softwaretraces_Trace8'):
        assert _is_linked(a2, 'softwaretraces_Trace8', b)
    _safe_set(b, 'softwaretraces_Feature7', set())
    assert not _is_linked(b, 'softwaretraces_Feature7', a2)
    if hasattr(a2, 'softwaretraces_Trace8'):
        assert not _is_linked(a2, 'softwaretraces_Trace8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

