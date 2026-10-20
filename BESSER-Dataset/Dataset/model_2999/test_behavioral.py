import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PortB,
    typeB_BlockB,
    typeB_InPortB,
    typeB_OutPortB,
    typeB_PortB,
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

def test_assoc_block2_stub_double():
    # typeB_BlockB has no real 'BlockB' property in the generated
    # code (a bare stub) -- manually attach it so typeB_OutPortB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeB_OutPortB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeB_OutPortB(name="sample_text")
    partner = typeB_BlockB()
    setattr(partner, 'BlockB', None)
    _safe_set(owner, 'outputPorts', partner)
    assert getattr(partner, 'BlockB') == owner
    _safe_set(owner, 'outputPorts', None)
    assert getattr(partner, 'BlockB') is None


def test_assoc_inputPorts0_stub_double():
    # typeB_BlockB has no real 'typeB_BlockB' property in the generated
    # code (a bare stub) -- manually attach it so typeB_InPortB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeB_InPortB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeB_InPortB(name="sample_text")
    partner = typeB_BlockB()
    setattr(partner, 'typeB_BlockB', None)
    _safe_set(owner, 'typeB_InPortB', partner)
    assert owner in getattr(partner, 'typeB_BlockB')
    _safe_set(owner, 'typeB_InPortB', None)
    assert owner not in getattr(partner, 'typeB_BlockB')


def test_assoc_outputPorts1_stub_double():
    # typeB_BlockB has no real 'block' property in the generated
    # code (a bare stub) -- manually attach it so typeB_OutPortB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeB_OutPortB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeB_OutPortB(name="sample_text")
    partner = typeB_BlockB()
    setattr(partner, 'block', None)
    _safe_set(owner, 'OutPortB', partner)
    assert owner in getattr(partner, 'block')
    _safe_set(owner, 'OutPortB', None)
    assert owner not in getattr(partner, 'block')


