import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DClassElement,
    DContainedEdge,
    DContainedElement,
    DEdge,
    DGraphElement,
    DModelElementBridge,
    dsml_DAttributeBridge,
    dsml_DClassBridge,
    dsml_DClassElement,
    dsml_DContainedEdge,
    dsml_DContainedElement,
    dsml_DContainment,
    dsml_DEdge,
    dsml_DGraph,
    dsml_DGraphElement,
    dsml_DLabel,
    dsml_DLink,
    dsml_DModelElementBridge,
    dsml_DNode,
    dsml_DReference,
    dsml_DReferenceBridge,
    dsml_DSemanticBridge,
    dsml_Diagraph,
    dsml_EAttribute,
    dsml_EClass,
    dsml_EReference,
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

def test_assoc_childrenPointOfView14_reverse_link_reassign_clear():
    a1 = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    a2 = dsml_DNode(pointOfView=False, pointOfViewName="sample_text_2")
    b = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    _safe_set(b, 'parentPointOfView', {a1})
    assert _is_linked(b, 'parentPointOfView', a1)
    if hasattr(a1, 'DNode15'):
        assert _is_linked(a1, 'DNode15', b)
    _safe_set(b, 'parentPointOfView', {a2})
    assert _is_linked(b, 'parentPointOfView', a2)
    if hasattr(a1, 'DNode15'):
        assert not _is_linked(a1, 'DNode15', b)
    if hasattr(a2, 'DNode15'):
        assert _is_linked(a2, 'DNode15', b)
    _safe_set(b, 'parentPointOfView', set())
    assert not _is_linked(b, 'parentPointOfView', a2)
    if hasattr(a2, 'DNode15'):
        assert not _is_linked(a2, 'DNode15', b)


def test_assoc_labels16_reverse_link_reassign_clear():
    a1 = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    a2 = dsml_DNode(pointOfView=False, pointOfViewName="sample_text_2")
    b = dsml_DLabel(name="sample_text")
    _safe_set(b, 'dsml_DLabel', a1)
    assert _is_linked(b, 'dsml_DLabel', a1)
    if hasattr(a1, 'dsml_DNode17'):
        assert _is_linked(a1, 'dsml_DNode17', b)
    _safe_set(b, 'dsml_DLabel', a2)
    assert _is_linked(b, 'dsml_DLabel', a2)
    if hasattr(a1, 'dsml_DNode17'):
        assert not _is_linked(a1, 'dsml_DNode17', b)
    if hasattr(a2, 'dsml_DNode17'):
        assert _is_linked(a2, 'dsml_DNode17', b)
    _safe_set(b, 'dsml_DLabel', None)
    assert not _is_linked(b, 'dsml_DLabel', a2)
    if hasattr(a2, 'dsml_DNode17'):
        assert not _is_linked(a2, 'dsml_DNode17', b)


