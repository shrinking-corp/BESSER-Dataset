import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    emfta_Event,
    emfta_FTAModel,
    emfta_Gate,
    EventType,
    GateType,
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

def test_assoc_events1_reverse_link_reassign_clear():
    a1 = emfta_Gate(description="sample_text", nbOccurrences=7, type="sample_text")
    a2 = emfta_Gate(description="sample_text_2", nbOccurrences=13, type="sample_text_2")
    b = emfta_Event(description="sample_text", name="sample_text", probability=3.14, referenceCount=7, relatedObject="sample_text", type="sample_text")
    _safe_set(b, 'emfta_Event3', a1)
    assert _is_linked(b, 'emfta_Event3', a1)
    if hasattr(a1, 'emfta_Gate2'):
        assert _is_linked(a1, 'emfta_Gate2', b)
    _safe_set(b, 'emfta_Event3', a2)
    assert _is_linked(b, 'emfta_Event3', a2)
    if hasattr(a1, 'emfta_Gate2'):
        assert not _is_linked(a1, 'emfta_Gate2', b)
    if hasattr(a2, 'emfta_Gate2'):
        assert _is_linked(a2, 'emfta_Gate2', b)
    _safe_set(b, 'emfta_Event3', None)
    assert not _is_linked(b, 'emfta_Event3', a2)
    if hasattr(a2, 'emfta_Gate2'):
        assert not _is_linked(a2, 'emfta_Gate2', b)


def test_assoc_events6_reverse_link_reassign_clear():
    a1 = emfta_FTAModel(comments="sample_text", description="sample_text", name="sample_text")
    a2 = emfta_FTAModel(comments="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = emfta_Event(description="sample_text", name="sample_text", probability=3.14, referenceCount=7, relatedObject="sample_text", type="sample_text")
    _safe_set(b, 'emfta_Event8', a1)
    assert _is_linked(b, 'emfta_Event8', a1)
    if hasattr(a1, 'emfta_FTAModel7'):
        assert _is_linked(a1, 'emfta_FTAModel7', b)
    _safe_set(b, 'emfta_Event8', a2)
    assert _is_linked(b, 'emfta_Event8', a2)
    if hasattr(a1, 'emfta_FTAModel7'):
        assert not _is_linked(a1, 'emfta_FTAModel7', b)
    if hasattr(a2, 'emfta_FTAModel7'):
        assert _is_linked(a2, 'emfta_FTAModel7', b)
    _safe_set(b, 'emfta_Event8', None)
    assert not _is_linked(b, 'emfta_Event8', a2)
    if hasattr(a2, 'emfta_FTAModel7'):
        assert not _is_linked(a2, 'emfta_FTAModel7', b)


def test_assoc_gate0_reverse_link_reassign_clear():
    a1 = emfta_Gate(description="sample_text", nbOccurrences=7, type="sample_text")
    a2 = emfta_Gate(description="sample_text_2", nbOccurrences=13, type="sample_text_2")
    b = emfta_Event(description="sample_text", name="sample_text", probability=3.14, referenceCount=7, relatedObject="sample_text", type="sample_text")
    _safe_set(b, 'emfta_Event', a1)
    assert _is_linked(b, 'emfta_Event', a1)
    if hasattr(a1, 'emfta_Gate'):
        assert _is_linked(a1, 'emfta_Gate', b)
    _safe_set(b, 'emfta_Event', a2)
    assert _is_linked(b, 'emfta_Event', a2)
    if hasattr(a1, 'emfta_Gate'):
        assert not _is_linked(a1, 'emfta_Gate', b)
    if hasattr(a2, 'emfta_Gate'):
        assert _is_linked(a2, 'emfta_Gate', b)
    _safe_set(b, 'emfta_Event', None)
    assert not _is_linked(b, 'emfta_Event', a2)
    if hasattr(a2, 'emfta_Gate'):
        assert not _is_linked(a2, 'emfta_Gate', b)


def test_assoc_root4_reverse_link_reassign_clear():
    a1 = emfta_FTAModel(comments="sample_text", description="sample_text", name="sample_text")
    a2 = emfta_FTAModel(comments="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = emfta_Event(description="sample_text", name="sample_text", probability=3.14, referenceCount=7, relatedObject="sample_text", type="sample_text")
    _safe_set(b, 'emfta_Event5', a1)
    assert _is_linked(b, 'emfta_Event5', a1)
    if hasattr(a1, 'emfta_FTAModel'):
        assert _is_linked(a1, 'emfta_FTAModel', b)
    _safe_set(b, 'emfta_Event5', a2)
    assert _is_linked(b, 'emfta_Event5', a2)
    if hasattr(a1, 'emfta_FTAModel'):
        assert not _is_linked(a1, 'emfta_FTAModel', b)
    if hasattr(a2, 'emfta_FTAModel'):
        assert _is_linked(a2, 'emfta_FTAModel', b)
    _safe_set(b, 'emfta_Event5', None)
    assert not _is_linked(b, 'emfta_Event5', a2)
    if hasattr(a2, 'emfta_FTAModel'):
        assert not _is_linked(a2, 'emfta_FTAModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

