from python_code import genSql_DataBase
from python_code import genSql_ForeignKey
from python_code import genSql_PrimaryKey
from python_code import genSql_Table

def test_genSql_Table___init__():
    assert genSql_Table.__init__(genSql_Table('', genSql_Table4=genSql_PrimaryKey(), genSql_Table6=set(), genSql_Table=genSql_DataBase(), genSql_Table2=set(), genSql_Table15=genSql_ForeignKey()), '', genSql_Table4=genSql_PrimaryKey(), genSql_Table6=set(), genSql_Table=genSql_DataBase(), genSql_Table2=set(), genSql_Table15=genSql_ForeignKey()) == None

