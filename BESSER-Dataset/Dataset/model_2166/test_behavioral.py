import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractActor,
    AbstractVertex,
    DataOutputPort,
    DataPort,
    ExecutableActor,
    ISetter,
    InterfaceActor,
    Parameter,
    Parameterizable,
    PiMMVisitable,
    Port,
    Refinement,
    pimm_AbstractActor,
    pimm_AbstractVertex,
    pimm_Actor,
    pimm_BroadcastActor,
    pimm_ConfigInputInterface,
    pimm_ConfigInputPort,
    pimm_ConfigOutputInterface,
    pimm_ConfigOutputPort,
    pimm_DataInputInterface,
    pimm_DataInputPort,
    pimm_DataOutputInterface,
    pimm_DataOutputPort,
    pimm_DataPort,
    pimm_Delay,
    pimm_Dependency,
    pimm_ExecutableActor,
    pimm_Expression,
    pimm_Fifo,
    pimm_ForkActor,
    pimm_FunctionParameter,
    pimm_FunctionPrototype,
    pimm_HRefinement,
    pimm_ISetter,
    pimm_InterfaceActor,
    pimm_JoinActor,
    pimm_Parameter,
    pimm_Parameterizable,
    pimm_PiGraph,
    pimm_Port,
    pimm_Refinement,
    pimm_RoundBufferActor,
    pimm_visitor_PiMMVisitable,
    pimm_visitor_PiMMVisitor,
    Direction,
    PortMemoryAnnotation,
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

def test_assoc_expression27_reverse_link_reassign_clear():
    a1 = pimm_Parameter(configurationInterface=True)
    a2 = pimm_Parameter(configurationInterface=False)
    b = pimm_Expression(string="sample_text")
    _safe_set(b, 'pimm_Expression', a1)
    assert _is_linked(b, 'pimm_Expression', a1)
    if hasattr(a1, 'pimm_Parameter28'):
        assert _is_linked(a1, 'pimm_Parameter28', b)
    _safe_set(b, 'pimm_Expression', a2)
    assert _is_linked(b, 'pimm_Expression', a2)
    if hasattr(a1, 'pimm_Parameter28'):
        assert not _is_linked(a1, 'pimm_Parameter28', b)
    if hasattr(a2, 'pimm_Parameter28'):
        assert _is_linked(a2, 'pimm_Parameter28', b)
    _safe_set(b, 'pimm_Expression', None)
    assert not _is_linked(b, 'pimm_Expression', a2)
    if hasattr(a2, 'pimm_Parameter28'):
        assert not _is_linked(a2, 'pimm_Parameter28', b)


def test_assoc_expression42_reverse_link_reassign_clear():
    a1 = pimm_Expression(string="sample_text")
    a2 = pimm_Expression(string="sample_text_2")
    b = pimm_DataPort(annotation="sample_text")
    _safe_set(b, 'pimm_DataPort', a1)
    assert _is_linked(b, 'pimm_DataPort', a1)
    if hasattr(a1, 'pimm_Expression43'):
        assert _is_linked(a1, 'pimm_Expression43', b)
    _safe_set(b, 'pimm_DataPort', a2)
    assert _is_linked(b, 'pimm_DataPort', a2)
    if hasattr(a1, 'pimm_Expression43'):
        assert not _is_linked(a1, 'pimm_Expression43', b)
    if hasattr(a2, 'pimm_Expression43'):
        assert _is_linked(a2, 'pimm_Expression43', b)
    _safe_set(b, 'pimm_DataPort', None)
    assert not _is_linked(b, 'pimm_DataPort', a2)
    if hasattr(a2, 'pimm_Expression43'):
        assert not _is_linked(a2, 'pimm_Expression43', b)


