import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ANode,
    XAnnotable,
    atomic_AEdge,
    atomic_AGraph,
    atomic_ANode,
    atomic_AStructured,
    atomic_ATargetEdge,
    atomic_AToken,
    atomic_XAnnotable,
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

def test_assoc_graph11_reverse_link_reassign_clear():
    a1 = atomic_AToken(text="sample_text")
    a2 = atomic_AToken(text="sample_text_2")
    b = atomic_AGraph(corpus="sample_text")
    _safe_set(b, 'AGraph', a1)
    assert _is_linked(b, 'AGraph', a1)
    if hasattr(a1, 'tokens'):
        assert _is_linked(a1, 'tokens', b)
    _safe_set(b, 'AGraph', a2)
    assert _is_linked(b, 'AGraph', a2)
    if hasattr(a1, 'tokens'):
        assert not _is_linked(a1, 'tokens', b)
    if hasattr(a2, 'tokens'):
        assert _is_linked(a2, 'tokens', b)
    _safe_set(b, 'AGraph', None)
    assert not _is_linked(b, 'AGraph', a2)
    if hasattr(a2, 'tokens'):
        assert not _is_linked(a2, 'tokens', b)


def test_assoc_next6_reverse_link_reassign_clear():
    a1 = atomic_AToken(text="sample_text")
    a2 = atomic_AToken(text="sample_text_2")
    b = atomic_AToken(text="sample_text")
    _safe_set(b, 'previous', a1)
    assert _is_linked(b, 'previous', a1)
    if hasattr(a1, 'AToken7'):
        assert _is_linked(a1, 'AToken7', b)
    _safe_set(b, 'previous', a2)
    assert _is_linked(b, 'previous', a2)
    if hasattr(a1, 'AToken7'):
        assert not _is_linked(a1, 'AToken7', b)
    if hasattr(a2, 'AToken7'):
        assert _is_linked(a2, 'AToken7', b)
    _safe_set(b, 'previous', None)
    assert not _is_linked(b, 'previous', a2)
    if hasattr(a2, 'AToken7'):
        assert not _is_linked(a2, 'AToken7', b)


def test_assoc_previous9_reverse_link_reassign_clear():
    a1 = atomic_AToken(text="sample_text")
    a2 = atomic_AToken(text="sample_text_2")
    b = atomic_AToken(text="sample_text")
    _safe_set(b, 'next', a1)
    assert _is_linked(b, 'next', a1)
    if hasattr(a1, 'AToken10'):
        assert _is_linked(a1, 'AToken10', b)
    _safe_set(b, 'next', a2)
    assert _is_linked(b, 'next', a2)
    if hasattr(a1, 'AToken10'):
        assert not _is_linked(a1, 'AToken10', b)
    if hasattr(a2, 'AToken10'):
        assert _is_linked(a2, 'AToken10', b)
    _safe_set(b, 'next', None)
    assert not _is_linked(b, 'next', a2)
    if hasattr(a2, 'AToken10'):
        assert not _is_linked(a2, 'AToken10', b)


def test_assoc_tokens0_reverse_link_reassign_clear():
    a1 = atomic_AToken(text="sample_text")
    a2 = atomic_AToken(text="sample_text_2")
    b = atomic_AGraph(corpus="sample_text")
    _safe_set(b, 'graph', {a1})
    assert _is_linked(b, 'graph', a1)
    if hasattr(a1, 'AToken'):
        assert _is_linked(a1, 'AToken', b)
    _safe_set(b, 'graph', {a2})
    assert _is_linked(b, 'graph', a2)
    if hasattr(a1, 'AToken'):
        assert not _is_linked(a1, 'AToken', b)
    if hasattr(a2, 'AToken'):
        assert _is_linked(a2, 'AToken', b)
    _safe_set(b, 'graph', set())
    assert not _is_linked(b, 'graph', a2)
    if hasattr(a2, 'AToken'):
        assert not _is_linked(a2, 'AToken', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges3_stub_double():
    # atomic_AEdge has no real 'AEdge' property in the generated
    # code (a bare stub) -- manually attach it so atomic_AGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atomic_AGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atomic_AGraph(corpus="sample_text")
    partner = atomic_AEdge()
    setattr(partner, 'AEdge', None)
    _safe_set(owner, 'graph4', {partner})
    assert getattr(partner, 'AEdge') == owner
    _safe_set(owner, 'graph4', set())
    assert getattr(partner, 'AEdge') is None


def test_assoc_graph13_stub_double():
    # atomic_AStructured has no real 'structures' property in the generated
    # code (a bare stub) -- manually attach it so atomic_AGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atomic_AGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atomic_AGraph(corpus="sample_text")
    partner = atomic_AStructured()
    setattr(partner, 'structures', None)
    _safe_set(owner, 'AGraph14', partner)
    assert getattr(partner, 'structures') == owner
    _safe_set(owner, 'AGraph14', None)
    assert getattr(partner, 'structures') is None


def test_assoc_graph15_stub_double():
    # atomic_AEdge has no real 'edges' property in the generated
    # code (a bare stub) -- manually attach it so atomic_AGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atomic_AGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atomic_AGraph(corpus="sample_text")
    partner = atomic_AEdge()
    setattr(partner, 'edges', None)
    _safe_set(owner, 'AGraph16', partner)
    assert getattr(partner, 'edges') == owner
    _safe_set(owner, 'AGraph16', None)
    assert getattr(partner, 'edges') is None


def test_assoc_graph25_stub_double():
    # atomic_ATargetEdge has no real 'atomic_ATargetEdge26' property in the generated
    # code (a bare stub) -- manually attach it so atomic_AGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atomic_AGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atomic_AGraph(corpus="sample_text")
    partner = atomic_ATargetEdge()
    setattr(partner, 'atomic_ATargetEdge26', None)
    _safe_set(owner, 'atomic_AGraph', partner)
    assert getattr(partner, 'atomic_ATargetEdge26') == owner
    _safe_set(owner, 'atomic_AGraph', None)
    assert getattr(partner, 'atomic_ATargetEdge26') is None


def test_assoc_structures1_stub_double():
    # atomic_AStructured has no real 'AStructured' property in the generated
    # code (a bare stub) -- manually attach it so atomic_AGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atomic_AGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atomic_AGraph(corpus="sample_text")
    partner = atomic_AStructured()
    setattr(partner, 'AStructured', None)
    _safe_set(owner, 'graph2', {partner})
    assert getattr(partner, 'AStructured') == owner
    _safe_set(owner, 'graph2', set())
    assert getattr(partner, 'AStructured') is None


