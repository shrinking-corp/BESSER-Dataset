from python_code import iso20022_AbstractDateTimeConcept

def test_iso20022_AbstractDateTimeConcept___init__():
    assert iso20022_AbstractDateTimeConcept.__init__(iso20022_AbstractDateTimeConcept('', '', '', '', ''), '', '', '', '', '') == None


from python_code import iso20022_Binary

def test_iso20022_Binary___init__():
    assert iso20022_Binary.__init__(iso20022_Binary('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import iso20022_Boolean

def test_iso20022_Boolean___init__():
    assert iso20022_Boolean.__init__(iso20022_Boolean(''), '') == None


from python_code import iso20022_BusinessProcessCatalogue
from python_code import iso20022_Repository
from python_code import iso20022_TopLevelCatalogueEntry

def test_iso20022_BusinessProcessCatalogue___init__():
    assert iso20022_BusinessProcessCatalogue.__init__(iso20022_BusinessProcessCatalogue(BusinessProcessCatalogue=iso20022_TopLevelCatalogueEntry(), businessProcessCatalogue=iso20022_Repository(), businessProcessCatalogue36=set(), BusinessProcessCatalogue40=iso20022_Repository()), BusinessProcessCatalogue=iso20022_TopLevelCatalogueEntry(), businessProcessCatalogue=iso20022_Repository(), businessProcessCatalogue36=set(), BusinessProcessCatalogue40=iso20022_Repository()) == None

def test_iso20022_BusinessProcessCatalogue_EntriesHaveUniqueName():
    assert iso20022_BusinessProcessCatalogue.EntriesHaveUniqueName(iso20022_BusinessProcessCatalogue(BusinessProcessCatalogue=iso20022_TopLevelCatalogueEntry(), businessProcessCatalogue=iso20022_Repository(), businessProcessCatalogue36=set(), BusinessProcessCatalogue40=iso20022_Repository()), 0, '\x00\x00') == None


from python_code import iso20022_ChoiceComponent

def test_iso20022_ChoiceComponent___init__():
    assert iso20022_ChoiceComponent.__init__(iso20022_ChoiceComponent()) == None

def test_iso20022_ChoiceComponent_AtLeastOneProperty():
    assert iso20022_ChoiceComponent.AtLeastOneProperty(iso20022_ChoiceComponent(), '', '') == None


from python_code import iso20022_DataDictionary
from python_code import iso20022_Repository
from python_code import iso20022_TopLevelDictionaryEntry

def test_iso20022_DataDictionary___init__():
    assert iso20022_DataDictionary.__init__(iso20022_DataDictionary(DataDictionary=iso20022_Repository(), dataDictionary=set(), dataDictionary43=iso20022_Repository(), DataDictionary46=iso20022_TopLevelDictionaryEntry()), DataDictionary=iso20022_Repository(), dataDictionary=set(), dataDictionary43=iso20022_Repository(), DataDictionary46=iso20022_TopLevelDictionaryEntry()) == None

def test_iso20022_DataDictionary_EntriesHaveUniqueName():
    assert iso20022_DataDictionary.EntriesHaveUniqueName(iso20022_DataDictionary(DataDictionary=iso20022_Repository(), dataDictionary=set(), dataDictionary43=iso20022_Repository(), DataDictionary46=iso20022_TopLevelDictionaryEntry()), 0, '\x00\x00') == None


from python_code import iso20022_Decimal

def test_iso20022_Decimal___init__():
    assert iso20022_Decimal.__init__(iso20022_Decimal('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import iso20022_ExternalSchema

def test_iso20022_ExternalSchema___init__():
    assert iso20022_ExternalSchema.__init__(iso20022_ExternalSchema('', '\x00'), '\x00\x00', '') == None


from python_code import iso20022_IdentifierSet

def test_iso20022_IdentifierSet___init__():
    assert iso20022_IdentifierSet.__init__(iso20022_IdentifierSet(''), '') == None


from python_code import iso20022_Indicator

def test_iso20022_Indicator___init__():
    assert iso20022_Indicator.__init__(iso20022_Indicator('', '\x00'), '\x00\x00', '') == None


from python_code import iso20022_LogicalType
from python_code import iso20022_MessageConstruct

def test_iso20022_MessageConstruct___init__():
    assert iso20022_MessageConstruct.__init__(iso20022_MessageConstruct('', iso20022_MessageConstruct=iso20022_LogicalType()), '', iso20022_MessageConstruct=iso20022_LogicalType()) == None


from python_code import iso20022_MultiplicityEntity

def test_iso20022_MultiplicityEntity___init__():
    assert iso20022_MultiplicityEntity.__init__(iso20022_MultiplicityEntity('', '\x00'), '\x00\x00', '') == None


from python_code import iso20022_Quantity

def test_iso20022_Quantity___init__():
    assert iso20022_Quantity.__init__(iso20022_Quantity(''), '') == None


from python_code import iso20022_Rate

def test_iso20022_Rate___init__():
    assert iso20022_Rate.__init__(iso20022_Rate('', '\x00'), '\x00\x00', '') == None


from python_code import iso20022_SchemaType

def test_iso20022_SchemaType___init__():
    assert iso20022_SchemaType.__init__(iso20022_SchemaType(''), '') == None


from python_code import iso20022_String

def test_iso20022_String___init__():
    assert iso20022_String.__init__(iso20022_String('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import iso20022_MessageInstance
from python_code import iso20022_MessagingEndpoint
from python_code import iso20022_TransportMessage

def test_iso20022_TransportMessage___init__():
    assert iso20022_TransportMessage.__init__(iso20022_TransportMessage(transportMessage=iso20022_MessageInstance(), receivedMessage=set(), TransportMessage=iso20022_MessagingEndpoint(), TransportMessage11=iso20022_MessagingEndpoint(), sentMessage=iso20022_MessagingEndpoint(), TransportMessage24=iso20022_MessageInstance()), transportMessage=iso20022_MessageInstance(), receivedMessage=set(), TransportMessage=iso20022_MessagingEndpoint(), TransportMessage11=iso20022_MessagingEndpoint(), sentMessage=iso20022_MessagingEndpoint(), TransportMessage24=iso20022_MessageInstance()) == None

def test_iso20022_TransportMessage_sameMessageTransportSystem():
    assert iso20022_TransportMessage.sameMessageTransportSystem(iso20022_TransportMessage(transportMessage=iso20022_MessageInstance(), receivedMessage=set(), TransportMessage=iso20022_MessagingEndpoint(), TransportMessage11=iso20022_MessagingEndpoint(), sentMessage=iso20022_MessagingEndpoint(), TransportMessage24=iso20022_MessageInstance()), 0, '\x00\x00') == None


from python_code import iso20022_UserDefined

def test_iso20022_UserDefined___init__():
    assert iso20022_UserDefined.__init__(iso20022_UserDefined('', '', '\x00\x00'), '', '', '') == None

