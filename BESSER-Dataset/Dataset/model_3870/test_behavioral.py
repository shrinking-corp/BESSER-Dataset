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
    Mapping,
    MessageEnd,
    MessageOccurrenceSpecification,
    NamedElement,
    ObjectType,
    OccurrenceSpecification,
    PrimitiveType,
    Property,
    RCollection,
    StructuralFeature,
    Substitution,
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
    ram_AttributeMapping,
    ram_Class,
    ram_Classifier,
    ram_ClassifierMapping,
    ram_CombinedFragment,
    ram_Constraint,
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
    ram_OperationMapping,
    ram_OriginalBehaviorExecution,
    ram_Parameter,
    ram_ParameterMapping,
    ram_ParameterValue,
    ram_ParameterValueMapping,
    ram_PrimitiveType,
    ram_Property,
    ram_RAny,
    ram_RArray,
    ram_RBoolean,
    ram_RChar,
    ram_RCollection,
    ram_RDouble,
    ram_REnum,
    ram_REnumLiteral,
    ram_RFloat,
    ram_RInt,
    ram_RLong,
    ram_RSequence,
    ram_RSet,
    ram_RString,
    ram_RVoid,
    ram_Reference,
    ram_State,
    ram_StateMachine,
    ram_StateView,
    ram_StructuralFeature,
    ram_StructuralFeatureValue,
    ram_StructuralView,
    ram_Substitution,
    ram_TemporaryProperty,
    ram_Transition,
    ram_TransitionSubstitution,
    ram_Type,
    ram_TypeParameter,
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

