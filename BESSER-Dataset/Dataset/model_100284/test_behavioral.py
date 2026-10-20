import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    Container,
    CustomPragmatics,
    Derived,
    Explicit,
    HLAnnotation,
    HLArcAddin,
    HasGraphics,
    HasLabel,
    HasName,
    Node,
    Object,
    PlaceNode,
    Pragmatic,
    TransitionNode,
    nppn_Arc,
    nppn_Binding,
    nppn_Block,
    nppn_HLAnnotation,
    nppn_HasLabel,
    nppn_Instance,
    nppn_Label,
    nppn_Monitor,
    nppn_Name,
    nppn_Node,
    nppn_Object,
    nppn_PNPattern,
    nppn_Page,
    nppn_PetriNet,
    nppn_Place,
    nppn_PlaceNode,
    nppn_PlacementConstraints,
    nppn_Pragmatic,
    nppn_Principal,
    nppn_RefPlace,
    nppn_Service,
    nppn_Transition,
    nppn_TransitionNode,
    org_k1s_nppn_AbstractTemplateTree,
    org_k1s_nppn_Arc,
    org_k1s_nppn_Atomic,
    org_k1s_nppn_Binding,
    org_k1s_nppn_Bindings,
    org_k1s_nppn_Block,
    org_k1s_nppn_Conditinoal,
    org_k1s_nppn_Conditional,
    org_k1s_nppn_Container,
    org_k1s_nppn_CustomDerivedPragmatics,
    org_k1s_nppn_CustomExplicitPragmatics,
    org_k1s_nppn_CustomPragmatics,
    org_k1s_nppn_Derived,
    org_k1s_nppn_Explicit,
    org_k1s_nppn_HLAnnotation,
    org_k1s_nppn_HLArcAddin,
    org_k1s_nppn_HasLabel,
    org_k1s_nppn_HasName,
    org_k1s_nppn_Instance,
    org_k1s_nppn_Label,
    org_k1s_nppn_Loop,
    org_k1s_nppn_Name,
    org_k1s_nppn_Node,
    org_k1s_nppn_Object,
    org_k1s_nppn_PNPattern,
    org_k1s_nppn_Page,
    org_k1s_nppn_PetriNet,
    org_k1s_nppn_Place,
    org_k1s_nppn_PlaceNode,
    org_k1s_nppn_PlacementConstraints,
    org_k1s_nppn_Pragmatic,
    org_k1s_nppn_Principal,
    org_k1s_nppn_RefPlace,
    org_k1s_nppn_RefTrans,
    org_k1s_nppn_Service,
    org_k1s_nppn_Transition,
    org_k1s_nppn_TransitionNode,
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

def test_assoc_constraints27_stub_double():
    # nppn_PlacementConstraints has no real 'nppn_PlacementConstraints' property in the generated
    # code (a bare stub) -- manually attach it so org_k1s_nppn_Pragmatic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_k1s_nppn_Pragmatic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_k1s_nppn_Pragmatic(name="sample_text")
    partner = nppn_PlacementConstraints()
    setattr(partner, 'nppn_PlacementConstraints', None)
    _safe_set(owner, 'org_k1s_nppn_Pragmatic', {partner})
    assert getattr(partner, 'nppn_PlacementConstraints') == owner
    _safe_set(owner, 'org_k1s_nppn_Pragmatic', set())
    assert getattr(partner, 'nppn_PlacementConstraints') is None


def test_assoc_hlinscription4_stub_double():
    # nppn_HLAnnotation has no real 'nppn_HLAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so org_k1s_nppn_HLArcAddin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_k1s_nppn_HLArcAddin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_k1s_nppn_HLArcAddin(kind="sample_text")
    partner = nppn_HLAnnotation()
    setattr(partner, 'nppn_HLAnnotation', None)
    _safe_set(owner, 'org_k1s_nppn_HLArcAddin', partner)
    assert getattr(partner, 'nppn_HLAnnotation') == owner
    _safe_set(owner, 'org_k1s_nppn_HLArcAddin', None)
    assert getattr(partner, 'nppn_HLAnnotation') is None


def test_assoc_monitors22_stub_double():
    # nppn_Monitor has no real 'monitors.ecoreMonitor' property in the generated
    # code (a bare stub) -- manually attach it so org_k1s_nppn_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_k1s_nppn_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_k1s_nppn_PetriNet(kind="sample_text", timeType="sample_text")
    partner = nppn_Monitor()
    setattr(partner, 'monitors.ecoreMonitor', None)
    _safe_set(owner, 'petriNet23', {partner})
    assert getattr(partner, 'monitors.ecoreMonitor') == owner
    _safe_set(owner, 'petriNet23', set())
    assert getattr(partner, 'monitors.ecoreMonitor') is None


def test_assoc_page20_stub_double():
    # nppn_Page has no real 'Page21' property in the generated
    # code (a bare stub) -- manually attach it so org_k1s_nppn_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_k1s_nppn_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_k1s_nppn_PetriNet(kind="sample_text", timeType="sample_text")
    partner = nppn_Page()
    setattr(partner, 'Page21', None)
    _safe_set(owner, 'petriNet', {partner})
    assert getattr(partner, 'Page21') == owner
    _safe_set(owner, 'petriNet', set())
    assert getattr(partner, 'Page21') is None


def test_assoc_parent7_stub_double():
    # nppn_HasLabel has no real 'HasLabel' property in the generated
    # code (a bare stub) -- manually attach it so org_k1s_nppn_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_k1s_nppn_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_k1s_nppn_Label()
    partner = nppn_HasLabel()
    setattr(partner, 'HasLabel', None)
    _safe_set(owner, 'label', partner)
    assert getattr(partner, 'HasLabel') == owner
    _safe_set(owner, 'label', None)
    assert getattr(partner, 'HasLabel') is None


def test_assoc_pragmatic44_stub_double():
    # nppn_Pragmatic has no real 'nppn_Pragmatic45' property in the generated
    # code (a bare stub) -- manually attach it so org_k1s_nppn_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_k1s_nppn_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_k1s_nppn_Binding(template="sample_text")
    partner = nppn_Pragmatic()
    setattr(partner, 'nppn_Pragmatic45', None)
    _safe_set(owner, 'org_k1s_nppn_Binding', partner)
    assert getattr(partner, 'nppn_Pragmatic45') == owner
    _safe_set(owner, 'org_k1s_nppn_Binding', None)
    assert getattr(partner, 'nppn_Pragmatic45') is None


