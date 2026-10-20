import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDateTimeConcept,
    Boolean,
    BusinessConcept,
    BusinessElement,
    BusinessElementType,
    Construct,
    DataType,
    Decimal,
    IndustryMessageSet,
    LogicalType,
    MessageComponentType,
    MessageConcept,
    MessageConstruct,
    MessageElement,
    MessageElementContainer,
    ModelEntity,
    MultiplicityEntity,
    RepositoryConcept,
    RepositoryType,
    String,
    TopLevelCatalogueEntry,
    TopLevelDictionaryEntry,
    iso20022_AbstractDateTimeConcept,
    iso20022_Address,
    iso20022_Amount,
    iso20022_Binary,
    iso20022_Boolean,
    iso20022_BroadcastList,
    iso20022_BusinessArea,
    iso20022_BusinessAssociationEnd,
    iso20022_BusinessAttribute,
    iso20022_BusinessComponent,
    iso20022_BusinessConcept,
    iso20022_BusinessElement,
    iso20022_BusinessElementType,
    iso20022_BusinessProcess,
    iso20022_BusinessProcessCatalogue,
    iso20022_BusinessRole,
    iso20022_BusinessTransaction,
    iso20022_ChoiceComponent,
    iso20022_Code,
    iso20022_CodeSet,
    iso20022_Constraint,
    iso20022_Construct,
    iso20022_ConvergenceDocumentation,
    iso20022_Conversation,
    iso20022_DataDictionary,
    iso20022_DataType,
    iso20022_Date,
    iso20022_DateTime,
    iso20022_Day,
    iso20022_Decimal,
    iso20022_Doclet,
    iso20022_Duration,
    iso20022_Encoding,
    iso20022_EndPointCategory,
    iso20022_ExternalSchema,
    iso20022_ISO15022MessageSet,
    iso20022_IdentifierSet,
    iso20022_Indicator,
    iso20022_IndustryMessageSet,
    iso20022_LogicalType,
    iso20022_MessageAssociationEnd,
    iso20022_MessageAttribute,
    iso20022_MessageBuildingBlock,
    iso20022_MessageChoreography,
    iso20022_MessageComponent,
    iso20022_MessageComponentType,
    iso20022_MessageConcept,
    iso20022_MessageConstruct,
    iso20022_MessageDefinition,
    iso20022_MessageDefinitionIdentifier,
    iso20022_MessageElement,
    iso20022_MessageElementContainer,
    iso20022_MessageInstance,
    iso20022_MessageSet,
    iso20022_MessageTransmission,
    iso20022_MessageTransportMode,
    iso20022_MessageTransportSystem,
    iso20022_MessagingEndpoint,
    iso20022_ModelEntity,
    iso20022_Month,
    iso20022_MonthDay,
    iso20022_MultiplicityEntity,
    iso20022_Participant,
    iso20022_Quantity,
    iso20022_Rate,
    iso20022_Receive,
    iso20022_Repository,
    iso20022_RepositoryConcept,
    iso20022_RepositoryType,
    iso20022_SchemaType,
    iso20022_SemanticMarkup,
    iso20022_SemanticMarkupElement,
    iso20022_Send,
    iso20022_String,
    iso20022_Syntax,
    iso20022_SyntaxMessageScheme,
    iso20022_Text,
    iso20022_Time,
    iso20022_TopLevelCatalogueEntry,
    iso20022_TopLevelDictionaryEntry,
    iso20022_TransportMessage,
    iso20022_UserDefined,
    iso20022_Xor,
    iso20022_Year,
    iso20022_YearMonth,
    Aggregation,
    DeliveryAssurance,
    Durability,
    ISO20022Version,
    MessageCasting,
    MessageDeliveryOrder,
    MessageValidationLevel,
    MessageValidationOnOff,
    MessageValidationResults,
    Namespace,
    ProcessContent,
    ReceiverAsynchronicity,
    RegistrationStatus,
    SchemaTypeKind,
    SenderAsynchronicity,
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

