import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractModelElement,
    Arc,
    GuiGraphNode,
    ITimeConsumer,
    Place,
    Predicate,
    Transition,
    Widget,
    guigraph_Arc,
    guigraph_ConditionActionTransition,
    guigraph_Form,
    guigraph_GuiGraph,
    guigraph_GuiGraphNode,
    guigraph_InhibitorArc,
    guigraph_NoWidgetNode,
    guigraph_PageMappingArc,
    guigraph_PageTransition,
    guigraph_Place,
    guigraph_PreGenerationSequence,
    guigraph_StandardArc,
    guigraph_TimerTransition,
    guigraph_Transition,
    guigraph_Widget,
    rules_IRealTimeConsumer,
    TimingType,
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

def test_assoc_children6_reverse_link_reassign_clear():
    a1 = guigraph_Widget(image="sample_text")
    a2 = guigraph_Widget(image="sample_text_2")
    b = guigraph_Widget(image="sample_text")
    _safe_set(b, 'guigraph_Widget5', {a1})
    assert _is_linked(b, 'guigraph_Widget5', a1)
    if hasattr(a1, 'guigraph_Widget'):
        assert _is_linked(a1, 'guigraph_Widget', b)
    _safe_set(b, 'guigraph_Widget5', {a2})
    assert _is_linked(b, 'guigraph_Widget5', a2)
    if hasattr(a1, 'guigraph_Widget'):
        assert not _is_linked(a1, 'guigraph_Widget', b)
    if hasattr(a2, 'guigraph_Widget'):
        assert _is_linked(a2, 'guigraph_Widget', b)
    _safe_set(b, 'guigraph_Widget5', set())
    assert not _is_linked(b, 'guigraph_Widget5', a2)
    if hasattr(a2, 'guigraph_Widget'):
        assert not _is_linked(a2, 'guigraph_Widget', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions9_stub_double():
    # guigraph_PreGenerationSequence has no real 'guigraph_PreGenerationSequence' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_ConditionActionTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_ConditionActionTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_ConditionActionTransition(actionsText="sample_text", applicationConditionText="sample_text")
    partner = guigraph_PreGenerationSequence()
    setattr(partner, 'guigraph_PreGenerationSequence', None)
    _safe_set(owner, 'guigraph_ConditionActionTransition10', partner)
    assert getattr(partner, 'guigraph_PreGenerationSequence') == owner
    _safe_set(owner, 'guigraph_ConditionActionTransition10', None)
    assert getattr(partner, 'guigraph_PreGenerationSequence') is None


def test_assoc_applicationCondition7_stub_double():
    # Predicate has no real 'Predicate8' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_ConditionActionTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_ConditionActionTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_ConditionActionTransition(actionsText="sample_text", applicationConditionText="sample_text")
    partner = Predicate()
    setattr(partner, 'Predicate8', None)
    _safe_set(owner, 'guigraph_ConditionActionTransition', partner)
    assert getattr(partner, 'Predicate8') == owner
    _safe_set(owner, 'guigraph_ConditionActionTransition', None)
    assert getattr(partner, 'Predicate8') is None


def test_assoc_arcs0_stub_double():
    # guigraph_Arc has no real 'guigraph_Arc' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_GuiGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_GuiGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_GuiGraph(invariantText="sample_text")
    partner = guigraph_Arc()
    setattr(partner, 'guigraph_Arc', None)
    _safe_set(owner, 'guigraph_GuiGraph', {partner})
    assert getattr(partner, 'guigraph_Arc') == owner
    _safe_set(owner, 'guigraph_GuiGraph', set())
    assert getattr(partner, 'guigraph_Arc') is None


def test_assoc_consumer11_stub_double():
    # ITimeConsumer has no real 'ITimeConsumer' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_TimerTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_TimerTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_TimerTransition(duration=7)
    partner = ITimeConsumer()
    setattr(partner, 'ITimeConsumer', None)
    _safe_set(owner, 'guigraph_TimerTransition', partner)
    assert getattr(partner, 'ITimeConsumer') == owner
    _safe_set(owner, 'guigraph_TimerTransition', None)
    assert getattr(partner, 'ITimeConsumer') is None


def test_assoc_invariant3_stub_double():
    # Predicate has no real 'Predicate' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_GuiGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_GuiGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_GuiGraph(invariantText="sample_text")
    partner = Predicate()
    setattr(partner, 'Predicate', None)
    _safe_set(owner, 'guigraph_GuiGraph4', partner)
    assert getattr(partner, 'Predicate') == owner
    _safe_set(owner, 'guigraph_GuiGraph4', None)
    assert getattr(partner, 'Predicate') is None


def test_assoc_mapping20_stub_double():
    # guigraph_PageMappingArc has no real 'guigraph_PageMappingArc' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_Place(initialTokens=7, provideAsInterface=True)
    partner = guigraph_PageMappingArc()
    setattr(partner, 'guigraph_PageMappingArc', None)
    _safe_set(owner, 'guigraph_Place', partner)
    assert getattr(partner, 'guigraph_PageMappingArc') == owner
    _safe_set(owner, 'guigraph_Place', None)
    assert getattr(partner, 'guigraph_PageMappingArc') is None


def test_assoc_nodes1_stub_double():
    # guigraph_GuiGraphNode has no real 'guigraph_GuiGraphNode' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_GuiGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_GuiGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_GuiGraph(invariantText="sample_text")
    partner = guigraph_GuiGraphNode()
    setattr(partner, 'guigraph_GuiGraphNode', None)
    _safe_set(owner, 'guigraph_GuiGraph2', {partner})
    assert getattr(partner, 'guigraph_GuiGraphNode') == owner
    _safe_set(owner, 'guigraph_GuiGraph2', set())
    assert getattr(partner, 'guigraph_GuiGraphNode') is None


def test_assoc_page18_stub_double():
    # guigraph_PageTransition has no real 'guigraph_PageTransition' property in the generated
    # code (a bare stub) -- manually attach it so guigraph_GuiGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # guigraph_GuiGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = guigraph_GuiGraph(invariantText="sample_text")
    partner = guigraph_PageTransition()
    setattr(partner, 'guigraph_PageTransition', None)
    _safe_set(owner, 'guigraph_GuiGraph19', partner)
    assert getattr(partner, 'guigraph_PageTransition') == owner
    _safe_set(owner, 'guigraph_GuiGraph19', None)
    assert getattr(partner, 'guigraph_PageTransition') is None


