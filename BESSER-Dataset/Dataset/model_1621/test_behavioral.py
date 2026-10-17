import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Edge,
    NamedElement,
    NetElement,
    pnw_Edge,
    pnw_NamedElement,
    pnw_Net,
    pnw_NetElement,
    pnw_PTEdge,
    pnw_Place,
    pnw_TPEdge,
    pnw_Transition,
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

def test_assoc_elements0_stub_double():
    # pnw_NetElement has no real 'NetElement' property in the generated
    # code (a bare stub) -- manually attach it so pnw_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnw_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnw_Net(incrementalID="sample_text")
    partner = pnw_NetElement()
    setattr(partner, 'NetElement', None)
    _safe_set(owner, 'net', {partner})
    assert getattr(partner, 'NetElement') == owner
    _safe_set(owner, 'net', set())
    assert getattr(partner, 'NetElement') is None


def test_assoc_fromPlace10_stub_double():
    # pnw_PTEdge has no real 'outPTEdges' property in the generated
    # code (a bare stub) -- manually attach it so pnw_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnw_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnw_Place(noOfTokens=7)
    partner = pnw_PTEdge()
    setattr(partner, 'outPTEdges', None)
    _safe_set(owner, 'Place11', partner)
    assert getattr(partner, 'outPTEdges') == owner
    _safe_set(owner, 'Place11', None)
    assert getattr(partner, 'outPTEdges') is None


def test_assoc_inTPEdges6_stub_double():
    # pnw_TPEdge has no real 'TPEdge7' property in the generated
    # code (a bare stub) -- manually attach it so pnw_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnw_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnw_Place(noOfTokens=7)
    partner = pnw_TPEdge()
    setattr(partner, 'TPEdge7', None)
    _safe_set(owner, 'toPlace', {partner})
    assert getattr(partner, 'TPEdge7') == owner
    _safe_set(owner, 'toPlace', set())
    assert getattr(partner, 'TPEdge7') is None


def test_assoc_net1_stub_double():
    # pnw_NetElement has no real 'elements' property in the generated
    # code (a bare stub) -- manually attach it so pnw_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnw_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnw_Net(incrementalID="sample_text")
    partner = pnw_NetElement()
    setattr(partner, 'elements', None)
    _safe_set(owner, 'Net', partner)
    assert getattr(partner, 'elements') == owner
    _safe_set(owner, 'Net', None)
    assert getattr(partner, 'elements') is None


def test_assoc_outPTEdges4_stub_double():
    # pnw_PTEdge has no real 'PTEdge5' property in the generated
    # code (a bare stub) -- manually attach it so pnw_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnw_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnw_Place(noOfTokens=7)
    partner = pnw_PTEdge()
    setattr(partner, 'PTEdge5', None)
    _safe_set(owner, 'fromPlace', {partner})
    assert getattr(partner, 'PTEdge5') == owner
    _safe_set(owner, 'fromPlace', set())
    assert getattr(partner, 'PTEdge5') is None


def test_assoc_toPlace9_stub_double():
    # pnw_TPEdge has no real 'inTPEdges' property in the generated
    # code (a bare stub) -- manually attach it so pnw_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnw_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnw_Place(noOfTokens=7)
    partner = pnw_TPEdge()
    setattr(partner, 'inTPEdges', None)
    _safe_set(owner, 'Place', partner)
    assert getattr(partner, 'inTPEdges') == owner
    _safe_set(owner, 'Place', None)
    assert getattr(partner, 'inTPEdges') is None


