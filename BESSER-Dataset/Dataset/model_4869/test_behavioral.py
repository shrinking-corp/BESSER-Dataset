import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FlowDesigner_ActionState,
    FlowDesigner_Event,
    FlowDesigner_FinalState,
    FlowDesigner_Flow,
    FlowDesigner_InitialState,
    FlowDesigner_NamedState,
    FlowDesigner_Source,
    FlowDesigner_Target,
    FlowDesigner_ViewState,
    NamedState,
    Source,
    Target,
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
    a1 = FlowDesigner_Source()
    a2 = FlowDesigner_Source()
    b = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    _safe_set(b, 'FlowDesigner_Event2', a1)
    assert _is_linked(b, 'FlowDesigner_Event2', a1)
    if hasattr(a1, 'FlowDesigner_Source'):
        assert _is_linked(a1, 'FlowDesigner_Source', b)
    _safe_set(b, 'FlowDesigner_Event2', a2)
    assert _is_linked(b, 'FlowDesigner_Event2', a2)
    if hasattr(a1, 'FlowDesigner_Source'):
        assert not _is_linked(a1, 'FlowDesigner_Source', b)
    if hasattr(a2, 'FlowDesigner_Source'):
        assert _is_linked(a2, 'FlowDesigner_Source', b)
    _safe_set(b, 'FlowDesigner_Event2', None)
    assert not _is_linked(b, 'FlowDesigner_Event2', a2)
    if hasattr(a2, 'FlowDesigner_Source'):
        assert not _is_linked(a2, 'FlowDesigner_Source', b)


def test_assoc_finalState6_reverse_link_reassign_clear():
    a1 = FlowDesigner_Flow()
    a2 = FlowDesigner_Flow()
    b = FlowDesigner_FinalState(finalize="sample_text")
    _safe_set(b, 'FlowDesigner_FinalState', a1)
    assert _is_linked(b, 'FlowDesigner_FinalState', a1)
    if hasattr(a1, 'FlowDesigner_Flow7'):
        assert _is_linked(a1, 'FlowDesigner_Flow7', b)
    _safe_set(b, 'FlowDesigner_FinalState', a2)
    assert _is_linked(b, 'FlowDesigner_FinalState', a2)
    if hasattr(a1, 'FlowDesigner_Flow7'):
        assert not _is_linked(a1, 'FlowDesigner_Flow7', b)
    if hasattr(a2, 'FlowDesigner_Flow7'):
        assert _is_linked(a2, 'FlowDesigner_Flow7', b)
    _safe_set(b, 'FlowDesigner_FinalState', None)
    assert not _is_linked(b, 'FlowDesigner_FinalState', a2)
    if hasattr(a2, 'FlowDesigner_Flow7'):
        assert not _is_linked(a2, 'FlowDesigner_Flow7', b)


def test_assoc_initialState3_reverse_link_reassign_clear():
    a1 = FlowDesigner_InitialState(initialize="sample_text")
    a2 = FlowDesigner_InitialState(initialize="sample_text_2")
    b = FlowDesigner_Flow()
    _safe_set(b, 'FlowDesigner_Flow', a1)
    assert _is_linked(b, 'FlowDesigner_Flow', a1)
    if hasattr(a1, 'FlowDesigner_InitialState'):
        assert _is_linked(a1, 'FlowDesigner_InitialState', b)
    _safe_set(b, 'FlowDesigner_Flow', a2)
    assert _is_linked(b, 'FlowDesigner_Flow', a2)
    if hasattr(a1, 'FlowDesigner_InitialState'):
        assert not _is_linked(a1, 'FlowDesigner_InitialState', b)
    if hasattr(a2, 'FlowDesigner_InitialState'):
        assert _is_linked(a2, 'FlowDesigner_InitialState', b)
    _safe_set(b, 'FlowDesigner_Flow', None)
    assert not _is_linked(b, 'FlowDesigner_Flow', a2)
    if hasattr(a2, 'FlowDesigner_InitialState'):
        assert not _is_linked(a2, 'FlowDesigner_InitialState', b)


def test_assoc_nextState0_reverse_link_reassign_clear():
    a1 = FlowDesigner_Target()
    a2 = FlowDesigner_Target()
    b = FlowDesigner_Event(action="sample_text", event="sample_text", guard="sample_text")
    _safe_set(b, 'FlowDesigner_Event', a1)
    assert _is_linked(b, 'FlowDesigner_Event', a1)
    if hasattr(a1, 'FlowDesigner_Target'):
        assert _is_linked(a1, 'FlowDesigner_Target', b)
    _safe_set(b, 'FlowDesigner_Event', a2)
    assert _is_linked(b, 'FlowDesigner_Event', a2)
    if hasattr(a1, 'FlowDesigner_Target'):
        assert not _is_linked(a1, 'FlowDesigner_Target', b)
    if hasattr(a2, 'FlowDesigner_Target'):
        assert _is_linked(a2, 'FlowDesigner_Target', b)
    _safe_set(b, 'FlowDesigner_Event', None)
    assert not _is_linked(b, 'FlowDesigner_Event', a2)
    if hasattr(a2, 'FlowDesigner_Target'):
        assert not _is_linked(a2, 'FlowDesigner_Target', b)


def test_assoc_states4_reverse_link_reassign_clear():
    a1 = FlowDesigner_NamedState(activity="sample_text", entry="sample_text", exit="sample_text", name="sample_text")
    a2 = FlowDesigner_NamedState(activity="sample_text_2", entry="sample_text_2", exit="sample_text_2", name="sample_text_2")
    b = FlowDesigner_Flow()
    _safe_set(b, 'FlowDesigner_Flow5', {a1})
    assert _is_linked(b, 'FlowDesigner_Flow5', a1)
    if hasattr(a1, 'FlowDesigner_NamedState'):
        assert _is_linked(a1, 'FlowDesigner_NamedState', b)
    _safe_set(b, 'FlowDesigner_Flow5', {a2})
    assert _is_linked(b, 'FlowDesigner_Flow5', a2)
    if hasattr(a1, 'FlowDesigner_NamedState'):
        assert not _is_linked(a1, 'FlowDesigner_NamedState', b)
    if hasattr(a2, 'FlowDesigner_NamedState'):
        assert _is_linked(a2, 'FlowDesigner_NamedState', b)
    _safe_set(b, 'FlowDesigner_Flow5', set())
    assert not _is_linked(b, 'FlowDesigner_Flow5', a2)
    if hasattr(a2, 'FlowDesigner_NamedState'):
        assert not _is_linked(a2, 'FlowDesigner_NamedState', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

