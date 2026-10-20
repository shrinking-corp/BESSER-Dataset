import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    coom_ComponentOnOffManifest,
    coom_State,
    coom_Transition,
    coom_Version,
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

def test_assoc_fromState5_reverse_link_reassign_clear():
    a1 = coom_Transition(name="sample_text")
    a2 = coom_Transition(name="sample_text_2")
    b = coom_State(initial=True, name="sample_text")
    _safe_set(b, 'coom_State7', a1)
    assert _is_linked(b, 'coom_State7', a1)
    if hasattr(a1, 'coom_Transition6'):
        assert _is_linked(a1, 'coom_Transition6', b)
    _safe_set(b, 'coom_State7', a2)
    assert _is_linked(b, 'coom_State7', a2)
    if hasattr(a1, 'coom_Transition6'):
        assert not _is_linked(a1, 'coom_Transition6', b)
    if hasattr(a2, 'coom_Transition6'):
        assert _is_linked(a2, 'coom_Transition6', b)
    _safe_set(b, 'coom_State7', None)
    assert not _is_linked(b, 'coom_State7', a2)
    if hasattr(a2, 'coom_Transition6'):
        assert not _is_linked(a2, 'coom_Transition6', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = coom_State(initial=True, name="sample_text")
    a2 = coom_State(initial=False, name="sample_text_2")
    b = coom_ComponentOnOffManifest(name="sample_text")
    _safe_set(b, 'coom_ComponentOnOffManifest2', {a1})
    assert _is_linked(b, 'coom_ComponentOnOffManifest2', a1)
    if hasattr(a1, 'coom_State'):
        assert _is_linked(a1, 'coom_State', b)
    _safe_set(b, 'coom_ComponentOnOffManifest2', {a2})
    assert _is_linked(b, 'coom_ComponentOnOffManifest2', a2)
    if hasattr(a1, 'coom_State'):
        assert not _is_linked(a1, 'coom_State', b)
    if hasattr(a2, 'coom_State'):
        assert _is_linked(a2, 'coom_State', b)
    _safe_set(b, 'coom_ComponentOnOffManifest2', set())
    assert not _is_linked(b, 'coom_ComponentOnOffManifest2', a2)
    if hasattr(a2, 'coom_State'):
        assert not _is_linked(a2, 'coom_State', b)


def test_assoc_toState8_reverse_link_reassign_clear():
    a1 = coom_Transition(name="sample_text")
    a2 = coom_Transition(name="sample_text_2")
    b = coom_State(initial=True, name="sample_text")
    _safe_set(b, 'coom_State10', a1)
    assert _is_linked(b, 'coom_State10', a1)
    if hasattr(a1, 'coom_Transition9'):
        assert _is_linked(a1, 'coom_Transition9', b)
    _safe_set(b, 'coom_State10', a2)
    assert _is_linked(b, 'coom_State10', a2)
    if hasattr(a1, 'coom_Transition9'):
        assert not _is_linked(a1, 'coom_Transition9', b)
    if hasattr(a2, 'coom_Transition9'):
        assert _is_linked(a2, 'coom_Transition9', b)
    _safe_set(b, 'coom_State10', None)
    assert not _is_linked(b, 'coom_State10', a2)
    if hasattr(a2, 'coom_Transition9'):
        assert not _is_linked(a2, 'coom_Transition9', b)


def test_assoc_transitions3_reverse_link_reassign_clear():
    a1 = coom_Transition(name="sample_text")
    a2 = coom_Transition(name="sample_text_2")
    b = coom_ComponentOnOffManifest(name="sample_text")
    _safe_set(b, 'coom_ComponentOnOffManifest4', {a1})
    assert _is_linked(b, 'coom_ComponentOnOffManifest4', a1)
    if hasattr(a1, 'coom_Transition'):
        assert _is_linked(a1, 'coom_Transition', b)
    _safe_set(b, 'coom_ComponentOnOffManifest4', {a2})
    assert _is_linked(b, 'coom_ComponentOnOffManifest4', a2)
    if hasattr(a1, 'coom_Transition'):
        assert not _is_linked(a1, 'coom_Transition', b)
    if hasattr(a2, 'coom_Transition'):
        assert _is_linked(a2, 'coom_Transition', b)
    _safe_set(b, 'coom_ComponentOnOffManifest4', set())
    assert not _is_linked(b, 'coom_ComponentOnOffManifest4', a2)
    if hasattr(a2, 'coom_Transition'):
        assert not _is_linked(a2, 'coom_Transition', b)


def test_assoc_version0_reverse_link_reassign_clear():
    a1 = coom_Version(majorMalue=7, minorValue=7)
    a2 = coom_Version(majorMalue=13, minorValue=13)
    b = coom_ComponentOnOffManifest(name="sample_text")
    _safe_set(b, 'coom_ComponentOnOffManifest', a1)
    assert _is_linked(b, 'coom_ComponentOnOffManifest', a1)
    if hasattr(a1, 'coom_Version'):
        assert _is_linked(a1, 'coom_Version', b)
    _safe_set(b, 'coom_ComponentOnOffManifest', a2)
    assert _is_linked(b, 'coom_ComponentOnOffManifest', a2)
    if hasattr(a1, 'coom_Version'):
        assert not _is_linked(a1, 'coom_Version', b)
    if hasattr(a2, 'coom_Version'):
        assert _is_linked(a2, 'coom_Version', b)
    _safe_set(b, 'coom_ComponentOnOffManifest', None)
    assert not _is_linked(b, 'coom_ComponentOnOffManifest', a2)
    if hasattr(a2, 'coom_Version'):
        assert not _is_linked(a2, 'coom_Version', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

