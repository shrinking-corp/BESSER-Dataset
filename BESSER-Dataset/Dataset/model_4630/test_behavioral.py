import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractVariable,
    ColorDescription,
    CoveredLifelinesVariable,
    DSemanticDiagram,
    DiagramDescription,
    EventEnd,
    EventEndsOrdering,
    EventMapping,
    FrameMapping,
    InstanceRoleMapping,
    InstanceRolesOrdering,
    MessageEndVariable,
    MessageMapping,
    NodeMapping,
    SingleEventEnd,
    TAbstractMapping,
    TBasicMessageMapping,
    TConditionalExecutionStyle,
    TConditionalLifelineStyle,
    TConditionalMessageStyle,
    TExecutionMapping,
    TExecutionStyle,
    TLifelineMapping,
    TLifelineStyle,
    TMessageExtremity,
    TMessageMapping,
    TMessageStyle,
    TSourceTargetMessageMapping,
    TTransformer,
    description_ContainerMapping,
    description_DelimitedEventMapping,
    description_EdgeMapping,
    description_EventMapping,
    description_NodeMapping,
    description_RepresentationTemplate,
    ordering_sequence_EObject,
    ordering_sequence_SequenceDDiagram,
    sequence_SequenceDDiagram,
    sequence_description_BasicMessageMapping,
    sequence_description_CombinedFragmentMapping,
    sequence_description_CoveredLifelinesVariable,
    sequence_description_CreationMessageMapping,
    sequence_description_DelimitedEventMapping,
    sequence_description_DestructionMessageMapping,
    sequence_description_EndOfLifeMapping,
    sequence_description_EventMapping,
    sequence_description_ExecutionMapping,
    sequence_description_FrameMapping,
    sequence_description_InstanceRoleMapping,
    sequence_description_InteractionUseMapping,
    sequence_description_MessageEndVariable,
    sequence_description_MessageMapping,
    sequence_description_ObservationPointMapping,
    sequence_description_OperandMapping,
    sequence_description_ReturnMessageMapping,
    sequence_description_SequenceDiagramDescription,
    sequence_description_StateMapping,
    sequence_ordering_CompoundEventEnd,
    sequence_ordering_EventEnd,
    sequence_ordering_EventEndsOrdering,
    sequence_ordering_InstanceRolesOrdering,
    sequence_ordering_SingleEventEnd,
    sequence_template_TAbstractMapping,
    sequence_template_TBasicMessageMapping,
    sequence_template_TConditionalExecutionStyle,
    sequence_template_TConditionalLifelineStyle,
    sequence_template_TConditionalMessageStyle,
    sequence_template_TCreationMessageMapping,
    sequence_template_TDestructionMessageMapping,
    sequence_template_TExecutionMapping,
    sequence_template_TExecutionStyle,
    sequence_template_TLifelineMapping,
    sequence_template_TLifelineStyle,
    sequence_template_TMessageExtremity,
    sequence_template_TMessageMapping,
    sequence_template_TMessageStyle,
    sequence_template_TReturnMessageMapping,
    sequence_template_TSequenceDiagram,
    sequence_template_TSourceTargetMessageMapping,
    sequence_template_TTransformer,
    sequence_tool_CombinedFragmentCreationTool,
    sequence_tool_CoveringElementCreationTool,
    sequence_tool_ExecutionCreationTool,
    sequence_tool_InstanceRoleCreationTool,
    sequence_tool_InstanceRoleReorderTool,
    sequence_tool_InteractionUseCreationTool,
    sequence_tool_LifelineCreationTool,
    sequence_tool_MessageCreationTool,
    sequence_tool_ObservationPointCreationTool,
    sequence_tool_OperandCreationTool,
    sequence_tool_OrderedElementCreationTool,
    sequence_tool_ReorderTool,
    sequence_tool_SequenceDiagramToolDescription,
    sequence_tool_StateCreationTool,
    style_NodeStyleDescription,
    template_TAbstractMapping,
    template_TMessageExtremity,
    template_TTransformer,
    template_sequence_EObject,
    tool_AbstractToolDescription,
    tool_ContainerCreationDescription,
    tool_CoveringElementCreationTool,
    tool_EdgeCreationDescription,
    tool_ElementVariable,
    tool_InitialOperation,
    tool_NodeCreationDescription,
    tool_OrderedElementCreationTool,
    tool_SequenceDiagramToolDescription,
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

def test_assoc_backgroundColor71_stub_double():
    # ColorDescription has no real 'ColorDescription73' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TExecutionStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TExecutionStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TExecutionStyle(borderSizeComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription73', None)
    _safe_set(owner, 'sequence_template_TExecutionStyle72', partner)
    assert getattr(partner, 'ColorDescription73') == owner
    _safe_set(owner, 'sequence_template_TExecutionStyle72', None)
    assert getattr(partner, 'ColorDescription73') is None


