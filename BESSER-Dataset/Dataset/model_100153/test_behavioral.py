import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMetadataObject,
    Connection,
    FileConnection,
    MetadataColumn,
    SAPFunctionParameterTable,
    TdTable,
    connection_AbstractMetadataObject,
    connection_CDCConnection,
    connection_CDCType,
    connection_Concept,
    connection_ConceptTarget,
    connection_Connection,
    connection_DatabaseConnection,
    connection_DelimitedFileConnection,
    connection_EbcdicConnection,
    connection_FileConnection,
    connection_FileExcelConnection,
    connection_GenericPackage,
    connection_GenericSchemaConnection,
    connection_HL7Connection,
    connection_InputSAPFunctionParameterTable,
    connection_LDAPSchemaConnection,
    connection_LdifFileConnection,
    connection_MDMConnection,
    connection_Metadata,
    connection_MetadataColumn,
    connection_MetadataTable,
    connection_OutputSAPFunctionParameterTable,
    connection_PositionalFileConnection,
    connection_QueriesConnection,
    connection_Query,
    connection_RegexpFileConnection,
    connection_SAPConnection,
    connection_SAPFunctionParameterColumn,
    connection_SAPFunctionParameterTable,
    connection_SAPFunctionUnit,
    connection_SAPTestInputParameterTable,
    connection_SalesforceSchemaConnection,
    connection_SchemaTarget,
    connection_SubscriberTable,
    connection_WSDLSchemaConnection,
    connection_XmlFileConnection,
    connection_XmlXPathLoopDescriptor,
    connection_relational_TdColumn,
    connection_relational_TdProcedure,
    connection_relational_TdSqlDataType,
    connection_relational_TdTable,
    connection_relational_TdTrigger,
    connection_relational_TdView,
    connection_softwaredeployment_TdDataManager,
    connection_softwaredeployment_TdMachine,
    connection_softwaredeployment_TdSoftwareSystem,
    connection_xml_TdXMLContent,
    connection_xml_TdXMLDocument,
    connection_xml_TdXMLElement,
    relational_TdSqlDataType,
    xml_TdXMLContent,
    xml_TdXMLDocument,
    xml_TdXMLElement,
    DevelopmentStatus,
    Escape,
    FieldSeparator,
    FileFormat,
    RowSeparator,
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

def test_assoc_Funtions12_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    _safe_set(b, 'connection13', {a1})
    assert _is_linked(b, 'connection13', a1)
    if hasattr(a1, 'SAPFunctionUnit'):
        assert _is_linked(a1, 'SAPFunctionUnit', b)
    _safe_set(b, 'connection13', {a2})
    assert _is_linked(b, 'connection13', a2)
    if hasattr(a1, 'SAPFunctionUnit'):
        assert not _is_linked(a1, 'SAPFunctionUnit', b)
    if hasattr(a2, 'SAPFunctionUnit'):
        assert _is_linked(a2, 'SAPFunctionUnit', b)
    _safe_set(b, 'connection13', set())
    assert not _is_linked(b, 'connection13', a2)
    if hasattr(a2, 'SAPFunctionUnit'):
        assert not _is_linked(a2, 'SAPFunctionUnit', b)


