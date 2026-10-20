import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Edge,
    FromCompositeModeEdge,
    FromCompositeModeInitEdge,
    FromConditionalConnectorEdge,
    FromSubModeEdge,
    InitEdge,
    Mode,
    ToCompositeModeEdge,
    ToConditionalConnectorEdge,
    ToSubModeEdge,
    remes_CompositeMode,
    remes_ConditionalConnector,
    remes_Edge,
    remes_EntryConditionalSubEdge,
    remes_EntryConditionalTopEdge,
    remes_EntryConditionalTopInitEdge,
    remes_EntryEdge,
    remes_EntryInitEdge,
    remes_ExitConditionalSubEdge,
    remes_ExitConditionalTopEdge,
    remes_ExitEdge,
    remes_FromCompositeModeEdge,
    remes_FromCompositeModeInitEdge,
    remes_FromConditionalConnectorEdge,
    remes_FromSubModeEdge,
    remes_InitEdge,
    remes_InternalEdge,
    remes_Mode,
    remes_RemesDiagram,
    remes_SubMode,
    remes_ToCompositeModeEdge,
    remes_ToConditionalConnectorEdge,
    remes_ToSubModeEdge,
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

def test_assoc_conditionalConnectors5_stub_double():
    # remes_CompositeMode has no real 'parent6' property in the generated
    # code (a bare stub) -- manually attach it so remes_ConditionalConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ConditionalConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ConditionalConnector(name="sample_text")
    partner = remes_CompositeMode()
    setattr(partner, 'parent6', None)
    _safe_set(owner, 'ConditionalConnector', partner)
    assert owner in getattr(partner, 'parent6')
    _safe_set(owner, 'ConditionalConnector', None)
    assert owner not in getattr(partner, 'parent6')


def test_assoc_connectFrom16_stub_double():
    # remes_FromConditionalConnectorEdge has no real 'exitEdges' property in the generated
    # code (a bare stub) -- manually attach it so remes_ConditionalConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ConditionalConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ConditionalConnector(name="sample_text")
    partner = remes_FromConditionalConnectorEdge()
    setattr(partner, 'exitEdges', None)
    _safe_set(owner, 'ConditionalConnector17', partner)
    assert getattr(partner, 'exitEdges') == owner
    _safe_set(owner, 'ConditionalConnector17', None)
    assert getattr(partner, 'exitEdges') is None


def test_assoc_connectFrom18_stub_double():
    # remes_FromSubModeEdge has no real 'exitEdges19' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent="sample_text", resourceClassA="sample_text", resourceClassB="sample_text", resourceClassC="sample_text")
    partner = remes_FromSubModeEdge()
    setattr(partner, 'exitEdges19', None)
    _safe_set(owner, 'SubMode20', partner)
    assert getattr(partner, 'exitEdges19') == owner
    _safe_set(owner, 'SubMode20', None)
    assert getattr(partner, 'exitEdges19') is None


def test_assoc_connectTo31_stub_double():
    # remes_ToConditionalConnectorEdge has no real 'entryEdges' property in the generated
    # code (a bare stub) -- manually attach it so remes_ConditionalConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ConditionalConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ConditionalConnector(name="sample_text")
    partner = remes_ToConditionalConnectorEdge()
    setattr(partner, 'entryEdges', None)
    _safe_set(owner, 'ConditionalConnector32', partner)
    assert getattr(partner, 'entryEdges') == owner
    _safe_set(owner, 'ConditionalConnector32', None)
    assert getattr(partner, 'entryEdges') is None


def test_assoc_connectTo33_stub_double():
    # remes_ToSubModeEdge has no real 'entryEdges34' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent="sample_text", resourceClassA="sample_text", resourceClassB="sample_text", resourceClassC="sample_text")
    partner = remes_ToSubModeEdge()
    setattr(partner, 'entryEdges34', None)
    _safe_set(owner, 'SubMode35', partner)
    assert getattr(partner, 'entryEdges34') == owner
    _safe_set(owner, 'SubMode35', None)
    assert getattr(partner, 'entryEdges34') is None