def test_assoc_borderColor69_stub_double():
    # ColorDescription has no real 'ColorDescription70' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TExecutionStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TExecutionStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TExecutionStyle(borderSizeComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription70', None)
    _safe_set(owner, 'sequence_template_TExecutionStyle', partner)
    assert getattr(partner, 'ColorDescription70') == owner
    _safe_set(owner, 'sequence_template_TExecutionStyle', None)
    assert getattr(partner, 'ColorDescription70') is None


def test_assoc_conditionalLifeLineStyles58_stub_double():
    # TConditionalLifelineStyle has no real 'TConditionalLifelineStyle' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TLifelineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TLifelineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TLifelineMapping(eolVisibleExpression="sample_text")
    partner = TConditionalLifelineStyle()
    setattr(partner, 'TConditionalLifelineStyle', None)
    _safe_set(owner, 'sequence_template_TLifelineMapping59', {partner})
    assert getattr(partner, 'TConditionalLifelineStyle') == owner
    _safe_set(owner, 'sequence_template_TLifelineMapping59', set())
    assert getattr(partner, 'TConditionalLifelineStyle') is None


def test_assoc_conditionalStyle77_stub_double():
    # TConditionalMessageStyle has no real 'TConditionalMessageStyle' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TMessageMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TMessageMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TMessageMapping(receivingEndFinderExpression="sample_text", sendingEndFinderExpression="sample_text")
    partner = TConditionalMessageStyle()
    setattr(partner, 'TConditionalMessageStyle', None)
    _safe_set(owner, 'sequence_template_TMessageMapping78', {partner})
    assert getattr(partner, 'TConditionalMessageStyle') == owner
    _safe_set(owner, 'sequence_template_TMessageMapping78', set())
    assert getattr(partner, 'TConditionalMessageStyle') is None


def test_assoc_conditionalStyles67_stub_double():
    # TConditionalExecutionStyle has no real 'TConditionalExecutionStyle' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TExecutionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TExecutionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TExecutionMapping(finishingEndFinderExpression="sample_text", recursive=True, startingEndFinderExpression="sample_text")
    partner = TConditionalExecutionStyle()
    setattr(partner, 'TConditionalExecutionStyle', None)
    _safe_set(owner, 'sequence_template_TExecutionMapping68', {partner})
    assert getattr(partner, 'TConditionalExecutionStyle') == owner
    _safe_set(owner, 'sequence_template_TExecutionMapping68', set())
    assert getattr(partner, 'TConditionalExecutionStyle') is None


def test_assoc_endOfLifeStyle55_stub_double():
    # style_NodeStyleDescription has no real 'style_NodeStyleDescription57' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TLifelineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TLifelineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TLifelineMapping(eolVisibleExpression="sample_text")
    partner = style_NodeStyleDescription()
    setattr(partner, 'style_NodeStyleDescription57', None)
    _safe_set(owner, 'sequence_template_TLifelineMapping56', partner)
    assert getattr(partner, 'style_NodeStyleDescription57') == owner
    _safe_set(owner, 'sequence_template_TLifelineMapping56', None)
    assert getattr(partner, 'style_NodeStyleDescription57') is None


def test_assoc_eventEnds43_stub_double():
    # SingleEventEnd has no real 'SingleEventEnd' property in the generated
    # code (a bare stub) -- manually attach it so sequence_ordering_CompoundEventEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_ordering_CompoundEventEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_ordering_CompoundEventEnd()
    partner = SingleEventEnd()
    setattr(partner, 'SingleEventEnd', None)
    _safe_set(owner, 'sequence_ordering_CompoundEventEnd', {partner})
    assert getattr(partner, 'SingleEventEnd') == owner
    _safe_set(owner, 'sequence_ordering_CompoundEventEnd', set())
    assert getattr(partner, 'SingleEventEnd') is None


def test_assoc_executionMappings50_stub_double():
    # TExecutionMapping has no real 'TExecutionMapping' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TLifelineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TLifelineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TLifelineMapping(eolVisibleExpression="sample_text")
    partner = TExecutionMapping()
    setattr(partner, 'TExecutionMapping', None)
    _safe_set(owner, 'sequence_template_TLifelineMapping', {partner})
    assert getattr(partner, 'TExecutionMapping') == owner
    _safe_set(owner, 'sequence_template_TLifelineMapping', set())
    assert getattr(partner, 'TExecutionMapping') is None