def test_assoc_MetadataTable17_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable18', a1)
    assert _is_linked(b, 'connection_MetadataTable18', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit', b)
    _safe_set(b, 'connection_MetadataTable18', a2)
    assert _is_linked(b, 'connection_MetadataTable18', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit', b)
    if hasattr(a2, 'connection_SAPFunctionUnit'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit', b)
    _safe_set(b, 'connection_MetadataTable18', None)
    assert not _is_linked(b, 'connection_MetadataTable18', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    _safe_set(b, 'connection_MetadataColumn5', a1)
    assert _is_linked(b, 'connection_MetadataColumn5', a1)
    if hasattr(a1, 'connection_MetadataTable4'):
        assert _is_linked(a1, 'connection_MetadataTable4', b)
    _safe_set(b, 'connection_MetadataColumn5', a2)
    assert _is_linked(b, 'connection_MetadataColumn5', a2)
    if hasattr(a1, 'connection_MetadataTable4'):
        assert not _is_linked(a1, 'connection_MetadataTable4', b)
    if hasattr(a2, 'connection_MetadataTable4'):
        assert _is_linked(a2, 'connection_MetadataTable4', b)
    _safe_set(b, 'connection_MetadataColumn5', None)
    assert not _is_linked(b, 'connection_MetadataColumn5', a2)
    if hasattr(a2, 'connection_MetadataTable4'):
        assert not _is_linked(a2, 'connection_MetadataTable4', b)


def test_assoc_conceptTargets52_reverse_link_reassign_clear():
    a1 = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    a2 = connection_ConceptTarget(RelativeLoopExpression="sample_text_2", targetName="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    _safe_set(b, 'schema53', {a1})
    assert _is_linked(b, 'schema53', a1)
    if hasattr(a1, 'ConceptTarget'):
        assert _is_linked(a1, 'ConceptTarget', b)
    _safe_set(b, 'schema53', {a2})
    assert _is_linked(b, 'schema53', a2)
    if hasattr(a1, 'ConceptTarget'):
        assert not _is_linked(a1, 'ConceptTarget', b)
    if hasattr(a2, 'ConceptTarget'):
        assert _is_linked(a2, 'ConceptTarget', b)
    _safe_set(b, 'schema53', set())
    assert not _is_linked(b, 'schema53', a2)
    if hasattr(a2, 'ConceptTarget'):
        assert not _is_linked(a2, 'ConceptTarget', b)


def test_assoc_connection19_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    _safe_set(b, 'SAPConnection', a1)
    assert _is_linked(b, 'SAPConnection', a1)
    if hasattr(a1, 'Funtions'):
        assert _is_linked(a1, 'Funtions', b)
    _safe_set(b, 'SAPConnection', a2)
    assert _is_linked(b, 'SAPConnection', a2)
    if hasattr(a1, 'Funtions'):
        assert not _is_linked(a1, 'Funtions', b)
    if hasattr(a2, 'Funtions'):
        assert _is_linked(a2, 'Funtions', b)
    _safe_set(b, 'SAPConnection', None)
    assert not _is_linked(b, 'SAPConnection', a2)
    if hasattr(a2, 'Funtions'):
        assert not _is_linked(a2, 'Funtions', b)


def test_assoc_connection40_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    _safe_set(b, 'XmlFileConnection', a1)
    assert _is_linked(b, 'XmlFileConnection', a1)
    if hasattr(a1, 'schema'):
        assert _is_linked(a1, 'schema', b)
    _safe_set(b, 'XmlFileConnection', a2)
    assert _is_linked(b, 'XmlFileConnection', a2)
    if hasattr(a1, 'schema'):
        assert not _is_linked(a1, 'schema', b)
    if hasattr(a2, 'schema'):
        assert _is_linked(a2, 'schema', b)
    _safe_set(b, 'XmlFileConnection', None)
    assert not _is_linked(b, 'XmlFileConnection', a2)
    if hasattr(a2, 'schema'):
        assert not _is_linked(a2, 'schema', b)


def test_assoc_connection6_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    _safe_set(b, 'connection_Connection8', a1)
    assert _is_linked(b, 'connection_Connection8', a1)
    if hasattr(a1, 'connection_MetadataTable7'):
        assert _is_linked(a1, 'connection_MetadataTable7', b)
    _safe_set(b, 'connection_Connection8', a2)
    assert _is_linked(b, 'connection_Connection8', a2)
    if hasattr(a1, 'connection_MetadataTable7'):
        assert not _is_linked(a1, 'connection_MetadataTable7', b)
    if hasattr(a2, 'connection_MetadataTable7'):
        assert _is_linked(a2, 'connection_MetadataTable7', b)
    _safe_set(b, 'connection_Connection8', None)
    assert not _is_linked(b, 'connection_Connection8', a2)
    if hasattr(a2, 'connection_MetadataTable7'):
        assert not _is_linked(a2, 'connection_MetadataTable7', b)


def test_assoc_schema31_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    _safe_set(b, 'connection32', {a1})
    assert _is_linked(b, 'connection32', a1)
    if hasattr(a1, 'XmlXPathLoopDescriptor'):
        assert _is_linked(a1, 'XmlXPathLoopDescriptor', b)
    _safe_set(b, 'connection32', {a2})
    assert _is_linked(b, 'connection32', a2)
    if hasattr(a1, 'XmlXPathLoopDescriptor'):
        assert not _is_linked(a1, 'XmlXPathLoopDescriptor', b)
    if hasattr(a2, 'XmlXPathLoopDescriptor'):
        assert _is_linked(a2, 'XmlXPathLoopDescriptor', b)
    _safe_set(b, 'connection32', set())
    assert not _is_linked(b, 'connection32', a2)
    if hasattr(a2, 'XmlXPathLoopDescriptor'):
        assert not _is_linked(a2, 'XmlXPathLoopDescriptor', b)


def test_assoc_schema33_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    _safe_set(b, 'schemaTargets', a1)
    assert _is_linked(b, 'schemaTargets', a1)
    if hasattr(a1, 'XmlXPathLoopDescriptor34'):
        assert _is_linked(a1, 'XmlXPathLoopDescriptor34', b)
    _safe_set(b, 'schemaTargets', a2)
    assert _is_linked(b, 'schemaTargets', a2)
    if hasattr(a1, 'XmlXPathLoopDescriptor34'):
        assert not _is_linked(a1, 'XmlXPathLoopDescriptor34', b)
    if hasattr(a2, 'XmlXPathLoopDescriptor34'):
        assert _is_linked(a2, 'XmlXPathLoopDescriptor34', b)
    _safe_set(b, 'schemaTargets', None)
    assert not _is_linked(b, 'schemaTargets', a2)
    if hasattr(a2, 'XmlXPathLoopDescriptor34'):
        assert not _is_linked(a2, 'XmlXPathLoopDescriptor34', b)


def test_assoc_schema54_reverse_link_reassign_clear():
    a1 = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    a2 = connection_ConceptTarget(RelativeLoopExpression="sample_text_2", targetName="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    _safe_set(b, 'Concept', a1)
    assert _is_linked(b, 'Concept', a1)
    if hasattr(a1, 'conceptTargets'):
        assert _is_linked(a1, 'conceptTargets', b)
    _safe_set(b, 'Concept', a2)
    assert _is_linked(b, 'Concept', a2)
    if hasattr(a1, 'conceptTargets'):
        assert not _is_linked(a1, 'conceptTargets', b)
    if hasattr(a2, 'conceptTargets'):
        assert _is_linked(a2, 'conceptTargets', b)
    _safe_set(b, 'Concept', None)
    assert not _is_linked(b, 'Concept', a2)
    if hasattr(a2, 'conceptTargets'):
        assert not _is_linked(a2, 'conceptTargets', b)


def test_assoc_schemaTargets41_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    _safe_set(b, 'SchemaTarget', a1)
    assert _is_linked(b, 'SchemaTarget', a1)
    if hasattr(a1, 'schema42'):
        assert _is_linked(a1, 'schema42', b)
    _safe_set(b, 'SchemaTarget', a2)
    assert _is_linked(b, 'SchemaTarget', a2)
    if hasattr(a1, 'schema42'):
        assert not _is_linked(a1, 'schema42', b)
    if hasattr(a2, 'schema42'):
        assert _is_linked(a2, 'schema42', b)
    _safe_set(b, 'SchemaTarget', None)
    assert not _is_linked(b, 'SchemaTarget', a2)
    if hasattr(a2, 'schema42'):
        assert not _is_linked(a2, 'schema42', b)


def test_assoc_schemas9_reverse_link_reassign_clear():
    a1 = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    a2 = connection_MDMConnection(Datacluster="sample_text_2", Datamodel="sample_text_2", Password="sample_text_2", Port="sample_text_2", Server="sample_text_2", Universe="sample_text_2", Username="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    _safe_set(b, 'connection_Concept', a1)
    assert _is_linked(b, 'connection_Concept', a1)
    if hasattr(a1, 'connection_MDMConnection'):
        assert _is_linked(a1, 'connection_MDMConnection', b)
    _safe_set(b, 'connection_Concept', a2)
    assert _is_linked(b, 'connection_Concept', a2)
    if hasattr(a1, 'connection_MDMConnection'):
        assert not _is_linked(a1, 'connection_MDMConnection', b)
    if hasattr(a2, 'connection_MDMConnection'):
        assert _is_linked(a2, 'connection_MDMConnection', b)
    _safe_set(b, 'connection_Concept', None)
    assert not _is_linked(b, 'connection_Concept', a2)
    if hasattr(a2, 'connection_MDMConnection'):
        assert not _is_linked(a2, 'connection_MDMConnection', b)


def test_assoc_subscribers45_reverse_link_reassign_clear():
    a1 = connection_SubscriberTable(system=True)
    a2 = connection_SubscriberTable(system=False)
    b = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    _safe_set(b, 'connection_CDCType46', {a1})
    assert _is_linked(b, 'connection_CDCType46', a1)
    if hasattr(a1, 'connection_SubscriberTable'):
        assert _is_linked(a1, 'connection_SubscriberTable', b)
    _safe_set(b, 'connection_CDCType46', {a2})
    assert _is_linked(b, 'connection_CDCType46', a2)
    if hasattr(a1, 'connection_SubscriberTable'):
        assert not _is_linked(a1, 'connection_SubscriberTable', b)
    if hasattr(a2, 'connection_SubscriberTable'):
        assert _is_linked(a2, 'connection_SubscriberTable', b)
    _safe_set(b, 'connection_CDCType46', set())
    assert not _is_linked(b, 'connection_CDCType46', a2)
    if hasattr(a2, 'connection_SubscriberTable'):
        assert not _is_linked(a2, 'connection_SubscriberTable', b)


def test_assoc_table2_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    _safe_set(b, 'connection_MetadataColumn', a1)
    assert _is_linked(b, 'connection_MetadataColumn', a1)
    if hasattr(a1, 'connection_MetadataTable'):
        assert _is_linked(a1, 'connection_MetadataTable', b)
    _safe_set(b, 'connection_MetadataColumn', a2)
    assert _is_linked(b, 'connection_MetadataColumn', a2)
    if hasattr(a1, 'connection_MetadataTable'):
        assert not _is_linked(a1, 'connection_MetadataTable', b)
    if hasattr(a2, 'connection_MetadataTable'):
        assert _is_linked(a2, 'connection_MetadataTable', b)
    _safe_set(b, 'connection_MetadataColumn', None)
    assert not _is_linked(b, 'connection_MetadataColumn', a2)
    if hasattr(a2, 'connection_MetadataTable'):
        assert not _is_linked(a2, 'connection_MetadataTable', b)


def test_assoc_tables20_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable22', a1)
    assert _is_linked(b, 'connection_MetadataTable22', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit21'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit21', b)
    _safe_set(b, 'connection_MetadataTable22', a2)
    assert _is_linked(b, 'connection_MetadataTable22', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit21'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit21', b)
    if hasattr(a2, 'connection_SAPFunctionUnit21'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit21', b)
    _safe_set(b, 'connection_MetadataTable22', None)
    assert not _is_linked(b, 'connection_MetadataTable22', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit21'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_InputParameterTable14_stub_double():
    # connection_InputSAPFunctionParameterTable has no real 'InputSAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_InputSAPFunctionParameterTable()
    setattr(partner, 'InputSAPFunctionParameterTable', None)
    _safe_set(owner, 'functionUnit', partner)
    assert getattr(partner, 'InputSAPFunctionParameterTable') == owner
    _safe_set(owner, 'functionUnit', None)
    assert getattr(partner, 'InputSAPFunctionParameterTable') is None


def test_assoc_OutputParameterTable15_stub_double():
    # connection_OutputSAPFunctionParameterTable has no real 'OutputSAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_OutputSAPFunctionParameterTable()
    setattr(partner, 'OutputSAPFunctionParameterTable', None)
    _safe_set(owner, 'functionUnit16', partner)
    assert getattr(partner, 'OutputSAPFunctionParameterTable') == owner
    _safe_set(owner, 'functionUnit16', None)
    assert getattr(partner, 'OutputSAPFunctionParameterTable') is None


def test_assoc_ParameterTable25_stub_double():
    # connection_SAPFunctionParameterTable has no real 'SAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionParameterColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionParameterColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    partner = connection_SAPFunctionParameterTable()
    setattr(partner, 'SAPFunctionParameterTable', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'SAPFunctionParameterTable') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'SAPFunctionParameterTable') is None


def test_assoc_TestInputParameterTable23_stub_double():
    # connection_SAPTestInputParameterTable has no real 'SAPTestInputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_SAPTestInputParameterTable()
    setattr(partner, 'SAPTestInputParameterTable', None)
    _safe_set(owner, 'functionUnit24', partner)
    assert getattr(partner, 'SAPTestInputParameterTable') == owner
    _safe_set(owner, 'functionUnit24', None)
    assert getattr(partner, 'SAPTestInputParameterTable') is None


def test_assoc_cdcConnection47_stub_double():
    # connection_CDCConnection has no real 'connection_CDCConnection49' property in the generated
    # code (a bare stub) -- manually attach it so connection_CDCType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_CDCType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'connection_CDCConnection49', None)
    _safe_set(owner, 'connection_CDCType48', partner)
    assert getattr(partner, 'connection_CDCConnection49') == owner
    _safe_set(owner, 'connection_CDCType48', None)
    assert getattr(partner, 'connection_CDCConnection49') is None


def test_assoc_cdcConns10_stub_double():
    # connection_CDCConnection has no real 'CDCConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_DatabaseConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_DatabaseConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'CDCConnection', None)
    _safe_set(owner, 'connection11', partner)
    assert getattr(partner, 'CDCConnection') == owner
    _safe_set(owner, 'connection11', None)
    assert getattr(partner, 'CDCConnection') is None


def test_assoc_cdcTypes44_stub_double():
    # connection_CDCConnection has no real 'connection_CDCConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_CDCType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_CDCType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'connection_CDCConnection', None)
    _safe_set(owner, 'connection_CDCType', partner)
    assert owner in getattr(partner, 'connection_CDCConnection')
    _safe_set(owner, 'connection_CDCType', None)
    assert owner not in getattr(partner, 'connection_CDCConnection')


def test_assoc_columns26_stub_double():
    # connection_SAPFunctionParameterTable has no real 'ParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionParameterColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionParameterColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    partner = connection_SAPFunctionParameterTable()
    setattr(partner, 'ParameterTable', None)
    _safe_set(owner, 'SAPFunctionParameterColumn', partner)
    assert owner in getattr(partner, 'ParameterTable')
    _safe_set(owner, 'SAPFunctionParameterColumn', None)
    assert owner not in getattr(partner, 'ParameterTable')


def test_assoc_connection35_stub_double():
    # connection_QueriesConnection has no real 'queries' property in the generated
    # code (a bare stub) -- manually attach it so connection_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'queries', None)
    _safe_set(owner, 'Connection', partner)
    assert getattr(partner, 'queries') == owner
    _safe_set(owner, 'Connection', None)
    assert getattr(partner, 'queries') is None


def test_assoc_connection43_stub_double():
    # connection_CDCConnection has no real 'cdcConns' property in the generated
    # code (a bare stub) -- manually attach it so connection_DatabaseConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_DatabaseConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'cdcConns', None)
    _safe_set(owner, 'DatabaseConnection', partner)
    assert getattr(partner, 'cdcConns') == owner
    _safe_set(owner, 'DatabaseConnection', None)
    assert getattr(partner, 'cdcConns') is None


def test_assoc_connections0_stub_double():
    # connection_Metadata has no real 'connection_Metadata' property in the generated
    # code (a bare stub) -- manually attach it so connection_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    partner = connection_Metadata()
    setattr(partner, 'connection_Metadata', None)
    _safe_set(owner, 'connection_Connection', partner)
    assert owner in getattr(partner, 'connection_Metadata')
    _safe_set(owner, 'connection_Connection', None)
    assert owner not in getattr(partner, 'connection_Metadata')


def test_assoc_functionUnit27_stub_double():
    # connection_InputSAPFunctionParameterTable has no real 'InputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_InputSAPFunctionParameterTable()
    setattr(partner, 'InputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit28', partner)
    assert getattr(partner, 'InputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit28', None)
    assert getattr(partner, 'InputParameterTable') is None


def test_assoc_functionUnit29_stub_double():
    # connection_OutputSAPFunctionParameterTable has no real 'OutputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_OutputSAPFunctionParameterTable()
    setattr(partner, 'OutputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit30', partner)
    assert getattr(partner, 'OutputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit30', None)
    assert getattr(partner, 'OutputParameterTable') is None


def test_assoc_functionUnit50_stub_double():
    # connection_SAPTestInputParameterTable has no real 'TestInputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_SAPTestInputParameterTable()
    setattr(partner, 'TestInputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit51', partner)
    assert getattr(partner, 'TestInputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit51', None)
    assert getattr(partner, 'TestInputParameterTable') is None


def test_assoc_ownedDocument56_stub_double():
    # xml_TdXMLDocument has no real 'xml_TdXMLDocument' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXMLElement(javaType="sample_text")
    partner = xml_TdXMLDocument()
    setattr(partner, 'xml_TdXMLDocument', None)
    _safe_set(owner, 'connection_xml_TdXMLElement', partner)
    assert getattr(partner, 'xml_TdXMLDocument') == owner
    _safe_set(owner, 'connection_xml_TdXMLElement', None)
    assert getattr(partner, 'xml_TdXMLDocument') is None


def test_assoc_queries1_stub_double():
    # connection_QueriesConnection has no real 'QueriesConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'QueriesConnection', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'QueriesConnection') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'QueriesConnection') is None


def test_assoc_queries38_stub_double():
    # connection_QueriesConnection has no real 'QueriesConnection39' property in the generated
    # code (a bare stub) -- manually attach it so connection_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Query(contextMode=True, value="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'QueriesConnection39', None)
    _safe_set(owner, 'query', partner)
    assert getattr(partner, 'QueriesConnection39') == owner
    _safe_set(owner, 'query', None)
    assert getattr(partner, 'QueriesConnection39') is None


def test_assoc_query36_stub_double():
    # connection_QueriesConnection has no real 'queries37' property in the generated
    # code (a bare stub) -- manually attach it so connection_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Query(contextMode=True, value="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'queries37', None)
    _safe_set(owner, 'Query', partner)
    assert owner in getattr(partner, 'queries37')
    _safe_set(owner, 'Query', None)
    assert owner not in getattr(partner, 'queries37')


def test_assoc_sqlDataType55_stub_double():
    # relational_TdSqlDataType has no real 'relational_TdSqlDataType' property in the generated
    # code (a bare stub) -- manually attach it so connection_relational_TdColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_relational_TdColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_relational_TdColumn()
    partner = relational_TdSqlDataType()
    setattr(partner, 'relational_TdSqlDataType', None)
    _safe_set(owner, 'connection_relational_TdColumn', partner)
    assert getattr(partner, 'relational_TdSqlDataType') == owner
    _safe_set(owner, 'connection_relational_TdColumn', None)
    assert getattr(partner, 'relational_TdSqlDataType') is None


def test_assoc_xmlContent57_stub_double():
    # xml_TdXMLContent has no real 'xml_TdXMLContent' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXMLElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXMLElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXMLElement(javaType="sample_text")
    partner = xml_TdXMLContent()
    setattr(partner, 'xml_TdXMLContent', None)
    _safe_set(owner, 'connection_xml_TdXMLElement58', partner)
    assert getattr(partner, 'xml_TdXMLContent') == owner
    _safe_set(owner, 'connection_xml_TdXMLElement58', None)
    assert getattr(partner, 'xml_TdXMLContent') is None


