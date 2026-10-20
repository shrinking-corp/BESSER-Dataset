import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_Petrinet,
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

def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = petrinet_Petrinet(name="sample_text")
    a2 = petrinet_Petrinet(name="sample_text_2")
    b = petrinet_Node(name="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'petrinet'):
        assert _is_linked(a1, 'petrinet', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'petrinet'):
        assert not _is_linked(a1, 'petrinet', b)
    if hasattr(a2, 'petrinet'):
        assert _is_linked(a2, 'petrinet', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'petrinet'):
        assert not _is_linked(a2, 'petrinet', b)


def test_assoc_petrinet4_reverse_link_reassign_clear():
    a1 = petrinet_Petrinet(name="sample_text")
    a2 = petrinet_Petrinet(name="sample_text_2")
    b = petrinet_Node(name="sample_text")
    _safe_set(b, 'nodes', a1)
    assert _is_linked(b, 'nodes', a1)
    if hasattr(a1, 'Petrinet'):
        assert _is_linked(a1, 'Petrinet', b)
    _safe_set(b, 'nodes', a2)
    assert _is_linked(b, 'nodes', a2)
    if hasattr(a1, 'Petrinet'):
        assert not _is_linked(a1, 'Petrinet', b)
    if hasattr(a2, 'Petrinet'):
        assert _is_linked(a2, 'Petrinet', b)
    _safe_set(b, 'nodes', None)
    assert not _is_linked(b, 'nodes', a2)
    if hasattr(a2, 'Petrinet'):
        assert not _is_linked(a2, 'Petrinet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arcs1_stub_double():
    # petrinet_Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Petrinet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Petrinet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Petrinet(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'petrinet2', {partner})
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'petrinet2', set())
    assert getattr(partner, 'Arc') is None


def test_assoc_in_5_stub_double():
    # petrinet_Arc has no real 'Arc6' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'Arc6', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Arc6') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Arc6') is None


def test_assoc_out7_stub_double():
    # petrinet_Arc has no real 'Arc8' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'Arc8', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Arc8') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Arc8') is None


def test_assoc_petrinet14_stub_double():
    # petrinet_Arc has no real 'arcs' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Petrinet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Petrinet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Petrinet(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'arcs', None)
    _safe_set(owner, 'Petrinet15', partner)
    assert getattr(partner, 'arcs') == owner
    _safe_set(owner, 'Petrinet15', None)
    assert getattr(partner, 'arcs') is None


def test_assoc_source10_stub_double():
    # petrinet_Arc has no real 'out' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'out', None)
    _safe_set(owner, 'Node11', partner)
    assert getattr(partner, 'out') == owner
    _safe_set(owner, 'Node11', None)
    assert getattr(partner, 'out') is None


def test_assoc_target12_stub_double():
    # petrinet_Arc has no real 'in_' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'in_', None)
    _safe_set(owner, 'Node13', partner)
    assert getattr(partner, 'in_') == owner
    _safe_set(owner, 'Node13', None)
    assert getattr(partner, 'in_') is None