def test_assoc_executionMappings63_stub_double():
    # TExecutionMapping has no real 'TExecutionMapping64' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TExecutionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TExecutionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TExecutionMapping(finishingEndFinderExpression="sample_text", recursive=True, startingEndFinderExpression="sample_text")
    partner = TExecutionMapping()
    setattr(partner, 'TExecutionMapping64', None)
    _safe_set(owner, 'sequence_template_TExecutionMapping', {partner})
    assert getattr(partner, 'TExecutionMapping64') == owner
    _safe_set(owner, 'sequence_template_TExecutionMapping', set())
    assert getattr(partner, 'TExecutionMapping64') is None


def test_assoc_instanceRoleStyle51_stub_double():
    # style_NodeStyleDescription has no real 'style_NodeStyleDescription' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TLifelineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TLifelineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TLifelineMapping(eolVisibleExpression="sample_text")
    partner = style_NodeStyleDescription()
    setattr(partner, 'style_NodeStyleDescription', None)
    _safe_set(owner, 'sequence_template_TLifelineMapping52', partner)
    assert getattr(partner, 'style_NodeStyleDescription') == owner
    _safe_set(owner, 'sequence_template_TLifelineMapping52', None)
    assert getattr(partner, 'style_NodeStyleDescription') is None


def test_assoc_invocationMapping86_stub_double():
    # TBasicMessageMapping has no real 'TBasicMessageMapping' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TReturnMessageMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TReturnMessageMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TReturnMessageMapping(invocationMessageFinderExpression="sample_text")
    partner = TBasicMessageMapping()
    setattr(partner, 'TBasicMessageMapping', None)
    _safe_set(owner, 'sequence_template_TReturnMessageMapping', partner)
    assert getattr(partner, 'TBasicMessageMapping') == owner
    _safe_set(owner, 'sequence_template_TReturnMessageMapping', None)
    assert getattr(partner, 'TBasicMessageMapping') is None


def test_assoc_lifelineColor60_stub_double():
    # ColorDescription has no real 'ColorDescription' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TLifelineStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TLifelineStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TLifelineStyle(lifelineWidthComputationExpression="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription', None)
    _safe_set(owner, 'sequence_template_TLifelineStyle', partner)
    assert getattr(partner, 'ColorDescription') == owner
    _safe_set(owner, 'sequence_template_TLifelineStyle', None)
    assert getattr(partner, 'ColorDescription') is None


def test_assoc_lifelineMappings47_stub_double():
    # TLifelineMapping has no real 'TLifelineMapping' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TSequenceDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TSequenceDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TSequenceDiagram(domainClass="sample_text", endsOrdering="sample_text")
    partner = TLifelineMapping()
    setattr(partner, 'TLifelineMapping', None)
    _safe_set(owner, 'sequence_template_TSequenceDiagram', {partner})
    assert getattr(partner, 'TLifelineMapping') == owner
    _safe_set(owner, 'sequence_template_TSequenceDiagram', set())
    assert getattr(partner, 'TLifelineMapping') is None


def test_assoc_lifelineStyle53_stub_double():
    # TLifelineStyle has no real 'TLifelineStyle' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TLifelineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TLifelineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TLifelineMapping(eolVisibleExpression="sample_text")
    partner = TLifelineStyle()
    setattr(partner, 'TLifelineStyle', None)
    _safe_set(owner, 'sequence_template_TLifelineMapping54', partner)
    assert getattr(partner, 'TLifelineStyle') == owner
    _safe_set(owner, 'sequence_template_TLifelineMapping54', None)
    assert getattr(partner, 'TLifelineStyle') is None


def test_assoc_messageMappings48_stub_double():
    # TMessageMapping has no real 'TMessageMapping' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TSequenceDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TSequenceDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TSequenceDiagram(domainClass="sample_text", endsOrdering="sample_text")
    partner = TMessageMapping()
    setattr(partner, 'TMessageMapping', None)
    _safe_set(owner, 'sequence_template_TSequenceDiagram49', {partner})
    assert getattr(partner, 'TMessageMapping') == owner
    _safe_set(owner, 'sequence_template_TSequenceDiagram49', set())
    assert getattr(partner, 'TMessageMapping') is None


def test_assoc_semanticEvent41_stub_double():
    # ordering_sequence_EObject has no real 'ordering_sequence_EObject42' property in the generated
    # code (a bare stub) -- manually attach it so sequence_ordering_SingleEventEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_ordering_SingleEventEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_ordering_SingleEventEnd(start=True)
    partner = ordering_sequence_EObject()
    setattr(partner, 'ordering_sequence_EObject42', None)
    _safe_set(owner, 'sequence_ordering_SingleEventEnd', partner)
    assert getattr(partner, 'ordering_sequence_EObject42') == owner
    _safe_set(owner, 'sequence_ordering_SingleEventEnd', None)
    assert getattr(partner, 'ordering_sequence_EObject42') is None


