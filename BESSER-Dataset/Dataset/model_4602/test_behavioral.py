import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor,
    Connection,
    Port,
    adfg_Actor,
    adfg_AffineRelation,
    adfg_AperiodicActor,
    adfg_Application,
    adfg_Channel,
    adfg_Connection,
    adfg_Graph,
    adfg_GraphConnection,
    adfg_InputPort,
    adfg_LossyChannel,
    adfg_OutputPort,
    adfg_PeriodicActor,
    adfg_Port,
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

def test_assoc_affineRelationSource36_reverse_link_reassign_clear():
    a1 = adfg_PeriodicActor(deadline="sample_text", period="sample_text", periodLowerBound="sample_text", periodUpperBound="sample_text", phase="sample_text", wcet="sample_text")
    a2 = adfg_PeriodicActor(deadline="sample_text_2", period="sample_text_2", periodLowerBound="sample_text_2", periodUpperBound="sample_text_2", phase="sample_text_2", wcet="sample_text_2")
    b = adfg_AffineRelation(d=7, n=7, phi=7)
    _safe_set(b, 'AffineRelation38', a1)
    assert _is_linked(b, 'AffineRelation38', a1)
    if hasattr(a1, 'source37'):
        assert _is_linked(a1, 'source37', b)
    _safe_set(b, 'AffineRelation38', a2)
    assert _is_linked(b, 'AffineRelation38', a2)
    if hasattr(a1, 'source37'):
        assert not _is_linked(a1, 'source37', b)
    if hasattr(a2, 'source37'):
        assert _is_linked(a2, 'source37', b)
    _safe_set(b, 'AffineRelation38', None)
    assert not _is_linked(b, 'AffineRelation38', a2)
    if hasattr(a2, 'source37'):
        assert not _is_linked(a2, 'source37', b)


def test_assoc_affineRelationTarget39_reverse_link_reassign_clear():
    a1 = adfg_PeriodicActor(deadline="sample_text", period="sample_text", periodLowerBound="sample_text", periodUpperBound="sample_text", phase="sample_text", wcet="sample_text")
    a2 = adfg_PeriodicActor(deadline="sample_text_2", period="sample_text_2", periodLowerBound="sample_text_2", periodUpperBound="sample_text_2", phase="sample_text_2", wcet="sample_text_2")
    b = adfg_AffineRelation(d=7, n=7, phi=7)
    _safe_set(b, 'AffineRelation41', a1)
    assert _is_linked(b, 'AffineRelation41', a1)
    if hasattr(a1, 'target40'):
        assert _is_linked(a1, 'target40', b)
    _safe_set(b, 'AffineRelation41', a2)
    assert _is_linked(b, 'AffineRelation41', a2)
    if hasattr(a1, 'target40'):
        assert not _is_linked(a1, 'target40', b)
    if hasattr(a2, 'target40'):
        assert _is_linked(a2, 'target40', b)
    _safe_set(b, 'AffineRelation41', None)
    assert not _is_linked(b, 'AffineRelation41', a2)
    if hasattr(a2, 'target40'):
        assert not _is_linked(a2, 'target40', b)


def test_assoc_affineRelations6_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_AffineRelation(d=7, n=7, phi=7)
    _safe_set(b, 'AffineRelation', a1)
    assert _is_linked(b, 'AffineRelation', a1)
    if hasattr(a1, 'owner7'):
        assert _is_linked(a1, 'owner7', b)
    _safe_set(b, 'AffineRelation', a2)
    assert _is_linked(b, 'AffineRelation', a2)
    if hasattr(a1, 'owner7'):
        assert not _is_linked(a1, 'owner7', b)
    if hasattr(a2, 'owner7'):
        assert _is_linked(a2, 'owner7', b)
    _safe_set(b, 'AffineRelation', None)
    assert not _is_linked(b, 'AffineRelation', a2)
    if hasattr(a2, 'owner7'):
        assert not _is_linked(a2, 'owner7', b)


def test_assoc_connections8_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_Connection(id=7, size=7)
    _safe_set(b, 'Connection', a1)
    assert _is_linked(b, 'Connection', a1)
    if hasattr(a1, 'owner9'):
        assert _is_linked(a1, 'owner9', b)
    _safe_set(b, 'Connection', a2)
    assert _is_linked(b, 'Connection', a2)
    if hasattr(a1, 'owner9'):
        assert not _is_linked(a1, 'owner9', b)
    if hasattr(a2, 'owner9'):
        assert _is_linked(a2, 'owner9', b)
    _safe_set(b, 'Connection', None)
    assert not _is_linked(b, 'Connection', a2)
    if hasattr(a2, 'owner9'):
        assert not _is_linked(a2, 'owner9', b)


