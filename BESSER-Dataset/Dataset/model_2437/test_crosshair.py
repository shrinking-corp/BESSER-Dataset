from python_code import sql_Column
from python_code import sql_ForeignKey
from python_code import sql_PrimaryKey

def test_sql_Column___init__():
    assert sql_Column.__init__(sql_Column('', '', False, sql_Column13=sql_ForeignKey(), sql_Column=sql_PrimaryKey(), sql_Column7=sql_ForeignKey()), '\x00', '', False, sql_Column13=sql_ForeignKey(), sql_Column=sql_PrimaryKey(), sql_Column7=sql_ForeignKey()) == None


from python_code import sql_Database
from python_code import sql_ForeignKey
from python_code import sql_Table

def test_sql_Table___init__():
    assert sql_Table.__init__(sql_Table('', sql_Table=sql_Database(), sql_Table4=set(), sql_Table10=sql_ForeignKey()), '', sql_Table=sql_Database(), sql_Table4=set(), sql_Table10=sql_ForeignKey()) == None

