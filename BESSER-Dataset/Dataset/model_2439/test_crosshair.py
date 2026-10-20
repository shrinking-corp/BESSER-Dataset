from python_code import Sql_Column
from python_code import Sql_Table

def test_Sql_Column___init__():
    assert Sql_Column.__init__(Sql_Column('', Sql_Column=Sql_Table()), '', Sql_Column=Sql_Table()) == None


from python_code import Sql_NamedElement

def test_Sql_NamedElement___init__():
    assert Sql_NamedElement.__init__(Sql_NamedElement(''), '') == None

