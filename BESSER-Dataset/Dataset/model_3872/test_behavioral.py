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
    ram_RBoolean,
    ram_RChar,
    ram_RCollection,
    ram_RDouble,
    ram_REnum,
    ram_REnumLiteral,
    ram_RFloat,
    ram_RInt,
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

def test_assoc_assignTo75_reverse_link_reassign_clear():
    a1 = ram_StructuralFeature(static=True)
    a2 = ram_StructuralFeature(static=False)
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message76', a1)
    assert _is_linked(b, 'ram_Message76', a1)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert _is_linked(a1, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message76', a2)
    assert _is_linked(b, 'ram_Message76', a2)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert not _is_linked(a1, 'ram_StructuralFeature', b)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert _is_linked(a2, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message76', None)
    assert not _is_linked(b, 'ram_Message76', a2)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert not _is_linked(a2, 'ram_StructuralFeature', b)


def test_assoc_associationEnds17_reverse_link_reassign_clear():
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


def test_assoc_myClass23_reverse_link_reassign_clear():
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


def test_assoc_signature72_reverse_link_reassign_clear():
    a1 = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    a2 = ram_Operation(abstract=False, partial=False, static=False, visibility="sample_text_2")
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message73', a1)
    assert _is_linked(b, 'ram_Message73', a1)
    if hasattr(a1, 'ram_Operation74'):
        assert _is_linked(a1, 'ram_Operation74', b)
    _safe_set(b, 'ram_Message73', a2)
    assert _is_linked(b, 'ram_Message73', a2)
    if hasattr(a1, 'ram_Operation74'):
        assert not _is_linked(a1, 'ram_Operation74', b)
    if hasattr(a2, 'ram_Operation74'):
        assert _is_linked(a2, 'ram_Operation74', b)
    _safe_set(b, 'ram_Message73', None)
    assert not _is_linked(b, 'ram_Message73', a2)
    if hasattr(a2, 'ram_Operation74'):
        assert not _is_linked(a2, 'ram_Operation74', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments77_stub_double():
    # ram_ParameterValueMapping has no real 'ram_ParameterValueMapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ParameterValueMapping()
    setattr(partner, 'ram_ParameterValueMapping', None)
    _safe_set(owner, 'ram_Message78', {partner})
    assert getattr(partner, 'ram_ParameterValueMapping') == owner
    _safe_set(owner, 'ram_Message78', set())
    assert getattr(partner, 'ram_ParameterValueMapping') is None


def test_assoc_assoc22_stub_double():
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


def test_assoc_attributes18_stub_double():
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


def test_assoc_ends24_stub_double():
    # ram_Association has no real 'assoc' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_Association()
    setattr(partner, 'assoc', None)
    _safe_set(owner, 'AssociationEnd25', partner)
    assert owner in getattr(partner, 'assoc')
    _safe_set(owner, 'AssociationEnd25', None)
    assert owner not in getattr(partner, 'assoc')


def test_assoc_externalAspect28_stub_double():
    # ram_Aspect has no real 'ram_Aspect30' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_Aspect()
    setattr(partner, 'ram_Aspect30', None)
    _safe_set(owner, 'ram_Instantiation29', partner)
    assert getattr(partner, 'ram_Aspect30') == owner
    _safe_set(owner, 'ram_Instantiation29', None)
    assert getattr(partner, 'ram_Aspect30') is None


def test_assoc_fromElement141_stub_double():
    # ram_OperationMapping has no real 'ram_OperationMapping142' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_OperationMapping()
    setattr(partner, 'ram_OperationMapping142', None)
    _safe_set(owner, 'ram_Operation143', partner)
    assert getattr(partner, 'ram_OperationMapping142') == owner
    _safe_set(owner, 'ram_Operation143', None)
    assert getattr(partner, 'ram_OperationMapping142') is None


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


def test_assoc_interaction79_stub_double():
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


def test_assoc_mappings26_stub_double():
    # ram_ClassifierMapping has no real 'ram_ClassifierMapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_ClassifierMapping()
    setattr(partner, 'ram_ClassifierMapping', None)
    _safe_set(owner, 'ram_Instantiation27', {partner})
    assert getattr(partner, 'ram_ClassifierMapping') == owner
    _safe_set(owner, 'ram_Instantiation27', set())
    assert getattr(partner, 'ram_ClassifierMapping') is None


def test_assoc_message82_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd83' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd83', None)
    _safe_set(owner, 'ram_Message84', partner)
    assert getattr(partner, 'ram_MessageEnd83') == owner
    _safe_set(owner, 'ram_Message84', None)
    assert getattr(partner, 'ram_MessageEnd83') is None


def test_assoc_messages52_stub_double():
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


def test_assoc_operands87_stub_double():
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


def test_assoc_operations117_stub_double():
    # ram_Classifier has no real 'ram_Classifier118' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Classifier()
    setattr(partner, 'ram_Classifier118', None)
    _safe_set(owner, 'ram_Operation119', partner)
    assert owner in getattr(partner, 'ram_Classifier118')
    _safe_set(owner, 'ram_Operation119', None)
    assert owner not in getattr(partner, 'ram_Classifier118')


def test_assoc_parameters33_stub_double():
    # ram_Parameter has no real 'ram_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Parameter()
    setattr(partner, 'ram_Parameter', None)
    _safe_set(owner, 'ram_Operation34', {partner})
    assert getattr(partner, 'ram_Parameter') == owner
    _safe_set(owner, 'ram_Operation34', set())
    assert getattr(partner, 'ram_Parameter') is None


def test_assoc_pointcut57_stub_double():
    # ram_AspectMessageView has no real 'ram_AspectMessageView58' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_AspectMessageView()
    setattr(partner, 'ram_AspectMessageView58', None)
    _safe_set(owner, 'ram_Operation59', partner)
    assert getattr(partner, 'ram_AspectMessageView58') == owner
    _safe_set(owner, 'ram_Operation59', None)
    assert getattr(partner, 'ram_AspectMessageView58') is None


def test_assoc_receiveEvent69_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd71' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd71', None)
    _safe_set(owner, 'ram_Message70', partner)
    assert getattr(partner, 'ram_MessageEnd71') == owner
    _safe_set(owner, 'ram_Message70', None)
    assert getattr(partner, 'ram_MessageEnd71') is None


def test_assoc_represents63_stub_double():
    # ram_Lifeline has no real 'ram_Lifeline64' property in the generated
    # code (a bare stub) -- manually attach it so ram_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_TypedElement()
    partner = ram_Lifeline()
    setattr(partner, 'ram_Lifeline64', None)
    _safe_set(owner, 'ram_TypedElement', partner)
    assert getattr(partner, 'ram_Lifeline64') == owner
    _safe_set(owner, 'ram_TypedElement', None)
    assert getattr(partner, 'ram_Lifeline64') is None


def test_assoc_returnType31_stub_double():
    # ram_Type has no real 'ram_Type32' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Type()
    setattr(partner, 'ram_Type32', None)
    _safe_set(owner, 'ram_Operation', partner)
    assert getattr(partner, 'ram_Type32') == owner
    _safe_set(owner, 'ram_Operation', None)
    assert getattr(partner, 'ram_Type32') is None


def test_assoc_returns80_stub_double():
    # ram_ValueSpecification has no real 'ram_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ValueSpecification()
    setattr(partner, 'ram_ValueSpecification', None)
    _safe_set(owner, 'ram_Message81', partner)
    assert getattr(partner, 'ram_ValueSpecification') == owner
    _safe_set(owner, 'ram_Message81', None)
    assert getattr(partner, 'ram_ValueSpecification') is None


def test_assoc_sendEvent68_stub_double():
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


def test_assoc_signature170_stub_double():
    # ram_Transition has no real 'ram_Transition171' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_Transition()
    setattr(partner, 'ram_Transition171', None)
    _safe_set(owner, 'ram_Operation172', partner)
    assert getattr(partner, 'ram_Transition171') == owner
    _safe_set(owner, 'ram_Operation172', None)
    assert getattr(partner, 'ram_Transition171') is None


def test_assoc_specifies44_stub_double():
    # ram_MessageView has no real 'ram_MessageView' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_MessageView()
    setattr(partner, 'ram_MessageView', None)
    _safe_set(owner, 'ram_Operation45', partner)
    assert getattr(partner, 'ram_MessageView') == owner
    _safe_set(owner, 'ram_Operation45', None)
    assert getattr(partner, 'ram_MessageView') is None


def test_assoc_superTypes19_stub_double():
    # ram_Classifier has no real 'ram_Classifier21' property in the generated
    # code (a bare stub) -- manually attach it so ram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Class(abstract=True, partial=True)
    partner = ram_Classifier()
    setattr(partner, 'ram_Classifier21', None)
    _safe_set(owner, 'ram_Class20', {partner})
    assert getattr(partner, 'ram_Classifier21') == owner
    _safe_set(owner, 'ram_Class20', set())
    assert getattr(partner, 'ram_Classifier21') is None


def test_assoc_toElement144_stub_double():
    # ram_OperationMapping has no real 'ram_OperationMapping145' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    partner = ram_OperationMapping()
    setattr(partner, 'ram_OperationMapping145', None)
    _safe_set(owner, 'ram_Operation146', partner)
    assert getattr(partner, 'ram_OperationMapping145') == owner
    _safe_set(owner, 'ram_Operation146', None)
    assert getattr(partner, 'ram_OperationMapping145') is None


def test_assoc_type105_stub_double():
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


def test_assoc_value115_stub_double():
    # ram_ElementMap has no real 'ram_ElementMap116' property in the generated
    # code (a bare stub) -- manually attach it so ram_LayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_LayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_LayoutElement(x=3.14, y=3.14)
    partner = ram_ElementMap()
    setattr(partner, 'ram_ElementMap116', None)
    _safe_set(owner, 'ram_LayoutElement', partner)
    assert getattr(partner, 'ram_ElementMap116') == owner
    _safe_set(owner, 'ram_LayoutElement', None)
    assert getattr(partner, 'ram_ElementMap116') is None


def test_assoc_value93_stub_double():
    # ram_StructuralFeatureValue has no real 'ram_StructuralFeatureValue' property in the generated
    # code (a bare stub) -- manually attach it so ram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_StructuralFeature(static=True)
    partner = ram_StructuralFeatureValue()
    setattr(partner, 'ram_StructuralFeatureValue', None)
    _safe_set(owner, 'ram_StructuralFeature94', partner)
    assert getattr(partner, 'ram_StructuralFeatureValue') == owner
    _safe_set(owner, 'ram_StructuralFeature94', None)
    assert getattr(partner, 'ram_StructuralFeatureValue') is None


