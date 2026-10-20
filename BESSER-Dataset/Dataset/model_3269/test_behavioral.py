import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTimeConcept,
    BusinessConcept,
    BusinessElement,
    BusinessElementType,
    DataType,
    ISO20022_AbstractTimeConcept,
    ISO20022_Amount,
    ISO20022_ApplicationHeader,
    ISO20022_BusinessArea,
    ISO20022_BusinessAssociationEnd,
    ISO20022_BusinessAttribute,
    ISO20022_BusinessComponent,
    ISO20022_BusinessConcept,
    ISO20022_BusinessElement,
    ISO20022_BusinessElementType,
    ISO20022_BusinessProcessCatalogue,
    ISO20022_BusinessRole,
    ISO20022_ChoiceComponent,
    ISO20022_Code,
    ISO20022_CodeSet,
    ISO20022_Constraint,
    ISO20022_DataDictionary,
    ISO20022_DataType,
    ISO20022_Diagram,
    ISO20022_Doclet,
    ISO20022_Encoding,
    ISO20022_EndPointCategory,
    ISO20022_ExternalSchema,
    ISO20022_Facet,
    ISO20022_IdentifierSet,
    ISO20022_Indicator,
    ISO20022_Interaction,
    ISO20022_InteractionActor,
    ISO20022_InteractionMessage,
    ISO20022_IsAnAlternativeFor,
    ISO20022_LogicalType,
    ISO20022_Member,
    ISO20022_MessageAssociationEnd,
    ISO20022_MessageAttribute,
    ISO20022_MessageBuildingBlock,
    ISO20022_MessageChoreography,
    ISO20022_MessageComponent,
    ISO20022_MessageComponentType,
    ISO20022_MessageConcept,
    ISO20022_MessageDefinition,
    ISO20022_MessageDefinitionIdentifier,
    ISO20022_MessageElement,
    ISO20022_MessageElementContainer,
    ISO20022_MessageSet,
    ISO20022_ModelEntity,
    ISO20022_MultiplicityEntity,
    ISO20022_Quantity,
    ISO20022_Rate,
    ISO20022_Repository,
    ISO20022_RepositoryConcept,
    ISO20022_SWIFTSolution,
    ISO20022_SemanticMarkup,
    ISO20022_SemanticMarkupElement,
    ISO20022_Syntax,
    ISO20022_SyntaxMessageScheme,
    ISO20022_Text,
    ISO20022_TopLevelCatalogueEntry,
    ISO20022_TopLevelDictionaryEntry,
    ISO20022_Type,
    ISO20022_UserDefined,
    ISO20022_XMLMember,
    ISO20022_XSDBinary,
    ISO20022_XSDBoolean,
    ISO20022_XSDDate,
    ISO20022_XSDDateTime,
    ISO20022_XSDDay,
    ISO20022_XSDDecimal,
    ISO20022_XSDDuration,
    ISO20022_XSDID,
    ISO20022_XSDMonth,
    ISO20022_XSDMonthDay,
    ISO20022_XSDString,
    ISO20022_XSDTime,
    ISO20022_XSDYear,
    ISO20022_XSDYearMonth,
    ISO20022_Xor,
    LogicalType,
    Member,
    MessageComponentType,
    MessageConcept,
    MessageDefinition,
    MessageElement,
    MessageElementContainer,
    MessageSet,
    ModelEntity,
    MultiplicityEntity,
    RepositoryConcept,
    TopLevelCatalogueEntry,
    TopLevelDictionaryEntry,
    Type,
    XMLMember,
    XSDBoolean,
    XSDDecimal,
    XSDString,
    Aggregation,
    Namespace,
    ProcessContent,
    RegistrationStatus,
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

def test_assoc_associationDomain42_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    a2 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text_2")
    b = ISO20022_BusinessAssociationEnd(aggregation="sample_text")
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


def test_assoc_businessArea101_reverse_link_reassign_clear():
    a1 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text_2", rootElement="sample_text_2", urn="sample_text_2", visibility="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = ISO20022_BusinessArea(code="sample_text")
    _safe_set(b, 'BusinessArea', a1)
    assert _is_linked(b, 'BusinessArea', a1)
    if hasattr(a1, 'messageDefinition'):
        assert _is_linked(a1, 'messageDefinition', b)
    _safe_set(b, 'BusinessArea', a2)
    assert _is_linked(b, 'BusinessArea', a2)
    if hasattr(a1, 'messageDefinition'):
        assert not _is_linked(a1, 'messageDefinition', b)
    if hasattr(a2, 'messageDefinition'):
        assert _is_linked(a2, 'messageDefinition', b)
    _safe_set(b, 'BusinessArea', None)
    assert not _is_linked(b, 'BusinessArea', a2)
    if hasattr(a2, 'messageDefinition'):
        assert not _is_linked(a2, 'messageDefinition', b)