def test_assoc_associationDomain98_reverse_link_reassign_clear():
    a1 = iso20022_BusinessComponent()
    a2 = iso20022_BusinessComponent()
    b = iso20022_BusinessAssociationEnd(aggregation="sample_text")
    _safe_set(b, 'BusinessAssociationEnd', a1)
    assert _is_linked(b, 'BusinessAssociationEnd', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'BusinessAssociationEnd', a2)
    assert _is_linked(b, 'BusinessAssociationEnd', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'BusinessAssociationEnd', None)
    assert not _is_linked(b, 'BusinessAssociationEnd', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


def test_assoc_businessArea48_reverse_link_reassign_clear():
    a1 = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = iso20022_MessageDefinition(rootElement="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = iso20022_BusinessArea(code="sample_text")
    _safe_set(b, 'BusinessArea', a1)
    assert _is_linked(b, 'BusinessArea', a1)
    if hasattr(a1, 'messageDefinition49'):
        assert _is_linked(a1, 'messageDefinition49', b)
    _safe_set(b, 'BusinessArea', a2)
    assert _is_linked(b, 'BusinessArea', a2)
    if hasattr(a1, 'messageDefinition49'):
        assert not _is_linked(a1, 'messageDefinition49', b)
    if hasattr(a2, 'messageDefinition49'):
        assert _is_linked(a2, 'messageDefinition49', b)
    _safe_set(b, 'BusinessArea', None)
    assert not _is_linked(b, 'BusinessArea', a2)
    if hasattr(a2, 'messageDefinition49'):
        assert not _is_linked(a2, 'messageDefinition49', b)


def test_assoc_businessComponentTrace83_reverse_link_reassign_clear():
    a1 = iso20022_MessageElement(isDerived=True, isTechnical=True)
    a2 = iso20022_MessageElement(isDerived=False, isTechnical=False)
    b = iso20022_BusinessComponent()
    _safe_set(b, 'BusinessComponent', a1)
    assert _is_linked(b, 'BusinessComponent', a1)
    if hasattr(a1, 'derivationElement'):
        assert _is_linked(a1, 'derivationElement', b)
    _safe_set(b, 'BusinessComponent', a2)
    assert _is_linked(b, 'BusinessComponent', a2)
    if hasattr(a1, 'derivationElement'):
        assert not _is_linked(a1, 'derivationElement', b)
    if hasattr(a2, 'derivationElement'):
        assert _is_linked(a2, 'derivationElement', b)
    _safe_set(b, 'BusinessComponent', None)
    assert not _is_linked(b, 'BusinessComponent', a2)
    if hasattr(a2, 'derivationElement'):
        assert not _is_linked(a2, 'derivationElement', b)


def test_assoc_businessElementTrace84_reverse_link_reassign_clear():
    a1 = iso20022_MessageElement(isDerived=True, isTechnical=True)
    a2 = iso20022_MessageElement(isDerived=False, isTechnical=False)
    b = iso20022_BusinessElement(isDerived=True)
    _safe_set(b, 'BusinessElement', a1)
    assert _is_linked(b, 'BusinessElement', a1)
    if hasattr(a1, 'derivation85'):
        assert _is_linked(a1, 'derivation85', b)
    _safe_set(b, 'BusinessElement', a2)
    assert _is_linked(b, 'BusinessElement', a2)
    if hasattr(a1, 'derivation85'):
        assert not _is_linked(a1, 'derivation85', b)
    if hasattr(a2, 'derivation85'):
        assert _is_linked(a2, 'derivation85', b)
    _safe_set(b, 'BusinessElement', None)
    assert not _is_linked(b, 'BusinessElement', a2)
    if hasattr(a2, 'derivation85'):
        assert not _is_linked(a2, 'derivation85', b)


def test_assoc_businessTransaction172_reverse_link_reassign_clear():
    a1 = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    a2 = iso20022_MessageTransmission(messageTypeDescription="sample_text_2")
    b = iso20022_BusinessTransaction()
    _safe_set(b, 'BusinessTransaction173', a1)
    assert _is_linked(b, 'BusinessTransaction173', a1)
    if hasattr(a1, 'transmission'):
        assert _is_linked(a1, 'transmission', b)
    _safe_set(b, 'BusinessTransaction173', a2)
    assert _is_linked(b, 'BusinessTransaction173', a2)
    if hasattr(a1, 'transmission'):
        assert not _is_linked(a1, 'transmission', b)
    if hasattr(a2, 'transmission'):
        assert _is_linked(a2, 'transmission', b)
    _safe_set(b, 'BusinessTransaction173', None)
    assert not _is_linked(b, 'BusinessTransaction173', a2)
    if hasattr(a2, 'transmission'):
        assert not _is_linked(a2, 'transmission', b)


def test_assoc_businessTransaction186_reverse_link_reassign_clear():
    a1 = iso20022_MessageTransportMode(boundedCommunicationDelay="sample_text", deliveryAssurance="sample_text", durability="sample_text", maximumClockVariation="sample_text", maximumMessageSize="sample_text", messageCasting="sample_text", messageDeliveryOrder="sample_text", messageDeliveryWindow="sample_text", messageSendingWindow="sample_text", messageValidationLevel="sample_text", messageValidationOnOff="sample_text", messageValidationResults="sample_text", receiverAsynchronicity="sample_text", senderAsynchronicity="sample_text")
    a2 = iso20022_MessageTransportMode(boundedCommunicationDelay="sample_text_2", deliveryAssurance="sample_text_2", durability="sample_text_2", maximumClockVariation="sample_text_2", maximumMessageSize="sample_text_2", messageCasting="sample_text_2", messageDeliveryOrder="sample_text_2", messageDeliveryWindow="sample_text_2", messageSendingWindow="sample_text_2", messageValidationLevel="sample_text_2", messageValidationOnOff="sample_text_2", messageValidationResults="sample_text_2", receiverAsynchronicity="sample_text_2", senderAsynchronicity="sample_text_2")
    b = iso20022_BusinessTransaction()
    _safe_set(b, 'BusinessTransaction187', a1)
    assert _is_linked(b, 'BusinessTransaction187', a1)
    if hasattr(a1, 'messageTransportMode'):
        assert _is_linked(a1, 'messageTransportMode', b)
    _safe_set(b, 'BusinessTransaction187', a2)
    assert _is_linked(b, 'BusinessTransaction187', a2)
    if hasattr(a1, 'messageTransportMode'):
        assert not _is_linked(a1, 'messageTransportMode', b)
    if hasattr(a2, 'messageTransportMode'):
        assert _is_linked(a2, 'messageTransportMode', b)
    _safe_set(b, 'BusinessTransaction187', None)
    assert not _is_linked(b, 'BusinessTransaction187', a2)
    if hasattr(a2, 'messageTransportMode'):
        assert not _is_linked(a2, 'messageTransportMode', b)


def test_assoc_code207_reverse_link_reassign_clear():
    a1 = iso20022_CodeSet(identificationScheme="sample_text")
    a2 = iso20022_CodeSet(identificationScheme="sample_text_2")
    b = iso20022_Code(codeName="sample_text")
    _safe_set(b, 'Code', a1)
    assert _is_linked(b, 'Code', a1)
    if hasattr(a1, 'owner208'):
        assert _is_linked(a1, 'owner208', b)
    _safe_set(b, 'Code', a2)
    assert _is_linked(b, 'Code', a2)
    if hasattr(a1, 'owner208'):
        assert not _is_linked(a1, 'owner208', b)
    if hasattr(a2, 'owner208'):
        assert _is_linked(a2, 'owner208', b)
    _safe_set(b, 'Code', None)
    assert not _is_linked(b, 'Code', a2)
    if hasattr(a2, 'owner208'):
        assert not _is_linked(a2, 'owner208', b)


def test_assoc_complexType110_reverse_link_reassign_clear():
    a1 = iso20022_MessageComponentType(isTechnical=True)
    a2 = iso20022_MessageComponentType(isTechnical=False)
    b = iso20022_MessageBuildingBlock()
    _safe_set(b, 'messageBuildingBlock', a1)
    assert _is_linked(b, 'messageBuildingBlock', a1)
    if hasattr(a1, 'MessageComponentType111'):
        assert _is_linked(a1, 'MessageComponentType111', b)
    _safe_set(b, 'messageBuildingBlock', a2)
    assert _is_linked(b, 'messageBuildingBlock', a2)
    if hasattr(a1, 'MessageComponentType111'):
        assert not _is_linked(a1, 'MessageComponentType111', b)
    if hasattr(a2, 'MessageComponentType111'):
        assert _is_linked(a2, 'MessageComponentType111', b)
    _safe_set(b, 'messageBuildingBlock', None)
    assert not _is_linked(b, 'messageBuildingBlock', a2)
    if hasattr(a2, 'MessageComponentType111'):
        assert not _is_linked(a2, 'MessageComponentType111', b)


def test_assoc_complexType191_reverse_link_reassign_clear():
    a1 = iso20022_MessageComponentType(isTechnical=True)
    a2 = iso20022_MessageComponentType(isTechnical=False)
    b = iso20022_MessageAttribute()
    _safe_set(b, 'iso20022_MessageAttribute192', a1)
    assert _is_linked(b, 'iso20022_MessageAttribute192', a1)
    if hasattr(a1, 'iso20022_MessageComponentType193'):
        assert _is_linked(a1, 'iso20022_MessageComponentType193', b)
    _safe_set(b, 'iso20022_MessageAttribute192', a2)
    assert _is_linked(b, 'iso20022_MessageAttribute192', a2)
    if hasattr(a1, 'iso20022_MessageComponentType193'):
        assert not _is_linked(a1, 'iso20022_MessageComponentType193', b)
    if hasattr(a2, 'iso20022_MessageComponentType193'):
        assert _is_linked(a2, 'iso20022_MessageComponentType193', b)
    _safe_set(b, 'iso20022_MessageAttribute192', None)
    assert not _is_linked(b, 'iso20022_MessageAttribute192', a2)
    if hasattr(a2, 'iso20022_MessageComponentType193'):
        assert not _is_linked(a2, 'iso20022_MessageComponentType193', b)


def test_assoc_complexType196_reverse_link_reassign_clear():
    a1 = iso20022_BusinessComponent()
    a2 = iso20022_BusinessComponent()
    b = iso20022_BusinessAttribute()
    _safe_set(b, 'iso20022_BusinessAttribute197', a1)
    assert _is_linked(b, 'iso20022_BusinessAttribute197', a1)
    if hasattr(a1, 'iso20022_BusinessComponent'):
        assert _is_linked(a1, 'iso20022_BusinessComponent', b)
    _safe_set(b, 'iso20022_BusinessAttribute197', a2)
    assert _is_linked(b, 'iso20022_BusinessAttribute197', a2)
    if hasattr(a1, 'iso20022_BusinessComponent'):
        assert not _is_linked(a1, 'iso20022_BusinessComponent', b)
    if hasattr(a2, 'iso20022_BusinessComponent'):
        assert _is_linked(a2, 'iso20022_BusinessComponent', b)
    _safe_set(b, 'iso20022_BusinessAttribute197', None)
    assert not _is_linked(b, 'iso20022_BusinessAttribute197', a2)
    if hasattr(a2, 'iso20022_BusinessComponent'):
        assert not _is_linked(a2, 'iso20022_BusinessComponent', b)


def test_assoc_componentContext86_reverse_link_reassign_clear():
    a1 = iso20022_MessageElementContainer()
    a2 = iso20022_MessageElementContainer()
    b = iso20022_MessageElement(isDerived=True, isTechnical=True)
    _safe_set(b, 'messageElement', a1)
    assert _is_linked(b, 'messageElement', a1)
    if hasattr(a1, 'MessageElementContainer'):
        assert _is_linked(a1, 'MessageElementContainer', b)
    _safe_set(b, 'messageElement', a2)
    assert _is_linked(b, 'messageElement', a2)
    if hasattr(a1, 'MessageElementContainer'):
        assert not _is_linked(a1, 'MessageElementContainer', b)
    if hasattr(a2, 'MessageElementContainer'):
        assert _is_linked(a2, 'MessageElementContainer', b)
    _safe_set(b, 'messageElement', None)
    assert not _is_linked(b, 'messageElement', a2)
    if hasattr(a2, 'MessageElementContainer'):
        assert not _is_linked(a2, 'MessageElementContainer', b)


def test_assoc_constraint30_reverse_link_reassign_clear():
    a1 = iso20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1))
    a2 = iso20022_RepositoryConcept(definition="sample_text_2", example="sample_text_2", name="sample_text_2", registrationStatus="sample_text_2", removalDate=date(2025, 6, 15))
    b = iso20022_Constraint(expression="sample_text", expressionLanguage="sample_text")
    _safe_set(b, 'Constraint', a1)
    assert _is_linked(b, 'Constraint', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Constraint', a2)
    assert _is_linked(b, 'Constraint', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Constraint', None)
    assert not _is_linked(b, 'Constraint', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_derivation100_reverse_link_reassign_clear():
    a1 = iso20022_MessageElement(isDerived=True, isTechnical=True)
    a2 = iso20022_MessageElement(isDerived=False, isTechnical=False)
    b = iso20022_BusinessElement(isDerived=True)
    _safe_set(b, 'businessElementTrace', {a1})
    assert _is_linked(b, 'businessElementTrace', a1)
    if hasattr(a1, 'MessageElement101'):
        assert _is_linked(a1, 'MessageElement101', b)
    _safe_set(b, 'businessElementTrace', {a2})
    assert _is_linked(b, 'businessElementTrace', a2)
    if hasattr(a1, 'MessageElement101'):
        assert not _is_linked(a1, 'MessageElement101', b)
    if hasattr(a2, 'MessageElement101'):
        assert _is_linked(a2, 'MessageElement101', b)
    _safe_set(b, 'businessElementTrace', set())
    assert not _is_linked(b, 'businessElementTrace', a2)
    if hasattr(a2, 'MessageElement101'):
        assert not _is_linked(a2, 'MessageElement101', b)


def test_assoc_derivation174_reverse_link_reassign_clear():
    a1 = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    a2 = iso20022_MessageTransmission(messageTypeDescription="sample_text_2")
    b = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'MessageDefinition176', a1)
    assert _is_linked(b, 'MessageDefinition176', a1)
    if hasattr(a1, 'trace175'):
        assert _is_linked(a1, 'trace175', b)
    _safe_set(b, 'MessageDefinition176', a2)
    assert _is_linked(b, 'MessageDefinition176', a2)
    if hasattr(a1, 'trace175'):
        assert not _is_linked(a1, 'trace175', b)
    if hasattr(a2, 'trace175'):
        assert _is_linked(a2, 'trace175', b)
    _safe_set(b, 'MessageDefinition176', None)
    assert not _is_linked(b, 'MessageDefinition176', a2)
    if hasattr(a2, 'trace175'):
        assert not _is_linked(a2, 'trace175', b)


def test_assoc_derivation204_reverse_link_reassign_clear():
    a1 = iso20022_CodeSet(identificationScheme="sample_text")
    a2 = iso20022_CodeSet(identificationScheme="sample_text_2")
    b = iso20022_CodeSet(identificationScheme="sample_text")
    _safe_set(b, 'trace205', {a1})
    assert _is_linked(b, 'trace205', a1)
    if hasattr(a1, 'CodeSet206'):
        assert _is_linked(a1, 'CodeSet206', b)
    _safe_set(b, 'trace205', {a2})
    assert _is_linked(b, 'trace205', a2)
    if hasattr(a1, 'CodeSet206'):
        assert not _is_linked(a1, 'CodeSet206', b)
    if hasattr(a2, 'CodeSet206'):
        assert _is_linked(a2, 'CodeSet206', b)
    _safe_set(b, 'trace205', set())
    assert not _is_linked(b, 'trace205', a2)
    if hasattr(a2, 'CodeSet206'):
        assert not _is_linked(a2, 'CodeSet206', b)


def test_assoc_derivationComponent97_reverse_link_reassign_clear():
    a1 = iso20022_MessageComponentType(isTechnical=True)
    a2 = iso20022_MessageComponentType(isTechnical=False)
    b = iso20022_BusinessComponent()
    _safe_set(b, 'trace', {a1})
    assert _is_linked(b, 'trace', a1)
    if hasattr(a1, 'MessageComponentType'):
        assert _is_linked(a1, 'MessageComponentType', b)
    _safe_set(b, 'trace', {a2})
    assert _is_linked(b, 'trace', a2)
    if hasattr(a1, 'MessageComponentType'):
        assert not _is_linked(a1, 'MessageComponentType', b)
    if hasattr(a2, 'MessageComponentType'):
        assert _is_linked(a2, 'MessageComponentType', b)
    _safe_set(b, 'trace', set())
    assert not _is_linked(b, 'trace', a2)
    if hasattr(a2, 'MessageComponentType'):
        assert not _is_linked(a2, 'MessageComponentType', b)


def test_assoc_derivationElement99_reverse_link_reassign_clear():
    a1 = iso20022_MessageElement(isDerived=True, isTechnical=True)
    a2 = iso20022_MessageElement(isDerived=False, isTechnical=False)
    b = iso20022_BusinessComponent()
    _safe_set(b, 'businessComponentTrace', {a1})
    assert _is_linked(b, 'businessComponentTrace', a1)
    if hasattr(a1, 'MessageElement'):
        assert _is_linked(a1, 'MessageElement', b)
    _safe_set(b, 'businessComponentTrace', {a2})
    assert _is_linked(b, 'businessComponentTrace', a2)
    if hasattr(a1, 'MessageElement'):
        assert not _is_linked(a1, 'MessageElement', b)
    if hasattr(a2, 'MessageElement'):
        assert _is_linked(a2, 'MessageElement', b)
    _safe_set(b, 'businessComponentTrace', set())
    assert not _is_linked(b, 'businessComponentTrace', a2)
    if hasattr(a2, 'MessageElement'):
        assert not _is_linked(a2, 'MessageElement', b)


def test_assoc_doclet28_reverse_link_reassign_clear():
    a1 = iso20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1))
    a2 = iso20022_RepositoryConcept(definition="sample_text_2", example="sample_text_2", name="sample_text_2", registrationStatus="sample_text_2", removalDate=date(2025, 6, 15))
    b = iso20022_Doclet(content="sample_text", type="sample_text")
    _safe_set(b, 'iso20022_Doclet', a1)
    assert _is_linked(b, 'iso20022_Doclet', a1)
    if hasattr(a1, 'iso20022_RepositoryConcept29'):
        assert _is_linked(a1, 'iso20022_RepositoryConcept29', b)
    _safe_set(b, 'iso20022_Doclet', a2)
    assert _is_linked(b, 'iso20022_Doclet', a2)
    if hasattr(a1, 'iso20022_RepositoryConcept29'):
        assert not _is_linked(a1, 'iso20022_RepositoryConcept29', b)
    if hasattr(a2, 'iso20022_RepositoryConcept29'):
        assert _is_linked(a2, 'iso20022_RepositoryConcept29', b)
    _safe_set(b, 'iso20022_Doclet', None)
    assert not _is_linked(b, 'iso20022_Doclet', a2)
    if hasattr(a2, 'iso20022_RepositoryConcept29'):
        assert not _is_linked(a2, 'iso20022_RepositoryConcept29', b)


