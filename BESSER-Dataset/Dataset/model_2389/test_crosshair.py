from python_code import database_Column
from python_code import database_ForeignKey
from python_code import database_Table

def test_database_Column___init__():
    assert database_Column.__init__(database_Column('', database_Column=database_Table(), database_Column5=database_Table(), database_Column10=database_ForeignKey()), '', database_Column=database_Table(), database_Column5=database_Table(), database_Column10=database_ForeignKey()) == None


from python_code import database_DataBaseElement

def test_database_DataBaseElement___init__():
    assert database_DataBaseElement.__init__(database_DataBaseElement(''), '') == None

