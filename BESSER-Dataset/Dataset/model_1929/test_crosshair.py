from python_code import Docbook_ArgType
from python_code import Docbook_CmdsynopsisType

def test_Docbook_ArgType___init__():
    assert Docbook_ArgType.__init__(Docbook_ArgType('', '', '', Docbook_ArgType=set(), Docbook_ArgType4=set(), Docbook_ArgType28=Docbook_CmdsynopsisType()), '', '', '', Docbook_ArgType=set(), Docbook_ArgType4=set(), Docbook_ArgType28=Docbook_CmdsynopsisType()) == None


from python_code import Docbook_AuthorinitialsType
from python_code import Docbook_RevisionType

def test_Docbook_AuthorinitialsType___init__():
    assert Docbook_AuthorinitialsType.__init__(Docbook_AuthorinitialsType('', Docbook_AuthorinitialsType=Docbook_RevisionType()), '', Docbook_AuthorinitialsType=Docbook_RevisionType()) == None


from python_code import Docbook_CmdsynopsisType
from python_code import Docbook_CommandType

def test_Docbook_CommandType___init__():
    assert Docbook_CommandType.__init__(Docbook_CommandType('', Docbook_CommandType=Docbook_CmdsynopsisType()), '', Docbook_CommandType=Docbook_CmdsynopsisType()) == None


from python_code import Docbook_DateType
from python_code import Docbook_RevisionType

def test_Docbook_DateType___init__():
    assert Docbook_DateType.__init__(Docbook_DateType('', Docbook_DateType=Docbook_RevisionType()), '', Docbook_DateType=Docbook_RevisionType()) == None


from python_code import Docbook_FirstnameType
from python_code import Docbook_PersonnameType

def test_Docbook_FirstnameType___init__():
    assert Docbook_FirstnameType.__init__(Docbook_FirstnameType('', Docbook_FirstnameType=Docbook_PersonnameType()), '', Docbook_FirstnameType=Docbook_PersonnameType()) == None


from python_code import Docbook_RevdescriptionType
from python_code import Docbook_RevisionType

def test_Docbook_RevdescriptionType___init__():
    assert Docbook_RevdescriptionType.__init__(Docbook_RevdescriptionType('', Docbook_RevdescriptionType=set(), Docbook_RevdescriptionType331=Docbook_RevisionType()), '', Docbook_RevdescriptionType=set(), Docbook_RevdescriptionType331=Docbook_RevisionType()) == None


from python_code import Docbook_RevisionType
from python_code import Docbook_RevnumberType

def test_Docbook_RevnumberType___init__():
    assert Docbook_RevnumberType.__init__(Docbook_RevnumberType('', Docbook_RevnumberType333=set(), Docbook_RevnumberType=Docbook_RevisionType()), '', Docbook_RevnumberType333=set(), Docbook_RevnumberType=Docbook_RevisionType()) == None


from python_code import Docbook_SegListItemType
from python_code import Docbook_SegType

def test_Docbook_SegType___init__():
    assert Docbook_SegType.__init__(Docbook_SegType('\x00\x00', '', '', '', Docbook_SegType=Docbook_SegListItemType()), '', '', '', '', Docbook_SegType=Docbook_SegListItemType()) == None


from python_code import Docbook_PersonnameType
from python_code import Docbook_SurnameType

def test_Docbook_SurnameType___init__():
    assert Docbook_SurnameType.__init__(Docbook_SurnameType('', Docbook_SurnameType=Docbook_PersonnameType()), '', Docbook_SurnameType=Docbook_PersonnameType()) == None


from python_code import Docbook_ListitemType
from python_code import Docbook_VarListEntryType
from python_code import Docbook_VariableListType

def test_Docbook_VarListEntryType___init__():
    assert Docbook_VarListEntryType.__init__(Docbook_VarListEntryType('', '', Docbook_VarListEntryType=Docbook_VariableListType(), Docbook_VarListEntryType440=set(), Docbook_VarListEntryType443=Docbook_ListitemType()), '', '', Docbook_VarListEntryType=Docbook_VariableListType(), Docbook_VarListEntryType440=set(), Docbook_VarListEntryType443=Docbook_ListitemType()) == None