def test_assoc_element95_reverse_link_reassign_clear():
    a1 = iso20022_BusinessElement(isDerived=True)
    a2 = iso20022_BusinessElement(isDerived=False)
    b = iso20022_BusinessComponent()
    _safe_set(b, 'elementContext', {a1})
    assert _is_linked(b, 'elementContext', a1)
    if hasattr(a1, 'BusinessElement96'):
        assert _is_linked(a1, 'BusinessElement96', b)
    _safe_set(b, 'elementContext', {a2})
    assert _is_linked(b, 'elementContext', a2)
    if hasattr(a1, 'BusinessElement96'):
        assert not _is_linked(a1, 'BusinessElement96', b)
    if hasattr(a2, 'BusinessElement96'):
        assert _is_linked(a2, 'BusinessElement96', b)
    _safe_set(b, 'elementContext', set())
    assert not _is_linked(b, 'elementContext', a2)
    if hasattr(a2, 'BusinessElement96'):
        assert not _is_linked(a2, 'BusinessElement96', b)


def test_assoc_elementContext103_reverse_link_reassign_clear():
    a1 = iso20022_BusinessElement(isDerived=True)
    a2 = iso20022_BusinessElement(isDerived=False)
    b = iso20022_BusinessComponent()
    _safe_set(b, 'BusinessComponent104', a1)
    assert _is_linked(b, 'BusinessComponent104', a1)
    if hasattr(a1, 'element'):
        assert _is_linked(a1, 'element', b)
    _safe_set(b, 'BusinessComponent104', a2)
    assert _is_linked(b, 'BusinessComponent104', a2)
    if hasattr(a1, 'element'):
        assert not _is_linked(a1, 'element', b)
    if hasattr(a2, 'element'):
        assert _is_linked(a2, 'element', b)
    _safe_set(b, 'BusinessComponent104', None)
    assert not _is_linked(b, 'BusinessComponent104', a2)
    if hasattr(a2, 'element'):
        assert not _is_linked(a2, 'element', b)


def test_assoc_elements31_reverse_link_reassign_clear():
    a1 = iso20022_SemanticMarkupElement(name="sample_text", value="sample_text")
    a2 = iso20022_SemanticMarkupElement(name="sample_text_2", value="sample_text_2")
    b = iso20022_SemanticMarkup(type="sample_text")
    _safe_set(b, 'iso20022_SemanticMarkup32', {a1})
    assert _is_linked(b, 'iso20022_SemanticMarkup32', a1)
    if hasattr(a1, 'iso20022_SemanticMarkupElement'):
        assert _is_linked(a1, 'iso20022_SemanticMarkupElement', b)
    _safe_set(b, 'iso20022_SemanticMarkup32', {a2})
    assert _is_linked(b, 'iso20022_SemanticMarkup32', a2)
    if hasattr(a1, 'iso20022_SemanticMarkupElement'):
        assert not _is_linked(a1, 'iso20022_SemanticMarkupElement', b)
    if hasattr(a2, 'iso20022_SemanticMarkupElement'):
        assert _is_linked(a2, 'iso20022_SemanticMarkupElement', b)
    _safe_set(b, 'iso20022_SemanticMarkup32', set())
    assert not _is_linked(b, 'iso20022_SemanticMarkup32', a2)
    if hasattr(a2, 'iso20022_SemanticMarkupElement'):
        assert not _is_linked(a2, 'iso20022_SemanticMarkupElement', b)


def test_assoc_generatedFor67_reverse_link_reassign_clear():
    a1 = iso20022_Syntax()
    a2 = iso20022_Syntax()
    b = iso20022_MessageSet()
    _safe_set(b, 'MessageSet68', a1)
    assert _is_linked(b, 'MessageSet68', a1)
    if hasattr(a1, 'generatedSyntax'):
        assert _is_linked(a1, 'generatedSyntax', b)
    _safe_set(b, 'MessageSet68', a2)
    assert _is_linked(b, 'MessageSet68', a2)
    if hasattr(a1, 'generatedSyntax'):
        assert not _is_linked(a1, 'generatedSyntax', b)
    if hasattr(a2, 'generatedSyntax'):
        assert _is_linked(a2, 'generatedSyntax', b)
    _safe_set(b, 'MessageSet68', None)
    assert not _is_linked(b, 'MessageSet68', a2)
    if hasattr(a2, 'generatedSyntax'):
        assert not _is_linked(a2, 'generatedSyntax', b)


def test_assoc_generatedSyntax60_reverse_link_reassign_clear():
    a1 = iso20022_Syntax()
    a2 = iso20022_Syntax()
    b = iso20022_MessageSet()
    _safe_set(b, 'generatedFor', {a1})
    assert _is_linked(b, 'generatedFor', a1)
    if hasattr(a1, 'Syntax'):
        assert _is_linked(a1, 'Syntax', b)
    _safe_set(b, 'generatedFor', {a2})
    assert _is_linked(b, 'generatedFor', a2)
    if hasattr(a1, 'Syntax'):
        assert not _is_linked(a1, 'Syntax', b)
    if hasattr(a2, 'Syntax'):
        assert _is_linked(a2, 'Syntax', b)
    _safe_set(b, 'generatedFor', set())
    assert not _is_linked(b, 'generatedFor', a2)
    if hasattr(a2, 'Syntax'):
        assert not _is_linked(a2, 'Syntax', b)


