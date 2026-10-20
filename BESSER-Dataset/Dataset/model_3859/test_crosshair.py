from python_code import grammarSql_Column
from python_code import grammarSql_ForeignKey
from python_code import grammarSql_PrimaryKey
from python_code import grammarSql_Reference

def test_grammarSql_Column___init__():
    assert grammarSql_Column.__init__(grammarSql_Column('', '', False, grammarSql_Column=grammarSql_PrimaryKey(), grammarSql_Column5=grammarSql_ForeignKey(), grammarSql_Column13=grammarSql_Reference()), '\x00', '', False, grammarSql_Column=grammarSql_PrimaryKey(), grammarSql_Column5=grammarSql_ForeignKey(), grammarSql_Column13=grammarSql_Reference()) == None


from python_code import grammarSql_Model
from python_code import grammarSql_Reference
from python_code import grammarSql_Table

def test_grammarSql_Table___init__():
    assert grammarSql_Table.__init__(grammarSql_Table('', grammarSql_Table10=grammarSql_Reference(), grammarSql_Table=grammarSql_Model(), grammarSql_Table2=set()), '', grammarSql_Table10=grammarSql_Reference(), grammarSql_Table=grammarSql_Model(), grammarSql_Table2=set()) == None

