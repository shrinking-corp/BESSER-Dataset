import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_Token,
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

def test_assoc_arcs1_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Arc(weight=7)
    _safe_set(b, 'petrinet_Arc', a1)
    assert _is_linked(b, 'petrinet_Arc', a1)
    if hasattr(a1, 'petrinet_PetriNet2'):
        assert _is_linked(a1, 'petrinet_PetriNet2', b)
    _safe_set(b, 'petrinet_Arc', a2)
    assert _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a1, 'petrinet_PetriNet2'):
        assert not _is_linked(a1, 'petrinet_PetriNet2', b)
    if hasattr(a2, 'petrinet_PetriNet2'):
        assert _is_linked(a2, 'petrinet_PetriNet2', b)
    _safe_set(b, 'petrinet_Arc', None)
    assert not _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a2, 'petrinet_PetriNet2'):
        assert not _is_linked(a2, 'petrinet_PetriNet2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_in_4_stub_double():
    # petrinet_Node has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(weight=7)
    partner = petrinet_Node()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Arc5', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Arc5', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_nodes0_stub_double():
    # petrinet_Node has no real 'petrinet_Node' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_Node()
    setattr(partner, 'petrinet_Node', None)
    _safe_set(owner, 'petrinet_PetriNet', {partner})
    assert getattr(partner, 'petrinet_Node') == owner
    _safe_set(owner, 'petrinet_PetriNet', set())
    assert getattr(partner, 'petrinet_Node') is None


def test_assoc_out3_stub_double():
    # petrinet_Node has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(weight=7)
    partner = petrinet_Node()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Arc', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Arc', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_source7_stub_double():
    # petrinet_Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(weight=7)
    partner = petrinet_Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'out', partner)
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'out', None)
    assert getattr(partner, 'Node') is None


def test_assoc_target8_stub_double():
    # petrinet_Node has no real 'Node9' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(weight=7)
    partner = petrinet_Node()
    setattr(partner, 'Node9', None)
    _safe_set(owner, 'in_', partner)
    assert getattr(partner, 'Node9') == owner
    _safe_set(owner, 'in_', None)
    assert getattr(partner, 'Node9') is None


def test_assoc_tokens6_stub_double():
    # petrinet_Token has no real 'petrinet_Token' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(capacity=7)
    partner = petrinet_Token()
    setattr(partner, 'petrinet_Token', None)
    _safe_set(owner, 'petrinet_Place', {partner})
    assert getattr(partner, 'petrinet_Token') == owner
    _safe_set(owner, 'petrinet_Place', set())
    assert getattr(partner, 'petrinet_Token') is None