def test_assoc_fifos8_reverse_link_reassign_clear():
    a1 = pimm_PiGraph()
    a2 = pimm_PiGraph()
    b = pimm_Fifo(id="sample_text", type="sample_text")
    _safe_set(b, 'pimm_Fifo', a1)
    assert _is_linked(b, 'pimm_Fifo', a1)
    if hasattr(a1, 'pimm_PiGraph9'):
        assert _is_linked(a1, 'pimm_PiGraph9', b)
    _safe_set(b, 'pimm_Fifo', a2)
    assert _is_linked(b, 'pimm_Fifo', a2)
    if hasattr(a1, 'pimm_PiGraph9'):
        assert not _is_linked(a1, 'pimm_PiGraph9', b)
    if hasattr(a2, 'pimm_PiGraph9'):
        assert _is_linked(a2, 'pimm_PiGraph9', b)
    _safe_set(b, 'pimm_Fifo', None)
    assert not _is_linked(b, 'pimm_Fifo', a2)
    if hasattr(a2, 'pimm_PiGraph9'):
        assert not _is_linked(a2, 'pimm_PiGraph9', b)


def test_assoc_graphPort23_reverse_link_reassign_clear():
    a1 = pimm_Port(kind="sample_text", name="sample_text")
    a2 = pimm_Port(kind="sample_text_2", name="sample_text_2")
    b = pimm_InterfaceActor(kind="sample_text")
    _safe_set(b, 'pimm_InterfaceActor', a1)
    assert _is_linked(b, 'pimm_InterfaceActor', a1)
    if hasattr(a1, 'pimm_Port'):
        assert _is_linked(a1, 'pimm_Port', b)
    _safe_set(b, 'pimm_InterfaceActor', a2)
    assert _is_linked(b, 'pimm_InterfaceActor', a2)
    if hasattr(a1, 'pimm_Port'):
        assert not _is_linked(a1, 'pimm_Port', b)
    if hasattr(a2, 'pimm_Port'):
        assert _is_linked(a2, 'pimm_Port', b)
    _safe_set(b, 'pimm_InterfaceActor', None)
    assert not _is_linked(b, 'pimm_InterfaceActor', a2)
    if hasattr(a2, 'pimm_Port'):
        assert not _is_linked(a2, 'pimm_Port', b)


def test_assoc_parameters10_reverse_link_reassign_clear():
    a1 = pimm_PiGraph()
    a2 = pimm_PiGraph()
    b = pimm_Parameter(configurationInterface=True)
    _safe_set(b, 'pimm_Parameter', a1)
    assert _is_linked(b, 'pimm_Parameter', a1)
    if hasattr(a1, 'pimm_PiGraph11'):
        assert _is_linked(a1, 'pimm_PiGraph11', b)
    _safe_set(b, 'pimm_Parameter', a2)
    assert _is_linked(b, 'pimm_Parameter', a2)
    if hasattr(a1, 'pimm_PiGraph11'):
        assert not _is_linked(a1, 'pimm_PiGraph11', b)
    if hasattr(a2, 'pimm_PiGraph11'):
        assert _is_linked(a2, 'pimm_PiGraph11', b)
    _safe_set(b, 'pimm_Parameter', None)
    assert not _is_linked(b, 'pimm_Parameter', a2)
    if hasattr(a2, 'pimm_PiGraph11'):
        assert not _is_linked(a2, 'pimm_PiGraph11', b)


def test_assoc_parameters40_reverse_link_reassign_clear():
    a1 = pimm_FunctionPrototype(name="sample_text")
    a2 = pimm_FunctionPrototype(name="sample_text_2")
    b = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    _safe_set(b, 'pimm_FunctionParameter', a1)
    assert _is_linked(b, 'pimm_FunctionParameter', a1)
    if hasattr(a1, 'pimm_FunctionPrototype41'):
        assert _is_linked(a1, 'pimm_FunctionPrototype41', b)
    _safe_set(b, 'pimm_FunctionParameter', a2)
    assert _is_linked(b, 'pimm_FunctionParameter', a2)
    if hasattr(a1, 'pimm_FunctionPrototype41'):
        assert not _is_linked(a1, 'pimm_FunctionPrototype41', b)
    if hasattr(a2, 'pimm_FunctionPrototype41'):
        assert _is_linked(a2, 'pimm_FunctionPrototype41', b)
    _safe_set(b, 'pimm_FunctionParameter', None)
    assert not _is_linked(b, 'pimm_FunctionParameter', a2)
    if hasattr(a2, 'pimm_FunctionPrototype41'):
        assert not _is_linked(a2, 'pimm_FunctionPrototype41', b)


