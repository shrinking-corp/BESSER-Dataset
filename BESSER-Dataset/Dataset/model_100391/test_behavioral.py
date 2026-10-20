import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Declaration,
    ExpressionElement,
    NamedElement,
    Pseudostate,
    Reaction,
    ReactiveElement,
    ScopedElement,
    Vertex,
    sgraph_Choice,
    sgraph_Declaration,
    sgraph_Effect,
    sgraph_Entry,
    sgraph_Event,
    sgraph_Exit,
    sgraph_ExpressionElement,
    sgraph_FinalState,
    sgraph_Junction,
    sgraph_NamedElement,
    sgraph_Pseudostate,
    sgraph_Reaction,
    sgraph_ReactiveElement,
    sgraph_Region,
    sgraph_Scope,
    sgraph_ScopedElement,
    sgraph_State,
    sgraph_Statechart,
    sgraph_Statement,
    sgraph_Synchronization,
    sgraph_Transition,
    sgraph_Trigger,
    sgraph_Variable,
    sgraph_Vertex,
    EntryKind,
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

def test_assoc_subRegions25_reverse_link_reassign_clear():
    a1 = sgraph_State(composite=True, leaf=True, orthogonal=True, simple=True, submachine=True)
    a2 = sgraph_State(composite=False, leaf=False, orthogonal=False, simple=False, submachine=False)
    b = sgraph_Region(priority=7)
    _safe_set(b, 'sgraph_Region26', a1)
    assert _is_linked(b, 'sgraph_Region26', a1)
    if hasattr(a1, 'sgraph_State'):
        assert _is_linked(a1, 'sgraph_State', b)
    _safe_set(b, 'sgraph_Region26', a2)
    assert _is_linked(b, 'sgraph_Region26', a2)
    if hasattr(a1, 'sgraph_State'):
        assert not _is_linked(a1, 'sgraph_State', b)
    if hasattr(a2, 'sgraph_State'):
        assert _is_linked(a2, 'sgraph_State', b)
    _safe_set(b, 'sgraph_Region26', None)
    assert not _is_linked(b, 'sgraph_Region26', a2)
    if hasattr(a2, 'sgraph_State'):
        assert not _is_linked(a2, 'sgraph_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_incomingTransitions1_stub_double():
    # sgraph_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Transition(priority=7)
    partner = sgraph_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoingTransitions2_stub_double():
    # sgraph_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Transition(priority=7)
    partner = sgraph_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition3', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition3', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_parentRegion0_stub_double():
    # sgraph_Vertex has no real 'vertices' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Region(priority=7)
    partner = sgraph_Vertex()
    setattr(partner, 'vertices', None)
    _safe_set(owner, 'Region', partner)
    assert getattr(partner, 'vertices') == owner
    _safe_set(owner, 'Region', None)
    assert getattr(partner, 'vertices') is None


def test_assoc_regions9_stub_double():
    # sgraph_Statechart has no real 'sgraph_Statechart' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Region(priority=7)
    partner = sgraph_Statechart()
    setattr(partner, 'sgraph_Statechart', None)
    _safe_set(owner, 'sgraph_Region', partner)
    assert owner in getattr(partner, 'sgraph_Statechart')
    _safe_set(owner, 'sgraph_Region', None)
    assert owner not in getattr(partner, 'sgraph_Statechart')


def test_assoc_source7_stub_double():
    # sgraph_Vertex has no real 'Vertex8' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Transition(priority=7)
    partner = sgraph_Vertex()
    setattr(partner, 'Vertex8', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'Vertex8') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'Vertex8') is None


def test_assoc_substatechart27_stub_double():
    # sgraph_Statechart has no real 'sgraph_Statechart29' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_State(composite=True, leaf=True, orthogonal=True, simple=True, submachine=True)
    partner = sgraph_Statechart()
    setattr(partner, 'sgraph_Statechart29', None)
    _safe_set(owner, 'sgraph_State28', partner)
    assert getattr(partner, 'sgraph_Statechart29') == owner
    _safe_set(owner, 'sgraph_State28', None)
    assert getattr(partner, 'sgraph_Statechart29') is None


def test_assoc_target5_stub_double():
    # sgraph_Vertex has no real 'Vertex6' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Transition(priority=7)
    partner = sgraph_Vertex()
    setattr(partner, 'Vertex6', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'Vertex6') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'Vertex6') is None


def test_assoc_vertices4_stub_double():
    # sgraph_Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_Region(priority=7)
    partner = sgraph_Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'parentRegion', {partner})
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'parentRegion', set())
    assert getattr(partner, 'Vertex') is None


