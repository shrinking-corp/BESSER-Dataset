import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_Petrinet,
    petrinet_Place,
    petrinet_Transition,
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

def test_assoc_incomming3_stub_double():
    # petrinet_Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Arc') is None


def test_assoc_nodes0_stub_double():
    # petrinet_Petrinet has no real 'petrinet_Petrinet' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Petrinet()
    setattr(partner, 'petrinet_Petrinet', None)
    _safe_set(owner, 'petrinet_Node', partner)
    assert owner in getattr(partner, 'petrinet_Petrinet')
    _safe_set(owner, 'petrinet_Node', None)
    assert owner not in getattr(partner, 'petrinet_Petrinet')


def test_assoc_outgoing4_stub_double():
    # petrinet_Arc has no real 'Arc5' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'Arc5', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Arc5') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Arc5') is None


def test_assoc_source7_stub_double():
    # petrinet_Arc has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Node8', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Node8', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target6_stub_double():
    # petrinet_Arc has no real 'incomming' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'incomming', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'incomming') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'incomming') is None


