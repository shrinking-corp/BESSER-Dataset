from python_code import sql_Column
from python_code import sql_Table

def test_sql_Column___init__():
    assert sql_Column.__init__(sql_Column('', Column=sql_Table(), sql_Column=sql_Table(), sql_Column4=sql_Table(), column=sql_Table()), '', Column=sql_Table(), sql_Column=sql_Table(), sql_Column4=sql_Table(), column=sql_Table()) == None


from python_code import sql_Element

def test_sql_Element___init__():
    assert sql_Element.__init__(sql_Element(''), '') == None