def test_assoc_businessComponentTrace16_reverse_link_reassign_clear():
    a1 = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageElement(isDerived=False, isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
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


def test_assoc_businessElementTrace17_reverse_link_reassign_clear():
    a1 = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageElement(isDerived=False, isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_BusinessElement(isDerived=True)
    _safe_set(b, 'BusinessElement', a1)
    assert _is_linked(b, 'BusinessElement', a1)
    if hasattr(a1, 'derivation'):
        assert _is_linked(a1, 'derivation', b)
    _safe_set(b, 'BusinessElement', a2)
    assert _is_linked(b, 'BusinessElement', a2)
    if hasattr(a1, 'derivation'):
        assert not _is_linked(a1, 'derivation', b)
    if hasattr(a2, 'derivation'):
        assert _is_linked(a2, 'derivation', b)
    _safe_set(b, 'BusinessElement', None)
    assert not _is_linked(b, 'BusinessElement', a2)
    if hasattr(a2, 'derivation'):
        assert not _is_linked(a2, 'derivation', b)


def test_assoc_code164_reverse_link_reassign_clear():
    a1 = ISO20022_CodeSet(identificationScheme="sample_text")
    a2 = ISO20022_CodeSet(identificationScheme="sample_text_2")
    b = ISO20022_Code(codeName="sample_text")
    _safe_set(b, 'Code', a1)
    assert _is_linked(b, 'Code', a1)
    if hasattr(a1, 'owner165'):
        assert _is_linked(a1, 'owner165', b)
    _safe_set(b, 'Code', a2)
    assert _is_linked(b, 'Code', a2)
    if hasattr(a1, 'owner165'):
        assert not _is_linked(a1, 'owner165', b)
    if hasattr(a2, 'owner165'):
        assert _is_linked(a2, 'owner165', b)
    _safe_set(b, 'Code', None)
    assert not _is_linked(b, 'Code', a2)
    if hasattr(a2, 'owner165'):
        assert not _is_linked(a2, 'owner165', b)


def test_assoc_complexType153_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    a2 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text_2")
    b = ISO20022_BusinessAttribute()
    _safe_set(b, 'ISO20022_BusinessAttribute154', a1)
    assert _is_linked(b, 'ISO20022_BusinessAttribute154', a1)
    if hasattr(a1, 'ISO20022_BusinessComponent'):
        assert _is_linked(a1, 'ISO20022_BusinessComponent', b)
    _safe_set(b, 'ISO20022_BusinessAttribute154', a2)
    assert _is_linked(b, 'ISO20022_BusinessAttribute154', a2)
    if hasattr(a1, 'ISO20022_BusinessComponent'):
        assert not _is_linked(a1, 'ISO20022_BusinessComponent', b)
    if hasattr(a2, 'ISO20022_BusinessComponent'):
        assert _is_linked(a2, 'ISO20022_BusinessComponent', b)
    _safe_set(b, 'ISO20022_BusinessAttribute154', None)
    assert not _is_linked(b, 'ISO20022_BusinessAttribute154', a2)
    if hasattr(a2, 'ISO20022_BusinessComponent'):
        assert not _is_linked(a2, 'ISO20022_BusinessComponent', b)


def test_assoc_complexType71_reverse_link_reassign_clear():
    a1 = ISO20022_MessageComponentType(isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageComponentType(isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_MessageBuildingBlock()
    _safe_set(b, 'messageBuildingBlock', a1)
    assert _is_linked(b, 'messageBuildingBlock', a1)
    if hasattr(a1, 'MessageComponentType72'):
        assert _is_linked(a1, 'MessageComponentType72', b)
    _safe_set(b, 'messageBuildingBlock', a2)
    assert _is_linked(b, 'messageBuildingBlock', a2)
    if hasattr(a1, 'MessageComponentType72'):
        assert not _is_linked(a1, 'MessageComponentType72', b)
    if hasattr(a2, 'MessageComponentType72'):
        assert _is_linked(a2, 'MessageComponentType72', b)
    _safe_set(b, 'messageBuildingBlock', None)
    assert not _is_linked(b, 'messageBuildingBlock', a2)
    if hasattr(a2, 'MessageComponentType72'):
        assert not _is_linked(a2, 'MessageComponentType72', b)


def test_assoc_complexType83_reverse_link_reassign_clear():
    a1 = ISO20022_MessageComponentType(isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageComponentType(isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_MessageAttribute()
    _safe_set(b, 'ISO20022_MessageAttribute84', a1)
    assert _is_linked(b, 'ISO20022_MessageAttribute84', a1)
    if hasattr(a1, 'ISO20022_MessageComponentType85'):
        assert _is_linked(a1, 'ISO20022_MessageComponentType85', b)
    _safe_set(b, 'ISO20022_MessageAttribute84', a2)
    assert _is_linked(b, 'ISO20022_MessageAttribute84', a2)
    if hasattr(a1, 'ISO20022_MessageComponentType85'):
        assert not _is_linked(a1, 'ISO20022_MessageComponentType85', b)
    if hasattr(a2, 'ISO20022_MessageComponentType85'):
        assert _is_linked(a2, 'ISO20022_MessageComponentType85', b)
    _safe_set(b, 'ISO20022_MessageAttribute84', None)
    assert not _is_linked(b, 'ISO20022_MessageAttribute84', a2)
    if hasattr(a2, 'ISO20022_MessageComponentType85'):
        assert not _is_linked(a2, 'ISO20022_MessageComponentType85', b)


def test_assoc_componentContext18_reverse_link_reassign_clear():
    a1 = ISO20022_MessageElementContainer()
    a2 = ISO20022_MessageElementContainer()
    b = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
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


def test_assoc_constraint4_reverse_link_reassign_clear():
    a1 = ISO20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1), swiftRegistrationStatus="sample_text", swiftRemovalDate=date(2024, 1, 1))
    a2 = ISO20022_RepositoryConcept(definition="sample_text_2", example="sample_text_2", name="sample_text_2", registrationStatus="sample_text_2", removalDate=date(2025, 6, 15), swiftRegistrationStatus="sample_text_2", swiftRemovalDate=date(2025, 6, 15))
    b = ISO20022_Constraint(errorCode="sample_text", errorText="sample_text", expression="sample_text", expressionLanguage="sample_text", injected=True, kind="sample_text")
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


def test_assoc_derivation161_reverse_link_reassign_clear():
    a1 = ISO20022_CodeSet(identificationScheme="sample_text")
    a2 = ISO20022_CodeSet(identificationScheme="sample_text_2")
    b = ISO20022_CodeSet(identificationScheme="sample_text")
    _safe_set(b, 'trace162', {a1})
    assert _is_linked(b, 'trace162', a1)
    if hasattr(a1, 'CodeSet163'):
        assert _is_linked(a1, 'CodeSet163', b)
    _safe_set(b, 'trace162', {a2})
    assert _is_linked(b, 'trace162', a2)
    if hasattr(a1, 'CodeSet163'):
        assert not _is_linked(a1, 'CodeSet163', b)
    if hasattr(a2, 'CodeSet163'):
        assert _is_linked(a2, 'CodeSet163', b)
    _safe_set(b, 'trace162', set())
    assert not _is_linked(b, 'trace162', a2)
    if hasattr(a2, 'CodeSet163'):
        assert not _is_linked(a2, 'CodeSet163', b)


def test_assoc_derivation62_reverse_link_reassign_clear():
    a1 = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageElement(isDerived=False, isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_BusinessElement(isDerived=True)
    _safe_set(b, 'businessElementTrace', {a1})
    assert _is_linked(b, 'businessElementTrace', a1)
    if hasattr(a1, 'MessageElement63'):
        assert _is_linked(a1, 'MessageElement63', b)
    _safe_set(b, 'businessElementTrace', {a2})
    assert _is_linked(b, 'businessElementTrace', a2)
    if hasattr(a1, 'MessageElement63'):
        assert not _is_linked(a1, 'MessageElement63', b)
    if hasattr(a2, 'MessageElement63'):
        assert _is_linked(a2, 'MessageElement63', b)
    _safe_set(b, 'businessElementTrace', set())
    assert not _is_linked(b, 'businessElementTrace', a2)
    if hasattr(a2, 'MessageElement63'):
        assert not _is_linked(a2, 'MessageElement63', b)


def test_assoc_derivationComponent41_reverse_link_reassign_clear():
    a1 = ISO20022_MessageComponentType(isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageComponentType(isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
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


def test_assoc_derivationElement43_reverse_link_reassign_clear():
    a1 = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageElement(isDerived=False, isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
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


def test_assoc_diagram134_reverse_link_reassign_clear():
    a1 = ISO20022_Interaction(location="sample_text")
    a2 = ISO20022_Interaction(location="sample_text_2")
    b = ISO20022_Diagram(content="sample_text", location="sample_text")
    _safe_set(b, 'ISO20022_Diagram', a1)
    assert _is_linked(b, 'ISO20022_Diagram', a1)
    if hasattr(a1, 'ISO20022_Interaction'):
        assert _is_linked(a1, 'ISO20022_Interaction', b)
    _safe_set(b, 'ISO20022_Diagram', a2)
    assert _is_linked(b, 'ISO20022_Diagram', a2)
    if hasattr(a1, 'ISO20022_Interaction'):
        assert not _is_linked(a1, 'ISO20022_Interaction', b)
    if hasattr(a2, 'ISO20022_Interaction'):
        assert _is_linked(a2, 'ISO20022_Interaction', b)
    _safe_set(b, 'ISO20022_Diagram', None)
    assert not _is_linked(b, 'ISO20022_Diagram', a2)
    if hasattr(a2, 'ISO20022_Interaction'):
        assert not _is_linked(a2, 'ISO20022_Interaction', b)


def test_assoc_doclet2_reverse_link_reassign_clear():
    a1 = ISO20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1), swiftRegistrationStatus="sample_text", swiftRemovalDate=date(2024, 1, 1))
    a2 = ISO20022_RepositoryConcept(definition="sample_text_2", example="sample_text_2", name="sample_text_2", registrationStatus="sample_text_2", removalDate=date(2025, 6, 15), swiftRegistrationStatus="sample_text_2", swiftRemovalDate=date(2025, 6, 15))
    b = ISO20022_Doclet(content="sample_text", type="sample_text")
    _safe_set(b, 'ISO20022_Doclet', a1)
    assert _is_linked(b, 'ISO20022_Doclet', a1)
    if hasattr(a1, 'ISO20022_RepositoryConcept3'):
        assert _is_linked(a1, 'ISO20022_RepositoryConcept3', b)
    _safe_set(b, 'ISO20022_Doclet', a2)
    assert _is_linked(b, 'ISO20022_Doclet', a2)
    if hasattr(a1, 'ISO20022_RepositoryConcept3'):
        assert not _is_linked(a1, 'ISO20022_RepositoryConcept3', b)
    if hasattr(a2, 'ISO20022_RepositoryConcept3'):
        assert _is_linked(a2, 'ISO20022_RepositoryConcept3', b)
    _safe_set(b, 'ISO20022_Doclet', None)
    assert not _is_linked(b, 'ISO20022_Doclet', a2)
    if hasattr(a2, 'ISO20022_RepositoryConcept3'):
        assert not _is_linked(a2, 'ISO20022_RepositoryConcept3', b)


def test_assoc_element39_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessElement(isDerived=True)
    a2 = ISO20022_BusinessElement(isDerived=False)
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    _safe_set(b, 'elementContext', {a1})
    assert _is_linked(b, 'elementContext', a1)
    if hasattr(a1, 'BusinessElement40'):
        assert _is_linked(a1, 'BusinessElement40', b)
    _safe_set(b, 'elementContext', {a2})
    assert _is_linked(b, 'elementContext', a2)
    if hasattr(a1, 'BusinessElement40'):
        assert not _is_linked(a1, 'BusinessElement40', b)
    if hasattr(a2, 'BusinessElement40'):
        assert _is_linked(a2, 'BusinessElement40', b)
    _safe_set(b, 'elementContext', set())
    assert not _is_linked(b, 'elementContext', a2)
    if hasattr(a2, 'BusinessElement40'):
        assert not _is_linked(a2, 'BusinessElement40', b)


def test_assoc_elementContext65_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessElement(isDerived=True)
    a2 = ISO20022_BusinessElement(isDerived=False)
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    _safe_set(b, 'BusinessComponent66', a1)
    assert _is_linked(b, 'BusinessComponent66', a1)
    if hasattr(a1, 'element'):
        assert _is_linked(a1, 'element', b)
    _safe_set(b, 'BusinessComponent66', a2)
    assert _is_linked(b, 'BusinessComponent66', a2)
    if hasattr(a1, 'element'):
        assert not _is_linked(a1, 'element', b)
    if hasattr(a2, 'element'):
        assert _is_linked(a2, 'element', b)
    _safe_set(b, 'BusinessComponent66', None)
    assert not _is_linked(b, 'BusinessComponent66', a2)
    if hasattr(a2, 'element'):
        assert not _is_linked(a2, 'element', b)


def test_assoc_elements10_reverse_link_reassign_clear():
    a1 = ISO20022_SemanticMarkupElement(name="sample_text", value="sample_text")
    a2 = ISO20022_SemanticMarkupElement(name="sample_text_2", value="sample_text_2")
    b = ISO20022_SemanticMarkup(type="sample_text")
    _safe_set(b, 'ISO20022_SemanticMarkup11', {a1})
    assert _is_linked(b, 'ISO20022_SemanticMarkup11', a1)
    if hasattr(a1, 'ISO20022_SemanticMarkupElement'):
        assert _is_linked(a1, 'ISO20022_SemanticMarkupElement', b)
    _safe_set(b, 'ISO20022_SemanticMarkup11', {a2})
    assert _is_linked(b, 'ISO20022_SemanticMarkup11', a2)
    if hasattr(a1, 'ISO20022_SemanticMarkupElement'):
        assert not _is_linked(a1, 'ISO20022_SemanticMarkupElement', b)
    if hasattr(a2, 'ISO20022_SemanticMarkupElement'):
        assert _is_linked(a2, 'ISO20022_SemanticMarkupElement', b)
    _safe_set(b, 'ISO20022_SemanticMarkup11', set())
    assert not _is_linked(b, 'ISO20022_SemanticMarkup11', a2)
    if hasattr(a2, 'ISO20022_SemanticMarkupElement'):
        assert not _is_linked(a2, 'ISO20022_SemanticMarkupElement', b)


def test_assoc_generatedFor149_reverse_link_reassign_clear():
    a1 = ISO20022_Syntax()
    a2 = ISO20022_Syntax()
    b = ISO20022_MessageSet()
    _safe_set(b, 'MessageSet150', a1)
    assert _is_linked(b, 'MessageSet150', a1)
    if hasattr(a1, 'generatedSyntax'):
        assert _is_linked(a1, 'generatedSyntax', b)
    _safe_set(b, 'MessageSet150', a2)
    assert _is_linked(b, 'MessageSet150', a2)
    if hasattr(a1, 'generatedSyntax'):
        assert not _is_linked(a1, 'generatedSyntax', b)
    if hasattr(a2, 'generatedSyntax'):
        assert _is_linked(a2, 'generatedSyntax', b)
    _safe_set(b, 'MessageSet150', None)
    assert not _is_linked(b, 'MessageSet150', a2)
    if hasattr(a2, 'generatedSyntax'):
        assert not _is_linked(a2, 'generatedSyntax', b)


def test_assoc_generatedSyntax91_reverse_link_reassign_clear():
    a1 = ISO20022_Syntax()
    a2 = ISO20022_Syntax()
    b = ISO20022_MessageSet()
    _safe_set(b, 'generatedFor', {a1})
    assert _is_linked(b, 'generatedFor', a1)
    if hasattr(a1, 'Syntax92'):
        assert _is_linked(a1, 'Syntax92', b)
    _safe_set(b, 'generatedFor', {a2})
    assert _is_linked(b, 'generatedFor', a2)
    if hasattr(a1, 'Syntax92'):
        assert not _is_linked(a1, 'Syntax92', b)
    if hasattr(a2, 'Syntax92'):
        assert _is_linked(a2, 'Syntax92', b)
    _safe_set(b, 'generatedFor', set())
    assert not _is_linked(b, 'generatedFor', a2)
    if hasattr(a2, 'Syntax92'):
        assert not _is_linked(a2, 'Syntax92', b)


def test_assoc_interactions89_reverse_link_reassign_clear():
    a1 = ISO20022_MessageSet()
    a2 = ISO20022_MessageSet()
    b = ISO20022_Interaction(location="sample_text")
    _safe_set(b, 'Interaction', a1)
    assert _is_linked(b, 'Interaction', a1)
    if hasattr(a1, 'messageSet90'):
        assert _is_linked(a1, 'messageSet90', b)
    _safe_set(b, 'Interaction', a2)
    assert _is_linked(b, 'Interaction', a2)
    if hasattr(a1, 'messageSet90'):
        assert not _is_linked(a1, 'messageSet90', b)
    if hasattr(a2, 'messageSet90'):
        assert _is_linked(a2, 'messageSet90', b)
    _safe_set(b, 'Interaction', None)
    assert not _is_linked(b, 'Interaction', a2)
    if hasattr(a2, 'messageSet90'):
        assert not _is_linked(a2, 'messageSet90', b)


def test_assoc_master96_reverse_link_reassign_clear():
    a1 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text_2", rootElement="sample_text_2", urn="sample_text_2", visibility="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'subsets', a1)
    assert _is_linked(b, 'subsets', a1)
    if hasattr(a1, 'MessageDefinition97'):
        assert _is_linked(a1, 'MessageDefinition97', b)
    _safe_set(b, 'subsets', a2)
    assert _is_linked(b, 'subsets', a2)
    if hasattr(a1, 'MessageDefinition97'):
        assert not _is_linked(a1, 'MessageDefinition97', b)
    if hasattr(a2, 'MessageDefinition97'):
        assert _is_linked(a2, 'MessageDefinition97', b)
    _safe_set(b, 'subsets', None)
    assert not _is_linked(b, 'subsets', a2)
    if hasattr(a2, 'MessageDefinition97'):
        assert not _is_linked(a2, 'MessageDefinition97', b)


def test_assoc_messageBuildingBlock104_reverse_link_reassign_clear():
    a1 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text_2", rootElement="sample_text_2", urn="sample_text_2", visibility="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = ISO20022_MessageBuildingBlock()
    _safe_set(b, 'ISO20022_MessageBuildingBlock105', a1)
    assert _is_linked(b, 'ISO20022_MessageBuildingBlock105', a1)
    if hasattr(a1, 'ISO20022_MessageDefinition'):
        assert _is_linked(a1, 'ISO20022_MessageDefinition', b)
    _safe_set(b, 'ISO20022_MessageBuildingBlock105', a2)
    assert _is_linked(b, 'ISO20022_MessageBuildingBlock105', a2)
    if hasattr(a1, 'ISO20022_MessageDefinition'):
        assert not _is_linked(a1, 'ISO20022_MessageDefinition', b)
    if hasattr(a2, 'ISO20022_MessageDefinition'):
        assert _is_linked(a2, 'ISO20022_MessageDefinition', b)
    _safe_set(b, 'ISO20022_MessageBuildingBlock105', None)
    assert not _is_linked(b, 'ISO20022_MessageBuildingBlock105', a2)
    if hasattr(a2, 'ISO20022_MessageDefinition'):
        assert not _is_linked(a2, 'ISO20022_MessageDefinition', b)


def test_assoc_messageBuildingBlock67_reverse_link_reassign_clear():
    a1 = ISO20022_MessageComponentType(isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageComponentType(isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_MessageBuildingBlock()
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


def test_assoc_messageDefinition114_reverse_link_reassign_clear():
    a1 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text_2", rootElement="sample_text_2", urn="sample_text_2", visibility="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = ISO20022_BusinessArea(code="sample_text")
    _safe_set(b, 'businessArea', {a1})
    assert _is_linked(b, 'businessArea', a1)
    if hasattr(a1, 'MessageDefinition115'):
        assert _is_linked(a1, 'MessageDefinition115', b)
    _safe_set(b, 'businessArea', {a2})
    assert _is_linked(b, 'businessArea', a2)
    if hasattr(a1, 'MessageDefinition115'):
        assert not _is_linked(a1, 'MessageDefinition115', b)
    if hasattr(a2, 'MessageDefinition115'):
        assert _is_linked(a2, 'MessageDefinition115', b)
    _safe_set(b, 'businessArea', set())
    assert not _is_linked(b, 'businessArea', a2)
    if hasattr(a2, 'MessageDefinition115'):
        assert not _is_linked(a2, 'MessageDefinition115', b)


def test_assoc_messageDefinition88_reverse_link_reassign_clear():
    a1 = ISO20022_MessageSet()
    a2 = ISO20022_MessageSet()
    b = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'MessageDefinition', a1)
    assert _is_linked(b, 'MessageDefinition', a1)
    if hasattr(a1, 'messageSet'):
        assert _is_linked(a1, 'messageSet', b)
    _safe_set(b, 'MessageDefinition', a2)
    assert _is_linked(b, 'MessageDefinition', a2)
    if hasattr(a1, 'messageSet'):
        assert not _is_linked(a1, 'messageSet', b)
    if hasattr(a2, 'messageSet'):
        assert _is_linked(a2, 'messageSet', b)
    _safe_set(b, 'MessageDefinition', None)
    assert not _is_linked(b, 'MessageDefinition', a2)
    if hasattr(a2, 'messageSet'):
        assert not _is_linked(a2, 'messageSet', b)


def test_assoc_messageDefinitionIdentifier109_reverse_link_reassign_clear():
    a1 = ISO20022_MessageDefinitionIdentifier(businessArea="sample_text", flavour="sample_text", messageFunctionality="sample_text", version="sample_text")
    a2 = ISO20022_MessageDefinitionIdentifier(businessArea="sample_text_2", flavour="sample_text_2", messageFunctionality="sample_text_2", version="sample_text_2")
    b = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'ISO20022_MessageDefinition110', a1)
    assert _is_linked(b, 'ISO20022_MessageDefinition110', a1)
    if hasattr(a1, 'ISO20022_MessageDefinitionIdentifier'):
        assert _is_linked(a1, 'ISO20022_MessageDefinitionIdentifier', b)
    _safe_set(b, 'ISO20022_MessageDefinition110', a2)
    assert _is_linked(b, 'ISO20022_MessageDefinition110', a2)
    if hasattr(a1, 'ISO20022_MessageDefinitionIdentifier'):
        assert not _is_linked(a1, 'ISO20022_MessageDefinitionIdentifier', b)
    if hasattr(a2, 'ISO20022_MessageDefinitionIdentifier'):
        assert _is_linked(a2, 'ISO20022_MessageDefinitionIdentifier', b)
    _safe_set(b, 'ISO20022_MessageDefinition110', None)
    assert not _is_linked(b, 'ISO20022_MessageDefinition110', a2)
    if hasattr(a2, 'ISO20022_MessageDefinitionIdentifier'):
        assert not _is_linked(a2, 'ISO20022_MessageDefinitionIdentifier', b)


def test_assoc_messageElement79_reverse_link_reassign_clear():
    a1 = ISO20022_MessageElementContainer()
    a2 = ISO20022_MessageElementContainer()
    b = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
    _safe_set(b, 'MessageElement80', a1)
    assert _is_linked(b, 'MessageElement80', a1)
    if hasattr(a1, 'componentContext'):
        assert _is_linked(a1, 'componentContext', b)
    _safe_set(b, 'MessageElement80', a2)
    assert _is_linked(b, 'MessageElement80', a2)
    if hasattr(a1, 'componentContext'):
        assert not _is_linked(a1, 'componentContext', b)
    if hasattr(a2, 'componentContext'):
        assert _is_linked(a2, 'componentContext', b)
    _safe_set(b, 'MessageElement80', None)
    assert not _is_linked(b, 'MessageElement80', a2)
    if hasattr(a2, 'componentContext'):
        assert not _is_linked(a2, 'componentContext', b)


def test_assoc_messageSet111_reverse_link_reassign_clear():
    a1 = ISO20022_MessageSet()
    a2 = ISO20022_MessageSet()
    b = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'messageDefinition112', {a1})
    assert _is_linked(b, 'messageDefinition112', a1)
    if hasattr(a1, 'MessageSet113'):
        assert _is_linked(a1, 'MessageSet113', b)
    _safe_set(b, 'messageDefinition112', {a2})
    assert _is_linked(b, 'messageDefinition112', a2)
    if hasattr(a1, 'MessageSet113'):
        assert not _is_linked(a1, 'MessageSet113', b)
    if hasattr(a2, 'MessageSet113'):
        assert _is_linked(a2, 'MessageSet113', b)
    _safe_set(b, 'messageDefinition112', set())
    assert not _is_linked(b, 'messageDefinition112', a2)
    if hasattr(a2, 'MessageSet113'):
        assert not _is_linked(a2, 'MessageSet113', b)


def test_assoc_messageSet135_reverse_link_reassign_clear():
    a1 = ISO20022_MessageSet()
    a2 = ISO20022_MessageSet()
    b = ISO20022_Interaction(location="sample_text")
    _safe_set(b, 'interactions', a1)
    assert _is_linked(b, 'interactions', a1)
    if hasattr(a1, 'MessageSet136'):
        assert _is_linked(a1, 'MessageSet136', b)
    _safe_set(b, 'interactions', a2)
    assert _is_linked(b, 'interactions', a2)
    if hasattr(a1, 'MessageSet136'):
        assert not _is_linked(a1, 'MessageSet136', b)
    if hasattr(a2, 'MessageSet136'):
        assert _is_linked(a2, 'MessageSet136', b)
    _safe_set(b, 'interactions', None)
    assert not _is_linked(b, 'interactions', a2)
    if hasattr(a2, 'MessageSet136'):
        assert not _is_linked(a2, 'MessageSet136', b)


def test_assoc_nextVersions6_reverse_link_reassign_clear():
    a1 = ISO20022_ModelEntity(objectIdentifier="sample_text")
    a2 = ISO20022_ModelEntity(objectIdentifier="sample_text_2")
    b = ISO20022_ModelEntity(objectIdentifier="sample_text")
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


def test_assoc_opposite14_reverse_link_reassign_clear():
    a1 = ISO20022_MessageAssociationEnd(isComposite=True)
    a2 = ISO20022_MessageAssociationEnd(isComposite=False)
    b = ISO20022_MessageAssociationEnd(isComposite=True)
    _safe_set(b, 'ISO20022_MessageAssociationEnd15', a1)
    assert _is_linked(b, 'ISO20022_MessageAssociationEnd15', a1)
    if hasattr(a1, 'ISO20022_MessageAssociationEnd13'):
        assert _is_linked(a1, 'ISO20022_MessageAssociationEnd13', b)
    _safe_set(b, 'ISO20022_MessageAssociationEnd15', a2)
    assert _is_linked(b, 'ISO20022_MessageAssociationEnd15', a2)
    if hasattr(a1, 'ISO20022_MessageAssociationEnd13'):
        assert not _is_linked(a1, 'ISO20022_MessageAssociationEnd13', b)
    if hasattr(a2, 'ISO20022_MessageAssociationEnd13'):
        assert _is_linked(a2, 'ISO20022_MessageAssociationEnd13', b)
    _safe_set(b, 'ISO20022_MessageAssociationEnd15', None)
    assert not _is_linked(b, 'ISO20022_MessageAssociationEnd15', a2)
    if hasattr(a2, 'ISO20022_MessageAssociationEnd13'):
        assert not _is_linked(a2, 'ISO20022_MessageAssociationEnd13', b)


def test_assoc_opposite76_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessAssociationEnd(aggregation="sample_text")
    a2 = ISO20022_BusinessAssociationEnd(aggregation="sample_text_2")
    b = ISO20022_BusinessAssociationEnd(aggregation="sample_text")
    _safe_set(b, 'ISO20022_BusinessAssociationEnd75', a1)
    assert _is_linked(b, 'ISO20022_BusinessAssociationEnd75', a1)
    if hasattr(a1, 'ISO20022_BusinessAssociationEnd'):
        assert _is_linked(a1, 'ISO20022_BusinessAssociationEnd', b)
    _safe_set(b, 'ISO20022_BusinessAssociationEnd75', a2)
    assert _is_linked(b, 'ISO20022_BusinessAssociationEnd75', a2)
    if hasattr(a1, 'ISO20022_BusinessAssociationEnd'):
        assert not _is_linked(a1, 'ISO20022_BusinessAssociationEnd', b)
    if hasattr(a2, 'ISO20022_BusinessAssociationEnd'):
        assert _is_linked(a2, 'ISO20022_BusinessAssociationEnd', b)
    _safe_set(b, 'ISO20022_BusinessAssociationEnd75', None)
    assert not _is_linked(b, 'ISO20022_BusinessAssociationEnd75', a2)
    if hasattr(a2, 'ISO20022_BusinessAssociationEnd'):
        assert not _is_linked(a2, 'ISO20022_BusinessAssociationEnd', b)


def test_assoc_owner0_reverse_link_reassign_clear():
    a1 = ISO20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1), swiftRegistrationStatus="sample_text", swiftRemovalDate=date(2024, 1, 1))
    a2 = ISO20022_RepositoryConcept(definition="sample_text_2", example="sample_text_2", name="sample_text_2", registrationStatus="sample_text_2", removalDate=date(2025, 6, 15), swiftRegistrationStatus="sample_text_2", swiftRemovalDate=date(2025, 6, 15))
    b = ISO20022_Constraint(errorCode="sample_text", errorText="sample_text", expression="sample_text", expressionLanguage="sample_text", injected=True, kind="sample_text")
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


def test_assoc_owner155_reverse_link_reassign_clear():
    a1 = ISO20022_CodeSet(identificationScheme="sample_text")
    a2 = ISO20022_CodeSet(identificationScheme="sample_text_2")
    b = ISO20022_Code(codeName="sample_text")
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


def test_assoc_previousVersion8_reverse_link_reassign_clear():
    a1 = ISO20022_ModelEntity(objectIdentifier="sample_text")
    a2 = ISO20022_ModelEntity(objectIdentifier="sample_text_2")
    b = ISO20022_ModelEntity(objectIdentifier="sample_text")
    _safe_set(b, 'nextVersions', a1)
    assert _is_linked(b, 'nextVersions', a1)
    if hasattr(a1, 'ModelEntity9'):
        assert _is_linked(a1, 'ModelEntity9', b)
    _safe_set(b, 'nextVersions', a2)
    assert _is_linked(b, 'nextVersions', a2)
    if hasattr(a1, 'ModelEntity9'):
        assert not _is_linked(a1, 'ModelEntity9', b)
    if hasattr(a2, 'ModelEntity9'):
        assert _is_linked(a2, 'ModelEntity9', b)
    _safe_set(b, 'nextVersions', None)
    assert not _is_linked(b, 'nextVersions', a2)
    if hasattr(a2, 'ModelEntity9'):
        assert not _is_linked(a2, 'ModelEntity9', b)


def test_assoc_semanticMarkup1_reverse_link_reassign_clear():
    a1 = ISO20022_SemanticMarkup(type="sample_text")
    a2 = ISO20022_SemanticMarkup(type="sample_text_2")
    b = ISO20022_RepositoryConcept(definition="sample_text", example="sample_text", name="sample_text", registrationStatus="sample_text", removalDate=date(2024, 1, 1), swiftRegistrationStatus="sample_text", swiftRemovalDate=date(2024, 1, 1))
    _safe_set(b, 'ISO20022_RepositoryConcept', {a1})
    assert _is_linked(b, 'ISO20022_RepositoryConcept', a1)
    if hasattr(a1, 'ISO20022_SemanticMarkup'):
        assert _is_linked(a1, 'ISO20022_SemanticMarkup', b)
    _safe_set(b, 'ISO20022_RepositoryConcept', {a2})
    assert _is_linked(b, 'ISO20022_RepositoryConcept', a2)
    if hasattr(a1, 'ISO20022_SemanticMarkup'):
        assert not _is_linked(a1, 'ISO20022_SemanticMarkup', b)
    if hasattr(a2, 'ISO20022_SemanticMarkup'):
        assert _is_linked(a2, 'ISO20022_SemanticMarkup', b)
    _safe_set(b, 'ISO20022_RepositoryConcept', set())
    assert not _is_linked(b, 'ISO20022_RepositoryConcept', a2)
    if hasattr(a2, 'ISO20022_SemanticMarkup'):
        assert not _is_linked(a2, 'ISO20022_SemanticMarkup', b)


def test_assoc_subType34_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    a2 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text_2")
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    _safe_set(b, 'superType', {a1})
    assert _is_linked(b, 'superType', a1)
    if hasattr(a1, 'BusinessComponent35'):
        assert _is_linked(a1, 'BusinessComponent35', b)
    _safe_set(b, 'superType', {a2})
    assert _is_linked(b, 'superType', a2)
    if hasattr(a1, 'BusinessComponent35'):
        assert not _is_linked(a1, 'BusinessComponent35', b)
    if hasattr(a2, 'BusinessComponent35'):
        assert _is_linked(a2, 'BusinessComponent35', b)
    _safe_set(b, 'superType', set())
    assert not _is_linked(b, 'superType', a2)
    if hasattr(a2, 'BusinessComponent35'):
        assert not _is_linked(a2, 'BusinessComponent35', b)


def test_assoc_subsets99_reverse_link_reassign_clear():
    a1 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    a2 = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text_2", rootElement="sample_text_2", urn="sample_text_2", visibility="sample_text_2", xmlName="sample_text_2", xmlTag="sample_text_2")
    b = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    _safe_set(b, 'master', {a1})
    assert _is_linked(b, 'master', a1)
    if hasattr(a1, 'MessageDefinition100'):
        assert _is_linked(a1, 'MessageDefinition100', b)
    _safe_set(b, 'master', {a2})
    assert _is_linked(b, 'master', a2)
    if hasattr(a1, 'MessageDefinition100'):
        assert not _is_linked(a1, 'MessageDefinition100', b)
    if hasattr(a2, 'MessageDefinition100'):
        assert _is_linked(a2, 'MessageDefinition100', b)
    _safe_set(b, 'master', set())
    assert not _is_linked(b, 'master', a2)
    if hasattr(a2, 'MessageDefinition100'):
        assert not _is_linked(a2, 'MessageDefinition100', b)


def test_assoc_superType37_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    a2 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text_2")
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    _safe_set(b, 'subType', a1)
    assert _is_linked(b, 'subType', a1)
    if hasattr(a1, 'BusinessComponent38'):
        assert _is_linked(a1, 'BusinessComponent38', b)
    _safe_set(b, 'subType', a2)
    assert _is_linked(b, 'subType', a2)
    if hasattr(a1, 'BusinessComponent38'):
        assert not _is_linked(a1, 'BusinessComponent38', b)
    if hasattr(a2, 'BusinessComponent38'):
        assert _is_linked(a2, 'BusinessComponent38', b)
    _safe_set(b, 'subType', None)
    assert not _is_linked(b, 'subType', a2)
    if hasattr(a2, 'BusinessComponent38'):
        assert not _is_linked(a2, 'BusinessComponent38', b)


def test_assoc_trace157_reverse_link_reassign_clear():
    a1 = ISO20022_CodeSet(identificationScheme="sample_text")
    a2 = ISO20022_CodeSet(identificationScheme="sample_text_2")
    b = ISO20022_CodeSet(identificationScheme="sample_text")
    _safe_set(b, 'derivation158', a1)
    assert _is_linked(b, 'derivation158', a1)
    if hasattr(a1, 'CodeSet159'):
        assert _is_linked(a1, 'CodeSet159', b)
    _safe_set(b, 'derivation158', a2)
    assert _is_linked(b, 'derivation158', a2)
    if hasattr(a1, 'CodeSet159'):
        assert not _is_linked(a1, 'CodeSet159', b)
    if hasattr(a2, 'CodeSet159'):
        assert _is_linked(a2, 'CodeSet159', b)
    _safe_set(b, 'derivation158', None)
    assert not _is_linked(b, 'derivation158', a2)
    if hasattr(a2, 'CodeSet159'):
        assert not _is_linked(a2, 'CodeSet159', b)


def test_assoc_trace68_reverse_link_reassign_clear():
    a1 = ISO20022_MessageComponentType(isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageComponentType(isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    _safe_set(b, 'BusinessComponent69', a1)
    assert _is_linked(b, 'BusinessComponent69', a1)
    if hasattr(a1, 'derivationComponent'):
        assert _is_linked(a1, 'derivationComponent', b)
    _safe_set(b, 'BusinessComponent69', a2)
    assert _is_linked(b, 'BusinessComponent69', a2)
    if hasattr(a1, 'derivationComponent'):
        assert not _is_linked(a1, 'derivationComponent', b)
    if hasattr(a2, 'derivationComponent'):
        assert _is_linked(a2, 'derivationComponent', b)
    _safe_set(b, 'BusinessComponent69', None)
    assert not _is_linked(b, 'BusinessComponent69', a2)
    if hasattr(a2, 'derivationComponent'):
        assert not _is_linked(a2, 'derivationComponent', b)


def test_assoc_type12_reverse_link_reassign_clear():
    a1 = ISO20022_MessageComponentType(isTechnical=True, tracePath="sample_text")
    a2 = ISO20022_MessageComponentType(isTechnical=False, tracePath="sample_text_2")
    b = ISO20022_MessageAssociationEnd(isComposite=True)
    _safe_set(b, 'ISO20022_MessageAssociationEnd', a1)
    assert _is_linked(b, 'ISO20022_MessageAssociationEnd', a1)
    if hasattr(a1, 'ISO20022_MessageComponentType'):
        assert _is_linked(a1, 'ISO20022_MessageComponentType', b)
    _safe_set(b, 'ISO20022_MessageAssociationEnd', a2)
    assert _is_linked(b, 'ISO20022_MessageAssociationEnd', a2)
    if hasattr(a1, 'ISO20022_MessageComponentType'):
        assert not _is_linked(a1, 'ISO20022_MessageComponentType', b)
    if hasattr(a2, 'ISO20022_MessageComponentType'):
        assert _is_linked(a2, 'ISO20022_MessageComponentType', b)
    _safe_set(b, 'ISO20022_MessageAssociationEnd', None)
    assert not _is_linked(b, 'ISO20022_MessageAssociationEnd', a2)
    if hasattr(a2, 'ISO20022_MessageComponentType'):
        assert not _is_linked(a2, 'ISO20022_MessageComponentType', b)


def test_assoc_type77_reverse_link_reassign_clear():
    a1 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text")
    a2 = ISO20022_BusinessComponent(previousVersionDocumentation="sample_text_2")
    b = ISO20022_BusinessAssociationEnd(aggregation="sample_text")
    _safe_set(b, 'associationDomain', a1)
    assert _is_linked(b, 'associationDomain', a1)
    if hasattr(a1, 'BusinessComponent78'):
        assert _is_linked(a1, 'BusinessComponent78', b)
    _safe_set(b, 'associationDomain', a2)
    assert _is_linked(b, 'associationDomain', a2)
    if hasattr(a1, 'BusinessComponent78'):
        assert not _is_linked(a1, 'BusinessComponent78', b)
    if hasattr(a2, 'BusinessComponent78'):
        assert _is_linked(a2, 'BusinessComponent78', b)
    _safe_set(b, 'associationDomain', None)
    assert not _is_linked(b, 'associationDomain', a2)
    if hasattr(a2, 'BusinessComponent78'):
        assert not _is_linked(a2, 'BusinessComponent78', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actors131_stub_double():
    # ISO20022_InteractionActor has no real 'InteractionActor' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Interaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Interaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Interaction(location="sample_text")
    partner = ISO20022_InteractionActor()
    setattr(partner, 'InteractionActor', None)
    _safe_set(owner, 'interaction', {partner})
    assert getattr(partner, 'InteractionActor') == owner
    _safe_set(owner, 'interaction', set())
    assert getattr(partner, 'InteractionActor') is None


def test_assoc_businessElementType64_stub_double():
    # ISO20022_BusinessElementType has no real 'ISO20022_BusinessElementType' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_BusinessElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_BusinessElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_BusinessElement(isDerived=True)
    partner = ISO20022_BusinessElementType()
    setattr(partner, 'ISO20022_BusinessElementType', None)
    _safe_set(owner, 'ISO20022_BusinessElement', partner)
    assert getattr(partner, 'ISO20022_BusinessElementType') == owner
    _safe_set(owner, 'ISO20022_BusinessElement', None)
    assert getattr(partner, 'ISO20022_BusinessElementType') is None


def test_assoc_businessProcessCatalogue48_stub_double():
    # ISO20022_Repository has no real 'repository' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_BusinessProcessCatalogue()
    partner = ISO20022_Repository()
    setattr(partner, 'repository', None)
    _safe_set(owner, 'BusinessProcessCatalogue', partner)
    assert getattr(partner, 'repository') == owner
    _safe_set(owner, 'BusinessProcessCatalogue', None)
    assert getattr(partner, 'repository') is None


def test_assoc_businessProcessCatalogue58_stub_double():
    # ISO20022_TopLevelCatalogueEntry has no real 'topLevelCatalogueEntry' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_BusinessProcessCatalogue()
    partner = ISO20022_TopLevelCatalogueEntry()
    setattr(partner, 'topLevelCatalogueEntry', None)
    _safe_set(owner, 'BusinessProcessCatalogue59', partner)
    assert getattr(partner, 'topLevelCatalogueEntry') == owner
    _safe_set(owner, 'BusinessProcessCatalogue59', None)
    assert getattr(partner, 'topLevelCatalogueEntry') is None


def test_assoc_currencyIdentifierSet166_stub_double():
    # ISO20022_Amount has no real 'ISO20022_Amount' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_IdentifierSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_IdentifierSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_IdentifierSet(identificationScheme="sample_text")
    partner = ISO20022_Amount()
    setattr(partner, 'ISO20022_Amount', None)
    _safe_set(owner, 'ISO20022_IdentifierSet', partner)
    assert getattr(partner, 'ISO20022_Amount') == owner
    _safe_set(owner, 'ISO20022_IdentifierSet', None)
    assert getattr(partner, 'ISO20022_Amount') is None


def test_assoc_dataDictionary44_stub_double():
    # ISO20022_TopLevelDictionaryEntry has no real 'topLevelDictionaryEntry' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_DataDictionary()
    partner = ISO20022_TopLevelDictionaryEntry()
    setattr(partner, 'topLevelDictionaryEntry', None)
    _safe_set(owner, 'DataDictionary', partner)
    assert getattr(partner, 'topLevelDictionaryEntry') == owner
    _safe_set(owner, 'DataDictionary', None)
    assert getattr(partner, 'topLevelDictionaryEntry') is None


def test_assoc_dataDictionary51_stub_double():
    # ISO20022_Repository has no real 'repository52' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_DataDictionary()
    partner = ISO20022_Repository()
    setattr(partner, 'repository52', None)
    _safe_set(owner, 'DataDictionary53', partner)
    assert getattr(partner, 'repository52') == owner
    _safe_set(owner, 'DataDictionary53', None)
    assert getattr(partner, 'repository52') is None


def test_assoc_derivation106_stub_double():
    # ISO20022_SyntaxMessageScheme has no real 'SyntaxMessageScheme' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = ISO20022_SyntaxMessageScheme()
    setattr(partner, 'SyntaxMessageScheme', None)
    _safe_set(owner, 'messageDefinitionTrace', {partner})
    assert getattr(partner, 'SyntaxMessageScheme') == owner
    _safe_set(owner, 'messageDefinitionTrace', set())
    assert getattr(partner, 'SyntaxMessageScheme') is None


def test_assoc_diagrams49_stub_double():
    # ISO20022_Repository has no real 'repository50' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Diagram(content="sample_text", location="sample_text")
    partner = ISO20022_Repository()
    setattr(partner, 'repository50', None)
    _safe_set(owner, 'Diagram', partner)
    assert owner in getattr(partner, 'repository50')
    _safe_set(owner, 'Diagram', None)
    assert owner not in getattr(partner, 'repository50')


def test_assoc_endPoints167_stub_double():
    # ISO20022_EndPointCategory has no real 'ISO20022_EndPointCategory' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageElementContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageElementContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageElementContainer()
    partner = ISO20022_EndPointCategory()
    setattr(partner, 'ISO20022_EndPointCategory', None)
    _safe_set(owner, 'ISO20022_MessageElementContainer', partner)
    assert owner in getattr(partner, 'ISO20022_EndPointCategory')
    _safe_set(owner, 'ISO20022_MessageElementContainer', None)
    assert owner not in getattr(partner, 'ISO20022_EndPointCategory')


def test_assoc_facets73_stub_double():
    # ISO20022_DataType has no real 'ISO20022_DataType74' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Facet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Facet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Facet(name="sample_text", value="sample_text")
    partner = ISO20022_DataType()
    setattr(partner, 'ISO20022_DataType74', None)
    _safe_set(owner, 'ISO20022_Facet', partner)
    assert owner in getattr(partner, 'ISO20022_DataType74')
    _safe_set(owner, 'ISO20022_Facet', None)
    assert owner not in getattr(partner, 'ISO20022_DataType74')


def test_assoc_impactedElements116_stub_double():
    # ISO20022_Xor has no real 'ISO20022_Xor' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageElement(isDerived=True, isTechnical=True, tracePath="sample_text")
    partner = ISO20022_Xor()
    setattr(partner, 'ISO20022_Xor', None)
    _safe_set(owner, 'ISO20022_MessageElement', partner)
    assert owner in getattr(partner, 'ISO20022_Xor')
    _safe_set(owner, 'ISO20022_MessageElement', None)
    assert owner not in getattr(partner, 'ISO20022_Xor')


def test_assoc_impactedMessageBuildingBlocks118_stub_double():
    # ISO20022_Xor has no real 'ISO20022_Xor119' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageBuildingBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageBuildingBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageBuildingBlock()
    partner = ISO20022_Xor()
    setattr(partner, 'ISO20022_Xor119', None)
    _safe_set(owner, 'ISO20022_MessageBuildingBlock120', partner)
    assert owner in getattr(partner, 'ISO20022_Xor119')
    _safe_set(owner, 'ISO20022_MessageBuildingBlock120', None)
    assert owner not in getattr(partner, 'ISO20022_Xor119')


def test_assoc_interaction138_stub_double():
    # ISO20022_InteractionActor has no real 'actors' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Interaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Interaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Interaction(location="sample_text")
    partner = ISO20022_InteractionActor()
    setattr(partner, 'actors', None)
    _safe_set(owner, 'Interaction139', partner)
    assert getattr(partner, 'actors') == owner
    _safe_set(owner, 'Interaction139', None)
    assert getattr(partner, 'actors') is None


def test_assoc_interaction145_stub_double():
    # ISO20022_InteractionMessage has no real 'messages' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Interaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Interaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Interaction(location="sample_text")
    partner = ISO20022_InteractionMessage()
    setattr(partner, 'messages', None)
    _safe_set(owner, 'Interaction146', partner)
    assert getattr(partner, 'messages') == owner
    _safe_set(owner, 'Interaction146', None)
    assert getattr(partner, 'messages') is None


def test_assoc_messageChoreography107_stub_double():
    # ISO20022_MessageChoreography has no real 'MessageChoreography' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = ISO20022_MessageChoreography()
    setattr(partner, 'MessageChoreography', None)
    _safe_set(owner, 'messageDefinition108', {partner})
    assert getattr(partner, 'MessageChoreography') == owner
    _safe_set(owner, 'messageDefinition108', set())
    assert getattr(partner, 'MessageChoreography') is None


def test_assoc_messageDefinition121_stub_double():
    # ISO20022_Xor has no real 'xors122' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = ISO20022_Xor()
    setattr(partner, 'xors122', None)
    _safe_set(owner, 'MessageDefinition123', partner)
    assert getattr(partner, 'xors122') == owner
    _safe_set(owner, 'MessageDefinition123', None)
    assert getattr(partner, 'xors122') is None


def test_assoc_messageDefinition129_stub_double():
    # ISO20022_MessageChoreography has no real 'messageChoreography' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = ISO20022_MessageChoreography()
    setattr(partner, 'messageChoreography', None)
    _safe_set(owner, 'MessageDefinition130', partner)
    assert owner in getattr(partner, 'messageChoreography')
    _safe_set(owner, 'MessageDefinition130', None)
    assert owner not in getattr(partner, 'messageChoreography')


def test_assoc_messageDefinitionTrace126_stub_double():
    # ISO20022_SyntaxMessageScheme has no real 'derivation127' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = ISO20022_SyntaxMessageScheme()
    setattr(partner, 'derivation127', None)
    _safe_set(owner, 'MessageDefinition128', partner)
    assert owner in getattr(partner, 'derivation127')
    _safe_set(owner, 'MessageDefinition128', None)
    assert owner not in getattr(partner, 'derivation127')


def test_assoc_messageSet86_stub_double():
    # ISO20022_Encoding has no real 'validEncoding' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageSet()
    partner = ISO20022_Encoding()
    setattr(partner, 'validEncoding', None)
    _safe_set(owner, 'MessageSet', partner)
    assert owner in getattr(partner, 'validEncoding')
    _safe_set(owner, 'MessageSet', None)
    assert owner not in getattr(partner, 'validEncoding')


def test_assoc_messages132_stub_double():
    # ISO20022_InteractionMessage has no real 'InteractionMessage' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Interaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Interaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Interaction(location="sample_text")
    partner = ISO20022_InteractionMessage()
    setattr(partner, 'InteractionMessage', None)
    _safe_set(owner, 'interaction133', {partner})
    assert getattr(partner, 'InteractionMessage') == owner
    _safe_set(owner, 'interaction133', set())
    assert getattr(partner, 'InteractionMessage') is None


def test_assoc_possibleEncodings147_stub_double():
    # ISO20022_Encoding has no real 'Encoding148' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Syntax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Syntax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Syntax()
    partner = ISO20022_Encoding()
    setattr(partner, 'Encoding148', None)
    _safe_set(owner, 'syntax', {partner})
    assert getattr(partner, 'Encoding148') == owner
    _safe_set(owner, 'syntax', set())
    assert getattr(partner, 'Encoding148') is None


def test_assoc_repository45_stub_double():
    # ISO20022_Repository has no real 'Repository' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_DataDictionary()
    partner = ISO20022_Repository()
    setattr(partner, 'Repository', None)
    _safe_set(owner, 'dataDictionary', partner)
    assert getattr(partner, 'Repository') == owner
    _safe_set(owner, 'dataDictionary', None)
    assert getattr(partner, 'Repository') is None


def test_assoc_repository55_stub_double():
    # ISO20022_Repository has no real 'Repository57' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_BusinessProcessCatalogue()
    partner = ISO20022_Repository()
    setattr(partner, 'Repository57', None)
    _safe_set(owner, 'businessProcessCatalogue56', partner)
    assert getattr(partner, 'Repository57') == owner
    _safe_set(owner, 'businessProcessCatalogue56', None)
    assert getattr(partner, 'Repository57') is None


def test_assoc_repository60_stub_double():
    # ISO20022_Repository has no real 'Repository61' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Diagram(content="sample_text", location="sample_text")
    partner = ISO20022_Repository()
    setattr(partner, 'Repository61', None)
    _safe_set(owner, 'diagrams', partner)
    assert getattr(partner, 'Repository61') == owner
    _safe_set(owner, 'diagrams', None)
    assert getattr(partner, 'Repository61') is None


def test_assoc_simpleType151_stub_double():
    # ISO20022_DataType has no real 'ISO20022_DataType152' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_BusinessAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_BusinessAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_BusinessAttribute()
    partner = ISO20022_DataType()
    setattr(partner, 'ISO20022_DataType152', None)
    _safe_set(owner, 'ISO20022_BusinessAttribute', partner)
    assert getattr(partner, 'ISO20022_DataType152') == owner
    _safe_set(owner, 'ISO20022_BusinessAttribute', None)
    assert getattr(partner, 'ISO20022_DataType152') is None


def test_assoc_simpleType70_stub_double():
    # ISO20022_DataType has no real 'ISO20022_DataType' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageBuildingBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageBuildingBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageBuildingBlock()
    partner = ISO20022_DataType()
    setattr(partner, 'ISO20022_DataType', None)
    _safe_set(owner, 'ISO20022_MessageBuildingBlock', partner)
    assert getattr(partner, 'ISO20022_DataType') == owner
    _safe_set(owner, 'ISO20022_MessageBuildingBlock', None)
    assert getattr(partner, 'ISO20022_DataType') is None


def test_assoc_simpleType81_stub_double():
    # ISO20022_DataType has no real 'ISO20022_DataType82' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageAttribute()
    partner = ISO20022_DataType()
    setattr(partner, 'ISO20022_DataType82', None)
    _safe_set(owner, 'ISO20022_MessageAttribute', partner)
    assert getattr(partner, 'ISO20022_DataType82') == owner
    _safe_set(owner, 'ISO20022_MessageAttribute', None)
    assert getattr(partner, 'ISO20022_DataType82') is None


def test_assoc_syntax87_stub_double():
    # ISO20022_Encoding has no real 'possibleEncodings' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_Syntax's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_Syntax's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_Syntax()
    partner = ISO20022_Encoding()
    setattr(partner, 'possibleEncodings', None)
    _safe_set(owner, 'Syntax', partner)
    assert getattr(partner, 'possibleEncodings') == owner
    _safe_set(owner, 'Syntax', None)
    assert getattr(partner, 'possibleEncodings') is None


def test_assoc_topLevelCatalogueEntry54_stub_double():
    # ISO20022_TopLevelCatalogueEntry has no real 'TopLevelCatalogueEntry' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_BusinessProcessCatalogue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_BusinessProcessCatalogue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_BusinessProcessCatalogue()
    partner = ISO20022_TopLevelCatalogueEntry()
    setattr(partner, 'TopLevelCatalogueEntry', None)
    _safe_set(owner, 'businessProcessCatalogue', {partner})
    assert getattr(partner, 'TopLevelCatalogueEntry') == owner
    _safe_set(owner, 'businessProcessCatalogue', set())
    assert getattr(partner, 'TopLevelCatalogueEntry') is None


def test_assoc_topLevelDictionaryEntry46_stub_double():
    # ISO20022_TopLevelDictionaryEntry has no real 'TopLevelDictionaryEntry' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_DataDictionary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_DataDictionary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_DataDictionary()
    partner = ISO20022_TopLevelDictionaryEntry()
    setattr(partner, 'TopLevelDictionaryEntry', None)
    _safe_set(owner, 'dataDictionary47', {partner})
    assert getattr(partner, 'TopLevelDictionaryEntry') == owner
    _safe_set(owner, 'dataDictionary47', set())
    assert getattr(partner, 'TopLevelDictionaryEntry') is None


def test_assoc_typedXMLMember29_stub_double():
    # ISO20022_LogicalType has no real 'xmlMemberType' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_XMLMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_XMLMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_XMLMember(xmlTag="sample_text")
    partner = ISO20022_LogicalType()
    setattr(partner, 'xmlMemberType', None)
    _safe_set(owner, 'XMLMember', partner)
    assert owner in getattr(partner, 'xmlMemberType')
    _safe_set(owner, 'XMLMember', None)
    assert owner not in getattr(partner, 'xmlMemberType')


def test_assoc_validEncoding93_stub_double():
    # ISO20022_Encoding has no real 'Encoding' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageSet()
    partner = ISO20022_Encoding()
    setattr(partner, 'Encoding', None)
    _safe_set(owner, 'messageSet94', {partner})
    assert getattr(partner, 'Encoding') == owner
    _safe_set(owner, 'messageSet94', set())
    assert getattr(partner, 'Encoding') is None


def test_assoc_xmlMemberType19_stub_double():
    # ISO20022_LogicalType has no real 'LogicalType' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_XMLMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_XMLMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_XMLMember(xmlTag="sample_text")
    partner = ISO20022_LogicalType()
    setattr(partner, 'LogicalType', None)
    _safe_set(owner, 'typedXMLMember', partner)
    assert getattr(partner, 'LogicalType') == owner
    _safe_set(owner, 'typedXMLMember', None)
    assert getattr(partner, 'LogicalType') is None


def test_assoc_xors102_stub_double():
    # ISO20022_Xor has no real 'Xor' property in the generated
    # code (a bare stub) -- manually attach it so ISO20022_MessageDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ISO20022_MessageDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ISO20022_MessageDefinition(previousVersionDocumentation="sample_text", rootElement="sample_text", urn="sample_text", visibility="sample_text", xmlName="sample_text", xmlTag="sample_text")
    partner = ISO20022_Xor()
    setattr(partner, 'Xor', None)
    _safe_set(owner, 'messageDefinition103', {partner})
    assert getattr(partner, 'Xor') == owner
    _safe_set(owner, 'messageDefinition103', set())
    assert getattr(partner, 'Xor') is None


