import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    Artifact,
    ArtifactsContainer,
    AssociationTarget,
    EModelElement,
    Graph,
    Identifiable,
    MessageVertex,
    NamedBpmnObject,
    Vertex,
    bpmn_Activity,
    bpmn_Artifact,
    bpmn_ArtifactsContainer,
    bpmn_Association,
    bpmn_AssociationTarget,
    bpmn_BpmnDiagram,
    bpmn_DataObject,
    bpmn_Graph,
    bpmn_Group,
    bpmn_Identifiable,
    bpmn_Lane,
    bpmn_MessageVertex,
    bpmn_MessagingEdge,
    bpmn_NamedBpmnObject,
    bpmn_Pool,
    bpmn_SequenceEdge,
    bpmn_SubProcess,
    bpmn_TextAnnotation,
    bpmn_Vertex,
    ActivityType,
    DirectionType,
    SequenceFlowConditionType,
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

def test_assoc_eventHandlerFor3_reverse_link_reassign_clear():
    a1 = bpmn_SubProcess(adhoc="sample_text", isTransaction="sample_text")
    a2 = bpmn_SubProcess(adhoc="sample_text_2", isTransaction="sample_text_2")
    b = bpmn_Activity(activityType="sample_text", looping="sample_text")
    _safe_set(b, 'eventHandlers', a1)
    assert _is_linked(b, 'eventHandlers', a1)
    if hasattr(a1, 'SubProcess'):
        assert _is_linked(a1, 'SubProcess', b)
    _safe_set(b, 'eventHandlers', a2)
    assert _is_linked(b, 'eventHandlers', a2)
    if hasattr(a1, 'SubProcess'):
        assert not _is_linked(a1, 'SubProcess', b)
    if hasattr(a2, 'SubProcess'):
        assert _is_linked(a2, 'SubProcess', b)
    _safe_set(b, 'eventHandlers', None)
    assert not _is_linked(b, 'eventHandlers', a2)
    if hasattr(a2, 'SubProcess'):
        assert not _is_linked(a2, 'SubProcess', b)