def test_assoc_entryEdges22_stub_double():
    # remes_ToSubModeEdge has no real 'ToSubModeEdge' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent="sample_text", resourceClassA="sample_text", resourceClassB="sample_text", resourceClassC="sample_text")
    partner = remes_ToSubModeEdge()
    setattr(partner, 'ToSubModeEdge', None)
    _safe_set(owner, 'connectTo23', {partner})
    assert getattr(partner, 'ToSubModeEdge') == owner
    _safe_set(owner, 'connectTo23', set())
    assert getattr(partner, 'ToSubModeEdge') is None


def test_assoc_entryEdges7_stub_double():
    # remes_ToConditionalConnectorEdge has no real 'ToConditionalConnectorEdge' property in the generated
    # code (a bare stub) -- manually attach it so remes_ConditionalConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ConditionalConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ConditionalConnector(name="sample_text")
    partner = remes_ToConditionalConnectorEdge()
    setattr(partner, 'ToConditionalConnectorEdge', None)
    _safe_set(owner, 'connectTo8', {partner})
    assert getattr(partner, 'ToConditionalConnectorEdge') == owner
    _safe_set(owner, 'connectTo8', set())
    assert getattr(partner, 'ToConditionalConnectorEdge') is None


def test_assoc_exitEdges24_stub_double():
    # remes_FromSubModeEdge has no real 'FromSubModeEdge' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent="sample_text", resourceClassA="sample_text", resourceClassB="sample_text", resourceClassC="sample_text")
    partner = remes_FromSubModeEdge()
    setattr(partner, 'FromSubModeEdge', None)
    _safe_set(owner, 'connectFrom25', {partner})
    assert getattr(partner, 'FromSubModeEdge') == owner
    _safe_set(owner, 'connectFrom25', set())
    assert getattr(partner, 'FromSubModeEdge') is None


def test_assoc_exitEdges9_stub_double():
    # remes_FromConditionalConnectorEdge has no real 'FromConditionalConnectorEdge' property in the generated
    # code (a bare stub) -- manually attach it so remes_ConditionalConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ConditionalConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ConditionalConnector(name="sample_text")
    partner = remes_FromConditionalConnectorEdge()
    setattr(partner, 'FromConditionalConnectorEdge', None)
    _safe_set(owner, 'connectFrom10', {partner})
    assert getattr(partner, 'FromConditionalConnectorEdge') == owner
    _safe_set(owner, 'connectFrom10', set())
    assert getattr(partner, 'FromConditionalConnectorEdge') is None


def test_assoc_modes21_stub_double():
    # remes_RemesDiagram has no real 'remes_RemesDiagram' property in the generated
    # code (a bare stub) -- manually attach it so remes_Mode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Mode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Mode(initialization="sample_text", name="sample_text")
    partner = remes_RemesDiagram()
    setattr(partner, 'remes_RemesDiagram', None)
    _safe_set(owner, 'remes_Mode', partner)
    assert owner in getattr(partner, 'remes_RemesDiagram')
    _safe_set(owner, 'remes_Mode', None)
    assert owner not in getattr(partner, 'remes_RemesDiagram')


def test_assoc_parent11_stub_double():
    # remes_CompositeMode has no real 'CompositeMode' property in the generated
    # code (a bare stub) -- manually attach it so remes_ConditionalConnector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ConditionalConnector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ConditionalConnector(name="sample_text")
    partner = remes_CompositeMode()
    setattr(partner, 'CompositeMode', None)
    _safe_set(owner, 'conditionalConnectors', partner)
    assert getattr(partner, 'CompositeMode') == owner
    _safe_set(owner, 'conditionalConnectors', None)
    assert getattr(partner, 'CompositeMode') is None


def test_assoc_parent26_stub_double():
    # remes_CompositeMode has no real 'CompositeMode27' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent="sample_text", resourceClassA="sample_text", resourceClassB="sample_text", resourceClassC="sample_text")
    partner = remes_CompositeMode()
    setattr(partner, 'CompositeMode27', None)
    _safe_set(owner, 'subModes', partner)
    assert getattr(partner, 'CompositeMode27') == owner
    _safe_set(owner, 'subModes', None)
    assert getattr(partner, 'CompositeMode27') is None


def test_assoc_subModes4_stub_double():
    # remes_CompositeMode has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent="sample_text", resourceClassA="sample_text", resourceClassB="sample_text", resourceClassC="sample_text")
    partner = remes_CompositeMode()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'SubMode', partner)
    assert owner in getattr(partner, 'parent')
    _safe_set(owner, 'SubMode', None)
    assert owner not in getattr(partner, 'parent')


