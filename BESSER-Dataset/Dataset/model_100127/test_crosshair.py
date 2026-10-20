from python_code import relationaldatabase_ForeignKey
from python_code import relationaldatabase_Table

def test_relationaldatabase_ForeignKey___init__():
    assert relationaldatabase_ForeignKey.__init__(relationaldatabase_ForeignKey('', '\x00', '', '', relationaldatabase_ForeignKey=relationaldatabase_Table(), relationaldatabase_ForeignKey15=set(), relationaldatabase_ForeignKey18=set(), relationaldatabase_ForeignKey21=relationaldatabase_Table()), '', '', '', '', relationaldatabase_ForeignKey=relationaldatabase_Table(), relationaldatabase_ForeignKey15=set(), relationaldatabase_ForeignKey18=set(), relationaldatabase_ForeignKey21=relationaldatabase_Table()) == None


from python_code import relationaldatabase_NamedElement

def test_relationaldatabase_NamedElement___init__():
    assert relationaldatabase_NamedElement.__init__(relationaldatabase_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import relationaldatabase_DatabaseModel
from python_code import relationaldatabase_Tag
from python_code import relationaldatabase_Taggable

def test_relationaldatabase_Tag___init__():
    assert relationaldatabase_Tag.__init__(relationaldatabase_Tag('', '\x00', relationaldatabase_Tag=relationaldatabase_DatabaseModel(), relationaldatabase_Tag24=relationaldatabase_Taggable()), '\x00\x00', '', relationaldatabase_Tag=relationaldatabase_DatabaseModel(), relationaldatabase_Tag24=relationaldatabase_Taggable()) == None