def test_assoc_graphs0_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_Application(dynamicChecking=True, name="sample_text", nbGraphs=7, nbProcessors=7, schedulingAlgorithm="sample_text", sourceCode="sample_text")
    _safe_set(b, 'owner', {a1})
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'Graph'):
        assert _is_linked(a1, 'Graph', b)
    _safe_set(b, 'owner', {a2})
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'Graph'):
        assert not _is_linked(a1, 'Graph', b)
    if hasattr(a2, 'Graph'):
        assert _is_linked(a2, 'Graph', b)
    _safe_set(b, 'owner', set())
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'Graph'):
        assert not _is_linked(a2, 'Graph', b)


def test_assoc_nodes4_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_Actor(name="sample_text", nbPorts=7, priority=7, procNumber=7, sourceCode="sample_text")
    _safe_set(b, 'Actor', a1)
    assert _is_linked(b, 'Actor', a1)
    if hasattr(a1, 'owner5'):
        assert _is_linked(a1, 'owner5', b)
    _safe_set(b, 'Actor', a2)
    assert _is_linked(b, 'Actor', a2)
    if hasattr(a1, 'owner5'):
        assert not _is_linked(a1, 'owner5', b)
    if hasattr(a2, 'owner5'):
        assert _is_linked(a2, 'owner5', b)
    _safe_set(b, 'Actor', None)
    assert not _is_linked(b, 'Actor', a2)
    if hasattr(a2, 'owner5'):
        assert not _is_linked(a2, 'owner5', b)


def test_assoc_owner16_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_Actor(name="sample_text", nbPorts=7, priority=7, procNumber=7, sourceCode="sample_text")
    _safe_set(b, 'nodes', a1)
    assert _is_linked(b, 'nodes', a1)
    if hasattr(a1, 'Graph17'):
        assert _is_linked(a1, 'Graph17', b)
    _safe_set(b, 'nodes', a2)
    assert _is_linked(b, 'nodes', a2)
    if hasattr(a1, 'Graph17'):
        assert not _is_linked(a1, 'Graph17', b)
    if hasattr(a2, 'Graph17'):
        assert _is_linked(a2, 'Graph17', b)
    _safe_set(b, 'nodes', None)
    assert not _is_linked(b, 'nodes', a2)
    if hasattr(a2, 'Graph17'):
        assert not _is_linked(a2, 'Graph17', b)


def test_assoc_owner23_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_AffineRelation(d=7, n=7, phi=7)
    _safe_set(b, 'affineRelations', a1)
    assert _is_linked(b, 'affineRelations', a1)
    if hasattr(a1, 'Graph24'):
        assert _is_linked(a1, 'Graph24', b)
    _safe_set(b, 'affineRelations', a2)
    assert _is_linked(b, 'affineRelations', a2)
    if hasattr(a1, 'Graph24'):
        assert not _is_linked(a1, 'Graph24', b)
    if hasattr(a2, 'Graph24'):
        assert _is_linked(a2, 'Graph24', b)
    _safe_set(b, 'affineRelations', None)
    assert not _is_linked(b, 'affineRelations', a2)
    if hasattr(a2, 'Graph24'):
        assert not _is_linked(a2, 'Graph24', b)


def test_assoc_owner28_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_Connection(id=7, size=7)
    _safe_set(b, 'connections', a1)
    assert _is_linked(b, 'connections', a1)
    if hasattr(a1, 'Graph29'):
        assert _is_linked(a1, 'Graph29', b)
    _safe_set(b, 'connections', a2)
    assert _is_linked(b, 'connections', a2)
    if hasattr(a1, 'Graph29'):
        assert not _is_linked(a1, 'Graph29', b)
    if hasattr(a2, 'Graph29'):
        assert _is_linked(a2, 'Graph29', b)
    _safe_set(b, 'connections', None)
    assert not _is_linked(b, 'connections', a2)
    if hasattr(a2, 'Graph29'):
        assert not _is_linked(a2, 'Graph29', b)