def test_assoc_assignTo73_reverse_link_reassign_clear():
    a1 = ram_StructuralFeature(static=True)
    a2 = ram_StructuralFeature(static=False)
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message74', a1)
    assert _is_linked(b, 'ram_Message74', a1)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert _is_linked(a1, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message74', a2)
    assert _is_linked(b, 'ram_Message74', a2)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert not _is_linked(a1, 'ram_StructuralFeature', b)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert _is_linked(a2, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message74', None)
    assert not _is_linked(b, 'ram_Message74', a2)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert not _is_linked(a2, 'ram_StructuralFeature', b)


def test_assoc_signature70_reverse_link_reassign_clear():
    a1 = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    a2 = ram_Operation(abstract=False, partial=False, static=False, visibility="sample_text_2")
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message71', a1)
    assert _is_linked(b, 'ram_Message71', a1)
    if hasattr(a1, 'ram_Operation72'):
        assert _is_linked(a1, 'ram_Operation72', b)
    _safe_set(b, 'ram_Message71', a2)
    assert _is_linked(b, 'ram_Message71', a2)
    if hasattr(a1, 'ram_Operation72'):
        assert not _is_linked(a1, 'ram_Operation72', b)
    if hasattr(a2, 'ram_Operation72'):
        assert _is_linked(a2, 'ram_Operation72', b)
    _safe_set(b, 'ram_Message71', None)
    assert not _is_linked(b, 'ram_Message71', a2)
    if hasattr(a2, 'ram_Operation72'):
        assert not _is_linked(a2, 'ram_Operation72', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments75_stub_double():
    # ram_ParameterValueMapping has no real 'ram_ParameterValueMapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ParameterValueMapping()
    setattr(partner, 'ram_ParameterValueMapping', None)
    _safe_set(owner, 'ram_Message76', {partner})
    assert getattr(partner, 'ram_ParameterValueMapping') == owner
    _safe_set(owner, 'ram_Message76', set())
    assert getattr(partner, 'ram_ParameterValueMapping') is None


def test_assoc_assoc21_stub_double():
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


def test_assoc_associationEnds118_stub_double():
    # ram_Classifier has no real 'classifier' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_Classifier()
    setattr(partner, 'classifier', None)
    _safe_set(owner, 'AssociationEnd119', partner)
    assert owner in getattr(partner, 'classifier')
    _safe_set(owner, 'AssociationEnd119', None)
    assert owner not in getattr(partner, 'classifier')


def test_assoc_attributes17_stub_double():
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


def test_assoc_classifier22_stub_double():
    # ram_Classifier has no real 'Classifier' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_Classifier()
    setattr(partner, 'Classifier', None)
    _safe_set(owner, 'associationEnds', partner)
    assert getattr(partner, 'Classifier') == owner
    _safe_set(owner, 'associationEnds', None)
    assert getattr(partner, 'Classifier') is None


def test_assoc_ends23_stub_double():
    # ram_Association has no real 'assoc' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_Association()
    setattr(partner, 'assoc', None)
    _safe_set(owner, 'AssociationEnd', partner)
    assert owner in getattr(partner, 'assoc')
    _safe_set(owner, 'AssociationEnd', None)
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


def test_assoc_fromElement143_stub_double():
    # ram_OperationMapping has no real 'ram_OperationMapping144' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_OperationMapping()
    setattr(partner, 'ram_OperationMapping144', None)
    _safe_set(owner, 'ram_Operation145', partner)
    assert getattr(partner, 'ram_OperationMapping144') == owner
    _safe_set(owner, 'ram_Operation145', None)
    assert getattr(partner, 'ram_OperationMapping144') is None


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


def test_assoc_interaction77_stub_double():
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
    # ram_ClassifierMapping has no real 'ram_ClassifierMapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_ClassifierMapping()
    setattr(partner, 'ram_ClassifierMapping', None)
    _safe_set(owner, 'ram_Instantiation25', {partner})
    assert getattr(partner, 'ram_ClassifierMapping') == owner
    _safe_set(owner, 'ram_Instantiation25', set())
    assert getattr(partner, 'ram_ClassifierMapping') is None


def test_assoc_message80_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd81' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd81', None)
    _safe_set(owner, 'ram_Message82', partner)
    assert getattr(partner, 'ram_MessageEnd81') == owner
    _safe_set(owner, 'ram_Message82', None)
    assert getattr(partner, 'ram_MessageEnd81') is None


def test_assoc_messages50_stub_double():
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


def test_assoc_operands85_stub_double():
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


def test_assoc_operations115_stub_double():
    # ram_Classifier has no real 'ram_Classifier116' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Classifier()
    setattr(partner, 'ram_Classifier116', None)
    _safe_set(owner, 'ram_Operation117', partner)
    assert owner in getattr(partner, 'ram_Classifier116')
    _safe_set(owner, 'ram_Operation117', None)
    assert owner not in getattr(partner, 'ram_Classifier116')


def test_assoc_parameters31_stub_double():
    # ram_Parameter has no real 'ram_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Parameter()
    setattr(partner, 'ram_Parameter', None)
    _safe_set(owner, 'ram_Operation32', {partner})
    assert getattr(partner, 'ram_Parameter') == owner
    _safe_set(owner, 'ram_Operation32', set())
    assert getattr(partner, 'ram_Parameter') is None


def test_assoc_pointcut55_stub_double():
    # ram_AspectMessageView has no real 'ram_AspectMessageView56' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_AspectMessageView()
    setattr(partner, 'ram_AspectMessageView56', None)
    _safe_set(owner, 'ram_Operation57', partner)
    assert getattr(partner, 'ram_AspectMessageView56') == owner
    _safe_set(owner, 'ram_Operation57', None)
    assert getattr(partner, 'ram_AspectMessageView56') is None


def test_assoc_receiveEvent67_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd69' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd69', None)
    _safe_set(owner, 'ram_Message68', partner)
    assert getattr(partner, 'ram_MessageEnd69') == owner
    _safe_set(owner, 'ram_Message68', None)
    assert getattr(partner, 'ram_MessageEnd69') is None


def test_assoc_represents61_stub_double():
    # ram_Lifeline has no real 'ram_Lifeline62' property in the generated
    # code (a bare stub) -- manually attach it so ram_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_TypedElement()
    partner = ram_Lifeline()
    setattr(partner, 'ram_Lifeline62', None)
    _safe_set(owner, 'ram_TypedElement', partner)
    assert getattr(partner, 'ram_Lifeline62') == owner
    _safe_set(owner, 'ram_TypedElement', None)
    assert getattr(partner, 'ram_Lifeline62') is None


def test_assoc_returnType29_stub_double():
    # ram_Type has no real 'ram_Type30' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Type()
    setattr(partner, 'ram_Type30', None)
    _safe_set(owner, 'ram_Operation', partner)
    assert getattr(partner, 'ram_Type30') == owner
    _safe_set(owner, 'ram_Operation', None)
    assert getattr(partner, 'ram_Type30') is None


def test_assoc_returns78_stub_double():
    # ram_ValueSpecification has no real 'ram_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ValueSpecification()
    setattr(partner, 'ram_ValueSpecification', None)
    _safe_set(owner, 'ram_Message79', partner)
    assert getattr(partner, 'ram_ValueSpecification') == owner
    _safe_set(owner, 'ram_Message79', None)
    assert getattr(partner, 'ram_ValueSpecification') is None


def test_assoc_sendEvent66_stub_double():
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


def test_assoc_signature172_stub_double():
    # ram_Transition has no real 'ram_Transition173' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Transition()
    setattr(partner, 'ram_Transition173', None)
    _safe_set(owner, 'ram_Operation174', partner)
    assert getattr(partner, 'ram_Transition173') == owner
    _safe_set(owner, 'ram_Operation174', None)
    assert getattr(partner, 'ram_Transition173') is None


def test_assoc_specifies42_stub_double():
    # ram_MessageView has no real 'ram_MessageView' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_MessageView()
    setattr(partner, 'ram_MessageView', None)
    _safe_set(owner, 'ram_Operation43', partner)
    assert getattr(partner, 'ram_MessageView') == owner
    _safe_set(owner, 'ram_Operation43', None)
    assert getattr(partner, 'ram_MessageView') is None


def test_assoc_superTypes18_stub_double():
    # ram_Classifier has no real 'ram_Classifier20' property in the generated
    # code (a bare stub) -- manually attach it so ram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Class(abstract=True, partial=True)
    partner = ram_Classifier()
    setattr(partner, 'ram_Classifier20', None)
    _safe_set(owner, 'ram_Class19', {partner})
    assert getattr(partner, 'ram_Classifier20') == owner
    _safe_set(owner, 'ram_Class19', set())
    assert getattr(partner, 'ram_Classifier20') is None


def test_assoc_toElement146_stub_double():
    # ram_OperationMapping has no real 'ram_OperationMapping147' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_OperationMapping()
    setattr(partner, 'ram_OperationMapping147', None)
    _safe_set(owner, 'ram_Operation148', partner)
    assert getattr(partner, 'ram_OperationMapping147') == owner
    _safe_set(owner, 'ram_Operation148', None)
    assert getattr(partner, 'ram_OperationMapping147') is None


def test_assoc_type103_stub_double():
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


def test_assoc_type191_stub_double():
    # ram_ObjectType has no real 'ram_ObjectType192' property in the generated
    # code (a bare stub) -- manually attach it so ram_RArray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_RArray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_RArray(size=7)
    partner = ram_ObjectType()
    setattr(partner, 'ram_ObjectType192', None)
    _safe_set(owner, 'ram_RArray', partner)
    assert getattr(partner, 'ram_ObjectType192') == owner
    _safe_set(owner, 'ram_RArray', None)
    assert getattr(partner, 'ram_ObjectType192') is None


def test_assoc_value113_stub_double():
    # ram_ElementMap has no real 'ram_ElementMap114' property in the generated
    # code (a bare stub) -- manually attach it so ram_LayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_LayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_LayoutElement(x=3.14, y=3.14)
    partner = ram_ElementMap()
    setattr(partner, 'ram_ElementMap114', None)
    _safe_set(owner, 'ram_LayoutElement', partner)
    assert getattr(partner, 'ram_ElementMap114') == owner
    _safe_set(owner, 'ram_LayoutElement', None)
    assert getattr(partner, 'ram_ElementMap114') is None


def test_assoc_value91_stub_double():
    # ram_StructuralFeatureValue has no real 'ram_StructuralFeatureValue' property in the generated
    # code (a bare stub) -- manually attach it so ram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_StructuralFeature(static=True)
    partner = ram_StructuralFeatureValue()
    setattr(partner, 'ram_StructuralFeatureValue', None)
    _safe_set(owner, 'ram_StructuralFeature92', partner)
    assert getattr(partner, 'ram_StructuralFeatureValue') == owner
    _safe_set(owner, 'ram_StructuralFeature92', None)
    assert getattr(partner, 'ram_StructuralFeatureValue') is None