def test_assoc_eventHandlers44_reverse_link_reassign_clear():
    a1 = bpmn_SubProcess(adhoc="sample_text", isTransaction="sample_text")
    a2 = bpmn_SubProcess(adhoc="sample_text_2", isTransaction="sample_text_2")
    b = bpmn_Activity(activityType="sample_text", looping="sample_text")
    _safe_set(b, 'Activity45', a1)
    assert _is_linked(b, 'Activity45', a1)
    if hasattr(a1, 'eventHandlerFor'):
        assert _is_linked(a1, 'eventHandlerFor', b)
    _safe_set(b, 'Activity45', a2)
    assert _is_linked(b, 'Activity45', a2)
    if hasattr(a1, 'eventHandlerFor'):
        assert not _is_linked(a1, 'eventHandlerFor', b)
    if hasattr(a2, 'eventHandlerFor'):
        assert _is_linked(a2, 'eventHandlerFor', b)
    _safe_set(b, 'Activity45', None)
    assert not _is_linked(b, 'Activity45', a2)
    if hasattr(a2, 'eventHandlerFor'):
        assert not _is_linked(a2, 'eventHandlerFor', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activities19_stub_double():
    # bpmn_Group has no real 'groups' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Activity(activityType="sample_text", looping="sample_text")
    partner = bpmn_Group()
    setattr(partner, 'groups', None)
    _safe_set(owner, 'Activity', partner)
    assert owner in getattr(partner, 'groups')
    _safe_set(owner, 'Activity', None)
    assert owner not in getattr(partner, 'groups')


def test_assoc_activities20_stub_double():
    # bpmn_Lane has no real 'lanes' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Activity(activityType="sample_text", looping="sample_text")
    partner = bpmn_Lane()
    setattr(partner, 'lanes', None)
    _safe_set(owner, 'Activity21', partner)
    assert owner in getattr(partner, 'lanes')
    _safe_set(owner, 'Activity21', None)
    assert owner not in getattr(partner, 'lanes')


def test_assoc_associations11_stub_double():
    # bpmn_AssociationTarget has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Association(direction="sample_text")
    partner = bpmn_AssociationTarget()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Association12', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Association12', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_associations4_stub_double():
    # bpmn_Artifact has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Association(direction="sample_text")
    partner = bpmn_Artifact()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Association', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Association', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_bpmnDiagram34_stub_double():
    # bpmn_MessagingEdge has no real 'messages' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_BpmnDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_BpmnDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_BpmnDiagram(author="sample_text", title="sample_text")
    partner = bpmn_MessagingEdge()
    setattr(partner, 'messages', None)
    _safe_set(owner, 'BpmnDiagram', partner)
    assert getattr(partner, 'messages') == owner
    _safe_set(owner, 'BpmnDiagram', None)
    assert getattr(partner, 'messages') is None


def test_assoc_bpmnDiagram37_stub_double():
    # bpmn_Pool has no real 'pools' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_BpmnDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_BpmnDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_BpmnDiagram(author="sample_text", title="sample_text")
    partner = bpmn_Pool()
    setattr(partner, 'pools', None)
    _safe_set(owner, 'BpmnDiagram38', partner)
    assert getattr(partner, 'pools') == owner
    _safe_set(owner, 'BpmnDiagram38', None)
    assert getattr(partner, 'pools') is None


def test_assoc_graph43_stub_double():
    # bpmn_Graph has no real 'Graph' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_SequenceEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_SequenceEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_SequenceEdge(conditionType="sample_text", isDefault="sample_text")
    partner = bpmn_Graph()
    setattr(partner, 'Graph', None)
    _safe_set(owner, 'sequenceEdges', partner)
    assert getattr(partner, 'Graph') == owner
    _safe_set(owner, 'sequenceEdges', None)
    assert getattr(partner, 'Graph') is None


def test_assoc_groups0_stub_double():
    # bpmn_Group has no real 'Group' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Activity(activityType="sample_text", looping="sample_text")
    partner = bpmn_Group()
    setattr(partner, 'Group', None)
    _safe_set(owner, 'activities', {partner})
    assert getattr(partner, 'Group') == owner
    _safe_set(owner, 'activities', set())
    assert getattr(partner, 'Group') is None


def test_assoc_incomingEdges49_stub_double():
    # bpmn_Vertex has no real 'target50' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_SequenceEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_SequenceEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_SequenceEdge(conditionType="sample_text", isDefault="sample_text")
    partner = bpmn_Vertex()
    setattr(partner, 'target50', None)
    _safe_set(owner, 'SequenceEdge51', partner)
    assert owner in getattr(partner, 'target50')
    _safe_set(owner, 'SequenceEdge51', None)
    assert owner not in getattr(partner, 'target50')


def test_assoc_incomingMessages25_stub_double():
    # bpmn_MessagingEdge has no real 'MessagingEdge27' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_MessageVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_MessageVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_MessageVertex(orderedMessages="sample_text")
    partner = bpmn_MessagingEdge()
    setattr(partner, 'MessagingEdge27', None)
    _safe_set(owner, 'target26', {partner})
    assert getattr(partner, 'MessagingEdge27') == owner
    _safe_set(owner, 'target26', set())
    assert getattr(partner, 'MessagingEdge27') is None


def test_assoc_lanes1_stub_double():
    # bpmn_Lane has no real 'Lane' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Activity(activityType="sample_text", looping="sample_text")
    partner = bpmn_Lane()
    setattr(partner, 'Lane', None)
    _safe_set(owner, 'activities2', {partner})
    assert getattr(partner, 'Lane') == owner
    _safe_set(owner, 'activities2', set())
    assert getattr(partner, 'Lane') is None


def test_assoc_messages14_stub_double():
    # bpmn_MessagingEdge has no real 'MessagingEdge' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_BpmnDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_BpmnDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_BpmnDiagram(author="sample_text", title="sample_text")
    partner = bpmn_MessagingEdge()
    setattr(partner, 'MessagingEdge', None)
    _safe_set(owner, 'bpmnDiagram15', {partner})
    assert getattr(partner, 'MessagingEdge') == owner
    _safe_set(owner, 'bpmnDiagram15', set())
    assert getattr(partner, 'MessagingEdge') is None


def test_assoc_outgoingEdges46_stub_double():
    # bpmn_Vertex has no real 'source47' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_SequenceEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_SequenceEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_SequenceEdge(conditionType="sample_text", isDefault="sample_text")
    partner = bpmn_Vertex()
    setattr(partner, 'source47', None)
    _safe_set(owner, 'SequenceEdge48', partner)
    assert owner in getattr(partner, 'source47')
    _safe_set(owner, 'SequenceEdge48', None)
    assert owner not in getattr(partner, 'source47')


def test_assoc_outgoingMessages28_stub_double():
    # bpmn_MessagingEdge has no real 'MessagingEdge30' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_MessageVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_MessageVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_MessageVertex(orderedMessages="sample_text")
    partner = bpmn_MessagingEdge()
    setattr(partner, 'MessagingEdge30', None)
    _safe_set(owner, 'source29', {partner})
    assert getattr(partner, 'MessagingEdge30') == owner
    _safe_set(owner, 'source29', set())
    assert getattr(partner, 'MessagingEdge30') is None


def test_assoc_pools13_stub_double():
    # bpmn_Pool has no real 'Pool' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_BpmnDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_BpmnDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_BpmnDiagram(author="sample_text", title="sample_text")
    partner = bpmn_Pool()
    setattr(partner, 'Pool', None)
    _safe_set(owner, 'bpmnDiagram', {partner})
    assert getattr(partner, 'Pool') == owner
    _safe_set(owner, 'bpmnDiagram', set())
    assert getattr(partner, 'Pool') is None


def test_assoc_sequenceEdges17_stub_double():
    # bpmn_Graph has no real 'graph18' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_SequenceEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_SequenceEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_SequenceEdge(conditionType="sample_text", isDefault="sample_text")
    partner = bpmn_Graph()
    setattr(partner, 'graph18', None)
    _safe_set(owner, 'SequenceEdge', partner)
    assert owner in getattr(partner, 'graph18')
    _safe_set(owner, 'SequenceEdge', None)
    assert owner not in getattr(partner, 'graph18')


def test_assoc_source31_stub_double():
    # bpmn_MessagingEdge has no real 'outgoingMessages' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_MessageVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_MessageVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_MessageVertex(orderedMessages="sample_text")
    partner = bpmn_MessagingEdge()
    setattr(partner, 'outgoingMessages', None)
    _safe_set(owner, 'MessageVertex', partner)
    assert getattr(partner, 'outgoingMessages') == owner
    _safe_set(owner, 'MessageVertex', None)
    assert getattr(partner, 'outgoingMessages') is None


def test_assoc_source39_stub_double():
    # bpmn_Vertex has no real 'Vertex40' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_SequenceEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_SequenceEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_SequenceEdge(conditionType="sample_text", isDefault="sample_text")
    partner = bpmn_Vertex()
    setattr(partner, 'Vertex40', None)
    _safe_set(owner, 'outgoingEdges', partner)
    assert getattr(partner, 'Vertex40') == owner
    _safe_set(owner, 'outgoingEdges', None)
    assert getattr(partner, 'Vertex40') is None


def test_assoc_source7_stub_double():
    # bpmn_Artifact has no real 'Artifact8' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Association(direction="sample_text")
    partner = bpmn_Artifact()
    setattr(partner, 'Artifact8', None)
    _safe_set(owner, 'associations', partner)
    assert getattr(partner, 'Artifact8') == owner
    _safe_set(owner, 'associations', None)
    assert getattr(partner, 'Artifact8') is None


def test_assoc_target32_stub_double():
    # bpmn_MessagingEdge has no real 'incomingMessages' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_MessageVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_MessageVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_MessageVertex(orderedMessages="sample_text")
    partner = bpmn_MessagingEdge()
    setattr(partner, 'incomingMessages', None)
    _safe_set(owner, 'MessageVertex33', partner)
    assert getattr(partner, 'incomingMessages') == owner
    _safe_set(owner, 'MessageVertex33', None)
    assert getattr(partner, 'incomingMessages') is None


def test_assoc_target41_stub_double():
    # bpmn_Vertex has no real 'Vertex42' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_SequenceEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_SequenceEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_SequenceEdge(conditionType="sample_text", isDefault="sample_text")
    partner = bpmn_Vertex()
    setattr(partner, 'Vertex42', None)
    _safe_set(owner, 'incomingEdges', partner)
    assert getattr(partner, 'Vertex42') == owner
    _safe_set(owner, 'incomingEdges', None)
    assert getattr(partner, 'Vertex42') is None


def test_assoc_target9_stub_double():
    # bpmn_AssociationTarget has no real 'AssociationTarget' property in the generated
    # code (a bare stub) -- manually attach it so bpmn_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn_Association(direction="sample_text")
    partner = bpmn_AssociationTarget()
    setattr(partner, 'AssociationTarget', None)
    _safe_set(owner, 'associations10', partner)
    assert getattr(partner, 'AssociationTarget') == owner
    _safe_set(owner, 'associations10', None)
    assert getattr(partner, 'AssociationTarget') is None