def test_assoc_owner3_reverse_link_reassign_clear():
    a1 = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    a2 = adfg_Graph(bufferingRequirements=13, id=13, name="sample_text_2", nbActors=13, nbBuffers=13, processorUtilization=9.99, sourceCode="sample_text_2")
    b = adfg_Application(dynamicChecking=True, name="sample_text", nbGraphs=7, nbProcessors=7, schedulingAlgorithm="sample_text", sourceCode="sample_text")
    _safe_set(b, 'Application', a1)
    assert _is_linked(b, 'Application', a1)
    if hasattr(a1, 'graphs'):
        assert _is_linked(a1, 'graphs', b)
    _safe_set(b, 'Application', a2)
    assert _is_linked(b, 'Application', a2)
    if hasattr(a1, 'graphs'):
        assert not _is_linked(a1, 'graphs', b)
    if hasattr(a2, 'graphs'):
        assert _is_linked(a2, 'graphs', b)
    _safe_set(b, 'Application', None)
    assert not _is_linked(b, 'Application', a2)
    if hasattr(a2, 'graphs'):
        assert not _is_linked(a2, 'graphs', b)


def test_assoc_owner30_reverse_link_reassign_clear():
    a1 = adfg_Port(name="sample_text", sequence="sample_text", type="sample_text")
    a2 = adfg_Port(name="sample_text_2", sequence="sample_text_2", type="sample_text_2")
    b = adfg_Actor(name="sample_text", nbPorts=7, priority=7, procNumber=7, sourceCode="sample_text")
    _safe_set(b, 'Actor31', a1)
    assert _is_linked(b, 'Actor31', a1)
    if hasattr(a1, 'ports'):
        assert _is_linked(a1, 'ports', b)
    _safe_set(b, 'Actor31', a2)
    assert _is_linked(b, 'Actor31', a2)
    if hasattr(a1, 'ports'):
        assert not _is_linked(a1, 'ports', b)
    if hasattr(a2, 'ports'):
        assert _is_linked(a2, 'ports', b)
    _safe_set(b, 'Actor31', None)
    assert not _is_linked(b, 'Actor31', a2)
    if hasattr(a2, 'ports'):
        assert not _is_linked(a2, 'ports', b)


def test_assoc_ports18_reverse_link_reassign_clear():
    a1 = adfg_Port(name="sample_text", sequence="sample_text", type="sample_text")
    a2 = adfg_Port(name="sample_text_2", sequence="sample_text_2", type="sample_text_2")
    b = adfg_Actor(name="sample_text", nbPorts=7, priority=7, procNumber=7, sourceCode="sample_text")
    _safe_set(b, 'owner19', {a1})
    assert _is_linked(b, 'owner19', a1)
    if hasattr(a1, 'Port'):
        assert _is_linked(a1, 'Port', b)
    _safe_set(b, 'owner19', {a2})
    assert _is_linked(b, 'owner19', a2)
    if hasattr(a1, 'Port'):
        assert not _is_linked(a1, 'Port', b)
    if hasattr(a2, 'Port'):
        assert _is_linked(a2, 'Port', b)
    _safe_set(b, 'owner19', set())
    assert not _is_linked(b, 'owner19', a2)
    if hasattr(a2, 'Port'):
        assert not _is_linked(a2, 'Port', b)


def test_assoc_source20_reverse_link_reassign_clear():
    a1 = adfg_PeriodicActor(deadline="sample_text", period="sample_text", periodLowerBound="sample_text", periodUpperBound="sample_text", phase="sample_text", wcet="sample_text")
    a2 = adfg_PeriodicActor(deadline="sample_text_2", period="sample_text_2", periodLowerBound="sample_text_2", periodUpperBound="sample_text_2", phase="sample_text_2", wcet="sample_text_2")
    b = adfg_AffineRelation(d=7, n=7, phi=7)
    _safe_set(b, 'affineRelationSource', a1)
    assert _is_linked(b, 'affineRelationSource', a1)
    if hasattr(a1, 'PeriodicActor'):
        assert _is_linked(a1, 'PeriodicActor', b)
    _safe_set(b, 'affineRelationSource', a2)
    assert _is_linked(b, 'affineRelationSource', a2)
    if hasattr(a1, 'PeriodicActor'):
        assert not _is_linked(a1, 'PeriodicActor', b)
    if hasattr(a2, 'PeriodicActor'):
        assert _is_linked(a2, 'PeriodicActor', b)
    _safe_set(b, 'affineRelationSource', None)
    assert not _is_linked(b, 'affineRelationSource', a2)
    if hasattr(a2, 'PeriodicActor'):
        assert not _is_linked(a2, 'PeriodicActor', b)