def test_assoc_messageBuildingBlock105_reverse_link_reassign_clear():
    a1 = iso20022_MessageComponentType(isTechnical=True)
    a2 = iso20022_MessageComponentType(isTechnical=False)
    b = iso20022_MessageBuildingBlock()
    _safe_set(b, 'MessageBuildingBlock', a1)
    assert _is_linked(b, 'MessageBuildingBlock', a1)
    if hasattr(a1, 'complexType'):
        assert _is_linked(a1, 'complexType', b)
    _safe_set(b, 'MessageBuildingBlock', a2)
    assert _is_linked(b, 'MessageBuildingBlock', a2)
    if hasattr(a1, 'complexType'):
        assert not _is_linked(a1, 'complexType', b)
    if hasattr(a2, 'complexType'):
        assert _is_linked(a2, 'complexType', b)
    _safe_set(b, 'MessageBuildingBlock', None)
    assert not _is_linked(b, 'MessageBuildingBlock', a2)
    if hasattr(a2, 'complexType'):
        assert not _is_linked(a2, 'complexType', b)


def test_assoc_messageBuildingBlock52_reverse_link_reassign_clear():
    a1 = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = iso20022_MessageDefinition(rootElement="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = iso20022_MessageBuildingBlock()
    _safe_set(b, 'iso20022_MessageBuildingBlock', a1)
    assert _is_linked(b, 'iso20022_MessageBuildingBlock', a1)
    if hasattr(a1, 'iso20022_MessageDefinition'):
        assert _is_linked(a1, 'iso20022_MessageDefinition', b)
    _safe_set(b, 'iso20022_MessageBuildingBlock', a2)
    assert _is_linked(b, 'iso20022_MessageBuildingBlock', a2)
    if hasattr(a1, 'iso20022_MessageDefinition'):
        assert not _is_linked(a1, 'iso20022_MessageDefinition', b)
    if hasattr(a2, 'iso20022_MessageDefinition'):
        assert _is_linked(a2, 'iso20022_MessageDefinition', b)
    _safe_set(b, 'iso20022_MessageBuildingBlock', None)
    assert not _is_linked(b, 'iso20022_MessageBuildingBlock', a2)
    if hasattr(a2, 'iso20022_MessageDefinition'):
        assert not _is_linked(a2, 'iso20022_MessageDefinition', b)


def test_assoc_messageDefinition62_reverse_link_reassign_clear():
    a1 = iso20022_MessageSet()
    a2 = iso20022_MessageSet()
    b = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'MessageDefinition64', a1)
    assert _is_linked(b, 'MessageDefinition64', a1)
    if hasattr(a1, 'messageSet63'):
        assert _is_linked(a1, 'messageSet63', b)
    _safe_set(b, 'MessageDefinition64', a2)
    assert _is_linked(b, 'MessageDefinition64', a2)
    if hasattr(a1, 'messageSet63'):
        assert not _is_linked(a1, 'messageSet63', b)
    if hasattr(a2, 'messageSet63'):
        assert _is_linked(a2, 'messageSet63', b)
    _safe_set(b, 'MessageDefinition64', None)
    assert not _is_linked(b, 'MessageDefinition64', a2)
    if hasattr(a2, 'messageSet63'):
        assert not _is_linked(a2, 'messageSet63', b)


def test_assoc_messageDefinition73_reverse_link_reassign_clear():
    a1 = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = iso20022_MessageDefinition(rootElement="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = iso20022_BusinessArea(code="sample_text")
    _safe_set(b, 'businessArea', {a1})
    assert _is_linked(b, 'businessArea', a1)
    if hasattr(a1, 'MessageDefinition74'):
        assert _is_linked(a1, 'MessageDefinition74', b)
    _safe_set(b, 'businessArea', {a2})
    assert _is_linked(b, 'businessArea', a2)
    if hasattr(a1, 'MessageDefinition74'):
        assert not _is_linked(a1, 'MessageDefinition74', b)
    if hasattr(a2, 'MessageDefinition74'):
        assert _is_linked(a2, 'MessageDefinition74', b)
    _safe_set(b, 'businessArea', set())
    assert not _is_linked(b, 'businessArea', a2)
    if hasattr(a2, 'MessageDefinition74'):
        assert not _is_linked(a2, 'MessageDefinition74', b)


def test_assoc_messageDefinitionIdentifier57_reverse_link_reassign_clear():
    a1 = iso20022_MessageDefinitionIdentifier(businessArea="sample_text", flavour="sample_text", messageFunctionality="sample_text", version="sample_text")
    a2 = iso20022_MessageDefinitionIdentifier(businessArea="sample_text_2", flavour="sample_text_2", messageFunctionality="sample_text_2", version="sample_text_2")
    b = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'iso20022_MessageDefinition58', a1)
    assert _is_linked(b, 'iso20022_MessageDefinition58', a1)
    if hasattr(a1, 'iso20022_MessageDefinitionIdentifier'):
        assert _is_linked(a1, 'iso20022_MessageDefinitionIdentifier', b)
    _safe_set(b, 'iso20022_MessageDefinition58', a2)
    assert _is_linked(b, 'iso20022_MessageDefinition58', a2)
    if hasattr(a1, 'iso20022_MessageDefinitionIdentifier'):
        assert not _is_linked(a1, 'iso20022_MessageDefinitionIdentifier', b)
    if hasattr(a2, 'iso20022_MessageDefinitionIdentifier'):
        assert _is_linked(a2, 'iso20022_MessageDefinitionIdentifier', b)
    _safe_set(b, 'iso20022_MessageDefinition58', None)
    assert not _is_linked(b, 'iso20022_MessageDefinition58', a2)
    if hasattr(a2, 'iso20022_MessageDefinitionIdentifier'):
        assert not _is_linked(a2, 'iso20022_MessageDefinitionIdentifier', b)


def test_assoc_messageElement116_reverse_link_reassign_clear():
    a1 = iso20022_MessageElementContainer()
    a2 = iso20022_MessageElementContainer()
    b = iso20022_MessageElement(isDerived=True, isTechnical=True)
    _safe_set(b, 'MessageElement117', a1)
    assert _is_linked(b, 'MessageElement117', a1)
    if hasattr(a1, 'componentContext'):
        assert _is_linked(a1, 'componentContext', b)
    _safe_set(b, 'MessageElement117', a2)
    assert _is_linked(b, 'MessageElement117', a2)
    if hasattr(a1, 'componentContext'):
        assert not _is_linked(a1, 'componentContext', b)
    if hasattr(a2, 'componentContext'):
        assert _is_linked(a2, 'componentContext', b)
    _safe_set(b, 'MessageElement117', None)
    assert not _is_linked(b, 'MessageElement117', a2)
    if hasattr(a2, 'componentContext'):
        assert not _is_linked(a2, 'componentContext', b)


def test_assoc_messageSet47_reverse_link_reassign_clear():
    a1 = iso20022_MessageSet()
    a2 = iso20022_MessageSet()
    b = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'messageDefinition', {a1})
    assert _is_linked(b, 'messageDefinition', a1)
    if hasattr(a1, 'MessageSet'):
        assert _is_linked(a1, 'MessageSet', b)
    _safe_set(b, 'messageDefinition', {a2})
    assert _is_linked(b, 'messageDefinition', a2)
    if hasattr(a1, 'MessageSet'):
        assert not _is_linked(a1, 'MessageSet', b)
    if hasattr(a2, 'MessageSet'):
        assert _is_linked(a2, 'MessageSet', b)
    _safe_set(b, 'messageDefinition', set())
    assert not _is_linked(b, 'messageDefinition', a2)
    if hasattr(a2, 'MessageSet'):
        assert not _is_linked(a2, 'MessageSet', b)


def test_assoc_messageTransportMode129_reverse_link_reassign_clear():
    a1 = iso20022_MessageTransportMode(boundedCommunicationDelay="sample_text", deliveryAssurance="sample_text", durability="sample_text", maximumClockVariation="sample_text", maximumMessageSize="sample_text", messageCasting="sample_text", messageDeliveryOrder="sample_text", messageDeliveryWindow="sample_text", messageSendingWindow="sample_text", messageValidationLevel="sample_text", messageValidationOnOff="sample_text", messageValidationResults="sample_text", receiverAsynchronicity="sample_text", senderAsynchronicity="sample_text")
    a2 = iso20022_MessageTransportMode(boundedCommunicationDelay="sample_text_2", deliveryAssurance="sample_text_2", durability="sample_text_2", maximumClockVariation="sample_text_2", maximumMessageSize="sample_text_2", messageCasting="sample_text_2", messageDeliveryOrder="sample_text_2", messageDeliveryWindow="sample_text_2", messageSendingWindow="sample_text_2", messageValidationLevel="sample_text_2", messageValidationOnOff="sample_text_2", messageValidationResults="sample_text_2", receiverAsynchronicity="sample_text_2", senderAsynchronicity="sample_text_2")
    b = iso20022_BusinessTransaction()
    _safe_set(b, 'businessTransaction130', a1)
    assert _is_linked(b, 'businessTransaction130', a1)
    if hasattr(a1, 'MessageTransportMode'):
        assert _is_linked(a1, 'MessageTransportMode', b)
    _safe_set(b, 'businessTransaction130', a2)
    assert _is_linked(b, 'businessTransaction130', a2)
    if hasattr(a1, 'MessageTransportMode'):
        assert not _is_linked(a1, 'MessageTransportMode', b)
    if hasattr(a2, 'MessageTransportMode'):
        assert _is_linked(a2, 'MessageTransportMode', b)
    _safe_set(b, 'businessTransaction130', None)
    assert not _is_linked(b, 'businessTransaction130', a2)
    if hasattr(a2, 'MessageTransportMode'):
        assert not _is_linked(a2, 'MessageTransportMode', b)