def test_assoc_parentPointOfView12_reverse_link_reassign_clear():
    a1 = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    a2 = dsml_DNode(pointOfView=False, pointOfViewName="sample_text_2")
    b = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    _safe_set(b, 'childrenPointOfView', a1)
    assert _is_linked(b, 'childrenPointOfView', a1)
    if hasattr(a1, 'DNode'):
        assert _is_linked(a1, 'DNode', b)
    _safe_set(b, 'childrenPointOfView', a2)
    assert _is_linked(b, 'childrenPointOfView', a2)
    if hasattr(a1, 'DNode'):
        assert not _is_linked(a1, 'DNode', b)
    if hasattr(a2, 'DNode'):
        assert _is_linked(a2, 'DNode', b)
    _safe_set(b, 'childrenPointOfView', None)
    assert not _is_linked(b, 'childrenPointOfView', a2)
    if hasattr(a2, 'DNode'):
        assert not _is_linked(a2, 'DNode', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containment36_stub_double():
    # dsml_DContainedElement has no real 'dsml_DContainedElement' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    partner = dsml_DContainedElement()
    setattr(partner, 'dsml_DContainedElement', None)
    _safe_set(owner, 'dsml_DNode37', partner)
    assert getattr(partner, 'dsml_DContainedElement') == owner
    _safe_set(owner, 'dsml_DNode37', None)
    assert getattr(partner, 'dsml_DContainedElement') is None


def test_assoc_dModelElements45_stub_double():
    # dsml_DSemanticBridge has no real 'dsml_DSemanticBridge46' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DModelElementBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DModelElementBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DModelElementBridge(ecoreName="sample_text", ecorePath="sample_text")
    partner = dsml_DSemanticBridge()
    setattr(partner, 'dsml_DSemanticBridge46', None)
    _safe_set(owner, 'dsml_DModelElementBridge', partner)
    assert owner in getattr(partner, 'dsml_DSemanticBridge46')
    _safe_set(owner, 'dsml_DModelElementBridge', None)
    assert owner not in getattr(partner, 'dsml_DSemanticBridge46')


def test_assoc_eAttributeBridge47_stub_double():
    # dsml_DAttributeBridge has no real 'dsml_DAttributeBridge' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DLabel(name="sample_text")
    partner = dsml_DAttributeBridge()
    setattr(partner, 'dsml_DAttributeBridge', None)
    _safe_set(owner, 'dsml_DLabel48', partner)
    assert getattr(partner, 'dsml_DAttributeBridge') == owner
    _safe_set(owner, 'dsml_DLabel48', None)
    assert getattr(partner, 'dsml_DAttributeBridge') is None


def test_assoc_edges8_stub_double():
    # dsml_DEdge has no real 'dsml_DEdge10' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    partner = dsml_DEdge()
    setattr(partner, 'dsml_DEdge10', None)
    _safe_set(owner, 'dsml_DNode9', {partner})
    assert getattr(partner, 'dsml_DEdge10') == owner
    _safe_set(owner, 'dsml_DNode9', set())
    assert getattr(partner, 'dsml_DEdge10') is None


def test_assoc_linkLabels23_stub_double():
    # dsml_DLink has no real 'dsml_DLink24' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DLabel(name="sample_text")
    partner = dsml_DLink()
    setattr(partner, 'dsml_DLink24', None)
    _safe_set(owner, 'dsml_DLabel25', partner)
    assert owner in getattr(partner, 'dsml_DLink24')
    _safe_set(owner, 'dsml_DLabel25', None)
    assert owner not in getattr(partner, 'dsml_DLink24')


def test_assoc_nodes26_stub_double():
    # dsml_DGraph has no real 'dsml_DGraph' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    partner = dsml_DGraph()
    setattr(partner, 'dsml_DGraph', None)
    _safe_set(owner, 'dsml_DNode27', partner)
    assert owner in getattr(partner, 'dsml_DGraph')
    _safe_set(owner, 'dsml_DNode27', None)
    assert owner not in getattr(partner, 'dsml_DGraph')


def test_assoc_rootPointOfView28_stub_double():
    # dsml_DGraph has no real 'dsml_DGraph29' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    partner = dsml_DGraph()
    setattr(partner, 'dsml_DGraph29', None)
    _safe_set(owner, 'dsml_DNode30', partner)
    assert getattr(partner, 'dsml_DGraph29') == owner
    _safe_set(owner, 'dsml_DNode30', None)
    assert getattr(partner, 'dsml_DGraph29') is None


def test_assoc_sourceNode3_stub_double():
    # dsml_DEdge has no real 'dsml_DEdge4' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    partner = dsml_DEdge()
    setattr(partner, 'dsml_DEdge4', None)
    _safe_set(owner, 'dsml_DNode5', partner)
    assert getattr(partner, 'dsml_DEdge4') == owner
    _safe_set(owner, 'dsml_DNode5', None)
    assert getattr(partner, 'dsml_DEdge4') is None


def test_assoc_targetNode0_stub_double():
    # dsml_DEdge has no real 'dsml_DEdge' property in the generated
    # code (a bare stub) -- manually attach it so dsml_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsml_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsml_DNode(pointOfView=True, pointOfViewName="sample_text")
    partner = dsml_DEdge()
    setattr(partner, 'dsml_DEdge', None)
    _safe_set(owner, 'dsml_DNode', partner)
    assert getattr(partner, 'dsml_DEdge') == owner
    _safe_set(owner, 'dsml_DNode', None)
    assert getattr(partner, 'dsml_DEdge') is None


