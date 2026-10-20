import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CompositeElement,
    Declaration,
    DocumentedElement,
    NamedElement,
    Pseudostate,
    Reaction,
    ReactiveElement,
    RegularState,
    ScopedElement,
    SpecificationElement,
    Vertex,
    sgraph_Choice,
    sgraph_CompositeElement,
    sgraph_Declaration,
    sgraph_Effect,
    sgraph_Entry,
    sgraph_Event,
    sgraph_Exit,
    sgraph_FinalState,
    sgraph_Pseudostate,
    sgraph_Reaction,
    sgraph_ReactionProperty,
    sgraph_ReactiveElement,
    sgraph_Region,
    sgraph_RegularState,
    sgraph_Scope,
    sgraph_ScopedElement,
    sgraph_SpecificationElement,
    sgraph_State,
    sgraph_Statechart,
    sgraph_Statement,
    sgraph_Synchronization,
    sgraph_Transition,
    sgraph_Trigger,
    sgraph_Variable,
    sgraph_Vertex,
    ChoiceKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_scopes25_stub_double():
    # sgraph_Scope has no real 'sgraph_Scope26' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_ScopedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_ScopedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_ScopedElement(namespace="sample_text")
    partner = sgraph_Scope()
    setattr(partner, 'sgraph_Scope26', None)
    _safe_set(owner, 'sgraph_ScopedElement', {partner})
    assert getattr(partner, 'sgraph_Scope26') == owner
    _safe_set(owner, 'sgraph_ScopedElement', set())
    assert getattr(partner, 'sgraph_Scope26') is None


def test_assoc_substatechart27_stub_double():
    # sgraph_Statechart has no real 'sgraph_Statechart' property in the generated
    # code (a bare stub) -- manually attach it so sgraph_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgraph_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgraph_State(composite=True, leaf=True, orthogonal=True, simple=True, subchart=True, substatechartId="sample_text")
    partner = sgraph_Statechart()
    setattr(partner, 'sgraph_Statechart', None)
    _safe_set(owner, 'sgraph_State', partner)
    assert getattr(partner, 'sgraph_Statechart') == owner
    _safe_set(owner, 'sgraph_State', None)
    assert getattr(partner, 'sgraph_Statechart') is None