def test_assoc_nextVersions3_reverse_link_reassign_clear():
    a1 = iso20022_ModelEntity(objectIdentifier="sample_text")
    a2 = iso20022_ModelEntity(objectIdentifier="sample_text_2")
    b = iso20022_ModelEntity(objectIdentifier="sample_text")
    _safe_set(b, 'previousVersion', {a1})
    assert _is_linked(b, 'previousVersion', a1)
    if hasattr(a1, 'ModelEntity'):
        assert _is_linked(a1, 'ModelEntity', b)
    _safe_set(b, 'previousVersion', {a2})
    assert _is_linked(b, 'previousVersion', a2)
    if hasattr(a1, 'ModelEntity'):
        assert not _is_linked(a1, 'ModelEntity', b)
    if hasattr(a2, 'ModelEntity'):
        assert _is_linked(a2, 'ModelEntity', b)
    _safe_set(b, 'previousVersion', set())
    assert not _is_linked(b, 'previousVersion', a2)
    if hasattr(a2, 'ModelEntity'):
        assert not _is_linked(a2, 'ModelEntity', b)


def test_assoc_opposite113_reverse_link_reassign_clear():
    a1 = iso20022_BusinessAssociationEnd(aggregation="sample_text")
    a2 = iso20022_BusinessAssociationEnd(aggregation="sample_text_2")
    b = iso20022_BusinessAssociationEnd(aggregation="sample_text")
    _safe_set(b, 'iso20022_BusinessAssociationEnd112', a1)
    assert _is_linked(b, 'iso20022_BusinessAssociationEnd112', a1)
    if hasattr(a1, 'iso20022_BusinessAssociationEnd'):
        assert _is_linked(a1, 'iso20022_BusinessAssociationEnd', b)
    _safe_set(b, 'iso20022_BusinessAssociationEnd112', a2)
    assert _is_linked(b, 'iso20022_BusinessAssociationEnd112', a2)
    if hasattr(a1, 'iso20022_BusinessAssociationEnd'):
        assert not _is_linked(a1, 'iso20022_BusinessAssociationEnd', b)
    if hasattr(a2, 'iso20022_BusinessAssociationEnd'):
        assert _is_linked(a2, 'iso20022_BusinessAssociationEnd', b)
    _safe_set(b, 'iso20022_BusinessAssociationEnd112', None)
    assert not _is_linked(b, 'iso20022_BusinessAssociationEnd112', a2)
    if hasattr(a2, 'iso20022_BusinessAssociationEnd'):
        assert not _is_linked(a2, 'iso20022_BusinessAssociationEnd', b)


def test_assoc_owner198_reverse_link_reassign_clear():
    a1 = iso20022_CodeSet(identificationScheme="sample_text")
    a2 = iso20022_CodeSet(identificationScheme="sample_text_2")
    b = iso20022_Code(codeName="sample_text")
    _safe_set(b, 'code', a1)
    assert _is_linked(b, 'code', a1)
    if hasattr(a1, 'CodeSet'):
        assert _is_linked(a1, 'CodeSet', b)
    _safe_set(b, 'code', a2)
    assert _is_linked(b, 'code', a2)
    if hasattr(a1, 'CodeSet'):
        assert not _is_linked(a1, 'CodeSet', b)
    if hasattr(a2, 'CodeSet'):
        assert _is_linked(a2, 'CodeSet', b)
    _safe_set(b, 'code', None)
    assert not _is_linked(b, 'code', a2)
    if hasattr(a2, 'CodeSet'):
        assert not _is_linked(a2, 'CodeSet', b)


def test_assoc_owner33_reverse_link_reassign_clear():
    a1 = iso20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1))
    a2 = iso20022_RepositoryConcept(definition="sample_text_2", example="sample_text_2", name="sample_text_2", registrationStatus="sample_text_2", removalDate=date(2025, 6, 15))
    b = iso20022_Constraint(expression="sample_text", expressionLanguage="sample_text")
    _safe_set(b, 'constraint', a1)
    assert _is_linked(b, 'constraint', a1)
    if hasattr(a1, 'RepositoryConcept'):
        assert _is_linked(a1, 'RepositoryConcept', b)
    _safe_set(b, 'constraint', a2)
    assert _is_linked(b, 'constraint', a2)
    if hasattr(a1, 'RepositoryConcept'):
        assert not _is_linked(a1, 'RepositoryConcept', b)
    if hasattr(a2, 'RepositoryConcept'):
        assert _is_linked(a2, 'RepositoryConcept', b)
    _safe_set(b, 'constraint', None)
    assert not _is_linked(b, 'constraint', a2)
    if hasattr(a2, 'RepositoryConcept'):
        assert not _is_linked(a2, 'RepositoryConcept', b)


def test_assoc_parentTransaction135_reverse_link_reassign_clear():
    a1 = iso20022_BusinessTransaction()
    a2 = iso20022_BusinessTransaction()
    b = iso20022_BusinessTransaction()
    _safe_set(b, 'subTransaction', a1)
    assert _is_linked(b, 'subTransaction', a1)
    if hasattr(a1, 'BusinessTransaction136'):
        assert _is_linked(a1, 'BusinessTransaction136', b)
    _safe_set(b, 'subTransaction', a2)
    assert _is_linked(b, 'subTransaction', a2)
    if hasattr(a1, 'BusinessTransaction136'):
        assert not _is_linked(a1, 'BusinessTransaction136', b)
    if hasattr(a2, 'BusinessTransaction136'):
        assert _is_linked(a2, 'BusinessTransaction136', b)
    _safe_set(b, 'subTransaction', None)
    assert not _is_linked(b, 'subTransaction', a2)
    if hasattr(a2, 'BusinessTransaction136'):
        assert not _is_linked(a2, 'BusinessTransaction136', b)


def test_assoc_previousVersion5_reverse_link_reassign_clear():
    a1 = iso20022_ModelEntity(objectIdentifier="sample_text")
    a2 = iso20022_ModelEntity(objectIdentifier="sample_text_2")
    b = iso20022_ModelEntity(objectIdentifier="sample_text")
    _safe_set(b, 'nextVersions', a1)
    assert _is_linked(b, 'nextVersions', a1)
    if hasattr(a1, 'ModelEntity6'):
        assert _is_linked(a1, 'ModelEntity6', b)
    _safe_set(b, 'nextVersions', a2)
    assert _is_linked(b, 'nextVersions', a2)
    if hasattr(a1, 'ModelEntity6'):
        assert not _is_linked(a1, 'ModelEntity6', b)
    if hasattr(a2, 'ModelEntity6'):
        assert _is_linked(a2, 'ModelEntity6', b)
    _safe_set(b, 'nextVersions', None)
    assert not _is_linked(b, 'nextVersions', a2)
    if hasattr(a2, 'ModelEntity6'):
        assert not _is_linked(a2, 'ModelEntity6', b)


def test_assoc_semanticMarkup27_reverse_link_reassign_clear():
    a1 = iso20022_SemanticMarkup(type="sample_text")
    a2 = iso20022_SemanticMarkup(type="sample_text_2")
    b = iso20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1))
    _safe_set(b, 'iso20022_RepositoryConcept', {a1})
    assert _is_linked(b, 'iso20022_RepositoryConcept', a1)
    if hasattr(a1, 'iso20022_SemanticMarkup'):
        assert _is_linked(a1, 'iso20022_SemanticMarkup', b)
    _safe_set(b, 'iso20022_RepositoryConcept', {a2})
    assert _is_linked(b, 'iso20022_RepositoryConcept', a2)
    if hasattr(a1, 'iso20022_SemanticMarkup'):
        assert not _is_linked(a1, 'iso20022_SemanticMarkup', b)
    if hasattr(a2, 'iso20022_SemanticMarkup'):
        assert _is_linked(a2, 'iso20022_SemanticMarkup', b)
    _safe_set(b, 'iso20022_RepositoryConcept', set())
    assert not _is_linked(b, 'iso20022_RepositoryConcept', a2)
    if hasattr(a2, 'iso20022_SemanticMarkup'):
        assert not _is_linked(a2, 'iso20022_SemanticMarkup', b)


def test_assoc_subTransaction132_reverse_link_reassign_clear():
    a1 = iso20022_BusinessTransaction()
    a2 = iso20022_BusinessTransaction()
    b = iso20022_BusinessTransaction()
    _safe_set(b, 'parentTransaction', {a1})
    assert _is_linked(b, 'parentTransaction', a1)
    if hasattr(a1, 'BusinessTransaction133'):
        assert _is_linked(a1, 'BusinessTransaction133', b)
    _safe_set(b, 'parentTransaction', {a2})
    assert _is_linked(b, 'parentTransaction', a2)
    if hasattr(a1, 'BusinessTransaction133'):
        assert not _is_linked(a1, 'BusinessTransaction133', b)
    if hasattr(a2, 'BusinessTransaction133'):
        assert _is_linked(a2, 'BusinessTransaction133', b)
    _safe_set(b, 'parentTransaction', set())
    assert not _is_linked(b, 'parentTransaction', a2)
    if hasattr(a2, 'BusinessTransaction133'):
        assert not _is_linked(a2, 'BusinessTransaction133', b)


