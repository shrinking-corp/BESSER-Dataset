from python_code import database_Database

def test_database_Database___init__():
    assert database_Database.__init__(database_Database('', database_Database=set(), database_Database13=set()), '', database_Database=set(), database_Database13=set()) == None


from python_code import database_FKey
from python_code import database_RefTable

def test_database_FKey___init__():
    assert database_FKey.__init__(database_FKey('', database_FKey=set(), database_FKey7=database_RefTable()), '', database_FKey=set(), database_FKey7=database_RefTable()) == None


from python_code import database_PKey

def test_database_PKey___init__():
    assert database_PKey.__init__(database_PKey('', database_PKey=set()), '', database_PKey=set()) == None


from python_code import database_Parameter
from python_code import database_RefType

def test_database_Parameter___init__():
    assert database_Parameter.__init__(database_Parameter('', database_Parameter=database_RefType()), '', database_Parameter=database_RefType()) == None


from python_code import database_Procedure
from python_code import database_RefType

def test_database_Procedure___init__():
    assert database_Procedure.__init__(database_Procedure('', database_Procedure=set(), database_Procedure16=database_RefType()), '', database_Procedure=set(), database_Procedure16=database_RefType()) == None


from python_code import database_Table

def test_database_Table___init__():
    assert database_Table.__init__(database_Table('', database_Table=set(), database_Table2=set(), database_Table4=set()), '', database_Table=set(), database_Table2=set(), database_Table4=set()) == None


from python_code import database_Type

def test_database_Type___init__():
    assert database_Type.__init__(database_Type(''), '') == None