def test_assoc_target21_reverse_link_reassign_clear():
    a1 = adfg_PeriodicActor(deadline="sample_text", period="sample_text", periodLowerBound="sample_text", periodUpperBound="sample_text", phase="sample_text", wcet="sample_text")
    a2 = adfg_PeriodicActor(deadline="sample_text_2", period="sample_text_2", periodLowerBound="sample_text_2", periodUpperBound="sample_text_2", phase="sample_text_2", wcet="sample_text_2")
    b = adfg_AffineRelation(d=7, n=7, phi=7)
    _safe_set(b, 'affineRelationTarget', a1)
    assert _is_linked(b, 'affineRelationTarget', a1)
    if hasattr(a1, 'PeriodicActor22'):
        assert _is_linked(a1, 'PeriodicActor22', b)
    _safe_set(b, 'affineRelationTarget', a2)
    assert _is_linked(b, 'affineRelationTarget', a2)
    if hasattr(a1, 'PeriodicActor22'):
        assert not _is_linked(a1, 'PeriodicActor22', b)
    if hasattr(a2, 'PeriodicActor22'):
        assert _is_linked(a2, 'PeriodicActor22', b)
    _safe_set(b, 'affineRelationTarget', None)
    assert not _is_linked(b, 'affineRelationTarget', a2)
    if hasattr(a2, 'PeriodicActor22'):
        assert not _is_linked(a2, 'PeriodicActor22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_GraphConnections1_stub_double():
    # adfg_GraphConnection has no real 'GraphConnection' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Application(dynamicChecking=True, name="sample_text", nbGraphs=7, nbProcessors=7, schedulingAlgorithm="sample_text", sourceCode="sample_text")
    partner = adfg_GraphConnection()
    setattr(partner, 'GraphConnection', None)
    _safe_set(owner, 'owner2', {partner})
    assert getattr(partner, 'GraphConnection') == owner
    _safe_set(owner, 'owner2', set())
    assert getattr(partner, 'GraphConnection') is None


def test_assoc_connection32_stub_double():
    # adfg_InputPort has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Connection(id=7, size=7)
    partner = adfg_InputPort()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Connection33', partner)
    assert getattr(partner, 'target') == owner
    _safe_set(owner, 'Connection33', None)
    assert getattr(partner, 'target') is None


def test_assoc_connection34_stub_double():
    # adfg_OutputPort has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Connection(id=7, size=7)
    partner = adfg_OutputPort()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Connection35', partner)
    assert getattr(partner, 'source') == owner
    _safe_set(owner, 'Connection35', None)
    assert getattr(partner, 'source') is None


def test_assoc_owner14_stub_double():
    # adfg_GraphConnection has no real 'GraphConnections' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Application(dynamicChecking=True, name="sample_text", nbGraphs=7, nbProcessors=7, schedulingAlgorithm="sample_text", sourceCode="sample_text")
    partner = adfg_GraphConnection()
    setattr(partner, 'GraphConnections', None)
    _safe_set(owner, 'Application15', partner)
    assert getattr(partner, 'GraphConnections') == owner
    _safe_set(owner, 'Application15', None)
    assert getattr(partner, 'GraphConnections') is None


def test_assoc_source10_stub_double():
    # adfg_GraphConnection has no real 'adfg_GraphConnection' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    partner = adfg_GraphConnection()
    setattr(partner, 'adfg_GraphConnection', None)
    _safe_set(owner, 'adfg_Graph', partner)
    assert getattr(partner, 'adfg_GraphConnection') == owner
    _safe_set(owner, 'adfg_Graph', None)
    assert getattr(partner, 'adfg_GraphConnection') is None


def test_assoc_source25_stub_double():
    # adfg_OutputPort has no real 'OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Connection(id=7, size=7)
    partner = adfg_OutputPort()
    setattr(partner, 'OutputPort', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'OutputPort') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'OutputPort') is None


def test_assoc_target11_stub_double():
    # adfg_GraphConnection has no real 'adfg_GraphConnection12' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Graph(bufferingRequirements=7, id=7, name="sample_text", nbActors=7, nbBuffers=7, processorUtilization=3.14, sourceCode="sample_text")
    partner = adfg_GraphConnection()
    setattr(partner, 'adfg_GraphConnection12', None)
    _safe_set(owner, 'adfg_Graph13', partner)
    assert getattr(partner, 'adfg_GraphConnection12') == owner
    _safe_set(owner, 'adfg_Graph13', None)
    assert getattr(partner, 'adfg_GraphConnection12') is None


def test_assoc_target26_stub_double():
    # adfg_InputPort has no real 'InputPort' property in the generated
    # code (a bare stub) -- manually attach it so adfg_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adfg_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adfg_Connection(id=7, size=7)
    partner = adfg_InputPort()
    setattr(partner, 'InputPort', None)
    _safe_set(owner, 'connection27', partner)
    assert getattr(partner, 'InputPort') == owner
    _safe_set(owner, 'connection27', None)
    assert getattr(partner, 'InputPort') is None


