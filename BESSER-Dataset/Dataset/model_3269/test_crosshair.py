from python_code import ISO20022_AbstractTimeConcept

def test_ISO20022_AbstractTimeConcept___init__():
    assert ISO20022_AbstractTimeConcept.__init__(ISO20022_AbstractTimeConcept('', '', '', '', ''), '', '', '', '', '') == None


from python_code import ISO20022_BusinessProcessCatalogue
from python_code import ISO20022_Repository
from python_code import ISO20022_TopLevelCatalogueEntry

def test_ISO20022_BusinessProcessCatalogue___init__():
    assert ISO20022_BusinessProcessCatalogue.__init__(ISO20022_BusinessProcessCatalogue(businessProcessCatalogue56=ISO20022_Repository(), BusinessProcessCatalogue59=ISO20022_TopLevelCatalogueEntry(), BusinessProcessCatalogue=ISO20022_Repository(), businessProcessCatalogue=set()), businessProcessCatalogue56=ISO20022_Repository(), BusinessProcessCatalogue59=ISO20022_TopLevelCatalogueEntry(), BusinessProcessCatalogue=ISO20022_Repository(), businessProcessCatalogue=set()) == None

def test_ISO20022_BusinessProcessCatalogue_EntriesHaveUniqueName():
    assert ISO20022_BusinessProcessCatalogue.EntriesHaveUniqueName(ISO20022_BusinessProcessCatalogue(businessProcessCatalogue56=ISO20022_Repository(), BusinessProcessCatalogue59=ISO20022_TopLevelCatalogueEntry(), BusinessProcessCatalogue=ISO20022_Repository(), businessProcessCatalogue=set()), 0, '\x00\x00') == None


from python_code import ISO20022_ChoiceComponent

def test_ISO20022_ChoiceComponent___init__():
    assert ISO20022_ChoiceComponent.__init__(ISO20022_ChoiceComponent()) == None

def test_ISO20022_ChoiceComponent_AtLeastOneProperty():
    assert ISO20022_ChoiceComponent.AtLeastOneProperty(ISO20022_ChoiceComponent(), '', '') == None


from python_code import ISO20022_DataDictionary
from python_code import ISO20022_Repository
from python_code import ISO20022_TopLevelDictionaryEntry

def test_ISO20022_DataDictionary___init__():
    assert ISO20022_DataDictionary.__init__(ISO20022_DataDictionary(dataDictionary=ISO20022_Repository(), dataDictionary47=set(), DataDictionary53=ISO20022_Repository(), DataDictionary=ISO20022_TopLevelDictionaryEntry()), dataDictionary=ISO20022_Repository(), dataDictionary47=set(), DataDictionary53=ISO20022_Repository(), DataDictionary=ISO20022_TopLevelDictionaryEntry()) == None

def test_ISO20022_DataDictionary_EntriesHaveUniqueName():
    assert ISO20022_DataDictionary.EntriesHaveUniqueName(ISO20022_DataDictionary(dataDictionary=ISO20022_Repository(), dataDictionary47=set(), DataDictionary53=ISO20022_Repository(), DataDictionary=ISO20022_TopLevelDictionaryEntry()), 0, '\x00\x00') == None


from python_code import ISO20022_ExternalSchema

def test_ISO20022_ExternalSchema___init__():
    assert ISO20022_ExternalSchema.__init__(ISO20022_ExternalSchema('', '\x00'), '\x00\x00', '') == None


from python_code import ISO20022_DataType
from python_code import ISO20022_Facet

def test_ISO20022_Facet___init__():
    assert ISO20022_Facet.__init__(ISO20022_Facet('', '\x00', ISO20022_Facet=ISO20022_DataType()), '\x00\x00', '', ISO20022_Facet=ISO20022_DataType()) == None


from python_code import ISO20022_Amount
from python_code import ISO20022_IdentifierSet

def test_ISO20022_IdentifierSet___init__():
    assert ISO20022_IdentifierSet.__init__(ISO20022_IdentifierSet('', ISO20022_IdentifierSet=ISO20022_Amount()), '', ISO20022_IdentifierSet=ISO20022_Amount()) == None


from python_code import ISO20022_Indicator

def test_ISO20022_Indicator___init__():
    assert ISO20022_Indicator.__init__(ISO20022_Indicator('', '', '\x00\x00'), '', '', '') == None


from python_code import ISO20022_MultiplicityEntity

def test_ISO20022_MultiplicityEntity___init__():
    assert ISO20022_MultiplicityEntity.__init__(ISO20022_MultiplicityEntity('', '\x00'), '\x00\x00', '') == None


from python_code import ISO20022_Quantity

def test_ISO20022_Quantity___init__():
    assert ISO20022_Quantity.__init__(ISO20022_Quantity(''), '') == None


from python_code import ISO20022_Rate

def test_ISO20022_Rate___init__():
    assert ISO20022_Rate.__init__(ISO20022_Rate('', '\x00'), '\x00\x00', '') == None


from python_code import ISO20022_SWIFTSolution

def test_ISO20022_SWIFTSolution___init__():
    assert ISO20022_SWIFTSolution.__init__(ISO20022_SWIFTSolution(''), '') == None


from python_code import ISO20022_UserDefined

def test_ISO20022_UserDefined___init__():
    assert ISO20022_UserDefined.__init__(ISO20022_UserDefined('', '', '\x00\x00'), '', '', '') == None


from python_code import ISO20022_LogicalType
from python_code import ISO20022_XMLMember

def test_ISO20022_XMLMember___init__():
    assert ISO20022_XMLMember.__init__(ISO20022_XMLMember('', typedXMLMember=ISO20022_LogicalType(), XMLMember=ISO20022_LogicalType()), '', typedXMLMember=ISO20022_LogicalType(), XMLMember=ISO20022_LogicalType()) == None


from python_code import ISO20022_XSDBinary

def test_ISO20022_XSDBinary___init__():
    assert ISO20022_XSDBinary.__init__(ISO20022_XSDBinary('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ISO20022_XSDDecimal

def test_ISO20022_XSDDecimal___init__():
    assert ISO20022_XSDDecimal.__init__(ISO20022_XSDDecimal('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import ISO20022_XSDString

def test_ISO20022_XSDString___init__():
    assert ISO20022_XSDString.__init__(ISO20022_XSDString('\x00\x00', '', '', ''), '', '', '', '') == None