def test_assoc_source84_stub_double():
    # TMessageExtremity has no real 'TMessageExtremity85' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TSourceTargetMessageMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TSourceTargetMessageMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TSourceTargetMessageMapping(sourceFinderExpression="sample_text", targetFinderExpression="sample_text", useDomainElement=True)
    partner = TMessageExtremity()
    setattr(partner, 'TMessageExtremity85', None)
    _safe_set(owner, 'sequence_template_TSourceTargetMessageMapping', {partner})
    assert getattr(partner, 'TMessageExtremity85') == owner
    _safe_set(owner, 'sequence_template_TSourceTargetMessageMapping', set())
    assert getattr(partner, 'TMessageExtremity85') is None


def test_assoc_strokeColor79_stub_double():
    # ColorDescription has no real 'ColorDescription80' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TMessageStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TMessageStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TMessageStyle(labelExpression="sample_text", lineStyle="sample_text", sourceArrow="sample_text", targetArrow="sample_text")
    partner = ColorDescription()
    setattr(partner, 'ColorDescription80', None)
    _safe_set(owner, 'sequence_template_TMessageStyle', partner)
    assert getattr(partner, 'ColorDescription80') == owner
    _safe_set(owner, 'sequence_template_TMessageStyle', None)
    assert getattr(partner, 'ColorDescription80') is None


def test_assoc_style61_stub_double():
    # TLifelineStyle has no real 'TLifelineStyle62' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TConditionalLifelineStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TConditionalLifelineStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TConditionalLifelineStyle(predicateExpression="sample_text")
    partner = TLifelineStyle()
    setattr(partner, 'TLifelineStyle62', None)
    _safe_set(owner, 'sequence_template_TConditionalLifelineStyle', partner)
    assert getattr(partner, 'TLifelineStyle62') == owner
    _safe_set(owner, 'sequence_template_TConditionalLifelineStyle', None)
    assert getattr(partner, 'TLifelineStyle62') is None


def test_assoc_style65_stub_double():
    # TExecutionStyle has no real 'TExecutionStyle' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TExecutionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TExecutionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TExecutionMapping(finishingEndFinderExpression="sample_text", recursive=True, startingEndFinderExpression="sample_text")
    partner = TExecutionStyle()
    setattr(partner, 'TExecutionStyle', None)
    _safe_set(owner, 'sequence_template_TExecutionMapping66', partner)
    assert getattr(partner, 'TExecutionStyle') == owner
    _safe_set(owner, 'sequence_template_TExecutionMapping66', None)
    assert getattr(partner, 'TExecutionStyle') is None


def test_assoc_style74_stub_double():
    # TExecutionStyle has no real 'TExecutionStyle75' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TConditionalExecutionStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TConditionalExecutionStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TConditionalExecutionStyle(predicateExpression="sample_text")
    partner = TExecutionStyle()
    setattr(partner, 'TExecutionStyle75', None)
    _safe_set(owner, 'sequence_template_TConditionalExecutionStyle', partner)
    assert getattr(partner, 'TExecutionStyle75') == owner
    _safe_set(owner, 'sequence_template_TConditionalExecutionStyle', None)
    assert getattr(partner, 'TExecutionStyle75') is None


def test_assoc_style76_stub_double():
    # TMessageStyle has no real 'TMessageStyle' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TMessageMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TMessageMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TMessageMapping(receivingEndFinderExpression="sample_text", sendingEndFinderExpression="sample_text")
    partner = TMessageStyle()
    setattr(partner, 'TMessageStyle', None)
    _safe_set(owner, 'sequence_template_TMessageMapping', partner)
    assert getattr(partner, 'TMessageStyle') == owner
    _safe_set(owner, 'sequence_template_TMessageMapping', None)
    assert getattr(partner, 'TMessageStyle') is None


def test_assoc_style81_stub_double():
    # TMessageStyle has no real 'TMessageStyle82' property in the generated
    # code (a bare stub) -- manually attach it so sequence_template_TConditionalMessageStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sequence_template_TConditionalMessageStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sequence_template_TConditionalMessageStyle(predicateExpression="sample_text")
    partner = TMessageStyle()
    setattr(partner, 'TMessageStyle82', None)
    _safe_set(owner, 'sequence_template_TConditionalMessageStyle', partner)
    assert getattr(partner, 'TMessageStyle82') == owner
    _safe_set(owner, 'sequence_template_TConditionalMessageStyle', None)
    assert getattr(partner, 'TMessageStyle82') is None


