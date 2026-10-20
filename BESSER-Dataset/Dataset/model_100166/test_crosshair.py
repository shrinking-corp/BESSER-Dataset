from python_code import properties_DatabaseAlias
from python_code import properties_DatabasePropertiesListType

def test_properties_DatabaseAlias___init__():
    assert properties_DatabaseAlias.__init__(properties_DatabaseAlias('', '\x00', properties_DatabaseAlias=properties_DatabasePropertiesListType()), '\x00\x00', '', properties_DatabaseAlias=properties_DatabasePropertiesListType()) == None


from python_code import properties_DatabaseProperties
from python_code import properties_DatabasePropertiesListType
from python_code import properties_SqlProperties

def test_properties_DatabaseProperties___init__():
    assert properties_DatabaseProperties.__init__(properties_DatabaseProperties('', '', '', '', '', '', '', '', '\x00', '', '', properties_DatabaseProperties=properties_SqlProperties(), properties_DatabaseProperties2=set(), properties_DatabaseProperties4=properties_DatabasePropertiesListType()), '', '', '', '', '', '', '', '', '', '', '', properties_DatabaseProperties=properties_SqlProperties(), properties_DatabaseProperties2=set(), properties_DatabaseProperties4=properties_DatabasePropertiesListType()) == None


from python_code import properties_DocumentRoot

def test_properties_DocumentRoot___init__():
    assert properties_DocumentRoot.__init__(properties_DocumentRoot('\x00', properties_DocumentRoot=set(), properties_DocumentRoot9=set(), properties_DocumentRoot12=set(), properties_DocumentRoot15=set()), '', properties_DocumentRoot=set(), properties_DocumentRoot9=set(), properties_DocumentRoot12=set(), properties_DocumentRoot15=set()) == None


from python_code import properties_Sql

def test_properties_Sql___init__():
    assert properties_Sql.__init__(properties_Sql('\x00\x00', '', properties_Sql=set()), '', '', properties_Sql=set()) == None

