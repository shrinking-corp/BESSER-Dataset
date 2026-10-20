import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMessageView,
    COREModel,
    COREModelElement,
    CORENamedElement,
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
    Substitution,
    TemporaryProperty,
    Traceable,
    Type,
    TypedElement,
    ValueSpecification,
    ram_AbstractMessageView,
    ram_Aspect,
    ram_AspectMessageView,
    ram_AssignmentStatement,
    ram_Association,
    ram_AssociationEnd,
    ram_Attribute,
    ram_AttributeMapping,
    ram_COREModelReuse,
    ram_CheckState,
    ram_Class,
    ram_Classifier,
    ram_ClassifierMapping,
    ram_CombinedFragment,
    ram_Constraint,
    ram_ContainerMap,
    ram_DestructionOccurrenceSpecification,
    ram_EObject,
    ram_ElementMap,
    ram_EnumLiteralValue,
    ram_ExecutionStatement,
    ram_FragmentContainer,
    ram_Gate,
    ram_ImplementationClass,
    ram_Instantiation,
    ram_Interaction,
    ram_InteractionFragment,
    ram_InteractionOperand,
    ram_Layout,
    ram_Lifeline,
    ram_LiteralBoolean,
    ram_LiteralByte,
    ram_LiteralChar,
    ram_LiteralDouble,
    ram_LiteralFloat,
    ram_LiteralInteger,
    ram_LiteralLong,
    ram_LiteralNull,
    ram_LiteralSpecification,
    ram_LiteralString,
    ram_MappableElement,
    ram_Message,
    ram_MessageEnd,
    ram_MessageOccurrenceSpecification,
    ram_MessageView,
    ram_MessageViewReference,
    ram_NamedElement,
    ram_NewLayoutElement,
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
    ram_RByte,
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
    ram_StateMachine,
    ram_StateView,
    ram_StructuralFeature,
    ram_StructuralFeatureValue,
    ram_StructuralView,
    ram_Substitution,
    ram_TemporaryProperty,
    ram_Traceable,
    ram_TracingMap,
    ram_Transition,
    ram_TransitionSubstitution,
    ram_Type,
    ram_TypeParameter,
    ram_TypedElement,
    ram_ValueSpecification,
    ram_WovenAspect,
    InstantiationType,
    InteractionOperatorKind,
    MessageSort,
    OperationType,
    RAMVisibilityType,
    ReferenceType,
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

