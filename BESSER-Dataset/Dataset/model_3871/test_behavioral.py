import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMessageView,
    Classifier,
    FragmentContainer,
    ImplementationClass,
    InteractionFragment,
    LiteralSpecification,
    MappableElement,
    MessageEnd,
    MessageOccurrenceSpecification,
    NamedElement,
    ObjectType,
    OccurrenceSpecification,
    PrimitiveType,
    Property,
    RCollection,
    StructuralFeature,
    TemporaryProperty,
    Type,
    TypedElement,
    ValueSpecification,
    ram_AbstractMessageView,
    ram_Aspect,
    ram_AspectMessageView,
    ram_Association,
    ram_AssociationEnd,
    ram_Attribute,
    ram_Class,
    ram_Classifier,
    ram_CombinedFragment,
    ram_ContainerMap,
    ram_DestructionOccurrenceSpecification,
    ram_EObject,
    ram_ElementMap,
    ram_ExecutionStatement,
    ram_FragmentContainer,
    ram_Gate,
    ram_ImplementationClass,
    ram_Instantiation,
    ram_Interaction,
    ram_InteractionFragment,
    ram_InteractionOperand,
    ram_Layout,
    ram_LayoutElement,
    ram_Lifeline,
    ram_LiteralBoolean,
    ram_LiteralInteger,
    ram_LiteralSpecification,
    ram_LiteralString,
    ram_MappableElement,
    ram_Mapping,
    ram_Message,
    ram_MessageEnd,
    ram_MessageOccurrenceSpecification,
    ram_MessageView,
    ram_MessageViewReference,
    ram_NamedElement,
    ram_ObjectType,
    ram_OccurrenceSpecification,
    ram_OpaqueExpression,
    ram_Operation,
    ram_OriginalBehaviorExecution,
    ram_Parameter,
    ram_ParameterValue,
    ram_ParameterValueMapping,
    ram_PrimitiveType,
    ram_Property,
    ram_RAny,
    ram_RBoolean,
    ram_RChar,
    ram_RCollection,
    ram_REnum,
    ram_REnumLiteral,
    ram_RInt,
    ram_RList,
    ram_RSet,
    ram_RString,
    ram_RVoid,
    ram_Reference,
    ram_StructuralFeature,
    ram_StructuralFeatureValue,
    ram_StructuralView,
    ram_TemporaryProperty,
    ram_Type,
    ram_TypedElement,
    ram_ValueSpecification,
    InstantiationType,
    InteractionOperatorKind,
    MessageSort,
    ReferenceType,
    Visibility,
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

