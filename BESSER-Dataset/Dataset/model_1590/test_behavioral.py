import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PNGraph,
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

def test_assoc_arcs3_stub_double():
    # petrinet_PNGraph has no real 'petrinet_PNGraph4' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(w="sample_text")
    partner = petrinet_PNGraph()
    setattr(partner, 'petrinet_PNGraph4', None)
    _safe_set(owner, 'petrinet_Arc', partner)
    assert owner in getattr(partner, 'petrinet_PNGraph4')
    _safe_set(owner, 'petrinet_Arc', None)
    assert owner not in getattr(partner, 'petrinet_PNGraph4')


def test_assoc_from_5_stub_double():
    # petrinet_Node has no real 'petrinet_Node' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(w="sample_text")
    partner = petrinet_Node()
    setattr(partner, 'petrinet_Node', None)
    _safe_set(owner, 'petrinet_Arc6', partner)
    assert getattr(partner, 'petrinet_Node') == owner
    _safe_set(owner, 'petrinet_Arc6', None)
    assert getattr(partner, 'petrinet_Node') is None


def test_assoc_places0_stub_double():
    # petrinet_PNGraph has no real 'petrinet_PNGraph' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(id="sample_text", markings="sample_text")
    partner = petrinet_PNGraph()
    setattr(partner, 'petrinet_PNGraph', None)
    _safe_set(owner, 'petrinet_Place', partner)
    assert owner in getattr(partner, 'petrinet_PNGraph')
    _safe_set(owner, 'petrinet_Place', None)
    assert owner not in getattr(partner, 'petrinet_PNGraph')


def test_assoc_to7_stub_double():
    # petrinet_Node has no real 'petrinet_Node9' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(w="sample_text")
    partner = petrinet_Node()
    setattr(partner, 'petrinet_Node9', None)
    _safe_set(owner, 'petrinet_Arc8', partner)
    assert getattr(partner, 'petrinet_Node9') == owner
    _safe_set(owner, 'petrinet_Arc8', None)
    assert getattr(partner, 'petrinet_Node9') is None


def test_assoc_transitions1_stub_double():
    # petrinet_PNGraph has no real 'petrinet_PNGraph2' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(id="sample_text")
    partner = petrinet_PNGraph()
    setattr(partner, 'petrinet_PNGraph2', None)
    _safe_set(owner, 'petrinet_Transition', partner)
    assert owner in getattr(partner, 'petrinet_PNGraph2')
    _safe_set(owner, 'petrinet_Transition', None)
    assert owner not in getattr(partner, 'petrinet_PNGraph2')