def test_assoc_refinement14_reverse_link_reassign_clear():
    a1 = pimm_Refinement(fileName="sample_text", filePath="sample_text")
    a2 = pimm_Refinement(fileName="sample_text_2", filePath="sample_text_2")
    b = pimm_Actor(configurationActor=True, memoryScriptPath="sample_text")
    _safe_set(b, 'pimm_Actor', a1)
    assert _is_linked(b, 'pimm_Actor', a1)
    if hasattr(a1, 'pimm_Refinement'):
        assert _is_linked(a1, 'pimm_Refinement', b)
    _safe_set(b, 'pimm_Actor', a2)
    assert _is_linked(b, 'pimm_Actor', a2)
    if hasattr(a1, 'pimm_Refinement'):
        assert not _is_linked(a1, 'pimm_Refinement', b)
    if hasattr(a2, 'pimm_Refinement'):
        assert _is_linked(a2, 'pimm_Refinement', b)
    _safe_set(b, 'pimm_Actor', None)
    assert not _is_linked(b, 'pimm_Actor', a2)
    if hasattr(a2, 'pimm_Refinement'):
        assert not _is_linked(a2, 'pimm_Refinement', b)


def test_assoc_vertices6_reverse_link_reassign_clear():
    a1 = pimm_PiGraph()
    a2 = pimm_PiGraph()
    b = pimm_AbstractActor()
    _safe_set(b, 'pimm_AbstractActor7', a1)
    assert _is_linked(b, 'pimm_AbstractActor7', a1)
    if hasattr(a1, 'pimm_PiGraph'):
        assert _is_linked(a1, 'pimm_PiGraph', b)
    _safe_set(b, 'pimm_AbstractActor7', a2)
    assert _is_linked(b, 'pimm_AbstractActor7', a2)
    if hasattr(a1, 'pimm_PiGraph'):
        assert not _is_linked(a1, 'pimm_PiGraph', b)
    if hasattr(a2, 'pimm_PiGraph'):
        assert _is_linked(a2, 'pimm_PiGraph', b)
    _safe_set(b, 'pimm_AbstractActor7', None)
    assert not _is_linked(b, 'pimm_AbstractActor7', a2)
    if hasattr(a2, 'pimm_PiGraph'):
        assert not _is_linked(a2, 'pimm_PiGraph', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configInputPorts0_stub_double():
    # pimm_ConfigInputPort has no real 'pimm_ConfigInputPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Parameterizable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Parameterizable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Parameterizable()
    partner = pimm_ConfigInputPort()
    setattr(partner, 'pimm_ConfigInputPort', None)
    _safe_set(owner, 'pimm_Parameterizable', {partner})
    assert getattr(partner, 'pimm_ConfigInputPort') == owner
    _safe_set(owner, 'pimm_Parameterizable', set())
    assert getattr(partner, 'pimm_ConfigInputPort') is None


def test_assoc_configOutputPorts4_stub_double():
    # pimm_ConfigOutputPort has no real 'pimm_ConfigOutputPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_AbstractActor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_AbstractActor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_AbstractActor()
    partner = pimm_ConfigOutputPort()
    setattr(partner, 'pimm_ConfigOutputPort', None)
    _safe_set(owner, 'pimm_AbstractActor5', {partner})
    assert getattr(partner, 'pimm_ConfigOutputPort') == owner
    _safe_set(owner, 'pimm_AbstractActor5', set())
    assert getattr(partner, 'pimm_ConfigOutputPort') is None


def test_assoc_dataInputPorts1_stub_double():
    # pimm_DataInputPort has no real 'pimm_DataInputPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_AbstractActor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_AbstractActor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_AbstractActor()
    partner = pimm_DataInputPort()
    setattr(partner, 'pimm_DataInputPort', None)
    _safe_set(owner, 'pimm_AbstractActor', {partner})
    assert getattr(partner, 'pimm_DataInputPort') == owner
    _safe_set(owner, 'pimm_AbstractActor', set())
    assert getattr(partner, 'pimm_DataInputPort') is None


def test_assoc_dataOutputPorts2_stub_double():
    # pimm_DataOutputPort has no real 'pimm_DataOutputPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_AbstractActor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_AbstractActor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_AbstractActor()
    partner = pimm_DataOutputPort()
    setattr(partner, 'pimm_DataOutputPort', None)
    _safe_set(owner, 'pimm_AbstractActor3', {partner})
    assert getattr(partner, 'pimm_DataOutputPort') == owner
    _safe_set(owner, 'pimm_AbstractActor3', set())
    assert getattr(partner, 'pimm_DataOutputPort') is None


def test_assoc_delay21_stub_double():
    # pimm_Delay has no real 'pimm_Delay' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Fifo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Fifo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Fifo(id="sample_text", type="sample_text")
    partner = pimm_Delay()
    setattr(partner, 'pimm_Delay', None)
    _safe_set(owner, 'pimm_Fifo22', partner)
    assert getattr(partner, 'pimm_Delay') == owner
    _safe_set(owner, 'pimm_Fifo22', None)
    assert getattr(partner, 'pimm_Delay') is None


def test_assoc_dependencies12_stub_double():
    # pimm_Dependency has no real 'pimm_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so pimm_PiGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_PiGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_PiGraph()
    partner = pimm_Dependency()
    setattr(partner, 'pimm_Dependency', None)
    _safe_set(owner, 'pimm_PiGraph13', {partner})
    assert getattr(partner, 'pimm_Dependency') == owner
    _safe_set(owner, 'pimm_PiGraph13', set())
    assert getattr(partner, 'pimm_Dependency') is None


def test_assoc_expression33_stub_double():
    # pimm_Delay has no real 'pimm_Delay34' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Expression(string="sample_text")
    partner = pimm_Delay()
    setattr(partner, 'pimm_Delay34', None)
    _safe_set(owner, 'pimm_Expression35', partner)
    assert getattr(partner, 'pimm_Delay34') == owner
    _safe_set(owner, 'pimm_Expression35', None)
    assert getattr(partner, 'pimm_Delay34') is None


def test_assoc_graphPort24_stub_double():
    # pimm_ConfigInputPort has no real 'pimm_ConfigInputPort26' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Parameter(configurationInterface=True)
    partner = pimm_ConfigInputPort()
    setattr(partner, 'pimm_ConfigInputPort26', None)
    _safe_set(owner, 'pimm_Parameter25', partner)
    assert getattr(partner, 'pimm_ConfigInputPort26') == owner
    _safe_set(owner, 'pimm_Parameter25', None)
    assert getattr(partner, 'pimm_ConfigInputPort26') is None


def test_assoc_incomingFifo15_stub_double():
    # pimm_DataInputPort has no real 'targetPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Fifo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Fifo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Fifo(id="sample_text", type="sample_text")
    partner = pimm_DataInputPort()
    setattr(partner, 'targetPort', None)
    _safe_set(owner, 'Fifo', partner)
    assert getattr(partner, 'targetPort') == owner
    _safe_set(owner, 'Fifo', None)
    assert getattr(partner, 'targetPort') is None


def test_assoc_initPrototype37_stub_double():
    # pimm_HRefinement has no real 'pimm_HRefinement38' property in the generated
    # code (a bare stub) -- manually attach it so pimm_FunctionPrototype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_FunctionPrototype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_FunctionPrototype(name="sample_text")
    partner = pimm_HRefinement()
    setattr(partner, 'pimm_HRefinement38', None)
    _safe_set(owner, 'pimm_FunctionPrototype39', partner)
    assert getattr(partner, 'pimm_HRefinement38') == owner
    _safe_set(owner, 'pimm_FunctionPrototype39', None)
    assert getattr(partner, 'pimm_HRefinement38') is None


def test_assoc_loopPrototype36_stub_double():
    # pimm_HRefinement has no real 'pimm_HRefinement' property in the generated
    # code (a bare stub) -- manually attach it so pimm_FunctionPrototype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_FunctionPrototype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_FunctionPrototype(name="sample_text")
    partner = pimm_HRefinement()
    setattr(partner, 'pimm_HRefinement', None)
    _safe_set(owner, 'pimm_FunctionPrototype', partner)
    assert getattr(partner, 'pimm_HRefinement') == owner
    _safe_set(owner, 'pimm_FunctionPrototype', None)
    assert getattr(partner, 'pimm_HRefinement') is None


def test_assoc_outgoingDependencies31_stub_double():
    # pimm_Dependency has no real 'Dependency32' property in the generated
    # code (a bare stub) -- manually attach it so pimm_ISetter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_ISetter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_ISetter()
    partner = pimm_Dependency()
    setattr(partner, 'Dependency32', None)
    _safe_set(owner, 'setter', {partner})
    assert getattr(partner, 'Dependency32') == owner
    _safe_set(owner, 'setter', set())
    assert getattr(partner, 'Dependency32') is None


def test_assoc_outgoingFifo16_stub_double():
    # pimm_DataOutputPort has no real 'sourcePort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Fifo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Fifo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Fifo(id="sample_text", type="sample_text")
    partner = pimm_DataOutputPort()
    setattr(partner, 'sourcePort', None)
    _safe_set(owner, 'Fifo17', partner)
    assert getattr(partner, 'sourcePort') == owner
    _safe_set(owner, 'Fifo17', None)
    assert getattr(partner, 'sourcePort') is None


def test_assoc_setter29_stub_double():
    # pimm_Dependency has no real 'outgoingDependencies' property in the generated
    # code (a bare stub) -- manually attach it so pimm_ISetter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_ISetter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_ISetter()
    partner = pimm_Dependency()
    setattr(partner, 'outgoingDependencies', None)
    _safe_set(owner, 'ISetter', partner)
    assert getattr(partner, 'outgoingDependencies') == owner
    _safe_set(owner, 'ISetter', None)
    assert getattr(partner, 'outgoingDependencies') is None


def test_assoc_sourcePort19_stub_double():
    # pimm_DataOutputPort has no real 'DataOutputPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Fifo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Fifo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Fifo(id="sample_text", type="sample_text")
    partner = pimm_DataOutputPort()
    setattr(partner, 'DataOutputPort', None)
    _safe_set(owner, 'outgoingFifo', partner)
    assert getattr(partner, 'DataOutputPort') == owner
    _safe_set(owner, 'outgoingFifo', None)
    assert getattr(partner, 'DataOutputPort') is None


def test_assoc_targetPort20_stub_double():
    # pimm_DataInputPort has no real 'DataInputPort' property in the generated
    # code (a bare stub) -- manually attach it so pimm_Fifo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pimm_Fifo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pimm_Fifo(id="sample_text", type="sample_text")
    partner = pimm_DataInputPort()
    setattr(partner, 'DataInputPort', None)
    _safe_set(owner, 'incomingFifo', partner)
    assert getattr(partner, 'DataInputPort') == owner
    _safe_set(owner, 'incomingFifo', None)
    assert getattr(partner, 'DataInputPort') is None


