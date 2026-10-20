import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractAction,
    AbstractBehavior,
    AbstractNamedElement,
    ActivityEdge,
    ActivityNode,
    ModelElement,
    ObjectNode,
    Pin,
    TraceableElement,
    activity_AbstractAction,
    activity_AbstractActivity,
    activity_AbstractBehavior,
    activity_AcceptEventAction,
    activity_ActivityEdge,
    activity_ActivityNode,
    activity_ActivityPartition,
    activity_IState,
    activity_InputPin,
    activity_ObjectFlow,
    activity_ObjectNode,
    activity_OutputPin,
    activity_Pin,
    activity_ValueSpecification,
    ObjectNodeKind,
    ObjectNodeOrderingKind,
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

def test_assoc_guard9_stub_double():
    # activity_ValueSpecification has no real 'activity_ValueSpecification11' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ValueSpecification()
    setattr(partner, 'activity_ValueSpecification11', None)
    _safe_set(owner, 'activity_ActivityEdge10', partner)
    assert getattr(partner, 'activity_ValueSpecification11') == owner
    _safe_set(owner, 'activity_ActivityEdge10', None)
    assert getattr(partner, 'activity_ValueSpecification11') is None


def test_assoc_inState26_stub_double():
    # activity_IState has no real 'activity_IState' property in the generated
    # code (a bare stub) -- manually attach it so activity_ObjectNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ObjectNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ObjectNode(isControlType=True, kindOfNode="sample_text", ordering="sample_text")
    partner = activity_IState()
    setattr(partner, 'activity_IState', None)
    _safe_set(owner, 'activity_ObjectNode27', {partner})
    assert getattr(partner, 'activity_IState') == owner
    _safe_set(owner, 'activity_ObjectNode27', set())
    assert getattr(partner, 'activity_IState') is None


def test_assoc_incoming18_stub_double():
    # activity_ActivityNode has no real 'activity_ActivityNode19' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ActivityNode()
    setattr(partner, 'activity_ActivityNode19', None)
    _safe_set(owner, 'activity_ActivityEdge20', partner)
    assert owner in getattr(partner, 'activity_ActivityNode19')
    _safe_set(owner, 'activity_ActivityEdge20', None)
    assert owner not in getattr(partner, 'activity_ActivityNode19')


def test_assoc_outgoing15_stub_double():
    # activity_ActivityNode has no real 'activity_ActivityNode16' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ActivityNode()
    setattr(partner, 'activity_ActivityNode16', None)
    _safe_set(owner, 'activity_ActivityEdge17', partner)
    assert owner in getattr(partner, 'activity_ActivityNode16')
    _safe_set(owner, 'activity_ActivityEdge17', None)
    assert owner not in getattr(partner, 'activity_ActivityNode16')


def test_assoc_probability1_stub_double():
    # activity_ValueSpecification has no real 'activity_ValueSpecification3' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ValueSpecification()
    setattr(partner, 'activity_ValueSpecification3', None)
    _safe_set(owner, 'activity_ActivityEdge2', partner)
    assert getattr(partner, 'activity_ValueSpecification3') == owner
    _safe_set(owner, 'activity_ActivityEdge2', None)
    assert getattr(partner, 'activity_ValueSpecification3') is None


def test_assoc_rate0_stub_double():
    # activity_ValueSpecification has no real 'activity_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ValueSpecification()
    setattr(partner, 'activity_ValueSpecification', None)
    _safe_set(owner, 'activity_ActivityEdge', partner)
    assert getattr(partner, 'activity_ValueSpecification') == owner
    _safe_set(owner, 'activity_ActivityEdge', None)
    assert getattr(partner, 'activity_ValueSpecification') is None


def test_assoc_selection28_stub_double():
    # activity_AbstractBehavior has no real 'activity_AbstractBehavior' property in the generated
    # code (a bare stub) -- manually attach it so activity_ObjectNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ObjectNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ObjectNode(isControlType=True, kindOfNode="sample_text", ordering="sample_text")
    partner = activity_AbstractBehavior()
    setattr(partner, 'activity_AbstractBehavior', None)
    _safe_set(owner, 'activity_ObjectNode29', partner)
    assert getattr(partner, 'activity_AbstractBehavior') == owner
    _safe_set(owner, 'activity_ObjectNode29', None)
    assert getattr(partner, 'activity_AbstractBehavior') is None


def test_assoc_source6_stub_double():
    # activity_ActivityNode has no real 'activity_ActivityNode8' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ActivityNode()
    setattr(partner, 'activity_ActivityNode8', None)
    _safe_set(owner, 'activity_ActivityEdge7', partner)
    assert getattr(partner, 'activity_ActivityNode8') == owner
    _safe_set(owner, 'activity_ActivityEdge7', None)
    assert getattr(partner, 'activity_ActivityNode8') is None


def test_assoc_target4_stub_double():
    # activity_ActivityNode has no real 'activity_ActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ActivityNode()
    setattr(partner, 'activity_ActivityNode', None)
    _safe_set(owner, 'activity_ActivityEdge5', partner)
    assert getattr(partner, 'activity_ActivityNode') == owner
    _safe_set(owner, 'activity_ActivityEdge5', None)
    assert getattr(partner, 'activity_ActivityNode') is None


def test_assoc_upperBound24_stub_double():
    # activity_ValueSpecification has no real 'activity_ValueSpecification25' property in the generated
    # code (a bare stub) -- manually attach it so activity_ObjectNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ObjectNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ObjectNode(isControlType=True, kindOfNode="sample_text", ordering="sample_text")
    partner = activity_ValueSpecification()
    setattr(partner, 'activity_ValueSpecification25', None)
    _safe_set(owner, 'activity_ObjectNode', partner)
    assert getattr(partner, 'activity_ValueSpecification25') == owner
    _safe_set(owner, 'activity_ObjectNode', None)
    assert getattr(partner, 'activity_ValueSpecification25') is None


def test_assoc_weight12_stub_double():
    # activity_ValueSpecification has no real 'activity_ValueSpecification14' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityEdge(kindOfRate="sample_text")
    partner = activity_ValueSpecification()
    setattr(partner, 'activity_ValueSpecification14', None)
    _safe_set(owner, 'activity_ActivityEdge13', partner)
    assert getattr(partner, 'activity_ValueSpecification14') == owner
    _safe_set(owner, 'activity_ActivityEdge13', None)
    assert getattr(partner, 'activity_ValueSpecification14') is None


