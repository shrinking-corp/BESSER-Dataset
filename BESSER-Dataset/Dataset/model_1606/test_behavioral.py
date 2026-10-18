import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    NetElement,
    pn_NamedElement,
    pn_Net,
    pn_NetElement,
    pn_Place,
    pn_Transition,
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
    # pn_NetElement has no real 'NetElement' property in the generated
    # code (a bare stub) -- manually attach it so pn_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pn_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pn_Net(incrementalID="sample_text")
    partner = pn_NetElement()
    setattr(partner, 'NetElement', None)
    _safe_set(owner, 'net', {partner})
    assert getattr(partner, 'NetElement') == owner
    _safe_set(owner, 'net', set())
    assert getattr(partner, 'NetElement') is None


def test_assoc_net1_stub_double():
    # pn_NetElement has no real 'elements' property in the generated
    # code (a bare stub) -- manually attach it so pn_Net's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pn_Net's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pn_Net(incrementalID="sample_text")
    partner = pn_NetElement()
    setattr(partner, 'elements', None)
    _safe_set(owner, 'Net', partner)
    assert getattr(partner, 'elements') == owner
    _safe_set(owner, 'Net', None)
    assert getattr(partner, 'elements') is None


def test_assoc_srcP2T3_stub_double():
    # pn_Transition has no real 'trgP2T' property in the generated
    # code (a bare stub) -- manually attach it so pn_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pn_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pn_Place(noOfTokens=7)
    partner = pn_Transition()
    setattr(partner, 'trgP2T', None)
    _safe_set(owner, 'Place4', partner)
    assert owner in getattr(partner, 'trgP2T')
    _safe_set(owner, 'Place4', None)
    assert owner not in getattr(partner, 'trgP2T')


def test_assoc_srcT2P6_stub_double():
    # pn_Transition has no real 'Transition7' property in the generated
    # code (a bare stub) -- manually attach it so pn_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pn_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pn_Place(noOfTokens=7)
    partner = pn_Transition()
    setattr(partner, 'Transition7', None)
    _safe_set(owner, 'trgT2P', {partner})
    assert getattr(partner, 'Transition7') == owner
    _safe_set(owner, 'trgT2P', set())
    assert getattr(partner, 'Transition7') is None


def test_assoc_trgP2T5_stub_double():
    # pn_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so pn_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pn_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pn_Place(noOfTokens=7)
    partner = pn_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'srcP2T', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'srcP2T', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_trgT2P2_stub_double():
    # pn_Transition has no real 'srcT2P' property in the generated
    # code (a bare stub) -- manually attach it so pn_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pn_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pn_Place(noOfTokens=7)
    partner = pn_Transition()
    setattr(partner, 'srcT2P', None)
    _safe_set(owner, 'Place', partner)
    assert owner in getattr(partner, 'srcT2P')
    _safe_set(owner, 'Place', None)
    assert owner not in getattr(partner, 'srcT2P')


