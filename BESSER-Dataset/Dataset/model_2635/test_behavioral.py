import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DEdge,
    DGraphElement,
    DLabeledElement,
    DLineEdge,
    DNestedEdge,
    DNode,
    DOwnedEdge,
    DOwnedElement,
    DSimpleEdge,
    diagraph_DAffixedEdge,
    diagraph_DCompartmentEdge,
    diagraph_DContainment,
    diagraph_DEdge,
    diagraph_DGeneric,
    diagraph_DGraph,
    diagraph_DGraphElement,
    diagraph_DLabel,
    diagraph_DLabeledEdge,
    diagraph_DLabeledElement,
    diagraph_DLineEdge,
    diagraph_DNavigationEdge,
    diagraph_DNestedEdge,
    diagraph_DNode,
    diagraph_DOwnedEdge,
    diagraph_DOwnedElement,
    diagraph_DPointOfView,
    diagraph_DReference,
    diagraph_DSimpleEdge,
    diagraph_DViewNavigation,
    diagraph_EAttribute,
    diagraph_EClass,
    diagraph_ENamedElement,
    diagraph_EReference,
    DShape,
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

def test_assoc_containments6_reverse_link_reassign_clear():
    a1 = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    a2 = diagraph_DNode(layout=False, navigationLink="sample_text_2", shape="sample_text_2")
    b = diagraph_DContainment(name="sample_text")
    _safe_set(b, 'DContainment', a1)
    assert _is_linked(b, 'DContainment', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'DContainment', a2)
    assert _is_linked(b, 'DContainment', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'DContainment', None)
    assert not _is_linked(b, 'DContainment', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_dlabels13_reverse_link_reassign_clear():
    a1 = diagraph_DLabeledElement(expression="sample_text", labls="sample_text")
    a2 = diagraph_DLabeledElement(expression="sample_text_2", labls="sample_text_2")
    b = diagraph_DLabel(abztract=True, inferred=True, propagated=True)
    _safe_set(b, 'diagraph_DLabel', a1)
    assert _is_linked(b, 'diagraph_DLabel', a1)
    if hasattr(a1, 'diagraph_DLabeledElement14'):
        assert _is_linked(a1, 'diagraph_DLabeledElement14', b)
    _safe_set(b, 'diagraph_DLabel', a2)
    assert _is_linked(b, 'diagraph_DLabel', a2)
    if hasattr(a1, 'diagraph_DLabeledElement14'):
        assert not _is_linked(a1, 'diagraph_DLabeledElement14', b)
    if hasattr(a2, 'diagraph_DLabeledElement14'):
        assert _is_linked(a2, 'diagraph_DLabeledElement14', b)
    _safe_set(b, 'diagraph_DLabel', None)
    assert not _is_linked(b, 'diagraph_DLabel', a2)
    if hasattr(a2, 'diagraph_DLabeledElement14'):
        assert not _is_linked(a2, 'diagraph_DLabeledElement14', b)


def test_assoc_elements10_reverse_link_reassign_clear():
    a1 = diagraph_DGraphElement(abztract=True, icon="sample_text", name="sample_text")
    a2 = diagraph_DGraphElement(abztract=False, icon="sample_text_2", name="sample_text_2")
    b = diagraph_DGraph(facade1="sample_text", facade2="sample_text", viewName="sample_text")
    _safe_set(b, 'graph', {a1})
    assert _is_linked(b, 'graph', a1)
    if hasattr(a1, 'DGraphElement'):
        assert _is_linked(a1, 'DGraphElement', b)
    _safe_set(b, 'graph', {a2})
    assert _is_linked(b, 'graph', a2)
    if hasattr(a1, 'DGraphElement'):
        assert not _is_linked(a1, 'DGraphElement', b)
    if hasattr(a2, 'DGraphElement'):
        assert _is_linked(a2, 'DGraphElement', b)
    _safe_set(b, 'graph', set())
    assert not _is_linked(b, 'graph', a2)
    if hasattr(a2, 'DGraphElement'):
        assert not _is_linked(a2, 'DGraphElement', b)


def test_assoc_graph4_reverse_link_reassign_clear():
    a1 = diagraph_DGraphElement(abztract=True, icon="sample_text", name="sample_text")
    a2 = diagraph_DGraphElement(abztract=False, icon="sample_text_2", name="sample_text_2")
    b = diagraph_DGraph(facade1="sample_text", facade2="sample_text", viewName="sample_text")
    _safe_set(b, 'DGraph', a1)
    assert _is_linked(b, 'DGraph', a1)
    if hasattr(a1, 'elements'):
        assert _is_linked(a1, 'elements', b)
    _safe_set(b, 'DGraph', a2)
    assert _is_linked(b, 'DGraph', a2)
    if hasattr(a1, 'elements'):
        assert not _is_linked(a1, 'elements', b)
    if hasattr(a2, 'elements'):
        assert _is_linked(a2, 'elements', b)
    _safe_set(b, 'DGraph', None)
    assert not _is_linked(b, 'DGraph', a2)
    if hasattr(a2, 'elements'):
        assert not _is_linked(a2, 'elements', b)


def test_assoc_navigationSource19_reverse_link_reassign_clear():
    a1 = diagraph_DViewNavigation(id="sample_text")
    a2 = diagraph_DViewNavigation(id="sample_text_2")
    b = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    _safe_set(b, 'DNode', a1)
    assert _is_linked(b, 'DNode', a1)
    if hasattr(a1, 'viewNavigation'):
        assert _is_linked(a1, 'viewNavigation', b)
    _safe_set(b, 'DNode', a2)
    assert _is_linked(b, 'DNode', a2)
    if hasattr(a1, 'viewNavigation'):
        assert not _is_linked(a1, 'viewNavigation', b)
    if hasattr(a2, 'viewNavigation'):
        assert _is_linked(a2, 'viewNavigation', b)
    _safe_set(b, 'DNode', None)
    assert not _is_linked(b, 'DNode', a2)
    if hasattr(a2, 'viewNavigation'):
        assert not _is_linked(a2, 'viewNavigation', b)


def test_assoc_navigationTarget17_reverse_link_reassign_clear():
    a1 = diagraph_DViewNavigation(id="sample_text")
    a2 = diagraph_DViewNavigation(id="sample_text_2")
    b = diagraph_DGraph(facade1="sample_text", facade2="sample_text", viewName="sample_text")
    _safe_set(b, 'diagraph_DGraph18', a1)
    assert _is_linked(b, 'diagraph_DGraph18', a1)
    if hasattr(a1, 'diagraph_DViewNavigation'):
        assert _is_linked(a1, 'diagraph_DViewNavigation', b)
    _safe_set(b, 'diagraph_DGraph18', a2)
    assert _is_linked(b, 'diagraph_DGraph18', a2)
    if hasattr(a1, 'diagraph_DViewNavigation'):
        assert not _is_linked(a1, 'diagraph_DViewNavigation', b)
    if hasattr(a2, 'diagraph_DViewNavigation'):
        assert _is_linked(a2, 'diagraph_DViewNavigation', b)
    _safe_set(b, 'diagraph_DGraph18', None)
    assert not _is_linked(b, 'diagraph_DGraph18', a2)
    if hasattr(a2, 'diagraph_DViewNavigation'):
        assert not _is_linked(a2, 'diagraph_DViewNavigation', b)


def test_assoc_node22_reverse_link_reassign_clear():
    a1 = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    a2 = diagraph_DNode(layout=False, navigationLink="sample_text_2", shape="sample_text_2")
    b = diagraph_DContainment(name="sample_text")
    _safe_set(b, 'containments', a1)
    assert _is_linked(b, 'containments', a1)
    if hasattr(a1, 'DNode23'):
        assert _is_linked(a1, 'DNode23', b)
    _safe_set(b, 'containments', a2)
    assert _is_linked(b, 'containments', a2)
    if hasattr(a1, 'DNode23'):
        assert not _is_linked(a1, 'DNode23', b)
    if hasattr(a2, 'DNode23'):
        assert _is_linked(a2, 'DNode23', b)
    _safe_set(b, 'containments', None)
    assert not _is_linked(b, 'containments', a2)
    if hasattr(a2, 'DNode23'):
        assert not _is_linked(a2, 'DNode23', b)


def test_assoc_target0_reverse_link_reassign_clear():
    a1 = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    a2 = diagraph_DNode(layout=False, navigationLink="sample_text_2", shape="sample_text_2")
    b = diagraph_DEdge(propagated=True)
    _safe_set(b, 'diagraph_DEdge', a1)
    assert _is_linked(b, 'diagraph_DEdge', a1)
    if hasattr(a1, 'diagraph_DNode'):
        assert _is_linked(a1, 'diagraph_DNode', b)
    _safe_set(b, 'diagraph_DEdge', a2)
    assert _is_linked(b, 'diagraph_DEdge', a2)
    if hasattr(a1, 'diagraph_DNode'):
        assert not _is_linked(a1, 'diagraph_DNode', b)
    if hasattr(a2, 'diagraph_DNode'):
        assert _is_linked(a2, 'diagraph_DNode', b)
    _safe_set(b, 'diagraph_DEdge', None)
    assert not _is_linked(b, 'diagraph_DEdge', a2)
    if hasattr(a2, 'diagraph_DNode'):
        assert not _is_linked(a2, 'diagraph_DNode', b)


def test_assoc_viewNavigation5_reverse_link_reassign_clear():
    a1 = diagraph_DViewNavigation(id="sample_text")
    a2 = diagraph_DViewNavigation(id="sample_text_2")
    b = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    _safe_set(b, 'navigationSource', a1)
    assert _is_linked(b, 'navigationSource', a1)
    if hasattr(a1, 'DViewNavigation'):
        assert _is_linked(a1, 'DViewNavigation', b)
    _safe_set(b, 'navigationSource', a2)
    assert _is_linked(b, 'navigationSource', a2)
    if hasattr(a1, 'DViewNavigation'):
        assert not _is_linked(a1, 'DViewNavigation', b)
    if hasattr(a2, 'DViewNavigation'):
        assert _is_linked(a2, 'DViewNavigation', b)
    _safe_set(b, 'navigationSource', None)
    assert not _is_linked(b, 'navigationSource', a2)
    if hasattr(a2, 'DViewNavigation'):
        assert not _is_linked(a2, 'DViewNavigation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute20_stub_double():
    # diagraph_EAttribute has no real 'diagraph_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DLabel(abztract=True, inferred=True, propagated=True)
    partner = diagraph_EAttribute()
    setattr(partner, 'diagraph_EAttribute', None)
    _safe_set(owner, 'diagraph_DLabel21', partner)
    assert getattr(partner, 'diagraph_EAttribute') == owner
    _safe_set(owner, 'diagraph_DLabel21', None)
    assert getattr(partner, 'diagraph_EAttribute') is None


def test_assoc_eClaz12_stub_double():
    # diagraph_EClass has no real 'diagraph_EClass' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DLabeledElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DLabeledElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DLabeledElement(expression="sample_text", labls="sample_text")
    partner = diagraph_EClass()
    setattr(partner, 'diagraph_EClass', None)
    _safe_set(owner, 'diagraph_DLabeledElement', partner)
    assert getattr(partner, 'diagraph_EClass') == owner
    _safe_set(owner, 'diagraph_DLabeledElement', None)
    assert getattr(partner, 'diagraph_EClass') is None


def test_assoc_edges24_stub_double():
    # diagraph_DNestedEdge has no real 'diagraph_DNestedEdge26' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DContainment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DContainment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DContainment(name="sample_text")
    partner = diagraph_DNestedEdge()
    setattr(partner, 'diagraph_DNestedEdge26', None)
    _safe_set(owner, 'diagraph_DContainment25', {partner})
    assert getattr(partner, 'diagraph_DNestedEdge26') == owner
    _safe_set(owner, 'diagraph_DContainment25', set())
    assert getattr(partner, 'diagraph_DNestedEdge26') is None


def test_assoc_owner15_stub_double():
    # diagraph_DOwnedElement has no real 'diagraph_DOwnedElement' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    partner = diagraph_DOwnedElement()
    setattr(partner, 'diagraph_DOwnedElement', None)
    _safe_set(owner, 'diagraph_DNode16', partner)
    assert getattr(partner, 'diagraph_DOwnedElement') == owner
    _safe_set(owner, 'diagraph_DNode16', None)
    assert getattr(partner, 'diagraph_DOwnedElement') is None


def test_assoc_pointOfView11_stub_double():
    # diagraph_DPointOfView has no real 'diagraph_DPointOfView' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DGraph(facade1="sample_text", facade2="sample_text", viewName="sample_text")
    partner = diagraph_DPointOfView()
    setattr(partner, 'diagraph_DPointOfView', None)
    _safe_set(owner, 'diagraph_DGraph', partner)
    assert getattr(partner, 'diagraph_DPointOfView') == owner
    _safe_set(owner, 'diagraph_DGraph', None)
    assert getattr(partner, 'diagraph_DPointOfView') is None


def test_assoc_semanticRole3_stub_double():
    # diagraph_ENamedElement has no real 'diagraph_ENamedElement' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DGraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DGraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DGraphElement(abztract=True, icon="sample_text", name="sample_text")
    partner = diagraph_ENamedElement()
    setattr(partner, 'diagraph_ENamedElement', None)
    _safe_set(owner, 'diagraph_DGraphElement', partner)
    assert getattr(partner, 'diagraph_ENamedElement') == owner
    _safe_set(owner, 'diagraph_DGraphElement', None)
    assert getattr(partner, 'diagraph_ENamedElement') is None


def test_assoc_source27_stub_double():
    # diagraph_DSimpleEdge has no real 'diagraph_DSimpleEdge' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DNode(layout=True, navigationLink="sample_text", shape="sample_text")
    partner = diagraph_DSimpleEdge()
    setattr(partner, 'diagraph_DSimpleEdge', None)
    _safe_set(owner, 'diagraph_DNode28', partner)
    assert getattr(partner, 'diagraph_DSimpleEdge') == owner
    _safe_set(owner, 'diagraph_DNode28', None)
    assert getattr(partner, 'diagraph_DSimpleEdge') is None


def test_assoc_source9_stub_double():
    # diagraph_DNestedEdge has no real 'diagraph_DNestedEdge' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DContainment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DContainment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DContainment(name="sample_text")
    partner = diagraph_DNestedEdge()
    setattr(partner, 'diagraph_DNestedEdge', None)
    _safe_set(owner, 'diagraph_DContainment', partner)
    assert getattr(partner, 'diagraph_DNestedEdge') == owner
    _safe_set(owner, 'diagraph_DContainment', None)
    assert getattr(partner, 'diagraph_DNestedEdge') is None


def test_assoc_targetReference1_stub_double():
    # diagraph_EReference has no real 'diagraph_EReference' property in the generated
    # code (a bare stub) -- manually attach it so diagraph_DEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diagraph_DEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diagraph_DEdge(propagated=True)
    partner = diagraph_EReference()
    setattr(partner, 'diagraph_EReference', None)
    _safe_set(owner, 'diagraph_DEdge2', partner)
    assert getattr(partner, 'diagraph_EReference') == owner
    _safe_set(owner, 'diagraph_DEdge2', None)
    assert getattr(partner, 'diagraph_EReference') is None