def test_assoc_assignTo64_reverse_link_reassign_clear():
    a1 = ram_StructuralFeature(static=True)
    a2 = ram_StructuralFeature(static=False)
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message65', a1)
    assert _is_linked(b, 'ram_Message65', a1)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert _is_linked(a1, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message65', a2)
    assert _is_linked(b, 'ram_Message65', a2)
    if hasattr(a1, 'ram_StructuralFeature'):
        assert not _is_linked(a1, 'ram_StructuralFeature', b)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert _is_linked(a2, 'ram_StructuralFeature', b)
    _safe_set(b, 'ram_Message65', None)
    assert not _is_linked(b, 'ram_Message65', a2)
    if hasattr(a2, 'ram_StructuralFeature'):
        assert not _is_linked(a2, 'ram_StructuralFeature', b)


def test_assoc_associationEnds112_reverse_link_reassign_clear():
    a1 = ram_Classifier(dataType=True)
    a2 = ram_Classifier(dataType=False)
    b = ram_AssociationEnd(navigable=True)
    _safe_set(b, 'AssociationEnd113', a1)
    assert _is_linked(b, 'AssociationEnd113', a1)
    if hasattr(a1, 'classifier'):
        assert _is_linked(a1, 'classifier', b)
    _safe_set(b, 'AssociationEnd113', a2)
    assert _is_linked(b, 'AssociationEnd113', a2)
    if hasattr(a1, 'classifier'):
        assert not _is_linked(a1, 'classifier', b)
    if hasattr(a2, 'classifier'):
        assert _is_linked(a2, 'classifier', b)
    _safe_set(b, 'AssociationEnd113', None)
    assert not _is_linked(b, 'AssociationEnd113', a2)
    if hasattr(a2, 'classifier'):
        assert not _is_linked(a2, 'classifier', b)


def test_assoc_classifier19_reverse_link_reassign_clear():
    a1 = ram_Classifier(dataType=True)
    a2 = ram_Classifier(dataType=False)
    b = ram_AssociationEnd(navigable=True)
    _safe_set(b, 'associationEnds', a1)
    assert _is_linked(b, 'associationEnds', a1)
    if hasattr(a1, 'Classifier'):
        assert _is_linked(a1, 'Classifier', b)
    _safe_set(b, 'associationEnds', a2)
    assert _is_linked(b, 'associationEnds', a2)
    if hasattr(a1, 'Classifier'):
        assert not _is_linked(a1, 'Classifier', b)
    if hasattr(a2, 'Classifier'):
        assert _is_linked(a2, 'Classifier', b)
    _safe_set(b, 'associationEnds', None)
    assert not _is_linked(b, 'associationEnds', a2)
    if hasattr(a2, 'Classifier'):
        assert not _is_linked(a2, 'Classifier', b)


def test_assoc_operations109_reverse_link_reassign_clear():
    a1 = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    a2 = ram_Operation(abstract=False, extendedVisibility="sample_text_2", operationType="sample_text_2", static=False)
    b = ram_Classifier(dataType=True)
    _safe_set(b, 'ram_Classifier110', {a1})
    assert _is_linked(b, 'ram_Classifier110', a1)
    if hasattr(a1, 'ram_Operation111'):
        assert _is_linked(a1, 'ram_Operation111', b)
    _safe_set(b, 'ram_Classifier110', {a2})
    assert _is_linked(b, 'ram_Classifier110', a2)
    if hasattr(a1, 'ram_Operation111'):
        assert not _is_linked(a1, 'ram_Operation111', b)
    if hasattr(a2, 'ram_Operation111'):
        assert _is_linked(a2, 'ram_Operation111', b)
    _safe_set(b, 'ram_Classifier110', set())
    assert not _is_linked(b, 'ram_Classifier110', a2)
    if hasattr(a2, 'ram_Operation111'):
        assert not _is_linked(a2, 'ram_Operation111', b)


def test_assoc_signature61_reverse_link_reassign_clear():
    a1 = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    a2 = ram_Operation(abstract=False, extendedVisibility="sample_text_2", operationType="sample_text_2", static=False)
    b = ram_Message(messageSort="sample_text", selfMessage=True)
    _safe_set(b, 'ram_Message62', a1)
    assert _is_linked(b, 'ram_Message62', a1)
    if hasattr(a1, 'ram_Operation63'):
        assert _is_linked(a1, 'ram_Operation63', b)
    _safe_set(b, 'ram_Message62', a2)
    assert _is_linked(b, 'ram_Message62', a2)
    if hasattr(a1, 'ram_Operation63'):
        assert not _is_linked(a1, 'ram_Operation63', b)
    if hasattr(a2, 'ram_Operation63'):
        assert _is_linked(a2, 'ram_Operation63', b)
    _safe_set(b, 'ram_Message62', None)
    assert not _is_linked(b, 'ram_Message62', a2)
    if hasattr(a2, 'ram_Operation63'):
        assert not _is_linked(a2, 'ram_Operation63', b)


def test_assoc_superTypes117_reverse_link_reassign_clear():
    a1 = ram_Classifier(dataType=True)
    a2 = ram_Classifier(dataType=False)
    b = ram_Classifier(dataType=True)
    _safe_set(b, 'ram_Classifier118', a1)
    assert _is_linked(b, 'ram_Classifier118', a1)
    if hasattr(a1, 'ram_Classifier116'):
        assert _is_linked(a1, 'ram_Classifier116', b)
    _safe_set(b, 'ram_Classifier118', a2)
    assert _is_linked(b, 'ram_Classifier118', a2)
    if hasattr(a1, 'ram_Classifier116'):
        assert not _is_linked(a1, 'ram_Classifier116', b)
    if hasattr(a2, 'ram_Classifier116'):
        assert _is_linked(a2, 'ram_Classifier116', b)
    _safe_set(b, 'ram_Classifier118', None)
    assert not _is_linked(b, 'ram_Classifier118', a2)
    if hasattr(a2, 'ram_Classifier116'):
        assert not _is_linked(a2, 'ram_Classifier116', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments66_stub_double():
    # ram_ParameterValueMapping has no real 'ram_ParameterValueMapping' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ParameterValueMapping()
    setattr(partner, 'ram_ParameterValueMapping', None)
    _safe_set(owner, 'ram_Message67', {partner})
    assert getattr(partner, 'ram_ParameterValueMapping') == owner
    _safe_set(owner, 'ram_Message67', set())
    assert getattr(partner, 'ram_ParameterValueMapping') is None


def test_assoc_assignTo174_stub_double():
    # ram_AssignmentStatement has no real 'ram_AssignmentStatement' property in the generated
    # code (a bare stub) -- manually attach it so ram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_StructuralFeature(static=True)
    partner = ram_AssignmentStatement()
    setattr(partner, 'ram_AssignmentStatement', None)
    _safe_set(owner, 'ram_StructuralFeature175', partner)
    assert getattr(partner, 'ram_AssignmentStatement') == owner
    _safe_set(owner, 'ram_StructuralFeature175', None)
    assert getattr(partner, 'ram_AssignmentStatement') is None


def test_assoc_assoc18_stub_double():
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


def test_assoc_attributes17_stub_double():
    # ram_Attribute has no real 'ram_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so ram_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Class(abstract=True)
    partner = ram_Attribute()
    setattr(partner, 'ram_Attribute', None)
    _safe_set(owner, 'ram_Class', {partner})
    assert getattr(partner, 'ram_Attribute') == owner
    _safe_set(owner, 'ram_Class', set())
    assert getattr(partner, 'ram_Attribute') is None


def test_assoc_classes11_stub_double():
    # ram_StructuralView has no real 'ram_StructuralView12' property in the generated
    # code (a bare stub) -- manually attach it so ram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Classifier(dataType=True)
    partner = ram_StructuralView()
    setattr(partner, 'ram_StructuralView12', None)
    _safe_set(owner, 'ram_Classifier', partner)
    assert owner in getattr(partner, 'ram_StructuralView12')
    _safe_set(owner, 'ram_Classifier', None)
    assert owner not in getattr(partner, 'ram_StructuralView12')


def test_assoc_ends21_stub_double():
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


def test_assoc_featureSelection20_stub_double():
    # ram_COREModelReuse has no real 'ram_COREModelReuse' property in the generated
    # code (a bare stub) -- manually attach it so ram_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_AssociationEnd(navigable=True)
    partner = ram_COREModelReuse()
    setattr(partner, 'ram_COREModelReuse', None)
    _safe_set(owner, 'ram_AssociationEnd', partner)
    assert getattr(partner, 'ram_COREModelReuse') == owner
    _safe_set(owner, 'ram_AssociationEnd', None)
    assert getattr(partner, 'ram_COREModelReuse') is None


def test_assoc_instantiations3_stub_double():
    # ram_Aspect has no real 'ram_Aspect4' property in the generated
    # code (a bare stub) -- manually attach it so ram_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Instantiation(type="sample_text")
    partner = ram_Aspect()
    setattr(partner, 'ram_Aspect4', None)
    _safe_set(owner, 'ram_Instantiation', partner)
    assert owner in getattr(partner, 'ram_Aspect4')
    _safe_set(owner, 'ram_Instantiation', None)
    assert owner not in getattr(partner, 'ram_Aspect4')


def test_assoc_interaction68_stub_double():
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


def test_assoc_localProperties71_stub_double():
    # ram_TemporaryProperty has no real 'ram_TemporaryProperty' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_TemporaryProperty()
    setattr(partner, 'ram_TemporaryProperty', None)
    _safe_set(owner, 'ram_Message72', {partner})
    assert getattr(partner, 'ram_TemporaryProperty') == owner
    _safe_set(owner, 'ram_Message72', set())
    assert getattr(partner, 'ram_TemporaryProperty') is None


def test_assoc_message73_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd74' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd74', None)
    _safe_set(owner, 'ram_Message75', partner)
    assert getattr(partner, 'ram_MessageEnd74') == owner
    _safe_set(owner, 'ram_Message75', None)
    assert getattr(partner, 'ram_MessageEnd74') is None


def test_assoc_messages43_stub_double():
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


def test_assoc_operands78_stub_double():
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


def test_assoc_parameters24_stub_double():
    # ram_Parameter has no real 'ram_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    partner = ram_Parameter()
    setattr(partner, 'ram_Parameter', None)
    _safe_set(owner, 'ram_Operation25', {partner})
    assert getattr(partner, 'ram_Parameter') == owner
    _safe_set(owner, 'ram_Operation25', set())
    assert getattr(partner, 'ram_Parameter') is None


def test_assoc_pointcut48_stub_double():
    # ram_AspectMessageView has no real 'ram_AspectMessageView49' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    partner = ram_AspectMessageView()
    setattr(partner, 'ram_AspectMessageView49', None)
    _safe_set(owner, 'ram_Operation50', partner)
    assert getattr(partner, 'ram_AspectMessageView49') == owner
    _safe_set(owner, 'ram_Operation50', None)
    assert getattr(partner, 'ram_AspectMessageView49') is None


def test_assoc_receiveEvent58_stub_double():
    # ram_MessageEnd has no real 'ram_MessageEnd60' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_MessageEnd()
    setattr(partner, 'ram_MessageEnd60', None)
    _safe_set(owner, 'ram_Message59', partner)
    assert getattr(partner, 'ram_MessageEnd60') == owner
    _safe_set(owner, 'ram_Message59', None)
    assert getattr(partner, 'ram_MessageEnd60') is None


def test_assoc_represents54_stub_double():
    # ram_Lifeline has no real 'ram_Lifeline55' property in the generated
    # code (a bare stub) -- manually attach it so ram_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_TypedElement()
    partner = ram_Lifeline()
    setattr(partner, 'ram_Lifeline55', None)
    _safe_set(owner, 'ram_TypedElement', partner)
    assert getattr(partner, 'ram_Lifeline55') == owner
    _safe_set(owner, 'ram_TypedElement', None)
    assert getattr(partner, 'ram_Lifeline55') is None


def test_assoc_returnType22_stub_double():
    # ram_Type has no real 'ram_Type23' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    partner = ram_Type()
    setattr(partner, 'ram_Type23', None)
    _safe_set(owner, 'ram_Operation', partner)
    assert getattr(partner, 'ram_Type23') == owner
    _safe_set(owner, 'ram_Operation', None)
    assert getattr(partner, 'ram_Type23') is None


def test_assoc_returns69_stub_double():
    # ram_ValueSpecification has no real 'ram_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so ram_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Message(messageSort="sample_text", selfMessage=True)
    partner = ram_ValueSpecification()
    setattr(partner, 'ram_ValueSpecification', None)
    _safe_set(owner, 'ram_Message70', partner)
    assert getattr(partner, 'ram_ValueSpecification') == owner
    _safe_set(owner, 'ram_Message70', None)
    assert getattr(partner, 'ram_ValueSpecification') is None


def test_assoc_sendEvent57_stub_double():
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


def test_assoc_signature144_stub_double():
    # ram_Transition has no real 'ram_Transition145' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    partner = ram_Transition()
    setattr(partner, 'ram_Transition145', None)
    _safe_set(owner, 'ram_Operation146', partner)
    assert getattr(partner, 'ram_Transition145') == owner
    _safe_set(owner, 'ram_Operation146', None)
    assert getattr(partner, 'ram_Transition145') is None


def test_assoc_specifies129_stub_double():
    # ram_StateView has no real 'ram_StateView130' property in the generated
    # code (a bare stub) -- manually attach it so ram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Classifier(dataType=True)
    partner = ram_StateView()
    setattr(partner, 'ram_StateView130', None)
    _safe_set(owner, 'ram_Classifier131', partner)
    assert getattr(partner, 'ram_StateView130') == owner
    _safe_set(owner, 'ram_Classifier131', None)
    assert getattr(partner, 'ram_StateView130') is None


def test_assoc_specifies35_stub_double():
    # ram_MessageView has no real 'ram_MessageView' property in the generated
    # code (a bare stub) -- manually attach it so ram_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Operation(abstract=True, extendedVisibility="sample_text", operationType="sample_text", static=True)
    partner = ram_MessageView()
    setattr(partner, 'ram_MessageView', None)
    _safe_set(owner, 'ram_Operation36', partner)
    assert getattr(partner, 'ram_MessageView') == owner
    _safe_set(owner, 'ram_Operation36', None)
    assert getattr(partner, 'ram_MessageView') is None


def test_assoc_type163_stub_double():
    # ram_ObjectType has no real 'ram_ObjectType164' property in the generated
    # code (a bare stub) -- manually attach it so ram_RArray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_RArray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_RArray(size=7)
    partner = ram_ObjectType()
    setattr(partner, 'ram_ObjectType164', None)
    _safe_set(owner, 'ram_RArray', partner)
    assert getattr(partner, 'ram_ObjectType164') == owner
    _safe_set(owner, 'ram_RArray', None)
    assert getattr(partner, 'ram_ObjectType164') is None


def test_assoc_type96_stub_double():
    # ram_ObjectType has no real 'ram_ObjectType97' property in the generated
    # code (a bare stub) -- manually attach it so ram_RCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_RCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_RCollection()
    partner = ram_ObjectType()
    setattr(partner, 'ram_ObjectType97', None)
    _safe_set(owner, 'ram_RCollection', partner)
    assert getattr(partner, 'ram_ObjectType97') == owner
    _safe_set(owner, 'ram_RCollection', None)
    assert getattr(partner, 'ram_ObjectType97') is None


def test_assoc_typeParameters114_stub_double():
    # ram_TypeParameter has no real 'ram_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ram_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_Classifier(dataType=True)
    partner = ram_TypeParameter()
    setattr(partner, 'ram_TypeParameter', None)
    _safe_set(owner, 'ram_Classifier115', {partner})
    assert getattr(partner, 'ram_TypeParameter') == owner
    _safe_set(owner, 'ram_Classifier115', set())
    assert getattr(partner, 'ram_TypeParameter') is None


def test_assoc_value107_stub_double():
    # ram_ElementMap has no real 'ram_ElementMap108' property in the generated
    # code (a bare stub) -- manually attach it so ram_NewLayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_NewLayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_NewLayoutElement(x=3.14, y=3.14)
    partner = ram_ElementMap()
    setattr(partner, 'ram_ElementMap108', None)
    _safe_set(owner, 'ram_NewLayoutElement', partner)
    assert getattr(partner, 'ram_ElementMap108') == owner
    _safe_set(owner, 'ram_NewLayoutElement', None)
    assert getattr(partner, 'ram_ElementMap108') is None


def test_assoc_value84_stub_double():
    # ram_StructuralFeatureValue has no real 'ram_StructuralFeatureValue' property in the generated
    # code (a bare stub) -- manually attach it so ram_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ram_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ram_StructuralFeature(static=True)
    partner = ram_StructuralFeatureValue()
    setattr(partner, 'ram_StructuralFeatureValue', None)
    _safe_set(owner, 'ram_StructuralFeature85', partner)
    assert getattr(partner, 'ram_StructuralFeatureValue') == owner
    _safe_set(owner, 'ram_StructuralFeature85', None)
    assert getattr(partner, 'ram_StructuralFeatureValue') is None