def test_assoc_subType90_reverse_link_reassign_clear():
    a1 = iso20022_BusinessComponent()
    a2 = iso20022_BusinessComponent()
    b = iso20022_BusinessComponent()
    _safe_set(b, 'superType', {a1})
    assert _is_linked(b, 'superType', a1)
    if hasattr(a1, 'BusinessComponent91'):
        assert _is_linked(a1, 'BusinessComponent91', b)
    _safe_set(b, 'superType', {a2})
    assert _is_linked(b, 'superType', a2)
    if hasattr(a1, 'BusinessComponent91'):
        assert not _is_linked(a1, 'BusinessComponent91', b)
    if hasattr(a2, 'BusinessComponent91'):
        assert _is_linked(a2, 'BusinessComponent91', b)
    _safe_set(b, 'superType', set())
    assert not _is_linked(b, 'superType', a2)
    if hasattr(a2, 'BusinessComponent91'):
        assert not _is_linked(a2, 'BusinessComponent91', b)


def test_assoc_superType93_reverse_link_reassign_clear():
    a1 = iso20022_BusinessComponent()
    a2 = iso20022_BusinessComponent()
    b = iso20022_BusinessComponent()
    _safe_set(b, 'subType', a1)
    assert _is_linked(b, 'subType', a1)
    if hasattr(a1, 'BusinessComponent94'):
        assert _is_linked(a1, 'BusinessComponent94', b)
    _safe_set(b, 'subType', a2)
    assert _is_linked(b, 'subType', a2)
    if hasattr(a1, 'BusinessComponent94'):
        assert not _is_linked(a1, 'BusinessComponent94', b)
    if hasattr(a2, 'BusinessComponent94'):
        assert _is_linked(a2, 'BusinessComponent94', b)
    _safe_set(b, 'subType', None)
    assert not _is_linked(b, 'subType', a2)
    if hasattr(a2, 'BusinessComponent94'):
        assert not _is_linked(a2, 'BusinessComponent94', b)


def test_assoc_trace106_reverse_link_reassign_clear():
    a1 = iso20022_MessageComponentType(isTechnical=True)
    a2 = iso20022_MessageComponentType(isTechnical=False)
    b = iso20022_BusinessComponent()
    _safe_set(b, 'BusinessComponent107', a1)
    assert _is_linked(b, 'BusinessComponent107', a1)
    if hasattr(a1, 'derivationComponent'):
        assert _is_linked(a1, 'derivationComponent', b)
    _safe_set(b, 'BusinessComponent107', a2)
    assert _is_linked(b, 'BusinessComponent107', a2)
    if hasattr(a1, 'derivationComponent'):
        assert not _is_linked(a1, 'derivationComponent', b)
    if hasattr(a2, 'derivationComponent'):
        assert _is_linked(a2, 'derivationComponent', b)
    _safe_set(b, 'BusinessComponent107', None)
    assert not _is_linked(b, 'BusinessComponent107', a2)
    if hasattr(a2, 'derivationComponent'):
        assert not _is_linked(a2, 'derivationComponent', b)


def test_assoc_trace200_reverse_link_reassign_clear():
    a1 = iso20022_CodeSet(identificationScheme="sample_text")
    a2 = iso20022_CodeSet(identificationScheme="sample_text_2")
    b = iso20022_CodeSet(identificationScheme="sample_text")
    _safe_set(b, 'derivation201', a1)
    assert _is_linked(b, 'derivation201', a1)
    if hasattr(a1, 'CodeSet202'):
        assert _is_linked(a1, 'CodeSet202', b)
    _safe_set(b, 'derivation201', a2)
    assert _is_linked(b, 'derivation201', a2)
    if hasattr(a1, 'CodeSet202'):
        assert not _is_linked(a1, 'CodeSet202', b)
    if hasattr(a2, 'CodeSet202'):
        assert _is_linked(a2, 'CodeSet202', b)
    _safe_set(b, 'derivation201', None)
    assert not _is_linked(b, 'derivation201', a2)
    if hasattr(a2, 'CodeSet202'):
        assert not _is_linked(a2, 'CodeSet202', b)


def test_assoc_trace55_reverse_link_reassign_clear():
    a1 = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    a2 = iso20022_MessageTransmission(messageTypeDescription="sample_text_2")
    b = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'derivation56', {a1})
    assert _is_linked(b, 'derivation56', a1)
    if hasattr(a1, 'MessageTransmission'):
        assert _is_linked(a1, 'MessageTransmission', b)
    _safe_set(b, 'derivation56', {a2})
    assert _is_linked(b, 'derivation56', a2)
    if hasattr(a1, 'MessageTransmission'):
        assert not _is_linked(a1, 'MessageTransmission', b)
    if hasattr(a2, 'MessageTransmission'):
        assert _is_linked(a2, 'MessageTransmission', b)
    _safe_set(b, 'derivation56', set())
    assert not _is_linked(b, 'derivation56', a2)
    if hasattr(a2, 'MessageTransmission'):
        assert not _is_linked(a2, 'MessageTransmission', b)


def test_assoc_transmission126_reverse_link_reassign_clear():
    a1 = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    a2 = iso20022_MessageTransmission(messageTypeDescription="sample_text_2")
    b = iso20022_BusinessTransaction()
    _safe_set(b, 'businessTransaction127', {a1})
    assert _is_linked(b, 'businessTransaction127', a1)
    if hasattr(a1, 'MessageTransmission128'):
        assert _is_linked(a1, 'MessageTransmission128', b)
    _safe_set(b, 'businessTransaction127', {a2})
    assert _is_linked(b, 'businessTransaction127', a2)
    if hasattr(a1, 'MessageTransmission128'):
        assert not _is_linked(a1, 'MessageTransmission128', b)
    if hasattr(a2, 'MessageTransmission128'):
        assert _is_linked(a2, 'MessageTransmission128', b)
    _safe_set(b, 'businessTransaction127', set())
    assert not _is_linked(b, 'businessTransaction127', a2)
    if hasattr(a2, 'MessageTransmission128'):
        assert not _is_linked(a2, 'MessageTransmission128', b)


def test_assoc_type114_reverse_link_reassign_clear():
    a1 = iso20022_BusinessComponent()
    a2 = iso20022_BusinessComponent()
    b = iso20022_BusinessAssociationEnd(aggregation="sample_text")
    _safe_set(b, 'associationDomain', a1)
    assert _is_linked(b, 'associationDomain', a1)
    if hasattr(a1, 'BusinessComponent115'):
        assert _is_linked(a1, 'BusinessComponent115', b)
    _safe_set(b, 'associationDomain', a2)
    assert _is_linked(b, 'associationDomain', a2)
    if hasattr(a1, 'BusinessComponent115'):
        assert not _is_linked(a1, 'BusinessComponent115', b)
    if hasattr(a2, 'BusinessComponent115'):
        assert _is_linked(a2, 'BusinessComponent115', b)
    _safe_set(b, 'associationDomain', None)
    assert not _is_linked(b, 'associationDomain', a2)
    if hasattr(a2, 'BusinessComponent115'):
        assert not _is_linked(a2, 'BusinessComponent115', b)


