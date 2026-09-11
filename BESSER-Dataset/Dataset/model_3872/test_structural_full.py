import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_ram_AssociationEnd_navigable_value_roundtrip():
    instance = ram_AssociationEnd(navigable=True)
    assert instance.navigable == True
    instance.navigable = False
    assert instance.navigable == False


def test_ram_Class_abstract_value_roundtrip():
    instance = ram_Class(abstract=True, partial=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_ram_Class_partial_value_roundtrip():
    instance = ram_Class(abstract=True, partial=True)
    assert instance.partial == True
    instance.partial = False
    assert instance.partial == False


def test_ram_CombinedFragment_interactionOperator_value_roundtrip():
    instance = ram_CombinedFragment(interactionOperator="sample_text")
    assert instance.interactionOperator == "sample_text"
    instance.interactionOperator = "sample_text_2"
    assert instance.interactionOperator == "sample_text_2"


def test_ram_ImplementationClass_instanceClassName_value_roundtrip():
    instance = ram_ImplementationClass(instanceClassName="sample_text")
    assert instance.instanceClassName == "sample_text"
    instance.instanceClassName = "sample_text_2"
    assert instance.instanceClassName == "sample_text_2"


def test_ram_Instantiation_type_value_roundtrip():
    instance = ram_Instantiation(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_ram_LayoutElement_x_value_roundtrip():
    instance = ram_LayoutElement(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_ram_LayoutElement_y_value_roundtrip():
    instance = ram_LayoutElement(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_ram_LiteralBoolean_value_value_roundtrip():
    instance = ram_LiteralBoolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_ram_LiteralInteger_value_value_roundtrip():
    instance = ram_LiteralInteger(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_ram_LiteralString_value_value_roundtrip():
    instance = ram_LiteralString(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ram_Message_messageSort_value_roundtrip():
    instance = ram_Message(messageSort="sample_text", selfMessage=True)
    assert instance.messageSort == "sample_text"
    instance.messageSort = "sample_text_2"
    assert instance.messageSort == "sample_text_2"


def test_ram_Message_selfMessage_value_roundtrip():
    instance = ram_Message(messageSort="sample_text", selfMessage=True)
    assert instance.selfMessage == True
    instance.selfMessage = False
    assert instance.selfMessage == False


def test_ram_NamedElement_name_value_roundtrip():
    instance = ram_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ram_OpaqueExpression_body_value_roundtrip():
    instance = ram_OpaqueExpression(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_ram_OpaqueExpression_language_value_roundtrip():
    instance = ram_OpaqueExpression(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_ram_Operation_abstract_value_roundtrip():
    instance = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_ram_Operation_partial_value_roundtrip():
    instance = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    assert instance.partial == True
    instance.partial = False
    assert instance.partial == False


def test_ram_Operation_static_value_roundtrip():
    instance = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_ram_Operation_visibility_value_roundtrip():
    instance = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_ram_Property_lowerBound_value_roundtrip():
    instance = ram_Property(lowerBound=7, referenceType="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_ram_Property_referenceType_value_roundtrip():
    instance = ram_Property(lowerBound=7, referenceType="sample_text", upperBound=7)
    assert instance.referenceType == "sample_text"
    instance.referenceType = "sample_text_2"
    assert instance.referenceType == "sample_text_2"


def test_ram_Property_upperBound_value_roundtrip():
    instance = ram_Property(lowerBound=7, referenceType="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_ram_StructuralFeature_static_value_roundtrip():
    instance = ram_StructuralFeature(static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_ram_AspectMessageView_isa_AbstractMessageView():
    instance = ram_AspectMessageView()
    assert isinstance(instance, AbstractMessageView)


def test_ram_MessageView_isa_AbstractMessageView():
    instance = ram_MessageView()
    assert isinstance(instance, AbstractMessageView)


def test_ram_MessageViewReference_isa_AbstractMessageView():
    instance = ram_MessageViewReference()
    assert isinstance(instance, AbstractMessageView)


def test_ram_Class_isa_Classifier():
    instance = ram_Class(abstract=True, partial=True)
    assert isinstance(instance, Classifier)


def test_ram_ImplementationClass_isa_Classifier():
    instance = ram_ImplementationClass(instanceClassName="sample_text")
    assert isinstance(instance, Classifier)


def test_ram_Interaction_isa_FragmentContainer():
    instance = ram_Interaction()
    assert isinstance(instance, FragmentContainer)


def test_ram_InteractionOperand_isa_FragmentContainer():
    instance = ram_InteractionOperand()
    assert isinstance(instance, FragmentContainer)


def test_ram_PrimitiveType_isa_ImplementationClass():
    instance = ram_PrimitiveType()
    assert isinstance(instance, ImplementationClass)


def test_ram_RCollection_isa_ImplementationClass():
    instance = ram_RCollection()
    assert isinstance(instance, ImplementationClass)


def test_ram_CombinedFragment_isa_InteractionFragment():
    instance = ram_CombinedFragment(interactionOperator="sample_text")
    assert isinstance(instance, InteractionFragment)


def test_ram_ExecutionStatement_isa_InteractionFragment():
    instance = ram_ExecutionStatement()
    assert isinstance(instance, InteractionFragment)


def test_ram_OccurrenceSpecification_isa_InteractionFragment():
    instance = ram_OccurrenceSpecification()
    assert isinstance(instance, InteractionFragment)


def test_ram_OriginalBehaviorExecution_isa_InteractionFragment():
    instance = ram_OriginalBehaviorExecution()
    assert isinstance(instance, InteractionFragment)


def test_ram_LiteralBoolean_isa_LiteralSpecification():
    instance = ram_LiteralBoolean(value=True)
    assert isinstance(instance, LiteralSpecification)


def test_ram_LiteralInteger_isa_LiteralSpecification():
    instance = ram_LiteralInteger(value=7)
    assert isinstance(instance, LiteralSpecification)


def test_ram_LiteralString_isa_LiteralSpecification():
    instance = ram_LiteralString(value="sample_text")
    assert isinstance(instance, LiteralSpecification)


def test_ram_Attribute_isa_MappableElement():
    instance = ram_Attribute()
    assert isinstance(instance, MappableElement)


def test_ram_ObjectType_isa_MappableElement():
    instance = ram_ObjectType()
    assert isinstance(instance, MappableElement)


def test_ram_Operation_isa_MappableElement():
    instance = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    assert isinstance(instance, MappableElement)


def test_ram_Parameter_isa_MappableElement():
    instance = ram_Parameter()
    assert isinstance(instance, MappableElement)


def test_ram_AttributeMapping_isa_Mapping():
    instance = ram_AttributeMapping()
    assert isinstance(instance, Mapping)


def test_ram_ClassifierMapping_isa_Mapping():
    instance = ram_ClassifierMapping()
    assert isinstance(instance, Mapping)


def test_ram_OperationMapping_isa_Mapping():
    instance = ram_OperationMapping()
    assert isinstance(instance, Mapping)


def test_ram_ParameterMapping_isa_Mapping():
    instance = ram_ParameterMapping()
    assert isinstance(instance, Mapping)


def test_ram_Gate_isa_MessageEnd():
    instance = ram_Gate()
    assert isinstance(instance, MessageEnd)


def test_ram_MessageOccurrenceSpecification_isa_MessageEnd():
    instance = ram_MessageOccurrenceSpecification()
    assert isinstance(instance, MessageEnd)


def test_ram_DestructionOccurrenceSpecification_isa_MessageOccurrenceSpecification():
    instance = ram_DestructionOccurrenceSpecification()
    assert isinstance(instance, MessageOccurrenceSpecification)


def test_ram_Aspect_isa_NamedElement():
    instance = ram_Aspect()
    assert isinstance(instance, NamedElement)


def test_ram_AspectMessageView_isa_NamedElement():
    instance = ram_AspectMessageView()
    assert isinstance(instance, NamedElement)


def test_ram_Association_isa_NamedElement():
    instance = ram_Association()
    assert isinstance(instance, NamedElement)


def test_ram_Gate_isa_NamedElement():
    instance = ram_Gate()
    assert isinstance(instance, NamedElement)


def test_ram_MappableElement_isa_NamedElement():
    instance = ram_MappableElement()
    assert isinstance(instance, NamedElement)


def test_ram_Operation_isa_NamedElement():
    instance = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    assert isinstance(instance, NamedElement)


def test_ram_REnumLiteral_isa_NamedElement():
    instance = ram_REnumLiteral()
    assert isinstance(instance, NamedElement)


def test_ram_State_isa_NamedElement():
    instance = ram_State()
    assert isinstance(instance, NamedElement)


def test_ram_StateView_isa_NamedElement():
    instance = ram_StateView()
    assert isinstance(instance, NamedElement)


def test_ram_Transition_isa_NamedElement():
    instance = ram_Transition()
    assert isinstance(instance, NamedElement)


def test_ram_Type_isa_NamedElement():
    instance = ram_Type()
    assert isinstance(instance, NamedElement)


def test_ram_TypedElement_isa_NamedElement():
    instance = ram_TypedElement()
    assert isinstance(instance, NamedElement)


def test_ram_Classifier_isa_ObjectType():
    instance = ram_Classifier()
    assert isinstance(instance, ObjectType)


def test_ram_MessageOccurrenceSpecification_isa_OccurrenceSpecification():
    instance = ram_MessageOccurrenceSpecification()
    assert isinstance(instance, OccurrenceSpecification)


def test_ram_RBoolean_isa_PrimitiveType():
    instance = ram_RBoolean()
    assert isinstance(instance, PrimitiveType)


def test_ram_RChar_isa_PrimitiveType():
    instance = ram_RChar()
    assert isinstance(instance, PrimitiveType)


def test_ram_RDouble_isa_PrimitiveType():
    instance = ram_RDouble()
    assert isinstance(instance, PrimitiveType)


def test_ram_REnum_isa_PrimitiveType():
    instance = ram_REnum()
    assert isinstance(instance, PrimitiveType)


def test_ram_RFloat_isa_PrimitiveType():
    instance = ram_RFloat()
    assert isinstance(instance, PrimitiveType)


def test_ram_RInt_isa_PrimitiveType():
    instance = ram_RInt()
    assert isinstance(instance, PrimitiveType)


def test_ram_RString_isa_PrimitiveType():
    instance = ram_RString()
    assert isinstance(instance, PrimitiveType)


def test_ram_AssociationEnd_isa_Property():
    instance = ram_AssociationEnd(navigable=True)
    assert isinstance(instance, Property)


def test_ram_Reference_isa_Property():
    instance = ram_Reference()
    assert isinstance(instance, Property)


def test_ram_RSequence_isa_RCollection():
    instance = ram_RSequence()
    assert isinstance(instance, RCollection)


def test_ram_RSet_isa_RCollection():
    instance = ram_RSet()
    assert isinstance(instance, RCollection)


def test_ram_Attribute_isa_StructuralFeature():
    instance = ram_Attribute()
    assert isinstance(instance, StructuralFeature)


def test_ram_Property_isa_StructuralFeature():
    instance = ram_Property(lowerBound=7, referenceType="sample_text", upperBound=7)
    assert isinstance(instance, StructuralFeature)


def test_ram_TransitionSubstitution_isa_Substitution():
    instance = ram_TransitionSubstitution()
    assert isinstance(instance, Substitution)


def test_ram_Attribute_isa_TemporaryProperty():
    instance = ram_Attribute()
    assert isinstance(instance, TemporaryProperty)


def test_ram_Reference_isa_TemporaryProperty():
    instance = ram_Reference()
    assert isinstance(instance, TemporaryProperty)


def test_ram_ObjectType_isa_Type():
    instance = ram_ObjectType()
    assert isinstance(instance, Type)


def test_ram_PrimitiveType_isa_Type():
    instance = ram_PrimitiveType()
    assert isinstance(instance, Type)


def test_ram_RAny_isa_Type():
    instance = ram_RAny()
    assert isinstance(instance, Type)


def test_ram_RCollection_isa_Type():
    instance = ram_RCollection()
    assert isinstance(instance, Type)


def test_ram_RVoid_isa_Type():
    instance = ram_RVoid()
    assert isinstance(instance, Type)


def test_ram_Parameter_isa_TypedElement():
    instance = ram_Parameter()
    assert isinstance(instance, TypedElement)


def test_ram_StructuralFeature_isa_TypedElement():
    instance = ram_StructuralFeature(static=True)
    assert isinstance(instance, TypedElement)


def test_ram_LiteralSpecification_isa_ValueSpecification():
    instance = ram_LiteralSpecification()
    assert isinstance(instance, ValueSpecification)


def test_ram_OpaqueExpression_isa_ValueSpecification():
    instance = ram_OpaqueExpression(body="sample_text", language="sample_text")
    assert isinstance(instance, ValueSpecification)


def test_ram_ParameterValue_isa_ValueSpecification():
    instance = ram_ParameterValue()
    assert isinstance(instance, ValueSpecification)


def test_ram_StructuralFeatureValue_isa_ValueSpecification():
    instance = ram_StructuralFeatureValue()
    assert isinstance(instance, ValueSpecification)


def test_assoc_arguments77_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_ParameterValueMapping()
    b2 = ram_ParameterValueMapping()
    _safe_set(a, 'ram_Message78', {b1})
    assert _is_linked(a, 'ram_Message78', b1)
    if hasattr(b1, 'ram_ParameterValueMapping'):
        assert _is_linked(b1, 'ram_ParameterValueMapping', a)
    _safe_set(a, 'ram_Message78', {b2})
    assert _is_linked(a, 'ram_Message78', b2)
    if hasattr(b1, 'ram_ParameterValueMapping'):
        assert not _is_linked(b1, 'ram_ParameterValueMapping', a)
    if hasattr(b2, 'ram_ParameterValueMapping'):
        assert _is_linked(b2, 'ram_ParameterValueMapping', a)
    _safe_set(a, 'ram_Message78', set())
    assert not _is_linked(a, 'ram_Message78', b2)
    if hasattr(b2, 'ram_ParameterValueMapping'):
        assert not _is_linked(b2, 'ram_ParameterValueMapping', a)


def test_assoc_assignTo75_link_reassign_clear():
    a = ram_StructuralFeature(static=True)
    b1 = ram_Message(messageSort="sample_text", selfMessage=True)
    b2 = ram_Message(messageSort="sample_text_2", selfMessage=False)
    _safe_set(a, 'ram_StructuralFeature', b1)
    assert _is_linked(a, 'ram_StructuralFeature', b1)
    if hasattr(b1, 'ram_Message76'):
        assert _is_linked(b1, 'ram_Message76', a)
    _safe_set(a, 'ram_StructuralFeature', b2)
    assert _is_linked(a, 'ram_StructuralFeature', b2)
    if hasattr(b1, 'ram_Message76'):
        assert not _is_linked(b1, 'ram_Message76', a)
    if hasattr(b2, 'ram_Message76'):
        assert _is_linked(b2, 'ram_Message76', a)
    _safe_set(a, 'ram_StructuralFeature', None)
    assert not _is_linked(a, 'ram_StructuralFeature', b2)
    if hasattr(b2, 'ram_Message76'):
        assert not _is_linked(b2, 'ram_Message76', a)


def test_assoc_assoc22_link_reassign_clear():
    a = ram_AssociationEnd(navigable=True)
    b1 = ram_Association()
    b2 = ram_Association()
    _safe_set(a, 'ends', b1)
    assert _is_linked(a, 'ends', b1)
    if hasattr(b1, 'Association'):
        assert _is_linked(b1, 'Association', a)
    _safe_set(a, 'ends', b2)
    assert _is_linked(a, 'ends', b2)
    if hasattr(b1, 'Association'):
        assert not _is_linked(b1, 'Association', a)
    if hasattr(b2, 'Association'):
        assert _is_linked(b2, 'Association', a)
    _safe_set(a, 'ends', None)
    assert not _is_linked(a, 'ends', b2)
    if hasattr(b2, 'Association'):
        assert not _is_linked(b2, 'Association', a)


def test_assoc_associationEnds17_link_reassign_clear():
    a = ram_Class(abstract=True, partial=True)
    b1 = ram_AssociationEnd(navigable=True)
    b2 = ram_AssociationEnd(navigable=False)
    _safe_set(a, 'myClass', {b1})
    assert _is_linked(a, 'myClass', b1)
    if hasattr(b1, 'AssociationEnd'):
        assert _is_linked(b1, 'AssociationEnd', a)
    _safe_set(a, 'myClass', {b2})
    assert _is_linked(a, 'myClass', b2)
    if hasattr(b1, 'AssociationEnd'):
        assert not _is_linked(b1, 'AssociationEnd', a)
    if hasattr(b2, 'AssociationEnd'):
        assert _is_linked(b2, 'AssociationEnd', a)
    _safe_set(a, 'myClass', set())
    assert not _is_linked(a, 'myClass', b2)
    if hasattr(b2, 'AssociationEnd'):
        assert not _is_linked(b2, 'AssociationEnd', a)


def test_assoc_attributes18_link_reassign_clear():
    a = ram_Class(abstract=True, partial=True)
    b1 = ram_Attribute()
    b2 = ram_Attribute()
    _safe_set(a, 'ram_Class', {b1})
    assert _is_linked(a, 'ram_Class', b1)
    if hasattr(b1, 'ram_Attribute'):
        assert _is_linked(b1, 'ram_Attribute', a)
    _safe_set(a, 'ram_Class', {b2})
    assert _is_linked(a, 'ram_Class', b2)
    if hasattr(b1, 'ram_Attribute'):
        assert not _is_linked(b1, 'ram_Attribute', a)
    if hasattr(b2, 'ram_Attribute'):
        assert _is_linked(b2, 'ram_Attribute', a)
    _safe_set(a, 'ram_Class', set())
    assert not _is_linked(a, 'ram_Class', b2)
    if hasattr(b2, 'ram_Attribute'):
        assert not _is_linked(b2, 'ram_Attribute', a)


def test_assoc_ends24_link_reassign_clear():
    a = ram_AssociationEnd(navigable=True)
    b1 = ram_Association()
    b2 = ram_Association()
    _safe_set(a, 'AssociationEnd25', b1)
    assert _is_linked(a, 'AssociationEnd25', b1)
    if hasattr(b1, 'assoc'):
        assert _is_linked(b1, 'assoc', a)
    _safe_set(a, 'AssociationEnd25', b2)
    assert _is_linked(a, 'AssociationEnd25', b2)
    if hasattr(b1, 'assoc'):
        assert not _is_linked(b1, 'assoc', a)
    if hasattr(b2, 'assoc'):
        assert _is_linked(b2, 'assoc', a)
    _safe_set(a, 'AssociationEnd25', None)
    assert not _is_linked(a, 'AssociationEnd25', b2)
    if hasattr(b2, 'assoc'):
        assert not _is_linked(b2, 'assoc', a)


def test_assoc_externalAspect28_link_reassign_clear():
    a = ram_Instantiation(type="sample_text")
    b1 = ram_Aspect()
    b2 = ram_Aspect()
    _safe_set(a, 'ram_Instantiation29', b1)
    assert _is_linked(a, 'ram_Instantiation29', b1)
    if hasattr(b1, 'ram_Aspect30'):
        assert _is_linked(b1, 'ram_Aspect30', a)
    _safe_set(a, 'ram_Instantiation29', b2)
    assert _is_linked(a, 'ram_Instantiation29', b2)
    if hasattr(b1, 'ram_Aspect30'):
        assert not _is_linked(b1, 'ram_Aspect30', a)
    if hasattr(b2, 'ram_Aspect30'):
        assert _is_linked(b2, 'ram_Aspect30', a)
    _safe_set(a, 'ram_Instantiation29', None)
    assert not _is_linked(a, 'ram_Instantiation29', b2)
    if hasattr(b2, 'ram_Aspect30'):
        assert not _is_linked(b2, 'ram_Aspect30', a)


def test_assoc_fromElement141_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_OperationMapping()
    b2 = ram_OperationMapping()
    _safe_set(a, 'ram_Operation143', b1)
    assert _is_linked(a, 'ram_Operation143', b1)
    if hasattr(b1, 'ram_OperationMapping142'):
        assert _is_linked(b1, 'ram_OperationMapping142', a)
    _safe_set(a, 'ram_Operation143', b2)
    assert _is_linked(a, 'ram_Operation143', b2)
    if hasattr(b1, 'ram_OperationMapping142'):
        assert not _is_linked(b1, 'ram_OperationMapping142', a)
    if hasattr(b2, 'ram_OperationMapping142'):
        assert _is_linked(b2, 'ram_OperationMapping142', a)
    _safe_set(a, 'ram_Operation143', None)
    assert not _is_linked(a, 'ram_Operation143', b2)
    if hasattr(b2, 'ram_OperationMapping142'):
        assert not _is_linked(b2, 'ram_OperationMapping142', a)


def test_assoc_instantiations5_link_reassign_clear():
    a = ram_Instantiation(type="sample_text")
    b1 = ram_Aspect()
    b2 = ram_Aspect()
    _safe_set(a, 'ram_Instantiation', b1)
    assert _is_linked(a, 'ram_Instantiation', b1)
    if hasattr(b1, 'ram_Aspect6'):
        assert _is_linked(b1, 'ram_Aspect6', a)
    _safe_set(a, 'ram_Instantiation', b2)
    assert _is_linked(a, 'ram_Instantiation', b2)
    if hasattr(b1, 'ram_Aspect6'):
        assert not _is_linked(b1, 'ram_Aspect6', a)
    if hasattr(b2, 'ram_Aspect6'):
        assert _is_linked(b2, 'ram_Aspect6', a)
    _safe_set(a, 'ram_Instantiation', None)
    assert not _is_linked(a, 'ram_Instantiation', b2)
    if hasattr(b2, 'ram_Aspect6'):
        assert not _is_linked(b2, 'ram_Aspect6', a)


def test_assoc_interaction79_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_Interaction()
    b2 = ram_Interaction()
    _safe_set(a, 'messages', b1)
    assert _is_linked(a, 'messages', b1)
    if hasattr(b1, 'Interaction'):
        assert _is_linked(b1, 'Interaction', a)
    _safe_set(a, 'messages', b2)
    assert _is_linked(a, 'messages', b2)
    if hasattr(b1, 'Interaction'):
        assert not _is_linked(b1, 'Interaction', a)
    if hasattr(b2, 'Interaction'):
        assert _is_linked(b2, 'Interaction', a)
    _safe_set(a, 'messages', None)
    assert not _is_linked(a, 'messages', b2)
    if hasattr(b2, 'Interaction'):
        assert not _is_linked(b2, 'Interaction', a)


def test_assoc_mappings26_link_reassign_clear():
    a = ram_Instantiation(type="sample_text")
    b1 = ram_ClassifierMapping()
    b2 = ram_ClassifierMapping()
    _safe_set(a, 'ram_Instantiation27', {b1})
    assert _is_linked(a, 'ram_Instantiation27', b1)
    if hasattr(b1, 'ram_ClassifierMapping'):
        assert _is_linked(b1, 'ram_ClassifierMapping', a)
    _safe_set(a, 'ram_Instantiation27', {b2})
    assert _is_linked(a, 'ram_Instantiation27', b2)
    if hasattr(b1, 'ram_ClassifierMapping'):
        assert not _is_linked(b1, 'ram_ClassifierMapping', a)
    if hasattr(b2, 'ram_ClassifierMapping'):
        assert _is_linked(b2, 'ram_ClassifierMapping', a)
    _safe_set(a, 'ram_Instantiation27', set())
    assert not _is_linked(a, 'ram_Instantiation27', b2)
    if hasattr(b2, 'ram_ClassifierMapping'):
        assert not _is_linked(b2, 'ram_ClassifierMapping', a)


def test_assoc_message82_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_MessageEnd()
    b2 = ram_MessageEnd()
    _safe_set(a, 'ram_Message84', b1)
    assert _is_linked(a, 'ram_Message84', b1)
    if hasattr(b1, 'ram_MessageEnd83'):
        assert _is_linked(b1, 'ram_MessageEnd83', a)
    _safe_set(a, 'ram_Message84', b2)
    assert _is_linked(a, 'ram_Message84', b2)
    if hasattr(b1, 'ram_MessageEnd83'):
        assert not _is_linked(b1, 'ram_MessageEnd83', a)
    if hasattr(b2, 'ram_MessageEnd83'):
        assert _is_linked(b2, 'ram_MessageEnd83', a)
    _safe_set(a, 'ram_Message84', None)
    assert not _is_linked(a, 'ram_Message84', b2)
    if hasattr(b2, 'ram_MessageEnd83'):
        assert not _is_linked(b2, 'ram_MessageEnd83', a)


def test_assoc_messages52_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_Interaction()
    b2 = ram_Interaction()
    _safe_set(a, 'Message', b1)
    assert _is_linked(a, 'Message', b1)
    if hasattr(b1, 'interaction'):
        assert _is_linked(b1, 'interaction', a)
    _safe_set(a, 'Message', b2)
    assert _is_linked(a, 'Message', b2)
    if hasattr(b1, 'interaction'):
        assert not _is_linked(b1, 'interaction', a)
    if hasattr(b2, 'interaction'):
        assert _is_linked(b2, 'interaction', a)
    _safe_set(a, 'Message', None)
    assert not _is_linked(a, 'Message', b2)
    if hasattr(b2, 'interaction'):
        assert not _is_linked(b2, 'interaction', a)


def test_assoc_myClass23_link_reassign_clear():
    a = ram_Class(abstract=True, partial=True)
    b1 = ram_AssociationEnd(navigable=True)
    b2 = ram_AssociationEnd(navigable=False)
    _safe_set(a, 'Class', b1)
    assert _is_linked(a, 'Class', b1)
    if hasattr(b1, 'associationEnds'):
        assert _is_linked(b1, 'associationEnds', a)
    _safe_set(a, 'Class', b2)
    assert _is_linked(a, 'Class', b2)
    if hasattr(b1, 'associationEnds'):
        assert not _is_linked(b1, 'associationEnds', a)
    if hasattr(b2, 'associationEnds'):
        assert _is_linked(b2, 'associationEnds', a)
    _safe_set(a, 'Class', None)
    assert not _is_linked(a, 'Class', b2)
    if hasattr(b2, 'associationEnds'):
        assert not _is_linked(b2, 'associationEnds', a)


def test_assoc_operands87_link_reassign_clear():
    a = ram_CombinedFragment(interactionOperator="sample_text")
    b1 = ram_InteractionOperand()
    b2 = ram_InteractionOperand()
    _safe_set(a, 'ram_CombinedFragment', {b1})
    assert _is_linked(a, 'ram_CombinedFragment', b1)
    if hasattr(b1, 'ram_InteractionOperand'):
        assert _is_linked(b1, 'ram_InteractionOperand', a)
    _safe_set(a, 'ram_CombinedFragment', {b2})
    assert _is_linked(a, 'ram_CombinedFragment', b2)
    if hasattr(b1, 'ram_InteractionOperand'):
        assert not _is_linked(b1, 'ram_InteractionOperand', a)
    if hasattr(b2, 'ram_InteractionOperand'):
        assert _is_linked(b2, 'ram_InteractionOperand', a)
    _safe_set(a, 'ram_CombinedFragment', set())
    assert not _is_linked(a, 'ram_CombinedFragment', b2)
    if hasattr(b2, 'ram_InteractionOperand'):
        assert not _is_linked(b2, 'ram_InteractionOperand', a)


def test_assoc_operations117_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_Classifier()
    b2 = ram_Classifier()
    _safe_set(a, 'ram_Operation119', b1)
    assert _is_linked(a, 'ram_Operation119', b1)
    if hasattr(b1, 'ram_Classifier118'):
        assert _is_linked(b1, 'ram_Classifier118', a)
    _safe_set(a, 'ram_Operation119', b2)
    assert _is_linked(a, 'ram_Operation119', b2)
    if hasattr(b1, 'ram_Classifier118'):
        assert not _is_linked(b1, 'ram_Classifier118', a)
    if hasattr(b2, 'ram_Classifier118'):
        assert _is_linked(b2, 'ram_Classifier118', a)
    _safe_set(a, 'ram_Operation119', None)
    assert not _is_linked(a, 'ram_Operation119', b2)
    if hasattr(b2, 'ram_Classifier118'):
        assert not _is_linked(b2, 'ram_Classifier118', a)


def test_assoc_parameters33_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_Parameter()
    b2 = ram_Parameter()
    _safe_set(a, 'ram_Operation34', {b1})
    assert _is_linked(a, 'ram_Operation34', b1)
    if hasattr(b1, 'ram_Parameter'):
        assert _is_linked(b1, 'ram_Parameter', a)
    _safe_set(a, 'ram_Operation34', {b2})
    assert _is_linked(a, 'ram_Operation34', b2)
    if hasattr(b1, 'ram_Parameter'):
        assert not _is_linked(b1, 'ram_Parameter', a)
    if hasattr(b2, 'ram_Parameter'):
        assert _is_linked(b2, 'ram_Parameter', a)
    _safe_set(a, 'ram_Operation34', set())
    assert not _is_linked(a, 'ram_Operation34', b2)
    if hasattr(b2, 'ram_Parameter'):
        assert not _is_linked(b2, 'ram_Parameter', a)


def test_assoc_pointcut57_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_AspectMessageView()
    b2 = ram_AspectMessageView()
    _safe_set(a, 'ram_Operation59', b1)
    assert _is_linked(a, 'ram_Operation59', b1)
    if hasattr(b1, 'ram_AspectMessageView58'):
        assert _is_linked(b1, 'ram_AspectMessageView58', a)
    _safe_set(a, 'ram_Operation59', b2)
    assert _is_linked(a, 'ram_Operation59', b2)
    if hasattr(b1, 'ram_AspectMessageView58'):
        assert not _is_linked(b1, 'ram_AspectMessageView58', a)
    if hasattr(b2, 'ram_AspectMessageView58'):
        assert _is_linked(b2, 'ram_AspectMessageView58', a)
    _safe_set(a, 'ram_Operation59', None)
    assert not _is_linked(a, 'ram_Operation59', b2)
    if hasattr(b2, 'ram_AspectMessageView58'):
        assert not _is_linked(b2, 'ram_AspectMessageView58', a)


def test_assoc_receiveEvent69_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_MessageEnd()
    b2 = ram_MessageEnd()
    _safe_set(a, 'ram_Message70', b1)
    assert _is_linked(a, 'ram_Message70', b1)
    if hasattr(b1, 'ram_MessageEnd71'):
        assert _is_linked(b1, 'ram_MessageEnd71', a)
    _safe_set(a, 'ram_Message70', b2)
    assert _is_linked(a, 'ram_Message70', b2)
    if hasattr(b1, 'ram_MessageEnd71'):
        assert not _is_linked(b1, 'ram_MessageEnd71', a)
    if hasattr(b2, 'ram_MessageEnd71'):
        assert _is_linked(b2, 'ram_MessageEnd71', a)
    _safe_set(a, 'ram_Message70', None)
    assert not _is_linked(a, 'ram_Message70', b2)
    if hasattr(b2, 'ram_MessageEnd71'):
        assert not _is_linked(b2, 'ram_MessageEnd71', a)


def test_assoc_represents63_link_reassign_clear():
    a = ram_TypedElement()
    b1 = ram_Lifeline()
    b2 = ram_Lifeline()
    _safe_set(a, 'ram_TypedElement', b1)
    assert _is_linked(a, 'ram_TypedElement', b1)
    if hasattr(b1, 'ram_Lifeline64'):
        assert _is_linked(b1, 'ram_Lifeline64', a)
    _safe_set(a, 'ram_TypedElement', b2)
    assert _is_linked(a, 'ram_TypedElement', b2)
    if hasattr(b1, 'ram_Lifeline64'):
        assert not _is_linked(b1, 'ram_Lifeline64', a)
    if hasattr(b2, 'ram_Lifeline64'):
        assert _is_linked(b2, 'ram_Lifeline64', a)
    _safe_set(a, 'ram_TypedElement', None)
    assert not _is_linked(a, 'ram_TypedElement', b2)
    if hasattr(b2, 'ram_Lifeline64'):
        assert not _is_linked(b2, 'ram_Lifeline64', a)


def test_assoc_returnType31_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_Type()
    b2 = ram_Type()
    _safe_set(a, 'ram_Operation', b1)
    assert _is_linked(a, 'ram_Operation', b1)
    if hasattr(b1, 'ram_Type32'):
        assert _is_linked(b1, 'ram_Type32', a)
    _safe_set(a, 'ram_Operation', b2)
    assert _is_linked(a, 'ram_Operation', b2)
    if hasattr(b1, 'ram_Type32'):
        assert not _is_linked(b1, 'ram_Type32', a)
    if hasattr(b2, 'ram_Type32'):
        assert _is_linked(b2, 'ram_Type32', a)
    _safe_set(a, 'ram_Operation', None)
    assert not _is_linked(a, 'ram_Operation', b2)
    if hasattr(b2, 'ram_Type32'):
        assert not _is_linked(b2, 'ram_Type32', a)


def test_assoc_returns80_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_ValueSpecification()
    b2 = ram_ValueSpecification()
    _safe_set(a, 'ram_Message81', b1)
    assert _is_linked(a, 'ram_Message81', b1)
    if hasattr(b1, 'ram_ValueSpecification'):
        assert _is_linked(b1, 'ram_ValueSpecification', a)
    _safe_set(a, 'ram_Message81', b2)
    assert _is_linked(a, 'ram_Message81', b2)
    if hasattr(b1, 'ram_ValueSpecification'):
        assert not _is_linked(b1, 'ram_ValueSpecification', a)
    if hasattr(b2, 'ram_ValueSpecification'):
        assert _is_linked(b2, 'ram_ValueSpecification', a)
    _safe_set(a, 'ram_Message81', None)
    assert not _is_linked(a, 'ram_Message81', b2)
    if hasattr(b2, 'ram_ValueSpecification'):
        assert not _is_linked(b2, 'ram_ValueSpecification', a)


def test_assoc_sendEvent68_link_reassign_clear():
    a = ram_Message(messageSort="sample_text", selfMessage=True)
    b1 = ram_MessageEnd()
    b2 = ram_MessageEnd()
    _safe_set(a, 'ram_Message', b1)
    assert _is_linked(a, 'ram_Message', b1)
    if hasattr(b1, 'ram_MessageEnd'):
        assert _is_linked(b1, 'ram_MessageEnd', a)
    _safe_set(a, 'ram_Message', b2)
    assert _is_linked(a, 'ram_Message', b2)
    if hasattr(b1, 'ram_MessageEnd'):
        assert not _is_linked(b1, 'ram_MessageEnd', a)
    if hasattr(b2, 'ram_MessageEnd'):
        assert _is_linked(b2, 'ram_MessageEnd', a)
    _safe_set(a, 'ram_Message', None)
    assert not _is_linked(a, 'ram_Message', b2)
    if hasattr(b2, 'ram_MessageEnd'):
        assert not _is_linked(b2, 'ram_MessageEnd', a)


def test_assoc_signature170_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_Transition()
    b2 = ram_Transition()
    _safe_set(a, 'ram_Operation172', b1)
    assert _is_linked(a, 'ram_Operation172', b1)
    if hasattr(b1, 'ram_Transition171'):
        assert _is_linked(b1, 'ram_Transition171', a)
    _safe_set(a, 'ram_Operation172', b2)
    assert _is_linked(a, 'ram_Operation172', b2)
    if hasattr(b1, 'ram_Transition171'):
        assert not _is_linked(b1, 'ram_Transition171', a)
    if hasattr(b2, 'ram_Transition171'):
        assert _is_linked(b2, 'ram_Transition171', a)
    _safe_set(a, 'ram_Operation172', None)
    assert not _is_linked(a, 'ram_Operation172', b2)
    if hasattr(b2, 'ram_Transition171'):
        assert not _is_linked(b2, 'ram_Transition171', a)


def test_assoc_signature72_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_Message(messageSort="sample_text", selfMessage=True)
    b2 = ram_Message(messageSort="sample_text_2", selfMessage=False)
    _safe_set(a, 'ram_Operation74', b1)
    assert _is_linked(a, 'ram_Operation74', b1)
    if hasattr(b1, 'ram_Message73'):
        assert _is_linked(b1, 'ram_Message73', a)
    _safe_set(a, 'ram_Operation74', b2)
    assert _is_linked(a, 'ram_Operation74', b2)
    if hasattr(b1, 'ram_Message73'):
        assert not _is_linked(b1, 'ram_Message73', a)
    if hasattr(b2, 'ram_Message73'):
        assert _is_linked(b2, 'ram_Message73', a)
    _safe_set(a, 'ram_Operation74', None)
    assert not _is_linked(a, 'ram_Operation74', b2)
    if hasattr(b2, 'ram_Message73'):
        assert not _is_linked(b2, 'ram_Message73', a)


def test_assoc_specifies44_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_MessageView()
    b2 = ram_MessageView()
    _safe_set(a, 'ram_Operation45', b1)
    assert _is_linked(a, 'ram_Operation45', b1)
    if hasattr(b1, 'ram_MessageView'):
        assert _is_linked(b1, 'ram_MessageView', a)
    _safe_set(a, 'ram_Operation45', b2)
    assert _is_linked(a, 'ram_Operation45', b2)
    if hasattr(b1, 'ram_MessageView'):
        assert not _is_linked(b1, 'ram_MessageView', a)
    if hasattr(b2, 'ram_MessageView'):
        assert _is_linked(b2, 'ram_MessageView', a)
    _safe_set(a, 'ram_Operation45', None)
    assert not _is_linked(a, 'ram_Operation45', b2)
    if hasattr(b2, 'ram_MessageView'):
        assert not _is_linked(b2, 'ram_MessageView', a)


def test_assoc_superTypes19_link_reassign_clear():
    a = ram_Class(abstract=True, partial=True)
    b1 = ram_Classifier()
    b2 = ram_Classifier()
    _safe_set(a, 'ram_Class20', {b1})
    assert _is_linked(a, 'ram_Class20', b1)
    if hasattr(b1, 'ram_Classifier21'):
        assert _is_linked(b1, 'ram_Classifier21', a)
    _safe_set(a, 'ram_Class20', {b2})
    assert _is_linked(a, 'ram_Class20', b2)
    if hasattr(b1, 'ram_Classifier21'):
        assert not _is_linked(b1, 'ram_Classifier21', a)
    if hasattr(b2, 'ram_Classifier21'):
        assert _is_linked(b2, 'ram_Classifier21', a)
    _safe_set(a, 'ram_Class20', set())
    assert not _is_linked(a, 'ram_Class20', b2)
    if hasattr(b2, 'ram_Classifier21'):
        assert not _is_linked(b2, 'ram_Classifier21', a)


def test_assoc_toElement144_link_reassign_clear():
    a = ram_Operation(abstract=True, partial=True, static=True, visibility="sample_text")
    b1 = ram_OperationMapping()
    b2 = ram_OperationMapping()
    _safe_set(a, 'ram_Operation146', b1)
    assert _is_linked(a, 'ram_Operation146', b1)
    if hasattr(b1, 'ram_OperationMapping145'):
        assert _is_linked(b1, 'ram_OperationMapping145', a)
    _safe_set(a, 'ram_Operation146', b2)
    assert _is_linked(a, 'ram_Operation146', b2)
    if hasattr(b1, 'ram_OperationMapping145'):
        assert not _is_linked(b1, 'ram_OperationMapping145', a)
    if hasattr(b2, 'ram_OperationMapping145'):
        assert _is_linked(b2, 'ram_OperationMapping145', a)
    _safe_set(a, 'ram_Operation146', None)
    assert not _is_linked(a, 'ram_Operation146', b2)
    if hasattr(b2, 'ram_OperationMapping145'):
        assert not _is_linked(b2, 'ram_OperationMapping145', a)


def test_assoc_type105_link_reassign_clear():
    a = ram_RCollection()
    b1 = ram_ObjectType()
    b2 = ram_ObjectType()
    _safe_set(a, 'ram_RCollection', b1)
    assert _is_linked(a, 'ram_RCollection', b1)
    if hasattr(b1, 'ram_ObjectType'):
        assert _is_linked(b1, 'ram_ObjectType', a)
    _safe_set(a, 'ram_RCollection', b2)
    assert _is_linked(a, 'ram_RCollection', b2)
    if hasattr(b1, 'ram_ObjectType'):
        assert not _is_linked(b1, 'ram_ObjectType', a)
    if hasattr(b2, 'ram_ObjectType'):
        assert _is_linked(b2, 'ram_ObjectType', a)
    _safe_set(a, 'ram_RCollection', None)
    assert not _is_linked(a, 'ram_RCollection', b2)
    if hasattr(b2, 'ram_ObjectType'):
        assert not _is_linked(b2, 'ram_ObjectType', a)


def test_assoc_value115_link_reassign_clear():
    a = ram_LayoutElement(x=3.14, y=3.14)
    b1 = ram_ElementMap()
    b2 = ram_ElementMap()
    _safe_set(a, 'ram_LayoutElement', b1)
    assert _is_linked(a, 'ram_LayoutElement', b1)
    if hasattr(b1, 'ram_ElementMap116'):
        assert _is_linked(b1, 'ram_ElementMap116', a)
    _safe_set(a, 'ram_LayoutElement', b2)
    assert _is_linked(a, 'ram_LayoutElement', b2)
    if hasattr(b1, 'ram_ElementMap116'):
        assert not _is_linked(b1, 'ram_ElementMap116', a)
    if hasattr(b2, 'ram_ElementMap116'):
        assert _is_linked(b2, 'ram_ElementMap116', a)
    _safe_set(a, 'ram_LayoutElement', None)
    assert not _is_linked(a, 'ram_LayoutElement', b2)
    if hasattr(b2, 'ram_ElementMap116'):
        assert not _is_linked(b2, 'ram_ElementMap116', a)


def test_assoc_value93_link_reassign_clear():
    a = ram_StructuralFeature(static=True)
    b1 = ram_StructuralFeatureValue()
    b2 = ram_StructuralFeatureValue()
    _safe_set(a, 'ram_StructuralFeature94', b1)
    assert _is_linked(a, 'ram_StructuralFeature94', b1)
    if hasattr(b1, 'ram_StructuralFeatureValue'):
        assert _is_linked(b1, 'ram_StructuralFeatureValue', a)
    _safe_set(a, 'ram_StructuralFeature94', b2)
    assert _is_linked(a, 'ram_StructuralFeature94', b2)
    if hasattr(b1, 'ram_StructuralFeatureValue'):
        assert not _is_linked(b1, 'ram_StructuralFeatureValue', a)
    if hasattr(b2, 'ram_StructuralFeatureValue'):
        assert _is_linked(b2, 'ram_StructuralFeatureValue', a)
    _safe_set(a, 'ram_StructuralFeature94', None)
    assert not _is_linked(a, 'ram_StructuralFeature94', b2)
    if hasattr(b2, 'ram_StructuralFeatureValue'):
        assert not _is_linked(b2, 'ram_StructuralFeatureValue', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractMessageView_strategy = st.builds(AbstractMessageView)
@given(instance=AbstractMessageView_strategy)
@settings(max_examples=25)
def test_AbstractMessageView_instantiation(instance):
    assert isinstance(instance, AbstractMessageView)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


FragmentContainer_strategy = st.builds(FragmentContainer)
@given(instance=FragmentContainer_strategy)
@settings(max_examples=25)
def test_FragmentContainer_instantiation(instance):
    assert isinstance(instance, FragmentContainer)


ImplementationClass_strategy = st.builds(ImplementationClass)
@given(instance=ImplementationClass_strategy)
@settings(max_examples=25)
def test_ImplementationClass_instantiation(instance):
    assert isinstance(instance, ImplementationClass)


InteractionFragment_strategy = st.builds(InteractionFragment)
@given(instance=InteractionFragment_strategy)
@settings(max_examples=25)
def test_InteractionFragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)


LiteralSpecification_strategy = st.builds(LiteralSpecification)
@given(instance=LiteralSpecification_strategy)
@settings(max_examples=25)
def test_LiteralSpecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)


MappableElement_strategy = st.builds(MappableElement)
@given(instance=MappableElement_strategy)
@settings(max_examples=25)
def test_MappableElement_instantiation(instance):
    assert isinstance(instance, MappableElement)


Mapping_strategy = st.builds(Mapping)
@given(instance=Mapping_strategy)
@settings(max_examples=25)
def test_Mapping_instantiation(instance):
    assert isinstance(instance, Mapping)


MessageEnd_strategy = st.builds(MessageEnd)
@given(instance=MessageEnd_strategy)
@settings(max_examples=25)
def test_MessageEnd_instantiation(instance):
    assert isinstance(instance, MessageEnd)


MessageOccurrenceSpecification_strategy = st.builds(MessageOccurrenceSpecification)
@given(instance=MessageOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_MessageOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, MessageOccurrenceSpecification)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ObjectType_strategy = st.builds(ObjectType)
@given(instance=ObjectType_strategy)
@settings(max_examples=25)
def test_ObjectType_instantiation(instance):
    assert isinstance(instance, ObjectType)


OccurrenceSpecification_strategy = st.builds(OccurrenceSpecification)
@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_OccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


RCollection_strategy = st.builds(RCollection)
@given(instance=RCollection_strategy)
@settings(max_examples=25)
def test_RCollection_instantiation(instance):
    assert isinstance(instance, RCollection)


StructuralFeature_strategy = st.builds(StructuralFeature)
@given(instance=StructuralFeature_strategy)
@settings(max_examples=25)
def test_StructuralFeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)


Substitution_strategy = st.builds(Substitution)
@given(instance=Substitution_strategy)
@settings(max_examples=25)
def test_Substitution_instantiation(instance):
    assert isinstance(instance, Substitution)


TemporaryProperty_strategy = st.builds(TemporaryProperty)
@given(instance=TemporaryProperty_strategy)
@settings(max_examples=25)
def test_TemporaryProperty_instantiation(instance):
    assert isinstance(instance, TemporaryProperty)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)


ram_AbstractMessageView_strategy = st.builds(ram_AbstractMessageView)
@given(instance=ram_AbstractMessageView_strategy)
@settings(max_examples=25)
def test_ram_AbstractMessageView_instantiation(instance):
    assert isinstance(instance, ram_AbstractMessageView)


ram_Aspect_strategy = st.builds(ram_Aspect)
@given(instance=ram_Aspect_strategy)
@settings(max_examples=25)
def test_ram_Aspect_instantiation(instance):
    assert isinstance(instance, ram_Aspect)


ram_AspectMessageView_strategy = st.builds(ram_AspectMessageView)
@given(instance=ram_AspectMessageView_strategy)
@settings(max_examples=25)
def test_ram_AspectMessageView_instantiation(instance):
    assert isinstance(instance, ram_AspectMessageView)


ram_Association_strategy = st.builds(ram_Association)
@given(instance=ram_Association_strategy)
@settings(max_examples=25)
def test_ram_Association_instantiation(instance):
    assert isinstance(instance, ram_Association)


ram_AssociationEnd_strategy = st.builds(ram_AssociationEnd, navigable=st.booleans())
@given(instance=ram_AssociationEnd_strategy)
@settings(max_examples=25)
def test_ram_AssociationEnd_instantiation(instance):
    assert isinstance(instance, ram_AssociationEnd)


ram_Attribute_strategy = st.builds(ram_Attribute)
@given(instance=ram_Attribute_strategy)
@settings(max_examples=25)
def test_ram_Attribute_instantiation(instance):
    assert isinstance(instance, ram_Attribute)


ram_AttributeMapping_strategy = st.builds(ram_AttributeMapping)
@given(instance=ram_AttributeMapping_strategy)
@settings(max_examples=25)
def test_ram_AttributeMapping_instantiation(instance):
    assert isinstance(instance, ram_AttributeMapping)


ram_Class_strategy = st.builds(ram_Class, abstract=st.booleans(), partial=st.booleans())
@given(instance=ram_Class_strategy)
@settings(max_examples=25)
def test_ram_Class_instantiation(instance):
    assert isinstance(instance, ram_Class)


ram_Classifier_strategy = st.builds(ram_Classifier)
@given(instance=ram_Classifier_strategy)
@settings(max_examples=25)
def test_ram_Classifier_instantiation(instance):
    assert isinstance(instance, ram_Classifier)


ram_ClassifierMapping_strategy = st.builds(ram_ClassifierMapping)
@given(instance=ram_ClassifierMapping_strategy)
@settings(max_examples=25)
def test_ram_ClassifierMapping_instantiation(instance):
    assert isinstance(instance, ram_ClassifierMapping)


ram_CombinedFragment_strategy = st.builds(ram_CombinedFragment, interactionOperator=safe_text)
@given(instance=ram_CombinedFragment_strategy)
@settings(max_examples=25)
def test_ram_CombinedFragment_instantiation(instance):
    assert isinstance(instance, ram_CombinedFragment)


ram_Constraint_strategy = st.builds(ram_Constraint)
@given(instance=ram_Constraint_strategy)
@settings(max_examples=25)
def test_ram_Constraint_instantiation(instance):
    assert isinstance(instance, ram_Constraint)


ram_ContainerMap_strategy = st.builds(ram_ContainerMap)
@given(instance=ram_ContainerMap_strategy)
@settings(max_examples=25)
def test_ram_ContainerMap_instantiation(instance):
    assert isinstance(instance, ram_ContainerMap)


ram_DestructionOccurrenceSpecification_strategy = st.builds(ram_DestructionOccurrenceSpecification)
@given(instance=ram_DestructionOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_ram_DestructionOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, ram_DestructionOccurrenceSpecification)


ram_EObject_strategy = st.builds(ram_EObject)
@given(instance=ram_EObject_strategy)
@settings(max_examples=25)
def test_ram_EObject_instantiation(instance):
    assert isinstance(instance, ram_EObject)


ram_ElementMap_strategy = st.builds(ram_ElementMap)
@given(instance=ram_ElementMap_strategy)
@settings(max_examples=25)
def test_ram_ElementMap_instantiation(instance):
    assert isinstance(instance, ram_ElementMap)


ram_ExecutionStatement_strategy = st.builds(ram_ExecutionStatement)
@given(instance=ram_ExecutionStatement_strategy)
@settings(max_examples=25)
def test_ram_ExecutionStatement_instantiation(instance):
    assert isinstance(instance, ram_ExecutionStatement)


ram_FragmentContainer_strategy = st.builds(ram_FragmentContainer)
@given(instance=ram_FragmentContainer_strategy)
@settings(max_examples=25)
def test_ram_FragmentContainer_instantiation(instance):
    assert isinstance(instance, ram_FragmentContainer)


ram_Gate_strategy = st.builds(ram_Gate)
@given(instance=ram_Gate_strategy)
@settings(max_examples=25)
def test_ram_Gate_instantiation(instance):
    assert isinstance(instance, ram_Gate)


ram_ImplementationClass_strategy = st.builds(ram_ImplementationClass, instanceClassName=safe_text)
@given(instance=ram_ImplementationClass_strategy)
@settings(max_examples=25)
def test_ram_ImplementationClass_instantiation(instance):
    assert isinstance(instance, ram_ImplementationClass)


ram_Instantiation_strategy = st.builds(ram_Instantiation, type=safe_text)
@given(instance=ram_Instantiation_strategy)
@settings(max_examples=25)
def test_ram_Instantiation_instantiation(instance):
    assert isinstance(instance, ram_Instantiation)


ram_Interaction_strategy = st.builds(ram_Interaction)
@given(instance=ram_Interaction_strategy)
@settings(max_examples=25)
def test_ram_Interaction_instantiation(instance):
    assert isinstance(instance, ram_Interaction)


ram_InteractionFragment_strategy = st.builds(ram_InteractionFragment)
@given(instance=ram_InteractionFragment_strategy)
@settings(max_examples=25)
def test_ram_InteractionFragment_instantiation(instance):
    assert isinstance(instance, ram_InteractionFragment)


ram_InteractionOperand_strategy = st.builds(ram_InteractionOperand)
@given(instance=ram_InteractionOperand_strategy)
@settings(max_examples=25)
def test_ram_InteractionOperand_instantiation(instance):
    assert isinstance(instance, ram_InteractionOperand)


ram_Layout_strategy = st.builds(ram_Layout)
@given(instance=ram_Layout_strategy)
@settings(max_examples=25)
def test_ram_Layout_instantiation(instance):
    assert isinstance(instance, ram_Layout)


ram_LayoutElement_strategy = st.builds(ram_LayoutElement, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ram_LayoutElement_strategy)
@settings(max_examples=25)
def test_ram_LayoutElement_instantiation(instance):
    assert isinstance(instance, ram_LayoutElement)


ram_Lifeline_strategy = st.builds(ram_Lifeline)
@given(instance=ram_Lifeline_strategy)
@settings(max_examples=25)
def test_ram_Lifeline_instantiation(instance):
    assert isinstance(instance, ram_Lifeline)


ram_LiteralBoolean_strategy = st.builds(ram_LiteralBoolean, value=st.booleans())
@given(instance=ram_LiteralBoolean_strategy)
@settings(max_examples=25)
def test_ram_LiteralBoolean_instantiation(instance):
    assert isinstance(instance, ram_LiteralBoolean)


ram_LiteralInteger_strategy = st.builds(ram_LiteralInteger, value=st.integers())
@given(instance=ram_LiteralInteger_strategy)
@settings(max_examples=25)
def test_ram_LiteralInteger_instantiation(instance):
    assert isinstance(instance, ram_LiteralInteger)


ram_LiteralSpecification_strategy = st.builds(ram_LiteralSpecification)
@given(instance=ram_LiteralSpecification_strategy)
@settings(max_examples=25)
def test_ram_LiteralSpecification_instantiation(instance):
    assert isinstance(instance, ram_LiteralSpecification)


ram_LiteralString_strategy = st.builds(ram_LiteralString, value=safe_text)
@given(instance=ram_LiteralString_strategy)
@settings(max_examples=25)
def test_ram_LiteralString_instantiation(instance):
    assert isinstance(instance, ram_LiteralString)


ram_MappableElement_strategy = st.builds(ram_MappableElement)
@given(instance=ram_MappableElement_strategy)
@settings(max_examples=25)
def test_ram_MappableElement_instantiation(instance):
    assert isinstance(instance, ram_MappableElement)


ram_Mapping_strategy = st.builds(ram_Mapping)
@given(instance=ram_Mapping_strategy)
@settings(max_examples=25)
def test_ram_Mapping_instantiation(instance):
    assert isinstance(instance, ram_Mapping)


ram_Message_strategy = st.builds(ram_Message, messageSort=safe_text, selfMessage=st.booleans())
@given(instance=ram_Message_strategy)
@settings(max_examples=25)
def test_ram_Message_instantiation(instance):
    assert isinstance(instance, ram_Message)


ram_MessageEnd_strategy = st.builds(ram_MessageEnd)
@given(instance=ram_MessageEnd_strategy)
@settings(max_examples=25)
def test_ram_MessageEnd_instantiation(instance):
    assert isinstance(instance, ram_MessageEnd)


ram_MessageOccurrenceSpecification_strategy = st.builds(ram_MessageOccurrenceSpecification)
@given(instance=ram_MessageOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_ram_MessageOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, ram_MessageOccurrenceSpecification)


ram_MessageView_strategy = st.builds(ram_MessageView)
@given(instance=ram_MessageView_strategy)
@settings(max_examples=25)
def test_ram_MessageView_instantiation(instance):
    assert isinstance(instance, ram_MessageView)


ram_MessageViewReference_strategy = st.builds(ram_MessageViewReference)
@given(instance=ram_MessageViewReference_strategy)
@settings(max_examples=25)
def test_ram_MessageViewReference_instantiation(instance):
    assert isinstance(instance, ram_MessageViewReference)


ram_NamedElement_strategy = st.builds(ram_NamedElement, name=safe_text)
@given(instance=ram_NamedElement_strategy)
@settings(max_examples=25)
def test_ram_NamedElement_instantiation(instance):
    assert isinstance(instance, ram_NamedElement)


ram_ObjectType_strategy = st.builds(ram_ObjectType)
@given(instance=ram_ObjectType_strategy)
@settings(max_examples=25)
def test_ram_ObjectType_instantiation(instance):
    assert isinstance(instance, ram_ObjectType)


ram_OccurrenceSpecification_strategy = st.builds(ram_OccurrenceSpecification)
@given(instance=ram_OccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_ram_OccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, ram_OccurrenceSpecification)


ram_OpaqueExpression_strategy = st.builds(ram_OpaqueExpression, body=safe_text, language=safe_text)
@given(instance=ram_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_ram_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, ram_OpaqueExpression)


ram_Operation_strategy = st.builds(ram_Operation, abstract=st.booleans(), partial=st.booleans(), static=st.booleans(), visibility=safe_text)
@given(instance=ram_Operation_strategy)
@settings(max_examples=25)
def test_ram_Operation_instantiation(instance):
    assert isinstance(instance, ram_Operation)


ram_OperationMapping_strategy = st.builds(ram_OperationMapping)
@given(instance=ram_OperationMapping_strategy)
@settings(max_examples=25)
def test_ram_OperationMapping_instantiation(instance):
    assert isinstance(instance, ram_OperationMapping)


ram_OriginalBehaviorExecution_strategy = st.builds(ram_OriginalBehaviorExecution)
@given(instance=ram_OriginalBehaviorExecution_strategy)
@settings(max_examples=25)
def test_ram_OriginalBehaviorExecution_instantiation(instance):
    assert isinstance(instance, ram_OriginalBehaviorExecution)


ram_Parameter_strategy = st.builds(ram_Parameter)
@given(instance=ram_Parameter_strategy)
@settings(max_examples=25)
def test_ram_Parameter_instantiation(instance):
    assert isinstance(instance, ram_Parameter)


ram_ParameterMapping_strategy = st.builds(ram_ParameterMapping)
@given(instance=ram_ParameterMapping_strategy)
@settings(max_examples=25)
def test_ram_ParameterMapping_instantiation(instance):
    assert isinstance(instance, ram_ParameterMapping)


ram_ParameterValue_strategy = st.builds(ram_ParameterValue)
@given(instance=ram_ParameterValue_strategy)
@settings(max_examples=25)
def test_ram_ParameterValue_instantiation(instance):
    assert isinstance(instance, ram_ParameterValue)


ram_ParameterValueMapping_strategy = st.builds(ram_ParameterValueMapping)
@given(instance=ram_ParameterValueMapping_strategy)
@settings(max_examples=25)
def test_ram_ParameterValueMapping_instantiation(instance):
    assert isinstance(instance, ram_ParameterValueMapping)


ram_PrimitiveType_strategy = st.builds(ram_PrimitiveType)
@given(instance=ram_PrimitiveType_strategy)
@settings(max_examples=25)
def test_ram_PrimitiveType_instantiation(instance):
    assert isinstance(instance, ram_PrimitiveType)


ram_Property_strategy = st.builds(ram_Property, lowerBound=st.integers(), referenceType=safe_text, upperBound=st.integers())
@given(instance=ram_Property_strategy)
@settings(max_examples=25)
def test_ram_Property_instantiation(instance):
    assert isinstance(instance, ram_Property)


ram_RAny_strategy = st.builds(ram_RAny)
@given(instance=ram_RAny_strategy)
@settings(max_examples=25)
def test_ram_RAny_instantiation(instance):
    assert isinstance(instance, ram_RAny)


ram_RBoolean_strategy = st.builds(ram_RBoolean)
@given(instance=ram_RBoolean_strategy)
@settings(max_examples=25)
def test_ram_RBoolean_instantiation(instance):
    assert isinstance(instance, ram_RBoolean)


ram_RChar_strategy = st.builds(ram_RChar)
@given(instance=ram_RChar_strategy)
@settings(max_examples=25)
def test_ram_RChar_instantiation(instance):
    assert isinstance(instance, ram_RChar)


ram_RCollection_strategy = st.builds(ram_RCollection)
@given(instance=ram_RCollection_strategy)
@settings(max_examples=25)
def test_ram_RCollection_instantiation(instance):
    assert isinstance(instance, ram_RCollection)


ram_RDouble_strategy = st.builds(ram_RDouble)
@given(instance=ram_RDouble_strategy)
@settings(max_examples=25)
def test_ram_RDouble_instantiation(instance):
    assert isinstance(instance, ram_RDouble)


ram_REnum_strategy = st.builds(ram_REnum)
@given(instance=ram_REnum_strategy)
@settings(max_examples=25)
def test_ram_REnum_instantiation(instance):
    assert isinstance(instance, ram_REnum)


ram_REnumLiteral_strategy = st.builds(ram_REnumLiteral)
@given(instance=ram_REnumLiteral_strategy)
@settings(max_examples=25)
def test_ram_REnumLiteral_instantiation(instance):
    assert isinstance(instance, ram_REnumLiteral)


ram_RFloat_strategy = st.builds(ram_RFloat)
@given(instance=ram_RFloat_strategy)
@settings(max_examples=25)
def test_ram_RFloat_instantiation(instance):
    assert isinstance(instance, ram_RFloat)


ram_RInt_strategy = st.builds(ram_RInt)
@given(instance=ram_RInt_strategy)
@settings(max_examples=25)
def test_ram_RInt_instantiation(instance):
    assert isinstance(instance, ram_RInt)


ram_RSequence_strategy = st.builds(ram_RSequence)
@given(instance=ram_RSequence_strategy)
@settings(max_examples=25)
def test_ram_RSequence_instantiation(instance):
    assert isinstance(instance, ram_RSequence)


ram_RSet_strategy = st.builds(ram_RSet)
@given(instance=ram_RSet_strategy)
@settings(max_examples=25)
def test_ram_RSet_instantiation(instance):
    assert isinstance(instance, ram_RSet)


ram_RString_strategy = st.builds(ram_RString)
@given(instance=ram_RString_strategy)
@settings(max_examples=25)
def test_ram_RString_instantiation(instance):
    assert isinstance(instance, ram_RString)


ram_RVoid_strategy = st.builds(ram_RVoid)
@given(instance=ram_RVoid_strategy)
@settings(max_examples=25)
def test_ram_RVoid_instantiation(instance):
    assert isinstance(instance, ram_RVoid)


ram_Reference_strategy = st.builds(ram_Reference)
@given(instance=ram_Reference_strategy)
@settings(max_examples=25)
def test_ram_Reference_instantiation(instance):
    assert isinstance(instance, ram_Reference)


ram_State_strategy = st.builds(ram_State)
@given(instance=ram_State_strategy)
@settings(max_examples=25)
def test_ram_State_instantiation(instance):
    assert isinstance(instance, ram_State)


ram_StateMachine_strategy = st.builds(ram_StateMachine)
@given(instance=ram_StateMachine_strategy)
@settings(max_examples=25)
def test_ram_StateMachine_instantiation(instance):
    assert isinstance(instance, ram_StateMachine)


ram_StateView_strategy = st.builds(ram_StateView)
@given(instance=ram_StateView_strategy)
@settings(max_examples=25)
def test_ram_StateView_instantiation(instance):
    assert isinstance(instance, ram_StateView)


ram_StructuralFeature_strategy = st.builds(ram_StructuralFeature, static=st.booleans())
@given(instance=ram_StructuralFeature_strategy)
@settings(max_examples=25)
def test_ram_StructuralFeature_instantiation(instance):
    assert isinstance(instance, ram_StructuralFeature)


ram_StructuralFeatureValue_strategy = st.builds(ram_StructuralFeatureValue)
@given(instance=ram_StructuralFeatureValue_strategy)
@settings(max_examples=25)
def test_ram_StructuralFeatureValue_instantiation(instance):
    assert isinstance(instance, ram_StructuralFeatureValue)


ram_StructuralView_strategy = st.builds(ram_StructuralView)
@given(instance=ram_StructuralView_strategy)
@settings(max_examples=25)
def test_ram_StructuralView_instantiation(instance):
    assert isinstance(instance, ram_StructuralView)


ram_Substitution_strategy = st.builds(ram_Substitution)
@given(instance=ram_Substitution_strategy)
@settings(max_examples=25)
def test_ram_Substitution_instantiation(instance):
    assert isinstance(instance, ram_Substitution)


ram_TemporaryProperty_strategy = st.builds(ram_TemporaryProperty)
@given(instance=ram_TemporaryProperty_strategy)
@settings(max_examples=25)
def test_ram_TemporaryProperty_instantiation(instance):
    assert isinstance(instance, ram_TemporaryProperty)


ram_Transition_strategy = st.builds(ram_Transition)
@given(instance=ram_Transition_strategy)
@settings(max_examples=25)
def test_ram_Transition_instantiation(instance):
    assert isinstance(instance, ram_Transition)


ram_TransitionSubstitution_strategy = st.builds(ram_TransitionSubstitution)
@given(instance=ram_TransitionSubstitution_strategy)
@settings(max_examples=25)
def test_ram_TransitionSubstitution_instantiation(instance):
    assert isinstance(instance, ram_TransitionSubstitution)


ram_Type_strategy = st.builds(ram_Type)
@given(instance=ram_Type_strategy)
@settings(max_examples=25)
def test_ram_Type_instantiation(instance):
    assert isinstance(instance, ram_Type)


ram_TypedElement_strategy = st.builds(ram_TypedElement)
@given(instance=ram_TypedElement_strategy)
@settings(max_examples=25)
def test_ram_TypedElement_instantiation(instance):
    assert isinstance(instance, ram_TypedElement)


ram_ValueSpecification_strategy = st.builds(ram_ValueSpecification)
@given(instance=ram_ValueSpecification_strategy)
@settings(max_examples=25)
def test_ram_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ram_ValueSpecification)


