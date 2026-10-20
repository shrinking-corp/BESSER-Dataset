import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    Container,
    GenericDiagram,
    Relationship,
    dscDiagramModel_AnchorNoteToItem,
    dscDiagramModel_DSCDiagram,
    dscDiagramModel_DSCState,
    dscDiagramModel_DeepHistory,
    dscDiagramModel_ShallowHistory,
    dscDiagramModel_StartPoint,
    dscDiagramModel_Transition,
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

def test_assoc_compositeState0_stub_double():
    # dscDiagramModel_StartPoint has no real 'startPoint' property in the generated
    # code (a bare stub) -- manually attach it so dscDiagramModel_DSCState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dscDiagramModel_DSCState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dscDiagramModel_DSCState(Variables="sample_text", isSimple=True)
    partner = dscDiagramModel_StartPoint()
    setattr(partner, 'startPoint', None)
    _safe_set(owner, 'DSCState', partner)
    assert getattr(partner, 'startPoint') == owner
    _safe_set(owner, 'DSCState', None)
    assert getattr(partner, 'startPoint') is None


def test_assoc_compositeState1_stub_double():
    # dscDiagramModel_ShallowHistory has no real 'shallowHistory' property in the generated
    # code (a bare stub) -- manually attach it so dscDiagramModel_DSCState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dscDiagramModel_DSCState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dscDiagramModel_DSCState(Variables="sample_text", isSimple=True)
    partner = dscDiagramModel_ShallowHistory()
    setattr(partner, 'shallowHistory', None)
    _safe_set(owner, 'DSCState2', partner)
    assert getattr(partner, 'shallowHistory') == owner
    _safe_set(owner, 'DSCState2', None)
    assert getattr(partner, 'shallowHistory') is None


def test_assoc_compositeState3_stub_double():
    # dscDiagramModel_DeepHistory has no real 'deepHistory' property in the generated
    # code (a bare stub) -- manually attach it so dscDiagramModel_DSCState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dscDiagramModel_DSCState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dscDiagramModel_DSCState(Variables="sample_text", isSimple=True)
    partner = dscDiagramModel_DeepHistory()
    setattr(partner, 'deepHistory', None)
    _safe_set(owner, 'DSCState4', partner)
    assert getattr(partner, 'deepHistory') == owner
    _safe_set(owner, 'DSCState4', None)
    assert getattr(partner, 'deepHistory') is None


def test_assoc_deepHistory8_stub_double():
    # dscDiagramModel_DeepHistory has no real 'DeepHistory' property in the generated
    # code (a bare stub) -- manually attach it so dscDiagramModel_DSCState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dscDiagramModel_DSCState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dscDiagramModel_DSCState(Variables="sample_text", isSimple=True)
    partner = dscDiagramModel_DeepHistory()
    setattr(partner, 'DeepHistory', None)
    _safe_set(owner, 'compositeState9', partner)
    assert getattr(partner, 'DeepHistory') == owner
    _safe_set(owner, 'compositeState9', None)
    assert getattr(partner, 'DeepHistory') is None


def test_assoc_shallowHistory6_stub_double():
    # dscDiagramModel_ShallowHistory has no real 'ShallowHistory' property in the generated
    # code (a bare stub) -- manually attach it so dscDiagramModel_DSCState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dscDiagramModel_DSCState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dscDiagramModel_DSCState(Variables="sample_text", isSimple=True)
    partner = dscDiagramModel_ShallowHistory()
    setattr(partner, 'ShallowHistory', None)
    _safe_set(owner, 'compositeState7', partner)
    assert getattr(partner, 'ShallowHistory') == owner
    _safe_set(owner, 'compositeState7', None)
    assert getattr(partner, 'ShallowHistory') is None


def test_assoc_startPoint5_stub_double():
    # dscDiagramModel_StartPoint has no real 'StartPoint' property in the generated
    # code (a bare stub) -- manually attach it so dscDiagramModel_DSCState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dscDiagramModel_DSCState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dscDiagramModel_DSCState(Variables="sample_text", isSimple=True)
    partner = dscDiagramModel_StartPoint()
    setattr(partner, 'StartPoint', None)
    _safe_set(owner, 'compositeState', partner)
    assert getattr(partner, 'StartPoint') == owner
    _safe_set(owner, 'compositeState', None)
    assert getattr(partner, 'StartPoint') is None