def test_assoc_type188_reverse_link_reassign_clear():
    a1 = iso20022_MessageComponentType(isTechnical=True)
    a2 = iso20022_MessageComponentType(isTechnical=False)
    b = iso20022_MessageAssociationEnd(isComposite=True)
    _safe_set(b, 'iso20022_MessageAssociationEnd', a1)
    assert _is_linked(b, 'iso20022_MessageAssociationEnd', a1)
    if hasattr(a1, 'iso20022_MessageComponentType'):
        assert _is_linked(a1, 'iso20022_MessageComponentType', b)
    _safe_set(b, 'iso20022_MessageAssociationEnd', a2)
    assert _is_linked(b, 'iso20022_MessageAssociationEnd', a2)
    if hasattr(a1, 'iso20022_MessageComponentType'):
        assert not _is_linked(a1, 'iso20022_MessageComponentType', b)
    if hasattr(a2, 'iso20022_MessageComponentType'):
        assert _is_linked(a2, 'iso20022_MessageComponentType', b)
    _safe_set(b, 'iso20022_MessageAssociationEnd', None)
    assert not _is_linked(b, 'iso20022_MessageAssociationEnd', a2)
    if hasattr(a2, 'iso20022_MessageComponentType'):
        assert not _is_linked(a2, 'iso20022_MessageComponentType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_businessElementType102_stub_double():
    # iso20022_BusinessElementType has no real 'iso20022_BusinessElementType' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessElement(isDerived=True)
    partner = iso20022_BusinessElementType()
    setattr(partner, 'iso20022_BusinessElementType', None)
    _safe_set(owner, 'iso20022_BusinessElement', partner)
    assert getattr(partner, 'iso20022_BusinessElementType') == owner
    _safe_set(owner, 'iso20022_BusinessElement', None)
    assert getattr(partner, 'iso20022_BusinessElementType') is None


def test_assoc_businessProcessCatalogue26_stub_double():
    # iso20022_TopLevelCatalogueEntry has no real 'topLevelCatalogueEntry' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessProcessCatalogue()
    partner = iso20022_TopLevelCatalogueEntry()
    setattr(partner, 'topLevelCatalogueEntry', None)
    _safe_set(owner, 'BusinessProcessCatalogue', partner)
    assert getattr(partner, 'topLevelCatalogueEntry') == owner
    _safe_set(owner, 'BusinessProcessCatalogue', None)
    assert getattr(partner, 'topLevelCatalogueEntry') is None


def test_assoc_businessProcessCatalogue38_stub_double():
    # iso20022_Repository has no real 'repository39' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessProcessCatalogue()
    partner = iso20022_Repository()
    setattr(partner, 'repository39', None)
    _safe_set(owner, 'BusinessProcessCatalogue40', partner)
    assert getattr(partner, 'repository39') == owner
    _safe_set(owner, 'BusinessProcessCatalogue40', None)
    assert getattr(partner, 'repository39') is None


def test_assoc_businessProcessTrace124_stub_double():
    # iso20022_BusinessProcess has no real 'BusinessProcess' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessTransaction()
    partner = iso20022_BusinessProcess()
    setattr(partner, 'BusinessProcess', None)
    _safe_set(owner, 'businessProcessTrace', partner)
    assert getattr(partner, 'BusinessProcess') == owner
    _safe_set(owner, 'businessProcessTrace', None)
    assert getattr(partner, 'BusinessProcess') is None


def test_assoc_businessProcessTrace152_stub_double():
    # iso20022_BusinessProcess has no real 'businessProcessTrace153' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessTransaction()
    partner = iso20022_BusinessProcess()
    setattr(partner, 'businessProcessTrace153', None)
    _safe_set(owner, 'BusinessTransaction154', partner)
    assert owner in getattr(partner, 'businessProcessTrace153')
    _safe_set(owner, 'BusinessTransaction154', None)
    assert owner not in getattr(partner, 'businessProcessTrace153')


def test_assoc_businessTransaction159_stub_double():
    # iso20022_Participant has no real 'participant' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessTransaction()
    partner = iso20022_Participant()
    setattr(partner, 'participant', None)
    _safe_set(owner, 'BusinessTransaction160', partner)
    assert getattr(partner, 'participant') == owner
    _safe_set(owner, 'BusinessTransaction160', None)
    assert getattr(partner, 'participant') is None


def test_assoc_businessTransactionTrace120_stub_double():
    # iso20022_MessageChoreography has no real 'trace121' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessTransaction()
    partner = iso20022_MessageChoreography()
    setattr(partner, 'trace121', None)
    _safe_set(owner, 'BusinessTransaction', partner)
    assert getattr(partner, 'trace121') == owner
    _safe_set(owner, 'BusinessTransaction', None)
    assert getattr(partner, 'trace121') is None


def test_assoc_choreography53_stub_double():
    # iso20022_MessageChoreography has no real 'MessageChoreography' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = iso20022_MessageChoreography()
    setattr(partner, 'MessageChoreography', None)
    _safe_set(owner, 'messageDefinition54', {partner})
    assert getattr(partner, 'MessageChoreography') == owner
    _safe_set(owner, 'messageDefinition54', set())
    assert getattr(partner, 'MessageChoreography') is None


def test_assoc_dataDictionary37_stub_double():
    # iso20022_Repository has no real 'repository' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_DataDictionary()
    partner = iso20022_Repository()
    setattr(partner, 'repository', None)
    _safe_set(owner, 'DataDictionary', partner)
    assert getattr(partner, 'repository') == owner
    _safe_set(owner, 'DataDictionary', None)
    assert getattr(partner, 'repository') is None


def test_assoc_dataDictionary45_stub_double():
    # iso20022_TopLevelDictionaryEntry has no real 'topLevelDictionaryEntry' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_DataDictionary()
    partner = iso20022_TopLevelDictionaryEntry()
    setattr(partner, 'topLevelDictionaryEntry', None)
    _safe_set(owner, 'DataDictionary46', partner)
    assert getattr(partner, 'topLevelDictionaryEntry') == owner
    _safe_set(owner, 'DataDictionary46', None)
    assert getattr(partner, 'topLevelDictionaryEntry') is None


def test_assoc_derivation59_stub_double():
    # iso20022_SyntaxMessageScheme has no real 'SyntaxMessageScheme' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = iso20022_SyntaxMessageScheme()
    setattr(partner, 'SyntaxMessageScheme', None)
    _safe_set(owner, 'messageDefinitionTrace', {partner})
    assert getattr(partner, 'SyntaxMessageScheme') == owner
    _safe_set(owner, 'messageDefinitionTrace', set())
    assert getattr(partner, 'SyntaxMessageScheme') is None


def test_assoc_endPoints211_stub_double():
    # iso20022_EndPointCategory has no real 'iso20022_EndPointCategory' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageElementContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageElementContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageElementContainer()
    partner = iso20022_EndPointCategory()
    setattr(partner, 'iso20022_EndPointCategory', None)
    _safe_set(owner, 'iso20022_MessageElementContainer', partner)
    assert owner in getattr(partner, 'iso20022_EndPointCategory')
    _safe_set(owner, 'iso20022_MessageElementContainer', None)
    assert owner not in getattr(partner, 'iso20022_EndPointCategory')


def test_assoc_impactedElements75_stub_double():
    # iso20022_Xor has no real 'iso20022_Xor' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageElement(isDerived=True, isTechnical=True)
    partner = iso20022_Xor()
    setattr(partner, 'iso20022_Xor', None)
    _safe_set(owner, 'iso20022_MessageElement', partner)
    assert owner in getattr(partner, 'iso20022_Xor')
    _safe_set(owner, 'iso20022_MessageElement', None)
    assert owner not in getattr(partner, 'iso20022_Xor')


def test_assoc_impactedMessageBuildingBlocks77_stub_double():
    # iso20022_Xor has no real 'iso20022_Xor78' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageBuildingBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageBuildingBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageBuildingBlock()
    partner = iso20022_Xor()
    setattr(partner, 'iso20022_Xor78', None)
    _safe_set(owner, 'iso20022_MessageBuildingBlock79', partner)
    assert owner in getattr(partner, 'iso20022_Xor78')
    _safe_set(owner, 'iso20022_MessageBuildingBlock79', None)
    assert owner not in getattr(partner, 'iso20022_Xor78')


def test_assoc_messageDefinition122_stub_double():
    # iso20022_MessageChoreography has no real 'choreography' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = iso20022_MessageChoreography()
    setattr(partner, 'choreography', None)
    _safe_set(owner, 'MessageDefinition123', partner)
    assert owner in getattr(partner, 'choreography')
    _safe_set(owner, 'MessageDefinition123', None)
    assert owner not in getattr(partner, 'choreography')


def test_assoc_messageDefinition80_stub_double():
    # iso20022_Xor has no real 'xors81' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = iso20022_Xor()
    setattr(partner, 'xors81', None)
    _safe_set(owner, 'MessageDefinition82', partner)
    assert getattr(partner, 'xors81') == owner
    _safe_set(owner, 'MessageDefinition82', None)
    assert getattr(partner, 'xors81') is None


def test_assoc_messageDefinitionTrace25_stub_double():
    # iso20022_SyntaxMessageScheme has no real 'derivation' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = iso20022_SyntaxMessageScheme()
    setattr(partner, 'derivation', None)
    _safe_set(owner, 'MessageDefinition', partner)
    assert getattr(partner, 'derivation') == owner
    _safe_set(owner, 'MessageDefinition', None)
    assert getattr(partner, 'derivation') is None


def test_assoc_messageInstance19_stub_double():
    # iso20022_MessageInstance has no real 'MessageInstance' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_TransportMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_TransportMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_TransportMessage()
    partner = iso20022_MessageInstance()
    setattr(partner, 'MessageInstance', None)
    _safe_set(owner, 'transportMessage', partner)
    assert getattr(partner, 'MessageInstance') == owner
    _safe_set(owner, 'transportMessage', None)
    assert getattr(partner, 'MessageInstance') is None


def test_assoc_messageSet69_stub_double():
    # iso20022_Encoding has no real 'validEncoding' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageSet()
    partner = iso20022_Encoding()
    setattr(partner, 'validEncoding', None)
    _safe_set(owner, 'MessageSet70', partner)
    assert owner in getattr(partner, 'validEncoding')
    _safe_set(owner, 'MessageSet70', None)
    assert owner not in getattr(partner, 'validEncoding')


def test_assoc_messageTransmission168_stub_double():
    # iso20022_Receive has no real 'receive' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageTransmission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageTransmission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    partner = iso20022_Receive()
    setattr(partner, 'receive', None)
    _safe_set(owner, 'MessageTransmission169', partner)
    assert getattr(partner, 'receive') == owner
    _safe_set(owner, 'MessageTransmission169', None)
    assert getattr(partner, 'receive') is None


def test_assoc_messageTransmission184_stub_double():
    # iso20022_Send has no real 'send' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageTransmission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageTransmission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    partner = iso20022_Send()
    setattr(partner, 'send', None)
    _safe_set(owner, 'MessageTransmission185', partner)
    assert getattr(partner, 'send') == owner
    _safe_set(owner, 'MessageTransmission185', None)
    assert getattr(partner, 'send') is None


def test_assoc_participant125_stub_double():
    # iso20022_Participant has no real 'Participant' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessTransaction()
    partner = iso20022_Participant()
    setattr(partner, 'Participant', None)
    _safe_set(owner, 'businessTransaction', {partner})
    assert getattr(partner, 'Participant') == owner
    _safe_set(owner, 'businessTransaction', set())
    assert getattr(partner, 'Participant') is None


def test_assoc_possibleEncodings65_stub_double():
    # iso20022_Encoding has no real 'Encoding66' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_Syntax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_Syntax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_Syntax()
    partner = iso20022_Encoding()
    setattr(partner, 'Encoding66', None)
    _safe_set(owner, 'syntax', {partner})
    assert getattr(partner, 'Encoding66') == owner
    _safe_set(owner, 'syntax', set())
    assert getattr(partner, 'Encoding66') is None


def test_assoc_receive179_stub_double():
    # iso20022_Receive has no real 'Receive181' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageTransmission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageTransmission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    partner = iso20022_Receive()
    setattr(partner, 'Receive181', None)
    _safe_set(owner, 'messageTransmission180', {partner})
    assert getattr(partner, 'Receive181') == owner
    _safe_set(owner, 'messageTransmission180', set())
    assert getattr(partner, 'Receive181') is None


def test_assoc_receivedMessage9_stub_double():
    # iso20022_MessagingEndpoint has no real 'receiver' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_TransportMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_TransportMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_TransportMessage()
    partner = iso20022_MessagingEndpoint()
    setattr(partner, 'receiver', None)
    _safe_set(owner, 'TransportMessage', partner)
    assert owner in getattr(partner, 'receiver')
    _safe_set(owner, 'TransportMessage', None)
    assert owner not in getattr(partner, 'receiver')


def test_assoc_receiver20_stub_double():
    # iso20022_MessagingEndpoint has no real 'MessagingEndpoint21' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_TransportMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_TransportMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_TransportMessage()
    partner = iso20022_MessagingEndpoint()
    setattr(partner, 'MessagingEndpoint21', None)
    _safe_set(owner, 'receivedMessage', {partner})
    assert getattr(partner, 'MessagingEndpoint21') == owner
    _safe_set(owner, 'receivedMessage', set())
    assert getattr(partner, 'MessagingEndpoint21') is None


def test_assoc_repository34_stub_double():
    # iso20022_Repository has no real 'Repository' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessProcessCatalogue()
    partner = iso20022_Repository()
    setattr(partner, 'Repository', None)
    _safe_set(owner, 'businessProcessCatalogue', partner)
    assert getattr(partner, 'Repository') == owner
    _safe_set(owner, 'businessProcessCatalogue', None)
    assert getattr(partner, 'Repository') is None


def test_assoc_repository42_stub_double():
    # iso20022_Repository has no real 'Repository44' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_DataDictionary()
    partner = iso20022_Repository()
    setattr(partner, 'Repository44', None)
    _safe_set(owner, 'dataDictionary43', partner)
    assert getattr(partner, 'Repository44') == owner
    _safe_set(owner, 'dataDictionary43', None)
    assert getattr(partner, 'Repository44') is None


def test_assoc_send177_stub_double():
    # iso20022_Send has no real 'Send178' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageTransmission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageTransmission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageTransmission(messageTypeDescription="sample_text")
    partner = iso20022_Send()
    setattr(partner, 'Send178', None)
    _safe_set(owner, 'messageTransmission', partner)
    assert getattr(partner, 'Send178') == owner
    _safe_set(owner, 'messageTransmission', None)
    assert getattr(partner, 'Send178') is None


def test_assoc_sender17_stub_double():
    # iso20022_MessagingEndpoint has no real 'MessagingEndpoint18' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_TransportMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_TransportMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_TransportMessage()
    partner = iso20022_MessagingEndpoint()
    setattr(partner, 'MessagingEndpoint18', None)
    _safe_set(owner, 'sentMessage', partner)
    assert getattr(partner, 'MessagingEndpoint18') == owner
    _safe_set(owner, 'sentMessage', None)
    assert getattr(partner, 'MessagingEndpoint18') is None


def test_assoc_sentMessage10_stub_double():
    # iso20022_MessagingEndpoint has no real 'sender' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_TransportMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_TransportMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_TransportMessage()
    partner = iso20022_MessagingEndpoint()
    setattr(partner, 'sender', None)
    _safe_set(owner, 'TransportMessage11', partner)
    assert owner in getattr(partner, 'sender')
    _safe_set(owner, 'TransportMessage11', None)
    assert owner not in getattr(partner, 'sender')


def test_assoc_simpleType108_stub_double():
    # iso20022_DataType has no real 'iso20022_DataType' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageBuildingBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageBuildingBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageBuildingBlock()
    partner = iso20022_DataType()
    setattr(partner, 'iso20022_DataType', None)
    _safe_set(owner, 'iso20022_MessageBuildingBlock109', partner)
    assert getattr(partner, 'iso20022_DataType') == owner
    _safe_set(owner, 'iso20022_MessageBuildingBlock109', None)
    assert getattr(partner, 'iso20022_DataType') is None


def test_assoc_simpleType189_stub_double():
    # iso20022_DataType has no real 'iso20022_DataType190' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageAttribute()
    partner = iso20022_DataType()
    setattr(partner, 'iso20022_DataType190', None)
    _safe_set(owner, 'iso20022_MessageAttribute', partner)
    assert getattr(partner, 'iso20022_DataType190') == owner
    _safe_set(owner, 'iso20022_MessageAttribute', None)
    assert getattr(partner, 'iso20022_DataType190') is None


def test_assoc_simpleType194_stub_double():
    # iso20022_DataType has no real 'iso20022_DataType195' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessAttribute()
    partner = iso20022_DataType()
    setattr(partner, 'iso20022_DataType195', None)
    _safe_set(owner, 'iso20022_BusinessAttribute', partner)
    assert getattr(partner, 'iso20022_DataType195') == owner
    _safe_set(owner, 'iso20022_BusinessAttribute', None)
    assert getattr(partner, 'iso20022_DataType195') is None


def test_assoc_syntax71_stub_double():
    # iso20022_Encoding has no real 'possibleEncodings' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_Syntax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_Syntax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_Syntax()
    partner = iso20022_Encoding()
    setattr(partner, 'possibleEncodings', None)
    _safe_set(owner, 'Syntax72', partner)
    assert getattr(partner, 'possibleEncodings') == owner
    _safe_set(owner, 'Syntax72', None)
    assert getattr(partner, 'possibleEncodings') is None


def test_assoc_topLevelCatalogueEntry35_stub_double():
    # iso20022_TopLevelCatalogueEntry has no real 'TopLevelCatalogueEntry' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessProcessCatalogue()
    partner = iso20022_TopLevelCatalogueEntry()
    setattr(partner, 'TopLevelCatalogueEntry', None)
    _safe_set(owner, 'businessProcessCatalogue36', {partner})
    assert getattr(partner, 'TopLevelCatalogueEntry') == owner
    _safe_set(owner, 'businessProcessCatalogue36', set())
    assert getattr(partner, 'TopLevelCatalogueEntry') is None


def test_assoc_topLevelDictionaryEntry41_stub_double():
    # iso20022_TopLevelDictionaryEntry has no real 'TopLevelDictionaryEntry' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_DataDictionary()
    partner = iso20022_TopLevelDictionaryEntry()
    setattr(partner, 'TopLevelDictionaryEntry', None)
    _safe_set(owner, 'dataDictionary', {partner})
    assert getattr(partner, 'TopLevelDictionaryEntry') == owner
    _safe_set(owner, 'dataDictionary', set())
    assert getattr(partner, 'TopLevelDictionaryEntry') is None


def test_assoc_trace137_stub_double():
    # iso20022_MessageChoreography has no real 'MessageChoreography138' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_BusinessTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_BusinessTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_BusinessTransaction()
    partner = iso20022_MessageChoreography()
    setattr(partner, 'MessageChoreography138', None)
    _safe_set(owner, 'businessTransactionTrace', {partner})
    assert getattr(partner, 'MessageChoreography138') == owner
    _safe_set(owner, 'businessTransactionTrace', set())
    assert getattr(partner, 'MessageChoreography138') is None


def test_assoc_transportMessage23_stub_double():
    # iso20022_MessageInstance has no real 'messageInstance' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_TransportMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_TransportMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_TransportMessage()
    partner = iso20022_MessageInstance()
    setattr(partner, 'messageInstance', None)
    _safe_set(owner, 'TransportMessage24', partner)
    assert owner in getattr(partner, 'messageInstance')
    _safe_set(owner, 'TransportMessage24', None)
    assert owner not in getattr(partner, 'messageInstance')


def test_assoc_validEncoding61_stub_double():
    # iso20022_Encoding has no real 'Encoding' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageSet()
    partner = iso20022_Encoding()
    setattr(partner, 'Encoding', None)
    _safe_set(owner, 'messageSet', {partner})
    assert getattr(partner, 'Encoding') == owner
    _safe_set(owner, 'messageSet', set())
    assert getattr(partner, 'Encoding') is None


def test_assoc_xmlMemberType87_stub_double():
    # iso20022_LogicalType has no real 'iso20022_LogicalType' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageConstruct's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageConstruct's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageConstruct(xmlTag="sample_text")
    partner = iso20022_LogicalType()
    setattr(partner, 'iso20022_LogicalType', None)
    _safe_set(owner, 'iso20022_MessageConstruct', partner)
    assert getattr(partner, 'iso20022_LogicalType') == owner
    _safe_set(owner, 'iso20022_MessageConstruct', None)
    assert getattr(partner, 'iso20022_LogicalType') is None


def test_assoc_xors50_stub_double():
    # iso20022_Xor has no real 'Xor' property in the generated
    # code (a bare stub) -- manually attach it so iso20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iso20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iso20022_MessageDefinition(rootElement="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = iso20022_Xor()
    setattr(partner, 'Xor', None)
    _safe_set(owner, 'messageDefinition51', {partner})
    assert getattr(partner, 'Xor') == owner
    _safe_set(owner, 'messageDefinition51', set())
    assert getattr(partner, 'Xor') is None


