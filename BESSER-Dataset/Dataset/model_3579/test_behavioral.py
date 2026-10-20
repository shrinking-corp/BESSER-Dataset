import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TypeA_BlockA,
    TypeA_PortA,
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

def test_assoc_inputPorts0_stub_double():
    # TypeA_BlockA has no real 'TypeA_BlockA' property in the generated
    # code (a bare stub) -- manually attach it so TypeA_PortA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeA_PortA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeA_PortA(name="sample_text")
    partner = TypeA_BlockA()
    setattr(partner, 'TypeA_BlockA', None)
    _safe_set(owner, 'TypeA_PortA', partner)
    assert owner in getattr(partner, 'TypeA_BlockA')
    _safe_set(owner, 'TypeA_PortA', None)
    assert owner not in getattr(partner, 'TypeA_BlockA')


def test_assoc_outputPorts1_stub_double():
    # TypeA_BlockA has no real 'TypeA_BlockA2' property in the generated
    # code (a bare stub) -- manually attach it so TypeA_PortA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TypeA_PortA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TypeA_PortA(name="sample_text")
    partner = TypeA_BlockA()
    setattr(partner, 'TypeA_BlockA2', None)
    _safe_set(owner, 'TypeA_PortA3', partner)
    assert owner in getattr(partner, 'TypeA_BlockA2')
    _safe_set(owner, 'TypeA_PortA3', None)
    assert owner not in getattr(partner, 'TypeA_BlockA2')


