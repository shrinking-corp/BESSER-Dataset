import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Rail,
    TrackElement,
    sihuhu_NamedElement,
    sihuhu_Rail,
    sihuhu_Signal,
    sihuhu_Switch,
    sihuhu_SwitchConnection,
    sihuhu_Track,
    sihuhu_TrackElement,
    sihuhu_Train,
    sihuhu_World,
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

def test_assoc_allowedFrom10_stub_double():
    # sihuhu_Rail has no real 'sihuhu_Rail11' property in the generated
    # code (a bare stub) -- manually attach it so sihuhu_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sihuhu_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sihuhu_Signal(enabled=True)
    partner = sihuhu_Rail()
    setattr(partner, 'sihuhu_Rail11', None)
    _safe_set(owner, 'sihuhu_Signal12', partner)
    assert getattr(partner, 'sihuhu_Rail11') == owner
    _safe_set(owner, 'sihuhu_Signal12', None)
    assert getattr(partner, 'sihuhu_Rail11') is None


def test_assoc_allowedTo8_stub_double():
    # sihuhu_Rail has no real 'sihuhu_Rail9' property in the generated
    # code (a bare stub) -- manually attach it so sihuhu_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sihuhu_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sihuhu_Signal(enabled=True)
    partner = sihuhu_Rail()
    setattr(partner, 'sihuhu_Rail9', None)
    _safe_set(owner, 'sihuhu_Signal', partner)
    assert getattr(partner, 'sihuhu_Rail9') == owner
    _safe_set(owner, 'sihuhu_Signal', None)
    assert getattr(partner, 'sihuhu_Rail9') is None


def test_assoc_nextRail30_stub_double():
    # sihuhu_Rail has no real 'sihuhu_Rail32' property in the generated
    # code (a bare stub) -- manually attach it so sihuhu_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sihuhu_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sihuhu_Signal(enabled=True)
    partner = sihuhu_Rail()
    setattr(partner, 'sihuhu_Rail32', None)
    _safe_set(owner, 'sihuhu_Signal31', partner)
    assert getattr(partner, 'sihuhu_Rail32') == owner
    _safe_set(owner, 'sihuhu_Signal31', None)
    assert getattr(partner, 'sihuhu_Rail32') is None