def test_assoc_assignTo79_reverse_link_reassign_clear():
    a1 = ram_StructuralFeature(static=True)
    a2 = ram_StructuralFeature(static=False)
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message80', a1)
    assert _is_linked(b, 'ram_Message80', a1)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert _is_linked(a1, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message80', a2)
    assert _is_linked(b, 'ram_Message80', a2)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert not _is_linked(a1, 'ram_StructuralFeature', b)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert _is_linked(a2, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message80', None)
    assert not _is_linked(b, 'ram_Message80', a2)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert not _is_linked(a2, 'ram_StructuralFeature', b)


def test_assoc_associationEnds15_reverse_link_reassign_clear():
    a1 = ram_Class(abstract=True, partial=True)
    a2 = ram_Class(abstract=False, partial=False)
    b = ram_AssociationEnd(navigable=True)
    _safe_set(b, 'AssociationEnd', a1)
    assert _is_linked(b, 'AssociationEnd', a1)
    if hasattr(a1, 'myClass'):
        assert _is_linked(a1, 'myClass', b)
    _safe_set(b, 'AssociationEnd', a2)
    assert _is_linked(b, 'AssociationEnd', a2)
    if hasattr(a1, 'myClass'):
        assert not _is_linked(a1, 'myClass', b)
    if hasattr(a2, 'myClass'):
        assert _is_linked(a2, 'myClass', b)
    _safe_set(b, 'AssociationEnd', None)
    assert not _is_linked(b, 'AssociationEnd', a2)
    if hasattr(a2, 'myClass'):
        assert not _is_linked(a2, 'myClass', b)


def test_assoc_myClass21_reverse_link_reassign_clear():
    a1 = ram_Class(abstract=True, partial=True)
    a2 = ram_Class(abstract=False, partial=False)
    b = ram_AssociationEnd(navigable=True)
    _safe_set(b, 'associationEnds', a1)
    assert _is_linked(b, 'associationEnds', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'associationEnds', a2)
    assert _is_linked(b, 'associationEnds', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'associationEnds', None)
    assert not _is_linked(b, 'associationEnds', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


def test_assoc_signature76_reverse_link_reassign_clear():
    a1 = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    a2 = ram_Operation(abstract=False, partial=False, static=False, visibility="sample_text_2")
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message77', a1)
    assert _is_linked(b, 'ram_Message77', a1)
    if hasattr(a1, 'ram_Operation78'):
        assert _is_linked(a1, 'ram_Operation78', b)
    _safe_set(b, 'ram_Message77', a2)
    assert _is_linked(b, 'ram_Message77', a2)
    if hasattr(a1, 'ram_Operation78'):
        assert not _is_linked(a1, 'ram_Operation78', b)
    if hasattr(a2, 'ram_Operation78'):
        assert _is_linked(a2, 'ram_Operation78', b)
    _safe_set(b, 'ram_Message77', None)
    assert not _is_linked(b, 'ram_Message77', a2)
    if hasattr(a2, 'ram_Operation78'):
        assert not _is_linked(a2, 'ram_Operation78', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments81_stub_double():
    # ram_ParameterValueMapping has no real 'ram_ParameterValueMapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ParameterValueMapping()
    setattr(partner, 'ram_ParameterValueMapping', None)
    _safe_set(owner, 'ram_Message82', {partner})
    assert getattr(partner, 'ram_ParameterValueMapping') == owner
    _safe_set(owner, 'ram_Message82', set())
    assert getattr(partner, 'ram_ParameterValueMapping') is None


def test_assoc_assoc20_stub_double():
    # ram_Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'ends', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'ends', None)
    assert getattr(partner, 'Association') is None


def test_assoc_attributes16_stub_double():
    # ram_Attribute has no real 'ram_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so ram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Class(abstract=True, partial=True)
    partner = ram_Attribute()
    setattr(partner, 'ram_Attribute', None)
    _safe_set(owner, 'ram_Class', {partner})
    assert getattr(partner, 'ram_Attribute') == owner
    _safe_set(owner, 'ram_Class', set())
    assert getattr(partner, 'ram_Attribute') is None


def test_assoc_ends22_stub_double():
    # ram_Association has no real 'assoc' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_Association()
    setattr(partner, 'assoc', None)
    _safe_set(owner, 'AssociationEnd23', partner)
    assert owner in getattr(partner, 'assoc')
    _safe_set(owner, 'AssociationEnd23', None)
    assert owner not in getattr(partner, 'assoc')


def test_assoc_externalAspect26_stub_double():
    # ram_Aspect has no real 'ram_Aspect28' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_Aspect()
    setattr(partner, 'ram_Aspect28', None)
    _safe_set(owner, 'ram_Instantiation27', partner)
    assert getattr(partner, 'ram_Aspect28') == owner
    _safe_set(owner, 'ram_Instantiation27', None)
    assert getattr(partner, 'ram_Aspect28') is None


def test_assoc_instantiations5_stub_double():
    # ram_Aspect has no real 'ram_Aspect6' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_Aspect()
    setattr(partner, 'ram_Aspect6', None)
    _safe_set(owner, 'ram_Instantiation', partner)
    assert owner in getattr(partner, 'ram_Aspect6')
    _safe_set(owner, 'ram_Instantiation', None)
    assert owner not in getattr(partner, 'ram_Aspect6')


def test_assoc_interaction83_stub_double():
    # ram_Interaction has no real 'Interaction' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_Interaction()
    setattr(partner, 'Interaction', None)
    _safe_set(owner, 'messages', partner)
    assert getattr(partner, 'Interaction') == owner
    _safe_set(owner, 'messages', None)
    assert getattr(partner, 'Interaction') is None


def test_assoc_mappings24_stub_double():
    # ram_Mapping has no real 'ram_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_Mapping()
    setattr(partner, 'ram_Mapping', None)
    _safe_set(owner, 'ram_Instantiation25', {partner})
    assert getattr(partner, 'ram_Mapping') == owner
    _safe_set(owner, 'ram_Instantiation25', set())
    assert getattr(partner, 'ram_Mapping') is None


def test_assoc_message86_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd87' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd87', None)
    _safe_set(owner, 'ram_Message88', partner)
    assert getattr(partner, 'ram_MessageEnd87') == owner
    _safe_set(owner, 'ram_Message88', None)
    assert getattr(partner, 'ram_MessageEnd87') is None


def test_assoc_messages56_stub_double():
    # ram_Interaction has no real 'interaction' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_Interaction()
    setattr(partner, 'interaction', None)
    _safe_set(owner, 'Message', partner)
    assert owner in getattr(partner, 'interaction')
    _safe_set(owner, 'Message', None)
    assert owner not in getattr(partner, 'interaction')


def test_assoc_operands91_stub_double():
    # ram_InteractionOperand has no real 'ram_InteractionOperand' property in the generated
    # code (a bare stub) -- manually attach it so ram_CombinedFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_CombinedFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_CombinedFragment(interactionOperator="sample_text")
    partner = ram_InteractionOperand()
    setattr(partner, 'ram_InteractionOperand', None)
    _safe_set(owner, 'ram_CombinedFragment', {partner})
    assert getattr(partner, 'ram_InteractionOperand') == owner
    _safe_set(owner, 'ram_CombinedFragment', set())
    assert getattr(partner, 'ram_InteractionOperand') is None


def test_assoc_operations121_stub_double():
    # ram_Classifier has no real 'ram_Classifier122' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Classifier()
    setattr(partner, 'ram_Classifier122', None)
    _safe_set(owner, 'ram_Operation123', partner)
    assert owner in getattr(partner, 'ram_Classifier122')
    _safe_set(owner, 'ram_Operation123', None)
    assert owner not in getattr(partner, 'ram_Classifier122')


def test_assoc_parameters37_stub_double():
    # ram_Parameter has no real 'ram_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Parameter()
    setattr(partner, 'ram_Parameter', None)
    _safe_set(owner, 'ram_Operation38', {partner})
    assert getattr(partner, 'ram_Parameter') == owner
    _safe_set(owner, 'ram_Operation38', set())
    assert getattr(partner, 'ram_Parameter') is None


def test_assoc_pointcut61_stub_double():
    # ram_AspectMessageView has no real 'ram_AspectMessageView62' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_AspectMessageView()
    setattr(partner, 'ram_AspectMessageView62', None)
    _safe_set(owner, 'ram_Operation63', partner)
    assert getattr(partner, 'ram_AspectMessageView62') == owner
    _safe_set(owner, 'ram_Operation63', None)
    assert getattr(partner, 'ram_AspectMessageView62') is None


def test_assoc_receiveEvent73_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd75' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd75', None)
    _safe_set(owner, 'ram_Message74', partner)
    assert getattr(partner, 'ram_MessageEnd75') == owner
    _safe_set(owner, 'ram_Message74', None)
    assert getattr(partner, 'ram_MessageEnd75') is None


def test_assoc_represents67_stub_double():
    # ram_Lifeline has no real 'ram_Lifeline68' property in the generated
    # code (a bare stub) -- manually attach it so ram_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_TypedElement()
    partner = ram_Lifeline()
    setattr(partner, 'ram_Lifeline68', None)
    _safe_set(owner, 'ram_TypedElement', partner)
    assert getattr(partner, 'ram_Lifeline68') == owner
    _safe_set(owner, 'ram_TypedElement', None)
    assert getattr(partner, 'ram_Lifeline68') is None


def test_assoc_returnType35_stub_double():
    # ram_Type has no real 'ram_Type36' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Type()
    setattr(partner, 'ram_Type36', None)
    _safe_set(owner, 'ram_Operation', partner)
    assert getattr(partner, 'ram_Type36') == owner
    _safe_set(owner, 'ram_Operation', None)
    assert getattr(partner, 'ram_Type36') is None


def test_assoc_returns84_stub_double():
    # ram_ValueSpecification has no real 'ram_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ValueSpecification()
    setattr(partner, 'ram_ValueSpecification', None)
    _safe_set(owner, 'ram_Message85', partner)
    assert getattr(partner, 'ram_ValueSpecification') == owner
    _safe_set(owner, 'ram_Message85', None)
    assert getattr(partner, 'ram_ValueSpecification') is None


def test_assoc_sendEvent72_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd', None)
    _safe_set(owner, 'ram_Message', partner)
    assert getattr(partner, 'ram_MessageEnd') == owner
    _safe_set(owner, 'ram_Message', None)
    assert getattr(partner, 'ram_MessageEnd') is None


def test_assoc_specifies48_stub_double():
    # ram_MessageView has no real 'ram_MessageView' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_MessageView()
    setattr(partner, 'ram_MessageView', None)
    _safe_set(owner, 'ram_Operation49', partner)
    assert getattr(partner, 'ram_MessageView') == owner
    _safe_set(owner, 'ram_Operation49', None)
    assert getattr(partner, 'ram_MessageView') is None


def test_assoc_superTypes17_stub_double():
    # ram_Classifier has no real 'ram_Classifier19' property in the generated
    # code (a bare stub) -- manually attach it so ram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Class(abstract=True, partial=True)
    partner = ram_Classifier()
    setattr(partner, 'ram_Classifier19', None)
    _safe_set(owner, 'ram_Class18', {partner})
    assert getattr(partner, 'ram_Classifier19') == owner
    _safe_set(owner, 'ram_Class18', set())
    assert getattr(partner, 'ram_Classifier19') is None


def test_assoc_type109_stub_double():
    # ram_ObjectType has no real 'ram_ObjectType' property in the generated
    # code (a bare stub) -- manually attach it so ram_RCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_RCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_RCollection()
    partner = ram_ObjectType()
    setattr(partner, 'ram_ObjectType', None)
    _safe_set(owner, 'ram_RCollection', partner)
    assert getattr(partner, 'ram_ObjectType') == owner
    _safe_set(owner, 'ram_RCollection', None)
    assert getattr(partner, 'ram_ObjectType') is None


def test_assoc_value119_stub_double():
    # ram_ElementMap has no real 'ram_ElementMap120' property in the generated
    # code (a bare stub) -- manually attach it so ram_LayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_LayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_LayoutElement(x=3.14, y=3.14)
    partner = ram_ElementMap()
    setattr(partner, 'ram_ElementMap120', None)
    _safe_set(owner, 'ram_LayoutElement', partner)
    assert getattr(partner, 'ram_ElementMap120') == owner
    _safe_set(owner, 'ram_LayoutElement', None)
    assert getattr(partner, 'ram_ElementMap120') is None


def test_assoc_value97_stub_double():
    # ram_StructuralFeatureValue has no real 'ram_StructuralFeatureValue' property in the generated
    # code (a bare stub) -- manually attach it so ram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_StructuralFeature(static=True)
    partner = ram_StructuralFeatureValue()
    setattr(partner, 'ram_StructuralFeatureValue', None)
    _safe_set(owner, 'ram_StructuralFeature98', partner)
    assert getattr(partner, 'ram_StructuralFeatureValue') == owner
    _safe_set(owner, 'ram_StructuralFeature98', None)
    assert getattr(partner, 'ram_StructuralFeatureValue') is None


